import os
from typing import Any
from pathlib import Path

import httpx
from openai import AsyncAzureOpenAI
import autogen
import logfire
import chromadb
from pydantic import Field, BaseModel
from pydantic_ai import Agent
from rich.console import Console
from chromadb.config import Settings
from pydantic_ai.models.openai import OpenAIModel
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from chromadb.utils.embedding_functions.openai_embedding_function import OpenAIEmbeddingFunction

console = Console()
logfire.configure(send_to_logfire=False)


def get_config_dict(model: str, temp: float = 0.5) -> dict[str, Any]:
    config_list = autogen.config_list_from_json(
        env_or_file="./configs/llm/OAI_CONFIG_LIST", filter_dict={"model": model}
    )
    llm_config = {
        "timeout": 60,
        "temperature": temp,
        "cache_seed": os.getenv("SEED", None),
        "config_list": config_list,
    }
    if "o1" in model or "o3" in model:
        llm_config.pop("temperature", None)
    return llm_config


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
    markdown_path = Path("./docs").rglob("*_parsed.md")
    text_path = Path("./docs").rglob("*.txt")
    subcircuit_lib = Path("./subcircuit_lib").rglob("*.py")
    all_docs = [*markdown_path, *text_path, *subcircuit_lib]
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
    all_docs_string = "\n- ".join(all_docs)
    response = agent.run_sync(
        user_prompt=f"""
        Here is all the docs: {all_docs_string}
        Please select the relevant docs to the following question by the docs titles:
        {query}

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
    rag_assistant = autogen.AssistantAgent(
        name="RetrieveAssistant",
        llm_config=llm_config,
        code_execution_config=False,
        silent=True,  # Set it to `False` if you want to see the conversation log.
    )
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
    )
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
    query = "How many opamps are there in the FIGURE 14 of `./docs/Razavi BGR/Razavi BGR.md`"
    result = retrieve_data(query=query)
    console.print(result)
