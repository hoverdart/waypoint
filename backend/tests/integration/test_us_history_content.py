import importlib

import pytest

from sqlmodel import select

from app.models.subject import Unit
from scripts.seed import seed_subject
from scripts.seed_data.units_topics.us_history import UNITS


def test_history_period_weights_match_current_official_framework(db_session):
    expected = [(4, 6), (6, 8)] + [(10, 17)] * 6 + [(4, 6)]
    assert [(u['ap_weight_min'], u['ap_weight_max']) for u in UNITS] == expected
    data = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, data)
    unit = db_session.exec(select(Unit).where(Unit.name == 'Period 2: 1607-1754')).one()
    unit.ap_weight_min, unit.ap_weight_max = 4, 6
    db_session.add(unit)
    db_session.flush()
    unit_id = unit.id
    seed_subject(db_session, data)
    db_session.refresh(unit)
    assert unit.id == unit_id
    assert (unit.ap_weight_min, unit.ap_weight_max) == (6, 8)


def test_period_one_additions_cover_missing_framework_topics_and_preserve_ids(db_session):
    from app.models.subject import Topic
    from app.models.question import Question
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_one_expansion import QUESTIONS
    assert len(UNITS[0]['topics']) == 7
    assert {t for topic in UNITS[0]['topics'] for t in topic['skill_tags'] if t.startswith('ced:')} == {f'ced:1.{i}' for i in range(1, 8)}
    assert len(QUESTIONS) == 9
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert 'not a primary-source quotation' in q['prompt']
        assert 'Research reference: https://' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    data = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, data)
    topics = {t.name: t.id for t in db_session.exec(select(Topic)).all()}
    questions = {q.id for q in db_session.exec(select(Question)).all()}
    seed_subject(db_session, data)
    assert {t.name: t.id for t in db_session.exec(select(Topic)).all()} == topics
    assert {q.id for q in db_session.exec(select(Question)).all()} == questions
    assert len(questions) == 312


