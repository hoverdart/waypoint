"""Regression coverage for ClerkAuthProvider, including the header-casing bug
where `_HeaderRequest` used a lowercase "authorization" key - a plain dict
lookup miss against clerk_backend_api's exact-case `request.headers.get(
'Authorization')`, silently failing every request."""

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from app.config import Settings
from app.services.auth.clerk_provider import ClerkAuthProvider
from app.services.auth.provider import AuthError


@pytest.fixture
def provider():
    return ClerkAuthProvider(Settings(clerk_secret_key="sk_test_fake"))


def test_verify_token_rejects_missing_header(provider):
    with pytest.raises(AuthError, match="Missing Authorization header"):
        provider.verify_token(None)


def test_verify_token_passes_the_header_under_the_exact_case_clerk_expects(provider):
    """clerk_backend_api reads `request.headers.get('Authorization')` (capital
    A) - a lowercase key here would silently break auth for every request."""
    signed_in_state = SimpleNamespace(
        is_signed_in=True, payload={"sub": "user_123", "email": "a@example.com", "name": "Ada"}
    )
    with patch("app.services.auth.clerk_provider.authenticate_request", return_value=signed_in_state) as mock_auth:
        provider.verify_token("Bearer real.jwt.token")

    request_arg = mock_auth.call_args[0][0]
    assert request_arg.headers.get("Authorization") == "Bearer real.jwt.token"
    assert request_arg.headers.get("authorization") is None


def test_verify_token_returns_identity_from_payload(provider):
    signed_in_state = SimpleNamespace(
        is_signed_in=True, payload={"sub": "user_123", "email": "a@example.com", "name": "Ada"}
    )
    with patch("app.services.auth.clerk_provider.authenticate_request", return_value=signed_in_state):
        identity = provider.verify_token("Bearer real.jwt.token")

    assert identity.provider_user_id == "user_123"
    assert identity.email == "a@example.com"
    assert identity.display_name == "Ada"


def test_verify_token_rejects_when_not_signed_in(provider):
    not_signed_in_state = SimpleNamespace(is_signed_in=False, payload=None, message="Session expired")
    with patch("app.services.auth.clerk_provider.authenticate_request", return_value=not_signed_in_state):
        with pytest.raises(AuthError, match="Invalid or expired session token"):
            provider.verify_token("Bearer expired.jwt.token")


def test_verify_token_wraps_sdk_exceptions_in_autherror(provider):
    with patch("app.services.auth.clerk_provider.authenticate_request", side_effect=ValueError("malformed JWT")):
        with pytest.raises(AuthError, match="Token verification failed"):
            provider.verify_token("Bearer not-a-real-jwt")


def test_verification_restricts_token_origin():
    provider = ClerkAuthProvider(Settings(cors_allowed_origins=["https://study.example.com"]))
    state = SimpleNamespace(is_signed_in=True, payload={"sub": "user_123"})
    with patch("app.services.auth.clerk_provider.authenticate_request", return_value=state) as verify:
        provider.verify_token("Bearer token")
    assert verify.call_args.args[1].authorized_parties == ["https://study.example.com"]


def test_sdk_failure_details_are_not_exposed(provider):
    with patch("app.services.auth.clerk_provider.authenticate_request", side_effect=ValueError("sensitive transport detail")):
        with pytest.raises(AuthError) as error:
            provider.verify_token("Bearer token")
    assert str(error.value) == "Token verification failed"


@pytest.mark.parametrize("payload", [{"name": "Missing ID"}, {"sub": 123}, {"sub": ""}])
def test_malformed_session_identity_is_rejected(provider, payload):
    state = SimpleNamespace(is_signed_in=True, payload=payload)
    with patch("app.services.auth.clerk_provider.authenticate_request", return_value=state):
        with pytest.raises(AuthError, match="Invalid session identity"):
            provider.verify_token("Bearer token")
