"""Original questions on immigration restriction and national identity."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic='1920s Cultural and Political Controversies', code='7.8', set_id='quota-policy',
    source_url='https://history.state.gov/milestones/1921-1936/immigration-act',
    source_kind='original instructional summary',
    stimulus='The 1924 immigration legislation tightened national-origin quotas and favored established northern and western European migration streams over newer southern and eastern European ones. It also excluded immigrants ineligible for citizenship, extending restrictions to Japanese immigration and provoking Japanese objections. This is an original instructional summary of selected restrictions, not a claim that every migrant faced the same admission rules.',
    items=[
        ('contextualization', 2, 'The quota preferences most directly reflected which political tendency?', 2, [
            ('An effort to distribute admission opportunities equally among all countries.', 'The preferences allocated opportunities unequally by origin.'),
            ('A decision to make industrial employers the sole authority over citizenship.', 'The policy was enacted by Congress and concerned admission restrictions.'),
            ('Nativist efforts to shape the national population through selective immigration restrictions.', 'The preferences treated some origins as more desirable and used admission policy to influence population composition.'),
            ('A requirement that every resident return to the country of their ancestors.', 'Admission restrictions were not a universal deportation requirement.'),
        ]),
        ('causation', 3, 'Why could the legislation affect foreign relations as well as domestic migration?', 0, [
            ('Other governments could view restrictions targeting their nationals as discriminatory treatment.', 'Japanese objections show how domestic admission rules could become a diplomatic grievance.'),
            ('National-origin quotas automatically created military alliances with excluded countries.', 'Exclusion did not create an alliance obligation.'),
            ('Admission legislation had no consequences outside the United States.', 'The Japanese response directly contradicts that claim.'),
            ('The law transferred control of American immigration offices to Japan.', 'Japanese objections did not confer control over American administration.'),
        ]),
        ('argumentation', 4, 'Which evidence would best evaluate the claim that the policy changed the composition, rather than merely the total volume, of immigration?', 1, [
            ('The nationwide admission total alone for one year.', 'A single total does not show how admissions were distributed among origins.'),
            ('Admissions by origin before and after implementation, assessed alongside quotas and other disruptions to migration.', 'Disaggregated evidence can test compositional change while considering competing explanations.'),
            ('The number of legislators attending the signing ceremony.', 'Attendance does not measure the composition of admissions.'),
            ('A later immigration law assumed to describe admissions rules in 1924.', 'Later rules cannot be projected backward onto the earlier policy.'),
        ]),
    ],
)