def test_period_two_maps_all_topics_and_distinguishes_primary_evidence():
    from collections import Counter
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_two_expansion import QUESTIONS
    assert len(UNITS[1]['topics']) == 8
    assert {t for topic in UNITS[1]['topics'] for t in topic['skill_tags'] if t.startswith('ced:')} == {f'ced:2.{i}' for i in range(1, 9)}
    assert len(QUESTIONS) == 12
    assert set(Counter(q['topic_name'] for q in QUESTIONS).values()) == {3}
    assert sum(q['prompt'].startswith('Primary excerpt:') for q in QUESTIONS) == 3
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[1]['topics']}
        assert q['unit_name'] == UNITS[1]['name']
        assert 'Source reference: https://' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_founding_text_sets_have_provenance_and_original_valid_questions():
    from collections import Counter
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_founding import QUESTIONS
    assert len(QUESTIONS) == 8
    assert set(Counter(q['topic_name'] for q in QUESTIONS).values()) == {4}
    for q in QUESTIONS:
        assert q['prompt'].startswith('Primary excerpt:')
        assert 'https://www.archives.gov/founding-docs/' in q['prompt']
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_western_expansion_source_set_validates_and_uses_distinct_skills():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_expansion import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    assert len({q['skill_tags'][0] for q in QUESTIONS}) == 4
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        assert 'ced:3.12' in q['skill_tags']
        assert q['prompt'].startswith('Primary excerpt:')
        assert 'https://www.archives.gov/milestone-documents/northwest-ordinance' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_confederation_and_ratification_sets_have_valid_keys_and_topic_alignment():
    from collections import Counter
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_ratification import QUESTIONS
    assert len(QUESTIONS) == 8
    assert set(Counter(q['topic_name'] for q in QUESTIONS).values()) == {4}
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topics = {t['name']: t for t in UNITS[2]['topics']}
    for q in QUESTIONS:
        assert q['prompt'].startswith('Primary excerpt:')
        assert 'Source reference: https://www.archives.gov/' in q['prompt']
        code = next(t for t in q['skill_tags'] if t.startswith('ced:'))
        assert code in topics[q['topic_name']]['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    for code in ('ced:3.7', 'ced:3.8'):
        assert {q['correct_answer'] for q in QUESTIONS if code in q['skill_tags']} == set('ABCD')


def test_revolutionary_rights_questions_distinguish_advocacy_from_outcomes():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_rights import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        assert 'ced:3.6' in q['skill_tags']
        assert q['prompt'].startswith('Primary excerpt:')
        assert 'Abigail Adams to John Adams, March 31, 1776' in q['prompt']
        assert 'Source reference: https://www.battlefields.org/' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_national_identity_source_questions_validate_and_identify_transcription():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_identity import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        assert 'ced:3.11' in q['skill_tags']
        assert 'spelling and punctuation modernized' in q['prompt']
        assert 'Source reference: https://www.senate.gov/' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_three_context_identifies_original_summary_and_validates():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_context import QUESTIONS
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        assert 'ced:3.1' in q['skill_tags']
        assert q['prompt'].startswith('Original instructional summary:')
        assert 'not a primary-source quotation' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_continuity_questions_validate_and_map_to_period_three():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_continuity import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        assert 'ced:3.13' in q['skill_tags']
        assert q['prompt'].startswith('Primary excerpt:')
        assert 'Source reference: https://www.archives.gov/' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_revolutionary_war_questions_validate_with_visible_summary_provenance():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_three_war import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[2]['topics']}
        assert 'ced:3.5' in q['skill_tags']
        assert q['prompt'].startswith('Original instructional summary:')
        assert 'not a primary-source quotation' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_three_sequence_maps_all_codes_and_reseeds_without_replacing_topics(db_session):
    from app.models.subject import Topic
    from app.models.question import Question
    expected = [
        'Contextualizing Period 3', "The Seven Years' War (French and Indian War)",
        'Taxation Without Representation and the Road to Revolution',
        'Political Ideas of the Revolution', 'The American Revolutionary War',
        'Influence of Revolutionary Ideals', "The American Revolution's Effects",
        'Government Under the Articles of Confederation',
        'The Articles of Confederation and the Constitution',
        'Constitutional Convention and Ratification', 'Constitutional Structure and Federal Power',
        'Washington, Hamilton, and the New Government', 'Developing an American Identity',
        'Movement in the Early Republic', 'Continuity and Change in Period 3',
    ]
    assert [t['name'] for t in UNITS[2]['topics']] == expected
    assert [t['display_order'] for t in UNITS[2]['topics']] == list(range(1, 16))
    assert {tag for t in UNITS[2]['topics'] for tag in t['skill_tags'] if tag.startswith('ced:')} == {f'ced:3.{i}' for i in range(1, 14)}
    subject = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, subject)
    unit = db_session.exec(select(Unit).where(Unit.name == 'Period 3: 1754-1800')).one()
    topics = db_session.exec(select(Topic).where(Topic.unit_id == unit.id)).all()
    ids = {t.name: t.id for t in topics}
    question_topics = {q.id: q.topic_id for q in db_session.exec(select(Question)).all()}
    for topic in topics:
        topic.display_order = 99
        topic.skill_tags = []
        db_session.add(topic)
    db_session.flush()
    seed_subject(db_session, subject)
    db_session.expire_all()
    restored = db_session.exec(select(Topic).where(Topic.unit_id == unit.id).order_by(Topic.display_order)).all()
    assert [t.name for t in restored] == expected
    assert {t.name: t.id for t in restored} == ids
    assert all(any(tag.startswith('ced:') for tag in t.skill_tags) for t in restored)
    assert {q.id: q.topic_id for q in db_session.exec(select(Question)).all()} == question_topics


