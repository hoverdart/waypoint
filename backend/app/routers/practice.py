from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.gamification import Badge
from app.models.practice import QuestionAttempt
from app.models.question import Question, QuestionExplanation
from app.models.user import User
from app.schemas.gamification import BadgeRead
from app.schemas.practice import (
    AnswerBreakdownItem,
    ExplanationRead,
    PracticeResultsResponse,
    PracticeSessionDetailResponse,
    PracticeStartRequest,
    PracticeStartResponse,
    PracticeSubmitRequest,
    PracticeSubmitResponse,
)
from app.services.practice.question_presentation import questions_to_reads
from app.services.practice.session_service import (
    get_results,
    get_session_questions,
    start_practice_session,
    submit_practice_session,
)
from app.services.practice.types import AnswerSubmission

router = APIRouter(tags=["practice"])


@router.post("/practice/start", response_model=PracticeStartResponse)
def start_practice(
    payload: PracticeStartRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> PracticeStartResponse:
    session, questions = start_practice_session(
        db,
        user_id=user.id,
        subject_id=payload.subject_id,
        unit_id=payload.unit_id,
        topic_id=payload.topic_id,
        session_type=payload.session_type,
        question_count=payload.question_count,
    )
    question_reads = questions_to_reads(db, questions)
    db.commit()
    return PracticeStartResponse(
        session_id=session.id, session_type=session.session_type, questions=question_reads
    )


def _owned_session_or_404(db: Session, session_id: int, user: User):
    session = get_results(db, session_id)
    if session is None or session.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return session


@router.get("/practice/{session_id}", response_model=PracticeSessionDetailResponse)
def get_practice_session(
    session_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> PracticeSessionDetailResponse:
    """Reconstructs an in-progress (or just-completed) session's question set
    from `session_metadata` - a fresh page load has no other way to know
    which questions belong to this session_id."""
    session = _owned_session_or_404(db, session_id, user)
    questions = get_session_questions(db, session)
    return PracticeSessionDetailResponse(
        session_id=session.id,
        session_type=session.session_type,
        subject_id=session.subject_id,
        is_completed=session.completed_at is not None,
        questions=questions_to_reads(db, questions),
    )


@router.post("/practice/{session_id}/submit", response_model=PracticeSubmitResponse)
def submit_practice(
    session_id: int,
    payload: PracticeSubmitRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> PracticeSubmitResponse:
    _owned_session_or_404(db, session_id, user)
    answers = [AnswerSubmission(**a.model_dump()) for a in payload.answers]
    session = submit_practice_session(
        db, session_id, answers, daily_plan_item_id=payload.daily_plan_item_id
    )
    db.commit()
    return PracticeSubmitResponse(
        session_id=session.id,
        session_type=session.session_type,
        correct_count=session.correct_count,
        total_questions=session.total_questions,
        score=session.score,
    )


@router.get("/practice/{session_id}/results", response_model=PracticeResultsResponse)
def practice_results(
    session_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> PracticeResultsResponse:
    session = _owned_session_or_404(db, session_id, user)

    attempts = db.exec(select(QuestionAttempt).where(QuestionAttempt.session_id == session_id)).all()
    breakdown = []
    for attempt in attempts:
        question = db.get(Question, attempt.question_id)
        explanations = db.exec(
            select(QuestionExplanation).where(QuestionExplanation.question_id == question.id)
        ).all()
        breakdown.append(
            AnswerBreakdownItem(
                question_id=question.id,
                topic_id=question.topic_id,
                prompt=question.prompt,
                type=question.type,
                is_correct=attempt.is_correct,
                score=attempt.score,
                max_score=attempt.max_score,
                correct_answer=question.correct_answer,
                selected_option_id=attempt.selected_option_id,
                free_response_text=attempt.free_response_text,
                explanations=[ExplanationRead.model_validate(e) for e in explanations],
            )
        )

    newly_earned_badge_ids = session.session_metadata.get("newly_earned_badge_ids", [])
    newly_earned_badges = [
        BadgeRead.model_validate(b)
        for b in db.exec(select(Badge).where(Badge.id.in_(newly_earned_badge_ids))).all()
    ]

    return PracticeResultsResponse(
        session_id=session.id,
        session_type=session.session_type,
        correct_count=session.correct_count,
        total_questions=session.total_questions,
        score=session.score,
        breakdown=breakdown,
        xp_earned=session.session_metadata.get("xp_earned", 0),
        newly_earned_badges=newly_earned_badges,
    )
