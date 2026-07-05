import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DashboardSubjectSummary, SubjectMastery, WeeklyCoachReport } from "@/lib/api";
import { WeeklyCoachReportCard } from "@/components/dashboard/WeeklyCoachReportCard";
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
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Analytics</h1>
        <p className="text-muted-foreground">Mastery trends and your weekly coach report.</p>
      </div>

      <SubjectFilterTabs subjects={enrolledSubjects} activeSubjectId={activeSubjectId} />

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Mastery by unit - {mastery.subject_name}</CardTitle>
          </CardHeader>
          <CardContent>
            <UnitMasteryChart mastery={mastery} />
          </CardContent>
        </Card>
        <WeeklyCoachReportCard report={weeklyReport} />
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Topic breakdown</CardTitle>
        </CardHeader>
        <CardContent>
          <TopicBreakdownTable mastery={mastery} />
        </CardContent>
      </Card>
    </div>
  );
}
