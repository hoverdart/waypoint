"""Original guided lessons. Examples are fictional instructional scenarios.

Skill categories checked against the AP English Language course overview.
Lesson completion records a learning check, not AP mastery or an exam score.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    slug: str
    title: str
    skill: str
    objective: str
    explanation: tuple[str, ...]
    example: str
    walkthrough: str
    prompt: str
    options: tuple[str, ...]
    feedback: tuple[str, ...]
    correct: int
    revision: int = 1


FOUNDATIONS = (
    Lesson(
        slug="read-the-situation", title="Read the situation before the sentence", skill="1.A",
        objective="Connect a writer's choice to the audience, occasion, and intended response.",
        explanation=(
            "Start with who is speaking, to whom, and why now. The topic is what a text discusses; the purpose is what the writer wants readers to think, feel, or do about it. A text about library hours might seek a policy change, explain a budget decision, or reassure worried families.",
            "Look for evidence of audience needs rather than inventing them. A reference to a shared deadline, responsibility, or concern can explain why an appeal matters to these readers. Then connect the choice to the intended response: the writer emphasizes X because this audience values Y, supporting the request for Z.",
            "Avoid stopping at a device label such as statistics or emotional appeal. Explain what the selected detail does in this situation. An effect is a supported interpretation, not proof that every reader was persuaded.",
        ),
        example="At a budget hearing, a librarian tells council members: 'Students whose shifts end at six reach locked doors at our branch. Keeping it open until eight on two evenings would let them use the computers they need for applications.'",
        walkthrough="The speaker requests an actionable schedule change from officials who can fund it. The working students' schedules establish a mismatch between current hours and access. The limited two-evening proposal makes the request concrete; it does not establish the proposal's cost or prove approval is inevitable.",
        prompt="A principal writes to families: 'Before next month's bus-route vote, please tell us which stops your children can reach safely.' What is the most supported account of the purpose?",
        options=("To announce that the routes have already been approved", "To gather families' practical knowledge before a decision", "To prove that every existing stop is dangerous"),
        feedback=("The vote is still ahead. Asking for information signals consultation, not a completed decision.", "Yes. The upcoming vote supplies the occasion, and families' knowledge of access is the requested contribution.", "Concern about safety does not establish that every stop is unsafe. Keep the inference within the text's evidence."),
        correct=1,
    ),
    Lesson(
        slug="separate-claim-and-evidence", title="Separate the claim from its support", skill="3.A",
        objective="Identify what a writer argues and evaluate what the evidence actually supports.",
        explanation=(
            "A claim asks readers to accept a position. Evidence provides grounds for accepting it: observations, records, examples, testimony, or data. A reason links support to the position. These roles depend on the argument; a statement can support a larger claim while needing evidence of its own.",
            "Test relevance and scope separately. Relevant evidence addresses the actual claim. Sufficient evidence supports the breadth of that claim. A successful trial at one school can justify further testing, but it cannot alone establish that the policy will work at every school.",
            "For a causal claim, ask what other explanations remain. A change that follows a policy may be consistent with an effect, but a comparison, baseline, and information about other changes make the causal inference stronger.",
        ),
        example="A student editorial argues: 'The district should pilot a later start. At one nearby school, reported tardiness fell during a later-start trial, although its bus routes also changed that semester.'",
        walkthrough="The policy claim is the recommendation to pilot a later start. The nearby school's record is supporting evidence. The simultaneous route change limits a claim that start time alone caused the decline. The modest pilot recommendation fits the uncertainty better than a promise that all schools will get identical results.",
        prompt="A writer claims that a new tutoring program caused higher scores. Which added evidence would best help evaluate that causal claim?",
        options=("A description of the tutoring room's decoration", "A testimonial that repeats the claim in stronger language", "Before-and-after scores for comparable participants and nonparticipants, with information about other instructional changes"),
        feedback=("The room's appearance does not directly test whether the program explains the score change.", "Repeating a conclusion does not independently support it or address alternative explanations.", "Yes. A comparison and information about other changes help evaluate the explanation, although they do not automatically remove every source of bias."),
        correct=2,
    ),
    Lesson(
        slug="develop-relevant-evidence", title="Make evidence earn its place", skill="4.A",
        objective="Choose specific evidence and explain how it develops an appropriately limited claim.",
        explanation=(
            "Before adding evidence, state the exact claim the paragraph must support. Choose details for their relevance, credibility, and precision rather than for how impressive they sound. A vivid anecdote may illustrate an experience without showing how common it is.",
            "Introduce enough context to make evidence interpretable. Who or what was studied? When? Compared with what? Preserve limitations rather than stretching a source into a stronger claim than it supports. If evidence complicates your position, refine the claim.",
            "Follow the detail with commentary explaining the link. A useful draft pattern is claim, specific evidence, and an explanation of why that evidence matters. This is a reasoning check, not a requirement that every paragraph follow an identical formula.",
        ),
        example="Draft claim: 'A shaded waiting area could make the afternoon bus stop more usable in hot weather.' Evidence: 'During three clear afternoons, a student group recorded lower surface temperatures under the stop's existing canopy than on adjacent exposed pavement.'",
        walkthrough="The observation is relevant to local heat conditions. It supports investigating additional shade, but surface temperature is not a direct measure of passenger comfort or air temperature. Strong commentary explains the connection and proposes checking comfort and accessibility before asserting the design solves every problem.",
        prompt="A paragraph recommends a small trial of weekend library hours. Which evidence best develops that recommendation?",
        options=("A local survey describing unmet weekend access needs, paired with estimated staffing costs for a trial", "A national statistic about the total number of books printed", "An assertion that libraries have always been valuable"),
        feedback=("Yes. Local demand and trial costs directly address why the proposal may be useful and feasible. Survey representativeness still matters.", "Book production does not directly establish local demand for weekend access or the feasibility of a trial.", "General value does not explain why this specific change is warranted. Add evidence tied to the proposal."),
        correct=0,
    ),
)


def lessons_for(code: str, unit_order: int) -> tuple[Lesson, ...]:
    return FOUNDATIONS if code == "english-language" and unit_order == 1 else ()
