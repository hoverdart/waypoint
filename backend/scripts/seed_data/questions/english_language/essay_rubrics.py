"""Student reflection rubric, adapted in original wording from the AP six-point structure.

Reference: https://apcentral.collegeboard.org/media/pdf/ap-english-language-and-composition-frqs-1-2-3-scoring-rubrics.pdf
A student selects levels; no keywords, LLM judge, or claim of official grading.
"""
from copy import deepcopy

BASE = [
    {'point': 'Thesis', 'points': 1, 'levels': [
        'Missing, off-task, or merely restates the issue.',
        'States a defensible interpretation or position answering the task.',
    ]},
    {'point': 'Evidence and commentary', 'points': 4, 'levels': [
        'No usable support for an argument.',
        'Mostly general support or summary.',
        'Some precise support and explanation; reasoning remains incomplete.',
        'Specific support throughout; some links to the reasoning need development.',
        'Specific support and sustained explanation develop a coherent argument.',
    ]},
    {'point': 'Sophistication', 'points': 1, 'levels': [
        'Complexity is absent or only mentioned.',
        'Explores meaningful tensions or implications throughout the argument.',
    ]},
]


def essay_rubric(kind):
    rows = deepcopy(BASE)
    if kind == 'synthesis':
        rows[1]['levels'] = [
            'No usable argument, or fewer than two supplied sources used.',
            'At least two sources referenced, mainly summarized.',
            'At least three sources used with some explanation but incomplete reasoning.',
            'At least three sources support the argument; some connections need development.',
            'At least three sources support a coherent argument through sustained explanation.',
        ]
    elif kind == 'rhetorical-analysis':
        rows[0]['levels'][1] = 'Makes a defensible claim about the writer’s rhetorical choices.'
        rows[1]['levels'][3] += ' Explains the effect of at least one choice.'
        rows[1]['levels'][4] += ' Explains the effects of multiple choices.'
    elif kind != 'argument':
        raise ValueError('Unknown English Language essay type')
    return {'scoring_method': 'self_review', 'checklist': rows,
            'reference_url': 'https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam'}
