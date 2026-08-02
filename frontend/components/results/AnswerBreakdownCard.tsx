import { Surface } from "@/components/kit/Surface";
import { Chip } from "@/components/kit/Pills";
import { ExplainButton } from "@/components/shared/ExplainButton";
import { AnswerBreakdownItem } from "@/lib/api";

export function AnswerBreakdownCard({ item }: { item: AnswerBreakdownItem }) {
  const selectedExplanation = item.explanations.find((e) => e.option_id === item.selected_option_id);
  const generalExplanation = item.explanations.find((e) => e.option_id === null);

  return (
    <Surface className="space-y-4 p-5 sm:p-6">
      <div className="flex items-start justify-between gap-4">
        <p className="text-sm leading-relaxed text-ink">{item.prompt}</p>
        <Chip tone={item.is_correct ? "green" : "coral"} dot className="shrink-0">
          {item.is_correct ? "Correct" : "Incorrect"}
        </Chip>
      </div>

      <p className="text-sm text-muted-foreground">
        Correct answer: <span className="font-medium text-ink">{item.correct_answer}</span>
        {" · "}
        {item.score}/{item.max_score} pts
      </p>

      {(selectedExplanation ?? generalExplanation) && (
        <p className="rounded-2xl bg-blue-soft/50 p-4 text-sm leading-relaxed text-ink">
          {(selectedExplanation ?? generalExplanation)?.explanation}
        </p>
      )}

      {!item.is_correct && (
        <ExplainButton
          questionId={item.question_id}
          selectedOptionId={item.selected_option_id}
          freeResponseText={item.free_response_text}
        />
      )}
    </Surface>
  );
}
