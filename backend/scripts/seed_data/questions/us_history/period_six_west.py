"""Original western-development questions with separate economic/social mappings."""
from .builders import source_set

TOPIC = 'The Western Frontier and Native American Displacement'
QUESTIONS = source_set(
    period='Period 6: 1865-1898', topic=TOPIC, code='6.2', set_id='railroad-aid',
    source_url='https://www.archives.gov/news/articles/utah-borrows-pacific-railroad-act',
    source_kind='original instructional summary',
    stimulus='The Pacific Railroad Act of 1862 authorized federal support for a transcontinental railroad through bonds and land grants to railroad companies. Construction joined the Central Pacific and Union Pacific lines in 1869. The project combined private companies with public assistance and helped connect western locations to wider markets. This is an original instructional summary; government support for construction did not mean that the entire railroad system became federally owned.',
    items=[
        ('contextualization', 2, 'Which interpretation of government’s economic role is most directly supported by the financing described?', 1, [
            ('The federal government confined itself to protecting existing routes and supplied no resources for new construction.', 'Bonds and land grants supplied support for new construction rather than merely protecting existing routes.'),
            ('Federal policy could encourage private economic development through public resources.', 'Public assistance and private companies operated together in the described project.'),
            ('Railroads could receive federal support only after surrendering all ownership to Congress.', 'The project did not require general federal ownership of the railroad system.'),
            ('Western infrastructure was financed exclusively through municipal property taxes.', 'The summary specifically identifies national bonds and land grants.'),
        ]),
        ('causation', 3, 'Which consequence most plausibly followed from linking a western agricultural district to a wider rail network?', 2, [
            ('The district became insulated from price changes in distant markets.', 'Market integration could expose producers to distant supply and demand rather than insulate them.'),
            ('Farmers no longer needed credit, equipment, or buyers to sustain production.', 'Transportation access did not remove other requirements for agricultural production.'),
            ('Producers gained access to more distant buyers while becoming more connected to transportation charges and market fluctuations.', 'A wider market offered opportunities while also linking producers to costs and conditions beyond the local district.'),
            ('Rail access guaranteed that every producer received identical profits.', 'Costs, output, prices, and bargaining power could differ even with access to the same network.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test whether federal railroad assistance benefited a particular western community?', 0, [
            ('Local shipping costs, business activity, land transfers, and residents’ accounts before and after connection, considered alongside other changes.', 'These sources can reveal varied effects while helping distinguish railroad-related changes from other influences.'),
            ('The total national land grant alone, treated as a measurement of every community’s gain.', 'The size of national assistance does not show how benefits and costs were distributed locally.'),
            ('A railroad advertisement treated as a complete record of residents’ experiences.', 'Promotional material reveals claims but needs comparison with evidence of actual outcomes.'),
            ('The completion date alone, interpreted as proof that all local economic problems ended.', 'Completion establishes timing, not a universal improvement in local conditions.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic=TOPIC, code='6.3', set_id='dawes-allotment',
    source_url='https://www.archives.gov/milestone-documents/dawes-act',
    source_kind='original instructional summary',
    stimulus='The Dawes Act of 1887 authorized allotment of reservation land to individual Native people and families, with allotted land initially held in federal trust. Its supporters sought assimilation through individual landholding and agriculture. The law also provided a process for acquiring unallotted reservation land for settlement. It initially exempted specified Native nations and territories; later legislation extended allotment. Allotment policies contributed to extensive Native land loss. This is an original instructional summary that distinguishes the policy’s stated rationale from its consequences.',
    items=[
        ('comparison', 2, 'Which change in landholding did the policy seek to promote?', 3, [
            ('Expansion of collective tribal control over all land previously claimed by settlers.', 'The act aimed to divide reservation lands into individual allotments, not broadly expand collective control.'),
            ('Immediate unrestricted sale of every allotment without any federal trust period.', 'The original scheme included a federal trust period rather than immediate unrestricted alienation of every allotment.'),
            ('Permanent exemption of every Native nation from all later federal allotment legislation.', 'Specified initial exemptions should not be confused with immunity from subsequent legislation.'),
            ('A shift from collectively held reservation land toward individual allotments under federal supervision.', 'The policy promoted individual holdings while retaining federal authority through the allotment and trust process.'),
        ]),
        ('sourcing', 3, 'The assimilation rationale is best used as evidence of which of the following?', 0, [
            ('Federal policymakers’ assumptions about how Native people should live, rather than proof of Native consent.', 'A policy rationale reveals the goals and assumptions of its proponents; it does not establish the agreement of those affected.'),
            ('A shared decision by every Native community to abandon collective institutions.', 'The summary supplies no evidence of universal Native agreement or a single response across nations.'),
            ('The absence of any federal effort to reshape Native social and economic practices.', 'Assimilation through individual farming was itself an effort to reshape those practices.'),
            ('The automatic success of allotment in protecting all Native land from transfer.', 'The stated rationale cannot establish success, and the summary identifies land loss.'),
        ]),
        ('argumentation', 4, 'Which approach would best investigate how allotment changed a particular Native nation’s land base?', 1, [
            ('Apply the 1887 law identically to every nation without checking exemptions or later legislation.', 'Implementation varied in legal scope and chronology; the initial statute did not apply uniformly to every nation.'),
            ('Trace applicable laws and local allotment records alongside land transfers and accounts from the Native community.', 'This connects legal chronology and administrative action with changes in landholding and community experience.'),
            ('Use the stated goal of protecting individual property as proof that no land was lost.', 'Policy goals must be tested against outcomes rather than substituted for them.'),
            ('Count allotments alone without examining acreage, unallotted lands, or subsequent transfers.', 'A count cannot establish the total land base or how it changed.'),
        ]),
    ],
)
