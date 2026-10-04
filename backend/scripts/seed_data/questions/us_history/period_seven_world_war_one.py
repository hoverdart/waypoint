"""Original diplomacy and migration practice with historical source references."""
from .builders import source_set

TOPIC = 'American Imperialism and World War I'
QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic=TOPIC, code='7.5', set_id='wilson-peace',
    source_url='https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points',
    source_kind='original instructional summary',
    stimulus='In January 1918, while the war continued, Wilson presented a peace program calling for open diplomacy, reduced armaments, and an association of nations. The eventual settlement incorporated the League of Nations, but the U.S. Senate did not adopt the Treaty of Versailles and the United States did not join the League. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'Wilson’s proposed association of nations most directly reflected which approach to preventing future wars?', 1, [
            ('Using territorial annexation by the United States as the main guarantee of European stability.', 'Wilson proposed international guarantees, not general American annexation of Europe.'),
            ('Creating a continuing institution through which states could support collective security.', 'The proposed association sought cooperation and mutual guarantees beyond a single peace settlement.'),
            ('Restoring secret bilateral agreements as the foundation of peace.', 'Open diplomacy was a stated element of the program.'),
            ('Leaving each state to deter aggression solely through its own armaments.', 'The association and reduced armaments departed from reliance solely on unilateral military deterrence.'),
        ]),
        ('sourcing', 3, 'Why should a historian distinguish the January 1918 program from a neutral description of the postwar settlement?', 0, [
            ('It advanced wartime objectives before the final negotiations and could influence audiences still fighting.', 'Timing and purpose make the program evidence of advocated aims rather than proof that those aims were implemented.'),
            ('It recorded the Senate’s final vote after the treaty had taken effect.', 'The address preceded both the settlement and the Senate debate.'),
            ('It was a private diary intended only to record Wilson’s retirement experiences.', 'It was a public program presented during the war.'),
            ('It summarized a peace settlement that Wilson had no role in attempting to shape.', 'Wilson sought to shape the peace through these proposals and subsequent diplomacy.'),
        ]),
        ('argumentation', 4, 'Which conclusion is best supported by the contrast between the League’s creation and U.S. nonmembership?', 2, [
            ('Senate rejection proves that every European government rejected international cooperation.', 'A U.S. constitutional decision cannot establish the position of every European government.'),
            ('Wilson’s diplomatic influence gave him sole authority to commit the United States to the treaty.', 'The Senate outcome demonstrates that presidential influence did not confer sole treaty authority.'),
            ('A president could influence an international institution without securing domestic approval for participation.', 'The League appeared in the settlement even though the United States did not join.'),
            ('The absence of U.S. membership means the League never existed.', 'Institutional existence and American participation are different questions.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 7: 1890-1945', topic=TOPIC, code='7.6', set_id='migration-and-work',
    source_url='https://www.loc.gov/classroom-materials/great-migration',
    source_kind='original instructional summary',
    stimulus='World War I created industrial job opportunities that helped draw Black migrants from the South to other regions. Migration offered new possibilities, but arrivals still encountered discrimination in employment and housing. Wartime movement formed part of a much longer Great Migration rather than a process confined to the years of American combat. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Which relationship best explains the connection between war and the migration described?', 3, [
            ('Military victory removed the need for industrial workers in receiving cities.', 'The summary identifies expanded job opportunities as a draw, not disappearing industrial demand.'),
            ('Migration resulted from the wartime abolition of all regional economic differences.', 'Different opportunities across regions helped motivate movement.'),
            ('The federal government required all Black southerners to relocate as a condition of citizenship.', 'The movement was not a universal citizenship relocation requirement.'),
            ('Changes in industrial labor demand created opportunities that migrants could pursue.', 'Wartime economic conditions contributed a pull factor without explaining every individual decision.'),
        ]),
        ('comparison', 3, 'Which comparison would best distinguish occupational change from continuing racial barriers after a family moved?', 1, [
            ('The distance traveled compared with the length of the train ride.', 'Travel measurements do not reveal employment opportunities or housing exclusion.'),
            ('Jobs held before and after relocation alongside evidence of restrictions on housing at the destination.', 'The combination can reveal economic change and continuing discrimination at the same time.'),
            ('A national population total compared with the date war was declared.', 'These aggregate facts do not establish the family’s work or housing conditions.'),
            ('The family’s arrival date alone compared with the end of combat.', 'Chronology alone cannot measure occupational change or persistent barriers.'),
        ]),
        ('argumentation', 4, 'A historian attributes the entire Great Migration to U.S. combat mobilization in 1917–1918. Which evidence most directly challenges that explanation?', 0, [
            ('Substantial migration before and after those years, accompanied by evidence of continuing economic and social motives.', 'Movement outside the proposed interval requires an explanation broader than combat mobilization alone.'),
            ('An employer’s recruitment notice from 1917.', 'This supports a wartime mechanism but does not test whether it explains the entire longer movement.'),
            ('A migrant’s statement that a wartime job helped finance a move.', 'One wartime experience supports the mechanism without establishing its sufficiency for all migration.'),
            ('A record of increased factory production during the war.', 'Wartime industrial expansion is consistent with the claim but does not establish its full chronological reach.'),
        ]),
    ],
)
