"""Original environmental-policy questions about institutional change."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='Environment and Natural Resources', code='8.13', set_id='epa-organization',
    source_url='https://www.epa.gov/history/origins-epa',
    source_kind='original instructional summary',
    stimulus='Amid heightened concern about pollution, the EPA began operating in 1970. Its creation brought together federal research, monitoring, standard-setting, and enforcement functions previously spread among several agencies. Reorganization addressed coordination, while the effects of particular environmental policies depended on implementation and other conditions. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Which problem did consolidating these functions most directly address?', 1, [
            ('A constitutional requirement that every pollutant be regulated by a separate department.', 'The summary identifies fragmented administration, not such a constitutional requirement.'),
            ('Fragmented responsibility for related environmental problems.', 'Bringing related functions together aimed to improve coordination across previously separate offices.'),
            ('The absence of any federal environmental activity before 1970.', 'Transferred functions demonstrate that federal activity already existed.'),
            ('A prohibition on using scientific research in public policy.', 'Research was among the functions consolidated, not an activity newly permitted after a prohibition.'),
        ]),
        ('comparison', 3, 'Which interpretation best captures both continuity and change in the agency’s creation?', 2, [
            ('All environmental concerns began in 1970, but governmental organization remained unchanged.', 'The agency was a new organizational arrangement drawing on existing activities and concerns.'),
            ('Existing offices continued unchanged and no responsibilities moved.', 'Consolidation involved transferring functions into a new agency.'),
            ('Existing governmental functions continued within a new structure intended to coordinate them.', 'This identifies continuity of functions alongside organizational change.'),
            ('The agency replaced public regulation with voluntary action by individual consumers alone.', 'The consolidated functions included governmental standard-setting and enforcement.'),
        ]),
        ('argumentation', 4, 'Which evidence would best evaluate whether the reorganization helped reduce pollution?', 0, [
            ('Comparable pollution measurements and enforcement records before and after the change, accounting for industrial and technological shifts.', 'This links outcomes to implementation while considering other causes of environmental change.'),
            ('The existence of a new agency name without records of its work.', 'A name establishes an organizational change, not environmental outcomes.'),
            ('Public concern about pollution treated as proof that pollution had already declined.', 'Concern can motivate policy but does not measure its effects.'),
            ('The announcement date used as the endpoint for all environmental improvement.', 'Effects require evidence over time rather than an assumption tied to an announcement.'),
        ]),
    ],
)
