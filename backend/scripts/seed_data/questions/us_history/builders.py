"""Assembly for individually authored history items with visible provenance."""
import re


def source_set(*, period, topic, code, source_url, source_kind, stimulus, items, set_id=None):
    """Use a stable set_id when adding another stimulus for an existing CED topic.

    Omitting it retains existing item identifiers for previously seeded content.
    """
    if set_id is not None and (not isinstance(set_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", set_id)):
        raise ValueError("set_id must be a nonempty lowercase alphanumeric slug")
    identity = code if set_id is None else f"{code}-{set_id}"
    if source_kind not in {'primary excerpt', 'original instructional summary'}:
        raise ValueError('Identify the nature of the historical stimulus')
    questions = []
    for number, (skill, difficulty, stem, correct, choices) in enumerate(items, 1):
        if len(choices) != 4 or len({text for text, _ in choices}) != 4 or not 0 <= correct < 4:
            raise ValueError('Four distinct options and one correct answer required')
        questions.append(dict(unit_name=period, topic_name=topic, type='mcq', difficulty=difficulty,
            prompt=f'{source_kind.capitalize()}:\n{stimulus}\n\nSource reference: {source_url}\n\n{stem}',
            correct_answer='ABCD'[correct], source='generated', validation_status='approved',
            skill_tags=[skill, f'ced:{code}', 'format:source-mcq', f'stimulus:ush-{identity}', f'item:ush-{identity}-{number}'],
            misconception_tags=[], rubric_json=None,
            options=[dict(label='ABCD'[i], text=text, is_correct=i == correct) for i, (text, _) in enumerate(choices)],
            explanations=[dict(option_label='ABCD'[i], explanation=reason, misconception_tag=None) for i, (_, reason) in enumerate(choices)]))
    return questions
