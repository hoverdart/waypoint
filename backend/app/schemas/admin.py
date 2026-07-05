from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.reports import QuestionReportRead


class AdminQuestionOptionInput(BaseModel):
    label: str
    text: str
    is_correct: bool


class AdminExplanationInput(BaseModel):
    option_label: str | None = None
    explanation: str
    misconception_tag: str | None = None


class AdminQuestionCreate(BaseModel):
    subject_id: int
    unit_id: int
    topic_id: int
    type: str
    difficulty: int
    prompt: str
    correct_answer: str
    rubric_json: dict | None = None
    skill_tags: list[str] = []
    misconception_tags: list[str] = []
    source: str = "human_written"
    validation_status: str = "draft"
    options: list[AdminQuestionOptionInput] = []
    explanations: list[AdminExplanationInput] = []


class AdminQuestionUpdate(BaseModel):
    prompt: str | None = None
    correct_answer: str | None = None
    difficulty: int | None = None
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
    status: str


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
