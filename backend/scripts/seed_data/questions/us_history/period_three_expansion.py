"""Original source-analysis questions; historical excerpt is public domain."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='Movement in the Early Republic', code='3.12',
    source_url='https://www.archives.gov/milestone-documents/northwest-ordinance',
    source_kind='primary excerpt',
    stimulus='Northwest Ordinance, Confederation Congress, 1787, section 13: “for their admission to a share in the federal councils on an equal footing with the original States”',
    items=[
        ('claims-evidence', 2, 'The provision most directly proposed which political future for western territories?', 2, [
            ('Permanent rule by the original states without representation.', 'Equal admission envisioned eventual statehood rather than permanent subordinate status.'),
            ('Independence as countries outside the United States.', 'Admission to federal councils meant participation within the Union.'),
            ('Admission as states with political standing equal to existing states.', 'The phrase equal footing identifies the intended relationship of new states to the original states.'),
            ('Immediate voting rights in Congress for every territorial resident.', 'The provision concerns eventual states, not immediate individual suffrage or territorial voting rights.'),
        ]),
        ('contextualization', 3, 'Which circumstance best explains the need for this provision in 1787?', 0, [
            ('The United States needed a framework for governing western lands and incorporating new states.', 'Independence left the Confederation with western territorial claims and a need to organize settlement and government.'),
            ('The Louisiana Purchase had doubled the nation’s claimed territory.', 'The Louisiana Purchase occurred in 1803, after the ordinance.'),
            ('The Mexican Cession required a settlement over western statehood.', 'The Mexican Cession occurred in 1848, decades after this provision.'),
            ('The British government was establishing elected colonial assemblies before independence.', 'The issuing government was the Confederation Congress of the independent United States.'),
        ]),
        ('argumentation', 4, 'A historian uses this provision to qualify the claim that the Confederation government accomplished nothing. Which argument best uses the evidence?', 3, [
            ('Congress had already secured equal voting rights for all residents.', 'Equality among states does not establish universal suffrage among individuals.'),
            ('Congress could directly collect every tax needed to govern the territory.', 'A statehood provision does not demonstrate an unrestricted federal taxing power.'),
            ('All conflicts over western land had ended before ratification of the Constitution.', 'A legal framework alone cannot establish the absence of conflict over land.'),
            ('Congress established an approach to territorial incorporation despite its broader institutional weaknesses.', 'The ordinance supplies a specific achievement without requiring the claim that the Confederation solved every problem.'),
        ]),
        ('sourcing', 3, 'Which additional evidence would best test whether this promised political status was realized?', 1, [
            ('A map showing only the region’s rivers and mountains.', 'Physical geography alone does not establish new states’ political standing.'),
            ('Admission acts and congressional representation records for states formed from the territory.', 'These records connect the legal promise to actual admission and participation in federal institutions.'),
            ('A second copy of the same ordinance printed in a different typeface.', 'Repeating the same prescription does not independently demonstrate its implementation.'),
            ('A European monarch’s genealogy.', 'A genealogy provides no direct evidence about the admission or representation of these states.'),
        ]),
    ],
)
