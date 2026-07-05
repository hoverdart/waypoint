from datetime import date, datetime

import sqlalchemy as sa
from sqlmodel import Column, Field, SQLModel

from app.models.common import JSONVariant


class DailyPlan(SQLModel, table=True):
    __tablename__ = "daily_plans"
    __table_args__ = (
        sa.CheckConstraint(
            "status IN ('pending','active','completed','skipped')",
            name="ck_daily_plans_status",
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    plan_date: date = Field(index=True)
    point_budget: int
    status: str = Field(default="pending")
    generated_reason: dict = Field(default_factory=dict, sa_column=Column(JSONVariant))
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))


class DailyPlanItem(SQLModel, table=True):
    __tablename__ = "daily_plan_items"
    __table_args__ = (
        sa.CheckConstraint(
            "item_type IN ('review','weakness','calibration','frq','challenge')",
            name="ck_daily_plan_items_item_type",
        ),
        sa.CheckConstraint(
            "status IN ('pending','completed','skipped')",
            name="ck_daily_plan_items_status",
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    daily_plan_id: int = Field(foreign_key="daily_plans.id", index=True)
    subject_id: int = Field(foreign_key="subjects.id")
    unit_id: int = Field(foreign_key="units.id")
    topic_id: int = Field(foreign_key="topics.id")
    item_type: str
    point_cost: int
    priority_score: float
    reason: str
    status: str = Field(default="pending")
