"""One original full essay set with sources, model approaches, and rubric reflection."""
from .essay_rubrics import essay_rubric
from .form_a_reading import TRANSLATION_PASSAGE
from scripts.seed_data.units_topics.english_language import SKILLS

SYNTHESIS_SOURCES = """Source A — Planning memorandum (fictional)
A planning committee proposes closing two blocks of Alder Street to private cars each Saturday for a six-month pilot. Delivery vehicles would have access before 10 a.m.; emergency access would remain open. Movable planters would separate seating from a continuous clear route through the street. The committee expects more room for walking and public events but has not yet estimated how many drivers would use neighboring streets. Its proposed evaluation counts visitors and retail sales. It does not currently include travel times for bus passengers or people using accessible transport. The committee recommends that the pilot proceed only if the city can remove the barriers quickly when needed.

Source B — Shop owners’ letter (fictional)
Our businesses do not all serve the same customers. A cafe may benefit from people lingering outside; an appliance shop depends on customers collecting large items. Several of us support a trial, but calling every visitor a potential customer obscures these differences. We ask the city to designate loading spaces near each end of the closed blocks and to compare results by business type. A busy street is not necessarily a profitable street for every shop. If the pilot succeeds on average while forcing essential businesses to relocate, its average will conceal a cost the neighborhood still has to bear.

Source C — Pilot observations from another fictional district
The table describes four Saturdays before and four during a similar closure. Weather and special events were not controlled; the figures show association, not proof of causation.

Measure                              Before       During
Mean pedestrians counted per day      1,200        1,860
Median shop sales index                 100          109
Mean bus trip through area, minutes       14           19
Reported loading conflicts per day         3            8

The shop-sales index combines participating shops and does not describe every business. The observations do not include long-term rent changes, customer satisfaction, or accessible-transport users’ experiences.

Source D — Accessibility adviser’s testimony (fictional)
“Car-free” can describe a pleasant afternoon for one resident and a lost route to a necessary service for another. Some people cannot travel the final two blocks from a distant drop-off point. Others benefit greatly when parked cars no longer interrupt a clear walking route. These experiences are not contradictory. They show why access should be designed with the people affected, rather than inferred from a slogan. The pilot should preserve nearby accessible drop-off points, provide seating at regular intervals, and publish a clear map in several formats. Consulting residents before placing barriers is less costly than discovering afterward that the layout excludes them.

Source E — Parks volunteer’s reflection (fictional)
During last year’s one-day street festival, I watched children draw on the pavement while older neighbors moved chairs into the shade. People who usually hurried past one another stayed to talk. We should not pretend that sales receipts capture the whole value of such a place. At the same time, a festival staffed by forty volunteers is not evidence that an ordinary Saturday will organize itself. Someone collected rubbish, kept a path clear, and answered questions about the closed road. If the city wants the social benefits, it should budget for the unglamorous work that makes them possible.

Source F — Concept diagram for the proposed closure (fictional)

                         NORTH
                  Adjacent residential street
              ─────────────────────────────────
                ↑ possible diverted traffic ↑
Bus stop → [West entry] ║ two closed blocks ║ [East entry] ← Clinic
                        ║ seating / events  ║
                        ║ clear center path ║
              ─────────────────────────────────
                    Southern delivery route

The diagram is conceptual, not to scale. The current proposal labels the center path and southern delivery route but shows no designated accessible drop-off point at either entry. The clinic sits beyond the east entry. A successful plan would need to resolve this omission before installation."""

SYNTHESIS_PROMPT = """Synthesis essay — Street access and public space
Suggested writing time: 40 minutes, after reading the sources. All six sources below are original fictional practice materials; do not treat the data as real-world findings.

A city is considering a six-month pilot that would close two downtown blocks to private cars on Saturdays. Write an essay that develops your position on the factors the city should prioritize when deciding whether and how to implement the pilot. Use evidence from at least three sources. Identify sources by letter, explain how the evidence supports your reasoning, and address relevant limits or competing concerns. More than one defensible position is possible.

""" + SYNTHESIS_SOURCES

SYNTHESIS_MODEL = """One defensible model approach:

The city should test the street closure, but access and accountable evaluation must be conditions of the trial rather than problems left until afterward. A pilot can reveal whether a street serves the public better without routine car traffic. It cannot answer that question if the city counts only people who can already reach it comfortably or businesses that happen to benefit.

Access comes first because a space is not meaningfully public when reaching it excludes some residents. Source D complicates the assumption that a car-free street is automatically either accessible or inaccessible: removing parked cars can help some users while a distant drop-off prevents others from entering. The missing drop-off point in Source F makes this concern concrete. The city should consult affected residents and mark nearby accessible arrival points before installing barriers. This condition does not reject pedestrian space; it makes the project more consistent with its public purpose.

The evaluation should also distinguish benefits from displaced burdens. Source C reports more pedestrians and a higher median sales index during another district’s closure, but bus trips and loading conflicts increased too. Because weather and events were uncontrolled, the table cannot establish that closure alone caused any change. It can, however, identify outcomes that Alder Street’s pilot should measure. The committee in Source A proposes counting visitors and sales while omitting bus journeys and accessible transport. Adding those measures would prevent an apparently successful average from hiding costs shifted to people outside the closed blocks.

Businesses need a similarly careful comparison. Source B explains why a cafe and an appliance shop may respond differently to the same crowd. Loading spaces and results separated by business type would answer that objection more directly than simply promising more visitors. This does not mean that every shop must gain every Saturday, but the city should know who bears recurring losses and whether practical changes can reduce them.

Finally, the city should protect benefits that receipts cannot measure. The encounters in Source E suggest how shared space can create social value, yet the writer also identifies staffing and maintenance that made the festival work. A regular program requires a realistic operating budget. By combining access safeguards, varied measures, and resources for coordination, the city can make the pilot a genuine experiment in public space rather than a temporary celebration whose costs appear only after the photographs are taken.

This is one possible argument, not the only acceptable position. Evaluate your reasoning and source use rather than matching this wording."""

RHETORICAL_PROMPT = """Rhetorical analysis essay — Translation and agency
Suggested time: 40 minutes.

The following original practice passage is a fictional community translator’s reflection for a general audience. Read it carefully. Write an essay analyzing how the writer’s rhetorical choices develop the message about responsible translation. Support your interpretation with specific evidence and explain the relationship between the choices and the writer’s purpose. Naming devices without explaining their effects is insufficient.

""" + TRANSLATION_PASSAGE

RHETORICAL_MODEL = """One defensible model approach:

The narrator presents responsible translation as both accurate language work and protection of a speaker’s agency. By exposing the limits of youthful confidence, revising an attractive metaphor, and admitting a later mistake, the writer invites readers to replace admiration for fluency alone with a more demanding respect for listening.

The opening initially seems to establish authority through academic success. The narrator knows every word in the housing letter and recognizes its official tone. The grandmother’s question about anger interrupts that confidence because vocabulary cannot resolve everything about an encounter. Her instruction to give an answer rather than an apology then transfers interpretive authority to the person presumed to need help. Readers see that the narrator’s extra politeness is not neutral: it changes the grandmother’s position. The brief dialogue makes agency visible through a specific correction rather than an abstract lecture.

The bridge metaphor extends this lesson to the narrator’s professional role. Calling translators bridges sounds complimentary, so acknowledging its generosity prevents the writer from simply dismissing volunteers’ good intentions. The objection that a bridge must “hold still,” however, exposes the image’s limits. A sequence of active verbs—asking, checking, telling—shows translation as inquiry and negotiation. The later package image further challenges the idea that a message can always be transported intact. Together, the comparisons make a technical service recognizable to nonspecialists while changing what that service appears to require.

The neighbor’s unfinished objection provides a self-critical turn. The narrator does not claim that one childhood lesson permanently solved the problem. Instead, fluency again becomes a source of error when the translator supplies meaning too early. Calling a pause “room that belongs to the speaker” converts an apparent absence into something deserving protection. The metaphor gives readers a practical ethical standard: silence need not be occupied by the person who can speak fastest.

The conclusion preserves the tension between accuracy and agency rather than choosing one at the expense of the other. References to dates and warnings acknowledge material consequences of inaccurate wording. The final distinction between making the grandmother sound like someone else and allowing someone else to hear her then returns to the opening. That return makes the essay’s message feel earned through experience: precision includes not just the words conveyed but the speaker whose intention remains audible.

Other interpretations can earn credit when supported by the passage. The goal is a coherent explanation of effects, not reproducing this inventory of choices."""

ARGUMENT_PROMPT = """Argument essay — The value of revising a decision
Suggested time: 40 minutes.

In public life, changing a decision is sometimes treated as evidence of weakness. In other circumstances, refusing to reconsider is treated as evidence of poor judgment. Write an essay that argues your position on the value of being willing to revise a decision. Use specific evidence from your reading, observations, knowledge, or experience. Explain how the evidence supports your reasoning and consider relevant limits. You do not need to agree with either characterization in the prompt, and you should not invent factual claims or quotations."""

ARGUMENT_MODEL = """One defensible model approach, using clearly identified hypothetical examples:

Willingness to revise a decision is valuable when it reflects attention to evidence and responsibility for consequences. It becomes less valuable when revision merely follows the latest pressure. The important distinction is not between changing and staying firm, but between having a reason for a decision and having only an attachment to it.

Consider a hypothetical school club that chooses an evening meeting time because most members initially report being free. Once meetings begin, several students repeatedly miss them because their bus leaves before the meeting ends. Changing the time would not show that the organizers have abandoned the club’s purpose. It would show that they understand the purpose more accurately: a convenient time on a survey is not necessarily an accessible time in practice. The observation provides new information about a consequence that the first decision failed to anticipate.

Revision can also make accountability more credible. Imagine an editor who publishes a school newspaper article using an incorrect figure, discovers the error, and then issues a clearly explained correction. Keeping the figure unchanged would protect the appearance of consistency while sacrificing accuracy. A correction acknowledges that readers deserve reliable information more than the editor deserves an unbroken record of being right. Explaining what changed and why is essential; silently replacing a figure would not provide the same accountability.

These examples do not mean every objection should reverse a decision. A club that changes its schedule after each individual complaint may become impossible for anyone to plan around. An editor who removes accurate reporting merely because its subject dislikes it would be yielding pressure rather than improving accuracy. Good revision therefore needs standards: evidence relevant to the original goal, attention to the people affected, and an explanation of why the proposed change is better than available alternatives.

There are also costs to reopening decisions. People may already have arranged transport or relied on a published plan. A responsible organizer can acknowledge those costs and set a regular review date rather than changing course unpredictably. That qualification strengthens the case for reconsideration because it separates thoughtful adjustment from instability. Being willing to revise is valuable precisely when a person remains committed enough to a purpose to correct the means of pursuing it.

These hypothetical examples illustrate one method. Specific, accurate historical, literary, or personal evidence could support a different defensible argument. This model is not a requirement to use hypothetical evidence."""


def make_essay(kind, unit, skill, prompt, model):
    return {'unit_name': f'Unit {unit}', 'topic_name': f'{skill}: {SKILLS[skill]}',
        'type': 'frq', 'difficulty': 4, 'prompt': prompt, 'correct_answer': model,
        'source': 'generated', 'validation_status': 'approved',
        'skill_tags': [f'ap-skill:{skill}', f'format:{kind}', f'item:lang-a-{kind}'],
        'misconception_tags': [], 'rubric_json': essay_rubric(kind), 'options': [],
        'explanations': [{'option_label': None, 'explanation':
            'Several positions and interpretations can be defensible. Use the rubric to assess the quality of your claim, evidence, and explanation. A high self-assessment is not an official score or an automatic mastery update.',
            'misconception_tag': None}]}


QUESTIONS = [
    make_essay('synthesis', 9, '4.C', SYNTHESIS_PROMPT, SYNTHESIS_MODEL),
    make_essay('rhetorical-analysis', 7, '1.A', RHETORICAL_PROMPT, RHETORICAL_MODEL),
    make_essay('argument', 6, '4.B', ARGUMENT_PROMPT, ARGUMENT_MODEL),
]
