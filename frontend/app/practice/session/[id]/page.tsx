import { redirect } from "next/navigation";
import { getCurrentUser, getPracticeSession, getSubject, getTodayPlan } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { PracticeSessionRoot } from "@/components/practice/PracticeSessionRoot";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

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
  const parsedPlanItemId = planItemId ? Number(planItemId) : undefined;

  const [session, user] = await Promise.all([getPracticeSession(sessionId, token), getCurrentUser(token)]);
  requireCompletedOnboarding(user);
  if (session.is_completed) {
    redirect(`/practice/results/${sessionId}`);
  }

  const firstQuestion = session.questions[0];
  let subjectName: string | undefined;
  let topicName: string | undefined;
  let reason: string | undefined;

  if (firstQuestion) {
    try {
      const subject = await getSubject(firstQuestion.subject_id);
      subjectName = subject.name;
      topicName = subject.units.flatMap((u) => u.topics).find((t) => t.id === firstQuestion.topic_id)?.name;
    } catch {
      // context is a nice-to-have - the session still works without it
    }
  }

  if (parsedPlanItemId) {
    try {
      const plans = await getTodayPlan(token);
      reason = plans.flatMap((p) => p.items).find((i) => i.id === parsedPlanItemId)?.reason;
    } catch {
      // same as above - best-effort context
    }
  }

  return (
    <PracticeSessionRoot
      sessionId={session.session_id}
      sessionType={session.session_type}
      questions={session.questions}
      planItemId={parsedPlanItemId}
      subjectName={subjectName}
      topicName={topicName}
      reason={reason}
    />
  );
}
