import { Sparkles } from "lucide-react";
import { DailyPlan, DashboardSubjectSummary, SubjectDetail } from "@/lib/api";
import { PageHeader } from "@/components/kit/PageHeader";
import { Chip } from "@/components/kit/Pills";
import { EmptyState } from "@/components/kit/EmptyState";
import { PlanItemList } from "./PlanItemList";
import { GenerateTodayPlanButton } from "./GenerateTodayPlanButton";
import { buildTopicNameMap } from "./topicNames";
import { StreakBadge } from "@/components/gamification/StreakBadge";

export function GamifiedDailyPlan({
  plans,
  subjectDetails,
  enrolledSubjects,
  streakDays,
}: {
  plans: DailyPlan[];
  subjectDetails: SubjectDetail[];
  enrolledSubjects: DashboardSubjectSummary[];
  streakDays: number;
}) {
  const topicNames = buildTopicNameMap(subjectDetails);
  const subjectNameById = Object.fromEntries(subjectDetails.map((s) => [s.id, s.name]));

  return (
    <div className="space-y-10">
      <PageHeader
        title="Today's quest"
        sub="Clear your plan to bank XP and keep the streak going."
        actions={
          <>
            <StreakBadge days={streakDays} />
            {plans.length > 0 && <GenerateTodayPlanButton subjects={enrolledSubjects} />}
          </>
        }
      />

      {plans.length === 0 ? (
        <EmptyState
          icon={<Sparkles className="size-5" aria-hidden="true" />}
          title="No plan generated yet for today."
          action={<GenerateTodayPlanButton subjects={enrolledSubjects} />}
        />
      ) : (
        <div className="space-y-10">
          {plans.map((plan) => {
            const subjectId = plan.items[0]?.subject_id;
            const availableXp = plan.items
              .filter((i) => i.status === "pending")
              .reduce((sum, i) => sum + i.point_cost, 0);
            return (
              <section key={plan.id} className="space-y-4">
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <h2 className="font-display text-xl text-ink sm:text-2xl">
                    {subjectId ? subjectNameById[subjectId] : "Plan"}
                  </h2>
                  <Chip tone="violet">{`+${availableXp} XP available today`}</Chip>
                </div>
                <PlanItemList items={plan.items} topicNames={topicNames} gamified />
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}
