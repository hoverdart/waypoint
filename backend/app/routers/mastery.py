from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.mastery import SubjectMastery, TopicMastery, UnitMastery
from app.models.subject import Subject, Topic, Unit
from app.models.user import User
from app.schemas.mastery import SubjectMasteryResponse, TopicMasteryRead, UnitMasteryRead

router = APIRouter(tags=["mastery"])


@router.get("/mastery/subject/{subject_id}", response_model=SubjectMasteryResponse)
def get_subject_mastery(
    subject_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> SubjectMasteryResponse:
    subject = db.get(Subject, subject_id)
    if subject is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")

    subject_mastery = db.get(SubjectMastery, (user.id, subject_id))
    units = list(
        db.exec(select(Unit).where(Unit.subject_id == subject_id).order_by(Unit.display_order)).all()
    )

    unit_reads = []
    for unit in units:
        unit_mastery = db.get(UnitMastery, (user.id, unit.id))
        topics = list(
            db.exec(select(Topic).where(Topic.unit_id == unit.id).order_by(Topic.display_order)).all()
        )
        topic_reads = []
        for topic in topics:
            tm = db.get(TopicMastery, (user.id, topic.id))
            topic_reads.append(
                TopicMasteryRead(
                    topic_id=topic.id,
                    topic_name=topic.name,
                    mastery_score=tm.mastery_score if tm else 0.0,
                    confidence_score=tm.confidence_score if tm else 0.0,
                    retention_score=tm.retention_score if tm else 1.0,
                    topic_timer=tm.topic_timer if tm else 0.0,
                    attempts_count=tm.attempts_count if tm else 0,
                    last_practiced_at=tm.last_practiced_at if tm else None,
                )
            )
        unit_reads.append(
            UnitMasteryRead(
                unit_id=unit.id,
                unit_name=unit.name,
                mastery_score=unit_mastery.mastery_score if unit_mastery else 0.0,
                confidence_score=unit_mastery.confidence_score if unit_mastery else 0.0,
                topics=topic_reads,
            )
        )

    return SubjectMasteryResponse(
        subject_id=subject.id,
        subject_name=subject.name,
        mastery_score=subject_mastery.mastery_score if subject_mastery else 0.0,
        confidence_score=subject_mastery.confidence_score if subject_mastery else 0.0,
        predicted_ap_score=subject_mastery.predicted_ap_score if subject_mastery else 1,
        units=unit_reads,
    )
