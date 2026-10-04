"""Assembly for individually authored history items with visible provenance."""
def source_set(*, period, topic, code, source_url, source_kind, stimulus, items):
    if source_kind not in {'primary excerpt', 'original instructional summary'}:
        raise ValueError('Identify the nature of the historical stimulus')
    questions = []
    for number, (skill, difficulty, stem, correct, choices) in enumerate(items, 1):
        if len(choices) != 4 or len({text for text, _ in choices}) != 4 or not 0 <= correct < 4:
            raise ValueError('Four distinct options and one correct answer required')
        questions.append(dict(unit_name=period, topic_name=topic, type='mcq', difficulty=difficulty,
            prompt=f'{source_kind.capitalize()}:\n{stimulus}\n\nSource reference: {source_url}\n\n{stem}',
            correct_answer='ABCD'[correct], source='generated', validation_status='approved',
            skill_tags=[skill, f'ced:{code}', 'format:source-mcq', f'stimulus:ush-{code}', f'item:ush-{code}-{number}'],
            misconception_tags=[], rubric_json=None,
            options=[dict(label='ABCD'[i], text=text, is_correct=i == correct) for i, (text, _) in enumerate(choices)],
            explanations=[dict(option_label='ABCD'[i], explanation=reason, misconception_tag=None) for i, (_, reason) in enumerate(choices)]))
    return questions
