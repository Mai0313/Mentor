import os
from typing import Any, Literal, Optional
from pathlib import Path
import datetime

import logfire

logfire.configure(send_to_logfire=False)

import warnings

import httpx
from openai import AzureOpenAI, AsyncAzureOpenAI
import autogen
from autogen import ChatResult, UserProxyAgent, config_list_from_json
import chromadb
from pydantic import Field, BaseModel, computed_field, model_validator
from markitdown import MarkItDown
from pydantic_ai import Agent
from rich.console import Console
from autogen.cache import Cache
from rich.markdown import Markdown
from chromadb.config import Settings
from autogen.code_utils import extract_code
from pydantic_ai.models.openai import OpenAIModel
from openai.types.completion_usage import CompletionUsage
from openai.types.chat.chat_completion import Choice, ChatCompletion
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from autogen.agentchat.contrib.captainagent.captainagent import CaptainAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from chromadb.utils.embedding_functions.openai_embedding_function import OpenAIEmbeddingFunction

console = Console()
warnings.filterwarnings("ignore", category=ResourceWarning)

MAX_ROUND = 12

def get_config_dict(model: str) -> dict[str, Any]:
    config_list = config_list_from_json(
        env_or_file="./configs/OAI_CONFIG_LIST", filter_dict={"model": model}
    )
    llm_config = {
        "timeout": 60,
        "temperature": 0.5,
        "cache_seed": os.getenv("SEED", None),
        "config_list": config_list,
    }
    return llm_config


def retrieve_data(query: str) -> str:
    """This tool is for retrieving knowledge from the docs.

    If you have any question, you can give a query keyword then this function will search the answer in the docs and return the answer.

    Args:
        query (str): The question you want to ask and search in the docs.

    Returns:
        str: The answer to the question.

    Examples:
        >>> query = "What is the Product Version of Bandgap Reference Verification"
        >>> retrieved_result = retrieve_data(query=query)
    """
    docs_path = Path("./docs").glob("**/*.*")
    subcircuit_lib = Path("./subcircuit_lib").glob("**/*.*")
    all_docs = [*docs_path, *subcircuit_lib]
    all_docs = [f.as_posix() for f in all_docs]
    llm_config = get_config_dict(model="aide-gpt-4o")
    rag_agent = autogen.AssistantAgent(
        name="RetrievalAgent",
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
        llm_config=llm_config,
        silent=True,
    )
    rag_user_proxy = RetrieveUserProxyAgent(
        name="RetrieveAgent",
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
        default_auto_reply="Reply `TERMINATE` if the task is done.",
        max_consecutive_auto_reply=3,
        retrieve_config={
            "task": "default",
            "docs_path": all_docs,
            "must_break_at_empty_line": False,
            "model": "gpt-4",
            "vector_db": None,
            "client": chromadb.Client(Settings(anonymized_telemetry=False)),
            "get_or_create": True,
            "update_context": False,
            "embedding_function": OpenAIEmbeddingFunction(
                api_key=llm_config["config_list"][0]["api_key"],
                api_base="http://mlop-azure-gateway.mediatek.inc",
                api_type=llm_config["config_list"][0]["api_type"],
                api_version=llm_config["config_list"][0]["api_version"],
                model_name="aide-text-embedding-ada-002-v2",
                default_headers=llm_config["config_list"][0]["default_headers"],
            ),
            "embedding_model": None,
        },
        code_execution_config=False,  # we don't want to execute code in this case.
        description="Assistant who has extra content retrieval power for solving difficult problems.",
        silent=True,
    )
    groupchat = autogen.GroupChat(
        agents=[rag_user_proxy, rag_agent],
        messages=[],
        max_round=12,
        speaker_selection_method="round_robin",
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config, silent=True)
    retrieve_result = rag_user_proxy.initiate_chat(
        recipient=manager,
        message=rag_user_proxy.message_generator,
        problem=query,
        # 這個會決定 LLM 能參考多少文件，要讓她拿到正確資訊，就要全部允許他看
        n_results=len(all_docs),
        # summary_method="last_msg",
        silent=True,
    )
    return retrieve_result.chat_history[-1]["content"]


