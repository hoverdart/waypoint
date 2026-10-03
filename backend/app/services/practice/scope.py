"""Validate the active curriculum scope before creating a study session."""

from sqlmodel import Session

from app.core.exceptions import DomainError, NotFoundError
from app.models.subject import Subject, Topic, Unit


def validate_practice_scope(
    db: Session, subject_id: int, unit_id: int | None = None, topic_id: int | None = None,
) -> None:
    subject = db.get(Subject, subject_id)
    if subject is None or not subject.is_active:
        raise NotFoundError("Course not found")
    if unit_id is not None:
        unit = db.get(Unit, unit_id)
        if unit is None or not unit.is_active or unit.subject_id != subject_id:
            raise DomainError("Unit does not belong to this active course")
    if topic_id is not None:
        topic = db.get(Topic, topic_id)
        unit = db.get(Unit, topic.unit_id) if topic else None
        if unit is None or not unit.is_active or unit.subject_id != subject_id:
            raise DomainError("Topic does not belong to this active course")
        if unit_id is not None and topic.unit_id != unit_id:
            raise DomainError("Topic does not belong to this unit")
