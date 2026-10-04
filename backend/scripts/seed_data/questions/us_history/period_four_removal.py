"""Original critical analysis of a public-domain presidential policy defense."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Jackson and Federal Power', code='4.8', set_id='removal-message',
    source_url='https://www.archives.gov/milestone-documents/jacksons-message-to-congress-on-indian-removal',
    source_kind='primary excerpt',
    stimulus='Andrew Jackson, annual message to Congress, December 6, 1830, defending Indian removal: “enable those States to advance rapidly in population, wealth, and power.” The phrase refers to Mississippi and Alabama.',
    items=[
        ('claims-evidence', 2, 'Which interest does Jackson emphasize in this excerpt?', 2, [
            ('Preserving Native nations’ exclusive control of their homelands.', 'Jackson emphasizes state growth through removal, not exclusive Native control of existing homelands.'),
            ('Ending the settlement of white Americans in the South.', 'The policy sought to open land to white settlement rather than end it.'),
            ('Increasing the population and economic strength of southern states.', 'Population, wealth, and power are the benefits Jackson explicitly claims for the states.'),
            ('Restoring British authority over the Mississippi Valley.', 'The statement promotes American state growth, not British government.'),
        ]),
        ('sourcing', 3, 'Which feature of the message most directly shapes its value as historical evidence?', 0, [
            ('Its author was defending a policy pursued by his own administration.', 'Jackson had a political interest in presenting removal favorably; the message is direct evidence of his justification, not an impartial measure of consequences.'),
            ('It was written by a displaced Cherokee family describing its journey.', 'The author was the president, not a Cherokee eyewitness describing a removal journey.'),
            ('It was a secret record never intended for policymakers.', 'An annual message to Congress addressed national policymakers publicly.'),
            ('It was a court decision establishing the facts of every removal treaty.', 'A presidential message is neither a judicial ruling nor a comprehensive record of treaty consent.'),
        ]),
        ('causation', 3, 'Which development was most directly facilitated by opening southeastern Native lands to white settlement?', 3, [
            ('The immediate abolition of slavery in the cotton-growing South.', 'Removal did not abolish slavery; new plantation lands contributed to its expansion.'),
            ('The end of disputes over Native sovereignty.', 'Removal intensified conflicts over sovereignty and did not resolve them through universal agreement.'),
            ('The abandonment of commercial agriculture throughout the region.', 'Settlement expanded commercial agriculture rather than eliminating it.'),
            ('The expansion of cotton cultivation and enslaved labor into additional land.', 'Land opened to white settlers supported the growth of the plantation economy and slavery.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly challenge an interpretation that state economic gains meant removal benefited all affected people?', 1, [
            ('Another politician’s praise of state population growth.', 'Repeating praise of state growth does not assess consequences for displaced people.'),
            ('Native petitions opposing removal and accounts documenting coercion, dispossession, and deaths.', 'These sources would reveal harms and opposition omitted from a claim centered on state gains.'),
            ('The date on which Jackson’s message was printed.', 'A publication date does not establish who benefited or suffered.'),
            ('An assumption that every group shares the interests of a state government.', 'That assumption obscures the differing interests that need historical investigation.'),
        ]),
    ],
)
