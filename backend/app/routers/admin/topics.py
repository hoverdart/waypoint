from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_db
from app.dependencies import require_admin
from app.models.user import User
from app.schemas.admin import AdminTopicCreate, AdminTopicUpdate
from app.schemas.subject import TopicRead
from app.services.admin import curriculum_service

router = APIRouter(prefix="/admin/topics", tags=["admin"])


@router.get("", response_model=list[TopicRead])
def list_topics(unit_id: int, db: Session = Depends(get_db), _admin: User = Depends(require_admin)):
    return curriculum_service.list_topics(db, unit_id)


@router.post("", response_model=TopicRead)
def create_topic(
    unit_id: int,
    payload: AdminTopicCreate,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    topic = curriculum_service.create_topic(db, unit_id, payload)
    db.commit()
    db.refresh(topic)
    return topic


@router.patch("/{topic_id}", response_model=TopicRead)
def update_topic(
    topic_id: int,
    payload: AdminTopicUpdate,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    topic = curriculum_service.update_topic(db, topic_id, payload)
    db.commit()
    db.refresh(topic)
    return topic
