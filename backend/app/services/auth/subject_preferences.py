"""Update enrollments without deleting practice or mastery history."""
from sqlmodel import Session, select

from app.core.exceptions import DomainError
from app.models.subject import Subject, UserSubject
from app.models.user import User
from app.schemas.onboarding import OnboardingSubjectInput


def save_subject_preferences(db: Session, user_id: int, subjects: list[OnboardingSubjectInput], *, replace: bool = False) -> list[UserSubject]:
    db.exec(select(User).where(User.id == user_id).with_for_update()).one()
    ids = [s.subject_id for s in subjects]
    available = set(db.exec(select(Subject.id).where(Subject.id.in_(ids), Subject.is_active == True)).all())
    if available != set(ids):
        raise DomainError("Choose active courses from the course catalog")
    existing = {s.subject_id: s for s in db.exec(select(UserSubject).where(UserSubject.user_id == user_id)).all()}
    if replace:
        for subject_id, row in existing.items():
            if subject_id not in ids:
                row.is_active = False
                db.add(row)
    selected = []
    for value in subjects:
        row = existing.get(value.subject_id) or UserSubject(user_id=user_id, subject_id=value.subject_id)
        for key, field in value.model_dump().items():
            setattr(row, key, field)
        row.is_active = True
        db.add(row)
        selected.append(row)
    db.flush()
    return selected
