import Link from "next/link";
import { CardContent } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { TopicMasteryPill } from "@/components/shared/MasteryPills";
import { DashboardSubjectSummary, Subject } from "@/lib/api";
import { DiagnosticStartButton } from "./DiagnosticStartButton";

export function SubjectGrid({
  allSubjects,
  enrolled,
}: {
  allSubjects: Subject[];
  enrolled: DashboardSubjectSummary[];
}) {
  const enrolledById = new Map(enrolled.map((s) => [s.subject_id, s]));

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {allSubjects.map((subject) => {
        const summary = enrolledById.get(subject.id);
        return (
          <WayPointCard key={subject.id} className={summary ? undefined : "opacity-60"}>
            <CardContent className="space-y-3 p-5">
              <div className="flex items-start justify-between gap-2">
                <p className="font-heading font-semibold text-navy">{subject.name}</p>
                {summary && (
                  <span className="shrink-0 rounded-full bg-blue-soft px-2.5 py-0.5 text-sm font-semibold text-navy">
                    {summary.predicted_ap_score}
                  </span>
                )}
              </div>
              <p className="text-xs text-muted-foreground">{subject.description}</p>

              {summary ? (
                <>
                  <TopicMasteryPill masteryScore={summary.mastery_score} />
                  <div className="flex items-center justify-between pt-1">
                    <Link
                      href={`/analytics?subject=${subject.id}`}
                      className="text-xs font-medium text-blue underline-offset-2 hover:underline"
                    >
                      View course
                    </Link>
                    <DiagnosticStartButton subjectId={subject.id} />
                  </div>
                </>
              ) : (
                <p className="text-xs text-muted-foreground">
                  Not added yet - visit onboarding to add this subject.
                </p>
              )}
            </CardContent>
          </WayPointCard>
        );
      })}
    </div>
  );
}
