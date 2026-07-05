from datetime import date, datetime

import sqlalchemy as sa
from sqlmodel import Column, Field, SQLModel

from app.models.common import JSONVariant


class WeeklyCoachReport(SQLModel, table=True):
    __tablename__ = "weekly_coach_reports"
    __table_args__ = (
        sa.UniqueConstraint("user_id", "week_start", name="uq_weekly_coach_reports_user_week"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    week_start: date
    week_end: date
    summary: str
    biggest_win: str | None = None
    biggest_weakness: str | None = None
    next_week_priorities: list = Field(default_factory=list, sa_column=Column(JSONVariant))
    projected_score_note: str | None = None
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
