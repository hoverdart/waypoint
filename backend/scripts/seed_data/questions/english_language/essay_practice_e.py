"""Additional original essay practice; not an additional multiple-choice exam form."""
from .form_a_essays import make_essay

SOURCES = """Source A — School assessment proposal (fictional)
A school proposes giving each member of a group project the same final grade. Its committee argues that a shared result encourages students to coordinate instead of dividing a task into unrelated pieces. The proposal would assess the finished work and a presentation, but it does not explain how teachers should respond when responsibilities change or a student misses several meetings. The committee suggests beginning with one short project. It has not yet collected student feedback about the proposed grading method.

Source B — Student representative's statement (fictional)
I learned more from our last group project than from many individual assignments because a teammate challenged an explanation I thought was clear. But the final poster did not show who arranged the interviews, who corrected the calculations, or who repeatedly failed to bring promised materials. A shared grade can recognize a shared result while hiding very different experiences. I do not want every helpful act turned into a competition for points. I do want a way to explain what happened before a teacher decides that the same result tells the same story about every student.

Source C — Hypothetical pilot survey
Two classes used different grading systems for one project. Students chose whether to answer the survey. The classes had different teachers and topics, so the figures cannot isolate the effect of grading.

System | Respondents | Said cooperation improved | Said effort was recognized fairly
Shared final grade | 24 | 18 | 11
Group result plus individual reflection | 26 | 19 | 20

The survey measured students' perceptions, not learning. It does not report how students who did not respond felt, or whether teachers assessed reflections consistently. No statistical significance is claimed.

Source D — Teacher's reflection (fictional)
Peer reports can reveal work that I do not see, but they are evidence to interpret rather than a machine for assigning grades. Friends may protect one another, a quiet student's contributions may be overlooked, and a disagreement about ideas may be described as poor cooperation. I ask students to identify actions and decisions, not to rank how much they like each member. Brief checkpoints let me respond while the project can still change. A final complaint submitted after grading is a much weaker opportunity to improve the group's work.

Source E — Proposed assessment diagram (fictional visual)
        FINISHED PRODUCT
               |
        ONE GROUP SCORE
          /    |    \\
     Student A B     C
     same score for each

The diagram shows no path for evidence about individual understanding, changing responsibilities, or contributions during the project. It illustrates the proposal in Source A; it is not a validated model of assessment.

Source F — Curriculum coordinator's memorandum (fictional)
The grading design should follow what the project is intended to teach. If the goal is coordinated performance, the group's result matters. If the goal includes each student's explanation of a method, teachers need evidence that each student can explain it. Asking for a short individual explanation need not mean abandoning a shared task. Yet extra records also take time to produce and review. A workable pilot should choose a few meaningful checkpoints rather than require students to document every minute of collaboration."""

SYNTHESIS_PROMPT = """Synthesis essay — Assessing group work
Suggested writing time: 40 minutes after reading the sources. All documents and figures are fictional practice materials.

A school is deciding how to grade collaborative projects. Develop your position on the factors that should guide its policy. Synthesize evidence from at least three sources, identify sources by letter, and explain how the evidence supports your reasoning. Consider relevant qualifications and competing concerns.

""" + SOURCES

SYNTHESIS_MODEL = """One defensible model approach:

The school should assess both the shared result and evidence of individual understanding, with a small number of checkpoints during the project. This approach preserves collaboration without assuming that a finished product reveals everything a teacher needs to know. The policy should begin with the learning goals and use several kinds of evidence rather than turn either a common score or peer ratings into an automatic verdict.

Source A identifies a legitimate purpose for a shared grade: students should coordinate their work instead of producing unrelated pieces. The student in Source B gives a concrete reason to preserve that interaction, describing a teammate who improved an explanation. These sources together show why simply replacing the group task with separate assignments would sacrifice something valuable. A portion of the assessment should therefore recognize the quality of the joint result and how its parts work together.

The same student also describes contributions that the poster does not reveal. Interviews, corrections, and missed commitments may lead to similar appearances at the final presentation while reflecting different participation. Source E makes this information gap visible: one product generates identical scores without any route for other evidence. A brief individual explanation could help a teacher distinguish what each student understands without requiring every act of assistance to become a competition for credit.

Source F supplies the governing principle for that choice. Evidence should match the intended learning. If students must explain a method, the teacher needs to hear each student's explanation; if coordinated performance is an objective, the group outcome deserves attention. This does not require exhaustive surveillance of the process. The coordinator's concern about time supports selecting a few relevant checkpoints rather than collecting records because records look thorough.

Peer reports can contribute to those checkpoints, but Source D warns against treating them as impartial measurements. Friendship, visibility, and disagreement can influence a report. Asking for specific actions and discussing problems while work continues would make reports more useful than an unexplained ranking at the end. That practice also gives students a chance to improve the collaboration instead of discovering its problems only through a final penalty.

The survey in Source C is consistent with investigating a mixed approach, but it does not prove that one system caused better cooperation or fairness. Different teachers, voluntary responses, and perceived rather than measured outcomes limit the comparison. The school should use such results to formulate questions for its pilot and collect evidence about learning as well as experience. A successful policy would make the grade a more informative judgment while leaving students room to learn with, and from, one another.

This is one possible synthesis, not a required policy recommendation."""

