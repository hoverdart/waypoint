"""Second independent revision form, focused on inference and rhetorical purpose."""
from .builders import passage_questions

RECIPE_PASSAGE = """(1) My aunt's recipe for flatbread contains a precise weight for flour and the instruction to add water “until the dough listens.” (2) When I first copied it into a notebook, I replaced that phrase with a measured quantity. (3) I thought I had rescued the recipe from vagueness. (4) On a dry winter afternoon, however, the measured dough cracked at the edges; in summer, the same quantity produced a sticky mass. (5) The number had made the instruction easier to repeat, but not necessarily easier to follow well.

(6) My aunt had not refused to explain her method. (7) She was describing a judgment that depended on texture, temperature, and the feel of the flour. (8) When I asked what listening meant, she pressed the dough with two fingers and showed me how slowly the indentation should rise. (9) She repeated the demonstration with a firmer piece, then asked me to compare them. (10) The lesson was less mysterious than the phrase had sounded, and more demanding than copying a number.

(11) Written recipes still have a purpose. (12) A beginner needs starting quantities, a sequence of steps, and warnings that do not depend on having an experienced cook in the room. (13) Yet a useful recipe should also say what to observe and what to change when conditions differ. (14) “Add another spoonful if the edges crack” teaches more than either an unexplained metaphor or a number presented as universal. (15) The best instructions make the writer's judgment available to someone who cannot borrow the writer's hands.

(16) I now keep both versions in my notebook. (17) The measured quantity remains, followed by descriptions of the dough at several stages and a note about the day I used unusually dry flour. (18) This does not turn every reader into an expert on the first attempt. (19) It does give the next attempt somewhere to begin. (20) My aunt says the longer recipe is good, though she still prefers to stand beside the person making it."""

RECIPE = passage_questions(passage_id='lang-b-recipe', title='Draft: Instructions for Listening', mode='writing',
    context='Original practice draft for a food magazine’s essay section. The narrator and events are fictional. Consider each proposed revision independently.', passage=RECIPE_PASSAGE, items=[
    (7, '2.A', 3, 'Which introductory sentence would best prepare readers for the essay’s concern with practical knowledge?', 1, [
        ('Flatbread appears in many cuisines and can be served with a variety of meals.', 'This introduces the food but not the essay’s inquiry into how instructions communicate judgment.'),
        ('I once believed that making an instruction more exact always made it more useful.', 'This introduces the assumption that the narrator’s experience will complicate.'),
        ('My notebook contains recipes from several relatives who live in different cities.', 'The family detail does not establish the central tension between precision and usefulness.'),
        ('A recipe is usually written before someone begins to cook from it.', 'The obvious sequence offers little reason to engage with the argument.'),
    ]),
    (4, '4.B', 4, 'Which revision of sentence 5 best states the insight developed by the whole essay?', 3, [
        ('The number was inaccurate, so written recipes should rely primarily on memorable images.', 'The essay keeps a starting quantity and clarifies the image rather than favoring metaphor over measurement.'),
        ('The recipe would succeed if the reader always cooked in exactly the same weather.', 'This avoids the need to teach adaptation and narrows the essay to conditions the reader cannot reliably control.'),
        ('The failed dough showed that skilled cooks should avoid instructions written for beginners.', 'The essay seeks better instructions for beginners rather than separating beginners from expertise.'),
        ('A useful instruction must offer a starting point and help the reader judge when an adjustment is needed.', 'This joins the value of measurement with the observational guidance developed in the later paragraphs.'),
    ]),
    (2, '4.A', 3, 'Which detail after sentence 8 would most directly develop the point about making tacit judgment observable?', 0, [
        ('She named the visible difference between dough that sprang back at once and dough that held a deep dent.', 'The detail explains how a felt judgment becomes a distinction the learner can observe.'),
        ('She had prepared flatbread for family gatherings since she was a teenager.', 'Experience may establish credibility, but this detail does not show how judgment is communicated.'),
        ('Her kitchen table stood close to a window overlooking the street.', 'The setting detail does not develop the explanation of dough texture.'),
        ('The notebook’s pages were ruled, with a wide margin for additional notes.', 'The physical notebook is less relevant than the demonstration’s instructional content.'),
    ]),
    (4, '6.C', 4, 'The writer wants to add a comparison after sentence 10. Which would best extend the reasoning?', 2, [
        ('Learning to cook is like winning a race because both are satisfying when completed.', 'The shared satisfaction does not illuminate how instructions teach judgment.'),
        ('A recipe is like a photograph because both can be stored for many years.', 'Durability does not explain the relationship between a starting rule and adaptive observation.'),
        ('A music teacher may mark a tempo while also demonstrating how a phrase should rise and settle.', 'The comparison combines a measurable starting point with modeled judgment, matching the recipe lesson.'),
        ('A shopping list is like a recipe because both contain the names of ingredients.', 'The resemblance concerns subject matter rather than the deeper instructional relationship.'),
    ]),
    (5, '6.A', 3, 'Which sentence would best follow sentence 12 to explain why the narrator retains a measured quantity?', 1, [
        ('Many cookbooks place ingredient lists before the steps of a recipe.', 'The convention does not explain why a beginner benefits from an initial measurement.'),
        ('A starting measure reduces the decisions a novice must make before learning what the dough should feel like.', 'This connects measurement to the learner’s limited experience while leaving room for later adjustment.'),
        ('Precise numbers appeal to readers because they look more authoritative on a page.', 'The essay does question apparent authority, but here the writer needs a genuine reason to retain measurements.'),
        ('My aunt has never needed to consult the notebook while she cooks.', 'Her expertise does not explain why the written quantity remains helpful to novices.'),
    ]),
    (5, '6.B', 4, 'The writer considers replacing “Yet” at the start of sentence 13 with “For example.” Which assessment is best?', 0, [
        ('Keep “Yet,” because the sentence adds a qualification to the benefits of basic instructions.', 'Sentence 13 identifies what starting quantities and steps alone do not provide; it is not merely an example of them.'),
        ('Use “For example,” because observing differences is identical to following a fixed sequence.', 'Observation and adjustment supplement a sequence; treating them as identical weakens the logical distinction.'),
        ('Keep “Yet,” because sentence 13 rejects every benefit listed in sentence 12.', 'The transition qualifies rather than cancels the earlier benefits.'),
        ('Use “For example,” because the essay has shifted entirely from argument to narrative.', 'The paragraph remains argumentative and explains the characteristics of useful instructions.'),
    ]),
    (5, '8.A', 3, 'Which replacement for sentence 15 best preserves its thoughtful tone and central idea?', 3, [
        ('The best recipes prove that good cooks always know more than their readers.', 'The sentence turns a claim about sharing judgment into an assertion of superiority.'),
        ('Readers should follow recipes exactly if they want results as good as the writer’s.', 'Exact repetition is the limitation the essay has been examining.'),
        ('Instructions are just vibes unless they are full of extremely precise numbers.', 'The casual phrasing and absolute opposition distort the measured argument.'),
        ('Good instructions help a distant reader recognize the choices an experienced cook would notice.', 'This retains the idea of making expertise available without the expert’s physical presence.'),
    ]),
    (7, '4.C', 3, 'Which sentence would best replace sentence 18 while maintaining an appropriate qualification?', 2, [
        ('With these notes, any reader will produce perfect bread every time.', 'The universal promise exceeds what the narrator’s experience can support.'),
        ('Because expertise takes time, descriptions cannot improve a beginner’s first attempts.', 'The need for practice does not imply that guidance has no benefit.'),
        ('The notes cannot replace practice, but they can help a beginner understand what went wrong.', 'This identifies a realistic limit and a specific benefit consistent with the essay.'),
        ('The notes are useful only to people whose kitchens are identical to my aunt’s.', 'The purpose of observational guidance is to support adaptation across different conditions.'),
    ]),
    (8, '8.B', 2, 'Which revision of sentence 17 most clearly keeps the starting measure and added observations distinct?', 1, [
        ('The measured quantity and the descriptions remain about the stages with a day in the flour.', 'The relationships among the quantity, observations, and example are obscured.'),
        ('I retain the starting quantity, then add descriptions of each stage and a note about using unusually dry flour.', 'The parallel actions clearly distinguish the retained measure from the added guidance.'),
        ('The quantity remains, which describes the flour at every stage of the day.', 'The relative clause incorrectly makes the quantity itself describe the changing stages.'),
        ('The measured quantity, descriptions, and dry flour all remain in the notebook.', 'The revision implies the flour itself is in the notebook and loses the example’s meaning.'),
    ]),
    (4, '2.A', 4, 'Which added final sentence would best build on the aunt’s preference in sentence 20 without reversing the essay’s argument?', 0, [
        ('The page can carry more of her knowledge now, even if it cannot carry the whole conversation.', 'This recognizes a limit of writing while preserving the improvement achieved through richer instructions.'),
        ('Her preference finally convinced me to stop writing recipes altogether.', 'That response abandons the value of written guidance developed in the essay.'),
        ('The next recipe in my notebook is for a soup that takes much longer to prepare.', 'The detail introduces a new subject without extending the present argument.'),
        ('I now know that demonstrations are useful only when written records are impossible.', 'The essay treats demonstration and writing as complementary rather than mutually exclusive.'),
    ]),
])

