import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import { MasteryBar } from "@/components/shared/MasteryBar";
import { DashboardSubjectSummary } from "@/lib/api";

function daysUntil(dateStr: string | null): string | null {
  if (!dateStr) return null;
  const diff = Math.ceil((new Date(dateStr).getTime() - Date.now()) / 86_400_000);
  if (diff < 0) return "Exam passed";
  if (diff === 0) return "Exam today";
  return `${diff} days to exam`;
}

export function DashboardSubjectCard({ subject }: { subject: DashboardSubjectSummary }) {
  const countdown = daysUntil(subject.exam_date);
  return (
    <Link href={`/analytics?subject=${subject.subject_id}`}>
      <Card className="h-full transition-colors hover:bg-muted/50">
        <CardContent className="space-y-3 pt-6">
          <div className="flex items-start justify-between">
            <p className="font-medium">{subject.subject_name}</p>
            <span className="rounded-full bg-primary/10 px-2 py-0.5 text-sm font-semibold text-primary">
              {subject.predicted_ap_score}
            </span>
          </div>
          <MasteryBar score={subject.mastery_score} />
          <p className="text-xs text-muted-foreground">
            {countdown ?? "No exam date set"}
            {subject.target_score ? ` · target ${subject.target_score}` : ""}
          </p>
        </CardContent>
      </Card>
    </Link>
  );
}
