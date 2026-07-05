"""Clerk adapter: verifies the bearer session token networklessly against
Clerk's JWKS (via clerk_backend_api.authenticate_request), avoiding a network
round-trip per request. `authenticate_request` only requires an object
exposing `.headers`, so `_HeaderRequest` is a minimal stand-in for a real
Next.js/Starlette request.
"""

from collections.abc import Mapping

from clerk_backend_api import authenticate_request
from clerk_backend_api.security.types import AuthenticateRequestOptions

from app.config import Settings
from app.services.auth.provider import AuthError, AuthIdentity


class _HeaderRequest:
    def __init__(self, headers: Mapping[str, str]):
        self.headers = headers


class ClerkAuthProvider:
    def __init__(self, settings: Settings):
        self._settings = settings

    def verify_token(self, authorization_header: str | None) -> AuthIdentity:
        if not authorization_header:
            raise AuthError("Missing Authorization header")

        # clerk_backend_api reads this via `request.headers.get('Authorization')`
        # (exact case) - a lowercase key here would silently miss on a plain dict.
        request = _HeaderRequest({"Authorization": authorization_header})
        options = AuthenticateRequestOptions(secret_key=self._settings.clerk_secret_key)

        try:
            state = authenticate_request(request, options)
        except Exception as exc:  # clerk_backend_api raises on malformed tokens
            raise AuthError(f"Token verification failed: {exc}") from exc

        if not state.is_signed_in or not state.payload:
            raise AuthError(state.message or "Invalid or expired session token")

        payload = state.payload
        return AuthIdentity(
            provider_user_id=payload["sub"],
            email=payload.get("email"),
            display_name=payload.get("name"),
        )
