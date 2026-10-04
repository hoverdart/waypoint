"""Original questions on the consequences and evidentiary limits of a treaty."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='The Mexican-American War', code='5.3', set_id='guadalupe-hidalgo',
    source_url='https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo',
    source_kind='original instructional summary',
    stimulus='The 1848 Treaty of Guadalupe Hidalgo ended the war between Mexico and the United States. Mexico ceded a vast northern territory, and the United States agreed to pay $15 million and assume specified claims against Mexico. The treaty also addressed the property and citizenship of Mexican residents in the transferred territory. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('causation', 2, 'Why did the territorial settlement intensify political conflict within the United States?', 1, [
            ('It required the immediate admission of every acquired territory as a slave state.', 'The treaty did not prescribe such automatic state admissions.'),
            ('It enlarged the area over which Americans disputed the future status of slavery.', 'Acquired territory renewed disputes about slavery’s expansion and sectional power.'),
            ('It abolished slavery in the existing southern states.', 'The settlement did not abolish slavery in those states.'),
            ('It transferred control of Congress to Mexican residents of the ceded territory.', 'Changing territorial sovereignty did not transfer control of Congress in that manner.'),
        ]),
        ('sourcing', 3, 'What limitation applies when using the treaty to study Mexican residents’ property rights after the war?', 2, [
            ('Diplomatic agreements cannot provide evidence about legal commitments.', 'Treaties are direct evidence of formal commitments between governments.'),
            ('The presence of property provisions proves that every resident retained all property without dispute.', 'A formal guarantee does not by itself establish how it was implemented in individual cases.'),
            ('The treaty establishes formal commitments, while land claims and court records are needed to examine implementation.', 'Distinguishing prescribed rights from lived outcomes requires evidence beyond the agreement.'),
            ('The treaty can establish residents’ experiences more precisely than their own property claims.', 'The agreement alone cannot reconstruct individual experiences or resolve every claim.'),
        ]),
        ('argumentation', 4, 'Which interpretation best accounts for both the payment and the wartime context of the settlement?', 0, [
            ('The payment was part of a territorial settlement reached after military conflict, so it does not by itself establish an equal bargaining relationship.', 'Financial terms must be interpreted alongside the circumstances in which the agreement was negotiated.'),
            ('The payment establishes that the territorial transfer was unrelated to the preceding war.', 'The treaty ended the war; payment does not sever that connection.'),
            ('The military context means that the treaty contained no negotiated financial obligations.', 'The summary identifies financial obligations despite the unequal wartime context.'),
            ('The payment proves that residents in every affected community approved the new boundary.', 'An agreement between governments does not establish unanimous local consent.'),
        ]),
    ],
)
