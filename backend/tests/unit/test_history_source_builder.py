import pytest

from scripts.seed_data.questions.us_history.builders import source_set
from scripts.seed_data.questions.us_history_questions import QUESTIONS


def make_set(**overrides):
    arguments = dict(
        period='Period 4: 1800-1848', topic='America on the World Stage', code='4.4',
        source_url='https://www.archives.gov/milestone-documents/monroe-doctrine',
        source_kind='primary excerpt', stimulus='Test excerpt',
        items=[('sourcing', 3, 'Test stem', 0, [(str(i), f'Explanation {i}') for i in range(4)])],
    )
    return source_set(**(arguments | overrides))[0]


def test_default_source_identifiers_remain_backward_compatible():
    tags = make_set()['skill_tags']
    assert 'stimulus:ush-4.4' in tags
    assert 'item:ush-4.4-1' in tags


def test_independent_sets_share_curriculum_code_without_sharing_identifiers():
    first = make_set(set_id='monroe-a')
    second = make_set(set_id='monroe-b')
    for q in (first, second):
        assert 'ced:4.4' in q['skill_tags']
    first_ids = {t for t in first['skill_tags'] if t.startswith(('item:', 'stimulus:'))}
    second_ids = {t for t in second['skill_tags'] if t.startswith(('item:', 'stimulus:'))}
    assert first_ids == {'item:ush-4.4-monroe-a-1', 'stimulus:ush-4.4-monroe-a'}
    assert first_ids.isdisjoint(second_ids)
    assert make_set(set_id='monroe-a') == first


@pytest.mark.parametrize('invalid', ['', 'Upper', 'two words', 'a:b', '-a', 'a-', 'a--b', 123])
def test_invalid_set_identifier_is_rejected(invalid):
    with pytest.raises(ValueError, match='set_id'):
        make_set(set_id=invalid)


def test_history_bank_item_ids_are_unique_and_stimulus_groups_are_consistent():
    items = set()
    stimuli = {}
    for question in QUESTIONS:
        tags = question['skill_tags']
        item_tags = [tag for tag in tags if tag.startswith('item:ush-')]
        stimulus_tags = [tag for tag in tags if tag.startswith('stimulus:ush-')]
        if not item_tags and not stimulus_tags:
            continue  # Foundation questions predate source-set metadata.
        assert len(item_tags) == len(stimulus_tags) == 1
        assert item_tags[0] not in items
        items.add(item_tags[0])
        # The shared stimulus includes source attribution, before the final stem.
        source = question['prompt'].rsplit('\n\n', 1)[0]
        identity = (question['unit_name'], question['topic_name'], source)
        assert stimuli.setdefault(stimulus_tags[0], identity) == identity
    assert items
