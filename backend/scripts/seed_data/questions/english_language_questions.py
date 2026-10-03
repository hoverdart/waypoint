"""Candidate English Language bank; enrollment is enabled only after rollout checks."""
from .english_language.form_a_reading import QUESTIONS as READING_A
from .english_language.form_a_writing import QUESTIONS as WRITING_A
from .english_language.form_a_essays import QUESTIONS as ESSAYS_A

QUESTIONS = READING_A + WRITING_A + ESSAYS_A
