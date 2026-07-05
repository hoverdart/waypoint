"""Admin CRUD for units/topics. Deliberately Create/Read/Update only - no
delete - since these are structural rows referenced by mastery, questions,
and planner state; removing one out from under existing user data is a rare,
dangerous operation well outside MVP scope.
"""

from sqlmodel import Session, select

from app.core.exceptions import NotFoundError
from app.models.subject import Topic, Unit
from app.schemas.admin import AdminTopicCreate, AdminTopicUpdate, AdminUnitCreate, AdminUnitUpdate


def list_units(db: Session, subject_id: int) -> list[Unit]:
    return list(db.exec(select(Unit).where(Unit.subject_id == subject_id)).all())


def create_unit(db: Session, subject_id: int, data: AdminUnitCreate) -> Unit:
    unit = Unit(subject_id=subject_id, **data.model_dump())
    db.add(unit)
    db.flush()
    return unit


def get_unit(db: Session, unit_id: int) -> Unit:
    unit = db.get(Unit, unit_id)
    if unit is None:
        raise NotFoundError(f"Unit {unit_id} not found")
    return unit


def update_unit(db: Session, unit_id: int, data: AdminUnitUpdate) -> Unit:
    unit = get_unit(db, unit_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(unit, key, value)
    db.add(unit)
    return unit


def list_topics(db: Session, unit_id: int) -> list[Topic]:
    return list(db.exec(select(Topic).where(Topic.unit_id == unit_id)).all())


def create_topic(db: Session, unit_id: int, data: AdminTopicCreate) -> Topic:
    topic = Topic(unit_id=unit_id, **data.model_dump())
    db.add(topic)
    db.flush()
    return topic


def get_topic(db: Session, topic_id: int) -> Topic:
    topic = db.get(Topic, topic_id)
    if topic is None:
        raise NotFoundError(f"Topic {topic_id} not found")
    return topic


def update_topic(db: Session, topic_id: int, data: AdminTopicUpdate) -> Topic:
    topic = get_topic(db, topic_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(topic, key, value)
    db.add(topic)
    return topic
