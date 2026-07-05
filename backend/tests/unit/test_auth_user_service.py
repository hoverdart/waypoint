from app.services.auth.provider import AuthIdentity
from app.services.auth.user_service import get_or_create_user


def test_get_or_create_user_creates_new_user(db_session):
    identity = AuthIdentity(provider_user_id="clerk_abc", email="a@example.com", display_name="A")
    user = get_or_create_user(db_session, identity)
    db_session.flush()
    assert user.id is not None
    assert user.email == "a@example.com"
    assert user.mode == "professional"


def test_get_or_create_user_is_idempotent(db_session):
    identity = AuthIdentity(provider_user_id="clerk_abc", email="a@example.com")
    user1 = get_or_create_user(db_session, identity)
    db_session.flush()
    user2 = get_or_create_user(db_session, identity)
    db_session.flush()
    assert user1.id == user2.id


def test_get_or_create_user_syncs_email_on_repeat_call(db_session):
    user = get_or_create_user(db_session, AuthIdentity(provider_user_id="clerk_xyz", email="old@example.com"))
    db_session.flush()

    updated = get_or_create_user(db_session, AuthIdentity(provider_user_id="clerk_xyz", email="new@example.com"))
    db_session.flush()

    assert updated.id == user.id
    assert updated.email == "new@example.com"
