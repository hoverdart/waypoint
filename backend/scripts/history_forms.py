"""Offline draft MCQ assembly; nothing is published by this script."""
import hashlib
import json
from collections import Counter
from math import ceil, floor

REQUIRED_SKILLS = frozenset({'sourcing', 'claims-evidence', 'contextualization',
    'comparison', 'causation', 'continuity-and-change'})

PERIOD_COUNTS = (3, 4, 9, 9, 9, 6, 6, 6, 3)


def assemble_draft_forms(units, questions):
    if len(units) != 9:
        raise ValueError('The blueprint requires nine periods')
    for unit, target in zip(units, PERIOD_COUNTS):
        if not ceil(55 * unit['ap_weight_min'] / 100) <= target <= floor(55 * unit['ap_weight_max'] / 100):
            raise ValueError('Blueprint conflicts with period weights')
    prompts = Counter(q['prompt'].strip() for q in questions)
    groups = {}
    for index, q in enumerate(questions):
        tags = {t for t in q.get('skill_tags', []) if t.startswith('stimulus:')}
        if len(tags) > 1:
            raise ValueError('Ambiguous source-group assignment')
        key = next(iter(tags)) if tags else f'ungrouped:{index}'
        groups.setdefault(key, []).append(q)
    eligible = {u['name']: [] for u in units}
    for key, rows in groups.items():
        periods = {q['unit_name'] for q in rows}
        if len(periods) != 1:
            raise ValueError('Source group spans multiple periods')
        period = next(iter(periods))
        if period in eligible and all(q['type'] == 'mcq' and q.get('validation_status') == 'approved'
                and prompts[q['prompt'].strip()] == 1 for q in rows):
            eligible[period].append((key, rows))
    form_groups = [[] for _ in range(4)]
    for unit, target in zip(units, PERIOD_COUNTS):
        states = {(0, 0, 0, 0): ((), (), (), ())}
        goal = (target,) * 4
        for key, rows in eligible[unit['name']]:
            updated = dict(states)
            for counts, allocations in states.items():
                for slot in range(4):
                    if counts[slot] + len(rows) > target:
                        continue
                    next_counts = list(counts)
                    next_counts[slot] += len(rows)
                    next_counts = tuple(next_counts)
                    if next_counts not in updated:
                        next_allocations = list(allocations)
                        next_allocations[slot] += (key,)
                        updated[next_counts] = tuple(next_allocations)
            states = updated
            if goal in states:
                break
        if goal not in states:
            raise ValueError(f'Cannot pack blueprint for {unit["name"]} without splitting sources')
        for slot, keys in enumerate(states[goal]):
            for key in keys:
                form_groups[slot].append(key)
    eligible_groups = {key: rows for entries in eligible.values() for key, rows in entries}
    form_groups = balance_skills(form_groups, eligible_groups)
    return [sum((groups[key] for key in keys), []) for keys in form_groups]


def balance_skills(form_groups, groups):
    """Deterministic improving swaps, never a proof of global infeasibility.

    Equal-size, same-period exchanges preserve all assembly constraints. If
    local search cannot satisfy the minimum, fail closed for editorial repair.
    """
    skills = {key: {tag for q in rows for tag in q.get('skill_tags', [])} for key, rows in groups.items()}
    def missing(keys):
        return len(REQUIRED_SKILLS - set().union(*(skills[key] for key in keys)))
    selected = [list(keys) for keys in form_groups]
    while True:
        deficits = [missing(keys) for keys in selected]
        if not any(deficits):
            return selected
        owners = {key: (i, j) for i, keys in enumerate(selected) for j, key in enumerate(keys)}
        improved = False
        for recipient, keys in enumerate(selected):
            if not deficits[recipient]:
                continue
            for position, old in enumerate(keys):
                for candidate, rows in groups.items():
                    owner = owners.get(candidate)
                    if owner and owner[0] == recipient:
                        continue
                    if len(rows) != len(groups[old]) or rows[0]['unit_name'] != groups[old][0]['unit_name']:
                        continue
                    proposal = [list(form) for form in selected]
                    proposal[recipient][position] = candidate
                    if owner:
                        proposal[owner[0]][owner[1]] = old
                    if sum(missing(form) for form in proposal) < sum(deficits):
                        selected = proposal
                        improved = True
                        break
                if improved:
                    break
            if improved:
                break
        if not improved:
            raise ValueError('Skill coverage unmet by local group swaps; review content or assembly strategy')


def manifest(units, questions):
    return {
        'status': 'offline_draft_not_published',
        'required_skills': sorted(REQUIRED_SKILLS),
        'limitations': 'Minimum skill-tag presence, period balance and source integrity only; tag accuracy, source variety, difficulty and historical quality require review. No FRQ sections included.',
        'forms': [dict(name=f'History draft {i + 1}', question_count=len(rows),
            periods=dict(Counter(q['unit_name'] for q in rows)),
            skills=dict(Counter(t for q in rows for t in q.get('skill_tags', []) if ':' not in t)),
            questions=[dict(prompt_sha256=hashlib.sha256(q['prompt'].encode()).hexdigest(),
                item_tags=[t for t in q.get('skill_tags', []) if t.startswith('item:')],
                stimulus_tags=[t for t in q.get('skill_tags', []) if t.startswith('stimulus:')]) for q in rows])
            for i, rows in enumerate(assemble_draft_forms(units, questions))],
    }


if __name__ == '__main__':
    from scripts.seed_data.units_topics.us_history import UNITS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS
    print(json.dumps(manifest(UNITS, QUESTIONS), indent=2))
