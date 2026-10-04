"""Original youth activism and voting-rights evidence questions."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='Youth Culture of the 1960s', code='8.12', set_id='youth-voting-age',
    source_url='https://prologue.blogs.archives.gov/2013/11/13/records-of-rights-vote-old-enough-to-fight-old-enough-to-vote/',
    source_kind='original instructional summary',
    stimulus='During the Vietnam era, advocates of a lower voting age argued that citizens old enough for military service should be able to vote. This argument had earlier roots, including World War II. Ratified in 1971, the Twenty-Sixth Amendment prohibited the federal government and states from denying or abridging the voting rights of citizens eighteen or older on account of age. The amendment concerned voting rights, not a requirement that every eligible person cast a ballot.',
    items=[
        ('contextualization', 2, 'Why did the military-service argument gain force during the Vietnam era?', 2, [
            ('All American military personnel were too young to qualify for citizenship.', 'The debate concerned citizens’ voting age, not a universal lack of citizenship among service members.'),
            ('The Constitution required military service before anyone could vote.', 'The constitutional voting system did not impose military service as a universal voting prerequisite.'),
            ('The draft highlighted a tension between imposing military obligations on young adults and withholding the vote from many of them.', 'Advocates connected responsibilities of citizenship with the ability to influence political decisions.'),
            ('The end of youth political activity made voting-age restrictions newly controversial.', 'The campaign developed amid active youth political involvement, not its disappearance.'),
        ]),
        ('continuity-and-change', 3, 'Which interpretation best accounts for both the argument’s World War II roots and the amendment’s 1971 ratification?', 1, [
            ('The campaign began only after ratification and therefore could not have contributed to the change.', 'The earlier arguments and Vietnam-era advocacy preceded the amendment.'),
            ('A longstanding demand gained renewed urgency in a later wartime setting and contributed to a new constitutional protection.', 'The interpretation combines continuity in the argument with change in constitutional voting rights.'),
            ('The use of an older argument shows that no political change occurred in 1971.', 'Continuity in advocacy is compatible with a later change in law.'),
            ('Ratification demonstrates that young people had never participated politically before 1971.', 'Young people could organize, protest, and campaign even when age rules limited their voting eligibility.'),
        ]),
        ('claims-evidence', 4, 'Which evidence is most necessary to assess whether the amendment led to high electoral participation among newly eligible voters?', 0, [
            ('Age-specific registration and turnout data after ratification, with attention to eligible population definitions.', 'These measures address actual participation rather than assuming it from a legal entitlement.'),
            ('The amendment’s date treated as a direct measurement of voter turnout.', 'The date establishes legal chronology, not the proportion of eligible people who voted.'),
            ('One student protest photograph treated as a representative national turnout survey.', 'A protest image cannot establish national electoral participation among an age group.'),
            ('The number of states that ratified the amendment treated as the number of young people voting.', 'State ratification and individual voter participation are different measures.'),
        ]),
    ],
)
