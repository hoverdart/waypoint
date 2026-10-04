"""Original questions distinguishing sectional concessions and consequences."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='The Compromise of 1850 and Escalating Sectional Conflict', code='5.4', set_id='sectional-concessions',
    source_url='https://www.archives.gov/milestone-documents/compromise-of-1850',
    source_kind='original instructional summary',
    stimulus='The measures enacted in 1850 admitted California as a free state, organized Utah and New Mexico as territories, settled the Texas boundary dispute, ended the slave trade in Washington, D.C., and strengthened federal procedures for recovering people claimed as fugitives from slavery. Slavery itself remained legal in the District of Columbia. This is an original instructional summary.',
    items=[
        ('claims-evidence', 2, 'Which distinction is necessary to describe the District of Columbia provision accurately?', 3, [
            ('Ending the slave trade in the District meant ending the trade throughout the United States.', 'The geographic scope of the provision was the District, not the entire country.'),
            ('Ending the slave trade and emancipating everyone enslaved in the District were the same measure.', 'The summary distinguishes restrictions on trade from the continued legality of slavery.'),
            ('Admission of California automatically changed the legal status of enslaved people in the District.', 'State admission and the District’s local legal provisions were separate matters.'),
            ('Restricting the trade did not itself abolish the institution of slavery in the District.', 'The settlement ended the trade while leaving slavery itself legal there.'),
        ]),
        ('causation', 3, 'Why could the stronger fugitive-slave provision generate conflict in free states?', 0, [
            ('It brought federal enforcement of enslavers’ claims into communities where many residents opposed slavery.', 'The provision extended conflict over slavery into disputes over enforcement and resistance in free states.'),
            ('It gave each free state final authority to disregard federal recovery procedures.', 'Strengthened federal procedures did not grant that final state authority.'),
            ('It replaced recovery claims with an automatic right to emancipation upon crossing a state line.', 'The measure strengthened recovery rather than making entry into a free state an automatic federal guarantee of freedom.'),
            ('It confined all recovery proceedings to the state from which the person had fled.', 'The conflict involved efforts to enforce claims where people had sought refuge, including free states.'),
        ]),
        ('argumentation', 4, 'Which interpretation best explains how the settlement could produce both immediate agreement and renewed conflict?', 2, [
            ('California’s admission required every legislator to accept abolition as a national goal.', 'Supporting a package of concessions did not establish agreement on nationwide abolition.'),
            ('The territorial provisions removed the need for later decisions about slavery in western lands.', 'Organizing territories did not resolve every future dispute over slavery’s status.'),
            ('Concessions assembled enough support for legislation while enforcement disputes exposed continuing disagreement over slavery.', 'Legislative agreement could manage an immediate crisis without eliminating incompatible sectional aims.'),
            ('Ending the slave trade in the District made the fugitive-slave provision irrelevant outside Washington.', 'The two provisions had different geographic and legal scopes; one did not neutralize the other.'),
        ]),
    ],
)
