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
            ('Disputes over how land should be redistributed to formerly enslaved families.', 'Land ownership was a major Reconstruction issue, but the citizenship clause does not allocate property.'),
            ('The terms under which former Confederate officials could return to public office.', 'Other Reconstruction provisions addressed officeholding; the quoted citizenship clause does not set those terms.'),
            ('The conditions governing repayment of debts incurred by the Confederacy.', 'War debt was addressed elsewhere in the amendment, not by the quoted citizenship provision.'),
        ]),
        ('claims-evidence', 3, 'What change in federal-state relations is most clearly reflected in the excerpt and its context?', 2, [
            ('National citizenship continued to depend on each state’s willingness to recognize it.', 'The amendment established a national constitutional definition rather than making citizenship contingent on state approval.'),
            ('Protection of individual rights remained solely a matter of state constitutional law.', 'The amendment placed limits on states in the federal Constitution.'),
            ('National constitutional guarantees limited state treatment of citizenship and individual rights.', 'The amendment constrained state authority through citizenship and equal-protection guarantees.'),
            ('State citizenship replaced national citizenship as the sole basis for legal membership.', 'The text recognizes national and state citizenship together, not the replacement of one by the other.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess the gap between the amendment’s guarantees and residents’ experiences during Reconstruction?', 1, [
            ('Congressional speeches advocating ratification, read without records of later enforcement.', 'These illuminate intended goals and arguments but cannot alone establish implementation in communities.'),
            ('Petitions describing discriminatory treatment compared with court decisions and officials’ responses in the same communities.', 'These records connect reported violations to institutional responses and can reveal the extent and limits of enforcement.'),
            ('State ratification tallies compared with party membership in the ratifying legislatures.', 'These help explain political support for adoption, not how rights were enforced after adoption.'),
            ('Newspaper editorials celebrating the amendment without testimony or records from affected residents.', 'Celebratory commentary documents reception, but offers less direct evidence of lived treatment and official responses.'),
        ]),
    ],
)
