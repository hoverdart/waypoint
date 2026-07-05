import { redirect } from "next/navigation";
import { ApiError, getDashboard, getLatestWeeklyReport, getSubjectMastery } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { AnalyticsView } from "@/components/analytics/AnalyticsView";
import { Card, CardContent } from "@/components/ui/card";

export default async function AnalyticsPage({
  searchParams,
}: {
  searchParams: Promise<{ subject?: string }>;
}) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { subject } = await searchParams;
  const dashboard = await getDashboard(token);

  if (dashboard.subjects.length === 0) {
    return (
      <div className="mx-auto w-full max-w-3xl px-4 py-8">
        <Card>
          <CardContent className="pt-6 text-center text-muted-foreground">
            Add a subject via onboarding to see analytics here.
          </CardContent>
        </Card>
      </div>
    );
  }

  const activeSubjectId = subject ? Number(subject) : dashboard.subjects[0].subject_id;

  const [mastery, weeklyReport] = await Promise.all([
    getSubjectMastery(activeSubjectId, token),
    getLatestWeeklyReport(token).catch((e) => {
      if (e instanceof ApiError && e.status === 404) return null;
      throw e;
    }),
  ]);

  return (
    <div className="mx-auto w-full max-w-5xl px-4 py-8">
      <AnalyticsView
        enrolledSubjects={dashboard.subjects}
        activeSubjectId={activeSubjectId}
        mastery={mastery}
        weeklyReport={weeklyReport}
      />
    </div>
  );
}
