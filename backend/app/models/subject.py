from datetime import date

import sqlalchemy as sa
from sqlmodel import Column, Field, SQLModel

from app.models.common import JSONVariant


class Subject(SQLModel, table=True):
    __tablename__ = "subjects"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    ap_exam_code: str = Field(unique=True, index=True)
    description: str | None = None
    is_active: bool = Field(default=True)
    display_order: int = Field(default=0)


class Unit(SQLModel, table=True):
    __tablename__ = "units"

    id: int | None = Field(default=None, primary_key=True)
    subject_id: int = Field(foreign_key="subjects.id", index=True)
    name: str
    description: str | None = None
    ap_weight_min: float = Field(default=0.0)
    ap_weight_max: float = Field(default=0.0)
    display_order: int = Field(default=0)


class Topic(SQLModel, table=True):
    __tablename__ = "topics"

    id: int | None = Field(default=None, primary_key=True)
    unit_id: int = Field(foreign_key="units.id", index=True)
    name: str
    description: str | None = None
    skill_tags: list = Field(default_factory=list, sa_column=Column(JSONVariant))
    display_order: int = Field(default=0)


class UserSubject(SQLModel, table=True):
    __tablename__ = "user_subjects"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    subject_id: int = Field(foreign_key="subjects.id", index=True)
    target_score: int | None = None
    exam_date: date | None = None
    is_active: bool = Field(default=True)
    # Approved addition beyond the literal spec: onboarding captures a study-time
    # preference per subject, but the given schema has nowhere to persist it and
    # the daily planner needs it to compute the point budget (see plan section 2).
    study_minutes_per_day: int = Field(default=20)
