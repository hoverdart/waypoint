import { redirect } from "next/navigation";
import { getDashboard, getSubjects } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { PageHeader } from "@/components/kit/PageHeader";
import { Reveal } from "@/components/motion/Reveal";
import { SubjectGrid } from "@/components/subjects/SubjectGrid";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

export default async function SubjectsPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const [allSubjects, dashboard] = await Promise.all([getSubjects(), getDashboard(token)]);
  requireCompletedOnboarding(dashboard.user);

  return (
    <div className="mx-auto w-full max-w-6xl space-y-10 px-6 py-10">
      <Reveal>
        <PageHeader title="Subjects" sub="All AP subjects WayPoint currently supports." />
      </Reveal>
      <SubjectGrid allSubjects={allSubjects} enrolled={dashboard.subjects} />
    </div>
  );
}
