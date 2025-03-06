import os
from typing import Any, Literal, Optional
from pathlib import Path
import datetime

import logfire

logfire.configure(send_to_logfire=False)

import warnings

import httpx
import hydra
from openai import AzureOpenAI, AsyncAzureOpenAI
import autogen
from autogen import ChatResult, UserProxyAgent, config_list_from_json
import chromadb
from pydantic import Field, BaseModel, computed_field, model_validator
from omegaconf import OmegaConf
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


def is_termination_msg(msg: dict[str, str]) -> bool:
    return "TERMINATE" in msg["content"]


dc_sweep_template = """
import numpy as np
import os
analysis = simulator.dc(V[IN_NAME]=slice(0, 5, 0.01))
file_path = "dc_sweep.txt"
with open("file_path", "w") as fopen:
    out_voltage = np.array(analysis.Vout)
    in_voltage = np.array(analysis.V[IN_NAME])
    print("out_voltage: ", out_voltage)
    print("in_voltage: ", in_voltage)
    for item in in_voltage:
        fopen.write(f"{item:.4f} ")
    fopen.write("\\n")
    for item in out_voltage:
        fopen.write(f"{item:.4f} ")
    fopen.write("\\n")
"""

pyspice_template = """
try:
    analysis = simulator.operating_point()
    with open("[OP_PATH]", "w") as fopen:
        for node in analysis.nodes.values():
            fopen.write(f"{str(node)}\\t{float(analysis[str(node)][0]):.6f}\\n")
except Exception as e:
    print("Analysis failed due to an error:")
    print(str(e))
"""

output_netlist_template = """
source = str(circuit)
print(source)
"""

best_voltage_template = """
with open("dc_sweep.txt") as fopen:
    vin = np.array([float(x) for x in fopen.readline().strip().split(" ")])
    vout = np.array([float(x) for x in fopen.readline().strip().split(" ")])
    if np.max(vout) - np.min(vout) < 1e-3:
        return "failed to find best voltage", 0
    min_margin = 10.0
    for i, v in enumerate(vout):
        if np.abs(v - 2.5) < min_margin:
            min_margin = np.abs(v - 2.5)
            best_voltage = vin[i]
    return "success to find best voltage", best_voltage
"""


class MessageModel(BaseModel):
    role: str = Field(
        default="",
        title="Role of the Message",
        description="Role of the Message, if model is o1, it should not be `system`.",
        frozen=False,
        deprecated=False,
    )
    content: str = Field(
        default="",
        title="Content of the Message",
        description="Content of the Message",
        frozen=False,
        deprecated=False,
    )


