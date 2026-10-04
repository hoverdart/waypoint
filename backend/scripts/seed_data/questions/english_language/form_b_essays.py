"""Second essay set: competing policy evidence, technology rhetoric, and tradition."""
from .form_a_essays import make_essay
from .form_b_reading import CLOCK_PASSAGE

SOURCES = """Source A — Principal’s proposed policy (fictional)
For one semester, students would store personal phones in numbered classroom slots during lessons. Devices would be available between classes and at lunch. Teachers could authorize their use for an activity. The proposed purpose is to reduce interruptions without requiring staff to search bags or confiscate devices for an entire day. A student who uses a phone for an approved health or accessibility need would keep it. The proposal allocates funds for storage but not replacement devices if a phone is damaged. The principal requests feedback on responsibility for secure storage and on how substitute teachers would identify authorized exceptions without disclosing private information.

Source B — Student council statement (fictional)
We agree that a class is harder to follow when phones repeatedly interrupt it. We disagree that all phone use has the same purpose. Some students check a translation tool, coordinate transport for a younger sibling, or use a device connected to a health monitor. A policy that grants exceptions only after students publicly explain themselves will make privacy the price of access. We propose a confidential approval process, school-provided alternatives for required class activities, and a way to contact home for urgent needs. Rules work better when students can understand and use the exceptions without having to negotiate them in front of an audience.

Source C — Classroom pilot summary (fictional data)
Eight volunteer teachers tested phone storage for four weeks. The table compares those classes with their own preceding four weeks. Teachers also introduced a common opening activity during the pilot. The classes were not randomly selected, and there was no separate comparison group.

Measure                                      Before      During
Mean teacher-recorded interruptions per week     12           5
Mean unit-assessment percentage score            71          72
Reported storage disputes across all classes      0          14
Teachers favoring continuation                              6/8

The summary does not report variation among classes, the seriousness of disputes, or longer-term outcomes. A change in an average cannot identify which part of the pilot caused it.

Source D — Teacher’s reflection (fictional)
The quietest minutes of the pilot were not always the most productive. My students sometimes sat silently because they did not understand the assignment. At other times, collecting phones removed the repeated negotiation that had consumed the start of a lesson, and we had more time for discussion. I support a consistent routine, but I would resist describing silence as learning. We need to ask whether students are attending to worthwhile work, not merely whether their hands are empty. The opening activity may have helped as much as storage because it made the first task clear to everyone.

Source E — Draft school poster (fictional visual stimulus)

          ┌─────────────────────────────────────┐
          │          READY TO LEARN?            │
          │  Phone in the slot → Eyes forward   │
          │       → Better learning             │
          │                                     │
          │      NO PHONE. NO DISTRACTIONS.     │
          └─────────────────────────────────────┘

Design description: three large arrows present storage, attention, and learning as a single linear sequence. A crossed-out phone is the only icon. There is no information about authorized exceptions, urgent contact, or device security. The poster has been proposed but not distributed.

Source F — Parent association letter (fictional)
Some parents want immediate access to a child during the school day, while others report that constant messages make it difficult for children to focus. Our association does not represent a single view. We could support classroom storage if the school publishes a reliable urgent-contact procedure and makes clear who is responsible for devices. The main office currently answers calls during lessons, but the proposal does not explain how quickly messages are relayed. Reassurance should be a procedure people can use, not simply a request to trust that everything will be fine. We also recommend reviewing the policy after a semester with students, staff, and families."""

SYNTHESIS_PROMPT = """Synthesis essay — Personal phones during lessons
Suggested writing time: 40 minutes after reviewing the sources. All sources, organizations, and data below are fictional materials written for this practice task.

A secondary school is considering classroom phone storage during lessons. Write an essay arguing your position on the conditions that should guide the school’s decision. Synthesize evidence from at least three sources, identify the sources by letter, and explain how they support your reasoning. Consider relevant tradeoffs or limits; your essay should develop an argument rather than summarize the sources in sequence.

""" + SOURCES

