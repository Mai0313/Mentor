import os
from typing import Any
from pathlib import Path

import httpx
from openai import AzureOpenAI, AsyncAzureOpenAI
import autogen
from autogen import config_list_from_json
import chromadb
from pydantic import Field, BaseModel
from pydantic_ai import Agent
from rich.console import Console
from chromadb.config import Settings
from pydantic_ai.models.openai import OpenAIModel
from autogen.agentchat.contrib.img_utils import get_pil_image, pil_to_data_uri
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from chromadb.utils.embedding_functions.openai_embedding_function import OpenAIEmbeddingFunction

console = Console()


def get_config_dict(model: str, temp: float = 0.5) -> dict[str, Any]:
    config_list = config_list_from_json(
        env_or_file="./configs/llm/OAI_CONFIG_LIST", filter_dict={"model": model}
    )
    llm_config = {"timeout": 60, "cache_seed": os.getenv("SEED", None), "config_list": config_list}
    if "o1" not in model:
        llm_config["temperature"] = temp
    return llm_config


class DescribeImageInput(BaseModel):
    question: str = Field(..., description="The question you want to ask.")
    image_url: str = Field(
        ...,
        description="The image urls you want to describe, it should be a string of path that pair with the question.",
    )


class DescribeImagesOutput(BaseModel):
    answer: str = Field(..., description="The answer to the question you asked.")
    image_url: str = Field(
        ...,
        description="The image urls you want to describe, it should be a string of path that pair with the question.",
    )


def describe_images(image_infos: list) -> list[DescribeImagesOutput]:
    """Given a question and a list of image absolute paths, this tool will describe the image(s) you provided.

    Args:
        image_infos (list[dict[str, str]]): It should be a list of dict[str, str], which contains a pair of question and image absolute path.
            For example:
                ```
                [
                    {
                        "question": "How many opamps are there in the graph",
                        "image_url": "/home/ds906659/aith/AnalogCoder/docs/Razavi BGR/_page_0_Figure_13.jpeg",
                    }
                ]
                ```

    Returns:
        list[DescribeImagesOutput]: The description of the image(s) you provided, it is a pydantic model, you should use `.model_dump()` to get the dict.
    """
    llm_config = get_config_dict(model="aide-gpt-4o", temp=0.0)
    client = AzureOpenAI(
        api_key=llm_config["config_list"][0]["api_key"],
        azure_endpoint=llm_config["config_list"][0]["base_url"],
        api_version=llm_config["config_list"][0]["api_version"],
        http_client=httpx.Client(headers=llm_config["config_list"][0]["default_headers"]),
    )
    response_outputs: list[DescribeImagesOutput] = []
    for image_info in image_infos:
        image_info = DescribeImageInput(**image_info)
        content: list[dict[str, Any]] = [
            {
                "type": "text",
                "text": "Please follow the question below to describe the image(s) you received.",
            },
            {"type": "text", "text": image_info.question},
        ]
        if Path(image_info.image_url).exists():
            base64_image = get_pil_image(image_file=image_info.image_url)
            image_uri = pil_to_data_uri(base64_image)
            content.append({"type": "image_url", "image_url": {"url": image_uri}})
            response = client.chat.completions.create(
                model=llm_config["config_list"][0]["model"],
                messages=[{"role": "user", "content": content}],
                temperature=0.0,
            )
            response_output = DescribeImagesOutput(
                answer=response.choices[0].message.content, image_url=image_info.image_url
            )
            response_outputs.append(response_output)
        else:
            response_output = DescribeImagesOutput(
                answer=f"Cannot find the image of {image_info.image_url}, please check the image path.",
                image_url=image_info.image_url,
            )
            response_outputs.append(response_output)
    return response_outputs