def read_prompt(filepath: str) -> str:
    path = Path(filepath)
    content = path.read_text()
    return content


def convert2markdown(path: str) -> list[dict[str, str]]:
    """Convert the docs to markdown format.

    Args:
        path (str): The path of the docs you want to convert, it can be either a file or a directory.

    Returns:
        list[dict[str, str]]: The list of the markdown content.
    """
    all_docs_paths = list(Path(path).glob("**/*.*")) if Path(path).is_dir() else [Path(path)]
    client = AzureOpenAI(
        api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBSURFIiwic3ViIjoiQUlERV9HQUlTRiIsImF1ZCI6WyJBSURFIl0sImlhdCI6MTY3ODg0NjkwNiwianRpIjoiZjdiYWVmMDItNzljYy00YTY3LTg5MWItYWIxOWM2MjBkY2MxIn0.0Sfk0QgU5RntmaIM0ALrOuk109dvQQttaigot8TPZZc",
        azure_endpoint="https://mlop-azure-gateway.mediatek.inc",
        api_version="2024-08-01-preview",
        http_client=httpx.Client(verify=False, headers={"X-User-Id": "srv_dvc_tma001"}),
    )
    md = MarkItDown(llm_client=client, llm_model="aide-gpt-4o")
    markdown_docs: list[dict[str, str]] = []
    for all_docs_path in all_docs_paths:
        result = md.convert(source=all_docs_path)
        if result and result.title is None:
            result.title = all_docs_path.stem
        markdown_docs.append({
            "filepath": all_docs_path.absolute().as_posix(),
            "title": result.title,
            "content": result.text_content,
        })
    return markdown_docs


class AutogenUsage(BaseModel):
    cost: Optional[float] = Field(default=0.0, title="Cost of the API call")
    prompt_tokens: Optional[int] = Field(default=0, title="Number of tokens in the prompt")
    completion_tokens: Optional[int] = Field(default=0, title="Number of tokens in the completion")
    total_tokens: Optional[int] = Field(
        default=0, title="Total number of tokens in the prompt and completion"
    )


class ChatResultConverter(BaseModel):
    chat_result: ChatResult = Field(
        ...,
        title="Chat Result from Autogen",
        description="The chat result from autogen groupchat or initiate_chat.",
        frozen=False,
        deprecated=False,
    )
    chat_result_override: str | None = Field(
        default=None,
        title="Chat Result Override",
        description="The real result from the groupchat or captain agent may not contain within the chat_result, so you can override the chat_result with this field by retrieving the messages from the assistant within the groups.",
        frozen=False,
        deprecated=False,
    )
    usage_data_override: dict[str, Any] | None = Field(
        default=None,
        title="Usage Data Override",
        description="The usage data may not contain within the chat_result, so you can override the usage data with this field.",
        frozen=False,
        deprecated=False,
    )
    revert: bool = Field(
        default=True,
        title="Revert the Chat History",
        description="Reverse the chat history, default is True because Analog Coder is using the first message as the result.",
        frozen=True,
        deprecated=False,
    )

    @model_validator(mode="after")
    def _setup(self) -> "ChatResultConverter":
        # HACK: 最後一句話不知道為何有可能是 empty string, 所以用 summary 直接取代以提升兼容性
        # if not self.chat_result.chat_history[-1]["content"]:
        #     self.chat_result.chat_history[-1]["content"] = self.chat_result.summary

        # NOTE: 把對話紀錄翻轉，因為Analog Coder是取第一個當作結果
        if self.revert is True:
            self.chat_result.chat_history = self.chat_result.chat_history[::-1]
        history_alike_summary = [
            {"content": self.chat_result.summary, "role": "assistant", "name": "manual_summary"}
        ]
        # 讓 summary 出現在第一個
        history_alike_summary.extend(self.chat_result.chat_history)
        self.chat_result.chat_history = history_alike_summary
        # console.print("+=" * 20, "Chat History Start", "+=" * 20)
        # console.print(f"{self.chat_result.chat_history}")
        # console.print("+=" * 20, "Chat History End", "+=" * 20)
        return self

    @computed_field
    @property
    def usage(self) -> CompletionUsage:
        usage_data = AutogenUsage()

        if self.usage_data_override:
            for value in self.usage_data_override.values():
                if isinstance(value, dict):
                    usage_data = AutogenUsage(**value)
        else:
            cost_dict = self.chat_result.cost.get("usage_including_cached_inference")
            if cost_dict:
                for value in cost_dict.values():
                    if isinstance(value, dict):
                        usage_data = AutogenUsage(**value)

        usage = CompletionUsage(
            completion_tokens=usage_data.completion_tokens,
            prompt_tokens=usage_data.prompt_tokens,
            total_tokens=usage_data.total_tokens,
        )
        return usage

    @computed_field
    @property
    def model(self) -> str:
        cost_dict = self.chat_result.cost["usage_including_cached_inference"]
        if cost_dict:
            for key in cost_dict:
                if key != "total_cost":
                    return key
        return "gpt-4o"

    @computed_field
    @property
    def choices(self) -> list[Choice]:
        choices = []
        if self.chat_result_override:
            pass
        else:
            for idx, chat_dict in enumerate(self.chat_result.chat_history, start=1):
                chat_dict["role"] = "assistant"
                message = ChatCompletionMessage(**chat_dict)
                choice = Choice(finish_reason="stop", index=idx, message=message)
                choices.append(choice)
        return choices

    def convert_to_chat_completion(self) -> ChatCompletion:
        chat_completion_result = ChatCompletion(
            id="1",
            choices=self.choices,
            created=int(datetime.datetime.now().timestamp()),
            model=self.model,
            object="chat.completion",
            usage=self.usage,
        )
        return chat_completion_result


