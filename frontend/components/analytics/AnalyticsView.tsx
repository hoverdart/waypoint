import { DashboardSubjectSummary, SubjectMastery, WeeklyCoachReport } from "@/lib/api";
import { WeeklyCoachReportCard } from "@/components/dashboard/WeeklyCoachReportCard";
import { Surface } from "@/components/kit/Surface";
import { PageHeader } from "@/components/kit/PageHeader";
import { Reveal } from "@/components/motion/Reveal";
import { SubjectFilterTabs } from "./SubjectFilterTabs";
import { UnitMasteryChart } from "./UnitMasteryChart";
import { TopicBreakdownTable } from "./TopicBreakdownTable";

export function AnalyticsView({
  enrolledSubjects,
  activeSubjectId,
  mastery,
  weeklyReport,
}: {
  enrolledSubjects: DashboardSubjectSummary[];
  activeSubjectId: number;
  mastery: SubjectMastery;
  weeklyReport: WeeklyCoachReport | null;
}) {
  return (
    <div className="space-y-8">
      <PageHeader title="Analytics" sub="Mastery trends and your weekly coach report." />

      <SubjectFilterTabs subjects={enrolledSubjects} activeSubjectId={activeSubjectId} />

      <div className="grid gap-4 lg:grid-cols-2">
        <Reveal className="h-full">
          <Surface className="flex h-full flex-col gap-5 p-6 sm:p-7">
            <h2 className="font-display text-lg text-ink">Mastery by unit - {mastery.subject_name}</h2>
            <div className="mt-auto">
              <UnitMasteryChart mastery={mastery} />
            </div>
          </Surface>
        </Reveal>

        <Reveal index={1} className="h-full">
          <WeeklyCoachReportCard report={weeklyReport} />
        </Reveal>
      </div>

      <Reveal index={2}>
        <Surface className="p-6 sm:p-7">
          <h2 className="font-display mb-5 text-lg text-ink">Topic breakdown</h2>
          <TopicBreakdownTable mastery={mastery} />
        </Surface>
      </Reveal>
    </div>
  );
}
