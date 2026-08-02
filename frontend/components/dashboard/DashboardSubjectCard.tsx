import Link from "next/link";
import { Surface } from "@/components/kit/Surface";
import { Chip } from "@/components/kit/Pills";
import { MasteryBar } from "@/components/shared/MasteryBar";
import { DashboardSubjectSummary } from "@/lib/api";

/** Kept local rather than swapped for the kit's ExamCountdown: that one words
 * the same states differently ("Exam date passed", "Exam is today"), and this
 * copy is asserted verbatim. */
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
    <Link
      href={`/analytics?subject=${subject.subject_id}`}
      className="block h-full rounded-surface outline-none focus-visible:ring-3 focus-visible:ring-blue/40"
    >
      <Surface interactive className="flex h-full flex-col gap-5 p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="font-display text-base leading-snug text-ink">{subject.subject_name}</p>
          <Chip tone="blue" className="shrink-0 font-semibold tabular-nums">
            {subject.predicted_ap_score}
          </Chip>
        </div>
        <div className="mt-auto space-y-2.5">
          <MasteryBar score={subject.mastery_score} />
          <p className="text-xs text-muted-foreground">
            {countdown ?? "No exam date set"}
            {subject.target_score ? ` · target ${subject.target_score}` : ""}
          </p>
        </div>
      </Surface>
    </Link>
  );
}
