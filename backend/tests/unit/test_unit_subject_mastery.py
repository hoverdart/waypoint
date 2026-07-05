import pytest

from app.services.mastery.subject_mastery import (
    compute_subject_mastery_from_units,
    predict_ap_score,
)
from app.services.mastery.unit_mastery import compute_unit_mastery_from_topics


def test_unit_mastery_is_equal_weighted_average_of_topics():
    mastery, confidence = compute_unit_mastery_from_topics([(0.8, 0.9), (0.4, 0.5), (0.6, 0.7)])
    assert mastery == pytest.approx((0.8 + 0.4 + 0.6) / 3)
    assert confidence == pytest.approx((0.9 + 0.5 + 0.7) / 3)


def test_unit_mastery_with_no_topics_is_zero():
    assert compute_unit_mastery_from_topics([]) == (0.0, 0.0)


def test_never_attempted_topics_pull_unit_mastery_toward_zero():
    with_gap = compute_unit_mastery_from_topics([(0.9, 0.9), (0.0, 0.0)])
    without_gap = compute_unit_mastery_from_topics([(0.9, 0.9)])
    assert with_gap[0] < without_gap[0]


def test_subject_mastery_weighted_by_ap_unit_frequency():
    # unit A: high AP weight, low mastery. unit B: low AP weight, high mastery.
    # subject mastery should lean toward unit A's low mastery.
    mastery, _ = compute_subject_mastery_from_units([(20.0, 0.2, 0.5), (5.0, 0.9, 0.5)])
    equal_weighted = (0.2 + 0.9) / 2
    assert mastery < equal_weighted


def test_subject_mastery_with_no_units_is_zero():
    assert compute_subject_mastery_from_units([]) == (0.0, 0.0)


def test_predict_ap_score_high_mastery_high_confidence():
    assert predict_ap_score(mastery_score=0.9, confidence_score=0.9) == 5


def test_predict_ap_score_low_mastery():
    assert predict_ap_score(mastery_score=0.1, confidence_score=0.9) == 1


def test_predict_ap_score_shrinks_toward_middle_when_low_confidence():
    """A student who looks like a 5 off a thin sample shouldn't be told
    they're a 5 -- low confidence should pull the prediction toward 3."""
    confident_five = predict_ap_score(mastery_score=0.95, confidence_score=0.9)
    unconfident_five = predict_ap_score(mastery_score=0.95, confidence_score=0.1)
    assert unconfident_five < confident_five


def test_predict_ap_score_bounded_1_to_5():
    for m in (0.0, 0.25, 0.5, 0.75, 1.0):
        for c in (0.0, 0.5, 1.0):
            score = predict_ap_score(mastery_score=m, confidence_score=c)
            assert 1 <= score <= 5
