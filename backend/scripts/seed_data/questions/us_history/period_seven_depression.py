"""Original Depression and social-insurance practice."""
from .builders import source_set

TOPIC = 'The Great Depression and the New Deal'
QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic=TOPIC, code='7.9', set_id='banking-contraction',
    source_url='https://www.federalreservehistory.org/essays/banking-panics-1930-31',
    source_kind='original instructional summary',
    stimulus='After the stock-market crash of 1929, banking panics in 1930 and 1931 intensified the downturn. Depositors held more cash, banks accumulated reserves, and the amount of money available through checking accounts contracted. This monetary mechanism helps explain the deepening crisis without making the crash the sole cause of every subsequent development. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Which sequence best describes the mechanism in the summary?', 1, [
            ('Bank runs increased deposits, which immediately expanded household purchasing power.', 'Withdrawals and hoarding reduced money held in checking accounts rather than expanding those deposits.'),
            ('Fear prompted withdrawals and reserve accumulation, reducing funds circulating through the banking system.', 'Depositor and bank responses together could intensify monetary contraction.'),
            ('Falling stock prices automatically canceled every borrower’s debt.', 'A decline in asset prices does not extinguish outstanding debt obligations.'),
            ('Higher bank reserves necessarily meant a proportional increase in new loans.', 'Banks could hold reserves instead of extending credit, especially during a panic.'),
        ]),
        ('comparison', 3, 'Which comparison best distinguishes a stock-market crash from a banking panic?', 2, [
            ('Both terms describe only a decline in farm output.', 'Neither is simply a measure of agricultural production.'),
            ('A crash concerns government elections, while a panic concerns tariffs.', 'These definitions do not describe the financial phenomena.'),
            ('A crash concerns a sharp fall in share prices, while a panic involves widespread attempts to withdraw bank funds.', 'The events can interact but concern different assets and institutions.'),
            ('A crash can affect confidence, while a banking panic has no connection to confidence.', 'Concern about access to deposits is central to a banking panic.'),
        ]),
        ('argumentation', 4, 'Which research design would best test whether banking disruption helped deepen the downturn?', 0, [
            ('Compare changes in credit, deposits, and employment across otherwise similar places with different banking disruption.', 'A comparison with attention to other conditions can test the proposed mechanism beyond simple national coincidence.'),
            ('Treat the occurrence of the 1929 crash as proof that every later policy was irrelevant.', 'This assumes the conclusion and excludes possible amplifying mechanisms.'),
            ('Use a single depositor’s fear to establish the precise national change in production.', 'One account cannot establish aggregate magnitude.'),
            ('Compare bank names without examining deposits, lending, or local economic conditions.', 'Names alone do not measure the financial mechanism or its consequences.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 7: 1890-1945', topic=TOPIC, code='7.10', set_id='social-insurance',
    source_url='https://www.archives.gov/milestone-documents/social-security-act',
    source_kind='original instructional summary',
    stimulus='The Social Security Act of 1935 established federal old-age benefits and supported state assistance and unemployment programs. Wage and payroll taxes helped finance the old-age insurance arrangement. The original law excluded agricultural labor and domestic service in a private home from its definition of covered employment for federal old-age benefits. This is an original instructional summary of selected provisions, not of every program in the act.',
    items=[
        ('contextualization', 2, 'Why is the old-age insurance system usually classified as lasting reform rather than only emergency relief?', 3, [
            ('It supplied only a single shipment of food to each city.', 'The law established continuing institutions and benefits rather than a one-time distribution.'),
            ('It required recipients to hold temporary construction jobs.', 'That describes a work-relief mechanism, not the old-age insurance arrangement.'),
            ('It made restoration of 1929 stock prices the condition for every payment.', 'The program’s eligibility and financing were not based on restoring a particular stock-market level.'),
            ('It created an ongoing federal mechanism for addressing a recurring source of economic insecurity.', 'Old-age insurance institutionalized a responsibility extending beyond immediate emergency assistance.'),
        ]),
        ('comparison', 3, 'Which description best captures the relationship between federal expansion and program limits?', 0, [
            ('Federal responsibility expanded, but occupational exclusions prevented universal coverage under old-age insurance.', 'The two features coexisted; expansion did not mean all workers were initially included.'),
            ('Occupational exclusions meant the federal government assumed no new responsibility.', 'Limits do not negate the creation of a new federal benefits system.'),
            ('Federal involvement eliminated every state role in assistance.', 'The act also supported state-administered programs.'),
            ('Payroll financing meant private employers alone determined the federal law’s terms.', 'A financing source does not transfer legislative authority to individual employers.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess whether the occupational exclusions produced unequal access across demographic groups?', 1, [
            ('The total number of pages in the statute.', 'Document length does not reveal who worked in excluded occupations.'),
            ('Employment data by occupation and demographic group combined with the original coverage rules.', 'This connects legal exclusions to the populations disproportionately working in excluded jobs.'),
            ('A later expansion of coverage treated as evidence that the original law covered everyone.', 'Later amendments cannot be projected backward onto the original statute.'),
            ('The tax rate alone without information about covered employment.', 'A rate cannot identify which workers were excluded from the system.'),
        ]),
    ],
)
