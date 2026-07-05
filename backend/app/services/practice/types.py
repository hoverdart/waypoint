from dataclasses import dataclass


@dataclass
class AnswerSubmission:
    """One student answer to one question, shared shape for both diagnostic
    and regular practice submission flows."""

    question_id: int
    selected_option_id: int | None = None
    free_response_text: str | None = None
    time_seconds: int = 0
    hints_used: int = 0
    explanation_opened: bool = False
    confidence_rating: int | None = None
