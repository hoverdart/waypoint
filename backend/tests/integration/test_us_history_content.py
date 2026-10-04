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
    assert len(questions) == 46