def get_config_dict(model: str, temp: float = 0.5) -> dict[str, Any]:
    config_list = config_list_from_json(
        env_or_file="./configs/llm/OAI_CONFIG_LIST", filter_dict={"model": model}
    )
    llm_config = {"timeout": 60, "cache_seed": os.getenv("SEED", None), "config_list": config_list}
    if "o1" not in model:
        llm_config["temperature"] = temp
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
    docs_path = Path("./docs").glob("**/*.md")
    subcircuit_lib = Path("./subcircuit_lib").glob("**/*.*")
    all_docs = [*docs_path, *subcircuit_lib]
    all_docs = [f.as_posix() for f in all_docs]
    llm_config = get_config_dict(model="aide-gpt-4o")
    rag_assistant = autogen.AssistantAgent(
        name="RetrieveAssistant", llm_config=llm_config, silent=True
    )
    rag_proxy_agent = RetrieveUserProxyAgent(
        name="RetrieveProxyAgent",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,
        retrieve_config={
            "task": "default",
            "docs_path": all_docs,
            "must_break_at_empty_line": False,
            "model": "gpt-4o",
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
        silent=True,
    )
    chat_result = rag_proxy_agent.initiate_chat(
        recipient=rag_assistant,
        message=rag_proxy_agent.message_generator,
        problem=query,
        # 這個會決定 LLM 能參考多少文件，要讓她拿到正確資訊，就要全部允許他看
        n_results=len(all_docs),
        # summary_method="last_msg",
    )
    return chat_result.chat_history[-1]["content"]


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

    def convert_init_message(self, messages: list[dict[str, str]]) -> dict[str, str]:
        """This function will convert `chat_completion` format into AG2 `init_chat` format.

        init_chat can accept dict[str, Any], but chat_completion will be list[dict[str, Any]].

        Args:
            messages (list[dict[str, str]]): The messages you want to convert.

        Returns:
            dict[str, str]: The converted messages.
                Output will follow this order: `system` -> `assistant` -> `user`.

        Examples:
            === "python"

            ```python
            messages = [
                {"role": "assistant", "content": "You should be kind."},
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hi there!"},
            ]
            analog_agent = AnalogAgent()
            parsed_message_dict = analog_agent.convert_init_message(messages=messages)
            print(parsed_message_dict)
            # >>> {'system': 'You are a helpful assistant.', 'assistant': 'You should be kind.', 'user': 'Hi there!'}
            ```
        """
        dict_order = ["system", "assistant", "user"]
        if not isinstance(messages, list):
            return {"role": "user", "content": f"{messages}"}
        parsed_messages = [MessageModel(**message) for message in messages]
        message_dict: dict[str, str] = {}
        for parsed_message in parsed_messages:
            if parsed_message.role in message_dict:
                message_dict[parsed_message.role] += "\n" + parsed_message.content
            else:
                message_dict[parsed_message.role] = parsed_message.content
        message_dict = {key: message_dict[key] for key in dict_order if key in message_dict}
        return message_dict

    def use_chat_completion(self, model: str, messages: list[dict[str, str]]) -> ChatCompletion:
        messages[-1]["content"] += (
            "\nYou should only output the Pyspice python code in code block."
        )
        llm_config = get_config_dict(model=model)
        client = AzureOpenAI(
            api_key=llm_config["config_list"][0]["api_key"],
            azure_endpoint=llm_config["config_list"][0]["base_url"],
            api_version=llm_config["config_list"][0]["api_version"],
            http_client=httpx.Client(headers=llm_config["config_list"][0]["default_headers"]),
        )
        if "o1" in model:
            result = client.chat.completions.create(messages=messages, model=model)
        else:
            result = client.chat.completions.create(
                messages=messages, model=model, temperature=llm_config["temperature"]
            )
        return result

    def testbench_hook(
        self, content: str, task: str, task_type: str, input_nodes: str, output_nodes: str
    ) -> str:
        prompt = f""" You are required to create checker functions for {task}, assuming the main input nodes are {input_nodes} and the main output nodes are {output_nodes}. These checker functions should help validate both the functionality and correctness of the netlist in an analog design context, using Spice simulations (e.g., PySpice).

        IMPORTANT GUIDELINES:

        Only perform checks that are relevant for the given task. Skip any checks not applicable to the current design objective.
        Each checker function should:
        Identify possible errors or design violations.
        Provide an explicit error message.
        Suggest relevant improvements or design solutions.
        Raise an exception if the design fails a crucial check.
        AVAILABLE CHECKS:

        Floating-point Check (Circuit Connection)

        Insert the PySpice netlist template "{pyspice_template}" to verify the presence and validity of all operating_nodes.
        Ensure no unintended floating nodes exist and that the circuit connectivity is intact.
        DC Sweep Check

        Step 1: Identify the netlist names for vinn and vinp (the negative and positive input supply nodes).
        Step 2: Use the DC sweep template "{dc_sweep_template}" to run a voltage sweep.
        Step 3: Determine the "best" operating voltage from the DC sweep results.
        Step 4: Modify the circuit netlist to fix the input supply at the 'best' voltage.
        Step 5: Validate that the circuit netlist still functions correctly under these conditions.
        Requirement Check

        First: Use the "{output_netlist_template}" to generate or finalize the netlist for the design.
        Verify that the correct input and output nodes are present in the netlist.
        Verify that the input voltages are defined and within reasonable bounds.
        Check basic netlist integrity (e.g., all references for power rails are valid, no missing components).
        Simulation and Device Check

        Verify that each MOSFET (NMOS and PMOS) follows fundamental transistor rules:
        NMOS: Vgs > Vth, Vds > (Vgs - Vth) for proper operation region.
        PMOS: Similar relevant conditions, ensuring correct source-drain orientation and threshold constraints.
        For each violation detected, raise an error detailing which device is at fault and suggest potential fixes (e.g., adjusting bias voltages, swapping pins).
        Functional Check

        (High-level) Confirm the circuit performs the intended function. For instance:
        Amplifier meets expected gain.
        Bias generator provides stable reference voltage.
        Switch or comparator transitions at the correct node voltages.
        """
        return f"{content}\n\n{prompt}"

    # def circuit_hook(
    #     self, content: str, task: str, task_type: str, input_nodes: str, output_nodes: str
    # ) -> str:
    #     prompt = f"""
    #         ## Your role \nAnalog_{task}_Expert is a seasoned analog integrated circuits specialist with a focus on designing {task_type} with input {input_nodes} and output {output_nodes}. In addition to expertise in analog circuit design, they possess strong Python programming skills and are proficient in using PySpice for accurate and robust simulation of analog circuits.
    #         \n\n## Task and skill instructions \n- Task description: The expert is responsible for designing high-performance {task_type} and employing simulation tools to verify the design integrity. This includes running comprehensive simulations to detect issues such as singular matrices, ensuring that the circuit designs work as intended under various operating conditions. \n- Skill description: The expert has in-depth knowledge of analog integrated circuit design, particularly in developing {task_type}. In parallel, they are skilled in Python programming and have extensive experience using PySpice for circuit simulation. This dual expertise ensures that designs are not only theoretically sound but are also rigorously tested and validated through simulation, addressing potential pitfalls before fabrication. \n- Additional information: Their work meticulously bridges the gap between circuit design and simulation verification, ensuring that every component of the design process is thoroughly checked for errors or issues, culminating in reliable, high-quality analog systems.
    #     """
    #     return f"{content}\n\n{prompt}"

    def dc_sweep_hook(
        self, content: str, task: str, task_type: str, input_nodes: str, output_nodes: str
    ) -> str:
        if task_type == "Opamp":
            prompt = f"""
            DCSweep_Checker is a verification engineer tasked with testing whether the {task} circuit passes the DC Sweep Check. You should keep the original code and create a file in your folder named dc_sweep.py that includes both the circuit code and the check code.

            Follow these steps to perform the complete DC Sweep Check:

                1. Generate netlist.sp from the existing circuit code.
                2. Extract the names of Vinn and Vinp from netlist.sp.
                3. If Vinp is found, replace both circuit.V(Vinn_name) and circuit.V(Vinp_name) with: circuit.V('dc', 'Vinn', 'Vinp', 0.0)
                4. Using {dc_sweep_template} (do not modify any template code), replace V[IN_NAME] and execute the DC sweep.
                5. Determine the best voltage from {best_voltage_template}.
                6. Update the original circuit code by setting the voltages of Vinn and Vinp to the best voltage (a floating-point value).
                7. Run an OP (operating point) test using the updated circuit code.
                8. If all steps succeed, generate a new netlist.sp to replace the old one.

            No plotting is required. If dc_sweep.py executes successfully, then the original code has passed the DC sweep check.
        """

        else:
            prompt = f"""
            DCSweep_Checker is a verification engineer tasked with testing whether the {task} circuit passes the DC Sweep Check. You should keep the original code and create a file in your folder named dc_sweep.py that includes both the circuit code and the check code.

            Follow these steps to perform the complete DC Sweep Check:

                1. Generate netlist.sp from the existing circuit code.
                2. Extract the names of Vinn and Vinp from netlist.sp.
                3. Using {dc_sweep_template} (do not modify any template code), replace V[IN_NAME] and execute the DC sweep.
                4. Determine the best voltage from {best_voltage_template}.
                5. Update the original circuit code by setting the voltages of Vinn and Vinp to the best voltage (a floating-point value).
                6. Run an OP (operating point) test using the updated circuit code.
                7. If all steps succeed, generate a new netlist.sp to replace the old one.

            No plotting is required. If dc_sweep.py executes successfully, then the original code has passed the DC sweep check.
        """
        return f"{content}\n\n{prompt}"

    def func_hook(
        self, content: str, task: str, task_type: str, input_nodes: str, output_nodes: str
    ) -> str:
        with open(f"problem_check/{task_type}.py") as test_code_file:
            test_code = test_code_file.read()

        if task_type == "Opamp" or task_type == "Amplifier":
            prompt = f"""
            Function_Checker is a verification engineer who introduces function-check code into the circuit for verification. You should create a file named function_check.py that contains both the circuit code and the check code needed to perform the function check.

            Follow these steps to complete the function check for {task}:

                1. Modify the voltage sources for Vinn and Vinp to "dc X.XX ac 1u". For example:

                    - circuit.V("inp", "Vinp", circuit.gnd, X.XX) → circuit.V("inp", "Vinp", circuit.gnd, "dc X.XX ac 1u")
                    - circuit.V("inn", "Vinn", circuit.gnd, X.XX) → circuit.V("inn", "Vinn", circuit.gnd, "dc X.XX ac 1u")

                2. Add the following verification code directly into your PySpice circuit (do not modify this check code): {test_code}

            If function_check.py runs successfully, the original code passes the function check. If it fails, return both the error message and your recommendation(s) for resolving it.
        """
        else:
            prompt = f"""
            Function_Checker is a verification engineer who introduces function-check code into the circuit for verification. You should create a file named function_check.py that contains both the circuit code and the check code needed to perform the function check.

            Follow these steps to complete the function check for {task}:

                1. Add the following verification code directly into your PySpice circuit (do not modify this check code): {test_code}

            If function_check.py runs successfully, the original code passes the function check. If it fails, return both the error message and your recommendation(s) for resolving it.
        """
        return f"{content}\n\n{prompt}\n\nPlease revert to the original code if the check passed."

    def mosfets_hook(
        self, content: str, task: str, task_type: str, input_nodes: str, output_nodes: str
    ) -> str:
        prompt = """
            GENERAL PURPOSE
            • Always ensure the MOSFET terminals (Drain, Source, Gate) have appropriate voltage levels for the device type.
            • Check that VGS (Gate-Source Voltage) is set correctly for the intended operation region (cut-off vs. conduction).
            • For an active (ON) NMOS, typically VDS ≥ 0 and VGS > VTH.
            • For an active (ON) PMOS, typically VSD ≥ 0 (meaning the source is at a higher potential than the drain) and VSG > |VTH| (or equivalently, VGS < -|VTH|).

            NMOS RULES AND CONCEPTS
            Drain-to-Source Voltage (VDS)
            • Do not connect the NMOS drain directly to ground if you expect high-side or switching behavior.
            • Ensure the drain node is at a higher potential than the source node. A drain voltage lower than the source indicates incorrect connection or reversed orientation for standard low-side configuration.
            • Typical requirement for conduction: VDS ≥ 0 (Drain ≥ Source).

            Gate-to-Source Voltage (VGS)
            • For an NMOS to turn on (enhancement mode), VGS must exceed the threshold voltage (VTH).
            • Avoid having the gate at the same or a lower voltage than the source if you want the transistor to conduct:
            - If gate = source ⇒ transistor is certainly off.
            - If gate < source ⇒ transistor is off or reversed.
            - If gate ≤ source + VTH ⇒ you are below or near threshold, so the MOSFET may be only weakly on or off.
            • Suggestion: Increase the gate voltage (relative to source) above VTH to operate in the ON region.

            Activation Tip
            • Ensure VGS > VTH and that the drain is at a higher potential than the source (VDS ≥ 0) if the NMOS is intended to conduct.

            PMOS RULES AND CONCEPTS

            Drain-to-Source Voltage (VDS)
            • Do not connect the PMOS drain directly to the supply rail (VDD) if you plan on switching or controlling a load.
            • Typically, for a PMOS in a high-side configuration, the source is at VDD, and the drain is at a lower potential (toward the load).
            • If the drain > source, this is reversed bias for a PMOS in normal operation.
            • In many practical circuits, VDS < 0 (Drain < Source) is the expected condition for conduction.

            Gate-to-Source Voltage (VGS)
            • For a PMOS to turn on (enhancement mode), the gate voltage must be sufficiently below the source voltage.
            • Avoid having the gate at the same or a higher voltage than the source if you want conduction:
            - If gate = source ⇒ transistor is off.
            - If gate > source ⇒ transistor is off or reversed.
            - If gate ≥ source - |VTH| ⇒ not significantly negative enough to switch on the PMOS.
            • Suggestion: Decrease the gate voltage (below the source) so that |VGS| > |VTH| to properly bias the PMOS.

            Activation Tip
            • Ensure VGS < -VTH (numerically negative beyond the threshold) and that the drain is at a sufficiently lower voltage than the source to turn the PMOS on.

            SUMMARY OF CHECKS
            • NMOS (enhancement mode):
            - VDS ≥ 0 for proper conduction.
            - VGS > VTH for “on” state.
            • PMOS (enhancement mode):
            - VSD ≥ 0 (Source ≥ Drain) in normal high-side usage.
            - VGS < -VTH for “on” state.
            • Avoid tying drain to a rail (ground for NMOS, VDD for PMOS) unless you fully understand the intended switching configuration (e.g., low-side vs. high-side switch).
            • Ensure the gate is not inadvertently tied to the source; that kills your driving signal unless it's an intentional pass-device configuration.
            • If the MOSFET is meant to be “on,” confirm that it can handle the required voltage and current, and that the gate voltage can swing as needed to turn it fully on.
        """
        return f"{content}\n\n{prompt}"

    def use_groupchat_tba(
        self,
        model: str,
        task: str,
        task_type: str,
        input_nodes: str,
        output_nodes: str,
        messages: list[dict[str, str]],
        work_dir: str,
        use_rag: bool = False,
    ) -> ChatCompletion:
        llm_config = get_config_dict(model=model)
        self._get_cache(llm_config=llm_config)
        pi_agent = autogen.AssistantAgent(
            name="Analog_Planning_Expert",
            description=f"Analog_Planning_Expert is a seasoned analog integrated circuits specialist who plan how to design {task} circuit and check function.",
            system_message=f"""
            ## Your role  \nAnalog_Planning_Expert is a seasoned analog integrated circuits specialist who plan how to design a circuit and check function.
            ## Your Job \n You are good at plannig how the {task} circuit will be designed. And you will dispatch the jobs to Analog_expert and checker agents, such as DCSweep_Checker, Function_Checker, MOSFET_Connection_Checker.

            The final code might be modified by the checkers, please revert it to the orginial one if the circuit pass the checks.
            """,
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=6,
            human_input_mode="NEVER",
            code_execution_config=False,
            llm_config=llm_config,
        )
        # pi_agent.register_hook(
        #     "process_last_received_message",
        #     lambda content: f"{content}\n\nLet's think step by step.",
        # )

        executor = autogen.UserProxyAgent(
            name="executor",
            human_input_mode="NEVER",
            is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
            code_execution_config={"use_docker": self.use_docker, "work_dir": work_dir},
        )
        circuit_agent = autogen.AssistantAgent(
            name=f"Analog_{task_type}_expert",
            description=f"Analog_{task_type}_expert is a seasoned analog integrated circuits specialist with a focus on designing and modify {task} who use Python and PySpice for rigorous simulation and verification to ensure reliable, error-free designs.",
            system_message=f"""
                ## Your role \nAnalog_{task}_Expert is a seasoned analog integrated circuits specialist with a focus on designing and modify {task_type} with input {input_nodes} and output {output_nodes}. In addition to expertise in analog circuit design, they possess strong Python programming skills and are proficient in using PySpice for accurate and robust simulation of analog circuits.
                \n\n## Task description: The expert is responsible for designing {task_type}. To make sure the circuit is executable add this code template to check: {pyspice_template}

                DO NOT MODIFTY THE CODE THAT ARE NOT FROM THIS EXPERT.
            """,
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=6,
            human_input_mode="NEVER",
            code_execution_config=False,
            llm_config=llm_config,
        )
        # circuit_agent.register_hook(
        #     "process_last_received_message", lambda content: self.circuit_hook(content, task, task_type, input_nodes, output_nodes)
        # )

        testbench_agent = autogen.AssistantAgent(
            name=f"{task_type}_TestBench_Agent",
            description=f"{task_type}_TestBench_Agent is a junior engineer who adds the Pyspice circuit checker functions(testbench) to code that Analog_{task_type}_expert generated and check if there are any error.",
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=12,
            human_input_mode="NEVER",
            code_execution_config=False,
            llm_config=llm_config,
        )
        testbench_agent.register_hook(
            "process_last_received_message",
            lambda content: self.testbench_hook(
                content, task, task_type, input_nodes, output_nodes
            ),
        )

        dc_sweep_agent = autogen.AssistantAgent(
            name="DCSweep_Checker",
            description=f"DCSweep_Checker is a verification engineer to add code to check if {task} circuit pass DC Sweep Check.",
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=6,
            human_input_mode="NEVER",
            code_execution_config=False,
            # code_execution_config={"use_docker": self.use_docker, "work_dir": work_dir},
            llm_config=llm_config,
        )
        dc_sweep_agent.register_hook(
            "process_last_received_message",
            lambda content: self.dc_sweep_hook(
                content, task, task_type, input_nodes, output_nodes
            ),
        )

        funcheck_agent = autogen.AssistantAgent(
            name="Function_Checker",
            description="Function_Checker is a verification engineer who add function check code to circuit to perform check.",
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=6,
            human_input_mode="NEVER",
            code_execution_config=False,
            # code_execution_config={"use_docker": self.use_docker, "work_dir": work_dir},
            llm_config=llm_config,
        )

        funcheck_agent.register_hook(
            "process_last_received_message",
            lambda content: self.func_hook(content, task, task_type, input_nodes, output_nodes),
        )

        mosfets_agent = autogen.AssistantAgent(
            name="MOSFETs_connection_checker",
            description="MOSFETs_connection_checker is a verification engineer who perform MOSFETs connection check.",
            # system_message="""
            #     Check all MOSFETs: Vgs > Vth, Vds > Vgs-Vth
            #         - NMOS
            #         - PMOS
            # """,
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            max_consecutive_auto_reply=6,
            human_input_mode="NEVER",
            code_execution_config=False,
            # code_execution_config={"use_docker": self.use_docker, "work_dir": work_dir},
            llm_config=llm_config,
        )
        mosfets_agent.register_hook(
            "process_last_received_message",
            lambda content: self.mosfets_hook(content, task, task_type, input_nodes, output_nodes),
        )

        proxies = [pi_agent]
        agents = [circuit_agent, testbench_agent]
        # if task_type in ["Opamp", "Amplifier"]:
        #     agents.append(dc_sweep_agent)
        #     agents.append(funcheck_agent)
        # if task_type in ["CurrentMirror", "Inverter"]:
        #     agents.append(funcheck_agent)

        groupchat = autogen.GroupChat(
            agents=[*proxies, *agents, executor],
            messages=[],
            max_round=12,
            speaker_selection_method="auto",
            allow_repeat_speaker=False,
        )
        manager = autogen.GroupChatManager(
            groupchat=groupchat,
            llm_config=llm_config,
            system_message="""
            1. The final code might be modified by the checkers, please revert it to the orginial one if the circuit pass the checks.
            2. If the executor successfully execute code for three time, TERMINATE the discussion.
            3. Execute code after every modification.
            """,
        )
        # manager.register_hook(
        #     "process_last_received_message", lambda content: f"{content}\n\n If the code answer or error repeat for three times in the chat history, please print TERMINATE to stop the discussion."
        # )

        # Start chatting with boss_aid as this is the user proxy agent.
        chat_result = pi_agent.initiate_chat(
            recipient=manager,
            message=f"{messages}, the final answer must and only contain a PySpice Code in Python.",
            summary_method=self._summary_method,
        )
        converter = ChatResultConverter(chat_result=chat_result)
        result = converter.convert_to_chat_completion()
        return result

    def use_groupchat(
        self,
        model: str,
        messages: list[dict[str, str]],
        work_dir: str,
        use_rag: bool,
        groupchat_config: str,
    ) -> ChatCompletion:
        llm_config = get_config_dict(model=model)
        self._get_cache(llm_config=llm_config)
        config = OmegaConf.load(groupchat_config)
        proxies: list[autogen.UserProxyAgent] = []
        for proxy_config in config.proxies:
            proxy: autogen.UserProxyAgent = hydra.utils.instantiate(proxy_config)
            if isinstance(proxy._code_execution_config, dict):  # noqa: SLF001
                proxy._code_execution_config.update({"work_dir": work_dir})  # noqa: SLF001
                proxy._code_execution_config.pop("_convert_")  # noqa: SLF001
            proxies.append(proxy)

        agents: list[autogen.AssistantAgent] = []
        for assistant_config in config.assistants:
            agent: autogen.AssistantAgent = hydra.utils.instantiate(assistant_config)
            if agent.name == "Analog_Expert":
                agent.register_hook(
                    "process_last_received_message",
                    lambda content: f"{content}\n\nPlease help me design the mentioned circuit. Think and tell me the necessary steps.\nLet's think step by step.",
                )
            agents.append(agent)

        if use_rag is True:
            for agent in agents:
                d_retrieve_content = agent.register_for_llm(
                    description="retrieve the information you need or if you have any question, you can use this function to get the answer.",
                    api_style="tool",
                )(retrieve_data)
            for proxy in proxies:
                proxy.register_for_execution()(d_retrieve_content)
                messages.append({
                    "role": "user",
                    "content": "You should use `retrieve_data` function to retrieve the information you need before making the correct decision and plan for your main PySpice Code.",
                })
        groupchat = autogen.GroupChat(
            agents=[*proxies, *agents],
            messages=[],
            max_round=12,
            speaker_selection_method="auto",
            allow_repeat_speaker=False,
        )
        manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

        # Start chatting with boss_aid as this is the user proxy agent.
        chat_result = proxies[0].initiate_chat(
            recipient=manager,
            message=f"{messages}, the final answer must contain a PySpice Code in Python. The code should be fully tested before terminated.",
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
                "config_file_or_env": "./configs/llm/OAI_CONFIG_LIST",
                "builder_model": "aide-o3-mini",
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
            silent=True,
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
        # extra_prompt_path = Path("./configs/prompt/prompt4checks.md")
        # extra_prompt = extra_prompt_path.read_text()
        # messages.append({"role": "user", "content": extra_prompt})
        messages.append({"role": "user", "content": "Please just seek_experts_help"})

        if use_rag is True:
            d_retrieve_content = captain_agent.assistant.register_for_llm(
                description="retrieve the information you need or if you have any question, you can use this function to get the answer.",
                api_style="tool",
            )(retrieve_data)
            captain_agent.executor.register_for_execution()(d_retrieve_content)
            messages.append({
                "role": "user",
                "content": "You should use `retrieve_data` function to retrieve the information you need before making the correct decision and plan for your main PySpice Code.",
            })
        # message = self.convert_init_message(messages=messages)
        chat_result = captain_user_proxy.initiate_chat(
            captain_agent,
            message=f"{messages}",
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
    groupchat_config: str,
    task: str = "",
    task_type: str = "",
    input_nodes: str = "",
    output_nodes: str = "",
) -> ChatCompletion:
    cache_path = Path("./.cache")
    cache_path.mkdir(parents=True, exist_ok=True)
    analog_agent = AnalogAgent(use_docker=False)
    if mode == "original":
        chat_result = analog_agent.use_chat_completion(model=model, messages=messages)
    elif "captain" in mode:
        use_rag = False
        if "rag" in mode:
            use_rag = True
        chat_result = analog_agent.use_captain(
            model=model, messages=messages, work_dir=work_dir, use_rag=use_rag
        )
    elif "groupchat+tba" in mode:
        chat_result = analog_agent.use_groupchat_tba(
            model=model,
            task=task,
            task_type=task_type,
            input_nodes=input_nodes,
            output_nodes=output_nodes,
            messages=messages,
            work_dir=work_dir,
        )
    elif "groupchat" in mode:
        use_rag = False
        if "rag" in mode:
            use_rag = True
        chat_result = analog_agent.use_groupchat(
            model=model,
            messages=messages,
            work_dir=work_dir,
            use_rag=use_rag,
            groupchat_config=groupchat_config,
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
