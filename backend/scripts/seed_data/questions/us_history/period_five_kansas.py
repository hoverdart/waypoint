"""Original questions on popular sovereignty and the unraveling of compromise."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='The Compromise of 1850 and Escalating Sectional Conflict', code='5.6', set_id='kansas-nebraska',
    source_url='https://www.senate.gov/artandhistory/history/minute/Kansas_Nebraska_Act.htm',
    source_kind='original instructional summary',
    stimulus='The Kansas-Nebraska Act of 1854 organized two territories and replaced the Missouri Compromise’s geographic restriction on slavery there with popular sovereignty. Supporters presented local decision-making as a way to manage the issue. The act instead provoked intense political conflict and helped fracture existing party alliances. This is an original instructional summary.',
    items=[
        ('comparison', 2, 'What most clearly distinguished this approach from the Missouri Compromise’s territorial restriction?', 1, [
            ('It extended the same geographic prohibition without changing how slavery’s status would be determined.', 'The new approach displaced the geographic restriction rather than simply extending it.'),
            ('It shifted the proposed basis of decision from a congressional geographic rule to territorial popular sovereignty.', 'This identifies the change in the stated mechanism for determining slavery’s status.'),
            ('It made California’s existing constitution binding on Kansas and Nebraska.', 'California’s constitution did not govern the newly organized territories.'),
            ('It required the paired admission of one free state and one slave state before organizing territory.', 'The act organized territories under popular sovereignty rather than requiring a balanced pair of state admissions.'),
        ]),
        ('causation', 3, 'Why could territorial popular sovereignty intensify conflict rather than settle it?', 3, [
            ('It made the outcome independent of who settled in the territories or controlled their political institutions.', 'Those factors became especially consequential when territorial decision-making would shape the outcome.'),
            ('It removed slavery’s status in western lands from the interests of national political groups.', 'National groups continued to view territorial outcomes as important to sectional power.'),
            ('It restored the prior geographic restriction as a rule neither side could challenge.', 'The act displaced that restriction rather than restoring it.'),
            ('It raised the stakes of settlement, elections, and control of territorial institutions for competing groups.', 'Local decision-making moved the struggle into contests over who would participate and exercise authority.'),
        ]),
        ('argumentation', 4, 'Which evidence would best support the claim that the act contributed to party realignment?', 0, [
            ('Correspondence, party platforms, and election returns connecting opposition to the act with defections and new coalitions.', 'These sources can connect expressed motives with changes in organization and electoral allegiance.'),
            ('A territorial map showing the boundaries established by the act.', 'A boundary map documents geography but does not directly establish changing partisan allegiance.'),
            ('The number of pages devoted to territorial administration in the statute.', 'The length of administrative provisions does not measure political realignment.'),
            ('A single speech predicting national harmony before the act took effect.', 'A prediction establishes an expectation rather than subsequent party changes.'),
        ]),
    ],
)
