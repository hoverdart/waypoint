"""Original questions using Jefferson's public-domain inaugural language."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Contextualizing Period 4', code='4.1', set_id='transition-1801',
    source_url='https://www.loc.gov/exhibits/creating-the-united-states/peaceful-transition.html', source_kind='primary excerpt',
    stimulus='Thomas Jefferson, first inaugural address, March 4, 1801: “We are all republicans, we are all federalists.”',
    items=[
        ('contextualization', 2, 'Which circumstance most directly explains this appeal?', 2, [
            ('The end of Reconstruction after the Civil War.', 'Reconstruction occurred many decades after Jefferson’s inauguration.'),
            ('The unanimous disappearance of party competition in the 1790s.', 'The 1790s saw intense party conflict, not its disappearance.'),
            ('A divisive election followed by a transfer of power between rival political groups.', 'The election of 1800 and transition to Jefferson’s administration gave urgency to an appeal for unity.'),
            ('The ratification of the Nineteenth Amendment.', 'The Nineteenth Amendment was ratified in 1920.'),
        ]),
        ('sourcing', 3, 'Jefferson’s position as an incoming president most directly helps explain his effort to', 0, [
            ('reassure political opponents that shared allegiance could survive electoral defeat.', 'An inaugural appeal to common principles could support acceptance of the new administration after a bitter contest.'),
            ('document every voter’s private political beliefs.', 'The statement is a public appeal rather than an individual-level survey.'),
            ('announce the legal abolition of every political association.', 'The phrase does not enact a prohibition on political organizations.'),
            ('request restoration of British colonial administration.', 'Jefferson affirmed American republican government rather than British rule.'),
        ]),
        ('claims-evidence', 3, 'Which inference is best supported by the statement itself?', 3, [
            ('All Federalists immediately adopted Jefferson’s policies.', 'A conciliatory statement does not establish opponents’ agreement with his program.'),
            ('Every adult enjoyed equal political rights in 1801.', 'The statement does not describe suffrage qualifications or establish universal participation.'),
            ('Political disputes permanently ended after the election.', 'A call for unity cannot prove the end of political disagreement.'),
            ('Jefferson publicly emphasized common principles across partisan divisions.', 'The inclusive phrasing places shared political belonging above party labels.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly help assess whether the transfer of power strengthened constitutional government?', 1, [
            ('The number of sentences in the inaugural address.', 'Length does not show whether institutions functioned during the transition.'),
            ('Records showing electoral disputes resolved through established institutions and opponents continuing political activity.', 'Such evidence would connect peaceful succession and continued opposition to the operation of constitutional government.'),
            ('An assumption that every change of leadership requires military intervention.', 'That assumption cannot substitute for evidence about this transition.'),
            ('A list of unrelated European royal marriages.', 'Royal marriages do not directly establish the functioning of American electoral institutions.'),
        ]),
    ],
)
