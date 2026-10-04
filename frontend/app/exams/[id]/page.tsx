import { notFound, redirect } from "next/navigation";
import { ApiError } from "@/lib/api/client";
import { getExam } from "@/lib/api/exams";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { ExamSessionRoot } from "@/components/exams/ExamSessionRoot";

export default async function ExamPage({ params }: { params: Promise<{ id: string }> }) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");
  const { id } = await params;
  const sessionId = Number(id);
  if (!Number.isSafeInteger(sessionId) || sessionId < 1) notFound();
  const exam = await getExam(sessionId, token).catch(error => {
    if (error instanceof ApiError && error.status === 404) notFound();
    throw error;
  });
  if (exam.completed) redirect(`/practice/results/${sessionId}`);
  return <ExamSessionRoot initialExam={exam} />;
}
