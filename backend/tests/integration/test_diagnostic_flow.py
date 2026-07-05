import random

from app.models.mastery import TopicMastery
from app.services.diagnostic.diagnostic_builder import allocate_questions_per_unit, build_diagnostic_session
from app.services.diagnostic.diagnostic_scorer import score_diagnostic
from app.services.practice.types import AnswerSubmission
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user


def test_allocate_questions_sums_exactly_to_total():
    allocation = allocate_questions_per_unit([(1, 10.0), (2, 20.0), (3, 5.0)], total_questions=17)
    assert sum(allocation.values()) == 17


def test_allocate_questions_favors_higher_weight_unit():
    allocation = allocate_questions_per_unit([(1, 10.0), (2, 40.0)], total_questions=10)
    assert allocation[2] > allocation[1]


def test_allocate_questions_empty_units_returns_empty():
    assert allocate_questions_per_unit([], total_questions=10) == {}


def test_build_diagnostic_session_respects_unit_weighting(db_session):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session, n_units=2, n_topics_per_unit=1)
    (unit1, topics1), (unit2, topics2) = units
    for _ in range(5):
        make_mcq_question(db_session, subject.id, unit1.id, topics1[0].id)
        make_mcq_question(db_session, subject.id, unit2.id, topics2[0].id)
    db_session.flush()

    session, questions = build_diagnostic_session(
        db_session, user_id=user.id, subject_id=subject.id, total_questions=6, rng=random.Random(1)
    )
    assert session.session_type == "diagnostic"
    assert len(questions) == session.total_questions
    assert len(questions) <= 6


def test_score_diagnostic_initializes_mastery_for_all_topics(db_session):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session, n_units=2, n_topics_per_unit=2)
    (unit1, topics1), (unit2, topics2) = units

    # Only build/answer questions for the first topic of unit 1.
    question, options = make_mcq_question(db_session, subject.id, unit1.id, topics1[0].id, correct_label="B")
    db_session.flush()

    from app.models.practice import PracticeSession

    session = PracticeSession(
        user_id=user.id, subject_id=subject.id, session_type="diagnostic", total_questions=1
    )
    db_session.add(session)
    db_session.flush()

    answers = [AnswerSubmission(question_id=question.id, selected_option_id=options["B"].id, time_seconds=30)]
    score_diagnostic(db_session, session.id, answers)
    db_session.flush()

    # The answered topic should reflect real evidence.
    answered_tm = db_session.get(TopicMastery, (user.id, topics1[0].id))
    assert answered_tm.attempts_count == 1
    assert answered_tm.mastery_score > 0.0

    # Every other topic in the subject should get an explicit neutral prior,
    # not be left absent.
    for unit, topics in units:
        for topic in topics:
            if topic.id == topics1[0].id:
                continue
            tm = db_session.get(TopicMastery, (user.id, topic.id))
            assert tm is not None
            assert tm.confidence_score == 0.0
            assert tm.mastery_score == 0.5
