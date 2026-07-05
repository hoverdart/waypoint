import { redirect } from "next/navigation";
import { getPracticeSession } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { PracticeSessionRoot } from "@/components/practice/PracticeSessionRoot";

export default async function PracticeSessionPage({
  params,
  searchParams,
}: {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ planItemId?: string }>;
}) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { id } = await params;
  const { planItemId } = await searchParams;
  const sessionId = Number(id);

  const session = await getPracticeSession(sessionId, token);
  if (session.is_completed) {
    redirect(`/practice/results/${sessionId}`);
  }

  return (
    <PracticeSessionRoot
      sessionId={session.session_id}
      sessionType={session.session_type}
      questions={session.questions}
      planItemId={planItemId ? Number(planItemId) : undefined}
    />
  );
}
