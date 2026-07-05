from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.session import get_db
from app.models.subject import Subject, Topic, Unit
from app.schemas.subject import SubjectDetailRead, SubjectRead, TopicRead, UnitRead, UnitWithTopicsRead

router = APIRouter(tags=["subjects"])


@router.get("/subjects", response_model=list[SubjectRead])
def list_subjects(db: Session = Depends(get_db)) -> list[Subject]:
    return list(
        db.exec(
            select(Subject).where(Subject.is_active == True).order_by(Subject.display_order)  # noqa: E712
        ).all()
    )


@router.get("/subjects/{subject_id}", response_model=SubjectDetailRead)
def get_subject(subject_id: int, db: Session = Depends(get_db)) -> SubjectDetailRead:
    subject = db.get(Subject, subject_id)
    if subject is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")

    units = list(
        db.exec(select(Unit).where(Unit.subject_id == subject_id).order_by(Unit.display_order)).all()
    )
    unit_reads = []
    for unit in units:
        topics = list(
            db.exec(select(Topic).where(Topic.unit_id == unit.id).order_by(Topic.display_order)).all()
        )
        unit_reads.append(
            UnitWithTopicsRead(
                **UnitRead.model_validate(unit).model_dump(),
                topics=[TopicRead.model_validate(t) for t in topics],
            )
        )

    return SubjectDetailRead(**SubjectRead.model_validate(subject).model_dump(), units=unit_reads)
