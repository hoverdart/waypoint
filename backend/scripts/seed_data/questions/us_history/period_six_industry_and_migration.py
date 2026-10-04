"""Original technology, corporate organization, and migration questions."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 6: 1865-1898', topic='Industrialization and Big Business', code='6.5', set_id='electric-systems',
    source_url='https://home.nps.gov/people/thomas-edison-biography-1847-1882-birth-to-pearl-street.htm',
    source_kind='original instructional summary',
    stimulus='Edison’s electric-lighting work involved a system for generating and distributing electricity as well as lamps. In 1882, the Pearl Street operation supplied part of New York City. Commercial use required equipment and connections that brought power to customers; demonstrating a lamp was not the same as making service available everywhere. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Which factor best explains why an invention could become usable in some places before others?', 1, [
            ('A patent automatically installed the invention in every household.', 'Legal recognition did not provide the equipment and connections needed for service.'),
            ('Adoption depended on supporting infrastructure and access, not only the existence of the device.', 'Generating and distributing power required a system that could reach particular customers.'),
            ('Urban customers were prohibited from using technologies demonstrated outside their own homes.', 'The summary identifies infrastructure, not such a prohibition, as necessary for service.'),
            ('Commercial adoption required all older lighting methods to disappear first.', 'New and older lighting methods could coexist during uneven adoption.'),
        ]),
        ('comparison', 3, 'Which evidence would most directly distinguish technological invention from commercial diffusion?', 2, [
            ('A single inventor’s announcement used as proof of nationwide access.', 'An announcement cannot establish how widely customers received service.'),
            ('The number of newspapers mentioning electricity without any evidence of installations.', 'Public attention does not directly measure use or access.'),
            ('The dates of successful demonstrations compared with service maps and customer connections over time.', 'These records distinguish technical achievement from the spread of working service.'),
            ('A later photograph of a fully electrified district projected back onto 1882.', 'Later conditions cannot be assumed to describe the initial service area.'),
        ]),
        ('argumentation', 4, 'Which finding would most directly qualify a claim that electric lighting immediately changed all urban residents’ lives in the same way?', 0, [
            ('Records showing that service reached only some streets and that households differed in their ability to obtain it.', 'Uneven physical and economic access challenges the claim of immediate uniform effects.'),
            ('Evidence that a functioning electric lamp existed.', 'A functioning device establishes possibility, not equal access or identical consequences.'),
            ('An advertisement describing the technology as revolutionary.', 'Promotional language is not evidence of uniform experience.'),
            ('A business report listing the year of the station’s opening.', 'An opening date does not show which residents obtained service or how their lives changed.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Industrialization and Big Business', code='6.6', set_id='trusts-and-antitrust',
    source_url='https://www.archives.gov/milestone-documents/sherman-anti-trust-act',
    source_kind='original instructional summary',
    stimulus='The Standard Oil Trust organized in 1882 placed component companies under common trustees. Critics of concentrated corporate power sought government action to preserve competition. The Sherman Act of 1890 addressed restraints of interstate trade and monopolization, but enforcement depended on interpretation. In United States v. E. C. Knight Company (1895), the Supreme Court distinguished manufacturing from commerce, limiting the act’s application in that case. This is an original instructional summary.',
    items=[
        ('comparison', 2, 'What feature of the trust arrangement most directly raised concerns about competition?', 3, [
            ('Each component company was required to pursue an entirely independent strategy.', 'Common trustees coordinated control rather than guaranteeing independence.'),
            ('All company shares were transferred to consumers elected by state governments.', 'The arrangement described placed control with trustees, not elected consumer bodies.'),
            ('The federal government became the owner of every participating refinery.', 'The trust was a private corporate arrangement, not general federal ownership.'),
            ('Common control could coordinate firms that might otherwise compete with one another.', 'Concentrated control reduced the independence of component companies and raised concerns about competitive markets.'),
        ]),
        ('contextualization', 3, 'The E. C. Knight decision most clearly illustrates which issue in early antitrust enforcement?', 0, [
            ('Judicial distinctions about federal authority could limit the reach of broadly worded economic legislation.', 'The distinction between manufacturing and commerce affected application of the federal statute.'),
            ('Congress had already placed every manufacturing firm under permanent federal ownership.', 'The case concerned regulation, not a system of universal public ownership.'),
            ('Antitrust policy was enforced without courts interpreting statutory or constitutional boundaries.', 'The decision demonstrates the importance of judicial interpretation.'),
            ('State governments had lost every power to regulate economic activity.', 'The limited application of a federal act does not establish the disappearance of all state authority.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test whether a trust’s formation reduced competitive independence in its industry?', 1, [
            ('The continued existence of several company names, assumed to prove separate decision-making.', 'Separate names do not establish independent control under a common trust.'),
            ('Ownership and management records compared with pricing decisions and the ability of rival firms to enter the market.', 'These sources connect organizational control with competitive behavior and barriers.'),
            ('The trust’s own claim of efficiency, accepted as proof that no competition was restricted.', 'Efficiency claims do not by themselves settle questions about market control.'),
            ('The date of the Sherman Act treated as proof that every earlier trust immediately disappeared.', 'Enactment did not automatically dissolve every trust or establish enforcement outcomes.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Immigration and Urbanization', code='6.8', set_id='ellis-inspection',
    source_url='https://home.nps.gov/elis/learn/historyculture/places_immigration.htm',
    source_kind='original instructional summary',
    stimulus='Ellis Island opened as a federal immigration station in 1892. Officials inspected arriving immigrants under admission rules, and inspection records documented particular encounters with the state. The station was one part of a wider migration system; its records do not represent every entry route or the later lives of all immigrants. This is an original instructional summary focused on the station’s early role, not the later restrictions adopted in the twentieth century.',
    items=[
        ('contextualization', 2, 'Which development is most directly reflected in the opening of the station?', 2, [
            ('The disappearance of federal involvement in immigrant admission.', 'A federal inspection station represents involvement rather than its disappearance.'),
            ('The replacement of immigration by internal migration alone.', 'The station processed people arriving from abroad, not only migrants within the country.'),
            ('The use of federal administrative institutions to process and screen arrivals.', 'The station made admission policy an administrative encounter involving inspection and records.'),
            ('The requirement that all immigrants become citizens immediately upon landing.', 'Admission and naturalization are distinct processes; entry did not itself confer citizenship.'),
        ]),
        ('sourcing', 3, 'What is the strongest reason not to use Ellis Island records alone to describe every immigrant’s arrival?', 0, [
            ('The records reflect the people and procedures associated with a particular entry institution rather than all migration routes.', 'The institution’s scope limits what its records can represent.'),
            ('Administrative records can never reveal information about migration.', 'Such records can be valuable when their creation and scope are considered.'),
            ('Every immigrant’s experience was necessarily identical regardless of port or time.', 'That assumption ignores differences in routes, policies, and circumstances.'),
            ('The opening of Ellis Island meant other routes ceased to exist.', 'A station’s opening does not establish that it became the only route of entry.'),
        ]),
        ('argumentation', 4, 'A historian wants to study how an arriving family established itself in a city. Which additional evidence would best extend an admission record?', 1, [
            ('The admission decision alone, treated as proof of later employment and housing conditions.', 'Admission records do not by themselves document the family’s subsequent life.'),
            ('Later census entries, city directories, employment evidence, and family accounts linked carefully to the same people.', 'These sources can follow settlement and work after arrival while requiring careful identification.'),
            ('A twentieth-century restriction assumed to have governed every arrival in 1892.', 'Later laws cannot be projected backward without checking their dates and applicability.'),
            ('A national population total without identifying the family or its destination.', 'An aggregate total cannot trace a particular family’s settlement experience.'),
        ]),
    ],
)
