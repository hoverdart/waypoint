from app.models.mastery import TopicMastery
from app.models.subject import Subject, Topic, Unit
from app.models.user import User
from app.services.mastery.topic_mastery import (
    AttemptSignal,
    learning_rate,
    update_topic_mastery_after_session,
)


def _make_user_and_topic(db_session):
    user = User(auth_provider_id="u1", email="u1@example.com")
    subject = Subject(name="AP Calculus AB", ap_exam_code="calculus-ab")
    db_session.add(user)
    db_session.add(subject)
    db_session.flush()
    unit = Unit(subject_id=subject.id, name="Limits", ap_weight_min=10, ap_weight_max=15)
    db_session.add(unit)
    db_session.flush()
    topic = Topic(unit_id=unit.id, name="Continuity")
    db_session.add(topic)
    db_session.flush()
    return user, topic


def test_learning_rate_shrinks_as_attempts_accumulate():
    assert learning_rate(0) > learning_rate(50)


def test_update_creates_topic_mastery_row_if_absent(db_session):
    user, topic = _make_user_and_topic(db_session)

    tm = update_topic_mastery_after_session(
        db_session,
        user_id=user.id,
        topic_id=topic.id,
        session_attempts=[
            AttemptSignal(is_correct=True, difficulty=3, hints_used=0, time_seconds=60),
            AttemptSignal(is_correct=True, difficulty=3, hints_used=0, time_seconds=60),
        ],
        recent_results=[True, True],
    )
    db_session.flush()

    assert tm.attempts_count == 2
    assert tm.correct_count == 2
    assert tm.mastery_score > 0.0
    assert tm.topic_timer == 0.0
    assert tm.timer_last_advanced_date is not None


def test_single_session_never_moves_mastery_from_zero_to_one(db_session):
    """A one-off perfect session shouldn't instantly declare mastery -- this
    is the whole reason mastery updates after a session, not a question."""
    user, topic = _make_user_and_topic(db_session)

    tm = update_topic_mastery_after_session(
        db_session,
        user_id=user.id,
        topic_id=topic.id,
        session_attempts=[
            AttemptSignal(is_correct=True, difficulty=3, hints_used=0, time_seconds=60)
        ],
        recent_results=[True],
    )
    assert tm.mastery_score < 1.0


def test_repeated_good_sessions_converge_mastery_upward(db_session):
    user, topic = _make_user_and_topic(db_session)

    tm = None
    for _ in range(15):
        tm = update_topic_mastery_after_session(
            db_session,
            user_id=user.id,
            topic_id=topic.id,
            session_attempts=[
                AttemptSignal(is_correct=True, difficulty=3, hints_used=0, time_seconds=60)
                for _ in range(5)
            ],
            recent_results=[True] * 10,
        )
        db_session.flush()

    assert tm.mastery_score > 0.8


def test_mastery_can_drop_after_a_poor_session(db_session):
    user, topic = _make_user_and_topic(db_session)
    tm = TopicMastery(
        user_id=user.id,
        topic_id=topic.id,
        mastery_score=0.8,
        confidence_score=0.7,
        retention_score=0.9,
        topic_timer=0.0,
        attempts_count=20,
        correct_count=16,
    )
    db_session.add(tm)
    db_session.flush()

    updated = update_topic_mastery_after_session(
        db_session,
        user_id=user.id,
        topic_id=topic.id,
        session_attempts=[
            AttemptSignal(is_correct=False, difficulty=3, hints_used=1, time_seconds=90)
            for _ in range(5)
        ],
        recent_results=[False] * 5,
    )
    assert updated.mastery_score < 0.8
