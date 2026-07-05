from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.question import Question
from app.models.reports import QuestionReport
from app.models.user import User
from app.schemas.reports import QuestionReportRead, QuestionReportRequest

router = APIRouter(tags=["question-reports"])


@router.post("/questions/{question_id}/report", response_model=QuestionReportRead)
def report_question(
    question_id: int,
    payload: QuestionReportRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> QuestionReport:
    question = db.get(Question, question_id)
    if question is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    report = QuestionReport(
        user_id=user.id, question_id=question_id, reason=payload.reason, details=payload.details
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report
