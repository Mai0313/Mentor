from enum import Enum
from typing import Any
from pathlib import Path

from pydantic import Field, BaseModel, ConfigDict, computed_field, model_validator
from autogen.cache import Cache
from autogen.code_utils import extract_code


class AnalogAgentMode(str, Enum):
    # Using ChatCompletion
    original: str = "original"
    # Using GroupChat Based
    groupchat: str = "groupchat"
    # Using Captain Agent
    captain: str = "captain"
    # Using Swarm Agent
    swarm: str = "swarm"
    # TestBench Mode
    groupchat_tba: str = "groupchat+tba"
    # RAG Mode
    groupchat_rag: str = "groupchat+rag"
    captain_rag: str = "captain+rag"
    # RAG Mode with CoS
    groupchat_rag_cos: str = "groupchat+rag+cos"
    captain_rag_cos: str = "captain+rag+cos"


class AnalogAgentArgs(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    model: str = Field(
        ...,
        title="The Model Name",
        description="The model name you want to use, such as aide-gpt-4o.",
        examples=["aide-gpt-4o", "aide-o3-mini"],
        frozen=True,
        deprecated=False,
    )
    messages: list[dict[str, str]] = Field(
        ...,
        title="The Original Input Messages",
        description="The original input messages to the agent; it should follow the format of openai ChatCompletion.",
        frozen=True,
        deprecated=False,
    )
    mode: AnalogAgentMode = Field(
        ...,
        title="The Mode of the Agent",
        description="The mode of the agent, such as original, captain, groupchat, etc.",
        examples=[
            "original",
            "groupchat",
            "captain",
            "swarm",
            "groupchat+tba",
            "captain+rag",
            "groupchat+rag",
            "captain+rag+cos",
            "groupchat+rag+cos",
        ],
        frozen=True,
        deprecated=False,
    )

    # Required only if `groupchat` or `captain` mode
    work_dir: str = Field(
        default=".",
        title="The Working Directory",
        description="The working directory groupchat can use; it is not required if you are using `original` mode.",
        examples=[".", "./path/to/folder"],
        frozen=False,
        deprecated=False,
    )
    groupchat_config: str = Field(
        default="./configs/agents/groupchat_wo_cos.yaml",
        title="The GroupChat Config File",
        description="The groupchat config file you want to use; it is not required if you are using `original` mode.",
        examples=["./configs/agents/groupchat.yaml", "./configs/agents/groupchat_wo_cos.yaml"],
        frozen=False,
        deprecated=False,
    )

    # Required only if `groupchat+tba` mode
    task: str = Field(
        default="",
        title="The Task Name",
        description="This is the Circuit name from problem set.",
        examples=["a single-stage common-source amplifier with resistive load R"],
        frozen=False,
        deprecated=False,
    )
    task_type: str = Field(
        default="",
        title="The Task Type",
        description="This is the Circuit type from problem set, it is required only if you are using `groupchat+tba` mode.",
        examples=["Amplifier", "Opamp", "CurrentMirror", "Inverter"],
        frozen=False,
        deprecated=False,
    )
    input_nodes: str = Field(
        default="",
        title="The Input Nodes",
        description="This is the input nodes of the circuit, it is required only if you are using `groupchat+tba` mode.",
        examples=["Vin", "Vbias"],
        frozen=False,
        deprecated=False,
    )
    output_nodes: str = Field(
        default="",
        title="The Output Nodes",
        description="This is the output nodes of the circuit, it is required only if you are using `groupchat+tba` mode.",
        examples=["Vout", "Vbias"],
        frozen=False,
        deprecated=False,
    )

    @computed_field
    @property
    def use_rag(self) -> bool:
        return "rag" in self.mode

    @computed_field
    @property
    def use_cos(self) -> bool:
        return "cos" in self.mode

    @model_validator(mode="after")
    def _setup_workdir(self) -> "AnalogAgentArgs":
        self.work_dir = Path(self.work_dir).parent.absolute().as_posix()
        return self

    def _get_cache(self, llm_config: dict[str, Any]) -> Cache:
        cache = None
        cache_seed = llm_config.get("cache_seed")
        if cache_seed:
            cache = Cache.disk(cache_seed=cache_seed, cache_path_root="./.cache")
        return cache
