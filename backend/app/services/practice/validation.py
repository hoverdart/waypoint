"""Shared submission checks, performed before attempts or rewards are written."""
from sqlmodel import Session, select

from app.core.exceptions import ConflictError, DomainError, NotFoundError
from app.models.practice import PracticeSession
from app.models.question import Question, QuestionOption
from app.services.practice.types import AnswerSubmission


def validate_submission(
    db: Session, session_id: int, answers: list[AnswerSubmission], *, diagnostic: bool, partial: bool = False, allow_exam: bool = False
) -> PracticeSession:
    # Serialize competing submissions so a session can award mastery and XP only once.
    session = db.exec(
        select(PracticeSession).where(PracticeSession.id == session_id)
        .with_for_update().execution_options(populate_existing=True)
    ).first()
    if session is None:
        raise NotFoundError("Session not found")
    if "exam" in session.session_metadata and not allow_exam:
        raise ConflictError("Use the exam section controls for this session")
    if session.completed_at is not None:
        raise ConflictError("This session has already been submitted")
    if (session.session_type == "diagnostic") != diagnostic:
        raise DomainError("Use the matching submission endpoint for this session")
    expected = set(session.session_metadata.get("question_ids", []))
    actual = [answer.question_id for answer in answers]
    valid_set = set(actual).issubset(expected) if partial else set(actual) == expected
    if not expected or len(actual) != len(set(actual)) or not valid_set:
        raise DomainError("Submit exactly one answer for every question in this session")
    for answer in answers:
        question = db.get(Question, answer.question_id)
        if question is None or question.subject_id != session.subject_id:
            raise DomainError("Question does not belong to this session")
        if answer.selected_option_id is not None:
            option = db.get(QuestionOption, answer.selected_option_id)
            if question.type != "mcq" or option is None or option.question_id != question.id:
                raise DomainError("Selected option does not belong to this question")
    return session
