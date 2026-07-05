from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Column, Field, SQLModel

from app.models.common import JSONVariant


class PracticeSession(SQLModel, table=True):
    __tablename__ = "practice_sessions"
    __table_args__ = (
        sa.CheckConstraint(
            "session_type IN ('diagnostic','daily_plan','mcq','frq','timed')",
            name="ck_practice_sessions_session_type",
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    subject_id: int = Field(foreign_key="subjects.id", index=True)
    unit_id: int | None = Field(default=None, foreign_key="units.id")
    topic_id: int | None = Field(default=None, foreign_key="topics.id")
    session_type: str
    started_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
    completed_at: datetime | None = None
    total_questions: int = Field(default=0)
    correct_count: int = Field(default=0)
    score: float = Field(default=0.0)
    # "metadata" is a reserved attribute name on SQLAlchemy declarative models;
    # the Python attribute is renamed but the DB column stays literally "metadata".
    session_metadata: dict = Field(
        default_factory=dict, sa_column=Column("metadata", JSONVariant)
    )


class QuestionAttempt(SQLModel, table=True):
    __tablename__ = "question_attempts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    session_id: int = Field(foreign_key="practice_sessions.id", index=True)
    question_id: int = Field(foreign_key="questions.id", index=True)
    selected_option_id: int | None = Field(default=None, foreign_key="question_options.id")
    free_response_text: str | None = None
    is_correct: bool = Field(default=False)
    score: float = Field(default=0.0)
    max_score: float = Field(default=1.0)
    time_seconds: int = Field(default=0)
    hints_used: int = Field(default=0)
    explanation_opened: bool = Field(default=False)
    confidence_rating: int | None = None
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
