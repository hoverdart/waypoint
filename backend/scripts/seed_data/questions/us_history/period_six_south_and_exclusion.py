"""Original Period 6 items on agricultural dependency and immigration exclusion."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 6: 1865-1898', topic='The New South', code='6.4', set_id='land-and-labor',
    source_url='https://www.nps.gov/semo/learn/historyculture/lowndes-interpretive-center.htm',
    source_kind='original instructional summary',
    stimulus='After emancipation, many Black southerners lacked land of their own. Under sharecropping arrangements, families worked land owned by others in exchange for a portion of the crop. Landowners retained substantial power over access to land and agricultural decisions, while violence and intimidation could reinforce that power. Legal freedom therefore coexisted with severe constraints on economic independence. This original summary concerns the post-Civil War agricultural system, not the later twentieth-century statistics on the referenced page.',
    items=[
        ('comparison', 2, 'Which interpretation best distinguishes the change in legal status from continuity in economic power?', 1, [
            ('Emancipation redistributed most plantation land, making landownership a weak source of influence.', 'Emancipation did not generally redistribute plantation land to formerly enslaved people; unequal ownership remained consequential.'),
            ('Formerly enslaved people gained legal freedom while unequal landownership continued to limit their bargaining power.', 'The summary distinguishes the end of chattel slavery from persistent constraints arising from control of land and coercion.'),
            ('Sharecropping restored the legal ownership of workers as property under a different name.', 'Sharecropping could involve exploitation and coercion, but it was not legally identical to chattel slavery.'),
            ('Agricultural employment shifted mainly to independent wage contracts unrelated to crop output.', 'The arrangement described compensates labor through a crop share and links access to land with the harvest.'),
        ]),
        ('causation', 3, 'Why would threats of eviction be a particularly significant source of pressure under the arrangement described?', 2, [
            ('They would primarily reduce the tenant family’s returns on independently owned industrial investments.', 'The described vulnerability concerns dependence on another person’s land, not independent industrial holdings.'),
            ('They would remove a constitutional guarantee that each freed family receive a plantation.', 'The Constitution did not guarantee a plantation to each freed family.'),
            ('They could jeopardize both the family’s livelihood and its ability to remain where it lived.', 'Dependence on access to the land made eviction a threat to economic survival and residence.'),
            ('They would automatically transfer control of the harvest from the landowner to a federal agency.', 'Eviction did not itself create federal control of the harvest.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test a claim that agricultural workers gained greater economic autonomy in a particular county during the late nineteenth century?', 0, [
            ('Changes in landownership, contract terms, and workers’ ability to leave arrangements, examined alongside reports of coercion.', 'These sources address both formal economic arrangements and practical freedom to make decisions.'),
            ('A rise in the county’s total cotton output without information about ownership or distribution of returns.', 'Higher output can coexist with unequal control and does not alone establish workers’ autonomy.'),
            ('An industrial promoter’s claim that the region had entered a new era, treated as a direct measure of agricultural bargaining power.', 'Promotional language is evidence of an argument, not a direct measurement of workers’ control over their conditions.'),
            ('The existence of written contracts, without examining their terms or the circumstances in which they were enforced.', 'A written agreement alone does not establish equal bargaining power or freedom from coercion.'),
        ]),
    ],
)

QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Responses to Immigration', code='6.9', set_id='chinese-exclusion',
    source_url='https://www.archives.gov/milestone-documents/chinese-exclusion-act',
    source_kind='original instructional summary',
    stimulus='The Chinese Exclusion Act of 1882 suspended the entry of Chinese laborers for ten years and barred Chinese people from naturalization. The law distinguished laborers from some other categories of travelers, while documentary requirements constrained entry. It translated anti-Chinese pressures into federal restrictions rather than imposing the same rule on every immigrant group. This is an original instructional summary of the law, not a quotation.',
    items=[
        ('contextualization', 2, 'The act most directly illustrates which development in late-nineteenth-century immigration policy?', 3, [
            ('The replacement of federal immigration rules with decisions made entirely by private employers.', 'The act used federal law to regulate admission and naturalization.'),
            ('The creation of a uniform numerical quota applied equally to every country of origin.', 'The measure targeted Chinese immigration rather than establishing an equal worldwide quota system.'),
            ('The extension of naturalization eligibility to Chinese residents as compensation for limits on new arrivals.', 'The act barred naturalization rather than extending it as compensation.'),
            ('The use of national authority to enforce exclusion directed at a particular group.', 'The restrictions made anti-Chinese exclusion part of federal immigration and citizenship policy.'),
        ]),
        ('comparison', 3, 'Which distinction is necessary to describe the act accurately?', 0, [
            ('Restriction of entry and restriction of naturalization were separate provisions affecting different legal processes.', 'Admission concerns entry into the country; naturalization concerns acquiring citizenship. The law addressed both.'),
            ('Naturalization restrictions applied only to people who had not yet entered the country.', 'Naturalization is a process that residents might seek; it is not simply a rule about future admission.'),
            ('The suspension of labor immigration meant the law required immediate removal of every Chinese resident.', 'The described admission restriction should not be conflated with a universal order to expel all residents.'),
            ('Exemptions for some travelers meant restrictions had no practical effect on entry.', 'Limited categories and documentary requirements did not make the exclusion policy ineffective or unrestricted.'),
        ]),
        ('sourcing', 4, 'A historian uses the statute to study Chinese immigrants’ experiences. Which additional source would most directly reveal how officials applied its categories to individuals?', 2, [
            ('An unrelated factory’s production totals, without employee or immigration records.', 'Production totals do not show how immigration officials classified applicants.'),
            ('The statute’s title alone, treated as a complete record of administrative decisions.', 'A title cannot reveal the evidence, questioning, or judgments used in individual cases.'),
            ('Admission case files containing applications, questioning, and decisions, evaluated for the officials’ institutional perspective.', 'Case files can reveal implementation and individual encounters while requiring attention to how officials created the record.'),
            ('A later general population total, without information about admissions or applicant categories.', 'Aggregate population counts cannot reconstruct the administrative reasoning in particular admission cases.'),
        ]),
    ],
)
