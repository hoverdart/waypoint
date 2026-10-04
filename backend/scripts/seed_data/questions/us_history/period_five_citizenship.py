"""Original questions on Reconstruction's constitutional changes."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Reconstruction', code='5.10', set_id='fourteenth-amendment',
    source_url='https://www.archives.gov/founding-docs/amendments-11-27',
    source_kind='primary excerpt',
    stimulus='Fourteenth Amendment, ratified 1868, Section 1: “All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside.” The section also prohibits states from denying any person within their jurisdiction equal protection of the laws.',
    items=[
        ('contextualization', 2, 'Which Reconstruction problem did the citizenship provision most directly address?', 0, [
            ('The contested legal status of formerly enslaved people after abolition.', 'The provision placed national and state citizenship on a constitutional foundation that included formerly enslaved people.'),
            ('The absence of any constitutional procedure for electing a president.', 'Presidential election procedures already existed; this provision concerns citizenship.'),
            ('The need to restore legal ownership of emancipated people to former enslavers.', 'Citizenship recognized formerly enslaved people as members of the political community, not property.'),
            ('The requirement that every citizen hold federal office.', 'Citizenship does not require officeholding.'),
        ]),
        ('claims-evidence', 3, 'What change in federal-state relations is most clearly reflected in the excerpt and its context?', 2, [
            ('Each state gained exclusive authority to define national citizenship.', 'The amendment established a national constitutional definition rather than exclusive state discretion.'),
            ('State governments ceased to exist as distinct political institutions.', 'The text expressly recognizes citizenship in a state as well as in the United States.'),
            ('National constitutional guarantees limited state treatment of citizenship and individual rights.', 'The amendment constrained state authority through citizenship and equal-protection guarantees.'),
            ('The federal government delegated enforcement of all rights to private organizations.', 'The provision does not make such a delegation.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess the gap between the amendment’s guarantees and residents’ experiences during Reconstruction?', 1, [
            ('A count of printed copies of the amendment distributed nationally.', 'Distribution measures do not establish whether people received protection in practice.'),
            ('Petitions describing discriminatory treatment compared with court decisions and officials’ responses in the same communities.', 'These records connect reported violations to institutional responses and can reveal the extent and limits of enforcement.'),
            ('The assumption that ratification immediately ended every form of unequal treatment.', 'A legal guarantee cannot by itself demonstrate universal implementation.'),
            ('A list of state capitals without records of legal disputes or enforcement.', 'The locations of capitals do not establish how rights operated in residents’ lives.'),
        ]),
    ],
)
