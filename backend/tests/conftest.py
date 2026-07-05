import os

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app.dependencies import get_auth_provider
from app.db.session import get_db
from app.main import app
from app.services.auth.provider import AuthError, AuthIdentity

TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL",
    "postgresql+psycopg://waypoint:waypoint@localhost:5432/waypoint_test",
)

_engine = create_engine(TEST_DATABASE_URL)


@pytest.fixture(scope="session", autouse=True)
def _ensure_schema():
    from app.db import base  # noqa: F401 - populate metadata

    SQLModel.metadata.create_all(_engine)
    yield


@pytest.fixture
def db_session():
    """Real Postgres-backed session, isolated per test via a SAVEPOINT: the
    app is free to call `.commit()` (which only ends the savepoint) while the
    outer transaction - and everything in it - is rolled back at teardown.
    """
    connection = _engine.connect()
    outer_transaction = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    try:
        yield session
    finally:
        session.close()
        outer_transaction.rollback()
        connection.close()


class FakeAuthProvider:
    """Test double for AuthProvider. Tokens look like "Bearer <id>:<email>" so
    a test can pick exactly which (possibly not-yet-synced) identity is
    calling, without touching real Clerk."""

    def verify_token(self, authorization_header: str | None) -> AuthIdentity:
        if not authorization_header:
            raise AuthError("Missing Authorization header")
        token = authorization_header.removeprefix("Bearer ").strip()
        provider_user_id, _, email = token.partition(":")
        if not provider_user_id:
            raise AuthError("Malformed fake token")
        return AuthIdentity(
            provider_user_id=provider_user_id, email=email or f"{provider_user_id}@example.com"
        )


def auth_header(provider_user_id: str, email: str | None = None) -> dict[str, str]:
    token = f"{provider_user_id}:{email}" if email else provider_user_id
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def client(db_session):
    def _get_db_override():
        yield db_session

    app.dependency_overrides[get_db] = _get_db_override
    app.dependency_overrides[get_auth_provider] = lambda: FakeAuthProvider()
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()
