"""Runs weekly via a cron-compatible script (scripts/weekly_coach_job.py), not
interactively. Since the given schema has no subject_id on
weekly_coach_reports, one report aggregates across all of the user's active
subjects; the most exam-imminent subject is called out in
projected_score_note. Idempotent per (user_id, week_start).

Mastery deltas are approximated: there is no history table to compute a true
week-over-week change, so a topic whose topic_mastery row was touched this
week (updated_at falls in-window) stands in for "changed this week", using
its current mastery_score - documented limitation, not a hidden bug.
"""

from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone

from sqlmodel import Session, select

from app.models.coach import WeeklyCoachReport
from app.models.mastery import SubjectMastery, TopicMastery
from app.models.practice import PracticeSession
from app.models.subject import Subject, Topic, Unit, UserSubject
from app.models.user import User
from app.services.xp.streak_service import compute_streak_days

FORGOTTEN_RETENTION_THRESHOLD = 0.4
# Weakness ranking nudges equally-weak topics on higher-AP-weight units ahead
# of the same weakness on a low-weight unit.
WEAKNESS_AP_WEIGHT_NUDGE = 0.3
NEXT_WEEK_PRIORITY_COUNT = 3
STREAK_LOOKBACK_DAYS = 90


@dataclass
class TopicSnapshot:
    topic_id: int
    topic_name: str
    unit_name: str
    subject_name: str
    mastery_score: float
    retention_score: float
    attempts_count: int
    ap_weight_midpoint: float
    touched_this_week: bool


def _weakness_rank(topic: TopicSnapshot) -> float:
    return topic.mastery_score - WEAKNESS_AP_WEIGHT_NUDGE * (topic.ap_weight_midpoint / 100.0)


def pick_biggest_win(topics: list[TopicSnapshot]) -> TopicSnapshot | None:
    touched = [t for t in topics if t.touched_this_week and t.attempts_count > 0]
    if not touched:
        return None
    return max(touched, key=lambda t: t.mastery_score)


def pick_biggest_weakness(topics: list[TopicSnapshot]) -> TopicSnapshot | None:
    attempted = [t for t in topics if t.attempts_count > 0]
    if not attempted:
        return None
    return min(attempted, key=_weakness_rank)


def find_forgotten_topics(topics: list[TopicSnapshot]) -> list[TopicSnapshot]:
    return [
        t for t in topics if t.attempts_count > 0 and t.retention_score < FORGOTTEN_RETENTION_THRESHOLD
    ]


def next_week_priority_topics(topics: list[TopicSnapshot], count: int = NEXT_WEEK_PRIORITY_COUNT) -> list[TopicSnapshot]:
    return sorted(topics, key=_weakness_rank)[:count]


def _format_percent(score: float) -> str:
    return f"{round(score * 100)}%"


def _gather_topic_snapshots(
    db: Session, subject_ids: list[int], user_id: int, week_start: date, week_end_exclusive: date
) -> list[TopicSnapshot]:
    snapshots = []
    for subject_id in subject_ids:
        subject = db.get(Subject, subject_id)
        units = db.exec(select(Unit).where(Unit.subject_id == subject_id)).all()
        for unit in units:
            ap_weight_midpoint = (unit.ap_weight_min + unit.ap_weight_max) / 2.0
            topics = db.exec(select(Topic).where(Topic.unit_id == unit.id)).all()
            for topic in topics:
                tm = db.get(TopicMastery, (user_id, topic.id))
                if tm is None:
                    continue
                touched = tm.updated_at is not None and week_start <= tm.updated_at.date() < week_end_exclusive
                snapshots.append(
                    TopicSnapshot(
                        topic_id=topic.id,
                        topic_name=topic.name,
                        unit_name=unit.name,
                        subject_name=subject.name,
                        mastery_score=tm.mastery_score,
                        retention_score=tm.retention_score,
                        attempts_count=tm.attempts_count,
                        ap_weight_midpoint=ap_weight_midpoint,
                        touched_this_week=touched,
                    )
                )
    return snapshots


