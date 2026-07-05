from app.models.question import Question
from app.services.practice.scoring import score_frq_attempt


def _frq_question(checklist):
    return Question(
        subject_id=1,
        unit_id=1,
        topic_id=1,
        type="frq",
        difficulty=3,
        prompt="Explain X.",
        correct_answer="model answer",
        rubric_json={"checklist": checklist},
    )


def test_full_credit_when_all_keywords_present():
    q = _frq_question(
        [
            {"point": "states rule", "keywords": ["chain rule"], "points": 2},
            {"point": "computes derivative", "keywords": ["derivative", "="], "points": 2},
        ]
    )
    is_correct, score, max_score = score_frq_attempt(
        q, "Using the chain rule, the derivative = 2x."
    )
    assert score == max_score == 4
    assert is_correct


def test_partial_credit_when_some_keywords_missing():
    q = _frq_question(
        [
            {"point": "states rule", "keywords": ["chain rule"], "points": 2},
            {"point": "computes derivative", "keywords": ["derivative", "="], "points": 2},
        ]
    )
    is_correct, score, max_score = score_frq_attempt(q, "The derivative is 2x.")
    assert score == 2
    assert max_score == 4
    assert not is_correct


def test_empty_response_scores_zero():
    q = _frq_question([{"point": "p", "keywords": ["x"], "points": 1}])
    is_correct, score, max_score = score_frq_attempt(q, None)
    assert score == 0.0
    assert not is_correct
    assert max_score == 1


def test_no_rubric_defaults_to_max_score_one():
    q = _frq_question([])
    is_correct, score, max_score = score_frq_attempt(q, "some answer")
    assert max_score == 1.0
    assert score == 0.0