class CodeBlock(BaseModel):
    code_type: str = Field(
        ...,
        title="Code Type of the Code Block",
        description="This field will contain the code type of the block, e.g. python, json, etc.",
        frozen=True,
        deprecated=False,
    )
    code_content: str = Field(
        ...,
        title="Code Content of the Code Block",
        description="This field will contain the pure code content of the block without any ``` or code type.",
        frozen=True,
        deprecated=False,
    )

    @computed_field
    @property
    def code_in_markdown(self) -> str:
        return f"```{self.code_type}\n{self.code_content}\n```"


class AnalogAgent(BaseModel):
    use_docker: Literal["mtkomcr.mediatek.inc/srv-aith/mtkllm-sdk-analog", False] = Field(
        default=False,
        title="Use Docker or Not",
        description="Use Docker or Not, if you wanna use, please provide the docker image name.",
        examples=["mtkomcr.mediatek.inc/srv-aith/mtkllm-sdk-analog", False],
    )

    @staticmethod
    def _summary_method(
        sender: autogen.ConversableAgent,
        recipient: CaptainAgent | autogen.ConversableAgent,
        summary_args: dict[str, Any],
    ) -> str:
        sender_messages = list(sender.chat_messages.values())[-1]
        recipient_messages = list(recipient.chat_messages.values())[-1]
        messages = [*sender_messages, *recipient_messages]
        if isinstance(recipient, CaptainAgent):
            executor_messages = list(recipient.executor.chat_messages.values())[-1]
            assistant_messages = list(recipient.assistant.chat_messages.values())[-1]
            messages.extend([*executor_messages, *assistant_messages])

        message_with_codes: list[CodeBlock] = []
        # for messages_list in messages:
        #     for message in messages_list:
        #         message_content = message.get("content")
        #         if message_content is None:
        #             continue
        #         code_messages = extract_code(text=message_content)
        #         all_code_found = []
        #         for code_type, code_content in code_messages:
        #             if code_type == "python":
        #                 all_code_found.append(
        #                     CodeBlock(code_type=code_type, code_content=code_content)
        #                 )
        #         if all_code_found:
        #             message_with_codes.append(all_code_found[-1])
        if message_with_codes:
            message_with_code = message_with_codes[-1]
            last_message = message_with_code.code_in_markdown
            console.print(
                f"Code Block Found from the last message in type {message_with_code.code_type}, replacing the summary using the following code block:",
                style="bold green",
            )
            console.print(Markdown(message_with_code.code_in_markdown))
        else:
            llm_config = get_config_dict(model="aide-gpt-4o")
            client = AsyncAzureOpenAI(
                api_key=llm_config["config_list"][0]["api_key"],
                azure_endpoint=llm_config["config_list"][0]["base_url"],
                api_version=llm_config["config_list"][0]["api_version"],
                http_client=httpx.AsyncClient(
                    headers=llm_config["config_list"][0]["default_headers"]
                ),
            )
            model = OpenAIModel(model_name="aide-gpt-4o", openai_client=client)
            agent = Agent(model=model, result_type=CodeBlock)
            response = agent.run_sync(
                user_prompt=f"{messages}\nPlease extract the final result code block from the content. The output should be a python code block only."
            )
            if response.data:
                last_message = response.data.code_in_markdown
                console.print(
                    f"Code Block Found by LLM from the last message in type {response.data.code_type}, replacing the summary using the following code block:",
                    style="bold yellow",
                )
                console.print(Markdown(response.data.code_in_markdown))
            else:
                last_message = recipient.last_message(sender)["content"]
                console.print(
                    "Failed to extract the code block by either LLM or manually, using the last message.",
                    style="bold red",
                )
        return last_message

    def _get_cache(self, llm_config: dict[str, Any]) -> Cache:
        cache = None
        cache_seed = llm_config.get("cache_seed")
        if cache_seed:
            cache = Cache.disk(cache_seed=cache_seed, cache_path_root="./.cache")
        return cache

    def read_prompt(self, filepath: str) -> str:
        path = Path(filepath)
        content = path.read_text()
        return content

    def use_chat_completion(self, model: str, messages: list[dict[str, str]]) -> ChatCompletion:
        llm_config = get_config_dict(model=model)
        client = AzureOpenAI(
            api_key=llm_config["config_list"][0]["api_key"],
            azure_endpoint=llm_config["config_list"][0]["base_url"],
            api_version=llm_config["config_list"][0]["api_version"],
            http_client=httpx.Client(headers=llm_config["config_list"][0]["default_headers"]),
        )
        result = client.chat.completions.create(
            messages=messages, model=model, temperature=llm_config["temperature"]
        )
        return result

    def use_groupchat(
        self, model: str, messages: list[dict[str, str]], work_dir: str, use_rag: bool
    ) -> ChatCompletion:
        llm_config = get_config_dict(model=model)
        self._get_cache(llm_config=llm_config)
        pi_agent = autogen.ConversableAgent(
            name="PIAgent",
            description="PI Agent is a senior engineer who takes the problem specification and then breakdown the necessary steps to do.",
            system_message="""You are an experience manager focusing on RF/Analog circuit design, can you help me design a circuit with the following spec?
            - Design a circuit with the Spec you received.
            - What could be the name of this circuit?
            - What relevant documents you have to guide a designer to design this circuit?
            The output should be:
            Find corresponding papers or RAK files from dataset or online search
            Key idea: Find required documents for RF engineers
            RAK: Rapid Adoption Kits
            """,
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=MAX_ROUND,
            human_input_mode="NEVER",
            code_execution_config=False,
            llm_config=llm_config,
        )
        pi_agent.register_hook("process_last_received_message", lambda content: f"{content}\n\nPlease help me design the mentioned circuit. Think and tell me the necessary steps.\nLet's think step by step.")
        executor = autogen.UserProxyAgent(
            name="executor",
            human_input_mode="NEVER",
            is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
            code_execution_config={"use_docker": self.use_docker, "work_dir": work_dir},
        )
        circuit_agent = autogen.AssistantAgent(
            name="CircuitAgent",
            description="Circuit Agent is a junior engineer who helps the PI Agent to design the circuit.",
            system_message="""
            Example Prompt: You are an experienced [circuit name] designers, please use the [docs name], and help me design a [circuit name]. It needs to follow the spec as below: xxxxxxxxx.
            Please output the PySpice code of this circuit.
            You have access to an [offline library name].
            If you find subcircuits that already be built, you can ask the corresponding agent using [xxx].
            If you find any problems when you are designing the circuit, please contact PI for further classification.
            The output should be:
            Circuit PySpice code
            """,
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=MAX_ROUND,
            human_input_mode="NEVER",
            code_execution_config=False,
            llm_config=llm_config,
        )
        testbench_agent = autogen.AssistantAgent(
            name="TestbenchAgent",
            description="Testbench Agent is a junior engineer who helps the PI Agent to design the testbench. It specialize at writing and debuggin testbench written in PySpice.",
            system_message="""
            Example prompt: You are an experience RF/Analog circuit validation engineer.
            You are required to validate a circuit based on given PySpice code.
            You must append PySpice code to simulate the circuit and validate if it satisfy the spec.
            Please call the executor to run the testbench.
            There might be attached files, such as relevant papers for the circuit.
            If it's correct, output the final circuit in PySpice.
            If not, output the error messages back to the circuit agent. And rerun the process, implementation limit+1.

            - NOTE: Output "TERMINATE" in the last line if you think the analog circuit design task has beed finished. That is, the PySpice codes are written, you have checked the implementation, and the executor has executed the PySpice testbench code successfully.
            """,
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=MAX_ROUND,
            human_input_mode="NEVER",
            code_execution_config=False,
            llm_config=llm_config,
        )
        # cos_agent = autogen.AssistantAgent(
        #     name="assistant",
        #     description="COS Agent is a junior engineer who helps the PI Agent to design the COS.",
        #     system_message="Please help me design a circuit. Think and tell me the necessary steps we need to do.",
        #     human_input_mode="NEVER",
        #     llm_config=llm_config,
        #     is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
        # )
        # math_reasoning_agent = autogen.AssistantAgent(
        #     name="assistant",
        #     human_input_mode="NEVER",
        #     llm_config=llm_config,
        #     is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
        # )
        # graph_analysis_agent = autogen.AssistantAgent(
        #     name="assistant",
        #     human_input_mode="NEVER",
        #     llm_config=llm_config,
        #     is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
        # )
        proxies = [pi_agent]
        agents = [circuit_agent, testbench_agent]
        if use_rag is True:
            # autogen.agentchat.register_function(
            #     f=retrieve_data,
            #     caller=pi_agent,
            #     executor=executor,
            #     name=retrieve_data.__name__,
            #     description=retrieve_data.__doc__,
            # )
            for agent in agents:
                d_retrieve_content = agent.register_for_llm(
                    description="retrieve the information you need or if you have any question, you can use this function to get the answer.",
                    api_style="tool",
                )(retrieve_data)

            for proxy in proxies:
                proxy.register_for_execution()(d_retrieve_content)
        groupchat = autogen.GroupChat(
            agents=[*proxies, executor, *agents],
            messages=[],
            max_round=MAX_ROUND,
            speaker_selection_method="auto",
            allow_repeat_speaker=False,
        )
        manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

        # Start chatting with boss_aid as this is the user proxy agent.
        chat_result = pi_agent.initiate_chat(
            recipient=manager,
            message=f"{messages}, the final answer must contain a PySpice Code in Python.",
            summary_method=self._summary_method,
        )
        converter = ChatResultConverter(chat_result=chat_result)
        result = converter.convert_to_chat_completion()
        return result

    def use_captain(
        self, model: str, messages: list[dict[str, str]], work_dir: str, use_rag: bool
    ) -> ChatCompletion:
        """A Captain Agent by using autogen.

        [ref](https://docs.ag2.ai/docs/use-cases/notebooks/notebooks/agentchat_captainagent).

        Args:
            model (str): The model name you want to use.
            messages (list[dict[str, str]]): The messages you want to chat with the Captain Agent.
            work_dir (str): The working directory you want to use.
            use_rag (bool): If you want to use the Retrieve Agent, set it to True.

        Returns:
            ChatCompletion: The chat result from the Captain Agent.
        """
        llm_config = get_config_dict(model=model)
        cache = self._get_cache(llm_config=llm_config)
        nested_config = {
            "autobuild_init_config": {
                "config_file_or_env": "./configs/OAI_CONFIG_LIST",
                "builder_model": model,  # "aide-o3-mini",
                "agent_model": model,
                "max_agents": 10,
            },
            "autobuild_build_config": {
                "default_llm_config": {
                    "temperature": llm_config["temperature"],
                    "top_p": 0.95,
                    "max_tokens": 2048,
                    "cache_seed": llm_config.get("cache_seed"),
                },
                "code_execution_config": {
                    "timeout": 300,
                    "work_dir": work_dir,
                    "last_n_messages": 1,
                    "use_docker": self.use_docker,
                },
                "coding": True,
                "library_path_or_json": None,
            },
            # "autobuild_tool_config": {
            #     "tool_root": "tools",
            #     "retriever": "all-mpnet-base-v2"
            # },
            "group_chat_config": {"max_round": 30},
            "group_chat_llm_config": None,
            "max_turns": 10,
        }

        captain_user_proxy = UserProxyAgent(
            name="captain_user_proxy",
            # llm_config=llm_config,
            human_input_mode="NEVER",
            code_execution_config=False,
            # system_message="Make sure the final answer contains the PySpice Code.",
        )
        captain_agent = CaptainAgent(
            name="captain_agent",
            llm_config=llm_config,
            code_execution_config={
                "timeout": 300,
                "work_dir": work_dir,
                "last_n_messages": 1,
                "use_docker": self.use_docker,
            },
            agent_config_save_path=Path(work_dir).parent.absolute().as_posix(),
            nested_config=nested_config,
            # tool_lib="./tools",
            # is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
        )
        # tools = [convert2markdown]
        # for tool in tools:
        #     captain_agent.register_for_execution(
        #         name=tool.__name__,  # Function name
        #         description=tool.__doc__,  # Function description, you need to annotated it with `"""`
        #     )(tool)
        if use_rag:
            messages.append({"role": "user", "content": "All Docs is in ./docs"})
        chat_result = captain_user_proxy.initiate_chat(
            captain_agent,
            message=f"{messages}\nPlease just seek_experts_help\nMake sure the code should not have singular matrix issue.",
            max_turns=1,
            summary_method=self._summary_method,
            cache=cache,
        )
        # console.print(captain_agent.executor.build_history)
        captain_agent.assistant.print_usage_summary(mode="total")
        usage_data_override = captain_agent.assistant.get_total_usage()
        converter = ChatResultConverter(
            chat_result=chat_result, usage_data_override=usage_data_override
        )
        result = converter.convert_to_chat_completion()
        return result


