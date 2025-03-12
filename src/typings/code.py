from pydantic import Field, BaseModel, computed_field


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
