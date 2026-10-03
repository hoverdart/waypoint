import { Surface } from "@/components/kit/Surface";
import { PillLink } from "@/components/kit/PillButton";
import { Chip } from "@/components/kit/Pills";
import { Eyebrow } from "@/components/kit/Typography";
import { PracticeResultsResponse } from "@/lib/api";
import { AchievementBadge } from "@/components/gamification/AchievementBadge";
import { AnswerBreakdownCard } from "./AnswerBreakdownCard";

export function GamifiedResults({ results, subjectId }: { results: PracticeResultsResponse; subjectId?: number }) {
  const isDiagnostic = results.session_type === "diagnostic";
  const gradedCount = results.graded_count ?? results.total_questions;
  const percent = Math.round(results.score * 100);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-8 px-6 py-12">
      <Surface tone="raised" className="px-6 py-10 text-center sm:py-12">
        <Eyebrow>{isDiagnostic ? "Baseline established" : "Session complete"}</Eyebrow>
        <p className="font-display mt-4 text-5xl text-ink tabular-nums sm:text-6xl">
          {gradedCount ? `${results.correct_count}/${gradedCount}` : "Time to reflect"}
        </p>
        <p className="mt-3 text-base text-muted-foreground">{gradedCount ? `${percent}% correct on scored questions` : "Review your responses with the rubric below."}</p>
        <Chip tone="violet" className="mt-5 px-3.5 py-1.5 text-sm font-semibold">
          +{results.xp_earned} XP earned
        </Chip>
        {!!results.self_review_count && <p className="mt-3 text-sm text-muted-foreground">{results.self_review_count} responses use rubric self-review and are excluded from automatic accuracy.</p>}
      </Surface>

      {results.newly_earned_badges.length > 0 && (
        <Surface className="space-y-4 p-6">
          <p className="font-display text-lg text-ink">
            New badge{results.newly_earned_badges.length > 1 ? "s" : ""} unlocked!
          </p>
          <div className="grid gap-2 sm:grid-cols-2">
            {results.newly_earned_badges.map((badge) => (
              <AchievementBadge key={badge.id} badge={badge} />
            ))}
          </div>
        </Surface>
      )}

      <div className="space-y-3">
        {results.breakdown.map((item) => (
          <AnswerBreakdownCard key={item.question_id} item={item} subjectId={subjectId} sessionId={results.session_id} />
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
