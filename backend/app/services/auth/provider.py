"""Auth-provider-agnostic contract. Swapping Clerk for Firebase (or anything
else) later means writing one new adapter implementing `AuthProvider`, nothing
else in the app changes.
"""

from typing import Protocol

from pydantic import BaseModel


class AuthIdentity(BaseModel):
    provider_user_id: str
    email: str | None = None
    display_name: str | None = None


class AuthError(Exception):
    """Missing, malformed, or expired credentials."""


class AuthProvider(Protocol):
    def verify_token(self, authorization_header: str | None) -> AuthIdentity: ...
