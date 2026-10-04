from datetime import datetime

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.stimulus import DataTable
from app.schemas.reports import QuestionReportRead


class AdminQuestionOptionInput(BaseModel):
    label: str = Field(min_length=1, max_length=5)
    text: str = Field(min_length=1, max_length=5000)
    is_correct: bool


class AdminExplanationInput(BaseModel):
    option_label: str | None = None
    explanation: str = Field(min_length=1, max_length=20000)
    misconception_tag: str | None = None


class AdminQuestionCreate(BaseModel):
    subject_id: int = Field(gt=0)
    unit_id: int = Field(gt=0)
    topic_id: int = Field(gt=0)
    type: Literal["mcq", "frq"]
    difficulty: int = Field(ge=1, le=5)
    prompt: str = Field(min_length=1, max_length=20000)
    correct_answer: str = Field(min_length=1, max_length=20000)
    data_table: DataTable | None = None
    rubric_json: dict | None = None
    skill_tags: list[str] = []
    misconception_tags: list[str] = []
    source: Literal["human_written", "generated", "imported"] = "human_written"
    validation_status: Literal["draft", "approved", "needs_review", "rejected"] = "draft"
    options: list[AdminQuestionOptionInput] = []
    explanations: list[AdminExplanationInput] = []


class AdminQuestionUpdate(BaseModel):
    prompt: str | None = Field(default=None, min_length=1, max_length=20000)
    correct_answer: str | None = Field(default=None, min_length=1, max_length=20000)
    difficulty: int | None = Field(default=None, ge=1, le=5)
    data_table: DataTable | None = None
    rubric_json: dict | None = None
    skill_tags: list[str] | None = None
    misconception_tags: list[str] | None = None
    options: list[AdminQuestionOptionInput] | None = None
    explanations: list[AdminExplanationInput] | None = None


class AdminQuestionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    unit_id: int
    topic_id: int
    type: str
    difficulty: int
    prompt: str
    correct_answer: str
    data_table: DataTable | None = None
    rubric_json: dict | None
    skill_tags: list
    misconception_tags: list
    source: str
    validation_status: str
    version: int
    is_active: bool
    created_at: datetime
    updated_at: datetime


class AdminQuestionDetailRead(AdminQuestionRead):
    options: list[AdminQuestionOptionInput] = []
    reports: list[QuestionReportRead] = []


class QuestionStatusUpdateRequest(BaseModel):
    status: Literal["draft", "approved", "needs_review", "rejected"]


class AdminUnitCreate(BaseModel):
    name: str
    description: str | None = None
    ap_weight_min: float
    ap_weight_max: float
    display_order: int = 0


class AdminUnitUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    ap_weight_min: float | None = None
    ap_weight_max: float | None = None
    display_order: int | None = None


class AdminTopicCreate(BaseModel):
    name: str
    description: str | None = None
    skill_tags: list[str] = []
    display_order: int = 0


class AdminTopicUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    skill_tags: list[str] | None = None
    display_order: int | None = None
