"""Report content depth independently of app readiness or editorial approval.

Run `python -m scripts.content_audit` from backend/. Counts never imply official
exam equivalence. Draft course banks are audited before enabling enrollment.
"""
import importlib
import json
from collections import Counter

from scripts.seed import SUBJECT_MODULES
from scripts.seed_data.rollout import COURSE_ROLLOUT, PARTICIPATION_YEAR


def audit_bank(units, questions):
    topics = {(u['name'], t['name']) for u in units for t in u['topics']}
    mapped = Counter((q['unit_name'], q['topic_name']) for q in questions)
    by_topic_difficulty = {topic: {q['difficulty'] for q in questions if (q['unit_name'], q['topic_name']) == topic} for topic in topics}
    stimuli = {tag for q in questions for tag in q.get('skill_tags', []) if tag.startswith('stimulus:')}
    formats = Counter(tag.removeprefix('format:') for q in questions for tag in q.get('skill_tags', []) if tag.startswith('format:'))
    topic_details = []
    for unit in units:
        for topic in sorted(unit['topics'], key=lambda t: t.get('display_order', 0)):
            key = (unit['name'], topic['name'])
            entries = [q for q in questions if (q['unit_name'], q['topic_name']) == key]
            curriculum_codes = {tag.removeprefix('ced:') for tag in topic.get('skill_tags', []) if tag.startswith('ced:')}
            question_codes = Counter(code for q in entries for code in {
                tag.removeprefix('ced:') for tag in q.get('skill_tags', []) if tag.startswith('ced:')
            })
            topic_details.append({
                'unit': key[0], 'topic': key[1],
                'curriculum_codes': sorted(curriculum_codes),
                'question_curriculum_counts': dict(sorted(question_codes.items())),
                'curriculum_codes_without_tagged_questions': sorted(curriculum_codes - question_codes.keys()),
                'question_codes_outside_topic_mapping': sorted(question_codes.keys() - curriculum_codes),
                'questions_without_curriculum_codes': sum(
                    not any(tag.startswith('ced:') for tag in q.get('skill_tags', [])) for q in entries
                ),
                'questions': len(entries),
                'difficulty_levels': sorted(by_topic_difficulty[key]),
                'stimulus_groups': len({t for q in entries for t in q.get('skill_tags', []) if t.startswith('stimulus:')}),
                'question_types': dict(Counter(q['type'] for q in entries)),
                'needs_more_questions': len(entries) < 3,
                'needs_difficulty_variety': len(by_topic_difficulty[key]) < 2,
            })
    return {
        'topic_details': topic_details,
        'unmapped_question_topics': [
            {'unit': key[0], 'topic': key[1], 'questions': count}
            for key, count in sorted(mapped.items()) if key not in topics
        ],
        'units': len(units), 'topics': len(topics), 'questions': len(questions),
        'mcq': sum(q['type'] == 'mcq' for q in questions),
        'frq': sum(q['type'] == 'frq' for q in questions),
        'independent_stimuli': len(stimuli), 'formats': dict(formats),
        'uncovered_topics': [f'{unit} / {topic}' for unit, topic in sorted(topics) if not mapped[(unit, topic)]],
        'topics_below_three_questions': sum(mapped[topic] < 3 for topic in topics),
        'topics_without_difficulty_variety': sum(len(by_topic_difficulty[topic]) < 2 for topic in topics),
    }


def report():
    rows = []
    for rank, (code, name, count) in enumerate(COURSE_ROLLOUT, start=1):
        row = {'priority': rank if count is not None else None, 'code': code, 'name': name,
               'exam_count': count, 'participation_year': PARTICIPATION_YEAR if count is not None else None,
               'status': 'not_started'}
        if code in SUBJECT_MODULES:
            unit_module, question_module = SUBJECT_MODULES[code]
            units = importlib.import_module(f'scripts.seed_data.{unit_module}').UNITS
            questions = importlib.import_module(f'scripts.seed_data.{question_module}').QUESTIONS
            row.update(status='live_expanded_bank' if code == 'english-language' else 'live_bank_requires_depth_review', coverage=audit_bank(units, questions))
            if code == 'us-history':
                from scripts.history_readiness import history_mcq_inventory
                row['mcq_form_inventory'] = history_mcq_inventory(units, questions)
        rows.append(row)
    return rows


if __name__ == '__main__':
    print(json.dumps({'note': 'Structural coverage only; not educator certification or official AP equivalence.', 'courses': report()}, indent=2))
