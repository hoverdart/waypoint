"""Builds QuestionRead response objects with their options attached. Built
explicitly (rather than mutating the Question ORM instance) because SQLModel
table models are Pydantic models under the hood and reject assignment of
attributes that aren't declared fields.
"""

from sqlmodel import Session, select

from app.models.question import Question, QuestionOption
from app.schemas.practice import QuestionOptionRead, QuestionRead


def questions_to_reads(db: Session, questions: list[Question]) -> list[QuestionRead]:
    if not questions:
        return []
    question_ids = [q.id for q in questions]
    options_by_question: dict[int, list[QuestionOption]] = {}
    for opt in db.exec(select(QuestionOption).where(QuestionOption.question_id.in_(question_ids))).all():
        options_by_question.setdefault(opt.question_id, []).append(opt)

    return [
        QuestionRead(
            id=q.id,
            subject_id=q.subject_id,
            unit_id=q.unit_id,
            topic_id=q.topic_id,
            type=q.type,
            difficulty=q.difficulty,
            prompt=q.prompt,
            options=[
                QuestionOptionRead(id=o.id, label=o.label, text=o.text)
                for o in options_by_question.get(q.id, [])
            ],
        )
        for q in questions
    ]
