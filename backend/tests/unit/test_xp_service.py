from app.services.xp.xp_service import award_xp, get_total_xp
from tests.factories import make_user


def test_get_total_xp_sums_events(db_session):
    user = make_user(db_session)
    award_xp(db_session, user.id, source="practice_session", amount=10)
    award_xp(db_session, user.id, source="practice_session", amount=15)
    db_session.flush()

    assert get_total_xp(db_session, user.id) == 25


def test_get_total_xp_is_zero_for_new_user(db_session):
    user = make_user(db_session)
    assert get_total_xp(db_session, user.id) == 0


def test_get_total_xp_only_counts_own_user(db_session):
    user_a = make_user(db_session, auth_provider_id="a", email="a@example.com")
    user_b = make_user(db_session, auth_provider_id="b", email="b@example.com")
    award_xp(db_session, user_a.id, source="practice_session", amount=10)
    award_xp(db_session, user_b.id, source="practice_session", amount=99)
    db_session.flush()

    assert get_total_xp(db_session, user_a.id) == 10
