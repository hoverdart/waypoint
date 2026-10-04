import pytest

from scripts.history_readiness import history_mcq_inventory


def unit(name, low=40, high=60):
    return {'name': name, 'ap_weight_min': low, 'ap_weight_max': high}


def items(name, count, **overrides):
    return [dict(unit_name=name, prompt=f'{name}-{i}', type='mcq', validation_status='approved', **overrides) for i in range(count)]


def test_surplus_in_one_period_cannot_hide_another_period_shortage():
    result = history_mcq_inventory([unit('a'), unit('b')], items('a', 50) + items('b', 6), forms=2, questions_per_form=10)
    assert result['periods'][1]['shortfall_to_minimum'] == 2
    assert result['usable_inventory_after_period_caps'] == 18
    assert result['shortfall_after_period_caps'] == 2
    assert not result['necessary_inventory_checks_pass']


def test_inventory_bounds_can_pass_without_claiming_form_readiness():
    result = history_mcq_inventory([unit('a'), unit('b')], items('a', 10) + items('b', 10), forms=2, questions_per_form=10)
    assert result['necessary_inventory_checks_pass']
    assert 'Does not assemble forms' in result['limitations']


def test_unapproved_frq_unknown_and_ambiguous_duplicates_do_not_count():
    rows = items('a', 5)
    rows[0]['validation_status'] = 'draft'
    rows[1]['type'] = 'frq'
    rows.append(dict(rows[2], unit_name='b'))
    rows += items('unknown', 5)
    result = history_mcq_inventory([unit('a', 100, 100)], rows, forms=1, questions_per_form=2)
    assert result['periods'][0]['approved_unique_mcq'] == 2


def test_integer_rounding_and_incompatible_bounds():
    result = history_mcq_inventory([unit('a', 4, 6)], items('a', 20), forms=1, questions_per_form=55)
    assert result['periods'][0]['minimum_per_form'] == 3
    assert result['periods'][0]['maximum_per_form'] == 3
    assert not result['necessary_inventory_checks_pass']


@pytest.mark.parametrize('forms,size', [(0, 55), (4, 0), (True, 55), (4, 2.5)])
def test_invalid_form_parameters(forms, size):
    with pytest.raises(ValueError):
        history_mcq_inventory([], [], forms=forms, questions_per_form=size)


def test_current_history_bank_meets_necessary_inventory_checks_only():
    from scripts.seed_data.units_topics.us_history import UNITS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS
    result = history_mcq_inventory(UNITS, QUESTIONS)
    assert result['necessary_inventory_checks_pass']
    assert result['periods'][7]['shortfall_to_minimum'] == 0
    assert result['periods'][8]['shortfall_to_minimum'] == 0
    assert result['periods'][1]['shortfall_to_minimum'] == 0


def grouped(name, sizes):
    rows = []
    for group, size in enumerate(sizes):
        for i in range(size):
            rows.append(dict(unit_name=name, prompt=f'{name}:{group}:{i}', type='mcq',
                validation_status='approved', skill_tags=[f'stimulus:{name}:{group}']))
    return rows


def test_raw_counts_can_pass_while_whole_groups_cannot_fit():
    from scripts.history_readiness import source_group_inventory
    units = [unit('a', 100, 100)]
    rows = grouped('a', [3, 3, 2])
    assert history_mcq_inventory(units, rows, forms=2, questions_per_form=4)['necessary_inventory_checks_pass']
    assert not source_group_inventory(units, rows, forms=2, questions_per_form=4)['all_periods_packable']


def test_whole_group_packing_can_combine_and_skip_groups():
    from scripts.history_readiness import source_group_inventory
    result = source_group_inventory([unit('a', 100, 100)], grouped('a', [3, 2, 1, 2, 5]), forms=2, questions_per_form=4)
    assert result['all_periods_packable']
    assert result['periods'][0]['example_period_counts'] == [4, 4]


def test_partial_approval_excludes_whole_source_group():
    from scripts.history_readiness import source_group_inventory
    rows = grouped('a', [3])
    rows[0]['validation_status'] = 'draft'
    result = source_group_inventory([unit('a', 100, 100)], rows, forms=1, questions_per_form=2)
    assert not result['all_periods_packable']
    assert result['excluded_groups'][0]['reason'] == 'ineligible_group_member'


def test_cross_period_group_is_not_silently_split():
    from scripts.history_readiness import source_group_inventory
    rows = grouped('a', [2])
    rows[1]['unit_name'] = 'b'
    result = source_group_inventory([unit('a'), unit('b')], rows, forms=1, questions_per_form=2)
    assert result['excluded_groups'][0]['reason'] == 'cross_period_group'
    assert not result['all_periods_packable']


def test_ambiguous_members_invalidate_related_groups():
    from scripts.history_readiness import source_group_inventory
    rows = grouped('a', [2])
    rows[0]['skill_tags'].append('stimulus:other')
    result = source_group_inventory([unit('a', 100, 100)], rows, forms=1, questions_per_form=1)
    assert not result['all_periods_packable']
    assert any(x['reason'] == 'ambiguous_group_member' for x in result['excluded_groups'])


def test_current_bank_needs_period_two_group_combinations():
    from scripts.history_readiness import source_group_inventory
    from scripts.seed_data.units_topics.us_history import UNITS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS
    result = source_group_inventory(UNITS, QUESTIONS)
    assert [p['unit'] for p in result['periods'] if not p['whole_group_allocation_possible']] == [UNITS[1]['name']]
