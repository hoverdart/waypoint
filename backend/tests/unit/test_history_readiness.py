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


def test_current_history_bank_still_has_period_two_inventory_shortage():
    from scripts.seed_data.units_topics.us_history import UNITS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS
    result = history_mcq_inventory(UNITS, QUESTIONS)
    assert not result['necessary_inventory_checks_pass']
    assert result['periods'][7]['shortfall_to_minimum'] == 0
    assert result['periods'][8]['shortfall_to_minimum'] == 0
    assert result['periods'][1]['shortfall_to_minimum'] == 1
