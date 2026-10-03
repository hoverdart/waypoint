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
    return {
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
            row.update(status='live_bank_requires_depth_review', coverage=audit_bank(units, questions))
        elif code == 'english-language':
            from scripts.seed_data.units_topics.english_language import UNITS
            from scripts.seed_data.questions.english_language_questions import QUESTIONS
            row.update(status='in_development', coverage=audit_bank(UNITS, QUESTIONS))
        rows.append(row)
    return rows


if __name__ == '__main__':
    print(json.dumps({'note': 'Structural coverage only; not educator certification or official AP equivalence.', 'courses': report()}, indent=2))
