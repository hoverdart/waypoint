"""Original questions on settlement reform and the 1892 People's Party platform."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 6: 1865-1898', topic='Reform in the Gilded Age', code='6.11', set_id='settlement-houses',
    source_url='https://hullhouse.uic.edu/about/our-history/', source_kind='original instructional summary',
    stimulus='Hull-House began in Chicago in 1889 as a settlement associated with Jane Addams and Ellen Gates Starr. Its reformers worked in a neighborhood shaped by immigrant families and industrial employment. The settlement developed educational, cultural, and practical services and connected neighborhood work with campaigns to improve social conditions. This is an original instructional summary, not a statement that every later Hull-House program already existed in 1889.',
    items=[
        ('contextualization', 2, 'The settlement approach most directly responded to which development?', 2, [
            ('The disappearance of industrial employment from major American cities.', 'The settlement operated amid industrial employment and urban growth, not their disappearance.'),
            ('The replacement of immigrant neighborhoods by a uniformly rural population.', 'The neighborhood’s immigrant and urban character is central to the described work.'),
            ('Urban growth that brought reformers into contact with working-class needs and unequal access to services.', 'The settlement’s neighborhood services and reform activity addressed conditions associated with industrial urban life.'),
            ('A federal requirement that all social services be operated through party campaign offices.', 'Settlement work was not the result of a universal requirement placing services in campaign offices.'),
        ]),
        ('comparison', 3, 'Which distinction best separates the approach described from the belief that poverty should be left entirely to unrestricted competition?', 0, [
            ('The settlement organized assistance and reform rather than treating existing social outcomes as beyond collective intervention.', 'Services and campaigns for improved conditions expressed a role for organized action in addressing urban problems.'),
            ('The settlement assumed that education alone had already eliminated every structural barrier.', 'The broader reform work is inconsistent with assuming all structural barriers were already gone.'),
            ('The settlement sought to remove every immigrant from the neighborhood before offering services.', 'The described institution worked within an immigrant neighborhood rather than making exclusion a prerequisite for service.'),
            ('The settlement abolished private ownership of all neighborhood businesses.', 'Neighborhood services and reform advocacy did not amount to abolishing all private business ownership.'),
        ]),
        ('sourcing', 4, 'Which additional evidence would best help assess how neighborhood residents experienced the settlement, beyond its leaders’ stated aims?', 1, [
            ('A list of the founders’ goals used as a complete record of residents’ reactions.', 'Goals establish intentions but cannot substitute for evidence of residents’ experiences.'),
            ('Residents’ correspondence and testimony compared with participation records, with attention to whose experiences were recorded.', 'These sources can reveal use, criticism, and differing experiences while making selection and preservation limits visible.'),
            ('A later tribute that assumes the founders and every resident held identical priorities.', 'A tribute cannot establish universal agreement or capture differences within the neighborhood.'),
            ('The settlement’s street address alone, interpreted as proof that all services met every resident’s needs.', 'Location establishes proximity, not the adequacy or reception of the services.'),
        ]),
    ],
)

QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Politics in the Gilded Age', code='6.13', set_id='omaha-platform',
    source_url='https://www.presidency.ucsb.edu/documents/populist-party-platform-1892',
    source_kind='original instructional summary',
    stimulus='The People’s Party platform adopted at Omaha in 1892 criticized concentrated wealth and the established parties. It called for expanded currency, a graduated income tax, and public ownership of railroads and communication systems. The platform presented rural and urban workers as sharing interests against powerful economic institutions. These were party proposals and arguments, not a description of policies all enacted in 1892. This is an original summary of the platform.',
    items=[
        ('contextualization', 2, 'Which interpretation best describes the platform’s proposed response to concentrated economic power?', 3, [
            ('Restricting national authority so that corporations alone would determine all transportation policy.', 'The platform proposed a larger public role, including ownership of transportation infrastructure.'),
            ('Relying exclusively on voluntary charity without changes to public policy.', 'Currency, taxation, and ownership proposals sought institutional policy changes.'),
            ('Ending all political organization among rural producers to preserve the existing party system.', 'The platform was itself an effort to organize an alternative political movement.'),
            ('Using public policy and expanded government functions to change economic relationships.', 'The proposals linked monetary, fiscal, and ownership changes to a critique of concentrated power.'),
        ]),
        ('comparison', 3, 'How did the platform’s railroad proposal differ from federal oversight under the Interstate Commerce Act of 1887?', 0, [
            ('It proposed public ownership, going beyond regulation of privately owned carriers.', 'Ownership and regulatory oversight are distinct approaches; the platform advocated the former for railroads.'),
            ('It proposed abolishing rail transportation, while the earlier act required new railroad construction.', 'The platform sought public operation, not abolition of rail transport, and the comparison misstates the earlier act.'),
            ('It proposed leaving all rates to private discretion, while the earlier act nationalized the railroads.', 'This reverses the contrast: the earlier act regulated private carriers, while the platform called for public ownership.'),
            ('It proposed transferring authority exclusively to individual shippers rather than any public institution.', 'The proposal assigned ownership and operation to government, not exclusively to individual shippers.'),
        ]),
        ('sourcing', 4, 'Which use of the platform most appropriately recognizes its purpose as a political document?', 2, [
            ('Treating its claim of shared worker interests as proof that every rural and urban worker supported the party.', 'A coalition-building claim does not establish universal support or erase differences among workers.'),
            ('Treating every proposal as an enacted federal law without checking legislative records.', 'A platform states goals; enactment requires separate evidence.'),
            ('Analyzing how its proposals sought to unite constituencies, then checking voting and organizational records to assess support.', 'This distinguishes the party’s persuasive strategy from evidence about its actual coalition and electoral reach.'),
            ('Rejecting it as useless because a document advocating a position cannot reveal historical beliefs.', 'Advocacy documents are valuable evidence of aims and arguments when their purpose is considered.'),
        ]),
    ],
)
