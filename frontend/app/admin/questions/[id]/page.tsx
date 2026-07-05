import { redirect } from "next/navigation";
import { ApiError, getAdminQuestion } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { AdminQuestionEditor } from "@/components/admin/AdminQuestionEditor";
import { Card, CardContent } from "@/components/ui/card";

export default async function AdminQuestionDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { id } = await params;

  let question;
  try {
    question = await getAdminQuestion(Number(id), token);
  } catch (e) {
    if (e instanceof ApiError && (e.status === 403 || e.status === 401 || e.status === 404)) {
      return (
        <div className="mx-auto w-full max-w-md px-4 py-16">
          <Card>
            <CardContent className="pt-6 text-center text-muted-foreground">
              {e.status === 404 ? "Question not found." : "You don't have access to this page."}
            </CardContent>
          </Card>
        </div>
      );
    }
    throw e;
  }

  return (
    <div className="mx-auto w-full max-w-3xl px-4 py-8">
      <AdminQuestionEditor question={question} />
    </div>
  );
}
