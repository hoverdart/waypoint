from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt

from app.schemas.gamification import BadgeRead


class AnswerInput(BaseModel):
    question_id: int = Field(gt=0)
    selected_option_id: int | None = None
    free_response_text: str | None = Field(default=None, max_length=20000)
    time_seconds: int = Field(default=0, ge=0, le=86400)
    hints_used: int = Field(default=0, ge=0, le=100)
    explanation_opened: bool = False
    confidence_rating: int | None = Field(default=None, ge=1, le=5)


class QuestionOptionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    label: str
    text: str


class QuestionRead(BaseModel):
    scoring_method: Literal["automatic", "keyword", "self_review"] = "automatic"
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    unit_id: int
    topic_id: int
    type: str
    difficulty: int
    prompt: str
    options: list[QuestionOptionRead] = []


class PracticeSessionDetailResponse(BaseModel):
    session_id: int
    session_type: str
    subject_id: int
    is_completed: bool
    questions: list[QuestionRead]
    draft_answers: list[AnswerInput] = []
    current_index: int = 0
    daily_plan_item_id: int | None = None


class PracticeDraftRequest(BaseModel):
    answers: list[AnswerInput] = Field(default_factory=list, max_length=60)
    current_index: int = Field(default=0, ge=0, le=59)
    daily_plan_item_id: int | None = Field(default=None, gt=0)


class PracticeHistoryItem(BaseModel):
    is_exam: bool = False
    graded_count: int | None = None
    self_review_count: int = 0
    session_id: int
    subject_id: int
    subject_name: str
    session_type: str
    started_at: datetime
    completed_at: datetime | None
    total_questions: int
    correct_count: int
    score: float
    answered_count: int


class PracticeStartRequest(BaseModel):
    subject_id: int
    unit_id: int | None = None
    topic_id: int | None = None
    session_type: Literal["mcq", "frq", "timed"] = "mcq"
    question_count: int = Field(default=12, ge=1, le=60)


class PracticeStartResponse(BaseModel):
    session_id: int
    session_type: str
    questions: list[QuestionRead]


class PracticeSubmitRequest(BaseModel):
    answers: list[AnswerInput] = Field(min_length=1, max_length=60)
    daily_plan_item_id: int | None = None


class PracticeSubmitResponse(BaseModel):
    session_id: int
    session_type: str
    correct_count: int
    total_questions: int
    score: float


class ExplanationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    option_id: int | None
    explanation: str
    misconception_tag: str | None


class SelfReviewRequest(BaseModel):
    points: list[StrictInt] = Field(min_length=1, max_length=20)


class SelfReviewRead(BaseModel):
    points: list[int]
    total: int
    reviewed_at: datetime


class RubricCriterionRead(BaseModel):
    levels: list[str] = []
    point: str
    points: float


class AnswerBreakdownItem(BaseModel):
    scoring_method: Literal["automatic", "keyword", "self_review"] = "automatic"
    self_review: SelfReviewRead | None = None
    question_id: int
    topic_id: int
    prompt: str
    type: str
    is_correct: bool | None
    score: float | None
    max_score: float
    correct_answer: str
    selected_option_id: int | None
    free_response_text: str | None
    explanations: list[ExplanationRead] = []
    options: list[QuestionOptionRead] = []
    rubric: list[RubricCriterionRead] = []


class PracticeResultsResponse(BaseModel):
    graded_count: int | None = None
    self_review_count: int = 0
    session_id: int
    session_type: str
    correct_count: int
    total_questions: int
    score: float
    breakdown: list[AnswerBreakdownItem]
    xp_earned: int = 0
    newly_earned_badges: list[BadgeRead] = []
