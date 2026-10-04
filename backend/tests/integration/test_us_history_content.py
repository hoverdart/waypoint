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
