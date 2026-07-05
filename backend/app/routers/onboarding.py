from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.subject import UserSubject
from app.models.user import User
from app.schemas.onboarding import OnboardingRequest, OnboardingResponse

router = APIRouter(tags=["onboarding"])


@router.post("/onboarding", response_model=OnboardingResponse)
def onboard(
    payload: OnboardingRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> OnboardingResponse:
    user.mode = payload.mode
    db.add(user)

    user_subjects = []
    for sub_input in payload.subjects:
        existing = db.exec(
            select(UserSubject).where(
                UserSubject.user_id == user.id, UserSubject.subject_id == sub_input.subject_id
            )
        ).first()
        if existing is None:
            existing = UserSubject(user_id=user.id, subject_id=sub_input.subject_id)
        existing.target_score = sub_input.target_score
        existing.exam_date = sub_input.exam_date
        existing.study_minutes_per_day = sub_input.study_minutes_per_day
        existing.is_active = True
        db.add(existing)
        db.flush()
        user_subjects.append(existing)

    db.commit()
    db.refresh(user)
    return OnboardingResponse(user=user, user_subjects=user_subjects)
