from app.services.planner.point_budget import ACTIVITY_COSTS, minutes_to_points


def test_anchor_points_map_exactly():
    assert minutes_to_points(10) == 25
    assert minutes_to_points(20) == 50
    assert minutes_to_points(45) == 100
    assert minutes_to_points(60) == 140


def test_interpolates_between_anchors():
    # halfway between 10 (25pts) and 20 (50pts) minutes
    assert minutes_to_points(15) == 38  # round(25 + 0.5*(50-25)) = round(37.5) = 38


def test_extrapolates_below_first_anchor():
    assert minutes_to_points(0) == 0
    assert 0 < minutes_to_points(5) < 25


def test_extrapolates_beyond_last_anchor():
    points_90 = minutes_to_points(90)
    assert points_90 > 140


def test_activity_costs_defined_for_all_item_types():
    assert set(ACTIVITY_COSTS.keys()) == {
        "easy_review",
        "normal_topic",
        "hard_frq",
        "timed_mini_exam",
    }
    assert ACTIVITY_COSTS["easy_review"] < ACTIVITY_COSTS["hard_frq"]
