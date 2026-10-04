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


def source_group_inventory(units, questions, *, forms=4, questions_per_form=55):
    """Check per-period packing without splitting/reusing source sets.

    This is deliberately a separate gate: feasible period allocations do not
    prove that combined forms have the requested length or balanced skills.
    """
    raw = history_mcq_inventory(units, questions, forms=forms, questions_per_form=questions_per_form)
    known = {u['name'] for u in units}
    prompts = Counter(q['prompt'].strip() for q in questions)
    groups = {}
    invalid = []
    ambiguous_tags = set()
    for index, q in enumerate(questions):
        tags = sorted({t for t in q.get('skill_tags', []) if t.startswith('stimulus:')})
        if len(tags) > 1:
            ambiguous_tags.update(tags)
            invalid.append({'question_index': index, 'reason': 'multiple_stimulus_groups'})
            continue
        identity = tags[0] if tags else f'ungrouped:{index}'
        groups.setdefault(identity, []).append(q)
    eligible = {name: [] for name in known}
    for identity, members in groups.items():
        if identity in ambiguous_tags:
            invalid.append({'group': identity, 'reason': 'ambiguous_group_member'})
            continue
        periods = {q['unit_name'] for q in members}
        if len(periods) != 1:
            invalid.append({'group': identity, 'reason': 'cross_period_group'})
            continue
        period = next(iter(periods))
        if period not in known:
            continue
        if not all(q['type'] == 'mcq' and q.get('validation_status') == 'approved'
                   and prompts[q['prompt'].strip()] == 1 for q in members):
            # Partial approval or duplicate copies must not silently truncate a set.
            invalid.append({'group': identity, 'reason': 'ineligible_group_member'})
            continue
        eligible[period].append(len(members))
    results = []
    for period in raw['periods']:
        low, high = period['minimum_per_form'], period['maximum_per_form']
        sizes = eligible[period['unit']]
        # Canonical sorted bins collapse permutations of equivalent forms.
        states = {(0,) * forms}
        for size in sizes:
            updated = set(states)  # Groups may be left unused.
            for state in states:
                for slot in range(forms):
                    if state[slot] + size <= high:
                        counts = list(state)
                        counts[slot] += size
                        updated.add(tuple(sorted(counts)))
            states = updated
        allocations = sorted(state for state in states if all(low <= n <= high for n in state))
        results.append({'unit': period['unit'], 'group_sizes': sorted(sizes),
            'minimum_per_form': low, 'maximum_per_form': high,
            'whole_group_allocation_possible': bool(allocations),
            'example_period_counts': list(allocations[0]) if allocations else None})
    return {'periods': results, 'excluded_groups': invalid,
        'all_periods_packable': all(p['whole_group_allocation_possible'] for p in results),
        'limitations': 'Per-period packing only; does not assemble complete forms, balance skills, or establish educational quality.'}
