"""Original questions connecting policy, leisure, and uneven industrial change."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 6: 1865-1898', topic='Contextualizing Period 6', code='6.1', set_id='homestead-context',
    source_url='https://www.archives.gov/milestone-documents/homestead-act', source_kind='original instructional summary',
    stimulus='The Homestead Act of 1862, enacted during the Civil War, offered eligible applicants a route to ownership of surveyed public land through settlement and cultivation. It helped shape migration after the war. Access to a claim did not supply the money needed for tools, livestock, and establishing a farm. This original summary identifies a pre-1865 policy relevant to the following period; it does not imply that land described as public was uninhabited or that all applicants obtained lasting prosperity.',
    items=[
        ('contextualization', 2, 'Why is the 1862 act useful for contextualizing developments after 1865?', 1, [
            ('It demonstrates that postwar migration occurred independently of national policy.', 'The act instead provides an example of national policy influencing settlement.'),
            ('It established a federal land policy during wartime whose effects continued into postwar settlement.', 'The act links Civil War-era policy decisions to developments in the following period.'),
            ('It shows that federal land policy began only after the Civil War ended.', 'The 1862 enactment predates the end of the war and contradicts that claim.'),
            ('It ended the need for capital in agricultural production after 1865.', 'The summary explicitly distinguishes access to land from the resources needed to establish a farm.'),
        ]),
        ('causation', 3, 'Which factor could limit the act’s ability to make landownership accessible to poor families?', 2, [
            ('The absence of any relationship between farming and material resources.', 'Establishing a farm required resources such as tools, livestock, and shelter.'),
            ('A universal federal guarantee to pay every claimant’s operating expenses.', 'The summary describes no such guarantee; expenses remained a barrier.'),
            ('The need to finance settlement and cultivation even when the land claim itself required relatively little payment.', 'Low entry costs for land did not remove the costs of starting and sustaining agricultural production.'),
            ('The requirement that every applicant already own a large railroad corporation.', 'Eligibility did not depend on owning a railroad corporation.'),
        ]),
        ('sourcing', 4, 'What evidence would best test whether the law produced durable ownership for a particular group of applicants?', 0, [
            ('Applications linked to final patents, later land records, and household circumstances.', 'Following claims through acquisition and subsequent ownership distinguishes initial access from lasting outcomes.'),
            ('The statute’s promise treated as proof that every claim succeeded.', 'Legal opportunity does not establish that all applicants fulfilled requirements or retained their farms.'),
            ('A single promotional notice without records of claims or settlement.', 'Promotion can reveal how opportunities were presented but not their long-term results.'),
            ('The acreage available nationally without identifying who applied or received title.', 'Aggregate availability does not show outcomes for a specific applicant group.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Development of the Middle Class', code='6.10', set_id='leisure-access',
    source_url='https://www.loc.gov/collections/america-at-work-and-leisure-1894-to-1915/articles-and-essays/america-at-leisure/',
    source_kind='original instructional summary',
    stimulus='In the decades after the Civil War, organized recreation and interest in exercise expanded. Facilities available to the public helped extend participation in activities beyond wealthy patrons to working- and middle-class participants. Access to recreation still depended on practical conditions such as time, location, and cost. This is an original summary of nineteenth-century developments; the referenced collection also contains later material that is not being assigned to Period 6.',
    items=[
        ('comparison', 2, 'Which interpretation best describes the relationship between class and recreation in the summary?', 3, [
            ('Recreation remained exclusively a privilege of wealthy patrons in every setting.', 'The summary describes expanded participation beyond wealthy patrons.'),
            ('The expansion of facilities eliminated every difference in access among social groups.', 'Wider availability did not automatically erase limits involving time, cost, or location.'),
            ('Working-class participation meant middle-class participation necessarily disappeared.', 'Participation by one group did not require exclusion of the other.'),
            ('Participation broadened while practical barriers could still produce unequal access.', 'The summary presents expansion and continuing constraints together.'),
        ]),
        ('causation', 3, 'Which change would most directly make an existing recreation facility usable by employees with long daytime schedules?', 0, [
            ('Opening hours that included times when those employees were not working.', 'Scheduling affects whether formal availability translates into practical access.'),
            ('Advertising its existence only during the hours employees were required to work.', 'Awareness alone does not resolve a schedule conflict.'),
            ('Restricting admission to patrons with inherited wealth.', 'That restriction would narrow access rather than address employees’ available time.'),
            ('Moving every activity farther from the neighborhoods where employees lived.', 'Greater distance could increase the time and cost barriers.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess a claim that leisure participation became less exclusive in a city during this period?', 1, [
            ('One advertisement claiming that an activity was for everyone.', 'An inclusive advertisement is not by itself evidence of who could attend or actually participated.'),
            ('Participation records and admission rules compared with fees, work schedules, and neighborhood access over time.', 'These sources can connect changes in rules and resources with the composition of participants.'),
            ('A photograph of one well-attended event treated as a representative sample of all residents.', 'A single image cannot establish representativeness or changes across social groups.'),
            ('The number of wealthy residents alone, without any evidence about facilities or participation.', 'That count does not directly establish whether access broadened.'),
        ]),
    ],
)

QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Continuity and Change in Period 6', code='6.14', set_id='uneven-industrialization',
    source_url='https://www.loc.gov/classroom-materials/united-states-history-primary-source-timeline/rise-of-industrial-america-1876-1900/overview/',
    source_kind='original instructional summary',
    stimulus='After the Civil War, industrial growth and migration changed where many Americans lived and worked. Expanding national markets connected regions more closely, and new industrial wealth and middle-class opportunities emerged. Economic gains were not shared evenly. This original summary describes broad changes and unequal outcomes rather than claiming that industrialization replaced every earlier occupation or erased regional differences.',
    items=[
        ('comparison', 2, 'Which thesis best accounts for both change and limits in the summary?', 2, [
            ('Industrial growth left employment and settlement patterns entirely unchanged.', 'The summary identifies changes in work, migration, and markets.'),
            ('The growth of industry immediately made every household equally prosperous.', 'The summary explicitly identifies unequal gains.'),
            ('Industrialization reorganized work and markets while prosperity remained unevenly distributed.', 'This interpretation combines substantial economic change with limits on who benefited.'),
            ('Closer market connections ended all regional differences in production.', 'Integration does not require identical production or the disappearance of regional differences.'),
        ]),
        ('argumentation', 3, 'Which finding would most directly challenge a claim that national output growth proves universal improvement in living conditions?', 0, [
            ('Household evidence showing stagnant or declining living conditions among some groups while aggregate output rose.', 'Different household outcomes can contradict the inference from total output to universal improvement.'),
            ('An additional estimate confirming that total national output increased.', 'That supports aggregate growth but does not establish its distribution.'),
            ('A list of newly established corporations without information about households.', 'Corporate formation alone cannot measure every household’s living conditions.'),
            ('A statement that economic change can be measured only through national totals.', 'This excludes rather than evaluates the distributional evidence needed to test the claim.'),
        ]),
        ('sourcing', 4, 'Which research design would best distinguish occupational change from continuity across the period?', 1, [
            ('Using a single factory photograph as proof that all Americans became industrial workers.', 'A photograph cannot establish the occupational distribution of a nation.'),
            ('Comparing occupational records across multiple dates and regions while checking for changes in classification.', 'Comparable records can reveal both shifting shares and continuing occupations; classification changes must be considered.'),
            ('Treating the appearance of a new occupation as proof that every older one disappeared.', 'New and older occupations can coexist.'),
            ('Comparing unrelated categories without checking what each record counted.', 'Inconsistent categories can create apparent changes that reflect measurement rather than historical transformation.'),
        ]),
    ],
)