def test_period_four_diplomacy_validates_and_identifies_excerpt_omission():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_diplomacy import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['unit_name'] == UNITS[3]['name']
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.4' in q['skill_tags']
        assert 'Ellipsis indicates omitted words.' in q['prompt']
        assert 'Source reference: https://www.archives.gov/' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_reform_set_validates_and_has_stable_named_stimulus():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_reform import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['unit_name'] == UNITS[3]['name']
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.11' in q['skill_tags']
        assert 'stimulus:ush-4.11-seneca-falls' in q['skill_tags']
        assert 'Source reference: https://www.nps.gov/' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_removal_set_validates_and_keeps_presidential_claim_attributed():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_removal import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['unit_name'] == UNITS[3]['name']
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.8' in q['skill_tags']
        assert 'stimulus:ush-4.8-removal-message' in q['skill_tags']
        assert 'Andrew Jackson, annual message to Congress' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_cherokee_petition_set_adds_distinct_perspective_without_identifier_collision():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_cherokee import QUESTIONS
    from scripts.seed_data.questions.us_history.period_four_removal import QUESTIONS as OTHER
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    ids = lambda bank: {t for q in bank for t in q['skill_tags'] if t.startswith(('item:', 'stimulus:'))}
    assert ids(QUESTIONS).isdisjoint(ids(OTHER))
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.8' in q['skill_tags']
        assert 'National Archives Identifier 2127291' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_bank_war_source_set_validates_with_distinct_identity():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_bank import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'stimulus:ush-4.8-bank-veto' in q['skill_tags']
        assert 'July 10, 1832' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_nullification_set_validates_and_maps_to_federal_power():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_nullification import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'stimulus:ush-4.8-nullification' in q['skill_tags']
        assert q['prompt'].startswith('Original instructional summary:')
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_industrialization_set_validates_and_maps_to_new_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_industry import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.5' in q['skill_tags']
        assert q['prompt'].startswith('Original instructional summary:')
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_factory_workers_source_set_validates_and_maps_to_social_change():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_workers import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.6' in q['skill_tags']
        assert 'Sarah Bagley' in q['prompt']
        assert q['prompt'].startswith('Primary excerpt:')
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_four_context_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_context import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.1' in q['skill_tags']
        assert q['prompt'].startswith('Primary excerpt:')
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_louisiana_set_deepens_existing_topic_with_valid_content():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_louisiana import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'Markets and Westward Expansion'
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.2' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_regional_interests_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_regions import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.3' in q['skill_tags']
        assert 'except Missouri' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_revival_set_deepens_existing_topic_with_varied_difficulty():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_revival import QUESTIONS
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.10' in q['skill_tags']
        assert q['prompt'].startswith('Original instructional summary:')
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


@pytest.mark.parametrize("module", ["period_four_revival", "period_five_citizenship"])
def test_revised_distractors_reseed_in_place_with_matching_rationales(db_session, module):
    from app.models.question import Question, QuestionOption, QuestionExplanation
    QUESTIONS = importlib.import_module(f"scripts.seed_data.questions.us_history.{module}").QUESTIONS
    subject = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, subject)
    expected = {q['prompt']: q for q in QUESTIONS}
    questions = db_session.exec(select(Question).where(Question.prompt.in_(list(expected)))).all()
    assert len(questions) == 3
    original_ids = {}
    for question in questions:
        options = db_session.exec(select(QuestionOption).where(QuestionOption.question_id == question.id)).all()
        original_ids[question.prompt] = (question.id, {o.label: o.id for o in options})
        for option in options:
            if not option.is_correct:
                option.text = 'Outdated distractor'
                db_session.add(option)
    db_session.flush()
    seed_subject(db_session, subject)
    db_session.expire_all()
    for question in db_session.exec(select(Question).where(Question.prompt.in_(list(expected)))).all():
        data = expected[question.prompt]
        options = db_session.exec(select(QuestionOption).where(QuestionOption.question_id == question.id)).all()
        assert (question.id, {o.label: o.id for o in options}) == original_ids[question.prompt]
        assert {o.label: o.text for o in options} == {o['label']: o['text'] for o in data['options']}
        assert question.correct_answer == data['correct_answer']
        explanations = db_session.exec(select(QuestionExplanation).where(QuestionExplanation.question_id == question.id)).all()
        assert {e.option_id: e.explanation for e in explanations} == {
            next(o.id for o in options if o.label == e['option_label']): e['explanation']
            for e in data['explanations']
        }


