"""Original practice on coalition-building and farmworker economic pressure."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Civil Rights Movement Expands', code='8.11', set_id='delano-coalition',
    source_url='https://www.nps.gov/articles/000/workers-united-the-delano-grape-strike-and-boycott.htm',
    source_kind='original instructional summary',
    stimulus='In September 1965, predominantly Filipino members of the Agricultural Workers Organizing Committee began a strike against grape growers in Delano, California. Members of the National Farm Workers Association, many of them Mexican American, voted to join. Organizers combined work stoppages with consumer boycotts and public demonstrations to seek improved pay, conditions, and union recognition. The campaign developed over several years rather than producing immediate agreement from every grower.',
    items=[
        ('comparison', 2, 'How did a consumer boycott differ from the workers’ strike while supporting a related goal?', 2, [
            ('The boycott withheld labor at the vineyards, while the strike withheld consumer purchases.', 'This reverses the principal mechanisms of a strike and a consumer boycott.'),
            ('The boycott depended on government ownership of every targeted business, while the strike required private ownership.', 'Neither tactic inherently depends on that ownership distinction.'),
            ('The boycott pressured sales through consumers’ purchasing choices, while the strike withheld workers’ labor.', 'The tactics acted at different points in the economic relationship and could reinforce each other.'),
            ('The boycott automatically created a binding labor contract, while the strike could only attract publicity.', 'Neither action automatically created a contract; both could apply pressure toward negotiation.'),
        ]),
        ('causation', 3, 'Why could cooperation between AWOC and NFWA strengthen the campaign?', 0, [
            ('It could reduce employers’ ability to play groups of workers against each other and broaden the organizing network.', 'Cooperation increased solidarity and coordinated pressure without requiring all participants to have identical backgrounds.'),
            ('It eliminated the need for workers to agree on shared demands or tactics.', 'Coalition-building depended on coordination rather than making it unnecessary.'),
            ('It placed every agricultural worker in the country under the same negotiated contract immediately.', 'A local coalition did not automatically establish nationwide contract coverage.'),
            ('It made consumer participation irrelevant because cooperation itself required growers to sign contracts.', 'Worker solidarity could strengthen leverage, but it did not automatically compel a settlement or remove the role of consumer pressure.'),
        ]),
        ('claims-evidence', 4, 'Which evidence would most directly challenge a narrative describing the campaign as the work of a single ethnic community?', 1, [
            ('A photograph of one speaker without identifying the audience or organizers.', 'One photograph may illustrate a participant but cannot establish the campaign’s overall composition.'),
            ('AWOC and NFWA meeting records, strike votes, and participant accounts documenting collaboration.', 'These sources can establish the distinct organizations and participants involved in coordinated action.'),
            ('A national statistic about grape consumption that does not identify boycott supporters.', 'Consumption totals alone do not reveal who organized or participated in the campaign.'),
            ('A later commemoration naming only the most famous leader, treated as a complete participant list.', 'Selective commemoration may reproduce the narrow narrative instead of testing it against organizational evidence.'),
        ]),
    ],
)
