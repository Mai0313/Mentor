from typing import Optional

from pydantic import Field, BaseModel


class AutogenUsage(BaseModel):
    cost: Optional[float] = Field(default=0.0, title="Cost of the API call")
    prompt_tokens: Optional[int] = Field(default=0, title="Number of tokens in the prompt")
    completion_tokens: Optional[int] = Field(default=0, title="Number of tokens in the completion")
    total_tokens: Optional[int] = Field(
        default=0, title="Total number of tokens in the prompt and completion"
    )
