import { Card, CardContent } from "@/components/ui/card";
import { LinkButton } from "@/components/shared/LinkButton";
import { PracticeResultsResponse } from "@/lib/api";
import { AnswerBreakdownCard } from "./AnswerBreakdownCard";

export function ProfessionalResults({ results }: { results: PracticeResultsResponse }) {
  const isDiagnostic = results.session_type === "diagnostic";
  const percent = Math.round(results.score * 100);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-6 px-4 py-8">
      <Card>
        <CardContent className="space-y-2 pt-6 text-center">
          <p className="text-sm text-muted-foreground">
            {isDiagnostic ? "Baseline established" : "Session complete"}
          </p>
          <p className="text-4xl font-semibold">
            {results.correct_count}/{results.total_questions}
          </p>
          <p className="text-muted-foreground">{percent}% correct</p>
        </CardContent>
      </Card>

      <div className="space-y-3">
        {results.breakdown.map((item) => (
          <AnswerBreakdownCard key={item.question_id} item={item} />
        ))}
      </div>

      <div className="flex justify-center gap-3">
        <LinkButton href="/dashboard" variant="outline">
          Back to dashboard
        </LinkButton>
        <LinkButton href="/daily-plan">Go to daily plan</LinkButton>
      </div>
    </div>
  );
}
