import Link from "next/link";
import { cn } from "@/lib/utils";
import { DashboardSubjectSummary } from "@/lib/api";

export function SubjectFilterTabs({
  subjects,
  activeSubjectId,
}: {
  subjects: DashboardSubjectSummary[];
  activeSubjectId: number;
}) {
  return (
    <div className="flex flex-wrap gap-2 border-b pb-3">
      {subjects.map((subject) => (
        <Link
          key={subject.subject_id}
          href={`/analytics?subject=${subject.subject_id}`}
          className={cn(
            "rounded-full px-3 py-1.5 text-sm transition-colors",
            subject.subject_id === activeSubjectId
              ? "bg-primary text-primary-foreground"
              : "text-muted-foreground hover:bg-muted"
          )}
        >
          {subject.subject_name}
        </Link>
      ))}
    </div>
  );
}
