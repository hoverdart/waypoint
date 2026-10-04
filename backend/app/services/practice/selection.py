"""Personalize ordinary MCQ practice using only the learner's completed work."""
from sqlalchemy import func
from sqlmodel import Session, select

from app.models.practice import PracticeSession, QuestionAttempt
from app.models.question import Question


def prioritize_mcq_candidates(db: Session, user_id: int, candidates: list[Question]) -> list[Question]:
    if not candidates:
        return candidates
    ranked = (
        select(
            QuestionAttempt.question_id,
            QuestionAttempt.is_correct,
            PracticeSession.completed_at,
            func.row_number().over(
                partition_by=QuestionAttempt.question_id,
                order_by=(PracticeSession.completed_at.desc(), QuestionAttempt.id.desc()),
            ).label('position'),
        )
        .join(PracticeSession, QuestionAttempt.session_id == PracticeSession.id)
        .where(
            QuestionAttempt.user_id == user_id,
            PracticeSession.user_id == user_id,
            PracticeSession.completed_at.is_not(None),
            QuestionAttempt.question_id.in_([q.id for q in candidates]),
        ).subquery()
    )
    latest = {
        row.question_id: row
        for row in db.exec(
            select(ranked.c.question_id, ranked.c.is_correct, ranked.c.completed_at)
            .where(ranked.c.position == 1)
        ).all()
    }

    def priority(question):
        previous = latest.get(question.id)
        if previous is None:
            return (1, 0)
        # Mistakes first; successful answers go behind unseen material. Within
        # reviewed groups, revisit the oldest completed work first. Stable sort
        # retains the caller's randomized order for ties and unseen questions.
        return (2 if previous.is_correct else 0, previous.completed_at)

    return sorted(candidates, key=priority)
