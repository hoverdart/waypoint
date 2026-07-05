from pydantic import BaseModel, ConfigDict


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    auth_provider_id: str
    email: str
    display_name: str | None
    mode: str


class UserUpdate(BaseModel):
    mode: str | None = None
    display_name: str | None = None