class RetrieveResultOutput(BaseModel):
    original_question: str = Field(
        ...,
        title="Original Question of the user",
        description="The original question of the user.",
        frozen=True,
        deprecated=False,
    )
    final_answer: str = Field(
        ...,
        title="Final Answer",
        description="""The final answer from the chat history
        - `<< Real Answer >>` if the answer is found and relevant to the question.
        - `Answer NOT Found` if there is no answer found.
        - `Answer NOT Relevant` if the answer is not relevant.
        """,
        examples=["<< Real Answer >>", "Answer not found", "Answer not relevant"],
        frozen=True,
        deprecated=False,
    )


class CheckRelevantDocuments(BaseModel):
    relevant_docs: list[str] = Field(
        ...,
        title="Relevant Documents to the question",
        description="The relevant documents to the question, those paths should be absolute paths.",
        examples=[
            "/home/ds906659/aith/AnalogCoder/docs/Razavi BGR/Razavi BGR.md",
            "/home/ds906659/aith/AnalogCoder/docs/Bandgap References/Bandgap References.md",
        ],
        frozen=True,
        deprecated=False,
    )


def rag_summary_method(
    sender: RetrieveUserProxyAgent,
    recipient: autogen.GroupChatManager,
    summary_args: dict[str, Any],
) -> str:
    sender_messages = list(sender.chat_messages.values())[-1]
    sender_messages = sender_messages[:1]
    recipient_messages = list(recipient.chat_messages.values())[-1]
    recipient_messages = recipient_messages[-2:]
    messages = [*sender_messages, *recipient_messages]
    llm_config = get_config_dict(model="aide-gpt-4o")
    client = AsyncAzureOpenAI(
        api_key=llm_config["config_list"][0]["api_key"],
        azure_endpoint=llm_config["config_list"][0]["base_url"],
        api_version=llm_config["config_list"][0]["api_version"],
        http_client=httpx.AsyncClient(headers=llm_config["config_list"][0]["default_headers"]),
    )
    model = OpenAIModel(model_name="aide-gpt-4o", openai_client=client)
    agent = Agent(model=model, result_type=RetrieveResultOutput)
    response = agent.run_sync(user_prompt=f"{messages}")
    console.print(response.data)
    return f"{response.data.model_dump()}"


