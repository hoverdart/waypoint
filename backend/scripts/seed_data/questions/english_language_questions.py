"""Candidate English Language bank; enrollment is enabled only after rollout checks."""
from .english_language.form_a_reading import QUESTIONS as READING_A
from .english_language.form_a_writing import QUESTIONS as WRITING_A
from .english_language.form_a_essays import QUESTIONS as ESSAYS_A

from .english_language.form_b_reading import QUESTIONS as READING_B
from .english_language.form_b_writing import QUESTIONS as WRITING_B

from .english_language.form_b_essays import QUESTIONS as ESSAYS_B
from .english_language.form_c_reading import QUESTIONS as READING_C
from .english_language.form_c_writing import QUESTIONS as WRITING_C
from .english_language.form_c_essays import QUESTIONS as ESSAYS_C
from .english_language.form_d_reading import QUESTIONS as READING_D
from .english_language.form_d_writing import QUESTIONS as WRITING_D

QUESTIONS = READING_A + WRITING_A + ESSAYS_A + READING_B + WRITING_B + ESSAYS_B + READING_C + WRITING_C + ESSAYS_C + READING_D + WRITING_D
