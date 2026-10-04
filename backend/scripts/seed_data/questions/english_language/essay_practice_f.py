"""Original supplemental essays with fictional sources and illustrative models."""
from .form_a_essays import make_essay

SOURCES = """Source A — Arts commission proposal (fictional)
The city has funds for one public-art program in a newly renovated square. The commission is considering either a permanent sculpture or a sequence of temporary installations over three years. A permanent work could become a recognizable landmark. A rotating program could support several artists and let residents experience different uses of the space. The available capital budget is the same for both options, but the proposal has not yet compared maintenance, installation, removal, storage, or public consultation costs.

Source B — Resident's letter (fictional)
The old fountain helped people explain where to meet even after it stopped working. A lasting object can gather meanings that its designer never planned. I worry that a square whose art changes every few months may feel like a display window rather than a place with a memory. Yet I also remember how long we lived with the broken fountain because nobody knew who should pay to repair it. Permanence is not simply the decision to leave something where it stands. It is a commitment that someone must continue to keep.

Source C — Invented budget scenarios
The figures below are planning estimates in thousands of budget units for a three-year period. They are not quotations from real artists or suppliers.

Expense | Permanent work | Six temporary installations
Commissioning | 90 | 66
Installation and removal | 15 | 30
Maintenance | 12 | 9
Public programming | 3 | 15
Total | 120 | 120

The permanent-work scenario excludes costs after year three. Temporary-work estimates assume that materials can be removed as planned; storage is not included. The table describes two possible budgets, not every design. Equal totals do not imply equal benefits or equal long-term obligations.

Source D — Artist's commentary (fictional)
Temporary art is sometimes described as less serious because it does not remain. But a work made for a season can invite participation that a protected object cannot. People may help assemble it, change it, or watch it disappear. Those possibilities do not make every temporary work successful. A hurried rotation can become an event calendar that gives audiences little time to encounter anything deeply. The duration should serve the work's purpose, not merely create another opening ceremony.

Source E — Concept layout of the square (fictional visual)
+--------------------------------------------+
| Library doors                 Bus shelter  |
|       \\                          /         |
|        \\    ART LOCATION        /          |
|         \\       [X]            /           |
|          Main pedestrian crossing          |
| Seating                           Shops    |
+--------------------------------------------+
The sketch is not to scale. The proposed art location overlaps a commonly used crossing route. It does not indicate clear passage widths or how crowds at an event would move. Either kind of art would require a more detailed access plan before installation.

Source F — Community forum summary (fictional)
Participants asked for several different things: a meeting landmark, opportunities for local artists, a place for children to explore, and an uncluttered route to the bus stop. Some wanted a work connected to the neighborhood's history; others wanted the square to make room for new residents' stories. The forum was attended by 42 volunteers and did not establish a single community preference. Several participants suggested publishing selection criteria and explaining how the final choice addresses competing uses of the square."""

SYNTHESIS_PROMPT = """Synthesis essay — How long should public art last?
Suggested writing time: 40 minutes after reading the sources. All six sources, diagrams, and figures are fictional practice materials.

A city is choosing between a permanent public artwork and a program of temporary installations in a square. Develop your position on the factors that should guide its decision. Use and identify evidence from at least three sources, explain its relationship to your reasoning, and address relevant complexities or limitations.

""" + SOURCES

SYNTHESIS_MODEL = """One defensible model approach:

The city should choose a duration only after deciding what the artwork is meant to contribute and how the square must function. Access, continuing responsibility, and opportunities for meaningful public engagement should guide the choice. Given the unresolved uses described in the sources, a carefully evaluated temporary program could be a useful first step, but rotation should not become a substitute for a clear artistic and public purpose.

Access is a condition for either option. Source E places the proposed work across a common pedestrian route without showing how people would pass it. Source F includes residents who value an uncluttered path to the bus stop alongside those seeking a landmark or an exploratory space. These interests are not evidence that art and everyday use are inherently incompatible. They show why the city must develop the layout with affected users before deciding that an attractive object or event has improved the square.

The city should also resist equating a permanent work with a single completed purchase. Source B values the memory accumulated around the old fountain but recalls uncertainty about repairing it. Source C reinforces that concern: its permanent-work estimate stops after three years. The equal totals therefore cannot establish equal lifetime costs. Temporary work has its own omissions, including storage and possible removal difficulties. A decision should identify who maintains, removes, or repairs a work and where the resources will come from, whichever duration is selected.

A temporary program could help the city explore different forms of participation. Source D explains how a seasonal work might invite people to assemble or change it, while Source A notes the opportunity to support several artists. These possibilities are particularly relevant when Source F records competing hopes rather than a settled preference. The program could commission a small number of works with explicit purposes and gather observations about how people actually encounter them.

That argument needs a qualification. As Source D warns, frequent openings can become an event calendar that leaves little room for sustained attention. The city should not measure success simply by the number of installations or launch-day visitors. It should allow enough time for each work, explain its selection criteria, and consider experiences beyond the forum's self-selected participants. A later decision about a permanent work could then draw on what the program reveals without treating the temporary artists merely as placeholders.

A lasting landmark may ultimately be the better choice, especially if a design gathers broad meaning and a credible maintenance commitment. The present sources do not identify that design. Beginning with purpose, access, and responsibility would let the city choose permanence or change as a means of serving the square rather than as a slogan about what public art must be.

This is an illustrative position; other conclusions can be defended through careful synthesis."""

