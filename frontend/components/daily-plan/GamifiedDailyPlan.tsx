import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DailyPlan, DashboardSubjectSummary, SubjectDetail } from "@/lib/api";
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
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Today&apos;s quest</h1>
          <p className="text-muted-foreground">Clear your plan to bank XP and keep the streak going.</p>
        </div>
        <div className="flex items-center gap-2">
          <StreakBadge days={streakDays} />
          {plans.length > 0 && <GenerateTodayPlanButton subjects={enrolledSubjects} />}
        </div>
      </div>

      {plans.length === 0 ? (
        <Card>
          <CardContent className="flex flex-col items-center gap-4 py-12 text-center">
            <p className="text-muted-foreground">No plan generated yet for today.</p>
            <GenerateTodayPlanButton subjects={enrolledSubjects} />
          </CardContent>
        </Card>
      ) : (
        plans.map((plan) => {
          const subjectId = plan.items[0]?.subject_id;
          const availableXp = plan.items
            .filter((i) => i.status === "pending")
            .reduce((sum, i) => sum + i.point_cost, 0);
          return (
            <Card key={plan.id}>
              <CardHeader>
                <CardTitle>{subjectId ? subjectNameById[subjectId] : "Plan"}</CardTitle>
                <p className="text-sm text-muted-foreground">+{availableXp} XP available today</p>
              </CardHeader>
              <CardContent>
                <PlanItemList items={plan.items} topicNames={topicNames} gamified />
              </CardContent>
            </Card>
          );
        })
      )}
    </div>
  );
}