def retrieve_data(query: str) -> str:
    """Retrieve the information you need or if you have any question by given a query string, this tool is for retrieving knowledge from the docs.

    Args:
        query (str): The question you want to ask and search in the docs.

    Returns:
        str: The description of the image(s) you provided.

    Examples:
        >>> query = "What is the Product Version of Bandgap Reference Verification"
        >>> retrieved_result = retrieve_data(query=query)
    """
    llm_config = get_config_dict(model="aide-gpt-4o", temp=0.0)
    markdown_path = Path("./docs").rglob("*.md")
    text_path = Path("./docs").rglob("*.txt")
    subcircuit_lib = Path("./subcircuit_lib").rglob("*.py")
    all_docs = [*markdown_path, *text_path, *subcircuit_lib]
    all_docs = [f for f in all_docs if f.stem.endswith("_parsed")]
    all_docs = [doc.resolve().as_posix() for doc in all_docs]
    client = AsyncAzureOpenAI(
        api_key=llm_config["config_list"][0]["api_key"],
        azure_endpoint=llm_config["config_list"][0]["base_url"],
        api_version=llm_config["config_list"][0]["api_version"],
        http_client=httpx.AsyncClient(headers=llm_config["config_list"][0]["default_headers"]),
    )
    model = OpenAIModel(model_name="aide-gpt-4o", openai_client=client)
    agent = Agent(model=model, result_type=CheckRelevantDocuments)
    subcircuit_description = Path("./lib_info.tsv").read_text(encoding="utf-8")
    response = agent.run_sync(
        user_prompt=f"""
        Here is all the docs: {all_docs}, please select the relevant docs to the question: {query} by the docs titles.

        And also, this is the description of subcircuit_lib
        You should use the description to find the best match for those file under ./subcircuit_lib:
        {subcircuit_description}
        """
    )
    new_all_docs = response.data.relevant_docs
    if not new_all_docs:
        console.print("No relevant docs found.")
        return "No relevant docs found, please try again with another keyword."
    console.print("Relevant docs: ", new_all_docs)
    # all_docs = ["/home/ds906659/aith/AnalogCoder/docs/Razavi BGR/Razavi BGR.md"]
    rag_assistant = autogen.AssistantAgent(
        name="RetrieveAssistant",
        llm_config=llm_config,
        code_execution_config=False,
        silent=True,  # Set it to `False` if you want to see the conversation log.
    )
    # executor = autogen.UserProxyAgent(
    #     name="executor",
    #     human_input_mode="NEVER",
    #     is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    #     code_execution_config={"use_docker": "False"},
    #     description="This is a code execution agent, it will simpily execute a function call.",
    # )
    rag_proxy_agent = RetrieveUserProxyAgent(
        name="RetrieveProxyAgent",
        human_input_mode="NEVER",
        description="This is a proxy agent, it will retrieve the information you need.",
        max_consecutive_auto_reply=3,
        retrieve_config={
            "task": "default",
            "docs_path": new_all_docs,
            "must_break_at_empty_line": False,
            "model": "gpt-4o",
            "vector_db": None,
            "client": chromadb.Client(Settings(anonymized_telemetry=False)),
            "get_or_create": True,
            "update_context": False,
            "embedding_function": OpenAIEmbeddingFunction(
                api_key=llm_config["config_list"][0]["api_key"],
                api_base="http://mlop-azure-gateway.mediatek.inc",
                api_type="azure",
                api_version="2024-08-01-preview",
                model_name="aide-text-embedding-ada-002-v2",
                default_headers={"X-User-Id": "mtk26247"},
            ),
            "embedding_model": None,
        },
        code_execution_config=False,
        silent=True,  # Set it to `False` if you want to see the conversation log.
    )
    # query += "\nYou can use `describe_images` to see the image if the question asked to do so or the document content contains the image."
    # autogen.register_function(
    #     f=describe_images,
    #     caller=rag_assistant,
    #     executor=executor,
    #     name=describe_images.__name__,
    #     description=describe_images.__doc__,
    # )
    groupchat = autogen.GroupChat(
        agents=[rag_proxy_agent, rag_assistant],
        messages=[],
        max_round=12,
        speaker_selection_method="round_robin",
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
    chat_result = rag_proxy_agent.initiate_chat(
        recipient=manager,
        message=rag_proxy_agent.message_generator,
        problem=query,
        # 這個會決定 LLM 能參考多少文件，要讓她拿到正確資訊，就要全部允許他看
        n_results=len(new_all_docs),
        # summary_method=rag_summary_method,
    )
    # print(manager.last_speaker)
    all_history = []
    for history in chat_result.chat_history:
        content = history["content"]
        if content != "":
            all_history.append(content)
    last_message = all_history[1:] if all_history else chat_result.chat_history[-1]["content"]
    last_message = "\n".join(last_message) if last_message else f"{last_message}"
    console.print("+" * 30)
    console.print("Retrieved Document")
    console.print(last_message)
    console.print("+" * 30)
    return last_message


if __name__ == "__main__":
    # image_infos = [
    #     {
    #         "question": "How many opamps are there in the graph",
    #         "image_url": "./docs/Razavi BGR/_page_4_Figure_4.jpeg",
    #     },
    #     {
    #         "question": "How many opamps are there in the graph",
    #         "image_url": "./docs/Razavi BGR/_page_1_Figure_15.jpeg",
    #     },
    # ]
    # result = describe_images(image_infos=image_infos)
    query = "How many opamps are there in the FIGURE 14 of `./docs/Razavi BGR/Razavi BGR.md`"
    result = retrieve_data(query=query)
    print(result)
