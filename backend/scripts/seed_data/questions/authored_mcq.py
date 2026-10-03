"""Convert checked-in original question records into the common seed schema.

No question generation or external service runs at application request time.
"""


def build_questions(units, items):
    topic_to_unit = {topic['name']: unit['name'] for unit in units for topic in unit['topics']}
    result = []
    for index, (topic, prompt, correct, distractors, reasoning) in enumerate(items):
        choices = list(distractors)
        position = index % 4
        choices.insert(position, correct)
        result.append({
            'unit_name': topic_to_unit[topic], 'topic_name': topic,
            'type': 'mcq', 'difficulty': 2 if index % 3 else 3,
            'prompt': prompt, 'correct_answer': 'ABCD'[position],
            'source': 'generated', 'validation_status': 'approved',
            'skill_tags': ['concept-application'], 'misconception_tags': [],
            'options': [{'label': 'ABCD'[i], 'text': text, 'is_correct': i == position}
                        for i, text in enumerate(choices)],
            'explanations': [{'option_label': 'ABCD'[i], 'explanation': reasoning,
                              'misconception_tag': None} for i in range(4)],
            'rubric_json': None,
        })
    return result
