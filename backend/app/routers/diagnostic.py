from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.config import Settings, get_settings
from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.diagnostic import (
    DiagnosticStartRequest,
    DiagnosticStartResponse,
    DiagnosticSubmitRequest,
    DiagnosticSubmitResponse,
)
from app.services.diagnostic.diagnostic_builder import build_diagnostic_session
from app.services.diagnostic.diagnostic_scorer import score_diagnostic
from app.services.practice.question_presentation import questions_to_reads
from app.services.practice.types import AnswerSubmission

router = APIRouter(tags=["diagnostic"])


@router.post("/diagnostic/start", response_model=DiagnosticStartResponse)
def start_diagnostic(
    payload: DiagnosticStartRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    settings: Settings = Depends(get_settings),
) -> DiagnosticStartResponse:
    session, questions = build_diagnostic_session(
        db, user.id, payload.subject_id, settings.diagnostic_question_count
    )
    question_reads = questions_to_reads(db, questions)
    db.commit()
    return DiagnosticStartResponse(
        session_id=session.id, session_type=session.session_type, questions=question_reads
    )


@router.post("/diagnostic/{session_id}/submit", response_model=DiagnosticSubmitResponse)
def submit_diagnostic(
    session_id: int,
    payload: DiagnosticSubmitRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> DiagnosticSubmitResponse:
    answers = [AnswerSubmission(**a.model_dump()) for a in payload.answers]
    session = score_diagnostic(db, session_id, answers)
    db.commit()
    return DiagnosticSubmitResponse(
        session_id=session.id,
        correct_count=session.correct_count,
        total_questions=session.total_questions,
        score=session.score,
    )
