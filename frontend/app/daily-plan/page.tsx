import { redirect } from "next/navigation";
import { getDashboard, getSubject, getTodayPlan } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { DailyPlanView } from "@/components/daily-plan/DailyPlanView";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

export default async function DailyPlanPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const [plans, dashboard] = await Promise.all([getTodayPlan(token), getDashboard(token)]);
  requireCompletedOnboarding(dashboard.user);

  const subjectDetails = await Promise.all(
    dashboard.subjects.map((s) => getSubject(s.subject_id))
  );

  return (
    <div className="mx-auto w-full max-w-4xl px-6 py-10">
      <DailyPlanView
        plans={plans}
        subjectDetails={subjectDetails}
        enrolledSubjects={dashboard.subjects}
        mode={dashboard.user.mode}
        streakDays={dashboard.streak_days}
      />
    </div>
  );
}
