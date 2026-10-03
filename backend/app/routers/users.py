from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserRead, UserUpdate

from app.models.subject import UserSubject
from app.schemas.subject import UserSubjectRead
from app.schemas.onboarding import SubjectPreferencesRequest
from app.services.auth.subject_preferences import save_subject_preferences

router = APIRouter(tags=["users"])


@router.get("/users/me", response_model=UserRead)
def get_me(user: User = Depends(get_current_user)) -> User:
    return user


@router.patch("/users/me", response_model=UserRead)
def update_me(
    payload: UserUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> User:
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/users/me/subjects", response_model=list[UserSubjectRead])
def my_subjects(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return list(db.exec(select(UserSubject).where(UserSubject.user_id == user.id, UserSubject.is_active == True)).all())


@router.patch("/users/me/subjects", response_model=list[UserSubjectRead])
def update_subjects(payload: SubjectPreferencesRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    rows = save_subject_preferences(db, user.id, payload.subjects, replace=True)
    db.commit()
    return rows
