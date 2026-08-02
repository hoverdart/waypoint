import { Surface } from "@/components/kit/Surface";
import { PillLink } from "@/components/kit/PillButton";
import { Eyebrow } from "@/components/kit/Typography";
import { PracticeResultsResponse } from "@/lib/api";
import { AnswerBreakdownCard } from "./AnswerBreakdownCard";

export function ProfessionalResults({ results, subjectId }: { results: PracticeResultsResponse; subjectId?: number }) {
  const isDiagnostic = results.session_type === "diagnostic";
  const percent = Math.round(results.score * 100);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-8 px-6 py-12">
      <Surface tone="raised" className="px-6 py-10 text-center sm:py-12">
        <Eyebrow>{isDiagnostic ? "Baseline established" : "Session complete"}</Eyebrow>
        <p className="font-display mt-4 text-5xl text-ink tabular-nums sm:text-6xl">
          {results.correct_count}/{results.total_questions}
        </p>
        <p className="mt-3 text-base text-muted-foreground">{percent}% correct</p>
      </Surface>

      <div className="space-y-3">
        {results.breakdown.map((item) => (
          <AnswerBreakdownCard key={item.question_id} item={item} subjectId={subjectId} />
        ))}
      </div>

      <div className="flex flex-wrap justify-center gap-3">
        <PillLink href="/dashboard" variant="secondary">
          Back to dashboard
        </PillLink>
        <PillLink href="/daily-plan" arrow>
          Go to daily plan
        </PillLink>
      </div>
    </div>
  );
}
