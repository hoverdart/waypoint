from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserRead, UserUpdate

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
