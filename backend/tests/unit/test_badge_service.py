from datetime import datetime, timedelta, timezone

from app.models.gamification import Badge, UserBadge
from app.models.practice import PracticeSession
from app.services.xp.badge_service import evaluate_and_award_badges
from app.services.xp.xp_service import award_xp
from tests.factories import make_subject_with_units_topics, make_user


def _make_subject(db):
    subject, _ = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=1)
    return subject.id


def _completed_session(db, user_id, subject_id, session_type="mcq", total=5, correct=5, completed_at=None):
    session = PracticeSession(
        user_id=user_id,
        subject_id=subject_id,
        session_type=session_type,
        total_questions=total,
        correct_count=correct,
        score=correct / total if total else 0.0,
        completed_at=completed_at or datetime.now(timezone.utc),
    )
    db.add(session)
    db.flush()
    return session


def test_first_session_badge_awarded_after_one_completed_session(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    badge = Badge(name="First Steps", rule_json={"type": "first_session"})
    db_session.add(badge)
    db_session.flush()

    session = _completed_session(db_session, user.id, subject_id, total=3, correct=1)
    newly_earned = evaluate_and_award_badges(db_session, user.id, session=session)

    assert [b.name for b in newly_earned] == ["First Steps"]


def test_badge_not_re_awarded_once_earned(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    badge = Badge(name="First Steps", rule_json={"type": "first_session"})
    db_session.add(badge)
    db_session.flush()
    db_session.add(UserBadge(user_id=user.id, badge_id=badge.id))
    db_session.flush()

    session = _completed_session(db_session, user.id, subject_id)
    newly_earned = evaluate_and_award_badges(db_session, user.id, session=session)

    assert newly_earned == []


def test_perfect_session_badge_requires_all_correct_and_min_questions(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    badge = Badge(name="Perfect Session", rule_json={"type": "perfect_session", "min_questions": 5})
    db_session.add(badge)
    db_session.flush()

    too_short = _completed_session(db_session, user.id, subject_id, total=3, correct=3)
    assert evaluate_and_award_badges(db_session, user.id, session=too_short) == []

    not_perfect = _completed_session(db_session, user.id, subject_id, total=5, correct=4)
    assert evaluate_and_award_badges(db_session, user.id, session=not_perfect) == []

    perfect = _completed_session(db_session, user.id, subject_id, total=5, correct=5)
    newly_earned = evaluate_and_award_badges(db_session, user.id, session=perfect)
    assert [b.name for b in newly_earned] == ["Perfect Session"]


def test_diagnostic_complete_badge_requires_diagnostic_session_type(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    badge = Badge(name="Diagnostic Complete", rule_json={"type": "diagnostic_complete"})
    db_session.add(badge)
    db_session.flush()

    mcq_session = _completed_session(db_session, user.id, subject_id, session_type="mcq")
    assert evaluate_and_award_badges(db_session, user.id, session=mcq_session) == []

    diagnostic_session = _completed_session(db_session, user.id, subject_id, session_type="diagnostic")
    newly_earned = evaluate_and_award_badges(db_session, user.id, session=diagnostic_session)
    assert [b.name for b in newly_earned] == ["Diagnostic Complete"]


def test_total_xp_badge_awarded_once_threshold_crossed(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    badge = Badge(name="Century Club", rule_json={"type": "total_xp", "amount": 50})
    db_session.add(badge)
    db_session.flush()

    award_xp(db_session, user.id, source="practice_session", amount=30)
    db_session.flush()
    session = _completed_session(db_session, user.id, subject_id)
    assert evaluate_and_award_badges(db_session, user.id, session=session) == []

    award_xp(db_session, user.id, source="practice_session", amount=25)
    db_session.flush()
    newly_earned = evaluate_and_award_badges(db_session, user.id, session=session)
    assert [b.name for b in newly_earned] == ["Century Club"]


def test_streak_badge_awarded_based_on_consecutive_days(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    badge = Badge(name="On Fire", rule_json={"type": "streak", "days": 3})
    db_session.add(badge)
    db_session.flush()

    now = datetime.now(timezone.utc)
    _completed_session(db_session, user.id, subject_id, completed_at=now - timedelta(days=1))
    _completed_session(db_session, user.id, subject_id, completed_at=now - timedelta(days=2))
    today_session = _completed_session(db_session, user.id, subject_id, completed_at=now)

    newly_earned = evaluate_and_award_badges(db_session, user.id, session=today_session)
    assert [b.name for b in newly_earned] == ["On Fire"]


def test_multiple_badges_can_be_earned_from_one_session(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    db_session.add(Badge(name="First Steps", rule_json={"type": "first_session"}))
    db_session.add(Badge(name="Diagnostic Complete", rule_json={"type": "diagnostic_complete"}))
    db_session.flush()

    session = _completed_session(db_session, user.id, subject_id, session_type="diagnostic")
    newly_earned = evaluate_and_award_badges(db_session, user.id, session=session)

    assert {b.name for b in newly_earned} == {"First Steps", "Diagnostic Complete"}
