import { CardContent } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { LinkButton } from "@/components/shared/LinkButton";
import { PracticeResultsResponse } from "@/lib/api";
import { AchievementBadge } from "@/components/gamification/AchievementBadge";
import { AnswerBreakdownCard } from "./AnswerBreakdownCard";

export function GamifiedResults({
  results,
  subjectId,
}: {
  results: PracticeResultsResponse;
  subjectId?: number;
}) {
  const isDiagnostic = results.session_type === "diagnostic";
  const percent = Math.round(results.score * 100);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-6 px-4 py-8">
      <WayPointCard elevated>
        <CardContent className="space-y-2 pt-6 text-center">
          <p className="text-sm text-muted-foreground">
            {isDiagnostic ? "Baseline established" : "Session complete"}
          </p>
          <p className="font-heading text-4xl font-semibold text-navy">
            {results.correct_count}/{results.total_questions}
          </p>
          <p className="text-muted-foreground">{percent}% correct</p>
          <p className="text-lg font-medium text-blue">+{results.xp_earned} XP earned</p>
        </CardContent>
      </WayPointCard>

      {results.newly_earned_badges.length > 0 && (
        <WayPointCard>
          <CardContent className="space-y-3 pt-6">
            <p className="text-sm font-medium text-navy">
              New badge{results.newly_earned_badges.length > 1 ? "s" : ""} unlocked!
            </p>
            <div className="grid gap-2 sm:grid-cols-2">
              {results.newly_earned_badges.map((badge) => (
                <AchievementBadge key={badge.id} badge={badge} />
              ))}
            </div>
          </CardContent>
        </WayPointCard>
      )}

      <div className="space-y-3">
        {results.breakdown.map((item) => (
          <AnswerBreakdownCard key={item.question_id} item={item} subjectId={subjectId} />
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