LETTER = """[1] You write that the new press has made you afraid of your own hands. Its sheets emerge so evenly that the pages you set last winter now appear to you like apologies. I have seen the press and admired it. I have also seen you mistake the work it can do for the whole of the work there is to do.

[2] When I began in the shop, my first duty was to sort the returned letters into their cases. I thought it a punishment devised for anyone too young to be trusted with printing. Only later did I understand how quickly an error in that quiet task could travel. A misplaced letter waited patiently until a compositor needed it. Then it entered a sentence wearing the authority of print. The reader did not know that the mistake had begun in a tired apprentice's haste.

[3] The new press will not tire as your hands tire. That is a reason to welcome it. A town that needs schoolbooks should not have to wait for us to become proud of every slow movement. But speed enlarges the reach of both care and carelessness. The machine can repeat a page more faithfully than you can; it cannot decide whether the page is faithful to what its writer meant.

[4] Yesterday a customer brought a notice for a meeting and asked me to make the date more prominent. The date was wrong. I might have arranged it beautifully and produced an excellent invitation to an empty room. Instead I asked a question that delayed the job by ten minutes. No visitor to the shop will admire those ten minutes. They will leave no mark in the margin. Yet they belong to the craft as surely as the straightness of the line.

[5] Do not hear this as an old printer's plea to keep every old method. There are movements I shall be glad to surrender. My shoulder has no affection for lifting the same weight all afternoon. Learn the machine. Learn its adjustments so well that you can notice when its regularity has begun to conceal a fault. Then remember that a sheet is going somewhere: to a school, a kitchen, a meeting, a person who may trust it because someone has taken the trouble to print it.

[6] Your hands need not compete with the press at being a press. They must learn what to do beside it. If you return next month, bring me a page you have made and a question you thought to ask before making it. I shall be interested in both."""

RHETORICAL_PROMPT = """Rhetorical analysis essay — A craft beside a machine
Suggested time: 40 minutes.

The following original fictional letter is set in a nineteenth-century print shop. An experienced printer answers a former apprentice who is unsettled by new equipment. Analyze how the writer's rhetorical choices develop advice about skill and responsibility. Support your analysis with specific evidence and explain how the choices respond to the recipient's concern. This is not an archival document.

""" + LETTER

RHETORICAL_MODEL = """One defensible model approach:

The printer reassures the apprentice by redefining craft rather than denying the machine's advantages. Direct address, practical anecdotes, and concessions to the value of speed distinguish repetitive execution from judgment about what a printed page should communicate. The advice lets the apprentice welcome new equipment without concluding that a skilled worker has become unnecessary.

The opening treats the apprentice's fear seriously while identifying a mistaken comparison. Describing old pages as apologies conveys how the apprentice now sees previous work as inadequate. The writer admits admiring the press, so reassurance does not depend on pretending its precision is unimpressive. The distinction between what the machine can do and the whole of the work then establishes the question the rest of the letter will answer: what remains beyond even reproduction?

The memory of sorting type answers through the writer's own apprenticeship. A seemingly minor error can wait in a case and later enter a sentence with the authority of print. Personifying the misplaced letter makes the path of the mistake easy to imagine, while the tired apprentice places responsibility within an ordinary working condition rather than a moral caricature. The recipient is invited to recognize that care in uncelebrated work has always mattered.

The next paragraph explicitly welcomes relief from tiring labor. The reference to schoolbooks connects speed to a public benefit and prevents the letter from becoming a defense of slowness for its own sake. The claim that speed enlarges both care and carelessness then changes the implication of efficiency. Repetition makes prior judgment more consequential, not less. The contrast between reproducing a page faithfully and being faithful to a writer's meaning sharpens that distinction through two senses of the same word.

The incorrect meeting date makes judgment concrete. A beautifully arranged notice could still send people to an empty room. The ten-minute question produces no visible mark, yet it changes the usefulness of the finished object. This example addresses the apprentice's fascination with even sheets by showing a kind of excellence that cannot be seen merely by inspecting their regularity.

Finally, the writer's tired shoulder and willingness to surrender old movements reinforce the absence of nostalgia. The commands to learn the machine are affirmative, followed by a reminder of the people who will use its output. The concluding request for both a page and a question gives the apprentice a manageable next step. Skill includes making an object and knowing when to interrupt its making. The letter restores confidence by expanding the apprentice's understanding of responsibility rather than promising victory in a contest of speed.

Other analyses can develop different supported choices and effects."""

ARGUMENT_PROMPT = """Argument essay — Leaving time unplanned
Suggested time: 40 minutes.

Schedules can protect time for important activities, yet unplanned time can make other experiences possible. Argue your position on the value of deliberately leaving some time unplanned. Support your position with specific evidence and explain your reasoning. Qualify the claim where appropriate; clearly identify hypothetical examples."""

ARGUMENT_MODEL = """One defensible model approach using hypothetical examples:

Leaving some time unplanned is valuable because it allows people to respond to discoveries and needs they could not predict when making a schedule. This is not a reason to treat commitments casually. Its value is greatest when a person protects essential obligations while refusing to assume that every worthwhile experience can be specified in advance.

Imagine a student who schedules every minute of a weekend museum visit around a list of famous objects. The plan may help the student see works that matter to a class project. But if an unfamiliar exhibit raises a new question, the schedule offers no room to investigate it. A short unassigned period would allow the student to follow that interest without abandoning the original purpose of the trip. The point is not that unfamiliar objects are necessarily more valuable than famous ones. It is that the visitor cannot know which encounter will provoke sustained attention before having the encounter.

Unplanned time can also make care possible. Consider a hypothetical volunteer who leaves a small gap between tutoring sessions. One student may need a few extra minutes to explain a difficulty that did not appear in the prepared exercise. Without any margin, the tutor must either cut off the conversation or delay the next person. A gap does not guarantee a useful discussion, but it makes responsive attention less likely to become a broken commitment to someone else. In this setting, spare time supports reliability rather than opposing it.

There are limits to both examples. A student who leaves an entire assignment unscheduled may simply avoid it. A tutoring program with too few appointments may exclude people who need help. Unplanned time has an opportunity cost, and the appropriate amount depends on the purpose and constraints of the activity. It should be a deliberate margin, not a claim that preparation is unnecessary.

Access to such margins is also unequal. Someone balancing paid work, travel, and family responsibilities may have little control over a timetable. Praising spontaneity without acknowledging those constraints can turn a useful practice into an unfair measure of character. Schools and organizations can sometimes create flexibility collectively, such as by leaving transition time, instead of assuming that individuals can manufacture it alone.

A schedule is a tool for directing attention, not a complete forecast of what will deserve attention. Reserving some space within it acknowledges the limits of that forecast. The result can be both more curious and more dependable: a person has a plan for what must happen and some capacity to respond when something else matters.

The scenarios are invented illustrations. Accurate personal or historical evidence may support other positions."""


def essay(kind, unit, skill, prompt, model):
    question = make_essay(kind, unit, skill, prompt, model)
    question['skill_tags'] = [f'ap-skill:{skill}', f'format:{kind}', f'item:lang-e-{kind}']
    return question


QUESTIONS = [
    essay('synthesis', 7, '4.C', SYNTHESIS_PROMPT, SYNTHESIS_MODEL),
    essay('rhetorical-analysis', 5, '5.A', RHETORICAL_PROMPT, RHETORICAL_MODEL),
    essay('argument', 4, '6.C', ARGUMENT_PROMPT, ARGUMENT_MODEL),
]
