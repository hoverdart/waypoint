import random

from app.services.planner.priority import (
    ap_unit_weight,
    compute_priority_score,
    confidence_uncertainty,
    derive_priority_factors,
    retention_factor,
    score_from_factors,
    weakness_factor,
)
from app.services.planner.reasons import reason_for_item


def test_priority_score_is_literal_product_of_factors():
    assert compute_priority_score(
        weakness=0.5, retention=0.4, ap_weight=0.3, confidence_unc=0.2, topic_timer=2.0, randomization=1.0
    ) == 0.5 * 0.4 * 0.3 * 0.2 * 2.0 * 1.0


def test_weaker_topics_score_higher_weakness_factor():
    assert weakness_factor(mastery_score=0.1) > weakness_factor(mastery_score=0.9)


def test_more_forgotten_topics_score_higher_retention_factor():
    assert retention_factor(retention_score=0.1) > retention_factor(retention_score=0.9)


def test_lower_confidence_scores_higher_uncertainty():
    assert confidence_uncertainty(confidence_score=0.1) > confidence_uncertainty(confidence_score=0.9)


def test_higher_ap_weight_scores_higher():
    assert ap_unit_weight(20.0) > ap_unit_weight(5.0)


def test_perfect_retention_never_zeroes_out_priority():
    """A never-attempted topic can default to retention_score=1.0 (fully
    'retained' since it's never been forgotten) - this must not zero out its
    priority entirely via the floored inverse factor."""
    assert retention_factor(retention_score=1.0) > 0.0
    assert weakness_factor(mastery_score=1.0) > 0.0
    assert confidence_uncertainty(confidence_score=1.0) > 0.0


def test_derive_priority_factors_returns_named_dict():
    rng = random.Random(42)
    factors = derive_priority_factors(
        mastery_score=0.2,
        retention_score=0.3,
        confidence_score=0.1,
        ap_weight_midpoint_percent=15.0,
        topic_timer=5.0,
        rng=rng,
    )
    assert set(factors.keys()) == {
        "weakness_factor",
        "retention_factor",
        "ap_unit_weight",
        "confidence_uncertainty",
        "topic_timer",
        "randomization_factor",
    }
    assert score_from_factors(factors) > 0.0


def test_reason_picks_dominant_factor():
    factors = {
        "weakness_factor": 0.9,
        "retention_factor": 0.1,
        "ap_unit_weight": 0.2,
        "confidence_uncertainty": 0.1,
        "topic_timer": 5.0,
        "randomization_factor": 1.0,
    }
    assert reason_for_item(factors, "weakness") == "Your mastery dropped"


def test_reason_ap_weight_dominant():
    factors = {
        "weakness_factor": 0.1,
        "retention_factor": 0.1,
        "ap_unit_weight": 0.95,
        "confidence_uncertainty": 0.1,
        "topic_timer": 1.0,
        "randomization_factor": 1.0,
    }
    assert reason_for_item(factors, "review") == "This unit is high-frequency on the AP exam"


def test_reason_calibration_overrides_dominant_factor():
    factors = {
        "weakness_factor": 0.9,
        "retention_factor": 0.1,
        "ap_unit_weight": 0.1,
        "confidence_uncertainty": 0.1,
        "topic_timer": 1.0,
        "randomization_factor": 1.0,
    }
    assert reason_for_item(factors, "calibration") == "Quick check to confirm what you already know"
