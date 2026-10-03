"""Candidate English Language bank; enrollment is enabled only after rollout checks."""
from .english_language.form_a_reading import QUESTIONS as READING_A
from .english_language.form_a_writing import QUESTIONS as WRITING_A
from .english_language.form_a_essays import QUESTIONS as ESSAYS_A

from .english_language.form_b_reading import QUESTIONS as READING_B
from .english_language.form_b_writing import QUESTIONS as WRITING_B

QUESTIONS = READING_A + WRITING_A + ESSAYS_A + READING_B + WRITING_B
