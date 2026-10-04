# U.S. History expansion

Status: in progress. The live bank currently contains 325 questions, including 288 new source-based items;
it is not a comprehensive AP U.S. History preparation bank.

## Verified format for May 2027

Checked 2026-10-04 against the [official exam page](https://apcentral.collegeboard.org/courses/ap-united-states-history/exam),
[2027 update](https://apcentral.collegeboard.org/courses/ap-history-exam-updates), and
[fall-2026 corrections](https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-and-exam-description-clarifications.pdf).

| Section | Required work | Time | Weight |
|---|---|---|---|
| I-A | 55 multiple-choice questions | 55 minutes | 40% |
| I-B | Three short-answer questions | 40 minutes | 20% |
| II | One DBQ and one long essay | 100 minutes total | 25% + 15% |

Build for the 2027 format: all three SAQs are required. Their stimuli comprise
secondary text, primary text, and a non-text source respectively, with different
periods represented. The LEQ is one broad required prompt with flexibility in the
evidence selected; do not reproduce the former menu of three LEQ prompts or the
former SAQ choice. The DBQ uses seven documents. The suggested division of Section II
is 60 minutes for DBQ (including reading) and 40 for LEQ; preserve the shared clock.
Course content and rubric criteria remain unchanged according to the update.

## Work and acceptance gates

1. Expand the current coarse topic list against the full current CED, preserving
   existing topic IDs where possible and explicitly mapping legacy questions.
   Period 2's live seed weighting is corrected to 6–8%; other period ranges match
   the [course page](https://apcentral.collegeboard.org/courses/ap-united-states-history).
2. Build a diverse source-based bank: primary texts with provenance, original
   secondary interpretations, maps, quantitative evidence, and visual sources.
   Use public-domain or licensed material with verified attribution. Do not invent
   a quotation and present it as an authentic historical document.
3. Target four independent 55-question MCQ forms (220 questions minimum), plus
   additional questions needed for at least three per curriculum topic and varied
   difficulty. Each form must meet period weights and sample sourcing, claims,
   contextualization, comparison, causation, and continuity/change skills.
4. Target at least 24 SAQs, eight DBQs with seven-document packs, and 12 broad LEQs.
   Include substantive models, evidence alternatives, and transparent self-review
   rubrics. Keyword matches cannot substitute for evaluating historical reasoning.
5. Extend the timed state machine to mixed free-response sections and distinct
   section types. The current implementation assumes MCQ first and FRQ afterward;
   it also needs explicit SAQ/DBQ/LEQ presentation and appropriate rubric guidance.
   No current U.S. History timed form is advertised as representative.
6. Verify normal practice, diagnostic exclusion of self-reviewed work, persisted
   drafts, section deadlines, results, source readability, and responsive layouts.
   Check existing-session compatibility when revising the foundation bank.

These are WayPoint depth targets. Counts, passing tests, and author-assigned
ratings do not establish educator review or calibrated AP difficulty. Released
exam archives remain external resources, with older formats identified as such.

Period 1 now maps all seven framework topic areas, with nine new questions across
its three previously missing areas. Period 2 now maps all eight areas, with 12 new questions across four added topics.
Period 3 adds political ideas, constitutional structure, western movement, confederation government,
ratification, revolutionary ideals, and national identity, and continuity/change topics with 32 primary-text questions. Three contextualization questions and four Revolutionary War questions use explicitly labeled original summaries. Its remaining expansion and Periods 4–9 are pending.

Next: inventory the remaining current CED topics and continue sourced period-based
question sets, then implement the three free-response workflows.

Period 3 now follows the framework sequence and maps all 13 topic codes. Its 15
stored topics include two retained foundation topics that overlap expanded areas;
these preserve existing question assignments and learner records. This mapping
is not a claim of comprehensive content depth or representative exam coverage.

Period 4 expansion has begun with four Monroe Doctrine source questions and the
America on the World Stage topic (4.4). Other Period 4 framework areas still need
mapping and expansion; this first set does not cover the full diplomacy topic.

Period 4 also includes four Declaration of Sentiments questions under An Age of
Reform (4.11). This named source set leaves room for independent abolition,
temperance, education, and other reform evidence; those areas need further depth.

Four Indian-removal questions begin Jackson and Federal Power (4.8), analyzing
presidential justification and its limits. Four complementary Cherokee petition questions address representation and consent.
Four Bank War questions analyze the veto message; four nullification questions compare enforcement with compromise. Further depth remains needed.

Four questions begin Market Revolution: Industrialization (4.5), examining cotton
supply chains and differences between wage and enslaved labor. Technology,
transportation, and workplace evidence still need additional sets.

Four Sarah Bagley source questions begin Market Revolution: Society and Culture
(4.6), examining workers’ dignity, corporate discipline, and women’s wage work.
Migration, class formation, and broader social changes still need additional sets.

## MCQ form inventory audit (2026-10-04)

The content audit now includes `mcq_form_inventory` for U.S. History. It checks
four independent 55-question forms against the configured period weight ranges,
rounding minimum counts up and maximum counts down. Only approved MCQs with
unique trimmed prompts and recognized periods count; ambiguous duplicate prompts
are excluded. This is a necessary inventory check, not a form assembler.

All nine periods now meet the necessary raw inventory minima for four forms.
The history bank has 325 questions, with 244 approved unique MCQs usable after
period caps against the 220-question target. This does not mean four valid forms
have been assembled: stimulus groups, skills, sources, and difficulty still need
to be balanced within each form.

Periods 7–9 still require broader curriculum coverage despite meeting their raw
inventory minima. The next exam gate is explicit form assembly with source-group
integrity and skill balance, followed by historical/editorial review. Non-text
stimuli, difficulty calibration, and FRQ readiness remain separate unmet gates
before publishing representative exam forms.

### Whole-source-group gate

`source_group_inventory` now checks whether each period's inventory can fill
four separate slots within its weight bounds without splitting or reusing a
source group. Untagged questions count as individual items. Groups with duplicate,
unapproved, non-MCQ, cross-period, or ambiguous members are excluded rather than
silently shortened. A dynamic-programming check permits unused groups.

Current result: **all periods pass** the necessary whole-group packing check.
The four-question Mayflower Compact set resolves the previous Period 2 packing
constraint without splitting sources. Per-period feasibility still does not
establish four complete 55-question forms, skill/source balance, or educator review.

### Offline draft assembly

Run `python -m scripts.history_forms` from `backend/` to generate a reproducible
review manifest. Four distinct 55-MCQ drafts now assemble with period counts
`3, 4, 9, 9, 9, 6, 6, 6, 3`, all within configured weights. Source sets stay intact
and no question or source group is reused across drafts. Unapproved, duplicate,
and non-MCQ items cannot fill slots. Invalid weights or ambiguous groups fail.
Prompt hashes identify the exact content version; they are not database IDs.

These drafts are **not published exams**. Assembly requires each draft to contain
sourcing, claims/evidence, contextualization, comparison, causation, and
continuity/change tags. Deterministic same-period, equal-size whole-group swaps
repair missing skills while preserving all existing assembly constraints. The
local search fails closed when it cannot improve coverage; this does not prove
that no globally feasible arrangement exists.

All four current drafts pass minimum tag presence, including continuity/change.
This is not balanced skill weighting or verification of tag accuracy. Source
variety, non-text stimuli, difficulty, and factual quality still require review
before student-facing exam integration.

### Migration and demographic evidence

Three original questions tagged 9.5 now extend the existing demographic-change
topic. A compact numeric series uses Census foreign-born population shares for
1970, 1980, 1990, and 2000. Questions distinguish population stocks from annual
arrivals, relate admission-policy changes to historical context, and identify
the geographic and arrival-period evidence needed to test settlement claims.
These are text-rendered data, not an interactive chart. Internal migration,
regional change, immigrant experiences, and policy debates still need depth.

Sources: [Census historical statistics](https://www.census.gov/library/working-papers/2006/demo/POP-twps0081.html)
and [National Archives on the 1965 act](https://prologue.blogs.archives.gov/2015/09/17/fifty-year-later-a-brief-history-of-the-immigration-act-of-1965/).

### Guided learning

Period 9 now includes a guided demographic-evidence lesson with explanation,
a worked Census example, a three-option check, individual feedback, and versioned
per-user completion. Its practice target uses topic tag `ced:9.5`; existing
English lessons continue using `ap-skill:` mappings. Completion is a learning
check, not a mastery score. Periods 2 and 8 also have introductory source-purpose and legal-implementation
lessons, respectively. These introductory lessons do not yet form full unit
sequences; other history units still need guided lessons.

The Period 2 lesson uses the [Mayflower Compact transcription](https://avalon.law.yale.edu/17th_century/mayflower.asp)
to distinguish local association, royal loyalty, and claims about participation.
The Period 8 lesson uses the [National Archives Brown record](https://www.archives.gov/milestone-documents/brown-v-board-of-education)
to distinguish constitutional change from local implementation. Each includes
original instruction, a worked example, a check with specific feedback, and a
curriculum-linked practice target.

Period 8 now adds two lessons on causal mechanisms and multiple policy motives,
using the [Office of the Historian's Marshall Plan account](https://history.state.gov/milestones/1945-1952/marshall-plan).
They distinguish chronology from causation, stated policy rationale from measured
outcomes, and humanitarian effects from exclusive humanitarian motives. The
three-lesson Period 8 sequence links to civil-rights and containment practice;
it does not yet cover the full period curriculum.
