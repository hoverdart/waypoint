import { ClipboardList } from "lucide-react";
import { DailyPlan, DashboardSubjectSummary, SubjectDetail } from "@/lib/api";
import { PageHeader } from "@/components/kit/PageHeader";
import { Chip } from "@/components/kit/Pills";
import { EmptyState } from "@/components/kit/EmptyState";
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
    <div className="space-y-10">
      <PageHeader
        title="Today's plan"
        sub="Highest-priority topics first, with the reason behind each pick."
        actions={plans.length > 0 ? <GenerateTodayPlanButton subjects={enrolledSubjects} /> : undefined}
      />

      {plans.length === 0 ? (
        <EmptyState
          icon={<ClipboardList className="size-5" aria-hidden="true" />}
          title="No plan generated yet for today."
          action={<GenerateTodayPlanButton subjects={enrolledSubjects} />}
        />
      ) : (
        <div className="space-y-10">
          {plans.map((plan) => {
            const subjectId = plan.items[0]?.subject_id;
            return (
              <section key={plan.id} className="space-y-4">
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <h2 className="font-display text-xl text-ink sm:text-2xl">
                    {subjectId ? subjectNameById[subjectId] : "Plan"}
                  </h2>
                  <Chip tone="neutral">{`${plan.point_budget} point budget`}</Chip>
                </div>
                <PlanItemList items={plan.items} topicNames={topicNames} />
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}