def test_american_culture_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_culture import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.9' in q['skill_tags']
        assert 'Phi Beta Kappa Society' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_expanding_democracy_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_democracy import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topic = next(t for t in UNITS[3]['topics'] if t['name'] == 'Expanding Democracy')
    assert 'ced:4.7' in topic['skill_tags']
    for q in QUESTIONS:
        assert q['topic_name'] == topic['name']
        assert 'ced:4.7' in q['skill_tags']
        assert '$250 net freehold-property' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_black_institutions_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_black_institutions import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topic = next(t for t in UNITS[3]['topics'] if t['name'] == 'African Americans in the Early Republic')
    assert 'ced:4.12' in topic['skill_tags']
    for q in QUESTIONS:
        assert q['topic_name'] == topic['name']
        assert 'ced:4.12' in q['skill_tags']
        assert 'not a primary-source quotation' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_douglass_set_validates_with_distinct_stimulus_in_existing_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_douglass import QUESTIONS
    from scripts.seed_data.questions.us_history.period_four_black_institutions import QUESTIONS as OTHER
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    assert {tag for q in QUESTIONS for tag in q['skill_tags'] if tag.startswith('stimulus:')}.isdisjoint(
        {tag for q in OTHER for tag in q['skill_tags'] if tag.startswith('stimulus:')})
    for q in QUESTIONS:
        assert q['topic_name'] == 'African Americans in the Early Republic'
        assert 'ced:4.12' in q['skill_tags']
        assert '1845' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_four_legacy_mappings_reseed_without_replacing_topics(db_session):
    from app.models.subject import Topic
    expected = {
        'The Rise of Political Parties and Democracy': {'ced:4.2', 'ced:4.7', 'ced:4.8'},
        'Markets and Westward Expansion': {'ced:4.2', 'ced:4.5', 'ced:4.6'},
        'The Cotton Revolution and the Expansion of Slavery': {'ced:4.13'},
        'Religious Revival and Reform Movements': {'ced:4.10', 'ced:4.11'},
    }
    subject = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, subject)
    topics = db_session.exec(select(Topic).where(Topic.name.in_(list(expected)))).all()
    original = {t.name: t.id for t in topics}
    assert len(original) == 4
    for topic in topics:
        topic.skill_tags = [tag for tag in topic.skill_tags if not tag.startswith('ced:')]
        db_session.add(topic)
    db_session.flush()
    seed_subject(db_session, subject)
    db_session.expire_all()
    topics = db_session.exec(select(Topic).where(Topic.name.in_(list(expected)))).all()
    assert {t.name: t.id for t in topics} == original
    for topic in topics:
        assert {tag for tag in topic.skill_tags if tag.startswith('ced:')} == expected[topic.name]
        assert any(not tag.startswith('ced:') for tag in topic.skill_tags)


def test_period_four_complete_mapping_and_causation_set_validation():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_causation import QUESTIONS
    assert {tag for t in UNITS[3]['topics'] for tag in t['skill_tags'] if tag.startswith('ced:')} == {f'ced:4.{i}' for i in range(1, 15)}
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] in {t['name'] for t in UNITS[3]['topics']}
        assert 'ced:4.14' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_cotton_expansion_deepens_existing_topic_with_validated_items():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_four_cotton import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    topic = 'The Cotton Revolution and the Expansion of Slavery'
    assert len(QUESTIONS) == 3
    assert len([q for q in ALL if q['topic_name'] == topic]) == 4
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == topic
        assert 'ced:4.13' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_election_set_validates_and_period_four_has_basic_topic_depth():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_four_election import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'The Rise of Political Parties and Democracy'
        assert 'ced:4.7' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    details = [t for t in audit_bank(UNITS, ALL)['topic_details'] if t['unit'] == UNITS[3]['name']]
    assert details
    assert all(not t['needs_more_questions'] and not t['needs_difficulty_variety'] for t in details)


