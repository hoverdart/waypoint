"""Original practice on Native activism and the Alcatraz occupation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Civil Rights Movement Expands', code='8.11', set_id='alcatraz-occupation',
    source_url='https://www.nps.gov/alca/occupations.htm',
    source_kind='original instructional summary',
    stimulus='From November 1969 to June 1971, activists calling themselves Indians of All Tribes occupied Alcatraz Island, a former federal prison site. They called for recognition of treaty obligations, return of land, and a Native cultural center. Participants came from different Native communities. Federal authorities eventually removed the remaining occupiers, but the action attracted attention to Native self-determination and inspired further activism. This is an original summary of National Park Service historical accounts.',
    items=[
        ('comparison', 2, 'What distinguishes the demands described from a campaign concerned only with equal access to existing institutions?', 1, [
            ('They asked the government to replace Native political communities with a single uniform national culture.', 'Treaty recognition and Native cultural institutions challenged pressures toward cultural and political erasure.'),
            ('They included collective claims involving land, treaties, and Native control of cultural institutions.', 'These demands concern collective political relationships and self-determination as well as equality.'),
            ('They focused exclusively on increasing the number of federal prison jobs available to Native applicants.', 'The former prison site was used for demands about land and cultural institutions, not solely prison employment.'),
            ('They sought to eliminate all distinctions among the participating Native nations.', 'Cooperation among communities did not necessarily mean abandoning their distinct identities or sovereignty claims.'),
        ]),
        ('causation', 3, 'How could occupying a highly visible federal site advance the activists’ goals even without immediate legal control of the island?', 2, [
            ('The occupation automatically transferred title under federal law as soon as activists arrived.', 'An asserted land claim and physical occupation did not by themselves establish legal transfer.'),
            ('Physical occupation made treaty history unnecessary to the activists’ arguments.', 'Treaty obligations were part of the claims the occupation brought to public attention.'),
            ('The action could attract public attention, build solidarity, and increase pressure to address Native demands.', 'This explains a possible political mechanism distinct from immediately winning legal ownership.'),
            ('Visibility guaranteed that all participating communities would support identical tactics in later campaigns.', 'Public attention cannot establish uniform views or future tactical agreement across communities.'),
        ]),
        ('argumentation', 4, 'Which interpretation best incorporates both the removal of occupiers and the action’s influence on later activism?', 0, [
            ('The occupation failed to secure continued possession but could still contribute to broader mobilization for self-determination.', 'This separates the immediate site outcome from wider political and cultural influence.'),
            ('Removal proves that the occupation could have no effect beyond the island.', 'A protest can influence networks, ideas, and later action without winning its immediate demand.'),
            ('Later activism proves that the federal government granted every demand during the occupation.', 'Influence on later movements is not evidence that all immediate demands were granted.'),
            ('The occupation alone explains every subsequent federal policy change affecting Native nations.', 'Such an exclusive causal claim requires evidence that rules out other movements, negotiations, and policy influences.'),
        ]),
    ],
)
