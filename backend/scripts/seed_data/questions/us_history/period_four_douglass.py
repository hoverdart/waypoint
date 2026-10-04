"""Original questions on literacy and resistance using a public-domain memoir."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='African Americans in the Early Republic', code='4.12', set_id='douglass-literacy',
    source_url='https://en.wikisource.org/wiki/Page:Narrative_of_the_Life_of_Frederick_Douglass,_an_American_Slave.djvu/57',
    source_kind='primary excerpt',
    stimulus='Frederick Douglass, Narrative of the Life of Frederick Douglass, an American Slave (1845), chapter VI. Context: Douglass recalls hearing Hugh Auld oppose teaching him to read. Douglass writes: “From that moment, I understood the pathway from slavery to freedom.”',
    items=[
        ('claims-evidence', 2, 'In this context, the “pathway” chiefly refers to', 2, [
            ('an agreement by Auld to grant freedom after a course of study.', 'Auld opposed instruction; the passage does not describe an agreement to emancipate Douglass.'),
            ('a law automatically emancipating enslaved people who could read.', 'Douglass describes a realization about knowledge and power, not a legal emancipation provision.'),
            ('the potential of literacy to challenge the dependence imposed by enslavement.', 'Auld’s opposition helped Douglass recognize learning as a means of resisting domination.'),
            ('the replacement of resistance with acceptance of an enslaver’s authority.', 'Douglass interprets the restriction as a reason to pursue knowledge, rather than accept enforced dependence.'),
        ]),
        ('causation', 3, 'Which explanation best accounts for the effect Auld’s opposition had on Douglass in this account?', 0, [
            ('An attempt to preserve control revealed to Douglass why access to knowledge mattered.', 'The prohibition unintentionally disclosed a connection between ignorance and domination.'),
            ('A promise of paid employment made Douglass willing to abandon reading.', 'The account concerns opposition to education, not a promise of wages.'),
            ('A change in legal status removed the risks associated with learning.', 'The realization occurred while Douglass remained enslaved; it did not remove those risks.'),
            ('Auld’s endorsement of schooling persuaded Douglass to follow an approved curriculum.', 'Auld prohibited instruction rather than endorsing it.'),
        ]),
        ('sourcing', 3, 'How should the memoir’s retrospective character affect a historian’s use of this passage?', 3, [
            ('It establishes that every enslaved person interpreted literacy in the same way.', 'One person’s account cannot establish a universal response across diverse circumstances.'),
            ('It makes the passage irrelevant to understanding resistance under slavery.', 'Retrospective testimony remains relevant, though its perspective and construction require analysis.'),
            ('It makes the quoted realization a verbatim diary entry written during the event.', 'A later memoir is not automatically a contemporaneous diary record.'),
            ('It provides Douglass’s later interpretation of an earlier experience, which can be compared with other evidence.', 'The memoir offers valuable testimony while reflecting recollection and the author’s purposes at publication.'),
        ]),
        ('argumentation', 4, 'Which additional evidence would best support an argument that resistance extended beyond open rebellion?', 1, [
            ('An inventory recording the market valuations assigned to enslaved workers.', 'Valuations document commodification but do not by themselves establish acts of resistance.'),
            ('Independent accounts of covert reading lessons and efforts to maintain forbidden networks of communication.', 'Such evidence documents resistance through knowledge and communication outside overt revolt.'),
            ('A plantation rule specifying obedience without evidence of how people responded.', 'A rule reveals an enslaver’s demands but cannot alone establish whether or how people resisted.'),
            ('An abolitionist newspaper’s circulation totals without information about enslaved readers.', 'Circulation alone does not establish resistance by enslaved people or their access to the newspaper.'),
        ]),
    ],
)