def test_mexican_war_set_validates_and_maps_to_period_five():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_treaty import QUESTIONS
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topic = next(t for t in UNITS[4]['topics'] if t['name'] == 'The Mexican-American War')
    assert 'ced:5.3' in topic['skill_tags']
    for q in QUESTIONS:
        assert q['unit_name'] == UNITS[4]['name']
        assert q['topic_name'] == topic['name']
        assert 'ced:5.3' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_five_legacy_codes_restore_metadata_and_preserve_topic_identity(db_session):
    from app.models.subject import Topic
    expected = {
        'Manifest Destiny and Continued Expansion': {'ced:5.2', 'ced:5.3'},
        'The Compromise of 1850 and Escalating Sectional Conflict': {'ced:5.4', 'ced:5.6'},
        'The Civil War': {'ced:5.7', 'ced:5.8'},
        'Reconstruction': {'ced:5.10', 'ced:5.11'},
    }
    subject = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, subject)
    topics = db_session.exec(select(Topic).where(Topic.name.in_(list(expected)))).all()
    original = {t.name: t.id for t in topics}
    assert len(original) == 4
    for topic in topics:
        topic.skill_tags = [tag for tag in topic.skill_tags if not tag.startswith('ced:')]
        db_session.add(topic)
    db_session.flush()
    seed_subject(db_session, subject)
    db_session.expire_all()
    topics = db_session.exec(select(Topic).where(Topic.name.in_(list(expected)))).all()
    assert {t.name: t.id for t in topics} == original
    for topic in topics:
        assert {tag for tag in topic.skill_tags if tag.startswith('ced:')} == expected[topic.name]
        assert any(not tag.startswith('ced:') for tag in topic.skill_tags)


def test_emancipation_set_validates_and_maps_to_wartime_policy():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_emancipation import QUESTIONS
    assert len(QUESTIONS) == 4
    assert {q['correct_answer'] for q in QUESTIONS} == set('ABCD')
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topic = next(t for t in UNITS[4]['topics'] if t['name'] == 'Government Policies During the Civil War')
    assert 'ced:5.9' in topic['skill_tags']
    for q in QUESTIONS:
        assert q['unit_name'] == UNITS[4]['name']
        assert q['topic_name'] == topic['name']
        assert 'ced:5.9' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_reconstruction_citizenship_set_validates_and_deepens_existing_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_citizenship import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert len([q for q in ALL if q['topic_name'] == 'Reconstruction']) == 7
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert 'ced:5.10' in q['skill_tags']
        assert 'subject to the jurisdiction thereof' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_compromise_set_validates_and_deepens_existing_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_compromise import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    topic = 'The Compromise of 1850 and Escalating Sectional Conflict'
    assert len(QUESTIONS) == 3
    assert len([q for q in ALL if q['topic_name'] == topic]) == 7
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == topic
        assert 'ced:5.4' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_kansas_set_validates_and_adds_failure_of_compromise_coverage():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_five_kansas import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert 'ced:5.6' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == QUESTIONS[0]['topic_name'])
    assert topic['question_curriculum_counts'] == {'5.4': 3, '5.6': 3}
    assert not topic['curriculum_codes_without_tagged_questions']


def test_period_five_context_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_context import QUESTIONS
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topic = next(t for t in UNITS[4]['topics'] if t['name'] == 'Contextualizing Period 5')
    assert 'ced:5.1' in topic['skill_tags']
    for q in QUESTIONS:
        assert q['topic_name'] == topic['name']
        assert q['unit_name'] == UNITS[4]['name']
        assert 'ced:5.1' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_five_regions_set_validates_and_maps_to_curriculum():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_regions import QUESTIONS
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    topic = next(t for t in UNITS[4]['topics'] if t['name'] == 'Sectional Conflict: Regional Differences')
    assert 'ced:5.5' in topic['skill_tags']
    for q in QUESTIONS:
        assert q['topic_name'] == topic['name']
        assert q['unit_name'] == UNITS[4]['name']
        assert 'ced:5.5' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_five_comparison_validates_and_completes_topic_code_mapping():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_comparison import QUESTIONS
    assert {tag for t in UNITS[4]['topics'] for tag in t['skill_tags'] if tag.startswith('ced:')} == {f'ced:5.{i}' for i in range(1, 13)}
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'Comparison in Period 5'
        assert q['unit_name'] == UNITS[4]['name']
        assert 'ced:5.12' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_vicksburg_set_validates_and_deepens_civil_war_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_vicksburg import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert len([q for q in ALL if q['topic_name'] == 'The Civil War']) == 7
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'The Civil War'
        assert 'ced:5.8' in q['skill_tags']
        assert 'Port Hudson' in q['prompt']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_oregon_set_validates_and_period_five_has_basic_topic_depth():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_five_oregon import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'Manifest Destiny and Continued Expansion'
        assert 'ced:5.2' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    details = [t for t in audit_bank(UNITS, ALL)['topic_details'] if t['unit'] == UNITS[4]['name']]
    assert len(details) == 9
    assert all(not t['needs_more_questions'] and not t['needs_difficulty_variety'] for t in details)


