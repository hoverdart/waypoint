import { redirect } from "next/navigation";
import { getDashboard, getSubject } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { buildTopicNameMap } from "@/lib/planItemLabels";
import { DashboardView } from "@/components/dashboard/DashboardView";

export default async function DashboardPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const data = await getDashboard(token);
  const subjectDetails = await Promise.all(data.subjects.map((s) => getSubject(s.subject_id)));
  const topicNames = buildTopicNameMap(subjectDetails);

  return (
    <div className="mx-auto w-full max-w-6xl px-4 py-8">
      <DashboardView data={data} topicNames={topicNames} />
    </div>
  );
}
