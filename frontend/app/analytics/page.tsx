import { redirect } from "next/navigation";
import { LineChart } from "lucide-react";
import { ApiError, getDashboard, getLatestWeeklyReport, getSubjectMastery } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { AnalyticsView } from "@/components/analytics/AnalyticsView";
import { EmptyState } from "@/components/kit/EmptyState";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

export default async function AnalyticsPage({
  searchParams,
}: {
  searchParams: Promise<{ subject?: string }>;
}) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { subject } = await searchParams;
  const dashboard = await getDashboard(token);
  requireCompletedOnboarding(dashboard.user);

  if (dashboard.subjects.length === 0) {
    return (
      <div className="mx-auto w-full max-w-6xl px-6 py-10">
        <EmptyState
          icon={<LineChart className="size-5" />}
          title="Add a subject via onboarding to see analytics here."
        />
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
    <div className="mx-auto w-full max-w-6xl px-6 py-10">
      <AnalyticsView
        enrolledSubjects={dashboard.subjects}
        activeSubjectId={activeSubjectId}
        mastery={mastery}
        weeklyReport={weeklyReport}
      />
    </div>
  );
}
