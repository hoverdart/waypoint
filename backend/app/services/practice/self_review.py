"""Owned, post-submission rubric reflection; never an automated mastery signal."""
from datetime import datetime, timezone

from sqlmodel import Session, select

from app.core.exceptions import ConflictError, DomainError, NotFoundError
from app.models.practice import PracticeSession, QuestionAttempt
from app.models.question import Question


def requires_self_review(question: Question) -> bool:
    return question.type == "frq" and (question.rubric_json or {}).get("scoring_method") == "self_review"


def save_self_review(db: Session, user_id: int, session_id: int, question_id: int, points: list[int]) -> dict:
    # The session lock serializes edits of its JSON metadata, including reviews
    # for different questions in the same session, preventing lost updates.
    session = db.exec(select(PracticeSession).where(
        PracticeSession.id == session_id, PracticeSession.user_id == user_id
    ).with_for_update().execution_options(populate_existing=True)).first()
    if session is None:
        raise NotFoundError("Session not found")
    if session.completed_at is None:
        raise ConflictError("Submit your response before reviewing its rubric")
    attempt = db.exec(select(QuestionAttempt).where(
        QuestionAttempt.session_id == session_id,
        QuestionAttempt.question_id == question_id,
        QuestionAttempt.user_id == user_id,
    )).first()
    question = db.get(Question, question_id)
    if attempt is None or question is None:
        raise NotFoundError("Response not found")
    if not requires_self_review(question):
        raise DomainError("This response does not use rubric self-review")
    criteria = question.rubric_json["checklist"]
    if len(points) != len(criteria) or any(type(p) is not int or p < 0 or p > c["points"] for p, c in zip(points, criteria)):
        raise DomainError("Choose a valid whole-number score for every rubric row")
    review = {"points": points, "total": sum(points), "reviewed_at": datetime.now(timezone.utc).isoformat()}
    session.session_metadata = {
        **session.session_metadata,
        "self_reviews": {**session.session_metadata.get("self_reviews", {}), str(question_id): review},
    }
    db.add(session)
    db.flush()
    return review
