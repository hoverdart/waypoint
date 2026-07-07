import { Compass } from "lucide-react";
import { CardContent } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { EmptyState } from "@/components/shared/EmptyState";
import { LinkButton } from "@/components/shared/LinkButton";
import { Dashboard } from "@/lib/api";
import { CourseReadinessCard } from "./CourseReadinessCard";
import { TodaysRouteCard } from "./TodaysRouteCard";
import { WeeklyCoachReportCard } from "./WeeklyCoachReportCard";
import { ProgressCompass } from "./ProgressCompass";
import { NeedsAttentionList } from "./NeedsAttentionList";
import { PlanReasoningPanel } from "./PlanReasoningPanel";
import { StreakBadge } from "@/components/gamification/StreakBadge";
import { XpBar } from "@/components/gamification/XpBar";
import { AchievementBadgeGrid } from "@/components/gamification/AchievementBadgeGrid";

export function GamifiedDashboard({
  data,
  topicNames,
}: {
  data: Dashboard;
  topicNames: Record<number, string>;
}) {
  const overall = data.subjects.length
    ? Math.round((data.subjects.reduce((sum, s) => sum + s.mastery_score, 0) / data.subjects.length) * 100)
    : null;

  return (
    <div className="space-y-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="font-heading text-2xl font-semibold tracking-tight text-navy sm:text-3xl">
            {overall !== null ? `You're ${overall}% exam-ready` : "Let's set up your first AP course"}
          </h1>
          <p className="text-muted-foreground">Clear today&apos;s quest to bank XP and keep the streak going.</p>
        </div>
        <StreakBadge days={data.streak_days} />
      </div>

      <XpBar totalXp={data.total_xp} />

      {data.subjects.length === 0 ? (
        <EmptyState
          icon={<Compass className="size-5" aria-hidden="true" />}
          title="No subjects yet"
          description="Visit onboarding to add your AP courses and get your first quest."
          action={<LinkButton href="/onboarding">Go to onboarding</LinkButton>}
        />
      ) : (
        <>
          <div className="grid gap-4 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.3fr)]">
            <WayPointCard elevated>
              <CardContent className="flex items-center p-6">
                <ProgressCompass subjects={data.subjects} />
              </CardContent>
            </WayPointCard>
            <TodaysRouteCard plan={data.today_plan} topicNames={topicNames} gamified />
          </div>

          {data.today_plan && <NeedsAttentionList items={data.today_plan.items} topicNames={topicNames} />}

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {data.subjects.map((subject) => (
              <CourseReadinessCard key={subject.subject_id} subject={subject} />
            ))}
          </div>

          <div className="grid gap-4 md:grid-cols-2">
            <WeeklyCoachReportCard report={data.latest_weekly_report} />
            {data.today_plan && <PlanReasoningPanel items={data.today_plan.items} topicNames={topicNames} />}
          </div>

          <AchievementBadgeGrid badges={data.earned_badges} />
        </>
      )}
    </div>
  );
}
