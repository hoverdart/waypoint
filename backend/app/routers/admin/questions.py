from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import require_admin
from app.models.question import QuestionOption
from app.models.user import User
from app.schemas.admin import (
    AdminQuestionCreate,
    AdminQuestionDetailRead,
    AdminQuestionOptionInput,
    AdminQuestionRead,
    AdminQuestionUpdate,
    QuestionStatusUpdateRequest,
)
from app.schemas.reports import QuestionReportRead
from app.services.admin import question_service

router = APIRouter(prefix="/admin/questions", tags=["admin"])


@router.get("", response_model=list[AdminQuestionRead])
def list_questions(
    subject_id: int | None = None,
    validation_status: str | None = None,
    limit: int = Query(default=50, le=200),
    offset: int = 0,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    return question_service.list_questions(db, subject_id, validation_status, limit, offset)


@router.post("", response_model=AdminQuestionRead)
def create_question(
    payload: AdminQuestionCreate, db: Session = Depends(get_db), _admin: User = Depends(require_admin)
):
    question = question_service.create_question(db, payload)
    db.commit()
    db.refresh(question)
    return question


@router.get("/{question_id}", response_model=AdminQuestionDetailRead)
def get_question(question_id: int, db: Session = Depends(get_db), _admin: User = Depends(require_admin)):
    question = question_service.get_question(db, question_id)
    options = db.exec(select(QuestionOption).where(QuestionOption.question_id == question_id)).all()
    reports = question_service.list_reports_for_question(db, question_id)
    return AdminQuestionDetailRead(
        **AdminQuestionRead.model_validate(question).model_dump(),
        options=[
            AdminQuestionOptionInput(label=o.label, text=o.text, is_correct=o.is_correct) for o in options
        ],
        reports=[QuestionReportRead.model_validate(r) for r in reports],
    )


@router.patch("/{question_id}", response_model=AdminQuestionRead)
def update_question(
    question_id: int,
    payload: AdminQuestionUpdate,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    question = question_service.update_question(db, question_id, payload)
    db.commit()
    db.refresh(question)
    return question


@router.post("/{question_id}/status", response_model=AdminQuestionRead)
def update_status(
    question_id: int,
    payload: QuestionStatusUpdateRequest,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    question = question_service.transition_validation_status(db, question_id, payload.status)
    db.commit()
    db.refresh(question)
    return question


@router.delete("/{question_id}", response_model=AdminQuestionRead)
def deactivate_question(
    question_id: int, db: Session = Depends(get_db), _admin: User = Depends(require_admin)
):
    question = question_service.deactivate_question(db, question_id)
    db.commit()
    db.refresh(question)
    return question
