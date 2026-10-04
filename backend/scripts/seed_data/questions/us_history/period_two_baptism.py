"""Original questions around a short public-domain statutory excerpt."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 2: 1607-1754', topic='Slavery in the British Colonies', code='2.6', set_id='baptism-law',
    source_url='https://encyclopediavirginia.org/primary-documents/an-act-declaring-that-baptisme-of-slaves-doth-not-exempt-them-from-bondage-1667/',
    source_kind='primary excerpt',
    stimulus='Virginia General Assembly, September 1667, excerpt (original spelling): “the conferring of baptisme doth not alter the condition of the person as to his bondage or ffreedome”.',
    items=[
        ('contextualization', 2, 'Which legal distinction did this provision establish?', 1, [
            ('Baptism automatically converted lifetime enslavement into a fixed term of labor.', 'The provision states that baptism did not alter the person’s legal condition.'),
            ('Religious conversion did not itself change whether a person was enslaved or free.', 'The law separated baptism from emancipation.'),
            ('All baptized residents became eligible to govern the colony.', 'The provision concerns bondage and freedom, not universal political eligibility.'),
            ('Owners were required to free enslaved people before allowing baptism.', 'The provision removed baptism as a change in legal status rather than requiring prior emancipation.'),
        ]),
        ('causation', 3, 'How could this rule help entrench hereditary slavery?', 2, [
            ('It made every religious congregation responsible for abolishing slavery.', 'The provision preserved bondage despite baptism rather than imposing abolition.'),
            ('It required enslaved children to leave Virginia permanently.', 'No such removal requirement appears in the provision.'),
            ('It closed a possible religious basis for claiming that an enslaved person’s status had changed.', 'Separating conversion from freedom helped preserve legal bondage across changes in religious identity.'),
            ('It replaced colonial law with individual choice about labor status.', 'The assembly imposed a binding rule rather than allowing each person to choose their status.'),
        ]),
        ('sourcing', 4, 'Which additional evidence would best reveal enslaved people’s responses to the rule?', 0, [
            ('Petitions, testimony, or other records preserving enslaved people’s claims, interpreted with attention to how those records were produced.', 'These can supplement the lawmakers’ perspective with evidence of responses and legal strategies.'),
            ('The statute alone treated as a record of every enslaved person’s beliefs.', 'A legislative rule cannot establish the views of the people subjected to it.'),
            ('An assumption that the absence of emancipation meant the absence of religious life.', 'Legal status does not establish the absence of religious beliefs or practices.'),
            ('A later colony’s unrelated voting rules treated as testimony from Virginia’s enslaved population.', 'Those rules do not provide the relevant people’s responses to this statute.'),
        ]),
    ],
)
