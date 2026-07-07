import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { ExamCountdown } from "@/components/shared/ExamCountdown";
import { DashboardSubjectSummary, SubjectMastery, WeeklyCoachReport } from "@/lib/api";
import { WeeklyCoachReportCard } from "@/components/dashboard/WeeklyCoachReportCard";
import { SubjectFilterTabs } from "./SubjectFilterTabs";
import { StudyRouteTimeline } from "./StudyRouteTimeline";
import { TopicBreakdownTable } from "./TopicBreakdownTable";

/** Reinterpreted as the course-detail experience for a single subject -
 * same props/data-fetching as before, presentation-only rebuild. */
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
  const activeSummary = enrolledSubjects.find((s) => s.subject_id === activeSubjectId);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-heading text-2xl font-semibold tracking-tight text-navy sm:text-3xl">
          {mastery.subject_name}
        </h1>
        <p className="text-muted-foreground">Your route through this course, unit by unit.</p>
      </div>

      <WayPointCard elevated>
        <CardContent className="flex flex-wrap items-center gap-4 p-5">
          <div>
            <p className="text-xs font-medium tracking-wide text-blue uppercase">Predicted AP score</p>
            <p className="font-heading text-3xl font-semibold text-navy">{mastery.predicted_ap_score}</p>
          </div>
          <div className="flex flex-1 flex-wrap items-center gap-2">
            {activeSummary?.exam_date ? (
              <ExamCountdown examDate={activeSummary.exam_date} />
            ) : (
              <span className="text-xs text-muted-foreground">No exam date set</span>
            )}
            {activeSummary?.target_score && (
              <span className="rounded-full bg-blue-soft px-3 py-1 text-xs font-medium text-navy">
                Target: {activeSummary.target_score}
              </span>
            )}
            <span className="rounded-full bg-blue-soft px-3 py-1 text-xs font-medium text-navy">
              {Math.round(mastery.confidence_score * 100)}% confidence in this estimate
            </span>
          </div>
        </CardContent>
      </WayPointCard>

      <SubjectFilterTabs subjects={enrolledSubjects} activeSubjectId={activeSubjectId} />

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Study route - {mastery.subject_name}</CardTitle>
          </CardHeader>
          <CardContent>
            <StudyRouteTimeline mastery={mastery} />
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
