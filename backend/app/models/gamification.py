from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Column, Field, SQLModel

from app.models.common import JSONVariant


class XPEvent(SQLModel, table=True):
    __tablename__ = "xp_events"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    source: str
    amount: int
    event_metadata: dict = Field(default_factory=dict, sa_column=Column("metadata", JSONVariant))
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))


class Badge(SQLModel, table=True):
    __tablename__ = "badges"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    icon: str | None = None
    rule_json: dict = Field(default_factory=dict, sa_column=Column(JSONVariant))


class UserBadge(SQLModel, table=True):
    __tablename__ = "user_badges"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    badge_id: int = Field(foreign_key="badges.id", index=True)
    earned_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
