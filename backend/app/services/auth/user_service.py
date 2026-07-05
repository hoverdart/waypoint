"""Provider-agnostic user upsert, kept out of the Clerk adapter so the DB logic
doesn't need to change if the auth provider ever does.
"""

from sqlmodel import Session, select

from app.models.user import User
from app.services.auth.provider import AuthIdentity


def get_or_create_user(db: Session, identity: AuthIdentity) -> User:
    user = db.exec(select(User).where(User.auth_provider_id == identity.provider_user_id)).first()
    if user is None:
        user = User(
            auth_provider_id=identity.provider_user_id,
            email=identity.email or f"{identity.provider_user_id}@unknown.local",
            display_name=identity.display_name,
        )
        db.add(user)
        db.flush()
        return user

    if identity.email:
        user.email = identity.email
    if identity.display_name:
        user.display_name = identity.display_name
    db.add(user)
    return user