SLEEP_PASSAGE = """(1) A headline in our student newspaper recently declared that later school start times “cause better grades.” (2) The article described a survey of students at two schools with different start times. (3) Students at the later-starting school reported more sleep and had a higher average course grade. (4) These findings are worth discussing, but the headline asks them to do more work than the study permits.

(5) The students were not randomly assigned to schools. (6) The two schools also differed in transport arrangements, homework policies, and the way some courses were graded. (7) Any of these differences might help explain the pattern. (8) The association between start time and grades therefore cannot, on its own, identify the effect of changing the start time. (9) That limitation is not evidence that start times have no effect. (10) It is a reason to distinguish a promising question from an established answer.

(11) A responsible report should give readers enough information to make that distinction. (12) It should state how students were selected, how sleep was measured, and which alternative explanations were examined. (13) Readers do not need every technical detail in the opening paragraph. (14) They do need to know whether “more sleep” means a measured change over time or a difference between groups who may differ in other ways. (15) Our newspaper could make this clear without burying the finding beneath specialized vocabulary.

(16) Better headlines also leave room for action. (17) The school board may have reasons to consider a later start even while the effect on grades remains uncertain. (18) Students' alertness, family schedules, and bus costs matter too. (19) A headline should not decide that debate by turning one association into a guaranteed result. (20) It should invite readers to ask what the study shows, what remains unresolved, and what other evidence a decision requires."""