def test_secession_set_validates_and_adds_election_coverage():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_five_secession import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert 'ced:5.7' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'The Civil War')
    assert topic['question_curriculum_counts'] == {'5.7': 3, '5.8': 3}
    assert not topic['curriculum_codes_without_tagged_questions']


def test_enforcement_set_validates_and_covers_all_period_five_codes_with_items():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_five_enforcement import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'Reconstruction'
        assert 'ced:5.11' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    period = [q for q in ALL if q['unit_name'] == UNITS[4]['name']]
    assert {tag for q in period for tag in q['skill_tags'] if tag.startswith('ced:')} == {f'ced:5.{i}' for i in range(1, 13)}


def test_period_six_legacy_mapping_restores_tags_without_replacing_topics(db_session):
    from app.models.subject import Topic
    expected = {
        'Industrialization and Big Business': {'ced:6.5', 'ced:6.6'},
        'Immigration and Urbanization': {'ced:6.8'},
        'Labor and the Rise of Unions': {'ced:6.7'},
        'The Western Frontier and Native American Displacement': {'ced:6.2', 'ced:6.3'},
    }
    subject = {'name': 'AP US History', 'ap_exam_code': 'us-history', 'display_order': 2}
    seed_subject(db_session, subject)
    topics = db_session.exec(select(Topic).where(Topic.name.in_(list(expected)))).all()
    original = {t.name: t.id for t in topics}
    assert len(original) == 4
    for topic in topics:
        topic.skill_tags = [tag for tag in topic.skill_tags if not tag.startswith('ced:')]
        db_session.add(topic)
    db_session.flush()
    seed_subject(db_session, subject)
    db_session.expire_all()
    topics = db_session.exec(select(Topic).where(Topic.name.in_(list(expected)))).all()
    assert {t.name: t.id for t in topics} == original
    for topic in topics:
        assert {tag for tag in topic.skill_tags if tag.startswith('ced:')} == expected[topic.name]
        assert any(not tag.startswith('ced:') for tag in topic.skill_tags)


def test_period_six_south_and_exclusion_items_map_and_validate():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_six_south_and_exclusion import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    expected = {'The New South': '6.4', 'Responses to Immigration': '6.9'}
    report = audit_bank(UNITS, ALL)
    for name, code in expected.items():
        rows = [q for q in QUESTIONS if q['topic_name'] == name]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        topic = next(t for t in report['topic_details'] if t['topic'] == name)
        assert topic['question_curriculum_counts'] == {code: 3}
        assert not topic['curriculum_codes_without_tagged_questions']
        for q in rows:
            assert q['unit_name'] == 'Period 6: 1865-1898'
            assert f'ced:{code}' in q['skill_tags']
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_six_railroad_sets_validate_and_preserve_legacy_topic_coverage():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_six_railroads import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    report = audit_bank(UNITS, ALL)
    for name, code, total in [('Labor and the Rise of Unions', '6.7', 4),
                              ('Government and Economic Controversies', '6.12', 3)]:
        rows = [q for q in QUESTIONS if q['topic_name'] == name]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        topic = next(t for t in report['topic_details'] if t['topic'] == name)
        assert topic['questions'] == total
        assert topic['question_curriculum_counts'] == {code: 3}
        for q in rows:
            assert q['unit_name'] == 'Period 6: 1865-1898'
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_six_reform_and_politics_sets_validate_and_map():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_six_reform_and_politics import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    report = audit_bank(UNITS, ALL)
    for name, code in [('Reform in the Gilded Age', '6.11'), ('Politics in the Gilded Age', '6.13')]:
        rows = [q for q in QUESTIONS if q['topic_name'] == name]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        topic = next(t for t in report['topic_details'] if t['topic'] == name)
        assert topic['question_curriculum_counts'] == {code: 3}
        for q in rows:
            assert q['unit_name'] == 'Period 6: 1865-1898'
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_period_six_context_sets_validate_and_complete_topic_mapping():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_six_context_and_change import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 9
    report = audit_bank(UNITS, ALL)
    for name, code in [('Contextualizing Period 6', '6.1'), ('Development of the Middle Class', '6.10'),
                       ('Continuity and Change in Period 6', '6.14')]:
        rows = [q for q in QUESTIONS if q['topic_name'] == name]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        topic = next(t for t in report['topic_details'] if t['topic'] == name)
        assert topic['question_curriculum_counts'] == {code: 3}
        for q in rows:
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    assert {tag for topic in UNITS[5]['topics'] for tag in topic['skill_tags'] if tag.startswith('ced:')} == {f'ced:6.{i}' for i in range(1, 15)}
    # Every mapped code now has tagged items, without implying comprehensive depth.
    period = [q for q in ALL if q['unit_name'] == UNITS[5]['name']]
    tagged = {tag for q in period for tag in q['skill_tags'] if tag.startswith('ced:')}
    assert tagged == {f'ced:6.{i}' for i in range(1, 15)}