def get_chat_completion(
    model: str,
    messages: list[dict[str, str]],
    mode: Literal["original", "captain", "captain+rag", "groupchat", "groupchat+rag"],
    work_dir: str,
    use_docker: Literal["mtkomcr.mediatek.inc/srv-aith/mtkllm-sdk-analog", False] = False,
) -> ChatCompletion:
    cache_path = Path("./.cache")
    cache_path.mkdir(parents=True, exist_ok=True)
    analog_agent = AnalogAgent(use_docker=use_docker)
    if mode == "original":
        chat_result = analog_agent.use_chat_completion(model=model, messages=messages)
    elif "captain" in mode:
        use_rag = False
        if "rag" in mode:
            use_rag = True
        chat_result = analog_agent.use_captain(
            model=model, messages=messages, work_dir=work_dir, use_rag=use_rag
        )
    elif "groupchat" in mode:
        use_rag = False
        if "rag" in mode:
            use_rag = True
        chat_result = analog_agent.use_groupchat(
            model=model, messages=messages, work_dir=work_dir, use_rag=use_rag
        )
    else:
        raise ValueError(f"Invalid mode: {mode}")
    return chat_result


if __name__ == "__main__":
    model = "aide-gpt-4o"
    messages = [
        # {
        #     "role": "user",
        #     "content": "Give me a python code that can print a random dataframe; the output should be a python code.",
        # },
        {"role": "user", "content": "Find me the author of `Bandgap Reference Verification_RAK`."}
    ]
    chat_result = get_chat_completion(model=model, messages=messages, mode="captain")
    console.print(chat_result)
