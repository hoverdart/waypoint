import { PillLink } from "@/components/kit/PillButton";
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
    <div className="flex flex-wrap gap-2">
      {subjects.map((subject) => {
        const isActive = subject.subject_id === activeSubjectId;
        return (
          <PillLink
            key={subject.subject_id}
            href={`/analytics?subject=${subject.subject_id}`}
            variant={isActive ? "secondary" : "ghost"}
            size="sm"
            className={cn(isActive && "border-blue bg-blue-soft/60 text-ink hover:bg-blue-soft/60")}
          >
            {subject.subject_name}
          </PillLink>
        );
      })}
    </div>
  );
}
