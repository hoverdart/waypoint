"""Original instructional questions on revival and voluntary reform."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Religious Revival and Reform Movements', code='4.10', set_id='voluntary-societies',
    source_url='https://www.loc.gov/exhibits/religion/rel07.html', source_kind='original instructional summary',
    stimulus='Early nineteenth-century revivals mobilized believers beyond traditional congregations. Evangelical networks supported voluntary societies devoted to religious instruction and moral reform. These organizations sought to shape public conduct through association and persuasion as well as campaigns for legal change. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('contextualization', 2, 'The developments described are most closely associated with', 1, [
            ('the expansion of state-financed established churches as the main agents of moral regulation.', 'The summary emphasizes voluntary associations, a different organizational basis from compulsory public support of established churches.'),
            ('the Second Great Awakening and antebellum reform.', 'Revival networks and moral reform were linked in the early nineteenth century.'),
            ('the spread of Enlightenment deism through elite intellectual discussion.', 'Deism emphasized reason and natural religion; the revival mobilization and evangelical reform networks described here point to the Second Great Awakening.'),
            ('the concentration of religious influence in inherited clerical offices rather than voluntary participation.', 'The summary describes mobilization beyond traditional congregations and participation in voluntary societies, not reliance chiefly on inherited offices.'),
        ]),
        ('causation', 3, 'How could revival networks contribute to reform campaigns?', 0, [
            ('They supplied shared commitments, participants, and channels for organizing.', 'Networks linking believers could help mobilize people and resources for reform.'),
            ('They made reform primarily a responsibility of state-supported clergy rather than lay associations.', 'The mechanism described is voluntary mobilization; assigning reform chiefly to state-supported clergy misidentifies the organizational base.'),
            ('They made doctrinal uniformity a prerequisite for cooperation on social goals.', 'Shared reform activity could cross denominational boundaries; complete doctrinal agreement was not the necessary mechanism.'),
            ('They confined moral responsibility to private conversion and discouraged organized public action.', 'The societies translated religious commitments into collective activity rather than confining them to private experience.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly test a claim that revival participation contributed to a local temperance campaign?', 2, [
            ('A county census showing population growth during the same decade.', 'Population growth may supply context, but by itself does not connect revival participation to the campaign’s organizers or motivations.'),
            ('A temperance pamphlet listing health risks of drinking without identifying its authors or sponsors.', 'The pamphlet reveals an argument for temperance but does not establish a connection to revival participants.'),
            ('Membership records and correspondence connecting revival participants with the campaign’s organizers.', 'Overlapping participation and correspondence about motivations could substantiate the proposed connection.'),
            ('A church building plan documenting additional seating before the campaign began.', 'Expanded seating may indicate institutional growth, but does not directly link revival participants to temperance organizing.'),
        ]),
    ],
)
