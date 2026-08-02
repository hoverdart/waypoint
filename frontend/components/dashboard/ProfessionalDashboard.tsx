import { Compass } from "lucide-react";
import { Dashboard } from "@/lib/api";
import { PageHeader } from "@/components/kit/PageHeader";
import { EmptyState } from "@/components/kit/EmptyState";
import { Reveal } from "@/components/motion/Reveal";
import { DashboardSubjectCard } from "./DashboardSubjectCard";
import { TodaysPlanSummaryCard } from "./TodaysPlanSummaryCard";
import { WeeklyCoachReportCard } from "./WeeklyCoachReportCard";

export function ProfessionalDashboard({ data, topicNames }: { data: Dashboard; topicNames: Record<number, string> }) {
  return (
    <div className="space-y-10">
      <PageHeader
        title={`Welcome back${data.user.display_name ? `, ${data.user.display_name}` : ""}`}
        sub="Here's where things stand across your subjects."
      />

      {data.subjects.length === 0 ? (
        <EmptyState
          icon={<Compass className="size-5" aria-hidden="true" />}
          title="You haven't added any subjects yet - visit onboarding to get started."
        />
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {data.subjects.map((subject, i) => (
            <Reveal key={subject.subject_id} index={i} className="h-full">
              <DashboardSubjectCard subject={subject} />
            </Reveal>
          ))}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-2">
        <Reveal className="h-full">
          <TodaysPlanSummaryCard plan={data.today_plan} topicNames={topicNames} />
        </Reveal>
        <Reveal index={1} className="h-full">
          <WeeklyCoachReportCard report={data.latest_weekly_report} />
        </Reveal>
      </div>
    </div>
  );
}
