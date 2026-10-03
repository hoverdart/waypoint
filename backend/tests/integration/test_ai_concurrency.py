from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from uuid import uuid4

from sqlmodel import Session, delete, select

from app.models.ai import AIUsage
from app.models.user import User
from app.services.ai.usage_service import get_or_create_current_period, record_usage, would_exceed_cap
from tests.conftest import _engine


def test_parallel_usage_creation_and_cap_enforcement():
    # Independent committed transactions are necessary to exercise row locks.
    with Session(_engine) as db:
        user = User(auth_provider_id=f"concurrency-{uuid4()}", email=f"{uuid4()}@example.com")
        db.add(user)
        db.commit()
        user_id = user.id
    barrier = Barrier(6)

    def request():
        with Session(_engine) as db:
            barrier.wait(timeout=10)
            usage = get_or_create_current_period(db, user_id, 2)
            accepted = not would_exceed_cap(usage, False)
            if accepted:
                record_usage(db, usage, False)
            db.commit()
            return accepted

    try:
        with ThreadPoolExecutor(max_workers=6) as executor:
            accepted = list(executor.map(lambda _: request(), range(6)))
        assert sum(accepted) == 2
        with Session(_engine) as db:
            rows = list(db.exec(select(AIUsage).where(AIUsage.user_id == user_id)).all())
            assert len(rows) == 1
            assert rows[0].free_used == 2
    finally:
        with Session(_engine) as db:
            db.exec(delete(AIUsage).where(AIUsage.user_id == user_id))
            db.exec(delete(User).where(User.id == user_id))
            db.commit()
