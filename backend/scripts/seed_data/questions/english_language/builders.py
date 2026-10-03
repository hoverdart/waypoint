"""Strict assembly of independently written passage questions; no template variants."""
from scripts.seed_data.units_topics.english_language import SKILLS, UNIT_SKILLS


def passage_questions(*, passage_id, title, context, passage, mode, items):
    """Items: (unit, skill, difficulty, stem, correct_index, [(choice, rationale)])."""
    if mode not in ('reading', 'writing'):
        raise ValueError('Unknown passage mode')
    questions = []
    for number, (unit, skill, difficulty, stem, correct, choices) in enumerate(items, start=1):
        if skill not in UNIT_SKILLS[unit - 1] or len(choices) != 4 or not 0 <= correct < 4:
            raise ValueError(f'Invalid mapping/choices in {passage_id}:{number}')
        if len({text for text, _ in choices}) != 4 or any(not explanation.strip() for _, explanation in choices):
            raise ValueError('Unique choices and individual rationales are required')
        questions.append({
            'unit_name': f'Unit {unit}', 'topic_name': f'{skill}: {SKILLS[skill]}',
            'type': 'mcq', 'difficulty': difficulty,
            'prompt': f'{title}\n\n{context}\n\n{passage}\n\n{stem}',
            'correct_answer': 'ABCD'[correct], 'source': 'generated', 'validation_status': 'approved',
            'skill_tags': [f'ap-skill:{skill}', f'format:{mode}', f'stimulus:{passage_id}', f'item:{passage_id}-{number:02d}'],
            'misconception_tags': [], 'rubric_json': None,
            'options': [{'label': 'ABCD'[i], 'text': text, 'is_correct': i == correct} for i, (text, _) in enumerate(choices)],
            'explanations': [{'option_label': 'ABCD'[i], 'explanation': reason, 'misconception_tag': None} for i, (_, reason) in enumerate(choices)],
        })
    return questions
