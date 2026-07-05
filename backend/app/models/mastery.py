from datetime import date, datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class TopicMastery(SQLModel, table=True):
    """Per-topic mastery. Composite PK, per spec's column list (no `id`).

    Written exclusively by services.mastery.topic_mastery.update_topic_mastery_after_session.
    """

    __tablename__ = "topic_mastery"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    topic_id: int = Field(foreign_key="topics.id", primary_key=True)
    mastery_score: float = Field(default=0.0)
    confidence_score: float = Field(default=0.0)
    retention_score: float = Field(default=1.0)
    topic_timer: float = Field(default=0.0)
    attempts_count: int = Field(default=0)
    correct_count: int = Field(default=0)
    last_practiced_at: datetime | None = None
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )
    # Approved addition beyond the literal spec: guarantees the topic timer
    # advances at most once per calendar day (see plan section 2), instead of
    # approximating idempotency off `updated_at`.
    timer_last_advanced_date: date | None = None


class UnitMastery(SQLModel, table=True):
    __tablename__ = "unit_mastery"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    unit_id: int = Field(foreign_key="units.id", primary_key=True)
    mastery_score: float = Field(default=0.0)
    confidence_score: float = Field(default=0.0)
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )


class SubjectMastery(SQLModel, table=True):
    __tablename__ = "subject_mastery"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    subject_id: int = Field(foreign_key="subjects.id", primary_key=True)
    mastery_score: float = Field(default=0.0)
    predicted_ap_score: int = Field(default=1)
    confidence_score: float = Field(default=0.0)
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )
