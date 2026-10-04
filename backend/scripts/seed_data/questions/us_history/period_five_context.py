"""Original questions connecting expansion to sectional and diplomatic conflict."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Contextualizing Period 5', code='5.1', set_id='texas-annexation',
    source_url='https://www.tsl.texas.gov/exhibits/annexation/index.html',
    source_kind='original instructional summary',
    stimulus='Texas declared independence from Mexico in 1836 and entered the United States in 1845 as a state permitting slavery. Annexation had generated debate over relations with Mexico and over the expansion of slaveholding power within the United States. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'Which earlier development provides the most useful context for the sectional dimension of this debate?', 1, [
            ('The establishment of a national bank to regulate federal deposits.', 'Banking disputes shaped politics, but the Missouri controversy provides a more direct precedent for slavery and state admission.'),
            ('The Missouri controversy over the balance between free and slave states.', 'The earlier controversy linked territorial growth, slavery, and representation in national institutions.'),
            ('The growth of voluntary temperance associations.', 'Temperance organized reform activity but did not directly establish the precedent for sectional disputes over admitting a slave state.'),
            ('The development of an independent American literary culture.', 'Literary developments are less directly connected to the political balance at issue in annexation.'),
        ]),
        ('causation', 3, 'Why could a debate over adding territory become a dispute over political power within the United States?', 2, [
            ('New states participated in presidential elections but had no representation in Congress.', 'New states gained congressional representation as well as a role in presidential elections.'),
            ('Annexation automatically removed existing states from the Senate.', 'Admitting Texas did not remove other states from the Union or their Senate seats.'),
            ('Admission added representation and raised questions about the future geographic reach of slavery.', 'Expansion changed the political community and could alter sectional influence.'),
            ('Territorial growth placed decisions about American slavery entirely under Mexican law.', 'Annexation expanded U.S. jurisdiction rather than transferring national slavery policy to Mexico.'),
        ]),
        ('argumentation', 4, 'Which evidence would most strongly qualify a claim that all opponents of annexation shared the same motive?', 0, [
            ('Contemporary letters distinguishing opposition based on the risk of war from opposition based on slavery’s expansion.', 'Different stated reasons would challenge a single-motive explanation while allowing that motives could overlap.'),
            ('A tally showing that several legislators voted against annexation, without their stated reasons.', 'A shared vote establishes a common position but not either uniform or differing motives.'),
            ('A map showing Texas outside the United States before 1845.', 'The map establishes territorial status, not opponents’ reasoning.'),
            ('The final date of Texas’s admission to the Union.', 'The admission date does not distinguish motives among opponents.'),
        ]),
    ],
)
