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
    assert len(questions) == 133


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
