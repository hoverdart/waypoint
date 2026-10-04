"""Original questions using Emerson's public-domain 1837 address."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='The Development of an American Culture', code='4.9', set_id='american-scholar',
    source_url='https://depts.washington.edu/lsearlec/TEXTS/EMERSON/AMSCHOL.HTM', source_kind='primary excerpt',
    stimulus='Ralph Waldo Emerson, “The American Scholar,” address to the Phi Beta Kappa Society at Cambridge, August 31, 1837: “Our day of dependence, our long apprenticeship to the learning of other lands, draws to a close.”',
    items=[
        ('claims-evidence', 2, 'Emerson’s metaphor of an ending apprenticeship chiefly advocates', 2, [
            ('preserving European literary standards as the final measure of American achievement.', 'An ending apprenticeship suggests moving beyond dependence on those standards.'),
            ('replacing literary study with technical training alone.', 'The appeal seeks intellectual creativity, not the abandonment of intellectual life for technical training.'),
            ('developing an intellectual life less dependent on inherited foreign models.', 'The metaphor presents American thinkers as ready to create rather than remain pupils of other lands.'),
            ('placing scholarship under the direction of a national political party.', 'The excerpt does not connect intellectual independence to party control.'),
        ]),
        ('sourcing', 3, 'How does the scholarly audience help explain Emerson’s emphasis?', 0, [
            ('He addressed people positioned to shape literary and intellectual practices.', 'An address to a learned society could challenge the habits of people involved in intellectual culture.'),
            ('He was negotiating tariff rates with foreign commercial representatives.', 'The audience and subject concern scholarship rather than an international trade negotiation.'),
            ('He was reporting the results of a survey of popular reading habits.', 'The address is an exhortation rather than a statistical report.'),
            ('He was issuing binding curriculum rules for all state schools.', 'A speech to a learned society did not carry legal authority over every school.'),
        ]),
        ('contextualization', 3, 'Which contemporary tendency is most consistent with this appeal?', 3, [
            ('Measuring cultural achievement chiefly by faithful imitation of European conventions.', 'The passage challenges dependence on foreign models rather than endorsing imitation as the chief standard.'),
            ('Locating intellectual authority exclusively in inherited institutions.', 'Emerson urges new intellectual initiative rather than exclusive deference to inherited authority.'),
            ('Treating national political independence as sufficient proof that cultural development was finished.', 'His call implies further cultural work remained despite political independence.'),
            ('Encouraging individual insight and a distinctive American literary voice.', 'The appeal fits a cultural movement toward intellectual self-reliance and original expression.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test whether writers acted on the aspiration expressed here?', 1, [
            ('Publication figures showing that more copies of Emerson’s address circulated over time.', 'Circulation measures exposure to the appeal, but does not establish whether writers changed their literary practices.'),
            ('Comparisons of literary works and authors’ correspondence showing how they adapted or challenged inherited models.', 'These sources can connect stated intentions with choices evident in literary production.'),
            ('Booksellers’ records showing a decline in the price of imported European books.', 'Prices describe access to foreign works, but do not show whether American writers imitated or challenged their models.'),
            ('Newspaper notices praising the size and prestige of the audience at Emerson’s address.', 'The audience’s prestige can establish the event’s visibility, but not its effect on subsequent literary choices.'),
        ]),
    ],
)
