"""Small hand-rolled test data builders - the schema is compact enough that a
dependency like factory-boy isn't justified."""

from app.models.question import Question, QuestionExplanation, QuestionOption
from app.models.subject import Subject, Topic, Unit
from app.models.user import User


def make_user(db, auth_provider_id="test-user", email="test@example.com"):
    user = User(auth_provider_id=auth_provider_id, email=email)
    db.add(user)
    db.flush()
    return user


def make_subject_with_units_topics(db, name="AP Calculus AB", code="calculus-ab", n_units=2, n_topics_per_unit=2):
    subject = Subject(name=name, ap_exam_code=code)
    db.add(subject)
    db.flush()

    units = []
    for u in range(n_units):
        unit = Unit(
            subject_id=subject.id,
            name=f"Unit {u + 1}",
            ap_weight_min=10.0 + u * 5,
            ap_weight_max=15.0 + u * 5,
            display_order=u,
        )
        db.add(unit)
        db.flush()
        topics = []
        for t in range(n_topics_per_unit):
            topic = Topic(unit_id=unit.id, name=f"Unit {u + 1} Topic {t + 1}", display_order=t)
            db.add(topic)
            db.flush()
            topics.append(topic)
        units.append((unit, topics))

    return subject, units


def make_mcq_question(db, subject_id, unit_id, topic_id, correct_label="B", difficulty=3, validation_status="approved"):
    question = Question(
        subject_id=subject_id,
        unit_id=unit_id,
        topic_id=topic_id,
        type="mcq",
        difficulty=difficulty,
        prompt="Sample MCQ prompt",
        correct_answer=correct_label,
        validation_status=validation_status,
    )
    db.add(question)
    db.flush()

    options = {}
    for label in ("A", "B", "C", "D"):
        option = QuestionOption(
            question_id=question.id, label=label, text=f"Option {label}", is_correct=label == correct_label
        )
        db.add(option)
        db.flush()
        options[label] = option
        db.add(
            QuestionExplanation(
                question_id=question.id,
                option_id=option.id,
                explanation=f"Explanation for {label}",
            )
        )

    return question, options


def make_frq_question(db, subject_id, unit_id, topic_id, checklist, difficulty=3, validation_status="approved"):
    question = Question(
        subject_id=subject_id,
        unit_id=unit_id,
        topic_id=topic_id,
        type="frq",
        difficulty=difficulty,
        prompt="Sample FRQ prompt",
        correct_answer="model answer",
        rubric_json={"checklist": checklist},
        validation_status=validation_status,
    )
    db.add(question)
    db.flush()
    return question