ADDRESS = """[1] When the committee invited me to speak about our laboratory's most successful project, I asked which one it meant. The chair named the experiment whose result appears on the poster outside this room. I had been thinking of the experiment that taught us the poster needed a different question. It produced no dramatic image. For three weeks it produced almost nothing at all.

[2] We were testing a new arrangement of sensors in a tank. Our first display showed a pattern so regular that we began discussing how to present it before we had finished checking the equipment. A younger colleague asked why the same pattern appeared when the tank was still. The question was unwelcome in the ordinary, embarrassing sense: it arrived just when we were enjoying ourselves. We checked. A setting in the display software had supplied the apparent regularity.

[3] I could tell this story as a warning against enthusiasm. That would be a comfortable lesson for anyone who has learned to look serious by expecting little. Enthusiasm helped us build the apparatus in the first place. The problem was not that we wanted a result. It was that wanting one had begun to determine which questions felt relevant. Our colleague's interruption returned a neglected question to the center of the work.

[4] The following weeks were slower. We changed the procedure, recorded checks that seemed repetitive, and argued about what a blank display could tell us. Some days the answer was only that the apparatus had not yet earned our confidence. That is a modest answer, but it changes what one may honestly claim. An instrument can produce a number before a team has produced a reason to trust it.

[5] Eventually we obtained a pattern that survived the checks we could devise. It is the one on the poster. I am proud of it, and I expect someone to devise a check we have not considered. That expectation does not cancel pride. It tells us what kind of pride is appropriate: pride in work made available for other people to examine, not pride in having placed a conclusion beyond their reach.

[6] To the students joining laboratories this year, I offer a request smaller than “be fearless.” Most of us will not manage that every afternoon. Ask one clear question when something seems too convenient, including when the convenience is your own. To those of us who supervise them, I offer the harder request: make that question useful to ask. A laboratory's openness cannot be measured by the number of times its director says that questions are welcome. It must be heard in what happens after an inconvenient one."""

RHETORICAL_PROMPT = """Rhetorical analysis essay — Making questions welcome
Suggested time: 40 minutes.

In this original fictional address, a laboratory director speaks to students and supervisors at a research institute's annual meeting. Analyze how the speaker develops an argument about inquiry and the responsibilities of scientific leadership. Use specific evidence and explain the relationship between rhetorical choices, audience, and purpose. The experiment is invented, not a report of real research.

""" + ADDRESS

