from app.services.mastery.topic_timer import (
    advance_topic_timer_daily,
    ap_multiplier,
    growth_rate,
    reset_timer,
)


def test_growth_rate_faster_for_low_mastery():
    assert growth_rate(mastery_score=0.0) > growth_rate(mastery_score=1.0)


def test_ap_multiplier_increases_with_higher_weight():
    assert ap_multiplier(1.0) > ap_multiplier(0.0)
    assert ap_multiplier(0.0) == 1.0


def test_timer_grows_when_practiced_low_mastery():
    grown = advance_topic_timer_daily(
        current_timer=0.0, mastery_score=0.0, unit_ap_weight_normalized=0.5, timer_max=30.0
    )
    assert grown > 0.0


def test_timer_grows_slower_for_high_mastery_topics():
    low_mastery_growth = advance_topic_timer_daily(
        current_timer=5.0, mastery_score=0.1, unit_ap_weight_normalized=0.5, timer_max=30.0
    )
    high_mastery_growth = advance_topic_timer_daily(
        current_timer=5.0, mastery_score=0.9, unit_ap_weight_normalized=0.5, timer_max=30.0
    )
    assert low_mastery_growth > high_mastery_growth


def test_timer_is_capped_at_maximum():
    grown = advance_topic_timer_daily(
        current_timer=29.9, mastery_score=0.0, unit_ap_weight_normalized=1.0, timer_max=30.0
    )
    assert grown <= 30.0

    # Repeated advances never exceed the cap even from a value already at it.
    for _ in range(10):
        grown = advance_topic_timer_daily(
            current_timer=grown, mastery_score=0.0, unit_ap_weight_normalized=1.0, timer_max=30.0
        )
    assert grown <= 30.0


def test_reset_timer_returns_zero():
    assert reset_timer() == 0.0
