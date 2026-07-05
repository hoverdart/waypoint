from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class AIUsage(SQLModel, table=True):
    __tablename__ = "ai_usage"
    __table_args__ = (
        sa.UniqueConstraint("user_id", "period_start", "period_end", name="uq_ai_usage_period"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    period_start: datetime
    period_end: datetime
    free_used: int = Field(default=0)
    premium_used: int = Field(default=0)
    max_allowed: int
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )
