"""Original guided lessons with fictional examples or attributed historical data.

English skill categories follow the AP English Language course overview.
Lesson completion records a learning check, not AP mastery or an exam score.
"""
from dataclasses import dataclass
from typing import Literal


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
    practice_tag: str | None = None
    example_kind: Literal["fictional", "historical"] = "fictional"


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

AUDIENCE_AND_THESIS = (
    Lesson(
        slug="infer-audience-values", title="Infer audience values from the text", skill="1.B",
        objective="Use textual clues to explain what a writer assumes the audience knows or values.",
        explanation=(
            "An audience is more specific than everyone who might read a text. Start with the occasion and distribution: a letter to donors, a testimony before a board, and a neighborhood notice invite different responses. Then examine what the writer explains, leaves unstated, or treats as a shared priority.",
            "A writer may appeal to values the audience already holds or try to reshape those values. Repeated references to cost might reflect anticipated budget concerns; they do not prove that readers care only about money. Separate the writer's apparent assumptions from facts about every member of the audience.",
            "Support your inference with a particular choice. Explain why that choice fits these readers and this purpose. If several audiences are present, identify the one most directly addressed rather than forcing a single description onto everyone.",
        ),
        example="In a letter to museum members, a director writes: 'You have kept our doors open through difficult years. A monthly contribution now will let us keep admission free for school groups.'",
        walkthrough="The reference to past support positions members as continuing partners. Connecting a monthly contribution with free school visits appeals to an interest in public access, while making a specific request. It does not show that every member has children or agrees with every museum policy.",
        prompt="A housing proposal addressed to a neighborhood association emphasizes that the design preserves the existing courtyard and walking paths. Which inference is best supported?",
        options=("The writer assumes every resident opposes additional housing", "The writer anticipates concern about shared spaces and familiar routes", "The writer believes residents have already approved the design"),
        feedback=("Preservation may address a concern without implying opposition from every resident.", "Yes. The details respond to possible concern about continuity and access in the neighborhood.", "A proposal's reassurance does not establish prior approval. That would require additional evidence."),
        correct=1,
    ),
    Lesson(
        slug="adapt-without-distorting", title="Adapt to readers without distorting the argument", skill="2.B",
        objective="Revise emphasis and explanation for an audience while preserving the claim's accuracy.",
        explanation=(
            "Audience awareness affects which information comes first, how much background readers need, and what objections deserve attention. Before revising, name the action or understanding you want from these particular readers. A change in tone alone cannot repair missing information.",
            "Readers with different responsibilities may need different evidence. Volunteers considering a project need schedules and tasks; officials approving it may need costs, safeguards, and accountability. Neither audience should receive a promise the evidence cannot support.",
            "Respectful acknowledgment can make disagreement productive. State a real concern accurately, then show how your proposal addresses it or where a tradeoff remains. Avoid flattery, stereotypes, and jargon that obscures the decision readers must make.",
        ),
        example="A student asks a facilities manager to approve a courtyard garden. Instead of 'Everyone loves gardens,' the revised request explains who will water it during breaks, where tools will be stored, and how paths will remain accessible.",
        walkthrough="The revision answers practical concerns connected to the manager's responsibilities. It does not abandon the garden proposal; it supplies information the decision requires. Benefits for students can still matter, but enthusiasm alone does not resolve maintenance and access questions.",
        prompt="A writer seeks approval from a school board for a student-run repair workshop. Which revision best addresses that audience's decision?",
        options=("Add a supervision plan, a proposed budget, and a clear description of permitted repairs", "Replace the budget section with a longer celebration of student creativity", "Describe the workshop as risk-free so the board feels reassured"),
        feedback=("Yes. These additions address feasibility and oversight while retaining the proposal's purpose.", "Creativity may be a benefit, but removing the budget withholds information needed for approval.", "An unsupported guarantee conceals uncertainty. Explain safeguards and limitations rather than claiming there is no risk."),
        correct=0,
    ),
    Lesson(
        slug="trace-supporting-claims", title="Trace the claims inside an argument", skill="3.A",
        objective="Distinguish a central claim, supporting reasons, and evidence in a short argument.",
        explanation=(
            "Arguments often contain several claims at different levels. The central claim gives the position the whole text develops. Supporting claims supply reasons for accepting it. Evidence grounds those reasons in something more specific than repetition or assertion.",
            "Ask what each sentence is doing relative to the others. A fact is not automatically evidence for every nearby claim. Test the connection by completing the thought: this detail supports this reason because of this relationship. If you cannot explain the link, the writer may need commentary or better evidence.",
            "An opposing claim can appear inside an argument without becoming the writer's position. Watch for attribution and responses: some critics contend, however, and although can signal different voices. Map the reasoning before deciding which position the writer endorses.",
        ),
        example="An editorial argues that the town should publish meeting recordings. It says recordings help residents whose shifts prevent attendance, then cites interviews with evening workers. It acknowledges that summaries are faster to read but argues that recordings preserve exchanges summaries omit.",
        walkthrough="Publishing recordings is the central recommendation. Access for workers is one supporting reason; the interviews support that reason. The point about convenient summaries is a concession, followed by a separate reason about preserving discussion. Merely counting these sentences would miss their different roles.",
        prompt="An essay states, 'Some opponents call the schedule inflexible. Yet the proposal lets teams select any two afternoons, so it preserves meaningful choice.' What role does the second sentence play?",
        options=("It accepts the opponents' characterization as the essay's conclusion", "It introduces an unrelated benefit of afternoon activities", "It responds to the objection by identifying a flexible feature"),
        feedback=("The word yet and the explanation of choice challenge that characterization.", "Choice among afternoons directly addresses the objection about inflexibility.", "Yes. The writer uses a specific provision to answer the preceding criticism."),
        correct=2,
    ),
    Lesson(
        slug="qualify-evidence-use", title="Use evidence at the scale it supports", skill="4.A",
        objective="Select and frame evidence without turning a limited observation into a universal conclusion.",
        explanation=(
            "Evidence has a scope: a population, time period, setting, and method. Identify those boundaries before using it. A survey of volunteers describes those respondents; it may not represent students who never heard about the survey or chose not to answer.",
            "Relevant evidence can still be limited. Do not discard every imperfect source, but match the claim to what it can establish and combine it with other suitable evidence. An interview can illuminate a mechanism or experience; a broader sample may help estimate prevalence.",
            "When revising, preserve information readers need to evaluate the inference. Words such as all, always, proves, and causes often make a claim broader than the source permits. Replace them when warranted with an accurate description of what was observed, then explain what further evidence would be useful.",
        ),
        example="Twenty students who already attend a writing center say appointments helped them plan essays. A draft concludes, 'Appointments improve every student's writing.' A revision says the responses suggest planning benefits for participating students and recommends a trial that also invites students who have not used the center.",
        walkthrough="The revision retains useful testimony while acknowledging selection and scope. The responses do not directly measure essay quality or represent every student. A broader trial and evaluation of writing would address different questions from the satisfaction survey.",
        prompt="A neighborhood poll of 40 self-selected respondents favors a proposed market. Which use of the poll is most responsible?",
        options=("Describe it as evidence of interest among respondents, then seek broader input before claiming neighborhood-wide support", "Present the result as proof that most residents favor the market because 40 is a precise count", "Omit how participants were selected so readers focus on the market's benefits"),
        feedback=("Yes. This uses the evidence while keeping its representativeness limits visible.", "A precise sample size does not make a self-selected sample representative of all residents.", "Selection is relevant to the inference. Omitting it can make the evidence seem stronger than it is."),
        correct=0,
    ),
    Lesson(
        slug="recognize-a-thesis", title="Recognize the thesis that organizes a text", skill="3.B",
        objective="Identify a defensible central position and connect it to the argument's supporting claims.",
        explanation=(
            "A thesis expresses a position that evidence and reasoning can develop. A subject announcement tells readers what will be discussed but may not establish a position. 'This essay considers public art' names a topic; 'Public art funding should reserve space for temporary neighborhood projects' makes a claim readers can examine.",
            "A thesis may appear after context or emerge across more than one sentence. Do not assume the first or last sentence is automatically the thesis. Look for the position that explains why the writer includes and connects the supporting claims.",
            "The thesis need not list exactly three reasons. What matters is a coherent relationship between the central claim and the reasoning that follows. If a paragraph supports an unrelated position, the writer may need to revise the thesis, the paragraph, or the explanation linking them.",
        ),
        example="After describing empty storefronts, a writer argues that the town should offer short-term leases to local groups. Later paragraphs explain how a trial could test demand and limit long-term commitments, then acknowledge the need for safety inspections.",
        walkthrough="The recommendation about short-term leases organizes the text. Testing demand and limiting commitments explain its appeal; inspections qualify how it should operate. The initial description establishes context, but a description of empty buildings alone does not make the policy argument.",
        prompt="Which sentence offers a central claim that could organize an argument about school announcements?",
        options=("School announcements appear in several formats", "Schools should provide written summaries of spoken announcements so absent students can access essential information", "This essay will discuss whether announcements are useful"),
        feedback=("This observation supplies context but does not establish a position about what should happen or why.", "Yes. The recommendation and access rationale can guide supporting evidence and discussion of implementation.", "This announces a discussion without taking a position that the discussion will defend."),
        correct=1,
    ),
    Lesson(
        slug="write-a-defensible-thesis", title="Write a thesis you can actually defend", skill="4.B",
        objective="Revise a broad assertion into a clear position with a manageable scope and line of reasoning.",
        explanation=(
            "Begin by answering the question the prompt actually asks. A thesis about whether a policy should be adopted differs from a thesis analyzing how a writer persuades an audience. Both need a defensible position, but the evidence and reasoning they require are different.",
            "Make the claim specific enough to guide your paragraphs, without adding a list of reasons you cannot support. A useful qualification identifies a meaningful condition, limit, or tradeoff. Adding sometimes to an otherwise vague statement does not by itself create a thoughtful argument.",
            "Test the draft thesis against your evidence. Could a reasonable reader disagree? Can you explain the connection between your support and your position? Revise overstatements rather than inventing proof. In rhetorical analysis, connect the writer's choices to purpose instead of merely listing devices.",
        ),
        example="Prompt: Should a town replace all printed public notices with online notices? Draft: 'Technology is the future.' Revision: 'The town should expand searchable online notices while retaining printed postings at key public sites, because digital convenience does not eliminate residents' unequal access to reliable internet.'",
        walkthrough="The revision answers the replacement question with a specific position and a rationale that can be supported. It allows a discussion of costs and access. The draft is a slogan about technology that does not resolve whether all printed notices should disappear.",
        prompt="A prompt asks whether schools should require every student to join a competitive team. Which thesis responds with the clearest defensible position?",
        options=("Competition has existed for a long time and affects many people", "There are arguments on both sides, so the issue is complicated", "Schools should offer competitive teams without requiring universal participation, since collaborative noncompetitive activities can also develop commitment"),
        feedback=("Historical context does not answer the question about a universal requirement.", "Acknowledging disagreement is a starting point, but this does not take a position.", "Yes. The thesis addresses the requirement and supplies a rationale that evidence and counterargument can develop."),
        correct=2,
    ),
)

REASONING_AND_DEVELOPMENT = (
    Lesson(
        slug="identify-the-assumption", title="Find the assumption between evidence and claim", skill="3.A",
        objective="Explain the unstated connection a writer needs for evidence to support a claim.",
        explanation=(
            "Evidence does not interpret itself. A writer moves from an observation to a conclusion by relying on a connection, sometimes called a warrant. Naming that connection helps you explain the argument instead of merely repeating its details.",
            "Try writing the argument as evidence, assumed relationship, and claim. Then ask whether the relationship is plausible and what could limit it. An assumption is not automatically a flaw: ordinary reasoning depends on assumptions. The useful question is whether this assumption is justified in this situation.",
            "Keep the scale of the conclusion in view. Evidence that one feature matters to some users may support testing a change without proving it should be adopted everywhere. A narrower claim can remain persuasive even when a sweeping version would fail.",
        ),
        example="A campus editorial says, 'Several students leave evening study sessions early to catch the last bus. Extending the bus schedule would allow those students to stay longer.'",
        walkthrough="The observation connects early departure with the last bus. The conclusion assumes transportation is a constraint on these students' attendance and that a later bus would be usable. The editorial would need more evidence to claim that all students would study longer or that the change would necessarily improve grades.",
        prompt="A proposal argues that posting recordings of public meetings will improve access for residents who work during meeting hours. Which assumption most directly connects the proposal to its reason?",
        options=("Most residents disagree with decisions made at public meetings", "At least some affected residents can access recordings at a more convenient time", "Recorded meetings will be shorter than live meetings"),
        feedback=("Disagreement is not necessary for the access argument. The relevant issue is when and how residents can follow proceedings.", "Yes. The argument depends on recordings being usable outside the conflicting work hours.", "The proposal can improve scheduling access even if a recording lasts as long as the original meeting."),
        correct=1,
    ),
    Lesson(
        slug="choose-complementary-evidence", title="Choose evidence that adds a new kind of support", skill="4.A",
        objective="Combine complementary evidence instead of accumulating details that repeat the same point.",
        explanation=(
            "More evidence is not always stronger evidence. Several anecdotes can repeat an experience without establishing how widespread it is. Choose the next source by identifying the question your existing support leaves unanswered.",
            "Different forms of evidence do different work. A personal account can reveal a mechanism or consequence. A representative survey can estimate how common a view is. A budget can address feasibility. Match the evidence to the claim rather than treating every statistic as inherently stronger than every example.",
            "Preserve disagreements and limits between sources. If interviewees report a benefit while cost records show an obstacle, develop a qualified proposal that addresses both. Synthesis means explaining relationships among evidence, not lining up quotations as if they all make the same point.",
        ),
        example="An argument for translated emergency notices includes a resident's account of misunderstanding an evacuation message. The writer adds a local language-access survey and estimates from qualified translation services.",
        walkthrough="The account illustrates consequences, the survey helps establish the scope of local need, and estimates address implementation. Each source supports a different part of the proposal. Neither one resident's experience nor the survey alone establishes the cost or reliability of a translation plan.",
        prompt="A writer has three interviews describing difficulty reaching a clinic by bus. The next paragraph claims a proposed shuttle is financially feasible. Which addition best supports that new claim?",
        options=("A fourth interview describing the same travel difficulty", "A photograph showing a long line at the clinic entrance", "A documented operating-cost estimate compared with identified funding"),
        feedback=("Another account may reinforce the access concern but does not establish the shuttle's affordability.", "The photograph may raise questions about demand, but it does not supply cost or funding information.", "Yes. Cost and funding evidence directly addresses financial feasibility; the writer should still identify assumptions in the estimate."),
        correct=2,
    ),
    Lesson(
        slug="test-the-line-of-reasoning", title="Test each step in the line of reasoning", skill="5.A",
        objective="Evaluate whether an argument's sequence of claims supports its conclusion.",
        explanation=(
            "A line of reasoning is the path from supporting claims to a conclusion. Outline what each paragraph contributes using verbs such as establishes, explains, compares, qualifies, and responds. This reveals relationships that a list of topics can miss.",
            "Check each transition in the logic. Does a local observation become a universal claim? Does sequence in time become proof of cause? Does the writer change the meaning of a key term? Identify the exact step and the missing support instead of simply calling the whole argument weak.",
            "A counterexample may require qualification rather than total rejection. Distinguish evidence against a reason from evidence against the conclusion itself. A sound conclusion can have a poorly supported justification, and a plausible reason may still be insufficient for a broad conclusion.",
        ),
        example="A writer notes that registrations rose after a recreation center extended its hours, then concludes that longer hours caused the entire increase. The center also reduced fees and launched an advertising campaign during the same period.",
        walkthrough="The chronology is relevant, but the causal conclusion exceeds it. Fees and advertising offer alternative explanations. The writer could revise to say the increase coincided with the changes and seek comparisons that help isolate the role of hours.",
        prompt="A proposal argues that one successful outdoor class proves every course should meet outdoors all year. Where does its reasoning most clearly need support?",
        options=("The move from one class in one setting to all courses and seasons", "The use of a specific example instead of an abstract opening", "The decision to discuss a school policy rather than a personal preference"),
        feedback=("Yes. The conclusion extends beyond the conditions the example establishes; different subjects and weather may matter.", "Specific examples can be useful. The issue is the breadth of the inference drawn from this one.", "Policy arguments are legitimate. The gap lies between the evidence's scope and the proposed universal rule."),
        correct=0,
    ),
    Lesson(
        slug="write-commentary-that-connects", title="Write commentary that makes the connection", skill="6.A",
        objective="Explain why evidence supports a claim rather than paraphrasing it or announcing its importance.",
        explanation=(
            "Commentary supplies the reasoning between a detail and your claim. Ask what the evidence shows, why that matters for this argument, and how far the inference extends. A sentence saying 'This proves my point' performs none of those jobs unless it explains the connection.",
            "In rhetorical analysis, connect a writer's choice to the audience and purpose. Do not treat naming a device as an explanation of its effect. In an argument, explain how an example or observation supports a reason and how that reason advances your position.",
            "Avoid claiming certainty about every reader's reaction. Use the text and situation to support a plausible effect. Strong commentary can also identify a limit: a detail may establish urgency without showing that the proposed solution is affordable.",
        ),
        example="A speaker urging repair of a footbridge tells officials that residents must now take a two-mile detour to reach a grocery store. Weak commentary says, 'This shows the bridge is important.' Stronger commentary explains that the detour turns structural damage into a daily access problem, giving officials a concrete public-service reason to prioritize repairs.",
        walkthrough="The stronger version explains the relationship between the detail and the request. It does not merely rename the topic. The detour helps establish the repair's significance, although it does not determine engineering costs or prove repairs should outrank every other project.",
        prompt="A writer advocating extended clinic hours cites workers who cannot attend during their shifts. Which commentary best connects that evidence to the proposal?",
        options=("The workers say they cannot attend during their shifts, which is what the evidence states", "Offering appointments outside those shifts would address a scheduling barrier identified in the workers' accounts", "The evidence is very powerful and proves the writer is completely correct"),
        feedback=("This repeats the evidence without explaining why the proposed change responds to it.", "Yes. The commentary identifies the barrier and explains how the proposal could address it without promising to solve every access problem.", "Praise and certainty do not supply reasoning. Explain the specific relationship between the accounts and the proposal."),
        correct=1,
    ),
    Lesson(
        slug="recognize-development-methods", title="Explain why a writer develops an idea this way", skill="5.C",
        objective="Identify a method of development and explain its function in the argument.",
        explanation=(
            "Writers develop ideas through methods such as narration, description, comparison, definition, and cause-and-effect explanation. A passage may combine several. Identify the method by what the sentences do, then connect it to the claim the writer is developing.",
            "A comparison can clarify a distinction, expose an inconsistency, or support an evaluation. A narrative can establish a problem through an experience. Neither method guarantees sound reasoning: check whether the compared cases are relevant or whether the story is being asked to represent more than it can.",
            "Avoid confusing organization with purpose. Chronological order tells you how a passage proceeds, but you still need to explain why that sequence helps the writer. A procedural account may show where a delay occurs; a before-and-after account may emphasize a change.",
        ),
        example="An article places two application processes side by side: one requires several office visits, while the other allows documents to be submitted in a single appointment. It compares the same steps in each process before recommending a trial of the second.",
        walkthrough="The comparison isolates procedural differences relevant to the recommendation. It helps readers see where repeated visits might be reduced. The writer would need separate evidence to establish effects on accuracy, staffing costs, or every applicant's experience.",
        prompt="A paragraph recounts each step a resident takes to report a broken streetlight, emphasizing that the same information must be submitted to three offices. What is the most supported account of the method's function?",
        options=("It defines the technical meaning of electrical failure", "It compares streetlights with other kinds of public infrastructure", "It traces a process to reveal duplication that motivates procedural reform"),
        feedback=("The sequence concerns reporting, not an explanation of an electrical concept.", "No second type of infrastructure is developed as a basis for comparison.", "Yes. Following the resident's steps makes the repeated submissions visible and supports considering a simpler process."),
        correct=2,
    ),
    Lesson(
        slug="develop-an-argument-purposefully", title="Choose a development method that serves your claim", skill="6.C",
        objective="Plan an argument's development around the reasoning readers need to follow.",
        explanation=(
            "Choose a method after identifying the job a paragraph must do. To clarify a misunderstood term, define it with relevant boundaries. To evaluate alternatives, compare them using consistent criteria. To explain a proposed remedy, show how it addresses the problem's causes or mechanisms.",
            "A method is a tool rather than a mandatory template. You can begin with an illustrative narrative and then compare alternatives, provided you explain the relationship. Do not let a vivid opening consume space needed for evidence or leave the central recommendation unstated.",
            "Check the completed plan for fairness and relevance. Compare options on the same criteria, acknowledge differences that limit the comparison, and explain tradeoffs. Develop the position the prompt asks for instead of substituting an easier description of the general topic.",
        ),
        example="A writer choosing between two school lunch systems organizes the argument around waiting time, dietary access, and cost. Under each criterion, the writer considers both systems, then recommends a limited trial with measures for judging the results.",
        walkthrough="Using shared criteria makes the comparison usable for a decision. Describing only the benefits of one system and only the costs of the other would create an uneven comparison. The trial recommendation can address uncertainty if the writer explains what it will test.",
        prompt="You are arguing that a confusing permit process should be simplified. Which plan most directly develops that argument?",
        options=("Trace where applicants repeat steps, explain the proposed changes, and evaluate how those changes preserve necessary review", "List every type of permit issued by the town without connecting the list to the process", "Describe a successful applicant's celebration and assume readers will infer the needed changes"),
        feedback=("Yes. This plan links the identified problem to a remedy while addressing a likely concern about maintaining oversight.", "A catalog may supply background but does not explain what is confusing or how simplification would work.", "A story can engage readers, but it cannot replace the explanation of the proposed reform and its consequences."),
        correct=0,
    ),
)

PURPOSE_AND_STRUCTURE = (
    Lesson(
        slug="connect-occasion-and-choice", title="Connect the occasion to the writer's choices", skill="1.A",
        objective="Explain how a specific situation makes a writer's emphasis meaningful.",
        explanation=(
            "A rhetorical situation includes more than a topic. Consider the speaker's role, the audience, the event that prompts the text, and what the writer hopes to accomplish. The same topic can produce a celebration, an explanation, a warning, or a request, depending on the occasion.",
            "Ask why this writer addresses these readers now. A looming decision can explain urgency; a recent misunderstanding can explain a careful definition; a commemoration can explain an appeal to shared memory. Support the connection with details rather than supplying an invented history.",
            "A text may serve several purposes, but distinguish the main aim from supporting moves. A speaker may praise volunteers to establish solidarity before requesting help. Explain how the praise contributes to the request rather than assuming praise is the only purpose.",
        ),
        example="Before a neighborhood vote on flood-prevention funding, a resident recalls helping neighbors clean their homes after a storm. She then asks voters to examine the proposed drainage plan, including its cost and maintenance requirements.",
        walkthrough="The approaching vote creates an immediate decision. The shared experience establishes why drainage matters, while the request directs that concern toward evaluating a particular plan. The account does not alone show that the plan is effective or that every resident supports it.",
        prompt="After residents mistake a preliminary map for an approved route, a transit director begins a notice by distinguishing proposals from final decisions. Why is that opening especially relevant to the occasion?",
        options=("It responds to a misunderstanding that could distort residents' participation in the pending decision", "It establishes that the director opposes all route changes", "It guarantees that no reader will misunderstand later notices"),
        feedback=("Yes. Clarifying the map's status helps readers understand what is still open for discussion.", "Explaining the stage of a decision does not establish opposition to every possible change.", "The clarification can help, but the text does not guarantee every reader's future response."),
        correct=0,
    ),
    Lesson(
        slug="open-and-close-with-purpose", title="Give openings and conclusions a job", skill="2.A",
        objective="Choose an opening and conclusion that advance the text's purpose rather than follow a formula.",
        explanation=(
            "An opening orients readers to the question, stakes, or perspective they need. A narrative, definition, contrast, or direct claim can work when it serves that job. A dramatic hook is not automatically useful, and broad claims about all of human history often delay the actual argument.",
            "Choose the background readers need before your claim makes sense. Do not summarize every related fact. For a practical proposal, clarify the problem and decision; for rhetorical analysis, establish the relevant speaker, audience, and purpose without retelling the whole passage.",
            "A conclusion can draw out an implication, explain why the reasoning matters, or specify a warranted next step. It may return to an opening image with new significance. Avoid introducing a major unsupported claim at the end or merely replacing words in the thesis with synonyms.",
        ),
        example="An essay proposing captioned recordings opens with the problem of missing an announcement in a noisy room. After discussing access, accuracy, and production costs, it closes by recommending a trial of captions on weekly notices and a process for correcting errors.",
        walkthrough="The opening makes an access problem concrete. The conclusion converts the developed reasoning into a limited next step and preserves the concern about accuracy. A promise that captions eliminate every communication barrier would exceed what the essay established.",
        prompt="An argument has compared the benefits and costs of a six-week community compost trial. Which conclusion best builds on that reasoning?",
        options=("People have produced waste throughout history, and waste is a very large topic", "Launch the trial with the proposed collection schedule, then assess participation and costs before expanding it", "All household waste problems will disappear once the trial begins"),
        feedback=("This broad background does not develop an implication of the comparison already made.", "Yes. The conclusion connects the evaluation to a specific, limited next step and a basis for judging expansion.", "The claim is much broader than a six-week trial and ignores limits discussed in the argument."),
        correct=1,
    ),
    Lesson(
        slug="map-thesis-to-sections", title="Map the thesis to the argument's sections", skill="3.B",
        objective="Explain how supporting claims develop the central position, including qualifications.",
        explanation=(
            "Once you identify a thesis, test how each section relates to it. A section may establish a reason, support that reason with evidence, define a condition, or answer an objection. A text's organization is not necessarily a list of independent reasons of equal importance.",
            "Look for qualifications within the central position. If the thesis recommends a change only under certain conditions, a paragraph about those conditions may be essential rather than a digression. A fair account of the thesis must preserve those limits.",
            "Separate a writer's position from the alternatives discussed. A paragraph describing a rejected option is not evidence that the writer endorses it. Follow the transitions and evaluation to see how the option contributes to the argument's final recommendation.",
        ),
        example="A writer recommends converting an unused lot into a recreation area if the plan preserves a stormwater channel. One section explains the need for play space; another evaluates drainage requirements; a third rejects a design that would block the channel.",
        walkthrough="The drainage section develops a condition in the thesis, not an unrelated technical issue. Rejecting one design is consistent with supporting a recreation area under the stated condition. Describing the thesis as simply 'build on the lot' would erase a central limitation.",
        prompt="A thesis favors expanded online services while retaining in-person help. What role would a paragraph about residents who cannot reliably use online forms most directly play?",
        options=("It necessarily abandons the thesis by criticizing digital tools", "It proves that online services are useless for every resident", "It develops the reason for retaining the in-person option specified in the thesis"),
        feedback=("The thesis already includes an in-person option, so this paragraph can support that qualified position.", "Difficulty for some residents does not establish that digital services have no value for anyone.", "Yes. The paragraph explains the need for one of the thesis's stated conditions."),
        correct=2,
    ),
    Lesson(
        slug="build-an-analysis-thesis", title="Turn an observation into an analysis thesis", skill="4.B",
        objective="Write a defensible thesis that connects rhetorical choices to a writer's purpose.",
        explanation=(
            "An analysis thesis makes a claim about how a text works. It does not simply agree with the writer's policy or list techniques. Start with a meaningful choice in the passage and explain how it contributes to the purpose in this rhetorical situation.",
            "You can describe a choice precisely without a specialized label. A writer might contrast a familiar routine with an unexpected consequence, repeat a shared responsibility, or acknowledge a likely objection. The thesis should point toward analysis that the passage can support.",
            "Avoid generic effects such as grabs attention when the text permits a more specific explanation. Also avoid claiming the writer succeeds with every reader. A thesis proposes an interpretation that the body develops through details and commentary; naming three devices is not required.",
        ),
        example="A safety notice begins by acknowledging that workers already complete many checklists, then describes one overlooked step that prevents a common equipment error. A thesis might argue that the notice recognizes workers' workload before narrowing its request, presenting the added check as a targeted precaution rather than indiscriminate paperwork.",
        walkthrough="The thesis identifies two related choices and interprets their role for a particular audience. It gives the analysis something to demonstrate. 'The writer uses persuasion and good examples' would not distinguish this notice from countless other texts.",
        prompt="A speech to volunteers recalls their past successes before asking them to train new members. Which thesis offers the strongest basis for rhetorical analysis?",
        options=("By presenting past achievements as the result of shared effort, the speaker frames mentoring as a continuation of the volunteers' existing commitment", "The speaker uses words, examples, and sentences to make a good speech", "The volunteers should train new members because mentoring is always beneficial"),
        feedback=("Yes. This connects a specific choice to the request and offers an interpretation the analysis can test against the speech.", "These categories are too broad to explain how this speech develops its purpose.", "This endorses the request rather than analyzing the speaker's choices, and its universal claim needs separate support."),
        correct=0,
    ),
    Lesson(
        slug="analyze-definition-and-contrast", title="Analyze how definition changes an argument", skill="5.C",
        objective="Explain how a writer uses definition or contrast to shape the terms of a debate.",
        explanation=(
            "Arguments often turn on the meaning of a key term. A writer may narrow, expand, or distinguish a term to change what readers consider relevant. Notice how the definition affects the claims that follow, rather than treating it as neutral background automatically.",
            "A contrast can make the definition visible. Distinguishing access from mere availability, for example, invites attention to whether people can actually use a service. Evaluate whether the distinction is relevant and consistently applied; a useful definition still needs supporting evidence.",
            "Do not assume a writer has proved a policy merely by choosing a favorable definition. Ask what consequences follow if readers accept it and what questions remain. Definitions organize reasoning; they do not replace evidence about costs, effects, or implementation.",
        ),
        example="An essay distinguishes making a public document available from making it usable. It notes that a scanned image may be online while still being difficult to search or read with assistive technology, then proposes publishing accessible text versions.",
        walkthrough="The distinction shifts evaluation from the fact of publication to how readers can use the document. It helps explain why a text version matters. The writer still needs evidence about the proposed process, and the example does not prove every scanned document is equally inaccessible.",
        prompt="A writer distinguishes attendance from participation before discussing students who are present but rarely have a chance to speak. What does the distinction contribute?",
        options=("It proves that attending class has no educational value", "It establishes a standard for evaluating involvement beyond physical presence", "It shows that every quiet student wants to speak more often"),
        feedback=("The distinction does not require rejecting the value of attendance; it identifies an additional dimension.", "Yes. The definition prepares readers to consider opportunities for contribution rather than counting presence alone.", "The writer would need further evidence about individual preferences. Quietness alone does not establish them."),
        correct=1,
    ),
    Lesson(
        slug="combine-development-methods", title="Combine methods without losing the argument", skill="6.C",
        objective="Build a coherent sequence that connects illustration, explanation, and evaluation.",
        explanation=(
            "A developed argument can use several methods for different jobs. An example may introduce a problem, a process explanation may show why it occurs, and a comparison may evaluate possible remedies. Make the relationship clear so the text does not become a collection of unrelated sections.",
            "Choose the order readers need. If they cannot evaluate alternatives without understanding the problem, establish the problem first. If a familiar term is misleading, define it before applying it. There is no single required order; justify your sequence through the reasoning it enables.",
            "After outlining, test each section against the central claim. Explain how an opening example represents the relevant issue without treating it as universal proof. Compare alternatives fairly, and preserve important limits in the recommendation that follows.",
        ),
        example="An essay about missed medical appointments begins with one patient's scheduling difficulty, explains how conflicting work hours and transit schedules can combine, then compares evening appointments with transportation vouchers. It recommends testing the option best suited to the documented local barrier.",
        walkthrough="The narrative illustrates an experience, the explanation identifies a possible mechanism, and the comparison evaluates responses. Broader local evidence is still needed before generalizing from the opening story. The recommendation depends on which barrier the evidence establishes.",
        prompt="An essay opens with a confusing evacuation notice and recommends clearer public warnings. Which next sequence most directly develops the recommendation?",
        options=("Retell several unrelated emergencies, then repeat that clear writing is good", "Describe the notice's paper quality, then rank printing companies by size", "Explain the ambiguous wording, compare clearer revisions, and address how officials can test comprehension"),
        feedback=("Additional stories may not explain the wording problem or establish how the proposed improvement would work.", "Paper and company size do not directly address the notice's confusing language.", "Yes. The sequence moves from a specific problem to alternatives and a practical way to evaluate the remedy."),
        correct=2,
    ),
)

COHERENCE_AND_STYLE = (
    Lesson(
        slug="follow-a-changing-explanation", title="Follow an explanation as it becomes more precise", skill="5.A",
        objective="Explain how a qualification or alternative explanation changes an argument's reasoning.",
        explanation=(
            "An argument does not always move in a straight line from certainty to proof. A writer may introduce a plausible explanation, examine evidence that complicates it, and arrive at a more limited conclusion. Track changes in the claim instead of treating each sentence as equally certain.",
            "Notice words that signal the writer's degree of confidence: suggests, is consistent with, establishes, or rules out. These expressions make different commitments. In science writing especially, evidence may support a hypothesis while leaving alternatives unresolved.",
            "Ask what each qualification does. Does it narrow the population, identify a condition, or acknowledge another cause? A qualification can strengthen reasoning by making the conclusion fit the evidence. It does not necessarily mean the writer has abandoned the argument.",
        ),
        example="A fictional field report notes that more insects were counted near restored vegetation than near bare ground. It first considers whether the plants explain the difference, then observes that the vegetated plots were also closer to water. The report recommends comparing plots with similar water access.",
        walkthrough="The observation supports investigating a relationship but does not isolate vegetation as the cause. The later detail introduces an alternative explanation, and the proposed comparison responds to that uncertainty. Describing the report as proving that restoration caused the increase would erase its reasoning.",
        prompt="A review says a rehearsal method coincided with fewer mistakes, then notes that the musicians also received more practice time. What does the second detail do?",
        options=("It proves the rehearsal method had no effect", "It introduces an alternative explanation that limits a causal conclusion", "It shows the initial observation was necessarily fabricated"),
        feedback=("Another possible cause does not establish that the method had no effect at all.", "Yes. The additional practice could contribute to the change, so the method's independent effect remains uncertain.", "The two details can both be accurate. The issue is what caused the observed difference."),
        correct=1,
    ),
    Lesson(
        slug="explain-a-detail-in-context", title="Make commentary specific to the detail", skill="6.A",
        objective="Develop commentary that explains a detail's significance in its particular context.",
        explanation=(
            "A useful commentary sentence should not fit almost any quotation. Identify what is distinctive about the detail: a contrast, a surprising description, a repeated idea, or a change in perspective. Then explain how it advances the interpretation you are developing.",
            "In a memoir or reflective essay, distinguish the experience being recalled from the later perspective of the narrator. A detail may reveal what the narrator did not understand at the time. Support this interpretation through the language and sequence rather than inventing an emotion.",
            "Move beyond paraphrase, but stay within the evidence. Commentary can explain why a small action complicates an earlier judgment. It should not turn one detail into an unsupported diagnosis of a person's entire character or a universal claim about human behavior.",
        ),
        example="In an original memoir passage, a narrator remembers dismissing a parent's habit of saving seed packets as clutter. Years later, the narrator reads planting dates penciled on each packet and describes them as 'a record of patient experiments.'",
        walkthrough="The shift from clutter to a record changes the meaning of the same objects. The later narrator recognizes deliberate work that the younger self overlooked. The detail supports an interpretation of revised understanding, not a claim that the parent never made a mistake.",
        prompt="A narrator once called a neighbor's careful repairs 'fussing' but later describes the repaired chair as 'steady after all these years.' Which commentary best explains the contrast?",
        options=("The narrator uses words to describe a chair and a neighbor", "The chair proves that all old objects are better than new ones", "The chair's durability leads the narrator to reassess care previously dismissed as needless effort"),
        feedback=("This identifies the subject without explaining the significance of the changed description.", "One chair cannot support that universal comparison, and the passage does not make it.", "Yes. The later observation gives the earlier judgment a different meaning and supports a change in perspective."),
        correct=2,
    ),
    Lesson(
        slug="read-paragraph-relationships", title="Read the relationship between paragraphs", skill="5.B",
        objective="Explain how paragraph order creates coherence and advances an argument.",
        explanation=(
            "Coherence comes from meaningful connections among ideas, not just transition words. Ask what readers learn in one paragraph that prepares them for the next. A paragraph may supply background, illustrate a generalization, complicate a claim, or explain a consequence.",
            "Track repeated key terms and changes in their meaning. A writer can begin with a familiar idea and refine it across paragraphs. If a new paragraph seems unrelated, look for the shared question before deciding whether it is a digression.",
            "Evaluate order by purpose. A definition may need to precede a distinction; evidence may prepare readers for a qualified conclusion. More than one arrangement can work, but moving a paragraph can change what readers assume or understand at that point.",
        ),
        example="An arts review first describes the strict symmetry of an exhibition's entrance gallery. The next paragraph examines a later room where uneven spacing and interrupted patterns replace that symmetry. The review then interprets the contrast as a deliberate disruption of expectations.",
        walkthrough="The first description establishes the pattern that the second complicates. Without that baseline, the later claim about disrupted expectations would be harder to follow. The sequence contributes to interpretation rather than simply listing rooms in no meaningful order.",
        prompt="A science essay defines the difference between weather and climate before examining why a cold week does not settle a claim about long-term trends. What is the first paragraph's most direct function?",
        options=("It supplies a distinction the subsequent evaluation depends on", "It conclusively establishes the cause of every temperature change", "It contradicts the possibility that a particular week can be cold"),
        feedback=("Yes. The definition separates short-term conditions from the kind of pattern the next paragraph evaluates.", "Defining terms does not identify the cause of every observed change.", "The distinction allows short-term variation; it does not deny the week's conditions."),
        correct=0,
    ),
    Lesson(
        slug="write-meaningful-transitions", title="Write the connection, not just a transition word", skill="6.B",
        objective="Choose transitions that accurately express relationships between ideas.",
        explanation=(
            "Before choosing a transition, identify the relationship: addition, contrast, concession, cause, consequence, example, or qualification. A word such as therefore makes a logical commitment. It cannot create a causal or inferential connection the surrounding sentences do not support.",
            "Sometimes a short connecting sentence works better than a single word. Repeat the relevant idea in a precise way and explain how the next point changes or extends it. Avoid vague references such as this when several possible antecedents compete.",
            "Read both sides of the transition after revising. A concession acknowledges a point before limiting its implications; a contrast identifies a difference. Do not use however automatically whenever a new paragraph begins or furthermore when the next point actually challenges the previous one.",
        ),
        example="Draft: 'The archive has digitized its photographs. Therefore, several descriptions still omit dates.' Revision: 'Digitization has made the photographs easier to locate. However, missing dates in several descriptions still limit researchers' ability to establish chronology.'",
        walkthrough="The revision identifies a benefit and a remaining limitation. Therefore would incorrectly suggest that digitization explains the missing dates. The fuller connection also clarifies why the limitation matters, rather than merely announcing another fact.",
        prompt="Choose the most accurate connection: 'The rehearsal recording preserves every note. ___ it cannot show the conductor's gestures, which shaped the performance.'",
        options=("As a result,", "However,", "For the same reason,"),
        feedback=("Preserving notes does not cause the absence of visual information; the second point limits what the recording captures.", "Yes. The second sentence qualifies the recording's usefulness by identifying a different kind of information it lacks.", "No shared cause has been established. The relationship is a contrast between what is preserved and what is missing."),
        correct=1,
    ),
    Lesson(
        slug="analyze-diction-and-comparison", title="Explain what diction and comparison contribute", skill="7.A",
        objective="Connect word choice or comparison to tone, perspective, and purpose.",
        explanation=(
            "Words carry associations as well as literal meanings. Calling a revision meticulous, fussy, or painstaking can describe similar attention while suggesting different attitudes. Explain those associations in context rather than treating a word as having the same tone everywhere.",
            "A comparison selects particular shared features. Ask which feature the writer invites readers to notice and why it matters to the argument. An analogy can clarify an unfamiliar process without proving that the two things are identical in every respect.",
            "Name tone precisely when the evidence supports it, then explain how it contributes to the text. Do not assume that vivid language is automatically admiring or that plain language lacks rhetorical effect. A restrained description may serve a cautious or corrective purpose.",
        ),
        example="A fictional essay calls an early scientific model 'a useful map with unfinished edges.' The comparison preserves the model's practical value while acknowledging limits in what it represents.",
        walkthrough="Useful resists dismissing the model as worthless; unfinished edges marks incomplete knowledge. The map comparison helps readers hold value and limitation together. It does not imply the model is a literal geographic map or that every unrepresented feature has equal importance.",
        prompt="A critic describes a performance as 'precise, but never mechanical.' What does the qualification most directly contribute?",
        options=("It retracts the description of the performance as precise", "It claims that the performers used no instruments or equipment", "It distinguishes technical control from an absence of expression"),
        feedback=("The critic retains the praise for precision while limiting a possible negative association.", "Mechanical describes a quality of performance here, not a literal inventory of equipment.", "Yes. The phrase suggests that accuracy and expressive vitality coexist in the performance."),
        correct=2,
    ),
    Lesson(
        slug="choose-style-for-purpose", title="Choose language that serves the purpose", skill="8.A",
        objective="Revise diction and comparison for a precise rhetorical effect without distorting meaning.",
        explanation=(
            "Style is a set of choices about how meaning reaches readers. Start with the intended effect: clarify a distinction, convey urgency, acknowledge uncertainty, or invite reflection. More elaborate language is not automatically more effective.",
            "Test connotations against the evidence. Calling a tentative finding a breakthrough can imply certainty or significance the source does not establish. A metaphor can help explain a process, but you should retain the limits that prevent readers from taking the comparison too far.",
            "Revise for both audience and accuracy. A public explanation may replace unnecessary jargon with a concrete description, while a specialist audience may need the technical term. Aim for the language that makes the relevant meaning clear, not simply the shortest or most dramatic sentence.",
        ),
        example="A draft museum label says, 'This revolutionary artifact single-handedly transformed domestic existence.' A revision says, 'This tool shortened one repeated household task, although access varied by region and income.'",
        walkthrough="The revision replaces sweeping praise with an interpretable claim and a relevant limitation. It may need additional explanation of the task, but it gives readers a clearer basis for understanding the object's significance without attributing all social change to one object.",
        prompt="A field team has observed a pattern in a small preliminary sample. Which phrasing best fits a careful public report?",
        options=("The early observations suggest a pattern that a larger sample could help test", "The observations settle the question forever", "The small sample makes every observation meaningless"),
        feedback=("Yes. This states the provisional value of the observations and identifies what further work could contribute.", "A preliminary sample cannot justify that degree of finality.", "Limited evidence can still guide investigation; acknowledging its scope does not require treating it as worthless."),
        correct=0,
    ),
)

SOURCES_AND_REFINEMENT = (
    Lesson(
        slug="evaluate-source-support", title="Evaluate what a source can support", skill="3.A",
        objective="Assess a source's relevance and basis of knowledge without treating authority as automatic proof.",
        explanation=(
            "Identify the exact claim a source is being used to support. Expertise is relevant when it concerns that claim, and a source's method matters as much as its title. A firsthand account can establish an experience without establishing how common that experience is.",
            "Consider when and why the source was produced, what evidence it uses, and whose perspective may be absent. An institutional interest gives you a reason to examine a claim carefully, not permission to dismiss every statement without evaluation. Likewise, agreement with your position does not make a source reliable.",
            "Separate what the source reports from what the writer infers. A report about participants' preferences does not necessarily demonstrate improved outcomes. Preserve these distinctions when explaining the relationship between evidence and a claim.",
        ),
        example="A fictional software vendor reports that most surveyed customers liked a new writing tool. An essay uses the report to claim that the tool improves all students' analytical writing. The survey measures reported satisfaction among customers, not writing gains across students.",
        walkthrough="The report may support a limited statement about the surveyed customers' views. The vendor's interest and sample selection deserve scrutiny, but the most direct problem is the mismatch between the measured outcome and the essay's claim. Independent assessment of writing would address a different question.",
        prompt="A retired engineer describes the tools used in one workshop decades ago. Which claim is most directly supported by that account alone?",
        options=("Every workshop in the country used identical tools", "The engineer recalls particular practices in that workshop during that period", "Those tools were more efficient than all modern alternatives"),
        feedback=("One workshop's account does not establish nationwide uniformity.", "Yes. This claim preserves the account's setting, time, and status as recollection; corroboration could strengthen it.", "A comparison of efficiency requires evidence about performance and alternatives, not only a recollection of use."),
        correct=1,
    ),
    Lesson(
        slug="put-sources-in-conversation", title="Put sources in conversation", skill="4.A",
        objective="Use relationships among sources to develop your own claim rather than summarize them separately.",
        explanation=(
            "Begin with the point your paragraph needs to establish. Then select evidence from sources that helps develop that point. Organizing every paragraph around a different source can produce a report on readings instead of an argument of your own.",
            "Look for a precise relationship: one source may extend another, explain a mechanism behind a finding, challenge an assumption, or describe a different population. Apparent disagreement may result from different questions or measures. Explain that difference before declaring one source wrong.",
            "Attribute evidence clearly and distinguish source claims from your interpretation. Do not blend different measures into a single unsupported conclusion. Your commentary should explain how the relationship affects the argument, including any limits it introduces.",
        ),
        example="One fictional transit report records shorter average travel times after a route change. A rider survey describes longer walks to several stops. An argument can use both to distinguish time spent traveling from access to the starting point, rather than treating the survey as a direct contradiction of the travel-time average.",
        walkthrough="The sources measure different aspects of service. Together they can support evaluating both travel time and access. The writer must still examine how the average and survey were produced before generalizing about all riders.",
        prompt="Source A reports high attendance at a free exhibit; Source B describes visitors who could not reach it during opening hours. Which synthesis best preserves both sources' contributions?",
        options=("High attendance shows that scheduling creates no access barriers", "The accounts of excluded visitors prove the attendance count is false", "The exhibit attracted many visitors while its hours may still have excluded some interested people"),
        feedback=("A large count does not establish that everyone interested could attend.", "The two findings can coexist. Visitors who could not attend are not part of the attendance count.", "Yes. This distinguishes observed participation from access and creates a basis for considering scheduling changes."),
        correct=2,
    ),
    Lesson(
        slug="find-the-thesis-in-a-complex-text", title="Find the position beneath competing perspectives", skill="3.B",
        objective="Identify a writer's central position while preserving the conditions and distinctions that shape it.",
        explanation=(
            "A text can describe several positions before stating its own. Track attribution and evaluation: which views are assigned to others, which are qualified, and which conclusion the writer ultimately defends. Do not select a vivid sentence simply because it sounds decisive.",
            "A nuanced thesis may distinguish circumstances rather than choose one universal rule. Preserve that distinction when summarizing it. Reducing a conditional position to a simple yes or no can misrepresent the argument and distort how its evidence works.",
            "Test your reading against the whole text. The central position should account for the main reasons and qualifications. If your summary makes a major section seem inexplicable, revisit the thesis rather than assuming the section is irrelevant.",
        ),
        example="An essay describes the convenience of recorded lectures, acknowledges the value of live discussion, and concludes that recordings should supplement courses rather than replace every meeting. Its final section explains which activities depend on immediate exchange.",
        walkthrough="The position combines support for recordings with a limit on replacement. The live-discussion section develops that limit. A summary saying the writer rejects recordings would ignore their stated benefit, while a summary endorsing complete replacement would erase the conclusion's condition.",
        prompt="A critic praises digital restorations for revealing faded details but argues that exhibitions should also explain which colors were reconstructed. Which summary best captures the position?",
        options=("Restoration can be valuable when viewers are informed about its interpretive choices", "Every reconstruction is deceptive and should be prohibited", "Restored colors should always be presented as certain historical facts"),
        feedback=("Yes. This preserves both the benefit and the condition the critic develops.", "The critic's praise is inconsistent with an absolute rejection of restoration.", "The request for explanation acknowledges interpretive choices rather than treating every reconstruction as certain."),
        correct=0,
    ),
    Lesson(
        slug="revise-a-thesis-with-evidence", title="Let the evidence refine the thesis", skill="4.B",
        objective="Revise a thesis when evidence reveals a meaningful limit or distinction.",
        explanation=(
            "A working thesis guides investigation, but it need not survive unchanged. If credible evidence complicates your position, identify exactly what needs revision: scope, cause, condition, or recommendation. Changing a claim to fit evidence is part of reasoning, not an admission that argument is impossible.",
            "Avoid two extremes: ignoring inconvenient evidence and retreating to an empty statement that everything is complicated. A revised thesis should still take a position. Name the condition or distinction that explains why the evidence supports this particular conclusion.",
            "After revising, check the body paragraphs. They may need new commentary or a different order to support the refined claim. A qualified thesis paired with paragraphs that still make universal claims creates an unresolved inconsistency.",
        ),
        example="A draft argues that every archive item should be digitized immediately. Evidence about fragile materials, limited staffing, and frequent requests leads to a revised thesis favoring phased digitization that prioritizes demand and preservation needs while maintaining access to uncopied materials.",
        walkthrough="The revision keeps a commitment to digitization but develops criteria for its sequence and scope. It responds to practical evidence rather than adding a vague sometimes. The argument must now support those criteria and explain tradeoffs among them.",
        prompt="A draft favors replacing every textbook with digital materials. Evidence shows benefits for search and updating but uneven device access. Which revision responds most directly?",
        options=("Digital materials are interesting, and education has many challenges", "Expand digital materials where they improve use while retaining accessible alternatives until reliable access is provided", "Replace every textbook because contrary evidence should not change a thesis"),
        feedback=("This avoids the actual decision rather than refining the position in light of the evidence.", "Yes. The claim retains the identified benefits while addressing a concrete condition that limits universal replacement.", "A defensible argument must respond to relevant evidence, not protect its first wording from revision."),
        correct=1,
    ),
    Lesson(
        slug="trace-a-shift-in-tone", title="Trace a shift in tone", skill="7.A",
        objective="Explain how changes in diction or comparison develop a writer's attitude and purpose.",
        explanation=(
            "Tone can change within a text. Mark where the language shifts and identify the choices that establish the difference. A move from playful exaggeration to restrained description may change how readers understand an experience or judgment.",
            "Use precise evidence before choosing a label. Look at verbs, comparisons, evaluative adjectives, and what the writer emphasizes. Two different topics do not automatically establish a tonal shift, and a single emotional word may not characterize the entire passage.",
            "Explain the shift's function. It may complicate an earlier attitude, prepare readers for a serious claim, or distinguish remembered experience from later reflection. Avoid saying only that the shift keeps readers interested when the text supports a more specific account.",
        ),
        example="An original travel essay first calls the narrator's overpacked suitcase 'a small traveling kingdom.' After a porter struggles to lift it, the narrator describes its weight plainly and reflects on expecting others to manage the consequences of personal excess.",
        walkthrough="The playful comparison initially treats overpacking as comic. The restrained description and reflection make its effect on another person harder to dismiss. The shift develops self-criticism; it does not require claiming that the narrator has rejected all travel or belongings.",
        prompt="A memoir moves from joking about a relative's repetitive stories to carefully recalling one story's details after the relative's death. What interpretation is most supported?",
        options=("The narrator's jokes prove the relative's stories never mattered", "The change establishes that the remembered details are historically infallible", "The more attentive language suggests a revised appreciation of stories once treated casually"),
        feedback=("The later attention complicates the earlier casual attitude rather than confirming permanent indifference.", "A respectful tone does not guarantee factual accuracy in memory.", "Yes. The contrast in treatment supports a change in the narrator's valuation of those stories."),
        correct=2,
    ),
    Lesson(
        slug="revise-tone-without-losing-force", title="Revise tone without losing the argument", skill="8.A",
        objective="Choose forceful, accurate language that addresses disagreement without misrepresenting it.",
        explanation=(
            "A strong position does not require attacking the intelligence or motives of everyone who disagrees. Identify the claim you dispute and the evidence that challenges it. Specific criticism gives readers something to evaluate; contempt can obscure the reasoning.",
            "Match intensity to what the evidence establishes. Words such as disastrous, fraudulent, or inevitable make substantial claims. If the evidence shows a narrower concern, describe that concern precisely. Restraint can sharpen an argument by removing assertions the writer cannot defend.",
            "Revision need not erase voice or urgency. Use concrete consequences, active verbs, and a clear recommendation. Acknowledge an opposing concern accurately, then explain why another consideration outweighs it or how the proposal addresses it.",
        ),
        example="Draft: 'Only people who hate readers would shorten library hours.' Revision: 'Reducing evening hours would remove the only available study period for some shift workers; the budget discussion should consider alternatives that preserve that access.'",
        walkthrough="The revision replaces an invented motive with a consequence and a request. It remains critical of the proposed cut while allowing readers to assess the access concern. The claim about workers still needs supporting evidence; respectful language does not substitute for it.",
        prompt="Which revision makes the most precise criticism of a report that draws a national conclusion from one town's data?",
        options=("The national conclusion exceeds the geographic scope of the evidence presented", "The authors are obviously incapable of understanding any evidence", "The report should be ignored because all local data are useless"),
        feedback=("Yes. This identifies the inferential problem without inventing motives or dismissing local evidence altogether.", "This personal attack does not explain the mismatch between the data and the conclusion.", "Local data can support local claims or further investigation. The problem is the unsupported national extension."),
        correct=0,
    ),
)

QUALIFICATION_AND_SENTENCES = (
    Lesson(
        slug="recognize-competing-purposes", title="Recognize competing demands in a situation", skill="1.A",
        objective="Explain how a writer responds to an audience with more than one concern.",
        explanation=(
            "A writer may need to reassure readers while asking them to change, or acknowledge a loss while defending a decision. Identify these demands through the occasion and language. Do not assume every sentence serves an identical immediate purpose.",
            "Explain how the moves work together. Acknowledging inconvenience can establish that a request takes readers' experience seriously. It does not necessarily withdraw the request or guarantee agreement. Keep your interpretation tied to the specific audience and circumstances.",
        ),
        example="A curator announces a gallery closure for conservation. She acknowledges visitors who planned trips, explains the damage that continued display could cause, and identifies other ways to view the collection during repairs.",
        walkthrough="The announcement must explain a restriction and respond to disappointed visitors. Acknowledgment and alternatives support that response, while the conservation explanation supplies the reason for closing. The text need not claim the alternatives fully replace the visit.",
        prompt="A director thanks volunteers before explaining why a familiar event must change its schedule. What is the most supported function of the thanks?",
        options=("It recognizes their investment before introducing a potentially unwelcome change", "It proves every volunteer already supports the new schedule", "It makes an explanation of the change unnecessary"),
        feedback=("Yes. Recognition can help address the audience's relationship to the event before the change is discussed.", "Thanks does not establish agreement; the schedule may still need justification.", "Acknowledgment can accompany reasons but cannot replace the explanation readers need."), correct=0,
    ),
    Lesson(
        slug="frame-a-qualified-position", title="Frame a qualified position from beginning to end", skill="2.A",
        objective="Use an opening and conclusion to preserve the argument's central tension.",
        explanation=(
            "When an argument weighs competing concerns, an opening can establish the decision without pretending one concern does not exist. Introduce only the context needed to understand the tension and the position you will develop.",
            "A conclusion should reflect the reasoning actually completed. If the body supports a conditional recommendation, do not end with an unconditional slogan. Draw out the warranted implication and identify the condition that remains important.",
        ),
        example="An essay on displaying fragile letters opens with the tension between public access and preservation. After comparing viewing arrangements, it concludes that short display periods paired with readable reproductions can expand access while limiting exposure of the originals.",
        walkthrough="The conclusion responds to the tension established at the start. It proposes a specific balance rather than claiming that preservation or access no longer matters. The body must supply evidence for the proposed arrangement.",
        prompt="An essay supports a pilot only if its costs are monitored. Which ending preserves that position?",
        options=("The pilot deserves unlimited expansion immediately", "Begin the pilot with regular cost reviews before deciding whether to expand", "Because costs exist, no trial can ever be justified"),
        feedback=("Immediate unlimited expansion removes the condition the essay defended.", "Yes. The ending carries the stated condition into the proposed action.", "This reverses the argument without showing why the conditional trial is untenable."), correct=1,
    ),
    Lesson(
        slug="read-concessions-carefully", title="Distinguish concession from surrender", skill="3.C",
        objective="Explain how a writer acknowledges a competing perspective while retaining or revising a claim.",
        explanation=(
            "A concession accepts a point without necessarily accepting every conclusion attached to it. Identify exactly what the writer grants and what remains disputed. Although and even if can help signal this relationship, but the reasoning matters more than any single word.",
            "A qualification narrows a claim's scope or specifies conditions. It can respond to a valid objection while preserving a defensible position. Avoid describing every acknowledgment of difficulty as a complete reversal.",
        ),
        example="A reviewer writes, 'The translation loses some of the original rhythm, but its clear notes make unfamiliar references accessible to new readers.'",
        walkthrough="The reviewer concedes a limitation and retains a favorable judgment about another feature. The sentence does not establish that rhythm is unimportant or that notes eliminate the loss. It weighs distinct considerations.",
        prompt="A writer states, 'The program is expensive, yet its benefits may justify a smaller trial.' What position is retained?",
        options=("The program has no meaningful costs", "The program must operate at its original full scale", "A limited trial may be warranted despite the acknowledged cost"),
        feedback=("The cost is explicitly acknowledged.", "The smaller trial qualifies the scale rather than preserving the original size.", "Yes. The writer grants a concern while proposing a narrower course of action."), correct=2,
    ),
    Lesson(
        slug="answer-the-strong-objection", title="Answer the objection your argument actually faces", skill="4.C",
        objective="Represent a competing claim fairly and respond with reasoning rather than dismissal.",
        explanation=(
            "Choose an objection that challenges a real premise, consequence, or priority in your argument. A weak caricature is easy to reject but leaves the substantive concern unanswered. State the opposing position in terms its reasonable supporters could recognize.",
            "Decide whether evidence rebuts the objection, whether a concession is appropriate, or whether your claim needs a condition. Your response should explain why the central position remains justified after the concern is considered.",
        ),
        example="A proposal for extended museum hours faces a staffing objection. Instead of accusing critics of opposing access, the writer proposes a limited evening schedule, identifies staffing costs, and explains how attendance and cost will be reviewed.",
        walkthrough="The response treats staffing as a practical constraint and adjusts the proposal. It still needs credible cost evidence. Merely saying access is valuable would not answer whether the plan can be staffed.",
        prompt="A critic argues that an outdoor event plan lacks an accessible route. Which response most directly addresses the objection?",
        options=("Revise the layout to provide an accessible route and explain how it will be checked before opening", "Describe the critic as someone who dislikes outdoor events", "Repeat that the event will be enjoyable without discussing the route"),
        feedback=("Yes. This responds to the specific access issue with an actionable revision and verification.", "An invented motive does not address the layout's accessibility.", "Enjoyment does not resolve the route problem identified by the critic."), correct=0,
    ),
    Lesson(
        slug="analyze-sentence-emphasis", title="Explain how sentence structure directs emphasis", skill="7.B",
        objective="Connect clause arrangement and sentence length to a specific rhetorical effect.",
        explanation=(
            "Sentence structure can foreground a claim, delay it, or place it beside a qualification. Identify the main clause and the relationship of other clauses to it. Do not assume every long sentence is complex in thought or every short sentence is emphatic in the same way.",
            "Read the sentence within its surroundings. A brief sentence after a sequence of detail can create a pause or focus attention on a conclusion. Explain which idea receives emphasis and how that emphasis serves this passage.",
        ),
        example="A memoir lists the narrator's attempts to locate a missing photograph: searching drawers, calling relatives, and sorting boxes. The paragraph ends, 'Then I stopped searching.'",
        walkthrough="The short final sentence contrasts with the accumulated activity and marks a change in action. Its significance depends on what follows; it does not by itself establish whether the narrator feels relief, despair, or something else.",
        prompt="In 'Although the route is longer, it avoids the steep stairs,' which idea occupies the main clause?",
        options=("The route is longer", "The route avoids the steep stairs", "The route has no disadvantages"),
        feedback=("The although clause acknowledges that point in a subordinate position.", "Yes. Avoiding the stairs receives the main-clause emphasis while length remains a concession.", "The sentence explicitly recognizes a drawback, so it does not claim there are none."), correct=1,
    ),
    Lesson(
        slug="revise-clause-relationships", title="Make sentence structure reflect the intended relationship", skill="8.B",
        objective="Revise clauses to express contrast, cause, or emphasis clearly and accurately.",
        explanation=(
            "Before combining sentences, identify how their ideas relate. Coordination can place ideas alongside one another; subordination can mark a concession, reason, or condition. Combining sentences is useful when it clarifies that relationship, not simply because longer sentences seem more advanced.",
            "Keep modifiers close to what they describe and make the actor clear. After revision, check whether the grammar implies a cause or condition you did not intend. Preserve the evidence's limits while improving flow.",
        ),
        example="Draft: 'The recording is incomplete. It preserves the opening speech.' Revision: 'Although the recording is incomplete, it preserves the opening speech.'",
        walkthrough="The revision makes incompleteness a concession and emphasizes the recording's remaining value. Because would create a different, unsupported causal relationship. Neither version establishes what else the recording contains.",
        prompt="Which revision clearly expresses a contrast without implying causation?",
        options=("Because the room is small, its acoustics are excellent", "The room is small, its acoustics are excellent", "Although the room is small, its acoustics are excellent"),
        feedback=("Because attributes the acoustics to size; that is a causal claim rather than the requested contrast.", "This joins two independent clauses with only a comma and leaves their relationship implicit.", "Yes. Although marks the contrast while the main clause emphasizes the positive acoustic judgment."), correct=2,
    ),
    Lesson(
        slug="read-punctuation-as-meaning", title="Explain what punctuation does in context", skill="7.C",
        objective="Analyze how punctuation separates, introduces, or emphasizes ideas.",
        explanation=(
            "Punctuation helps readers interpret relationships and pacing. A colon can introduce an explanation or specification after a complete clause; a semicolon can link closely related independent clauses. Dashes and parentheses can set off material with different degrees of interruption or emphasis in context.",
            "Do not assign a fixed emotion to a mark. Explain what the punctuation does to these words in this sentence. Replacing a mark may preserve the basic information while changing how the reader encounters it.",
        ),
        example="An essay states, 'The collection lacked one essential feature: a record of where the objects came from.'",
        walkthrough="The complete clause creates an expectation that the colon's following phrase fulfills. The specification identifies provenance as the missing feature. The colon does not add evidence proving why the records are absent.",
        prompt="In 'The door was open; no one entered,' what does the semicolon most directly accomplish?",
        options=("It links two complete clauses closely while allowing readers to notice the contrast", "It proves that the open door caused everyone to stay outside", "It marks the second clause as a quotation from another speaker"),
        feedback=("Yes. Both clauses can stand independently; their close placement makes the unexpected relationship available for interpretation.", "The mark does not establish a causal explanation for the lack of entry.", "A semicolon does not attribute speech or mark quoted material."), correct=0,
    ),
    Lesson(
        slug="edit-conventions-in-context", title="Edit punctuation without changing the claim", skill="8.C",
        objective="Choose a grammatically sound sentence that preserves the intended relationship and scope.",
        explanation=(
            "Editing requires more than locating a possible pause. Identify complete clauses, dependent clauses, and the relationships between them. Two independent clauses cannot normally be joined by a comma alone; a conjunction, semicolon, or period can resolve the boundary depending on the intended connection.",
            "Check meaning after fixing form. Adding because may repair a sentence boundary but introduce an unsupported cause. A colon needs an appropriate grammatical setup. Preserve distinctions such as which people or objects a modifying phrase identifies.",
        ),
        example="Draft: 'The archive is open, appointments are required.' Revision: 'The archive is open, but appointments are required.' Another grammatical option is 'The archive is open; appointments are required.'",
        walkthrough="Both revisions repair the comma splice. But explicitly presents the appointment rule as a limitation on access; the semicolon leaves the relationship less explicit. Neither claims that opening the archive causes the appointment requirement.",
        prompt="Which revision repairs the sentence boundary while explicitly retaining the contrast: 'The scan is clear, the original is faded'?",
        options=("The scan is clear, the original is faded", "The scan is clear, but the original is faded", "Because the scan is clear, the original is faded"),
        feedback=("This retains the comma splice between two independent clauses.", "Yes. The coordinating conjunction repairs the boundary and explicitly signals contrast.", "This is grammatical but introduces an unsupported causal relationship instead of the intended contrast."), correct=1,
    ),
)

AUDIENCE_AND_VOICE = (
    Lesson(
        slug="infer-shared-knowledge", title="Infer what readers are expected to know", skill="1.B",
        objective="Use explanation and omission as evidence of a writer's assumptions about readers.",
        explanation=(
            "Writers make decisions about what needs explaining. An unexplained technical term may suggest a specialist audience, while an analogy or definition can make a concept available to newcomers. Treat these as clues, not proof that every reader has the same knowledge.",
            "Look for multiple signals: the publication context, direct address, examples, and level of detail. Distinguish assumed knowledge from shared values. Readers might understand a technical process without agreeing about how it should be used.",
        ),
        example="An original astronomy article defines a telescope's aperture as the opening that gathers light, then compares two instruments using the amount of light each can collect. It avoids assuming readers already know the technical term.",
        walkthrough="The definition and concrete comparison support an inference that the article welcomes nonspecialists. They do not show that every reader is a beginner or that technical accuracy is unimportant.",
        prompt="A guide explains an unfamiliar abbreviation on first use but then uses it throughout. What is the best-supported audience inference?",
        options=("The writer expects all readers to reject technical language", "The writer assumes readers cannot learn new terminology", "The writer accommodates readers who may not initially know the abbreviation"),
        feedback=("Explaining a term makes it usable; it does not establish opposition to technical language.", "Later use of the abbreviation expects readers to apply the explanation.", "Yes. The introduction supplies knowledge that readers can then use in the rest of the guide."), correct=2,
    ),
    Lesson(
        slug="adapt-an-explanation", title="Adapt an explanation while preserving its meaning", skill="2.B",
        objective="Revise background and examples for readers with different levels of familiarity.",
        explanation=(
            "Changing audiences often requires changing the route into an idea. Identify what the new audience needs to understand before it can evaluate your point. Define necessary terms, choose a relevant example, and retain qualifications that affect meaning.",
            "Do not confuse accessibility with removing uncertainty or replacing a claim with a slogan. An analogy can help, but explain its relevant feature. Specialists and general readers both deserve an accurate account of what is known and what remains unresolved.",
        ),
        example="A technical report says a result has considerable measurement uncertainty. A public summary explains that repeated measurements may vary within a stated range, rather than describing the finding as either exact or worthless.",
        walkthrough="The revision explains a technical limitation without erasing it. The report's method and range still matter; plain language should make them interpretable rather than imply certainty the evidence lacks.",
        prompt="Which revision best prepares general readers to understand an archive's metadata?",
        options=("Define metadata as information describing an item, such as its date and creator, before explaining how those details support searches", "Delete every reference to dates and creators because the term is technical", "Replace metadata with a claim that the archive can answer every question instantly"),
        feedback=("Yes. The definition and examples establish a useful basis for understanding the search function.", "Removing relevant details would weaken the explanation instead of making it clearer.", "This introduces an unsupported promise and loses the original meaning."), correct=0,
    ),
    Lesson(
        slug="analyze-patterns-in-diction", title="Read a pattern of words, not an isolated label", skill="7.A",
        objective="Explain how related word choices develop a perspective across a passage.",
        explanation=(
            "A pattern of diction can sustain an attitude or frame an idea. Look for words that share associations, but check whether each contributes to the interpretation. One word alone may have several plausible meanings; a pattern can help distinguish them.",
            "Explain what the pattern encourages readers to notice. Language of cultivation might represent learning as gradual work, while language of competition could foreground ranking. These frames are interpretations to support with context, not universal meanings attached to a vocabulary list.",
        ),
        example="A reflective essay describes learning a craft through 'small repairs,' 'patient adjustments,' and 'work returned to the bench.' The recurring language presents improvement as iterative effort rather than sudden perfection.",
        walkthrough="The terms work together to emphasize revision and persistence. The interpretation does not require claiming that the writer rejects talent entirely; the passage foregrounds a process without resolving every cause of achievement.",
        prompt="A critic calls a building 'a conversation with its surroundings' and describes its windows as 'answering' neighboring rooflines. What shared effect do the comparisons most directly support?",
        options=("They establish that buildings can literally hear speech", "They portray design as responding to an existing environment", "They prove that all neighboring residents approve of the building"),
        feedback=("The language is figurative, not a claim about literal hearing.", "Yes. Both comparisons emphasize relationships between the building and surrounding forms.", "The description does not supply evidence about residents' opinions."), correct=1,
    ),
    Lesson(
        slug="sustain-an-appropriate-voice", title="Sustain a voice that fits the task", skill="8.A",
        objective="Revise inconsistent diction while preserving a clear, credible stance.",
        explanation=(
            "Voice emerges from repeated choices in diction, detail, and attitude. A shift can be purposeful, but accidental changes may distract from the argument. Compare the revision with the surrounding passage and the relationship you are establishing with readers.",
            "A formal voice need not be inflated, and a conversational voice need not be careless. Prefer precise language that fits the evidence. Keep quotations or clearly attributed voices distinct from your own so readers know whose attitude they are hearing.",
        ),
        example="A measured exhibition review discusses lighting and placement, then calls one room 'the greatest thing ever.' A revision describes how the room's arrangement allows visitors to compare sketches with finished works.",
        walkthrough="The revision preserves a positive evaluation but gives readers a concrete reason for it. It fits the surrounding analytical voice better than an unsupported superlative. Enthusiasm can remain when its basis is explained.",
        prompt="Which sentence best fits a careful review that has praised a film's editing while acknowledging uneven pacing?",
        options=("The editing often clarifies shifts in perspective, though several transitions slow the middle section", "This film is perfect in every possible way", "Anyone who dislikes the film clearly understands nothing"),
        feedback=("Yes. The sentence maintains the review's qualified evaluation and names a specific effect.", "This contradicts the acknowledged limitation and substitutes a universal judgment.", "Attacking readers supplies no analysis of the editing or pacing."), correct=0,
    ),
    Lesson(
        slug="analyze-parallel-structure", title="Explain how parallel structure organizes emphasis", skill="7.B",
        objective="Connect repeated grammatical patterns to relationships among ideas.",
        explanation=(
            "Parallel structure places related elements in similar grammatical forms. It can make a sequence easier to follow, emphasize a shared category, or sharpen a contrast. Identify what the pattern groups together and why that grouping matters here.",
            "Repetition alone does not establish agreement, causation, or truth. Examine the content within the pattern. A writer may use similar forms to contrast different commitments, and the resulting rhythm still needs interpretation in relation to purpose.",
        ),
        example="A speaker describes a community archive as a place 'to preserve records, to question memories, and to share discoveries.' The repeated infinitive phrases give three activities a coordinated role in the institution's purpose.",
        walkthrough="The pattern makes the activities easy to compare and resists reducing the archive to storage alone. It does not establish that every activity receives equal funding or produces equally successful results.",
        prompt="What does the parallel form in 'We can document the loss; we can examine its causes; we can prevent its repetition' most directly do?",
        options=("It proves that prevention is guaranteed", "It makes the three activities logically identical", "It presents related actions in a clear, cumulative sequence"),
        feedback=("The form emphasizes possibility and action but does not prove the outcome.", "The actions differ even though their grammatical structures match.", "Yes. Repeated structure connects the actions while the verbs move from recording toward response."), correct=2,
    ),
    Lesson(
        slug="revise-for-clear-agency", title="Make the actor and emphasis clear", skill="8.B",
        objective="Revise sentence structure to clarify who acts and what the reader should focus on.",
        explanation=(
            "Choose active or passive voice according to what the sentence needs to foreground. Active voice can identify responsibility directly; passive voice can appropriately foreground a recipient or process when the actor is unknown or less relevant. Neither choice is automatically better in every context.",
            "Check modifiers and pronouns for clear attachment. A phrase describing an action should connect to the person or thing performing it. If a revision changes who acted or implies information not in the source, it has changed more than style.",
        ),
        example="Draft: 'After reviewing the records, several errors were found.' Revision: 'After reviewing the records, the archivist found several errors.'",
        walkthrough="The revision names the actor who reviewed and found, correcting the awkward implication that the errors performed the review. If the actor is unknown, another revision can avoid invention: 'A review of the records revealed several errors.'",
        prompt="Which revision clearly identifies who made the decision without changing the stated facts: 'The committee reviewed the proposals. The committee selected two finalists'?",
        options=("After reviewing the proposals, two finalists selected the committee", "After reviewing the proposals, the committee selected two finalists", "The proposals reviewed the committee and selected two finalists"),
        feedback=("This makes the finalists the actor and reverses the decision relationship.", "Yes. The introductory phrase attaches to the committee, preserving its role in both actions.", "This incorrectly makes the proposals perform the review and selection."), correct=1,
    ),
)

QUALIFIED_ARGUMENTS = (
    Lesson(
        slug="evaluate-the-final-qualification", title="Evaluate whether a qualification resolves the objection", skill="3.C",
        objective="Assess whether a writer's concession and response adequately support the revised claim.",
        explanation=(
            "A qualification should address the actual challenge to a claim. Identify the objection's target: cost, fairness, evidence, feasibility, or another premise. Then ask whether the response changes the relevant part of the argument or merely acknowledges the concern in passing.",
            "A concession does not automatically make an argument balanced or sufficient. The writer still needs evidence for the retained position. Distinguish a condition that could be checked from vague reassurance that everything will work out.",
        ),
        example="A proposal promises a service for everyone. After evidence of uneven internet access, it adds, 'Some access problems may occur,' but still requires online registration without an alternative.",
        walkthrough="The acknowledgment names a concern but does not resolve the mismatch between universal access and the registration requirement. A meaningful revision would need to address registration access or narrow the promise, with evidence about the result.",
        prompt="Which qualification most directly responds to evidence that a pilot's success depended on additional staff?",
        options=("The model may transfer where comparable staffing can be provided; expansion should account for that requirement", "The pilot succeeded, so staffing details never matter", "There are many opinions about pilots, so no conclusion is possible"),
        feedback=("Yes. This identifies a relevant condition and ties the expansion claim to it.", "This dismisses the condition raised by the evidence rather than addressing it.", "Uncertainty calls for a suitably limited conclusion, not necessarily abandonment of all inference."), correct=0,
    ),
    Lesson(
        slug="compose-a-qualified-recommendation", title="Build a recommendation that survives its limits", skill="4.C",
        objective="Integrate evidence, an important objection, and a specific condition into a defensible position.",
        explanation=(
            "Bring the argument's pieces together: state the position, identify the strongest relevant support, and address a serious limitation. A useful qualification explains where or when the recommendation applies. It should sharpen the claim rather than bury it beneath indecision.",
            "Check the relationship among the final thesis, body, and conclusion. If the response to an objection changes the proposed action, carry that change through the whole argument. Retain unresolved uncertainty openly and explain what further evidence or evaluation would affect the decision.",
            "Before drafting, try a short plan: position, support, objection, response, and implication. This is a thinking aid, not a required paragraph formula. In the completed essay, use the order and emphasis that make your reasoning clearest to readers.",
        ),
        example="A writer recommends public access to digitized oral histories. Evidence supports educational value, but interviews include sensitive personal material. The revised recommendation prioritizes recordings whose permissions support release, explains review of sensitive content, and identifies access alternatives where public release is inappropriate.",
        walkthrough="The revision retains an access goal while responding to a concrete limitation. It avoids claiming that educational value alone resolves every release decision. Its safeguards still need a clear process and support; naming a condition does not prove it will be implemented well.",
        prompt="An argument favors extending a successful small reading program. Evidence shows benefits but leaves costs at larger scale uncertain. Which position is best supported?",
        options=("Expand without limits because success at one scale proves success at every scale", "Expand in stages while measuring costs and outcomes before committing to the full proposed scale", "Close the program because an unanswered cost question disproves every reported benefit"),
        feedback=("The evidence does not establish performance or affordability at every scale.", "Yes. The recommendation uses the observed benefits while making further commitment depend on evidence about the unresolved issue.", "The uncertainty concerns expansion costs; it does not automatically invalidate the observed benefits."), correct=1,
    ),
)


def lessons_for(code: str, unit_order: int) -> tuple[Lesson, ...]:
    if code == "us-history":
        return {2: HISTORY_SOURCE_PURPOSE, 8: HISTORY_IMPLEMENTATION + HISTORY_CAUSATION,
                9: HISTORY_DEMOGRAPHY}.get(unit_order, ())
    if code != "english-language":
        return ()
    return {1: FOUNDATIONS, 2: AUDIENCE_AND_THESIS, 3: REASONING_AND_DEVELOPMENT,
            4: PURPOSE_AND_STRUCTURE, 5: COHERENCE_AND_STYLE,
            6: SOURCES_AND_REFINEMENT, 7: QUALIFICATION_AND_SENTENCES,
            8: AUDIENCE_AND_VOICE, 9: QUALIFIED_ARGUMENTS}.get(unit_order, ())


HISTORY_DEMOGRAPHY = (
    Lesson(
        slug="read-population-evidence", title="Read population evidence precisely",
        skill="claims-evidence", practice_tag="ced:9.5", example_kind="historical",
        objective="Distinguish a population share from an arrival rate before making a historical claim.",
        explanation=(
            "Identify the population, date, and unit of measurement first. A percentage of residents describes who lived in a place at a particular time. It does not tell you how many people arrived during that year. Foreign-born residents may have arrived decades earlier.",
            "Compare like measures. Subtracting two percentages gives a change in percentage points. Explaining that change requires more evidence: arrivals, departures, deaths, and changes in the total population can affect a population share.",
            "Keep a claim within the source's geographic scope. National figures cannot by themselves establish where immigrants settled, why they moved, or how they experienced their new communities. Pair demographic patterns with regional records and accounts of experience.",
        ),
        example="Census historical figures show that foreign-born residents represented 7.9 percent of the U.S. population in 1990 and 11.1 percent in 2000. Source: Census Bureau, Historical Census Statistics on the Foreign-Born Population, 1850–2000 (2006).",
        walkthrough="The share increased by 3.2 percentage points. This supports a claim about the changing composition of the resident population. It does not mean that 11.1 percent of residents arrived in 2000, or identify the region receiving the most new arrivals.",
        prompt="A hypothetical regional census reports that foreign-born residents were 8 percent of the population in 1980 and 12 percent in 2000. Which conclusion follows from these figures alone?",
        options=("Twelve percent of the population immigrated during 2000", "The foreign-born share rose by four percentage points", "The region received more immigrants than any other region"),
        feedback=("The figure describes residents at the census date, including people who arrived earlier.", "Yes. Subtracting 8 from 12 gives four percentage points; the figures do not establish arrivals or comparisons with other regions.", "That comparison requires evidence from other regions, which the source does not provide."),
        correct=1,
    ),
)


HISTORY_SOURCE_PURPOSE = (
    Lesson(
        slug="source-purpose-and-limits", title="Explain a document's purpose and limits",
        skill="sourcing", practice_tag="ced:2.3", example_kind="historical",
        objective="Connect a document's purpose to a supported historical claim without inventing participation rights.",
        explanation=(
            "Start with the document's creator, setting, audience, and intended action. A governing agreement can tell you what its signers promised and how they justified authority. Its existence alone does not establish how every inhabitant participated in government.",
            "Explain why the source's situation matters to your claim. Naming a date or saying that a document is biased is not enough. Identify the commitment or perspective visible in its wording, then explain what it helps establish and what needs corroboration.",
        ),
        example="The Mayflower Compact (1620) describes its signers as loyal subjects of King James while agreeing to form a civil political association for collective order. Original summary based on Yale's Avalon transcription.",
        walkthrough="The agreement supports a claim about local institution-building within an English colonial setting. Its expression of loyalty cautions against treating it as a declaration of independence. Its collective language does not establish voting rights for every person affected by colonial government.",
        prompt="A historian uses the compact to argue that the settlers organized local government. Which extension of that argument requires additional evidence?",
        options=("The agreement expressed a commitment to collective order", "The signers described themselves as subjects of the king", "All inhabitants had equal access to voting and officeholding"),
        feedback=("The agreement's stated purpose directly supports collective ordering.", "The description of royal loyalty appears in the document itself.", "Yes. A claim about everyone's participation requires evidence of eligibility and actual practice, beyond the signers' agreement."), correct=2,
    ),
)

HISTORY_IMPLEMENTATION = (
    Lesson(
        slug="rights-and-implementation", title="Separate a legal change from its implementation",
        skill="comparison", practice_tag="ced:8.6", example_kind="historical",
        objective="Compare a constitutional ruling with evidence about institutions and lived outcomes.",
        explanation=(
            "A legal decision establishes a ruling about rights or authority. It is important evidence of institutional change, but it is not a direct measurement of every institution's subsequent behavior. Distinguish what the decision required from how, when, and where it was implemented.",
            "Build the comparison with sources suited to each question. Read a judicial opinion for its reasoning and scope; examine enrollment records, local orders, enforcement actions, and community accounts for implementation. Resistance does not mean the ruling never occurred, and the ruling does not mean resistance immediately ended.",
        ),
        example="Brown v. Board of Education (1954) held state-sanctioned segregation in public schools unconstitutional under the Fourteenth Amendment. Disputes and resistance over implementation followed. Original summary based on the National Archives' Brown milestone document.",
        walkthrough="A historian can identify a major constitutional change while also explaining uneven implementation. School records across places and years help assess institutional change; testimony can illuminate experiences that enrollment totals alone miss.",
        prompt="Which evidence best tests whether a particular district changed enrollment practices after Brown?",
        options=("District enrollment and assignment records before and after the ruling, checked against enforcement records", "The date of the Supreme Court decision by itself", "A later commemorative speech praising the decision without discussing the district"),
        feedback=("Yes. Local records over time address actual practices; enforcement evidence helps explain their timing and limits.", "The date establishes chronology, not the district's response.", "Commemoration can reveal later memory, but this speech does not establish the district's enrollment practices."), correct=0,
    ),
)


HISTORY_CAUSATION = (
    Lesson(
        slug="explain-a-causal-mechanism", title="Explain how a cause could produce an effect",
        skill="causation", practice_tag="ced:8.2", example_kind="historical",
        objective="Build a causal explanation that identifies a mechanism and acknowledges competing influences.",
        explanation=(
            "Chronology is a starting point: a proposed cause must precede its effect. It is not the whole explanation. Identify the intervening process that connects the cause to the outcome, then choose evidence that could support or challenge that connection.",
            "Distinguish what policymakers expected from what happened. A speech can establish a stated rationale; it cannot alone measure a program's effects. To assess outcomes, compare changes over time and consider other conditions that could contribute to them.",
            "Use proportionate language. A policy may contribute to an outcome without being its sole cause. A strong explanation can weigh several factors and identify why one mattered in a particular setting rather than merely listing events.",
        ),
        example="In 1947 Marshall called for European reconstruction; Congress funded the recovery program in 1948. Supporters connected economic stabilization with limiting Communist influence. Original summary based on the State Department Office of the Historian's Marshall Plan account.",
        walkthrough="The proposed mechanism connects economic assistance to improved conditions, then to greater political stability. That describes the policy rationale. Establishing how much aid actually contributed requires economic and political evidence and consideration of other influences on recovery.",
        prompt="Which argument best explains a possible mechanism linking reconstruction aid to containment?",
        options=("Aid preceded later political developments, which proves it caused all of them", "Aid could improve economic conditions and strengthen governments, reducing the appeal of Communist movements", "Aid and containment appeared in the same speech, so they were identical policies"),
        feedback=("Sequence alone does not establish causation or exclude other influences.", "Yes. This connects assistance, economic conditions, and political stability while presenting a possible mechanism rather than a guaranteed outcome.", "Policies can serve a related goal through different instruments. Shared mention does not make them identical."), correct=1,
    ),
    Lesson(
        slug="weigh-multiple-policy-motives", title="Weigh motives without erasing consequences",
        skill="argumentation", practice_tag="ced:8.2", example_kind="historical",
        objective="Qualify a claim of exclusive motivation using relevant evidence about policy choices.",
        explanation=(
            "Separate motives, instruments, and consequences. A government may pursue security through economic assistance that also relieves suffering. Humanitarian benefits do not prove that humanitarian concern was the only motive; strategic motives do not erase those benefits.",
            "An exclusive claim is demanding: it rules out other meaningful motives. Test it with evidence from deliberations, speeches, funding decisions, and implementation. Different policymakers may emphasize different goals, so avoid assigning one uniform intention without support.",
        ),
        example="The Marshall Plan supported Western European reconstruction and markets for American goods while policymakers linked recovery to resistance to Communist influence. Original summary based on the State Department Office of the Historian's Marshall Plan account.",
        walkthrough="This evidence supports examining humanitarian, economic, and strategic objectives together. It challenges a claim of purely humanitarian motivation without implying that assistance provided no humanitarian benefit. Relative importance requires closer evidence about decisions and actors.",
        prompt="An essay says reconstruction aid was motivated only by humanitarian concern. Which revision best responds to evidence of strategic objectives?",
        options=("Aid could serve humanitarian and strategic purposes; evidence of decision-making is needed to weigh their importance", "Strategic objectives prove that nobody benefited from reconstruction", "Humanitarian benefits make policymakers' strategic statements irrelevant"),
        feedback=("Yes. The revision addresses the exclusive claim and identifies what further evidence can establish.", "A motive does not by itself determine whether recipients benefited.", "Benefits and intentions answer different questions. Strategic statements remain relevant to a claim about motives."), correct=0,
    ),
)
