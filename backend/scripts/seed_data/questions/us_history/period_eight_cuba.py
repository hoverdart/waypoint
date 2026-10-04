"""Original crisis-decision practice, distinguishing coercion and negotiation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='America as a World Power', code='8.7', set_id='cuban-missile-crisis',
    source_url='https://history.state.gov/milestones/1961-1968/cuban-missile-crisis',
    source_kind='original instructional summary',
    stimulus='In October 1962, U.S. reconnaissance photographs revealed Soviet missile installations in Cuba. Kennedy’s advisers debated responses including air strikes and invasion. Kennedy chose a naval quarantine while diplomatic contacts continued. The resolution included Soviet removal of missiles from Cuba and a U.S. assurance against invasion. A private understanding also concerned removal of U.S. Jupiter missiles from Turkey; that element was not part of the public resolution.',
    items=[
        ('comparison', 2, 'Compared with an immediate air strike, what distinguished the quarantine as an initial response?', 1, [
            ('It abandoned pressure on Soviet deployments in favor of recognizing them as permanent.', 'The quarantine applied pressure while the United States sought missile removal.'),
            ('It applied military pressure while leaving time for further communication before attacking the installations.', 'The quarantine offered a coercive step short of an immediate strike; it still involved risks.'),
            ('It required occupying Cuba before diplomatic contact could begin.', 'The chosen response did not begin with an invasion and occupation.'),
            ('It eliminated the possibility of an armed encounter between the two sides.', 'Naval interception and military readiness could still lead to confrontation.'),
        ]),
        ('causation', 3, 'Why could fear of nuclear escalation encourage leaders to maintain diplomatic contacts during the crisis?', 2, [
            ('Nuclear weapons made every limited military action incapable of provoking a response.', 'Limited actions could trigger retaliation or escalation; nuclear weapons did not remove those risks.'),
            ('Diplomacy required leaders to agree on every ideological dispute before discussing missiles.', 'A limited settlement could address the immediate crisis without resolving ideological conflict.'),
            ('The potentially catastrophic cost of retaliation gave leaders an incentive to seek an acceptable way to end the confrontation.', 'Escalation risk increased the value of negotiation even while coercive pressure continued.'),
            ('The possibility of nuclear war made the location of missiles irrelevant to both governments.', 'Deployment locations and perceived vulnerability remained central to the dispute.'),
        ]),
        ('sourcing', 3, 'Why might a historian studying only public announcements from October 1962 produce an incomplete account of the settlement?', 0, [
            ('Public statements did not disclose the private understanding concerning missiles in Turkey.', 'Private diplomatic records can reveal elements unavailable in contemporary public announcements.'),
            ('Public statements are inherently unable to establish any government position.', 'They can establish publicly stated positions even when they omit confidential negotiations.'),
            ('The existence of a private understanding proves every public announcement was factually false.', 'Omission of a confidential element does not make every public statement false.'),
            ('A later historian must exclude diplomatic records because they were not immediately public.', 'Later access to diplomatic records can broaden the evidence available for historical interpretation.'),
        ]),
        ('argumentation', 4, 'Which interpretation best accounts for both the military pressure and the diplomatic terms described?', 3, [
            ('The crisis ended through military destruction of the installations, leaving diplomacy without a role.', 'The account describes negotiated removal rather than destruction by U.S. strikes.'),
            ('The outcome was a Soviet withdrawal with no accompanying U.S. assurances or adjustments.', 'The noninvasion assurance and private Turkey understanding complicate an unconditional-withdrawal interpretation.'),
            ('The settlement ended the Cold War by establishing a shared political system in Cuba.', 'Resolution of the missile confrontation did not end the larger ideological conflict.'),
            ('Coercive pressure and negotiated assurances combined to resolve the immediate confrontation without ending superpower rivalry.', 'This interpretation includes both instruments and limits its conclusion to what the settlement accomplished.'),
        ]),
    ],
)
