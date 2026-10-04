"""Original instructional questions on revival and voluntary reform."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Religious Revival and Reform Movements', code='4.10', set_id='voluntary-societies',
    source_url='https://www.loc.gov/exhibits/religion/rel07.html', source_kind='original instructional summary',
    stimulus='Early nineteenth-century revivals mobilized believers beyond traditional congregations. Evangelical networks supported voluntary societies devoted to religious instruction and moral reform. These organizations sought to shape public conduct through association and persuasion as well as campaigns for legal change. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('contextualization', 2, 'The developments described are most closely associated with', 1, [
            ('the establishment of medieval European monasteries.', 'The summary concerns voluntary associations in the early American republic.'),
            ('the Second Great Awakening and antebellum reform.', 'Revival networks and moral reform were linked in the early nineteenth century.'),
            ('the wartime mobilization of the 1940s.', 'The chronology predates World War II by more than a century.'),
            ('the disappearance of religious activity after independence.', 'The growth of revival networks contradicts a claim that religious activity disappeared.'),
        ]),
        ('causation', 3, 'How could revival networks contribute to reform campaigns?', 0, [
            ('They supplied shared commitments, participants, and channels for organizing.', 'Networks linking believers could help mobilize people and resources for reform.'),
            ('They automatically enacted federal laws without political action.', 'Voluntary organizations could advocate legislation but could not enact federal laws themselves.'),
            ('They eliminated all disagreements among denominations.', 'Cooperation on some goals did not remove all religious differences.'),
            ('They required every participant to abandon moral concerns.', 'Moral concerns motivated these organizations rather than being excluded from them.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly test a claim that revival participation contributed to a local temperance campaign?', 2, [
            ('An unrelated map of European royal territories.', 'That map would not link local religious participation and organizing.'),
            ('The assumption that all religious people favor the same reforms.', 'This generalization substitutes an assumption for evidence of a specific connection.'),
            ('Membership records and correspondence connecting revival participants with the campaign’s organizers.', 'Overlapping participation and correspondence about motivations could substantiate the proposed connection.'),
            ('The publication date of a twentieth-century automobile advertisement.', 'That evidence does not address the antebellum campaign.'),
        ]),
    ],
)
