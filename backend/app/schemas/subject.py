from datetime import date

from pydantic import BaseModel, ConfigDict


class TopicRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    unit_id: int
    name: str
    description: str | None
    skill_tags: list
    display_order: int


class UnitRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    name: str
    description: str | None
    ap_weight_min: float
    ap_weight_max: float
    display_order: int


class UnitWithTopicsRead(UnitRead):
    topics: list[TopicRead] = []


class SubjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    ap_exam_code: str
    description: str | None
    is_active: bool
    display_order: int


class SubjectDetailRead(SubjectRead):
    units: list[UnitWithTopicsRead] = []


class UserSubjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    target_score: int | None
    exam_date: date | None
    study_minutes_per_day: int
    is_active: bool