def test_western_sets_cover_economic_and_social_codes_without_replacing_legacy_items():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_six_west import QUESTIONS, TOPIC
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    for code in ['6.2', '6.3']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        for q in rows:
            assert q['topic_name'] == TOPIC
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == TOPIC)
    assert topic['questions'] == 7
    assert topic['question_curriculum_counts'] == {'6.2': 3, '6.3': 3}
    assert topic['questions_without_curriculum_codes'] == 1


def test_industry_and_migration_sets_validate_with_period_six_minimum_depth():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_six_industry_and_migration import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 9
    for code in ['6.5', '6.6', '6.8']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        for q in rows:
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topics = [t for t in audit_bank(UNITS, ALL)['topic_details'] if t['unit'] == UNITS[5]['name']]
    assert len(topics) == 12
    assert all(t['questions'] >= 3 and len(t['difficulty_levels']) >= 2 for t in topics)
    assert all(not t['curriculum_codes_without_tagged_questions'] for t in topics)


def test_period_seven_expansion_and_reform_validate_and_preserve_topic_identity():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_seven_expansion_and_reform import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    assert [t['name'] for t in UNITS[6]['topics'][:4]] == [
        'The Progressive Movement', 'American Imperialism and World War I',
        'The Great Depression and the New Deal', 'World War II',
    ]
    for code in ['7.3', '7.4']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        for q in rows:
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topics = [t for t in audit_bank(UNITS, ALL)['topic_details'] if t['unit'] == UNITS[6]['name']]
    for name, code in [('The Progressive Movement', '7.4'), ('American Imperialism and World War I', '7.3')]:
        topic = next(t for t in topics if t['topic'] == name)
        assert topic['question_curriculum_counts'][code] == 3
    # Broad legacy mappings must not be mistaken for tagged practice coverage.
    mapped = {tag for t in UNITS[6]['topics'] for tag in t['skill_tags'] if tag.startswith('ced:')}
    assert mapped == {f'ced:7.{n}' for n in [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14]}