SYNTHESIS_MODEL = """One defensible model approach:

The school should try a limited classroom-storage policy only if it protects confidential access needs, defines responsibility for devices, and evaluates learning rather than treating quiet as success. Reducing interruptions is a legitimate goal, but a policy that reaches that goal by creating new barriers or confusing compliance with education would need revision.

The proposed classroom-only routine is a reasonable starting point because it narrows the restriction to the period when shared attention matters most. Source A leaves devices available between lessons and allows authorized educational use. Source C offers suggestive support: recorded interruptions fell during the pilot. However, those classes also adopted an opening activity, lacked a comparison group, and were taught by volunteers. The decline therefore cannot be assigned entirely to phone storage. The school can use the finding to justify a trial without presenting it as a guaranteed effect for every classroom.

Confidential exceptions are a necessary condition of that trial. Source B identifies uses that a general distraction rule does not adequately describe, including translation and health monitoring. Requiring a student to explain a health need aloud would make enforcement itself exclusionary. Source A’s concern about substitutes shows that a private approval system must work in ordinary classroom conditions, not just exist on paper. School-provided alternatives for required activities and a discreet method of verifying exceptions would make the policy more consistent with its educational purpose.

Responsibility also cannot disappear when a device enters a numbered slot. The fourteen disputes in Source C do not prove that storage is unworkable, since the summary gives no account of their seriousness. They do show why the school needs a clear process for damaged or misplaced property. Source F makes a parallel point about urgent family contact: a usable procedure is more persuasive than a vague assurance. Families should know whom to contact and how messages reach students.

Finally, the evaluation should resist the shortcut displayed in Source E. Its arrows turn storage into attention and attention into better learning without showing the conditions needed for either step. Source D explains why that sequence can fail: silence may indicate confusion, while a well-designed opening task may improve engagement. The school should measure participation, students’ access to necessary tools, staff workload, disputes, and learning over time. A review after one semester would allow the routine to improve rather than forcing supporters to defend every consequence as proof of success.

Other positions may be defensible. The important work is explaining the connections and limitations across sources, not adopting this recommendation."""

RHETORICAL_PROMPT = """Rhetorical analysis essay — Measurement and judgment
Suggested time: 40 minutes.

In this original fictional letter, set in an early twentieth-century industrial town, an employee replies to a relative’s question about newly installed electric clocks. Analyze how the writer’s rhetorical choices develop the argument about measurement and fairness. Use specific evidence and explain how the choices work within the letter’s situation. This is an invented practice text, not a quotation from a historical archive.

""" + CLOCK_PASSAGE

RHETORICAL_MODEL = """One defensible model approach:

The letter argues that precise records can improve fairness without making human judgment unnecessary. The employee develops that position through a conversational distinction, balanced concessions, and concrete examples that expose the choices hidden beneath the apparent neutrality of a table. These choices make the argument a practical reply to a relative rather than a blanket attack on machinery.

The opening answers the relative’s question by separating “easier” from “more exact.” The short distinction unsettles the assumption that a technical improvement must simplify everyone’s experience. Describing the old foreman’s attention to weather and workers coming over the hill then makes discretion visible. The writer does not initially declare that discretion good or bad; the important observation is that everyone could see where judgment entered. That framing prepares readers to question a new system in which judgment might remain while becoming harder to identify.

Paragraph 2 gives the new clocks a serious defense. An independent record can protect a punctual worker and prevent favoritism. By presenting benefits from the workers’ perspective, the narrator avoids an easy opposition between humane employees and inhuman machines. The concession strengthens the later distinction: the objection is not to evidence but to allowing evidence of one fact to settle every other question.

The tram and locked school door supply circumstances that a timestamp cannot explain. These examples connect an abstract limitation to experiences a relative could readily understand. The admission that some explanations may be false prevents the appeal from becoming a demand to accept every excuse. The paired statements about making arrival visible without making circumstances disappear then compress the argument into a distinction the reader can carry into the manager’s table.

That table becomes the central test of the manager’s claim to have facts without opinion. The writer accepts its correct totals but asks who chose the quarter-hour penalty for a one-minute delay. “No wire in the clock” chose it. This brief sentence strips a human rule of borrowed mechanical authority. The argument has not vanished; it has moved into the use of the figures. The writer thereby gives the relative a way to locate judgment even when it is presented as mere calculation.

The conclusion keeps the clocks and keeps a hearing process. Its return to the original question avoids nostalgia for the old system. The final language of spending judgment links the practical world of time and pay to the responsibility that remains after a new instrument arrives. Fairness requires both a reliable record and an account of what that record can reasonably mean.

This model demonstrates one supported line of analysis; other choices and interpretations can be developed with evidence."""

