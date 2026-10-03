"""Nine-unit skill progression; labels are WayPoint paraphrases.

Framework: https://apcentral.collegeboard.org/media/pdf/ap-english-language-and-composition-course-and-exam-description.pdf
Effective fall 2024; checked 2026-10-03. College Board weights skill categories,
not these spiraling units. Zero unit weights deliberately select the planner's
equal-weight fallback rather than inventing official percentages.
"""

SKILLS = {
    "1.A": "Rhetorical context and purpose", "1.B": "Audience values and needs",
    "2.A": "Purposeful openings and conclusions", "2.B": "Writing for an audience",
    "3.A": "Claims and supporting evidence", "3.B": "Thesis and argument structure",
    "3.C": "Qualification and competing perspectives", "4.A": "Developing evidence",
    "4.B": "Defensible thesis statements", "4.C": "Qualifying an argument",
    "5.A": "Evaluating a line of reasoning", "5.B": "Coherence and organization",
    "5.C": "Methods of development", "6.A": "Commentary and reasoning",
    "6.B": "Transitions and connections", "6.C": "Developing an argument",
    "7.A": "Diction, comparison, and tone", "7.B": "Syntax and emphasis",
    "7.C": "Punctuation and rhetorical effect", "8.A": "Purposeful style",
    "8.B": "Clear and effective sentences", "8.C": "Conventions in context",
}
UNIT_SKILLS = [
    ["1.A", "3.A", "4.A"],
    ["1.B", "2.B", "3.A", "4.A", "3.B", "4.B"],
    ["3.A", "4.A", "5.A", "6.A", "5.C", "6.C"],
    ["1.A", "2.A", "3.B", "4.B", "5.C", "6.C"],
    ["5.A", "6.A", "5.B", "6.B", "7.A", "8.A"],
    ["3.A", "4.A", "3.B", "4.B", "7.A", "8.A"],
    ["1.A", "2.A", "3.C", "4.C", "7.B", "8.B", "7.C", "8.C"],
    ["1.B", "2.B", "7.A", "8.A", "7.B", "8.B"],
    ["3.C", "4.C"],
]
UNITS = [{
    "name": f"Unit {index}",
    "description": "Reading and writing practice: " + "; ".join(SKILLS[skill] for skill in skills) + ".",
    "ap_weight_min": 0.0, "ap_weight_max": 0.0, "display_order": index,
    "topics": [{"name": f"{skill}: {SKILLS[skill]}", "description": f"Apply skill {skill} to nonfiction reading and composition.",
                "skill_tags": [f"ap-skill:{skill}"], "display_order": order}
               for order, skill in enumerate(skills, start=1)],
} for index, skills in enumerate(UNIT_SKILLS, start=1)]
