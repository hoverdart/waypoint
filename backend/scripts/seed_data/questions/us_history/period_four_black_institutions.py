"""Original questions about Black institutional autonomy in the early republic."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='African Americans in the Early Republic', code='4.12', set_id='allen-institutions',
    source_url='https://exhibits.episcopalarchives.org/s/church-awakens/page/allen',
    source_kind='original instructional summary',
    stimulus='Richard Allen and Absalom Jones helped organize Philadelphia’s Free African Society in 1787 as an independent mutual-aid association. Allen retained his Methodist commitments and founded Bethel in 1794. In 1816 he became the first bishop of the African Methodist Episcopal denomination. These institutions developed within a society that subjected Black people to racial discrimination. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('claims-evidence', 2, 'Which conclusion is best supported by the sequence described?', 0, [
            ('Black community leaders built independent institutions while adapting existing religious traditions.', 'Allen’s Methodist commitments and independent leadership show religious continuity alongside organizational autonomy.'),
            ('Independent Black churches required members to abandon Christianity.', 'Allen continued to identify with Methodism, a Christian tradition.'),
            ('Mutual-aid associations were agencies administered by the federal government.', 'The society was an independent community association rather than a federal agency.'),
            ('Religious leadership followed automatically from winning elected state office.', 'The sequence concerns community and denominational leadership, not a transition from state office.'),
        ]),
        ('causation', 3, 'Which mechanism best explains how independent associations could strengthen a community facing discrimination?', 2, [
            ('They made assistance depend primarily on approval by white church officials.', 'Institutional independence reduced dependence on outside authorities rather than making it the organizing principle.'),
            ('They converted private donations into an automatic legal right to vote.', 'Community aid did not itself change statutory voting qualifications.'),
            ('They pooled resources and developed leadership through organizations controlled by community members.', 'Mutual aid and independent governance could support practical assistance and collective action.'),
            ('They eliminated the need for cooperation among households by assigning relief entirely to the state.', 'Mutual aid relies on cooperation within the association rather than exclusively on state administration.'),
        ]),
        ('comparison', 3, 'Which distinction would be most useful when comparing these institutions with white-led religious reform associations?', 3, [
            ('Whether either group could use voluntary organization to pursue collective goals.', 'Both kinds of association could use voluntary organization, making that a similarity rather than the clearest distinction.'),
            ('Whether religion could encourage members to support community improvement.', 'Religion could motivate community work in both settings.'),
            ('Whether either group needed resources to maintain its activities.', 'Resource needs are common to both kinds of institution.'),
            ('How racial exclusion shaped the need to secure control over leadership and resources.', 'Racial discrimination gave organizational autonomy a particular importance for Black communities.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly extend the summary into an account of ordinary members’ experiences?', 1, [
            ('A later biography concentrating on Allen’s appointment as bishop.', 'A leadership biography may add context but remains centered on an institutional leader.'),
            ('Aid ledgers and correspondence from members describing support received and participation in association decisions.', 'These records can reveal members’ material experiences and involvement beyond the founders’ careers.'),
            ('A list of dates on which new church buildings were dedicated.', 'Dedication dates establish institutional growth but reveal relatively little about members’ everyday experiences.'),
            ('A theological statement specifying the denomination’s formal beliefs.', 'Formal doctrine describes prescribed belief rather than directly documenting members’ participation or assistance.'),
        ]),
    ],
)
