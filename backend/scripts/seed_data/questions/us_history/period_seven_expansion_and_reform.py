"""Original questions on overseas expansion and Progressive regulation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic='American Imperialism and World War I', code='7.3', set_id='war-and-territory',
    source_url='https://history.state.gov/milestones/1866-1898/spanish-american-war',
    source_kind='original instructional summary',
    stimulus='Cuban insurgents fought Spain before U.S. intervention in 1898. Congress disclaimed an intention to annex Cuba. After the war, Spain relinquished its claim to Cuba and ceded Puerto Rico, Guam, and the Philippines to the United States. Hawaii was annexed through a separate congressional resolution during the same year, rather than acquired from Spain. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'Which interpretation best accounts for the different territorial outcomes described?', 1, [
            ('U.S. intervention established the same political arrangement in every island involved.', 'The distinction between relinquishing Cuba and ceding other islands contradicts a uniform arrangement.'),
            ('A war associated with Cuban independence also expanded U.S. control beyond Cuba.', 'The settlement combined relinquishment of Spanish claims to Cuba with U.S. acquisitions elsewhere.'),
            ('Spanish defeat ended U.S. interest in overseas possessions.', 'The acquisitions demonstrate an expansion of overseas holdings.'),
            ('Hawaii became a U.S. possession because it had been a Spanish colony.', 'Its separate annexation was not a transfer of Spanish sovereignty.'),
        ]),
        ('causation', 3, 'Which development most directly helps explain why the conflict became an issue for the United States before 1898?', 2, [
            ('The rejection of the Treaty of Versailles by the U.S. Senate.', 'That debate followed World War I, not the Cuban conflict of the 1890s.'),
            ('A congressional decision to grant statehood to the Philippines.', 'There was no such grant; this does not explain intervention in Cuba.'),
            ('The interaction of a nearby independence struggle with American economic and strategic interests.', 'The Cuban struggle preceded intervention and intersected with U.S. concerns in the Caribbean.'),
            ('The implementation of the Good Neighbor policy toward Latin America.', 'That policy belongs to the 1930s and cannot explain the outbreak of this war.'),
        ]),
        ('argumentation', 4, 'A historian argues that declarations of support for independence constrained expansion only selectively. Which comparison most directly supports the claim?', 0, [
            ('The pledge concerning Cuba compared with the treaty provisions transferring other islands.', 'These different outcomes reveal the selective scope of the commitment.'),
            ('The dates of the declaration of war compared with the date of the cease-fire.', 'Duration alone does not establish how independence commitments shaped territorial outcomes.'),
            ('The number of naval vessels compared with the number of land troops.', 'Force composition does not directly test the territorial scope of an independence pledge.'),
            ('The location of Havana compared with the location of Santiago.', 'Geographic locations alone do not establish differences in political commitments.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 7: 1890-1945', topic='The Progressive Movement', code='7.4', set_id='consumer-protection',
    source_url='https://www.fda.gov/about-fda/fda-history-exhibits/80-years-federal-food-drug-and-cosmetic-act',
    source_kind='original instructional summary',
    stimulus='The 1906 Pure Food and Drugs Act expanded federal consumer protection through requirements concerning product labeling, purity, and strength. Its reach nevertheless had limits: the law did not provide a general means to remove inherently dangerous drugs, and proving fraudulent misbranding could be difficult. Later legislation addressed shortcomings. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'The law best illustrates which Progressive approach to industrial society?', 3, [
            ('Replacing private production with federal ownership of food factories.', 'The measure regulated products rather than nationalizing their producers.'),
            ('Relying exclusively on consumers to detect adulteration without public oversight.', 'Federal requirements expanded the public role beyond individual consumer judgment.'),
            ('Restricting reform to the distribution of western farmland.', 'This measure concerned consumers and manufactured products, not land distribution.'),
            ('Using government authority to address harms that individual purchasers struggled to evaluate.', 'Requirements for labeling and purity sought to protect consumers in the marketplace.'),
        ]),
        ('comparison', 3, 'How did this approach resemble the Interstate Commerce Act of 1887?', 0, [
            ('Both extended federal regulation of private economic activity without requiring general public ownership.', 'Railroad regulation and consumer protection both increased oversight while retaining private enterprise.'),
            ('Both established public ownership as the sole permissible form of business organization.', 'Neither measure imposed general public ownership.'),
            ('Both made constitutional amendments the required mechanism for each enforcement action.', 'These were statutes implemented through enforcement processes, not repeated constitutional amendments.'),
            ('Both transferred federal regulatory functions entirely to voluntary industry associations.', 'Both created a federal regulatory role rather than simply surrendering it to industry.'),
        ]),
        ('argumentation', 4, 'Which evidence would best evaluate the claim that passage of the act immediately eliminated dangerous products?', 2, [
            ('A reformer’s celebration of the signing ceremony.', 'A statement of hope cannot establish the practical reach of enforcement.'),
            ('The date on which Congress passed the bill.', 'Enactment establishes a legal change, not the elimination of harmful products.'),
            ('Enforcement records and continued sales of dangerous products compared with the law’s available remedies.', 'This comparison tests outcomes against the authority actually available to regulators.'),
            ('The number of pages in the law compared with an earlier bill.', 'Length does not establish effectiveness or the disappearance of dangerous products.'),
        ]),
    ],
)
