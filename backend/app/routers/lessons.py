from dataclasses import asdict
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.dialects.postgresql import insert
from sqlmodel import Session, select

from app.content.lessons import lessons_for
from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.lesson import LessonCompletion
from app.models.subject import Subject, Topic, Unit
from app.models.question import Question
from app.models.user import User

router = APIRouter(tags=["lessons"])


class CheckAnswer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    option: int = Field(ge=0, le=2, strict=True)
    revision: int = Field(ge=1, strict=True)


def unit_lessons(db, unit_id):
    unit = db.get(Unit, unit_id)
    subject = db.get(Subject, unit.subject_id) if unit else None
    if not unit or not unit.is_active or not subject or not subject.is_active:
        raise HTTPException(404, "Unit not found")
    return lessons_for(subject.ap_exam_code, unit.display_order)


@router.get("/units/{unit_id}/lessons")
def get_lessons(unit_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    lessons = unit_lessons(db, unit_id)
    completed = {(row.lesson_slug, row.revision) for row in db.exec(
        select(LessonCompletion).where(LessonCompletion.user_id == user.id, LessonCompletion.unit_id == unit_id)
    ).all()}
    topics = db.exec(select(Topic).where(Topic.unit_id == unit_id).order_by(Topic.display_order, Topic.id)).all()
    unit = db.get(Unit, unit_id)
    available = set(db.exec(select(Question.topic_id, Question.type).where(
        Question.unit_id == unit_id,
        Question.subject_id == unit.subject_id,
        Question.is_active == True,
        Question.validation_status == "approved",
    ).distinct()).all())

    def practice_targets(lesson):
        tag = lesson.practice_tag or f"ap-skill:{lesson.skill}"
        matching = [topic for topic in topics if tag in topic.skill_tags]
        return {kind: next((topic.id for topic in matching if (topic.id, kind) in available), None)
                for kind in ("mcq", "frq")}

    return [{**{key: value for key, value in asdict(lesson).items() if key not in ("correct", "feedback", "practice_tag")},
             "completed": (lesson.slug, lesson.revision) in completed,
             "practice_topic_ids": practice_targets(lesson)} for lesson in lessons]


@router.post("/units/{unit_id}/lessons/{slug}/check")
def check_lesson(unit_id: int, slug: str, payload: CheckAnswer,
                 db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    lesson = next((item for item in unit_lessons(db, unit_id) if item.slug == slug), None)
    if lesson is None:
        raise HTTPException(404, "Lesson not found")
    if payload.revision != lesson.revision:
        raise HTTPException(409, "This lesson has changed. Reload it before checking your answer.")
    correct = payload.option == lesson.correct
    if correct:
        db.execute(insert(LessonCompletion).values(user_id=user.id, unit_id=unit_id,
            lesson_slug=slug, revision=lesson.revision, completed_at=datetime.now(timezone.utc))
            .on_conflict_do_nothing())
        db.commit()
    return {"correct": correct, "feedback": lesson.feedback[payload.option]}
