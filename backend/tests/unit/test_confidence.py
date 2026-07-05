from app.services.mastery.confidence import (
    compute_confidence_score,
    consistency_factor,
    difficulty_factor,
    hint_penalty,
    recency_decay,
    time_factor,
    volume_factor,
)


def test_volume_factor_saturates_at_20():
    assert volume_factor(20) == 1.0
    assert volume_factor(40) == 1.0


def test_volume_factor_scales_linearly_below_saturation():
    assert volume_factor(10) == 0.5
    assert volume_factor(0) == 0.0


def test_consistency_factor_perfect_when_all_same():
    assert consistency_factor([True, True, True, True]) == 1.0
    assert consistency_factor([False, False, False]) == 1.0


def test_consistency_factor_low_when_erratic():
    erratic = consistency_factor([True, False, True, False, True, False])
    assert erratic < 0.5


def test_consistency_factor_neutral_with_insufficient_data():
    assert consistency_factor([]) == 0.5
    assert consistency_factor([True]) == 0.5


def test_difficulty_factor_scales_with_difficulty():
    assert difficulty_factor(5) == 1.0
    assert difficulty_factor(1) == 0.2


def test_hint_penalty_reduces_with_more_hints():
    assert hint_penalty(0.0) == 1.0
    assert hint_penalty(1.0) == 0.7


def test_time_factor_penalizes_answering_much_faster_than_expected():
    # answering in 10s when 60s expected is a guessing risk -> clamped low
    assert time_factor(avg_time_seconds=10, expected_time_seconds=60) == 0.5


def test_time_factor_does_not_reward_answering_slower_than_expected():
    assert time_factor(avg_time_seconds=600, expected_time_seconds=60) == 1.0


def test_time_factor_neutral_near_expected_time():
    assert time_factor(avg_time_seconds=60, expected_time_seconds=60) == 1.0


def test_recency_decay_is_1_at_zero_days():
    assert recency_decay(0) == 1.0


def test_recency_decay_shrinks_with_more_days():
    assert recency_decay(30) < recency_decay(5)


def test_confidence_score_three_attempts_vs_fifty_at_same_accuracy():
    """Two students at the same session-derived accuracy shouldn't get equal
    confidence if one has 3 attempts and the other has 50 -- volume must
    dominate the composite."""
    low_volume = compute_confidence_score(
        attempts_count=3,
        recent_results=[True, False, True],
        avg_difficulty=3,
        hints_used_ratio=0.0,
        avg_time_seconds=60,
        expected_time_seconds=60,
        days_since_last_practice=0,
    )
    high_volume = compute_confidence_score(
        attempts_count=50,
        recent_results=[True, False, True, False, True, True, False, True, True, True],
        avg_difficulty=3,
        hints_used_ratio=0.0,
        avg_time_seconds=60,
        expected_time_seconds=60,
        days_since_last_practice=0,
    )
    assert high_volume > low_volume


def test_confidence_score_bounded_between_0_and_1():
    score = compute_confidence_score(
        attempts_count=100,
        recent_results=[True] * 10,
        avg_difficulty=5,
        hints_used_ratio=0.0,
        avg_time_seconds=60,
        expected_time_seconds=60,
        days_since_last_practice=0,
    )
    assert 0.0 <= score <= 1.0