SLEEP = passage_questions(passage_id='lang-b-sleep', title='Draft: A Headline Ahead of the Evidence', mode='writing',
    context='Original practice draft by a fictional student science editor. The survey and schools are invented to illustrate research communication, not report actual findings.', passage=SLEEP_PASSAGE, items=[
    (8, '2.B', 3, 'The writer wants to address students who support later starts and may see criticism of the headline as opposition to that policy. Which addition after sentence 4 is best?', 2, [
        ('Students who favor the policy are unlikely to understand research methods.', 'The dismissive claim alienates the audience and confuses policy preferences with competence.'),
        ('The newspaper should avoid discussing school policies until every uncertainty is resolved.', 'The essay supports informed discussion under uncertainty, not silence.'),
        ('Questioning the headline does not require rejecting the proposal; it helps us give the proposal an honest hearing.', 'The sentence separates scrutiny of evidence from opposition to a policy, directly addressing the audience’s likely concern.'),
        ('A later start would certainly improve every aspect of student life.', 'The assurance repeats the kind of unwarranted certainty the essay criticizes.'),
    ]),
    (6, '4.A', 4, 'Which additional detail after sentence 6 would best illustrate a plausible alternative explanation for the grade difference?', 0, [
        ('One school allowed students to revise assignments for a higher mark, while the other generally did not.', 'A grading-policy difference could influence reported grades independently of start time.'),
        ('Both schools had a library and a gymnasium.', 'A shared feature does not explain the between-school difference described.'),
        ('The newspaper printed the article on its front page.', 'Article placement cannot explain the earlier difference in student grades.'),
        ('Students at both schools said they sometimes felt tired.', 'This shared general experience does not identify a specific alternative explanation for the grade difference.'),
    ]),
    (7, '4.C', 4, 'Which replacement for sentence 8 makes the most justified claim from the described study?', 3, [
        ('The association proves that changing either school’s start time will change grades by the same amount.', 'The observational comparison cannot isolate that causal effect or establish an identical effect at each school.'),
        ('Because the schools differed in several ways, the survey provides no information worth considering.', 'The limitations restrict causal inference but do not make the observed association meaningless.'),
        ('The schools’ grading differences must account for the entire association.', 'A plausible alternative is not proof of the sole explanation.'),
        ('The survey identifies an association, while leaving open how much start time itself contributed to it.', 'This preserves the observed pattern and accurately limits the causal conclusion.'),
    ]),
    (3, '6.A', 3, 'Which sentence would best explain the reasoning linking sentences 5 and 6 to sentence 8?', 1, [
        ('Random assignment is a phrase that appears in many research reports.', 'The statement names a convention without explaining the inferential problem.'),
        ('When several conditions vary together, the observed outcome cannot be attributed to one of them without further evidence.', 'This explains why the school comparison alone cannot isolate the effect of start time.'),
        ('Schools should make every policy identical before students are allowed to compare their experiences.', 'This is an impractical policy demand rather than an explanation of the study’s limitation.'),
        ('A higher average grade always indicates that students learned more during the school day.', 'This assumes an interpretation that differences in grading practices specifically call into question.'),
    ]),
    (4, '6.C', 4, 'Which example would best clarify the distinction in sentence 14 for a general student audience?', 0, [
        ('A rise in the same students’ sleep after a schedule change answers a different question from comparing two schools at one moment.', 'The example concretely distinguishes change over time from a cross-sectional group difference without claiming either alone proves causation.'),
        ('Students often use different alarm sounds even when they attend the same school.', 'Alarm preferences do not clarify the difference between within-group change and between-group comparison.'),
        ('A report becomes more accurate whenever it includes a larger number of technical terms.', 'Terminology does not by itself explain or improve the evidence, and the draft advocates clarity.'),
        ('A school with a later start is similar to a school with an earlier start because both have students.', 'The broad similarity hides rather than clarifies the relevant design distinction.'),
    ]),
    (5, '6.B', 2, 'Which transition best begins sentence 9?', 2, [
        ('For that identical reason,', 'The sentence blocks a mistaken inference rather than repeating the same reason for the causal limitation.'),
        ('As a result of the newspaper’s layout,', 'Layout has not been presented as a cause of the study’s inferential limitations.'),
        ('At the same time,', 'This introduces a balancing qualification: failure to prove an effect is not proof of no effect.'),
        ('Several years earlier,', 'The relationship is logical, not chronological.'),
    ]),
    (5, '8.A', 4, 'Which revision of sentence 4 best maintains a critical but measured tone?', 3, [
        ('The headline exposes the newspaper as an institution that cannot be trusted on any subject.', 'This general accusation extends beyond the specific reporting error.'),
        ('The headline is probably fine because readers know newspapers like dramatic wording.', 'This dismisses the consequential distinction the essay is trying to explain.'),
        ('The study is so technical that ordinary students should leave its interpretation to experts.', 'The draft argues that clear reporting can equip general readers to judge the claim.'),
        ('The findings deserve attention, but the headline expresses a certainty the comparison does not establish.', 'The sentence values the evidence while precisely identifying the overstatement.'),
    ]),
    (7, '8.C', 3, 'Which version of sentence 12 uses parallel structure most effectively?', 1, [
        ('It should state student selection, how sleep was measured, and alternative explanations were examined.', 'The mixed noun phrase and clauses obscure the coordinated list of information.'),
        ('It should explain how students were selected, how sleep was measured, and how alternative explanations were tested.', 'Three parallel “how” clauses make the reporting requirements easy to follow.'),
        ('It should state how students were selected, sleep measurement, and examining alternatives.', 'The shifts from clause to noun phrase to participle weaken parallelism.'),
        ('It should explain selection, to measure sleep, and alternatives that were tested.', 'The grammatical mismatch makes the relationship among the three items unclear.'),
    ]),
    (7, '8.B', 4, 'Which revision best combines sentences 13 and 14 while emphasizing the distinction readers do need?', 0, [
        ('Although readers do not need every technical detail immediately, they need to know whether the report describes change over time or a difference between groups.', 'The subordinate concession gives way to the central requirement and preserves the study-design distinction.'),
        ('Readers need details immediately, although changes over time are differences between groups.', 'This reverses the concession and falsely equates the two designs.'),
        ('Details about time and groups are technical, so readers do not need them in a report.', 'This excludes the very distinction the writer argues is essential.'),
        ('Readers need every detail about groups and times because specialized vocabulary explains research.', 'This contradicts the draft’s selective approach and substitutes jargon for clarity.'),
    ]),
    (2, '4.B', 3, 'Which sentence would best replace sentence 16 as a topic sentence for the final paragraph?', 2, [
        ('The school board should decide the start time without consulting any additional evidence.', 'The paragraph identifies several further considerations and ends by asking what evidence a decision requires.'),
        ('The effect on grades is the only issue that should influence the start-time decision.', 'Sentence 18 expressly adds alertness, family schedules, and transport costs.'),
        ('Accurately describing uncertainty can improve a policy debate rather than prevent a decision.', 'This previews both continued consideration of the policy and the need to avoid guaranteed outcomes.'),
        ('Scientific studies settle policy disputes when newspapers present their conclusions briefly.', 'The paragraph resists treating a single compressed finding as decisive.'),
    ]),
    (7, '2.A', 3, 'Which alternative final sentence best concludes the draft by returning to the headline’s role?', 1, [
        ('The next issue will contain an interview with several members of the school board.', 'An announcement does not develop the argument about evidence and public judgment.'),
        ('A useful headline opens a question at the strength the evidence supports, instead of closing it with a promise.', 'This restates the central standard and connects accurate framing with continued inquiry.'),
        ('Readers can avoid misleading headlines by refusing to read about education research.', 'Avoidance contradicts the draft’s aim of enabling informed readers.'),
        ('The survey’s limitations show that grades should never appear in a newspaper.', 'A limitation on one inference does not justify excluding all discussion of grades.'),
    ]),
])

QUESTIONS = RECIPE + SLEEP
