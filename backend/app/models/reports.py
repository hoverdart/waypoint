from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class QuestionReport(SQLModel, table=True):
    __tablename__ = "question_reports"
    __table_args__ = (
        sa.CheckConstraint(
            "status IN ('pending','reviewed','dismissed')", name="ck_question_reports_status"
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    question_id: int = Field(foreign_key="questions.id", index=True)
    reason: str
    details: str | None = None
    status: str = Field(default="pending")
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
