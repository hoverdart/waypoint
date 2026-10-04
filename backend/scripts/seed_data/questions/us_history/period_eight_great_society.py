"""Original historical practice on Great Society health programs."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Great Society', code='8.9', set_id='health-programs',
    source_url='https://www.archives.gov/milestone-documents/medicare-and-medicaid-act',
    source_kind='original instructional summary',
    stimulus='The Social Security Amendments of 1965 established Medicare for older Americans and Medicaid assistance for eligible low-income groups. These programs extended public responsibility for health coverage, following earlier debates over national health insurance. They did not establish one universal program covering every resident. This is an original instructional summary of the programs at enactment, not current eligibility guidance.',
    items=[
        ('contextualization', 2, 'The legislation most directly illustrates which Great Society objective?', 2, [
            ('Replacing federal social programs with exclusive reliance on local charity.', 'The legislation expanded public responsibility rather than withdrawing it.'),
            ('Limiting domestic reform to military veterans alone.', 'The programs addressed older people and eligible low-income groups, not veterans alone.'),
            ('Using federal policy to reduce forms of insecurity associated with age and poverty.', 'Health coverage extended the public role in addressing these sources of insecurity.'),
            ('Requiring universal military service as the basis of access to medical care.', 'The historical program categories did not impose that requirement.'),
        ]),
        ('comparison', 3, 'Which distinction best describes the original programs in the summary?', 0, [
            ('Medicare centered on older Americans, while Medicaid served eligible low-income groups through a separate program.', 'Different eligibility frameworks mattered even though both expanded health coverage.'),
            ('Both programs initially used age alone as their sole eligibility criterion.', 'This incorrectly treats Medicaid as identical to Medicare.'),
            ('Medicaid provided only retirement pensions, while Medicare provided only unemployment payments.', 'Both concerned health coverage rather than those cash-benefit categories.'),
            ('The programs were two names for a single universal insurance system.', 'They were distinct programs and did not cover every resident as one universal system.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess whether expanded coverage improved practical access to care?', 1, [
            ('The signing date alone compared with the date of an earlier proposal.', 'Legislative chronology does not measure access to services.'),
            ('Enrollment, use of services, and remaining access barriers among eligible groups before and after implementation.', 'These measures distinguish formal coverage from practical changes and remaining limits.'),
            ('A statement that all eligible residents necessarily received identical care immediately.', 'That assumes the outcome instead of testing it.'),
            ('The total number of congressional speeches without their content or subsequent program records.', 'Speech counts do not establish implementation or access.'),
        ]),
    ],
)
