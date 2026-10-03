from scripts.seed_data.rollout import COURSE_ROLLOUT, PRIORITY
from scripts.seed_data.subjects import SUBJECTS


def test_rollout_uses_complete_descending_2025_exam_counts():
    counts = [count for _, _, count in COURSE_ROLLOUT if count is not None]
    assert len(counts) == 40
    assert sum(counts) == 6182171
    assert counts == sorted(counts, reverse=True)
    assert len(PRIORITY) == len(COURSE_ROLLOUT) == 43
    assert COURSE_ROLLOUT[0][0] == 'english-language'
    assert all(count is None for _, _, count in COURSE_ROLLOUT[40:])
    assert all(subject['ap_exam_code'] in PRIORITY for subject in SUBJECTS)
