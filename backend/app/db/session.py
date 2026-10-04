from collections.abc import Generator

from sqlmodel import Session, create_engine

from app.config import get_settings

settings = get_settings()

# Timestamp columns currently store UTC without an offset. Pin the connection
# zone so PostgreSQL never casts aware writes into the host's local date.
engine = create_engine(settings.database_url, echo=False, pool_pre_ping=True,
                       connect_args={"options": "-c timezone=UTC"})


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
