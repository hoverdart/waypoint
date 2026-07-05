import { redirect } from "next/navigation";
import { getCurrentUser, getPracticeResults } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { ResultsView } from "@/components/results/ResultsView";

export default async function PracticeResultsPage({ params }: { params: Promise<{ id: string }> }) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { id } = await params;
  const [results, user] = await Promise.all([getPracticeResults(Number(id), token), getCurrentUser(token)]);

  return <ResultsView results={results} mode={user.mode} />;
}
