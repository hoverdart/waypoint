"""Original questions on sectional balance and the Missouri settlement."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Politics and Regional Interests', code='4.3', set_id='missouri',
    source_url='https://www.archives.gov/milestone-documents/missouri-compromise', source_kind='original instructional summary',
    stimulus='The Missouri settlement paired Maine’s admission as a free state with Missouri’s admission as a slave state. It also prohibited slavery in the remaining Louisiana Purchase territory north of 36°30′, except Missouri. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('causation', 2, 'Pairing the two states’ admissions most directly addressed concern about', 1, [
            ('the location of the national capital.', 'The pairing concerned sectional representation, not relocation of the capital.'),
            ('the balance between free and slave states in the Senate.', 'Each state received two senators, so the pairing preserved a balance in that chamber.'),
            ('ending all congressional representation for western states.', 'Both states gained representation rather than losing it.'),
            ('restoring French control of Louisiana.', 'The settlement regulated American statehood and territory, not French sovereignty.'),
        ]),
        ('claims-evidence', 3, 'Which statement accurately describes the territorial restriction?', 3, [
            ('It abolished slavery everywhere in the United States.', 'The restriction applied to specified territory, not nationwide abolition.'),
            ('It prohibited slavery in Missouri itself.', 'Missouri was explicitly excepted and entered as a slave state.'),
            ('It prohibited slavery throughout every territory south of the line.', 'The described restriction applied north of the line, with the Missouri exception.'),
            ('It drew a geographic limit within the Louisiana Purchase while making an exception for Missouri.', 'This distinguishes the settlement’s territorial scope from its exception.'),
        ]),
        ('contextualization', 3, 'Which broader development made this dispute especially significant?', 0, [
            ('Westward expansion repeatedly raised questions about slavery and political representation.', 'New territories and states brought the future of slavery and sectional influence before Congress.'),
            ('The end of all migration across the Appalachians.', 'Westward migration continued rather than ending.'),
            ('The abolition of state representation in the Senate.', 'States retained equal Senate representation.'),
            ('The disappearance of plantation agriculture before 1820.', 'Plantation slavery remained central to the southern economy.'),
        ]),
        ('argumentation', 4, 'Which interpretation best describes the limits of this compromise?', 2, [
            ('It established unanimous agreement that slavery should end immediately.', 'Admission of a slave state and a geographic restriction did not constitute agreement on immediate abolition.'),
            ('It ensured that future territorial acquisitions could never raise sectional disputes.', 'The settlement could not prevent future disputes over additional territory.'),
            ('It managed an immediate sectional conflict without resolving the underlying dispute over slavery’s expansion.', 'A negotiated boundary and balanced admissions addressed the immediate controversy while leaving deeper disagreements intact.'),
            ('It removed slavery from national politics permanently.', 'Slavery remained a recurring and intensifying national political issue.'),
        ]),
    ],
)