def test_world_war_one_sets_validate_and_reach_existing_practice_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_seven_world_war_one import QUESTIONS, TOPIC
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    for code in ['7.5', '7.6']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        for q in rows:
            assert q['topic_name'] == TOPIC
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == TOPIC)
    assert topic['question_curriculum_counts'] == {'7.2': 3, '7.3': 3, '7.5': 3, '7.6': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []


def test_depression_sets_validate_and_cover_both_legacy_topic_codes():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_seven_depression import QUESTIONS, TOPIC
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    for code in ['7.9', '7.10']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        for q in rows:
            assert q['topic_name'] == TOPIC
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == TOPIC)
    assert topic['question_curriculum_counts'] == {'7.9': 3, '7.10': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []


def test_fair_employment_set_validates_with_world_war_two_mapping():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_seven_fair_employment import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'World War II'
        assert 'ced:7.12' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'World War II')
    assert topic['question_curriculum_counts'] == {'7.12': 3, '7.13': 3, '7.14': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []


def test_allied_strategy_sets_validate_and_keep_distinct_stimuli():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_seven_allied_strategy import QUESTIONS
    assert len(QUESTIONS) == 6
    for code in ['7.13', '7.14']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        assert len({tag for q in rows for tag in q['skill_tags'] if tag.startswith('stimulus:')}) == 1
        for q in rows:
            assert q['topic_name'] == 'World War II'
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_interwar_topic_maps_and_validates_original_practice():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_seven_interwar import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'Interwar Foreign Policy')
    assert topic['question_curriculum_counts'] == {'7.11': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []
    assert UNITS[6]['topics'][4]['display_order'] == 5


def test_quota_practice_validates_and_maps_to_new_cultural_conflict_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_seven_quota import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == '1920s Cultural and Political Controversies')
    assert topic['question_curriculum_counts'] == {'7.8': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []
    assert UNITS[6]['topics'][5]['display_order'] == 6


def test_imperialism_debate_items_validate_in_existing_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.seed_data.questions.us_history.period_seven_imperialism import QUESTIONS
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'American Imperialism and World War I'
        assert 'ced:7.2' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_marshall_plan_items_validate_and_reduce_period_eight_shortfall():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.history_readiness import history_mcq_inventory
    from scripts.seed_data.questions.us_history.period_eight_recovery import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'The Cold War and Containment'
        assert 'ced:8.2' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    period = history_mcq_inventory(UNITS, ALL)['periods'][7]
    assert period['approved_unique_mcq'] == 24
    assert period['shortfall_to_minimum'] == 0


def test_civil_rights_sets_validate_across_two_curriculum_codes():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_eight_civil_rights import QUESTIONS, TOPIC
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 6
    for code in ['8.6', '8.10']:
        rows = [q for q in QUESTIONS if f'ced:{code}' in q['skill_tags']]
        assert len(rows) == 3
        assert {q['difficulty'] for q in rows} == {2, 3, 4}
        for q in rows:
            validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
                **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == TOPIC)
    assert topic['question_curriculum_counts'] == {'8.6': 3, '8.10': 3}


def test_veterans_benefit_items_validate_with_economic_topic_mapping():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_eight_veterans import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'Postwar Prosperity and Suburbanization')
    assert topic['question_curriculum_counts'] == {'8.4': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []


def test_vietnam_items_validate_and_map_to_existing_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_eight_vietnam import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'The Vietnam War and Social Movements of the 1960s-70s')
    assert topic['question_curriculum_counts'] == {'8.8': 3}
    assert topic['curriculum_codes_without_tagged_questions'] == []


def test_great_society_items_validate_and_reach_new_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_eight_great_society import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'The Great Society')
    assert topic['question_curriculum_counts'] == {'8.9': 3}
    assert UNITS[7]['topics'][4]['display_order'] == 5


def test_environment_set_validates_and_maps_to_new_topic():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_eight_environment import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'Environment and Natural Resources')
    assert topic['question_curriculum_counts'] == {'8.13': 3}
    assert UNITS[7]['topics'][5]['display_order'] == 6


def test_inf_items_validate_and_reduce_period_nine_shortfall():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.history_readiness import history_mcq_inventory
    from scripts.seed_data.questions.us_history.period_nine_arms import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        assert q['topic_name'] == 'The End of the Cold War'
        assert 'ced:9.3' in q['skill_tags']
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    period = history_mcq_inventory(UNITS, ALL)['periods'][8]
    assert period['approved_unique_mcq'] == 10
    assert period['shortfall_to_minimum'] == 2


def test_reagan_economic_proposal_items_validate_with_curriculum_mapping():
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    from scripts.content_audit import audit_bank
    from scripts.seed_data.questions.us_history.period_nine_economy import QUESTIONS
    from scripts.seed_data.questions.us_history_questions import QUESTIONS as ALL
    assert len(QUESTIONS) == 3
    assert {q['difficulty'] for q in QUESTIONS} == {2, 3, 4}
    for q in QUESTIONS:
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    topic = next(t for t in audit_bank(UNITS, ALL)['topic_details'] if t['topic'] == 'The Reagan Revolution and Conservative Resurgence')
    assert topic['question_curriculum_counts'] == {'9.2': 3}
