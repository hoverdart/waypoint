# U.S. History expansion

Status: in progress. The live bank currently contains 288 questions, including 251 new source-based items;
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

Current shortages against the four-form period minima are Period 2: **1**,
Period 8: **18**, and Period 9: **8**. Although the whole history bank has 285
questions, period caps leave only 217 usable MCQs toward the 220-question target.
The three-question aggregate shortfall must not obscure the larger per-period
shortages: adding three questions alone would not meet the period minima.

Next inventory priorities are substantive Period 8 and 9 expansion and the
Period 2 minimum, alongside the remaining Period 7 topic gaps. Even passing this
check will not establish stimulus-group integrity, skill balance, source variety,
difficulty calibration, factual review, or FRQ readiness. Those remain separate
gates before publishing representative exam forms.
