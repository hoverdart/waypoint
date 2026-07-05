from pydantic import BaseModel, ConfigDict

from app.schemas.gamification import BadgeRead


class AnswerInput(BaseModel):
    question_id: int
    selected_option_id: int | None = None
    free_response_text: str | None = None
    time_seconds: int = 0
    hints_used: int = 0
    explanation_opened: bool = False
    confidence_rating: int | None = None


class QuestionOptionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    label: str
    text: str


class QuestionRead(BaseModel):
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


class PracticeStartRequest(BaseModel):
    subject_id: int
    unit_id: int | None = None
    topic_id: int | None = None
    session_type: str = "mcq"
    question_count: int = 12


class PracticeStartResponse(BaseModel):
    session_id: int
    session_type: str
    questions: list[QuestionRead]


class PracticeSubmitRequest(BaseModel):
    answers: list[AnswerInput]
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


class AnswerBreakdownItem(BaseModel):
    question_id: int
    prompt: str
    type: str
    is_correct: bool
    score: float
    max_score: float
    correct_answer: str
    selected_option_id: int | None
    free_response_text: str | None
    explanations: list[ExplanationRead] = []


class PracticeResultsResponse(BaseModel):
    session_id: int
    session_type: str
    correct_count: int
    total_questions: int
    score: float
    breakdown: list[AnswerBreakdownItem]
    xp_earned: int = 0
    newly_earned_badges: list[BadgeRead] = []
