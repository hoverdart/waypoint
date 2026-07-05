from fastapi import Depends, Header, HTTPException, status
from sqlmodel import Session, select

from app.config import Settings, get_settings
from app.db.session import get_db
from app.models.user import User
from app.services.ai.anthropic_provider import AnthropicAIProvider
from app.services.ai.provider import AIProvider
from app.services.auth.clerk_provider import ClerkAuthProvider
from app.services.auth.provider import AuthError, AuthProvider
from app.services.auth.user_service import get_or_create_user


def get_auth_provider(settings: Settings = Depends(get_settings)) -> AuthProvider:
    if settings.auth_provider == "clerk":
        return ClerkAuthProvider(settings)
    raise NotImplementedError(f"Unknown auth provider: {settings.auth_provider}")


def get_ai_provider(settings: Settings = Depends(get_settings)) -> AIProvider:
    return AnthropicAIProvider(settings)


def sync_current_user(
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db),
    provider: AuthProvider = Depends(get_auth_provider),
) -> User:
    """Used only by POST /auth/sync-user - the one route allowed to create a
    user as a side effect. Safe/idempotent to call repeatedly."""
    try:
        identity = provider.verify_token(authorization)
    except AuthError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    user = get_or_create_user(db, identity)
    db.commit()
    db.refresh(user)
    return user


def get_current_user(
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db),
    provider: AuthProvider = Depends(get_auth_provider),
) -> User:
    """Every other authenticated route requires the user to already be synced."""
    try:
        identity = provider.verify_token(authorization)
    except AuthError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

    user = db.exec(select(User).where(User.auth_provider_id == identity.provider_user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not synced - call POST /auth/sync-user first",
        )
    return user


def require_admin(
    user: User = Depends(get_current_user),
    settings: Settings = Depends(get_settings),
) -> User:
    if user.auth_provider_id not in settings.admin_user_ids:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return user
