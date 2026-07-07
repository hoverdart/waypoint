import { redirect } from "next/navigation";
import { getDashboard, getSubjects } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { SubjectGrid } from "@/components/subjects/SubjectGrid";

export default async function SubjectsPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const [allSubjects, dashboard] = await Promise.all([getSubjects(), getDashboard(token)]);

  return (
    <div className="mx-auto w-full max-w-6xl space-y-6 px-4 py-8">
      <div>
        <h1 className="font-heading text-2xl font-semibold tracking-tight text-navy sm:text-3xl">
          Your AP courses
        </h1>
        <p className="text-muted-foreground">Every subject WayPoint plots a study route for.</p>
      </div>
      <SubjectGrid allSubjects={allSubjects} enrolled={dashboard.subjects} />
    </div>
  );
}
