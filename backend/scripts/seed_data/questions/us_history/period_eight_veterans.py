"""Original questions on postwar opportunity and unequal access."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='Postwar Prosperity and Suburbanization', code='8.4', set_id='veterans-benefits',
    source_url='https://www.archives.gov/milestone-documents/servicemens-readjustment-act',
    source_kind='original instructional summary',
    stimulus='The 1944 G.I. Bill supported veterans’ transition to civilian life through education and training benefits and assistance with home and business purchases. Its effects extended into the postwar years. Black veterans nevertheless encountered discriminatory lending and barriers to purchasing homes in white suburbs. This is an original instructional summary of selected benefits and limits.',
    items=[
        ('causation', 2, 'How could the benefits described contribute to postwar economic growth?', 2, [
            ('By requiring veterans to remain in military service rather than seek civilian employment.', 'The program assisted readjustment to civilian life.'),
            ('By replacing private home purchases with mandatory residence in military barracks.', 'Home-purchase assistance supported civilian ownership rather than compulsory military housing.'),
            ('By helping veterans obtain training and finance purchases that expanded household opportunity and demand.', 'Education and purchase assistance could support both workers’ opportunities and economic activity.'),
            ('By making veterans’ education independent of funding or institutional access.', 'Benefits supplied resources, but actual education still required access to institutions.'),
        ]),
        ('comparison', 3, 'Which interpretation best reconciles expanded benefits with discriminatory housing outcomes?', 0, [
            ('Federal assistance expanded opportunity while institutions involved in lending and housing could restrict access unequally.', 'Formal benefits and discriminatory implementation could coexist.'),
            ('Housing discrimination proves that no veterans received meaningful assistance.', 'Unequal access does not negate benefits received by other veterans or all benefits received by Black veterans.'),
            ('The existence of benefits proves that lending practices were identical for all applicants.', 'A benefit’s existence does not establish equal treatment by lenders.'),
            ('Postwar home ownership can be explained solely by veterans’ personal preferences.', 'Policy and institutional barriers also shaped available choices.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test whether discriminatory lending limited use of housing benefits?', 1, [
            ('The number of veterans eligible nationwide without records of their applications.', 'Eligibility totals do not establish how applications were handled.'),
            ('Loan decisions for similarly situated applicants, compared by race and neighborhood, with lending-policy records.', 'These comparisons can connect unequal decisions to institutional practices while accounting for other applicant characteristics.'),
            ('Advertisements describing suburban homes as desirable.', 'Marketing establishes an appeal, not differential access to financing.'),
            ('The total number of homes built without information about buyers or financing.', 'Aggregate construction cannot reveal which eligible veterans obtained loans.'),
        ]),
    ],
)
