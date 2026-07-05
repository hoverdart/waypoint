from sqlmodel import Session, select

from app.core.exceptions import ConflictError, NotFoundError
from app.models.question import Question, QuestionExplanation, QuestionOption
from app.models.reports import QuestionReport
from app.schemas.admin import AdminExplanationInput, AdminQuestionCreate, AdminQuestionOptionInput, AdminQuestionUpdate

# A question can't jump straight from rejected back to approved - it must pass
# through needs_review first, so a human re-confirms the fix actually landed.
ALLOWED_STATUS_TRANSITIONS: dict[str, set[str]] = {
    "draft": {"approved", "rejected", "needs_review"},
    "needs_review": {"approved", "rejected"},
    "approved": {"needs_review", "rejected"},
    "rejected": {"needs_review"},
}


def list_questions(
    db: Session,
    subject_id: int | None = None,
    validation_status: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[Question]:
    query = select(Question)
    if subject_id is not None:
        query = query.where(Question.subject_id == subject_id)
    if validation_status is not None:
        query = query.where(Question.validation_status == validation_status)
    query = query.order_by(Question.id).offset(offset).limit(limit)
    return list(db.exec(query).all())


def get_question(db: Session, question_id: int) -> Question:
    question = db.get(Question, question_id)
    if question is None:
        raise NotFoundError(f"Question {question_id} not found")
    return question


def _replace_options_and_explanations(
    db: Session,
    question: Question,
    options_data: list[AdminQuestionOptionInput],
    explanations_data: list[AdminExplanationInput],
) -> None:
    for option in db.exec(select(QuestionOption).where(QuestionOption.question_id == question.id)).all():
        db.delete(option)
    for explanation in db.exec(
        select(QuestionExplanation).where(QuestionExplanation.question_id == question.id)
    ).all():
        db.delete(explanation)
    db.flush()

    option_by_label = {}
    for opt in options_data:
        option = QuestionOption(
            question_id=question.id, label=opt.label, text=opt.text, is_correct=opt.is_correct
        )
        db.add(option)
        db.flush()
        option_by_label[opt.label] = option

    for exp in explanations_data:
        option_id = option_by_label[exp.option_label].id if exp.option_label else None
        db.add(
            QuestionExplanation(
                question_id=question.id,
                option_id=option_id,
                explanation=exp.explanation,
                misconception_tag=exp.misconception_tag,
            )
        )


def create_question(db: Session, data: AdminQuestionCreate) -> Question:
    question = Question(
        subject_id=data.subject_id,
        unit_id=data.unit_id,
        topic_id=data.topic_id,
        type=data.type,
        difficulty=data.difficulty,
        prompt=data.prompt,
        correct_answer=data.correct_answer,
        rubric_json=data.rubric_json,
        skill_tags=data.skill_tags,
        misconception_tags=data.misconception_tags,
        source=data.source,
        validation_status=data.validation_status,
    )
    db.add(question)
    db.flush()
    _replace_options_and_explanations(db, question, data.options, data.explanations)
    return question


def update_question(db: Session, question_id: int, data: AdminQuestionUpdate) -> Question:
    question = get_question(db, question_id)
    for key, value in data.model_dump(exclude_unset=True, exclude={"options", "explanations"}).items():
        setattr(question, key, value)
    question.version += 1
    db.add(question)
    db.flush()
    if data.options is not None:
        _replace_options_and_explanations(db, question, data.options, data.explanations or [])
    return question


def transition_validation_status(db: Session, question_id: int, new_status: str) -> Question:
    question = get_question(db, question_id)
    if new_status != question.validation_status and new_status not in ALLOWED_STATUS_TRANSITIONS.get(
        question.validation_status, set()
    ):
        raise ConflictError(
            f"Cannot transition question from '{question.validation_status}' to '{new_status}'"
        )
    question.validation_status = new_status
    db.add(question)
    return question


def deactivate_question(db: Session, question_id: int) -> Question:
    question = get_question(db, question_id)
    question.is_active = False
    db.add(question)
    return question


def list_reports_for_question(db: Session, question_id: int) -> list[QuestionReport]:
    return list(db.exec(select(QuestionReport).where(QuestionReport.question_id == question_id)).all())