RHETORICAL_MODEL = """One defensible model approach:

The director uses a story of premature confidence to argue that openness in research depends on how a group responds to inconvenient questions. By revising the meaning of success, admitting the attraction of an apparent result, and addressing students and supervisors differently, the speaker makes intellectual humility a practical responsibility rather than a ceremonial virtue.

The opening disagreement about the laboratory's most successful project challenges the occasion's likely emphasis on achievement. The chair points to the public poster; the director points to an unremarkable period that changed the question. This contrast does not deny the value of the displayed result. It asks the audience to include less visible work in its account of how that result became worth presenting. The absence of a dramatic image is therefore part of the argument rather than a failure to provide an entertaining success story.

The account of the regular display makes the group's error recognizable. The researchers begin planning presentation before finishing checks, and the speaker admits that the younger colleague's question interrupted their enjoyment. This admission gives the story more force than a general warning against bias. The director includes personal embarrassment and shared desire in the explanation, avoiding a division between foolish colleagues and an unusually wise narrator. The audience can see why a relevant question might feel unwelcome even when no one openly opposes inquiry.

Paragraph 3 then rejects an overly simple lesson against enthusiasm. The observation about appearing serious by expecting little exposes the limitations of automatic skepticism. Enthusiasm built the apparatus; the problem arose when desire narrowed the questions treated as relevant. That distinction preserves ambition while locating the needed correction in the team's habits of attention.

The slower work and blank displays give the correction material form. Repetitive checks can establish that an apparatus has not yet earned trust, even when that finding is modest. The contrast between producing a number and producing a reason to trust it separates output from justified knowledge. When the director finally expresses pride in the surviving pattern, the expected future check qualifies that pride without making it insincere. Examination by others becomes part of success, not an insult to it.

The conclusion translates the narrative into unequal responsibilities. Students are asked for one clear question rather than a heroic state of fearlessness. Supervisors are asked to make that question useful to ask, a harder obligation because they shape its consequences. The final contrast between announcing openness and responding to an actual interruption tests institutional language against behavior. It returns the audience to the younger colleague's question and asks whether their own laboratories would allow such a moment to improve the work.

This model shows one line of analysis; other supported interpretations can explain different relationships among the choices."""

ARGUMENT_PROMPT = """Argument essay — Goals beyond easy reach
Suggested time: 40 minutes.

An ambitious goal may inspire work that a cautious goal would never prompt, but it may also distort decisions about success. Argue your position on the value of setting goals that may not be fully achievable. Support your position with specific evidence and explain your reasoning. Consider relevant qualifications, and distinguish hypothetical examples from factual claims."""

ARGUMENT_MODEL = """One defensible model approach using hypothetical examples:

Goals beyond easy reach can be valuable when they organize effort without making anything short of total achievement meaningless. Their value depends on how people use them. An ambitious goal should help identify worthwhile next actions and honest measures of progress; it should not authorize pretending that limits or competing responsibilities have disappeared.

Imagine a community reading program that hopes every child in a neighborhood will have regular access to books. The organizers may not be able to accomplish that goal in a single year. Yet its breadth can reveal who is missing from a plan that initially serves only children able to visit the library after school. The program might develop delivery routes or partnerships because the larger goal directs attention beyond an easily counted group. In this case, ambition improves the questions asked even before it produces a complete result.

A hypothetical athlete provides a different example. A runner may aim for a demanding time that current performance does not yet make likely. The target can encourage consistent training and careful feedback. But if the runner treats every slower race as worthless, the same goal can conceal useful evidence of improvement or encourage ignoring an injury. The distinction is between a challenging direction and a rule that invalidates every partial achievement. Progress measures and willingness to revise a training plan make ambition more informative.

The examples also show why a goal must remain connected to its purpose. A reading program could distribute many books while failing to help children find material they can use. A runner could achieve a number by sacrificing the health that makes continued participation possible. A demanding target is not automatically a good target; its measures must represent the value the activity is meant to produce. Otherwise, enthusiasm can make a narrow result seem more important than the reason for pursuing it.

Some commitments require particular caution. When other people depend on a promised delivery date or essential service, calling the target aspirational does not excuse failing to explain uncertainty. Ambition can coexist with realistic commitments: an organization may hold a long-term aim while making specific near-term promises it can support. That distinction protects trust and makes progress review possible.

An unreachable horizon is therefore useful only if it improves the journey's actual decisions. People should be able to say both that a goal remains unfinished and that a particular advance matters. With honest measures, attention to consequences, and room for revision, ambitious goals can draw effort beyond routine expectations. Without those conditions, they risk becoming a language for disappointment or self-deception rather than a guide to worthwhile work.

The scenarios are hypothetical. Accurate evidence from experience, history, or literature can support other defensible arguments."""


def essay(kind, unit, skill, prompt, model):
    question = make_essay(kind, unit, skill, prompt, model)
    question['skill_tags'] = [f'ap-skill:{skill}', f'format:{kind}', f'item:lang-f-{kind}']
    return question


QUESTIONS = [
    essay('synthesis', 6, '4.A', SYNTHESIS_PROMPT, SYNTHESIS_MODEL),
    essay('rhetorical-analysis', 7, '3.C', RHETORICAL_PROMPT, RHETORICAL_MODEL),
    essay('argument', 9, '4.C', ARGUMENT_PROMPT, ARGUMENT_MODEL),
]
