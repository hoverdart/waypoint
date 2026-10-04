"""Original questions using a short public-domain Mayflower Compact excerpt."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 2: 1607-1754', topic='The English Colonies: Regional Development', code='2.3', set_id='mayflower-compact',
    source_url='https://avalon.law.yale.edu/17th_century/mayflower.asp',
    source_kind='primary excerpt',
    stimulus='Mayflower Compact, 1620, excerpt: “covenant and combine ourselves together into a civil Body Politick, for our better Ordering and Preservation”.',
    items=[
        ('sourcing', 2, 'What immediate purpose is expressed in the excerpt?', 1, [
            ('To declare all English colonies independent of the monarchy.', 'The excerpt creates a local governing association, not independence for all colonies.'),
            ('To establish an agreed civil association for collective order.', 'The signers combine into a political body for ordering and preservation.'),
            ('To set uniform trade duties for the entire Atlantic empire.', 'No such imperial trade schedule appears in the excerpt.'),
            ('To end all collective obligations among the settlers.', 'The covenant creates mutual obligations rather than abolishing them.'),
        ]),
        ('contextualization', 3, 'The compact is most useful as evidence of which feature of English colonial development?', 2, [
            ('The absence of local institutions in English settlements.', 'The agreement provides evidence of local institution-building.'),
            ('An identical constitution imposed on every settlement.', 'A particular settlement’s agreement does not establish a uniform colonial constitution.'),
            ('The development of local arrangements for governance within the colonial setting.', 'The compact illustrates settlers forming a civil association to meet local governing needs.'),
            ('The disappearance of religion from colonial political language.', 'Covenant language does not establish the disappearance of religious influence.'),
        ]),
        ('argumentation', 4, 'What additional evidence is essential before using this excerpt to claim universal political participation?', 0, [
            ('Records identifying who could consent, vote, hold office, and participate in subsequent government.', 'The collective language does not define the participation rights of every person affected by the government.'),
            ('The document’s date alone.', 'Dating the agreement does not establish eligibility to participate.'),
            ('The number of words in the excerpt.', 'Length does not establish the political rights of inhabitants.'),
            ('A later author’s praise treated as a complete description of colonial practice.', 'Later commemoration cannot substitute for evidence of actual participation rules.'),
        ]),
        ('comparison', 3, 'How does an agreement to form a political body differ from a detailed constitution?', 3, [
            ('An agreement cannot create any expectation of collective action.', 'The excerpt expressly creates a collective civil association.'),
            ('A detailed constitution must reject all consent from those it governs.', 'Institutional detail does not require rejection of consent.'),
            ('The two documents necessarily specify exactly the same offices and procedures.', 'The excerpt does not specify those institutional arrangements.'),
            ('An agreement may establish a commitment to govern together without specifying a complete institutional structure.', 'The excerpt describes association and purpose, leaving particular offices and procedures unspecified.'),
        ]),
    ],
)
