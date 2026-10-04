"""Original questions on diplomatic expansion and historical inference."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Manifest Destiny and Continued Expansion', code='5.2', set_id='oregon-settlement',
    source_url='https://history.state.gov/milestones/1830-1860/oregon-territory',
    source_kind='original instructional summary',
    stimulus='In 1846, the United States and Britain negotiated a settlement of their competing claims in the Oregon country, using the 49th parallel for the mainland boundary. During the same year, the United States went to war with Mexico. This is an original instructional summary of contrasting routes to territorial expansion.',
    items=[
        ('comparison', 2, 'Which comparison best describes the two developments?', 2, [
            ('Both depended on the defeat of British forces in North America.', 'The Oregon settlement was negotiated with Britain; the war involved Mexico.'),
            ('Both were territorial purchases completed without military conflict.', 'The Mexican-American War was an armed conflict, not simply a peaceful purchase.'),
            ('Expansion involved a negotiated boundary agreement in one case and armed conflict in the other.', 'The comparison identifies different means of pursuing territorial objectives.'),
            ('The Oregon settlement resulted from the same peace treaty that ended the war with Mexico.', 'The Oregon agreement with Britain and the later peace with Mexico were separate settlements.'),
        ]),
        ('argumentation', 3, 'Which claim is most clearly challenged by the Oregon settlement?', 0, [
            ('Expansionist goals necessarily required war with every competing foreign power.', 'A negotiated settlement with Britain shows that expansionist policy could include diplomatic compromise.'),
            ('Territorial expansion was a major issue in American diplomacy during the 1840s.', 'The settlement supports the importance of territorial questions in diplomacy.'),
            ('Different foreign relationships could produce different methods of resolving territorial claims.', 'The contrasting cases support rather than challenge this claim.'),
            ('National leaders could accept a boundary agreement while continuing to pursue expansion elsewhere.', 'The simultaneous developments are consistent with this claim.'),
        ]),
        ('sourcing', 4, 'What additional evidence would be needed to assess whether the Oregon agreement represented the interests of Native nations in the region?', 1, [
            ('The assumption that an agreement between Britain and the United States represented every resident.', 'Agreement between two governments does not establish representation or consent of other peoples.'),
            ('Records of Native leaders’ positions and participation, compared with the treaty negotiations and subsequent land policies.', 'These sources can examine representation, consent, and consequences beyond the agreement between the two powers.'),
            ('A map of the new international boundary alone.', 'A boundary map cannot establish Native participation or responses.'),
            ('The fact that Britain and the United States avoided war with each other.', 'Peace between those governments does not by itself establish the treatment of Native interests.'),
        ]),
    ],
)
