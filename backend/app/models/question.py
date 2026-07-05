from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Column, Field, SQLModel

from app.models.common import JSONVariant


class Question(SQLModel, table=True):
    __tablename__ = "questions"
    __table_args__ = (
        sa.CheckConstraint("difficulty BETWEEN 1 AND 5", name="ck_questions_difficulty_range"),
        sa.CheckConstraint("type IN ('mcq','frq')", name="ck_questions_type"),
        sa.CheckConstraint(
            "source IN ('generated','imported','human_written')", name="ck_questions_source"
        ),
        sa.CheckConstraint(
            "validation_status IN ('draft','approved','rejected','needs_review')",
            name="ck_questions_validation_status",
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    subject_id: int = Field(foreign_key="subjects.id", index=True)
    unit_id: int = Field(foreign_key="units.id", index=True)
    topic_id: int = Field(foreign_key="topics.id", index=True)
    type: str
    difficulty: int
    prompt: str
    correct_answer: str
    rubric_json: dict | None = Field(default=None, sa_column=Column(JSONVariant))
    skill_tags: list = Field(default_factory=list, sa_column=Column(JSONVariant))
    misconception_tags: list = Field(default_factory=list, sa_column=Column(JSONVariant))
    source: str = Field(default="human_written")
    validation_status: str = Field(default="draft", index=True)
    version: int = Field(default=1)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime, server_default=sa.func.now()))
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )


class QuestionOption(SQLModel, table=True):
    __tablename__ = "question_options"

    id: int | None = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="questions.id", index=True)
    label: str
    text: str
    is_correct: bool = Field(default=False)


class QuestionExplanation(SQLModel, table=True):
    __tablename__ = "question_explanations"

    id: int | None = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="questions.id", index=True)
    option_id: int | None = Field(default=None, foreign_key="question_options.id")
    explanation: str
    misconception_tag: str | None = None
