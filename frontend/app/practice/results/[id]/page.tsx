import { redirect } from "next/navigation";
import { getCurrentUser, getPracticeResults, getPracticeSession } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { ResultsView } from "@/components/results/ResultsView";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

export default async function PracticeResultsPage({ params }: { params: Promise<{ id: string }> }) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { id } = await params;
  const sessionId = Number(id);
  const [results, user, session] = await Promise.all([
    getPracticeResults(sessionId, token),
    getCurrentUser(token),
    getPracticeSession(sessionId, token),
  ]);
  requireCompletedOnboarding(user);

  return <ResultsView results={results} mode={user.mode} subjectId={session.subject_id} />;
}
