"""Necessary inventory checks, not an exam assembler or educational certification."""
from collections import Counter
from math import ceil, floor


def history_mcq_inventory(units, questions, *, forms=4, questions_per_form=55):
    if type(forms) is not int or forms < 1 or type(questions_per_form) is not int or questions_per_form < 1:
        raise ValueError('Form count and questions per form must be positive integers')
    known = {u['name'] for u in units}
    # A repeated prompt must not count as independent inventory, even if it is
    # assigned to different topics or periods. Exclude all ambiguous copies.
    prompt_counts = Counter(q['prompt'].strip() for q in questions)
    inventory = Counter(q['unit_name'] for q in questions
        if q['type'] == 'mcq' and q.get('validation_status') == 'approved'
        and q['unit_name'] in known and prompt_counts[q['prompt'].strip()] == 1)
    periods = []
    for unit in units:
        minimum = ceil(questions_per_form * unit['ap_weight_min'] / 100)
        maximum = floor(questions_per_form * unit['ap_weight_max'] / 100)
        available = inventory[unit['name']]
        periods.append({
            'unit': unit['name'], 'approved_unique_mcq': available,
            'minimum_per_form': minimum, 'maximum_per_form': maximum,
            'minimum_for_all_forms': minimum * forms,
            'shortfall_to_minimum': max(0, minimum * forms - available),
            'usable_with_period_cap': min(available, maximum * forms),
        })
    total_needed = forms * questions_per_form
    usable = sum(p['usable_with_period_cap'] for p in periods)
    minimums_fit = sum(p['minimum_per_form'] for p in periods) <= questions_per_form
    maximums_fit = sum(p['maximum_per_form'] for p in periods) >= questions_per_form
    possible_bounds = all(p['minimum_per_form'] <= p['maximum_per_form'] for p in periods)
    return {
        'forms': forms, 'questions_per_form': questions_per_form, 'required_mcq': total_needed,
        'periods': periods,
        'usable_inventory_after_period_caps': usable,
        'shortfall_after_period_caps': max(0, total_needed - usable),
        'necessary_inventory_checks_pass': minimums_fit and maximums_fit and possible_bounds
            and usable >= total_needed and all(not p['shortfall_to_minimum'] for p in periods),
        'limitations': 'Necessary inventory checks only. Does not assemble forms or verify stimulus-group integrity, skill balance, source diversity, difficulty, historical accuracy, or educator review.',
    }
