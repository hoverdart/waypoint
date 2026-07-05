from fastapi import APIRouter, Depends

from app.dependencies import sync_current_user
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter(tags=["auth"])


@router.post("/auth/sync-user", response_model=UserRead)
def sync_user(user: User = Depends(sync_current_user)) -> User:
    return user
