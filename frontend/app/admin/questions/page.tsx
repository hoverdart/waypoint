import Link from "next/link";
import { redirect } from "next/navigation";
import { ApiError, listAdminQuestions } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { AdminQuestionsTable } from "@/components/admin/AdminQuestionsTable";
import { Card, CardContent } from "@/components/ui/card";

const STATUSES = ["draft", "needs_review", "approved", "rejected"] as const;

export default async function AdminQuestionsPage({
  searchParams,
}: {
  searchParams: Promise<{ status?: string }>;
}) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const { status } = await searchParams;

  let questions;
  try {
    questions = await listAdminQuestions({ validation_status: status }, token);
  } catch (e) {
    if (e instanceof ApiError && (e.status === 403 || e.status === 401)) {
      return (
        <div className="mx-auto w-full max-w-md px-4 py-16">
          <Card>
            <CardContent className="pt-6 text-center text-muted-foreground">
              You don&apos;t have access to this page.
            </CardContent>
          </Card>
        </div>
      );
    }
    throw e;
  }

  return (
    <div className="mx-auto w-full max-w-5xl space-y-6 px-4 py-8">
      <h1 className="text-2xl font-semibold tracking-tight">Question review</h1>
      <div className="flex gap-2 text-sm">
        <Link href="/admin/questions" className={!status ? "font-medium" : "text-muted-foreground"}>
          All
        </Link>
        {STATUSES.map((s) => (
          <Link
            key={s}
            href={`/admin/questions?status=${s}`}
            className={status === s ? "font-medium" : "text-muted-foreground"}
          >
            {s}
          </Link>
        ))}
      </div>
      <AdminQuestionsTable questions={questions} />
    </div>
  );
}
