import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DailyPlan, DashboardSubjectSummary, SubjectDetail } from "@/lib/api";
import { PlanItemList } from "./PlanItemList";
import { GenerateTodayPlanButton } from "./GenerateTodayPlanButton";
import { buildTopicNameMap } from "./topicNames";

export function ProfessionalDailyPlan({
  plans,
  subjectDetails,
  enrolledSubjects,
}: {
  plans: DailyPlan[];
  subjectDetails: SubjectDetail[];
  enrolledSubjects: DashboardSubjectSummary[];
}) {
  const topicNames = buildTopicNameMap(subjectDetails);
  const subjectNameById = Object.fromEntries(subjectDetails.map((s) => [s.id, s.name]));

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Today&apos;s plan</h1>
          <p className="text-muted-foreground">
            Highest-priority topics first, with the reason behind each pick.
          </p>
        </div>
        {plans.length > 0 && <GenerateTodayPlanButton subjects={enrolledSubjects} />}
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
          return (
            <Card key={plan.id}>
              <CardHeader>
                <CardTitle>{subjectId ? subjectNameById[subjectId] : "Plan"}</CardTitle>
                <p className="text-sm text-muted-foreground">{plan.point_budget} point budget</p>
              </CardHeader>
              <CardContent>
                <PlanItemList items={plan.items} topicNames={topicNames} />
              </CardContent>
            </Card>
          );
        })
      )}
    </div>
  );
}
