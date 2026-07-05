"""Idempotent seed script: upserts the 6 priority AP subjects, their
College-Board-weighted units/topics, and a demo-scale question bank.

Safe to re-run - subjects/units/topics are matched by natural key (ap_exam_code,
then name within parent), and questions are matched by (topic_id, prompt).

Usage: python -m scripts.seed
"""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlmodel import Session, select

from app.db.session import engine
from app.models.gamification import Badge
from app.models.question import Question, QuestionExplanation, QuestionOption
from app.models.subject import Subject, Topic, Unit
from scripts.seed_data.badges import BADGES
from scripts.seed_data.subjects import SUBJECTS

SUBJECT_MODULES = {
    "calculus-ab": ("units_topics.calculus_ab", "questions.calculus_ab_questions"),
    "biology": ("units_topics.biology", "questions.biology_questions"),
    "psychology": ("units_topics.psychology", "questions.psychology_questions"),
    "us-history": ("units_topics.us_history", "questions.us_history_questions"),
    "chemistry": ("units_topics.chemistry", "questions.chemistry_questions"),
    "computer-science-a": (
        "units_topics.computer_science_a",
        "questions.computer_science_a_questions",
    ),
}


def upsert_subject(db: Session, data: dict) -> Subject:
    subject = db.exec(select(Subject).where(Subject.ap_exam_code == data["ap_exam_code"])).first()
    if subject is None:
        subject = Subject(**data, is_active=True)
        db.add(subject)
    else:
        for key, value in data.items():
            setattr(subject, key, value)
    db.flush()
    return subject


def upsert_unit(db: Session, subject_id: int, data: dict) -> Unit:
    unit = db.exec(
        select(Unit).where(Unit.subject_id == subject_id, Unit.name == data["name"])
    ).first()
    if unit is None:
        unit = Unit(subject_id=subject_id, **data)
        db.add(unit)
    else:
        for key, value in data.items():
            setattr(unit, key, value)
    db.flush()
    return unit


def upsert_topic(db: Session, unit_id: int, data: dict) -> Topic:
    topic = db.exec(
        select(Topic).where(Topic.unit_id == unit_id, Topic.name == data["name"])
    ).first()
    if topic is None:
        topic = Topic(unit_id=unit_id, **data)
        db.add(topic)
    else:
        for key, value in data.items():
            setattr(topic, key, value)
    db.flush()
    return topic


def upsert_question(db: Session, subject_id: int, unit_id: int, topic_id: int, data: dict) -> Question:
    existing = db.exec(
        select(Question).where(Question.topic_id == topic_id, Question.prompt == data["prompt"])
    ).first()

    fields = dict(
        subject_id=subject_id,
        unit_id=unit_id,
        topic_id=topic_id,
        type=data["type"],
        difficulty=data["difficulty"],
        prompt=data["prompt"],
        correct_answer=data["correct_answer"],
        rubric_json=data.get("rubric_json"),
        skill_tags=data.get("skill_tags", []),
        misconception_tags=data.get("misconception_tags", []),
        source=data.get("source", "human_written"),
        validation_status=data.get("validation_status", "draft"),
        is_active=True,
    )

    if existing is None:
        question = Question(**fields)
        db.add(question)
        db.flush()
    else:
        question = existing
        for key, value in fields.items():
            setattr(question, key, value)
        db.flush()
        # Explanations have no downstream FK dependents, so delete+recreate is
        # safe. Options do (question_attempts.selected_option_id) once a real
        # user has practiced this question, so those are upserted in place by
        # label instead - deleting them would break re-seeding permanently.
        for explanation in db.exec(
            select(QuestionExplanation).where(QuestionExplanation.question_id == question.id)
        ).all():
            db.delete(explanation)
        db.flush()

    existing_options = {
        o.label: o
        for o in db.exec(select(QuestionOption).where(QuestionOption.question_id == question.id)).all()
    }
    option_by_label = {}
    seen_labels = set()
    for opt_data in data.get("options", []):
        label = opt_data["label"]
        seen_labels.add(label)
        option = existing_options.get(label)
        if option is None:
            option = QuestionOption(question_id=question.id, label=label, text=opt_data["text"], is_correct=opt_data["is_correct"])
            db.add(option)
        else:
            option.text = opt_data["text"]
            option.is_correct = opt_data["is_correct"]
        db.flush()
        option_by_label[label] = option
    for label, option in existing_options.items():
        if label not in seen_labels:
            db.delete(option)

    for exp_data in data.get("explanations", []):
        option_label = exp_data.get("option_label")
        option_id = option_by_label[option_label].id if option_label else None
        db.add(
            QuestionExplanation(
                question_id=question.id,
                option_id=option_id,
                explanation=exp_data["explanation"],
                misconception_tag=exp_data.get("misconception_tag"),
            )
        )

    return question


def seed_subject(db: Session, subject_data: dict) -> None:
    subject = upsert_subject(db, subject_data)
    code = subject_data["ap_exam_code"]
    units_module_name, questions_module_name = SUBJECT_MODULES[code]
    units_module = importlib.import_module(f"scripts.seed_data.{units_module_name}")
    questions_module = importlib.import_module(f"scripts.seed_data.{questions_module_name}")

    unit_by_name: dict[str, Unit] = {}
    topic_by_key: dict[tuple[str, str], Topic] = {}

    for unit_data in units_module.UNITS:
        topics_data = unit_data.get("topics", [])
        unit_fields = {k: v for k, v in unit_data.items() if k != "topics"}
        unit = upsert_unit(db, subject.id, unit_fields)
        unit_by_name[unit.name] = unit
        for topic_data in topics_data:
            topic = upsert_topic(db, unit.id, topic_data)
            topic_by_key[(unit.name, topic.name)] = topic

    question_count = 0
    for q_data in questions_module.QUESTIONS:
        unit = unit_by_name.get(q_data["unit_name"])
        if unit is None:
            print(f"  WARNING [{code}]: unknown unit_name {q_data['unit_name']!r}, skipping question")
            continue
        topic = topic_by_key.get((q_data["unit_name"], q_data["topic_name"]))
        if topic is None:
            print(
                f"  WARNING [{code}]: unknown topic_name {q_data['topic_name']!r} "
                f"under unit {q_data['unit_name']!r}, skipping question"
            )
            continue
        upsert_question(db, subject.id, unit.id, topic.id, q_data)
        question_count += 1

    print(
        f"  {subject.name}: {len(unit_by_name)} units, {len(topic_by_key)} topics, "
        f"{question_count} questions"
    )


def upsert_badge(db: Session, data: dict) -> Badge:
    badge = db.exec(select(Badge).where(Badge.name == data["name"])).first()
    if badge is None:
        badge = Badge(**data)
        db.add(badge)
    else:
        for key, value in data.items():
            setattr(badge, key, value)
    db.flush()
    return badge


def main() -> None:
    with Session(engine) as db:
        print("Seeding AP subjects...")
        for subject_data in SUBJECTS:
            seed_subject(db, subject_data)
        print("Seeding badges...")
        for badge_data in BADGES:
            upsert_badge(db, badge_data)
        db.commit()
        print("Seed complete.")


if __name__ == "__main__":
    main()
