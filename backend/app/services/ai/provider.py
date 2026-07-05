"""AI-provider-agnostic contract for the capped, optional runtime "explain"
feature. Question generation is offline/manual and never goes through this
path - this is strictly for the six explicit on-demand actions the product
spec calls out.
"""

from enum import Enum
from typing import Protocol

from pydantic import BaseModel


class ExplainAction(str, Enum):
    EXPLAIN_DIFFERENTLY = "explain_differently"
    ANALOGY = "analogy"
    EASIER_EXAMPLE = "easier_example"
    HARDER_EXAMPLE = "harder_example"
    WHY_WRONG = "why_wrong"
    COMPARE_CONCEPTS = "compare_concepts"


class ExplainContext(BaseModel):
    question_prompt: str
    correct_answer: str
    student_answer: str | None = None
    action: ExplainAction
    compare_topic: str | None = None


class AIProvider(Protocol):
    def explain(self, context: ExplainContext) -> str: ...
