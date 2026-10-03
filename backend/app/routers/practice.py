from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.gamification import Badge
from app.models.practice import PracticeSession, QuestionAttempt
from app.models.subject import Subject
from app.models.planner import DailyPlan, DailyPlanItem
from app.core.exceptions import DomainError, NotFoundError
from app.services.practice.validation import validate_submission
from app.models.question import Question, QuestionExplanation, QuestionOption
from app.models.user import User
from app.schemas.gamification import BadgeRead
from app.schemas.practice import (
    AnswerBreakdownItem,
    SelfReviewRequest,
    SelfReviewRead,
    PracticeDraftRequest,
    PracticeHistoryItem,
    ExplanationRead,
    QuestionOptionRead,
    RubricCriterionRead,
    PracticeResultsResponse,
    PracticeSessionDetailResponse,
    PracticeStartRequest,
    PracticeStartResponse,
    PracticeSubmitRequest,
    PracticeSubmitResponse,
)
from app.services.practice.self_review import requires_self_review, save_self_review
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


@router.get("/practice", response_model=list[PracticeHistoryItem])
def list_practice_sessions(
    db: Session = Depends(get_db), user: User = Depends(get_current_user),
    limit: int = Query(default=30, ge=1, le=100), offset: int = Query(default=0, ge=0),
) -> list[PracticeHistoryItem]:
    rows = db.exec(
        select(PracticeSession, Subject.name)
        .join(Subject, Subject.id == PracticeSession.subject_id)
        .where(PracticeSession.user_id == user.id)
        .order_by(PracticeSession.started_at.desc(), PracticeSession.id.desc())
        .offset(offset).limit(limit)
    ).all()
    return [PracticeHistoryItem(
        session_id=s.id, subject_id=s.subject_id, subject_name=name,
        session_type=s.session_type, started_at=s.started_at, completed_at=s.completed_at,
        total_questions=s.total_questions, correct_count=s.correct_count, score=s.score,
        graded_count=s.session_metadata.get("graded_count", s.total_questions),
        self_review_count=len(s.session_metadata.get("self_review_question_ids", [])),
        answered_count=s.total_questions if s.completed_at else sum(a.get("selected_option_id") is not None or bool((a.get("free_response_text") or "").strip()) for a in s.session_metadata.get("draft_answers", [])),
    ) for s, name in rows]


@router.patch("/practice/{session_id}/draft", status_code=204)
def save_practice_draft(
    session_id: int, payload: PracticeDraftRequest,
    db: Session = Depends(get_db), user: User = Depends(get_current_user),
) -> None:
    owned = _owned_session_or_404(db, session_id, user)
    session = validate_submission(
        db, session_id, [AnswerSubmission(**a.model_dump()) for a in payload.answers],
        diagnostic=owned.session_type == "diagnostic", partial=True,
    )
    if payload.current_index >= session.total_questions:
        raise DomainError("Question index is outside this session")
    if payload.daily_plan_item_id is not None:
        item = db.get(DailyPlanItem, payload.daily_plan_item_id)
        plan = db.get(DailyPlan, item.daily_plan_id) if item else None
        if plan is None or plan.user_id != user.id:
            raise NotFoundError("Plan item not found")
        if item.subject_id != session.subject_id or item.topic_id != session.topic_id:
            raise DomainError("Plan item does not match this practice session")
    session.session_metadata = {
        **session.session_metadata, "draft_answers": [a.model_dump() for a in payload.answers],
        "current_index": payload.current_index, "daily_plan_item_id": payload.daily_plan_item_id,
    }
    db.add(session)
    db.commit()


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
        draft_answers=session.session_metadata.get("draft_answers", []),
        current_index=session.session_metadata.get("current_index", 0),
        daily_plan_item_id=session.session_metadata.get("daily_plan_item_id"),
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

    if session.completed_at is None:
        raise HTTPException(status_code=409, detail="Finish this session before viewing results")
    attempts = db.exec(select(QuestionAttempt).where(QuestionAttempt.session_id == session_id).order_by(QuestionAttempt.id)).all()
    breakdown = []
    for attempt in attempts:
        question = db.get(Question, attempt.question_id)
        explanations = db.exec(
            select(QuestionExplanation).where(QuestionExplanation.question_id == question.id)
        ).all()
        breakdown.append(
            AnswerBreakdownItem(
                scoring_method="self_review" if requires_self_review(question) else "keyword" if question.type == "frq" else "automatic",
                self_review=session.session_metadata.get("self_reviews", {}).get(str(question.id)),
                question_id=question.id,
                topic_id=question.topic_id,
                prompt=question.prompt,
                type=question.type,
                is_correct=None if requires_self_review(question) else attempt.is_correct,
                score=None if requires_self_review(question) else attempt.score,
                max_score=attempt.max_score,
                correct_answer=question.correct_answer,
                selected_option_id=attempt.selected_option_id,
                free_response_text=attempt.free_response_text,
                explanations=[ExplanationRead.model_validate(e) for e in explanations],
                options=[QuestionOptionRead.model_validate(o) for o in db.exec(
                    select(QuestionOption).where(QuestionOption.question_id == question.id).order_by(QuestionOption.label)
                ).all()],
                rubric=[RubricCriterionRead(point=c.get("point", ""), points=c.get("points", 0), levels=c.get("levels", []))
                        for c in (question.rubric_json or {}).get("checklist", [])],
            )
        )

    newly_earned_badge_ids = session.session_metadata.get("newly_earned_badge_ids", [])
    newly_earned_badges = [
        BadgeRead.model_validate(b)
        for b in db.exec(select(Badge).where(Badge.id.in_(newly_earned_badge_ids))).all()
    ]

    return PracticeResultsResponse(
        graded_count=session.session_metadata.get("graded_count", session.total_questions),
        self_review_count=len(session.session_metadata.get("self_review_question_ids", [])),
        session_id=session.id,
        session_type=session.session_type,
        correct_count=session.correct_count,
        total_questions=session.total_questions,
        score=session.score,
        breakdown=breakdown,
        xp_earned=session.session_metadata.get("xp_earned", 0),
        newly_earned_badges=newly_earned_badges,
    )


@router.put("/practice/{session_id}/questions/{question_id}/self-review", response_model=SelfReviewRead)
def review_response(
    session_id: int, question_id: int, payload: SelfReviewRequest,
    db: Session = Depends(get_db), user: User = Depends(get_current_user),
) -> SelfReviewRead:
    review = save_self_review(db, user.id, session_id, question_id, payload.points)
    db.commit()
    return SelfReviewRead(**review)
