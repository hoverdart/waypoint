import { Compass } from "lucide-react";
import { CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { EmptyState } from "@/components/shared/EmptyState";
import { ExamCountdown } from "@/components/shared/ExamCountdown";
import { DailyPlan, DashboardSubjectSummary, SubjectDetail } from "@/lib/api";
import { PlanItemList } from "./PlanItemList";
import { GenerateTodayPlanButton } from "./GenerateTodayPlanButton";
import { RegenerateTimeBudgetControl } from "./RegenerateTimeBudgetControl";
import { buildTopicNameMap } from "@/lib/planItemLabels";
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
  const examDateBySubjectId = Object.fromEntries(enrolledSubjects.map((s) => [s.subject_id, s.exam_date]));

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-heading text-2xl font-semibold tracking-tight text-navy sm:text-3xl">
            Today&apos;s quest
          </h1>
          <p className="text-muted-foreground">Clear your plan to bank XP and keep the streak going.</p>
        </div>
        <div className="flex items-center gap-2">
          <StreakBadge days={streakDays} />
          {plans.length > 0 && (
            <>
              <RegenerateTimeBudgetControl />
              <GenerateTodayPlanButton subjects={enrolledSubjects} />
            </>
          )}
        </div>
      </div>

      {plans.length === 0 ? (
        <WayPointCard elevated>
          <CardContent className="p-6">
            <EmptyState
              icon={<Compass className="size-5" aria-hidden="true" />}
              title="No plan generated yet for today."
              action={<GenerateTodayPlanButton subjects={enrolledSubjects} />}
            />
          </CardContent>
        </WayPointCard>
      ) : (
        plans.map((plan) => {
          const subjectId = plan.items[0]?.subject_id;
          const availableXp = plan.items
            .filter((i) => i.status === "pending")
            .reduce((sum, i) => sum + i.point_cost, 0);
          const examDate = subjectId ? examDateBySubjectId[subjectId] : null;
          return (
            <WayPointCard key={plan.id} elevated>
              <CardHeader className="flex-row items-center justify-between gap-3 space-y-0">
                <div>
                  <CardTitle className="font-heading text-navy">
                    {subjectId ? subjectNameById[subjectId] : "Plan"}
                  </CardTitle>
                  <p className="text-sm text-muted-foreground">+{availableXp} XP available today</p>
                </div>
                {examDate && <ExamCountdown examDate={examDate} />}
              </CardHeader>
              <CardContent>
                <PlanItemList items={plan.items} topicNames={topicNames} gamified />
              </CardContent>
            </WayPointCard>
          );
        })
      )}
    </div>
  );
}
