from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_db
from app.dependencies import get_current_user
from app.services.auth.subject_preferences import save_subject_preferences
from app.models.user import User
from app.schemas.onboarding import OnboardingRequest, OnboardingResponse

router = APIRouter(tags=["onboarding"])


@router.post("/onboarding", response_model=OnboardingResponse)
def onboard(
    payload: OnboardingRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> OnboardingResponse:
    user.mode = payload.mode
    db.add(user)

    user_subjects = save_subject_preferences(db, user.id, payload.subjects)

    db.commit()
    db.refresh(user)
    return OnboardingResponse(user=user, user_subjects=user_subjects)
