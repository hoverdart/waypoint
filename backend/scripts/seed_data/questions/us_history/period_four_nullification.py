"""Original summary and questions on the nullification crisis."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Jackson and Federal Power', code='4.8', set_id='nullification',
    source_url='https://guides.loc.gov/nullification-proclamation', source_kind='original instructional summary',
    stimulus='South Carolina challenged federal tariff laws in 1832. Jackson rejected nullification. Congress subsequently authorized force to enforce federal law while adopting a compromise that reduced tariff rates over time. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('claims-evidence', 2, 'The central constitutional question in this crisis concerned whether', 1, [
            ('Congress could choose the British prime minister.', 'The crisis involved American federal and state authority, not British political offices.'),
            ('a state could invalidate a federal law within its boundaries.', 'Nullification asserted a state’s authority to render federal law ineffective within that state.'),
            ('all taxes had to be collected by foreign governments.', 'Foreign tax collection was not the issue.'),
            ('the presidency should become hereditary.', 'The crisis did not concern hereditary succession.'),
        ]),
        ('causation', 3, 'Why did the compromise tariff help reduce the immediate danger of confrontation?', 3, [
            ('It transferred all congressional powers to South Carolina.', 'The compromise changed tariff policy rather than transferring all federal legislative authority.'),
            ('It abolished the federal government.', 'Federal institutions continued to operate.'),
            ('It required every state to leave the Union.', 'The settlement helped avert confrontation rather than requiring disunion.'),
            ('It addressed tariff grievances while federal enforcement authority remained asserted.', 'Tariff reductions provided a policy concession alongside the federal government’s insistence that its laws could be enforced.'),
        ]),
        ('comparison', 3, 'Taken together with Jackson’s attack on the national bank, his response to nullification best supports which interpretation?', 0, [
            ('He opposed some federal institutions while vigorously defending federal authority in other conflicts.', 'Opposition to the Bank did not prevent Jackson from defending the Union and enforcement of tariff laws.'),
            ('He consistently supported every state’s claim against the federal government.', 'His rejection of South Carolina’s nullification claim contradicts this generalization.'),
            ('He refused to use presidential authority in domestic disputes.', 'Both conflicts involved assertive presidential action.'),
            ('He believed Congress should never pass economic legislation.', 'Opposition to a specific institution did not mean rejection of all congressional economic legislation.'),
        ]),
        ('argumentation', 4, 'Which conclusion would overstate what the settlement demonstrates?', 2, [
            ('Federal leaders combined enforcement measures with a policy compromise.', 'Both the force authorization and the tariff compromise support this description.'),
            ('Tariff policy could become a dispute about sovereignty.', 'The conflict connected economic legislation with competing claims about state and federal power.'),
            ('The settlement permanently ended sectional disputes about federal authority.', 'Resolving an immediate confrontation did not eliminate later sectional conflicts or debates about sovereignty.'),
            ('A concession on tariff rates did not necessarily concede the right of nullification.', 'Policy compromise and recognition of a constitutional right are distinct; federal enforcement authority was still asserted.'),
        ]),
    ],
)
