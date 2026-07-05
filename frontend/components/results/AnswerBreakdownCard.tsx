import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { ExplainButton } from "@/components/shared/ExplainButton";
import { AnswerBreakdownItem } from "@/lib/api";

export function AnswerBreakdownCard({ item }: { item: AnswerBreakdownItem }) {
  const selectedExplanation = item.explanations.find((e) => e.option_id === item.selected_option_id);
  const generalExplanation = item.explanations.find((e) => e.option_id === null);

  return (
    <Card>
      <CardContent className="space-y-3 pt-6">
        <div className="flex items-start justify-between gap-4">
          <p className="text-sm">{item.prompt}</p>
          <Badge variant={item.is_correct ? "default" : "destructive"} className="shrink-0">
            {item.is_correct ? "Correct" : "Incorrect"}
          </Badge>
        </div>

        <p className="text-sm text-muted-foreground">
          Correct answer: <span className="font-medium text-foreground">{item.correct_answer}</span>
          {" · "}
          {item.score}/{item.max_score} pts
        </p>

        {(selectedExplanation ?? generalExplanation) && (
          <p className="rounded-md bg-muted p-3 text-sm">
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
      </CardContent>
    </Card>
  );
}
