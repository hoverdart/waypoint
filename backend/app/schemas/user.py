from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    auth_provider_id: str
    email: str
    display_name: str | None
    mode: str


class UserUpdate(BaseModel):
    mode: Literal["professional", "gamified"] | None = None
    display_name: str | None = Field(default=None, max_length=100)

    @field_validator("mode")
    @classmethod
    def mode_cannot_be_null(cls, value):
        if value is None:
            raise ValueError("Mode cannot be null")
        return value
