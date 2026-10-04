"""Original mobilization and civil-rights practice."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic='World War II', code='7.12', set_id='fair-employment',
    source_url='https://www.archives.gov/milestone-documents/executive-order-8802',
    source_kind='original instructional summary',
    stimulus='As defense employment expanded in 1941, A. Philip Randolph and other Black leaders pressed for action against discrimination and threatened a mass march in Washington. Roosevelt issued Executive Order 8802, requiring nondiscrimination provisions in new defense contracts and establishing a committee to investigate complaints. Randolph called off the planned march. The policy concerned defense employment; it did not itself desegregate the armed forces. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Which interpretation best explains the connection between mobilization and the order?', 2, [
            ('Military preparation made civilian labor disputes irrelevant to federal policy.', 'The order shows that access to civilian defense employment became a federal concern.'),
            ('The expansion of defense jobs automatically eliminated discrimination before activists intervened.', 'Activists sought action because expanding employment still involved discriminatory barriers.'),
            ('Mobilization created opportunities that organized activists used to press demands for equal access.', 'The threat of collective action linked wartime labor needs with civil-rights demands.'),
            ('The order responded primarily to a demand that all defense contracts be canceled.', 'The demand concerned access to employment, not ending defense production.'),
        ]),
        ('comparison', 3, 'Which distinction is necessary when comparing this policy with the later desegregation of the military?', 0, [
            ('Regulating defense employment and changing military personnel policy addressed different institutions.', 'Civilian defense employment requirements did not themselves end segregation in the armed forces.'),
            ('Both policies concerned only voting qualifications in state elections.', 'Employment and military organization are distinct from state voting qualifications.'),
            ('The 1941 order had already abolished all forms of segregation in military units.', 'That overstates the order’s scope and erases the need for later military policy changes.'),
            ('Because defense companies were private, their federal contracts could contain no employment requirements.', 'The order explicitly used contracting requirements to address discrimination.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test whether the order changed hiring practices, beyond establishing a formal policy?', 1, [
            ('The fact that the planned march was canceled, without examining workplaces.', 'Cancellation indicates an activist response to the policy, not the extent of employer compliance.'),
            ('Hiring and job-assignment records before and after the order, together with complaints and their outcomes.', 'These records connect formal requirements to workplace behavior and enforcement.'),
            ('The order’s publication date alone.', 'Publication establishes timing but not implementation.'),
            ('A defense company’s total production, without information about its workforce.', 'Production alone cannot show whether discriminatory hiring or assignment changed.'),
        ]),
    ],
)
