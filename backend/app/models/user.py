from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (
        sa.CheckConstraint("mode IN ('professional','gamified')", name="ck_users_mode"),
    )

    id: int | None = Field(default=None, primary_key=True)
    auth_provider_id: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    display_name: str | None = None
    mode: str = Field(default="professional")
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )
