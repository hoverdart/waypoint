"""The single writer of topic_mastery. Called once per completed practice
session (never per-question) so single-question flukes can't distort the
model. Blends session accuracy into existing mastery via an exponential moving
average whose learning rate shrinks as evidence accumulates - early sessions
move mastery a lot, later ones refine it. The exact blend formula is not
specified by the product spec beyond "update after a full session"; this is a
documented, tunable default.
"""

import math
from dataclasses import dataclass
from datetime import datetime, timezone

from sqlmodel import Session

from app.core.mathutils import clamp
from app.models.mastery import TopicMastery
from app.services.mastery.confidence import (
    EXPECTED_TIME_SECONDS_BY_DIFFICULTY,
    compute_confidence_score,
)
from app.services.mastery.retention import compute_retention_score
from app.services.mastery.topic_timer import reset_timer

MIN_LEARNING_RATE = 0.05
MAX_LEARNING_RATE = 0.4
LEARNING_RATE_NUMERATOR = 0.5


@dataclass
class AttemptSignal:
    is_correct: bool
    difficulty: int
    hints_used: int
    time_seconds: int


def learning_rate(prior_attempts_count: int) -> float:
    return clamp(
        LEARNING_RATE_NUMERATOR / math.sqrt(prior_attempts_count + 1),
        MIN_LEARNING_RATE,
        MAX_LEARNING_RATE,
    )


def get_or_create_topic_mastery(db: Session, user_id: int, topic_id: int) -> TopicMastery:
    tm = db.get(TopicMastery, (user_id, topic_id))
    if tm is None:
        tm = TopicMastery(
            user_id=user_id,
            topic_id=topic_id,
            mastery_score=0.0,
            confidence_score=0.0,
            retention_score=1.0,
            topic_timer=0.0,
        )
        db.add(tm)
    return tm


def update_topic_mastery_after_session(
    db: Session,
    user_id: int,
    topic_id: int,
    session_attempts: list[AttemptSignal],
    recent_results: list[bool],
    now: datetime | None = None,
) -> TopicMastery:
    """`recent_results` is the chronological correct/incorrect history for this
    topic, including this session's attempts, used only for the confidence
    consistency factor - callers should pass up to the last ~10 results.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    tm = get_or_create_topic_mastery(db, user_id, topic_id)

    total = len(session_attempts)
    correct = sum(1 for a in session_attempts if a.is_correct)
    session_accuracy = (correct / total) if total else 0.0

    lr = learning_rate(tm.attempts_count)
    tm.mastery_score = clamp(
        tm.mastery_score + lr * (session_accuracy - tm.mastery_score), 0.0, 1.0
    )

    avg_difficulty = (
        sum(a.difficulty for a in session_attempts) / total if total else 3.0
    )
    avg_time = sum(a.time_seconds for a in session_attempts) / total if total else 0.0
    expected_time = (
        sum(EXPECTED_TIME_SECONDS_BY_DIFFICULTY.get(a.difficulty, 60) for a in session_attempts)
        / total
        if total
        else 60.0
    )
    hints_used_ratio = (
        sum(1 for a in session_attempts if a.hints_used > 0) / total if total else 0.0
    )
    days_since_last_practice = (
        (now - tm.last_practiced_at.replace(tzinfo=timezone.utc)).total_seconds() / 86400
        if tm.last_practiced_at
        else 0.0
    )

    tm.confidence_score = compute_confidence_score(
        attempts_count=tm.attempts_count + total,
        recent_results=recent_results,
        avg_difficulty=avg_difficulty,
        hints_used_ratio=hints_used_ratio,
        avg_time_seconds=avg_time,
        expected_time_seconds=expected_time,
        days_since_last_practice=days_since_last_practice,
    )
    tm.retention_score = compute_retention_score(
        mastery_score=tm.mastery_score, days_since_practiced=0.0
    )

    tm.attempts_count += total
    tm.correct_count += correct
    tm.last_practiced_at = now
    tm.topic_timer = reset_timer()
    tm.timer_last_advanced_date = now.date()
    # Set explicitly rather than relying on the column's server-side onupdate:
    # code in the same request/session (e.g. the weekly coach report's
    # "touched this week" check) reads this back before any refresh would
    # ever pick up a DB-computed value.
    tm.updated_at = now

    db.add(tm)
    return tm
