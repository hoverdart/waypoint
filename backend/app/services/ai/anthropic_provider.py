from anthropic import Anthropic

from app.config import Settings
from app.core.exceptions import ServiceUnavailableError
from app.services.ai.provider import ExplainAction, ExplainContext

ACTION_INSTRUCTIONS: dict[ExplainAction, str] = {
    ExplainAction.EXPLAIN_DIFFERENTLY: (
        "Explain the concept behind this question in a different way than a "
        "standard textbook explanation would."
    ),
    ExplainAction.ANALOGY: (
        "Give a concrete, relatable analogy that illuminates the core concept in this question."
    ),
    ExplainAction.EASIER_EXAMPLE: (
        "Give a simpler example illustrating the same underlying concept, then relate it "
        "back to this question."
    ),
    ExplainAction.HARDER_EXAMPLE: (
        "Give a more challenging follow-up example that extends the same underlying concept."
    ),
    ExplainAction.WHY_WRONG: (
        "Explain specifically why the student's answer was incorrect and what misconception "
        "likely caused it."
    ),
    ExplainAction.COMPARE_CONCEPTS: (
        "Compare and contrast the concept in this question with the concept the student named."
    ),
}

MAX_RESPONSE_TOKENS = 400


class AnthropicAIProvider:
    def __init__(self, settings: Settings):
        self._api_key = settings.anthropic_api_key
        self._client = Anthropic(api_key=settings.anthropic_api_key or "unset")
        self._model = settings.anthropic_model

    def explain(self, context: ExplainContext) -> str:
        if not self._api_key:
            raise ServiceUnavailableError(
                "AI explanations aren't configured yet - deterministic explanations are still available."
            )

        parts = [
            f"Question: {context.question_prompt}",
            f"Correct answer: {context.correct_answer}",
        ]
        if context.student_answer:
            parts.append(f"Student's answer: {context.student_answer}")
        if context.compare_topic:
            parts.append(f"Concept to compare against: {context.compare_topic}")
        parts.append(ACTION_INSTRUCTIONS[context.action])
        parts.append("Keep the response under 150 words, encouraging, and appropriate for an AP student.")

        message = self._client.messages.create(
            model=self._model,
            max_tokens=MAX_RESPONSE_TOKENS,
            messages=[{"role": "user", "content": "\n\n".join(parts)}],
        )
        return "".join(block.text for block in message.content if block.type == "text")