ARGUMENT_PROMPT = """Argument essay — Traditions and their purposes
Suggested time: 40 minutes.

Communities often preserve traditions because repetition connects people across time. Yet repeating a practice without understanding its purpose may also limit what a community can become. Write an essay arguing your position on the value of adapting traditions. Support your position with specific evidence from your reading, knowledge, observations, or experience, and explain the reasoning connecting that evidence to your claim. Consider relevant qualifications. Do not invent quotations or present hypothetical examples as historical facts."""

ARGUMENT_MODEL = """One defensible model approach, using expressly hypothetical examples:

Adapting a tradition can preserve its value more effectively than repeating every detail unchanged. A tradition connects people through a shared practice, but the connection depends on what people can actually experience within it. Adaptation is valuable when it keeps that purpose accessible while taking the practice’s history seriously.

Consider a hypothetical neighborhood that holds a meal each year to welcome new residents. For many years, the meal takes place in a room reached only by stairs. When a new resident cannot enter, moving the event to an accessible room changes a familiar detail but strengthens the tradition’s purpose. Insisting on the old room would preserve the setting while weakening the welcome. In this case, the most faithful continuation is a change in the means rather than an abandonment of the event.

A school ceremony offers a different example. Imagine that students traditionally read a list of local volunteers’ contributions aloud. As the list grows, organizers consider replacing it with a short video. The change could allow more people to be recognized and preserve the accounts for later viewing. It could also lose the sense of a community publicly giving its attention to each person. The proposal should therefore be judged by more than convenience. Students might combine a shorter live reading with an accessible recording, preserving collective recognition while adapting the form.

These examples show why adaptation should involve people who understand what a practice means. A newcomer may identify a barrier insiders have stopped noticing, while a longtime participant may explain a detail that seems arbitrary but carries an important memory. Neither perspective is sufficient by itself. Conversation can distinguish a necessary feature from a habit whose original purpose no longer applies.

There are limits to this argument. Some traditions are valuable partly because participants encounter a form they did not design for themselves. Changing every demanding or unfamiliar element can remove the continuity that made participation meaningful. An adaptation should therefore be explained, not simply assumed to be better because it is newer. It should make clear what is being preserved, what is being changed, and why the change serves the community.

Traditions need not be either untouched objects or disposable customs. They can be practices for which each generation accepts responsibility. Thoughtful adaptation honors the past by asking how its purposes can remain available to people whose circumstances differ from those of earlier participants.

The examples here are hypothetical, not factual reports. Accurate literary, historical, or personal evidence can support other defensible positions."""


def essay(kind, unit, skill, prompt, model):
    question = make_essay(kind, unit, skill, prompt, model)
    question['skill_tags'] = [f'ap-skill:{skill}', f'format:{kind}', f'item:lang-b-{kind}']
    return question


QUESTIONS = [
    essay('synthesis', 7, '4.C', SYNTHESIS_PROMPT, SYNTHESIS_MODEL),
    essay('rhetorical-analysis', 4, '1.A', RHETORICAL_PROMPT, RHETORICAL_MODEL),
    essay('argument', 4, '4.B', ARGUMENT_PROMPT, ARGUMENT_MODEL),
]
