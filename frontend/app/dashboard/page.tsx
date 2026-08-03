import { redirect } from "next/navigation";
import { getDashboard, getSubject } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { DashboardView } from "@/components/dashboard/DashboardView";
import { buildTopicNameMap } from "@/lib/planItemLabels";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

export default async function DashboardPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const data = await getDashboard(token);
  requireCompletedOnboarding(data.user);
  // The compact dashboard cards still need friendly topic labels for the next
  // route item. Fetching the enrolled subject details keeps that context out
  // of the dashboard API response and matches the pre-redesign contract.
  const subjectDetails = await Promise.all(data.subjects.map((subject) => getSubject(subject.subject_id)));
  const topicNames = buildTopicNameMap(subjectDetails);
  return (
    <div className="mx-auto w-full max-w-6xl px-6 py-10">
      <DashboardView data={data} topicNames={topicNames} />
    </div>
  );
}
