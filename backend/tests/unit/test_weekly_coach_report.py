from datetime import date

from app.services.coach.weekly_report_service import (
    TopicSnapshot,
    compute_streak_days,
    find_forgotten_topics,
    next_week_priority_topics,
    pick_biggest_weakness,
    pick_biggest_win,
)


def _topic(topic_id, mastery=0.5, retention=1.0, attempts=1, ap_weight=10.0, touched=False):
    return TopicSnapshot(
        topic_id=topic_id,
        topic_name=f"Topic {topic_id}",
        unit_name="Unit",
        subject_name="Subject",
        mastery_score=mastery,
        retention_score=retention,
        attempts_count=attempts,
        ap_weight_midpoint=ap_weight,
        touched_this_week=touched,
    )


def test_compute_streak_days_counts_consecutive_days_ending_today():
    dates = {date(2026, 1, 5), date(2026, 1, 4), date(2026, 1, 3)}
    assert compute_streak_days(dates, as_of=date(2026, 1, 5)) == 3


def test_compute_streak_days_allows_yesterday_if_nothing_today_yet():
    dates = {date(2026, 1, 4), date(2026, 1, 3)}
    assert compute_streak_days(dates, as_of=date(2026, 1, 5)) == 2


def test_compute_streak_days_zero_when_gap():
    dates = {date(2026, 1, 1)}
    assert compute_streak_days(dates, as_of=date(2026, 1, 5)) == 0


def test_pick_biggest_win_requires_touched_and_attempted():
    topics = [
        _topic(1, mastery=0.9, touched=True, attempts=5),
        _topic(2, mastery=0.95, touched=False, attempts=5),  # not touched -> excluded
        _topic(3, mastery=0.1, touched=True, attempts=0),  # never attempted -> excluded
    ]
    win = pick_biggest_win(topics)
    assert win.topic_id == 1


def test_pick_biggest_win_none_when_nothing_touched():
    assert pick_biggest_win([_topic(1, touched=False)]) is None


def test_pick_biggest_weakness_favors_low_mastery_high_ap_weight():
    equally_weak = [
        _topic(1, mastery=0.2, ap_weight=5.0, attempts=3),
        _topic(2, mastery=0.2, ap_weight=25.0, attempts=3),
    ]
    weakness = pick_biggest_weakness(equally_weak)
    assert weakness.topic_id == 2


def test_pick_biggest_weakness_ignores_never_attempted_topics():
    topics = [_topic(1, mastery=0.0, attempts=0), _topic(2, mastery=0.4, attempts=2)]
    assert pick_biggest_weakness(topics).topic_id == 2


def test_find_forgotten_topics_only_flags_attempted_low_retention():
    topics = [
        _topic(1, retention=0.2, attempts=3),
        _topic(2, retention=0.9, attempts=3),
        _topic(3, retention=0.1, attempts=0),
    ]
    forgotten_ids = {t.topic_id for t in find_forgotten_topics(topics)}
    assert forgotten_ids == {1}


def test_next_week_priorities_returns_weakest_topics_first():
    topics = [_topic(1, mastery=0.9), _topic(2, mastery=0.1), _topic(3, mastery=0.5)]
    priorities = next_week_priority_topics(topics, count=2)
    assert [t.topic_id for t in priorities] == [2, 3]
