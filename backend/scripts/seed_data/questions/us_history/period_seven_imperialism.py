"""Original practice distinguishing motives and perspectives on empire."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic='American Imperialism and World War I', code='7.2', set_id='philippine-debate',
    source_url='https://history.state.gov/milestones/1899-1913/war',
    source_kind='original instructional summary',
    stimulus='Supporters of annexing the Philippines invoked Asian commercial opportunities, competition with other powers, and claims that Filipinos were unprepared for self-government. American opponents included critics of colonial domination, people expressing racial fears about incorporating Filipinos, and opponents of the administration. Filipino nationalists sought independence rather than replacement of Spanish rule with American rule. This is an original instructional summary of differing positions, not an endorsement of racial assumptions.',
    items=[
        ('comparison', 2, 'Which pair of objections reaches a similar policy conclusion through different principles?', 1, [
            ('Concern about rival powers and interest in Asian trade.', 'Both were arguments for annexation in this account, rather than objections grounded in different principles.'),
            ('Opposition to governing without consent and opposition to incorporating a nonwhite population.', 'Both could oppose annexation, but one challenges domination while the other rests on racial exclusion.'),
            ('Claims of Filipino unpreparedness and calls for American supervision.', 'These reinforce the same paternalist justification rather than contrast distinct objections.'),
            ('Filipino independence and replacement of Spain by another colonial ruler.', 'These are incompatible outcomes, not different reasons for the same policy.'),
        ]),
        ('sourcing', 3, 'An American official calls Filipino resistance an insurrection; a Filipino nationalist describes defense against foreign rule. What disagreement most directly explains the labels?', 2, [
            ('Whether trade with Asia could be profitable.', 'Commercial expectations do not directly determine whether resistance is rebellion or defense of independence.'),
            ('Whether Spain had been defeated at sea.', 'Both positions could acknowledge Spanish defeat while disagreeing over subsequent sovereignty.'),
            ('Whether American sovereignty was legitimate or Filipino independence should be recognized.', 'The labels assume different answers to who had legitimate governing authority.'),
            ('Whether the islands had economic resources.', 'Resource assessments do not resolve the legitimacy claims embedded in these labels.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly challenge a claim that American opposition to annexation uniformly supported racial equality?', 0, [
            ('Anti-annexation speeches arguing that Filipinos should be excluded from participation in American government because of race.', 'Such evidence demonstrates that opposition to annexation could coexist with racial exclusion.'),
            ('Pro-annexation speeches predicting growth in Asian trade.', 'These illuminate supporters’ motives, not the racial commitments of opponents.'),
            ('Filipino declarations asserting a right to independence.', 'These establish Filipino nationalist aims rather than the uniformity of American opponents’ views.'),
            ('Military reports describing the resources needed to occupy the islands.', 'Occupation costs may explain pragmatic objections but do not directly establish racial attitudes.'),
        ]),
    ],
)
