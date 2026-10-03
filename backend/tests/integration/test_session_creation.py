import random

import pytest
from sqlmodel import select

from app.core.exceptions import DomainError
from app.models.practice import PracticeSession
from app.services.diagnostic.diagnostic_builder import build_diagnostic_session
from app.services.practice.session_service import start_practice_session
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user


@pytest.mark.parametrize("diagnostic", [False, True])
def test_empty_selection_does_not_create_session(db_session, diagnostic):
    user = make_user(db_session)
    subject, _ = make_subject_with_units_topics(db_session)
    with pytest.raises(DomainError, match="No approved questions"):
        if diagnostic:
            build_diagnostic_session(db_session, user.id, subject.id, 10)
        else:
            start_practice_session(db_session, user.id, subject.id)
    assert list(db_session.exec(select(PracticeSession)).all()) == []


@pytest.mark.parametrize("scope", ["missing", "inactive", "foreign_unit", "foreign_topic", "mismatched_topic", "archived"])
def test_invalid_scope_does_not_create_session(db_session, scope):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session)
    _, other_units = make_subject_with_units_topics(db_session, code="other")
    unit, topics = units[0]
    make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    args = {"subject_id": subject.id}
    if scope == "missing":
        args["subject_id"] = 999999
    elif scope == "inactive":
        subject.is_active = False
        db_session.add(subject)
    elif scope == "foreign_unit":
        args["unit_id"] = other_units[0][0].id
    elif scope == "foreign_topic":
        args["topic_id"] = other_units[0][1][0].id
    elif scope == "mismatched_topic":
        args.update(unit_id=units[1][0].id, topic_id=topics[0].id)
    else:
        unit.is_active = False
        db_session.add(unit)
        args["topic_id"] = topics[0].id
    db_session.flush()
    with pytest.raises(DomainError):
        start_practice_session(db_session, user.id, **args)
    assert list(db_session.exec(select(PracticeSession)).all()) == []


def test_diagnostic_fills_sparse_units_and_uses_difficulty_fallback(db_session):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    approved = []
    for difficulty in [3, 1, 1, 5, 5, 5]:
        q, _ = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, difficulty=difficulty)
        approved.append(q.id)
    make_mcq_question(db_session, subject.id, unit.id, topics[0].id, validation_status="needs_review")
    db_session.flush()
    session, questions = build_diagnostic_session(db_session, user.id, subject.id, 6, rng=random.Random(1))
    assert session.total_questions == 6
    assert {q.id for q in questions} == set(approved)


def test_zero_weight_units_still_produce_unique_available_questions(db_session):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session)
    for unit, topics in units:
        unit.ap_weight_min = unit.ap_weight_max = 0
        db_session.add(unit)
        make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.flush()
    session, questions = build_diagnostic_session(db_session, user.id, subject.id, 10)
    assert session.total_questions == len({q.id for q in questions}) == 2
