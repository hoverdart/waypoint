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


def test_every_draft_contains_required_reasoning_skills():
    from scripts.history_forms import REQUIRED_SKILLS
    for form in assemble_draft_forms(UNITS, QUESTIONS):
        assert REQUIRED_SKILLS <= {tag for q in form for tag in q['skill_tags']}
    assert manifest(UNITS, QUESTIONS)['required_skills'] == sorted(REQUIRED_SKILLS)


@pytest.mark.parametrize('use_donor', [False, True])
def test_skill_repair_preserves_groups_and_does_not_mutate_inputs(use_donor):
    from scripts.history_forms import balance_skills, REQUIRED_SKILLS
    def group(tags, period='one', size=1):
        return [{'unit_name': period, 'skill_tags': list(tags)} for _ in range(size)]
    partial = REQUIRED_SKILLS - {'continuity-and-change'}
    groups = {'old': group(partial), 'replacement': group(REQUIRED_SKILLS),
              'reserve': group(REQUIRED_SKILLS)}
    selected = [['old'], ['replacement', 'reserve']] if use_donor else [['old']]
    before = deepcopy((selected, groups))
    result = balance_skills(selected, groups)
    assert result[0] == ['replacement']
    if use_donor:
        assert result[1] == ['old', 'reserve']
    assert (selected, groups) == before
    assert result == balance_skills(selected, groups)


@pytest.mark.parametrize('period,size', [('other', 1), ('one', 2)])
def test_skill_repair_cannot_violate_period_or_group_size(period, size):
    from scripts.history_forms import balance_skills, REQUIRED_SKILLS
    groups = {
        'old': [{'unit_name': 'one', 'skill_tags': []}],
        'replacement': [{'unit_name': period, 'skill_tags': list(REQUIRED_SKILLS)}] * size,
    }
    with pytest.raises(ValueError, match='Skill coverage unmet'):
        balance_skills([['old']], groups)


def test_skill_repair_does_not_transfer_deficit_to_another_form():
    from scripts.history_forms import balance_skills, REQUIRED_SKILLS
    groups = {
        'old': [{'unit_name': 'one', 'skill_tags': []}],
        'replacement': [{'unit_name': 'one', 'skill_tags': list(REQUIRED_SKILLS)}],
    }
    with pytest.raises(ValueError, match='Skill coverage unmet'):
        balance_skills([['old'], ['replacement']], groups)