def build_weekly_report(
    db: Session, user_id: int, week_start: date, now: datetime | None = None
) -> WeeklyCoachReport:
    now = now or datetime.now(timezone.utc)
    week_end_exclusive = week_start + timedelta(days=7)
    week_end_inclusive = week_start + timedelta(days=6)

    user_subjects = db.exec(
        select(UserSubject).where(UserSubject.user_id == user_id, UserSubject.is_active == True)  # noqa: E712
    ).all()
    subject_ids = [us.subject_id for us in user_subjects]

    window_start_dt = datetime(week_start.year, week_start.month, week_start.day)
    window_end_dt = datetime(week_end_exclusive.year, week_end_exclusive.month, week_end_exclusive.day)
    sessions_this_week = db.exec(
        select(PracticeSession).where(
            PracticeSession.user_id == user_id,
            PracticeSession.completed_at.is_not(None),
            PracticeSession.completed_at >= window_start_dt,
            PracticeSession.completed_at < window_end_dt,
        )
    ).all()
    sessions_completed = len(sessions_this_week)
    questions_answered = sum(s.total_questions for s in sessions_this_week)
    correct_answered = sum(s.correct_count for s in sessions_this_week)

    lookback_start = window_start_dt - timedelta(days=STREAK_LOOKBACK_DAYS)
    recent_sessions = db.exec(
        select(PracticeSession).where(
            PracticeSession.user_id == user_id,
            PracticeSession.completed_at.is_not(None),
            PracticeSession.completed_at >= lookback_start,
        )
    ).all()
    session_dates = {s.completed_at.date() for s in recent_sessions}
    streak_days = compute_streak_days(session_dates, now.date())

    topics = _gather_topic_snapshots(db, subject_ids, user_id, week_start, week_end_exclusive)
    biggest_win_topic = pick_biggest_win(topics)
    biggest_weakness_topic = pick_biggest_weakness(topics)
    forgotten = find_forgotten_topics(topics)
    priority_topics = next_week_priority_topics(topics)

    next_week_priorities = [
        {
            "topic_id": t.topic_id,
            "topic_name": t.topic_name,
            "subject_name": t.subject_name,
            "reason": "Low mastery relative to how much it's worth on the exam",
        }
        for t in priority_topics
    ]

    most_urgent_us = min(
        (us for us in user_subjects if us.exam_date is not None), key=lambda us: us.exam_date, default=None
    )
    projected_score_note = None
    if most_urgent_us is not None:
        subject_mastery = db.get(SubjectMastery, (user_id, most_urgent_us.subject_id))
        subject = db.get(Subject, most_urgent_us.subject_id)
        if subject_mastery is not None:
            days_left = (most_urgent_us.exam_date - now.date()).days
            when = f", {days_left} days out" if days_left > 0 else ""
            projected_score_note = (
                f"You're currently tracking toward a {subject_mastery.predicted_ap_score} "
                f"on {subject.name}{when}."
            )

    biggest_win = (
        f"{biggest_win_topic.topic_name} ({biggest_win_topic.subject_name}) is looking strong at "
        f"{_format_percent(biggest_win_topic.mastery_score)} mastery."
        if biggest_win_topic
        else None
    )
    biggest_weakness = (
        f"{biggest_weakness_topic.topic_name} ({biggest_weakness_topic.subject_name}) is your "
        "biggest opportunity right now."
        if biggest_weakness_topic
        else None
    )

    summary_parts = [f"You completed {sessions_completed} practice session(s) and answered {questions_answered} questions this week"]
    summary_parts[0] += (
        f" ({round(100 * correct_answered / questions_answered)}% correct)."
        if questions_answered
        else "."
    )
    if streak_days > 0:
        summary_parts.append(f"You're on a {streak_days}-day streak - keep it going!")
    if forgotten:
        summary_parts.append(
            f"{len(forgotten)} topic(s) are at risk of being forgotten and could use a quick review."
        )
    summary = " ".join(summary_parts)

    report = db.exec(
        select(WeeklyCoachReport).where(
            WeeklyCoachReport.user_id == user_id, WeeklyCoachReport.week_start == week_start
        )
    ).first()
    if report is None:
        report = WeeklyCoachReport(user_id=user_id, week_start=week_start, week_end=week_end_inclusive)

    report.week_end = week_end_inclusive
    report.summary = summary
    report.biggest_win = biggest_win
    report.biggest_weakness = biggest_weakness
    report.next_week_priorities = next_week_priorities
    report.projected_score_note = projected_score_note
    db.add(report)
    db.flush()
    return report


def last_monday(today: date | None = None) -> date:
    today = today or date.today()
    return today - timedelta(days=today.weekday())


def run_for_all_users(db: Session, week_start: date) -> tuple[int, int]:
    """Used by both the cron script and the internal HTTP trigger endpoint.
    Wraps each user independently so one failure doesn't kill the batch."""
    users = db.exec(select(User)).all()
    succeeded = 0
    for user in users:
        try:
            build_weekly_report(db, user.id, week_start)
            db.commit()
            succeeded += 1
        except Exception as exc:  # noqa: BLE001 - deliberately broad, one bad user shouldn't kill the batch
            db.rollback()
            print(f"WARNING: weekly report failed for user {user.id}: {exc}")
    return succeeded, len(users)
