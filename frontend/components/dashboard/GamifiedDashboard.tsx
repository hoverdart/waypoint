import { Dashboard } from "@/lib/api";
import { DashboardSubjectCard } from "./DashboardSubjectCard";
import { TodaysPlanSummaryCard } from "./TodaysPlanSummaryCard";
import { WeeklyCoachReportCard } from "./WeeklyCoachReportCard";
import { StreakBadge } from "@/components/gamification/StreakBadge";
import { XpBar } from "@/components/gamification/XpBar";
import { AchievementBadgeGrid } from "@/components/gamification/AchievementBadgeGrid";

export function GamifiedDashboard({ data }: { data: Dashboard }) {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">
            Welcome back{data.user.display_name ? `, ${data.user.display_name}` : ""}
          </h1>
          <p className="text-muted-foreground">Let&apos;s keep the streak alive.</p>
        </div>
        <StreakBadge days={data.streak_days} />
      </div>

      <XpBar totalXp={data.total_xp} />

      {data.subjects.length === 0 ? (
        <p className="text-sm text-muted-foreground">
          You haven&apos;t added any subjects yet - visit onboarding to get started.
        </p>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {data.subjects.map((subject) => (
            <DashboardSubjectCard key={subject.subject_id} subject={subject} />
          ))}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-2">
        <TodaysPlanSummaryCard plan={data.today_plan} />
        <WeeklyCoachReportCard report={data.latest_weekly_report} />
      </div>

      <AchievementBadgeGrid badges={data.earned_badges} />
    </div>
  );
}
