from scripts.content_audit import audit_bank


def test_audit_identifies_specific_depth_gaps_in_curriculum_order():
    units = [{'name': 'Period', 'topics': [
        {'name': 'Second', 'display_order': 2, 'skill_tags': ['ced:4.2']},
        {'name': 'First', 'display_order': 1, 'skill_tags': ['ced:4.1']},
        {'name': 'Empty', 'display_order': 3},
    ]}]
    questions = [
        dict(unit_name='Period', topic_name=topic, type=kind, difficulty=level,
             skill_tags=['stimulus:shared'])
        for topic, kind, level in [('First', 'mcq', 2), ('First', 'mcq', 3), ('First', 'frq', 4), ('Second', 'mcq', 2)]
    ]
    questions.append(dict(unit_name='Period', topic_name='Typo', type='mcq', difficulty=2))
    result = audit_bank(units, questions)
    first, second, empty = result['topic_details']
    assert [t['topic'] for t in result['topic_details']] == ['First', 'Second', 'Empty']
    assert first['curriculum_codes'] == ['4.1']
    assert first['difficulty_levels'] == [2, 3, 4]
    assert first['stimulus_groups'] == 1
    assert first['question_types'] == {'mcq': 2, 'frq': 1}
    assert not first['needs_more_questions'] and not first['needs_difficulty_variety']
    assert second['needs_more_questions'] and second['needs_difficulty_variety']
    assert empty['questions'] == 0 and empty['curriculum_codes'] == []
    assert result['unmapped_question_topics'] == [{'unit': 'Period', 'topic': 'Typo', 'questions': 1}]
    assert result['topics_below_three_questions'] == 2


def test_live_history_audit_reports_real_remaining_depth_gaps():
    from scripts.seed_data.units_topics.us_history import UNITS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS
    result = audit_bank(UNITS, QUESTIONS)
    assert not result['unmapped_question_topics']
    assert sum(t['questions'] for t in result['topic_details']) == len(QUESTIONS)
    assert result['topics_below_three_questions'] == sum(t['needs_more_questions'] for t in result['topic_details'])
    assert any(t['needs_more_questions'] for t in result['topic_details'])
