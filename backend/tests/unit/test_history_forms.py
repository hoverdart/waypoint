from collections import Counter
from copy import deepcopy
import pytest
from scripts.history_forms import assemble_draft_forms, manifest, PERIOD_COUNTS
from scripts.seed_data.units_topics.us_history import UNITS
from scripts.seed_data.questions.us_history_questions import QUESTIONS


def test_four_complete_independent_forms_preserve_groups_and_weights():
    forms = assemble_draft_forms(UNITS, QUESTIONS)
    assert [len(f) for f in forms] == [55] * 4
    prompts = [q['prompt'] for f in forms for q in f]
    assert len(set(prompts)) == 220
    membership = {}
    original = Counter(t for q in QUESTIONS for t in q['skill_tags'] if t.startswith('stimulus:'))
    for index, form in enumerate(forms):
        assert Counter(q['unit_name'] for q in form) == dict(zip([u['name'] for u in UNITS], PERIOD_COUNTS))
        groups = Counter(t for q in form for t in q['skill_tags'] if t.startswith('stimulus:'))
        for group, count in groups.items():
            assert group not in membership
            membership[group] = index
            assert count == original[group]
        assert all(q['type'] == 'mcq' and q['validation_status'] == 'approved' for q in form)


def test_manifest_is_deterministic_and_explicitly_unpublished():
    assert manifest(UNITS, QUESTIONS) == manifest(UNITS, QUESTIONS)
    assert manifest(UNITS, QUESTIONS)['status'] == 'offline_draft_not_published'


def test_insufficient_bank_fails_instead_of_reusing_items():
    with pytest.raises(ValueError, match='Cannot pack'):
        assemble_draft_forms(UNITS, QUESTIONS[:10])


def test_ambiguous_or_cross_period_groups_are_rejected():
    rows = deepcopy(QUESTIONS)
    rows[0]['skill_tags'] += ['stimulus:ambiguous-a', 'stimulus:ambiguous-b']
    with pytest.raises(ValueError, match='Ambiguous'):
        assemble_draft_forms(UNITS, rows)
    rows = deepcopy(QUESTIONS)
    rows[0]['skill_tags'] = ['stimulus:cross']
    other = next(q for q in rows if q['unit_name'] != rows[0]['unit_name'])
    other['skill_tags'] = ['stimulus:cross']
    with pytest.raises(ValueError, match='spans multiple'):
        assemble_draft_forms(UNITS, rows)


def test_changed_weights_cannot_silently_invalidate_blueprint():
    units = deepcopy(UNITS)
    units[0]['ap_weight_min'] = 20
    with pytest.raises(ValueError, match='conflicts'):
        assemble_draft_forms(units, QUESTIONS)


@pytest.mark.parametrize('invalid', ['draft', 'frq', 'duplicate'])
def test_ineligible_period_items_do_not_fill_blueprint(invalid):
    rows = deepcopy(QUESTIONS)
    first = [q for q in rows if q['unit_name'] == UNITS[0]['name']]
    if invalid == 'duplicate':
        rows.extend(deepcopy(first))
    else:
        for q in first:
            q['validation_status' if invalid == 'draft' else 'type'] = invalid
    with pytest.raises(ValueError, match='Cannot pack'):
        assemble_draft_forms(UNITS, rows)
