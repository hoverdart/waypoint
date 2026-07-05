from app.services.mastery.retention import compute_retention_score


def test_retention_is_1_at_zero_days():
    assert compute_retention_score(mastery_score=0.5, days_since_practiced=0) == 1.0


def test_retention_decays_over_time():
    assert compute_retention_score(
        mastery_score=0.5, days_since_practiced=30
    ) < compute_retention_score(mastery_score=0.5, days_since_practiced=1)


def test_high_mastery_topics_retained_longer_than_low_mastery():
    days = 20
    low_mastery_retention = compute_retention_score(mastery_score=0.1, days_since_practiced=days)
    high_mastery_retention = compute_retention_score(mastery_score=0.9, days_since_practiced=days)
    assert high_mastery_retention > low_mastery_retention


def test_retention_score_bounded_between_0_and_1():
    score = compute_retention_score(mastery_score=0.0, days_since_practiced=365)
    assert 0.0 <= score <= 1.0
