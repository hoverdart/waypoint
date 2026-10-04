"""Offline draft MCQ assembly; nothing is published by this script."""
import hashlib
import json
from collections import Counter
from math import ceil, floor

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
    forms = [[] for _ in range(4)]
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
                forms[slot].extend(groups[key])
    return forms


def manifest(units, questions):
    return {
        'status': 'offline_draft_not_published',
        'limitations': 'Period balance and source integrity only; skills, source variety, difficulty and historical quality require review. No FRQ sections included.',
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
