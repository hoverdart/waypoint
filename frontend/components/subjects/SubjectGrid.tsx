import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import { MasteryBar } from "@/components/shared/MasteryBar";
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
          <Card key={subject.id} className={summary ? undefined : "opacity-60"}>
            <CardContent className="space-y-3 pt-6">
              <div className="flex items-start justify-between">
                <p className="font-medium">{subject.name}</p>
                {summary && (
                  <span className="rounded-full bg-primary/10 px-2 py-0.5 text-sm font-semibold text-primary">
                    {summary.predicted_ap_score}
                  </span>
                )}
              </div>
              <p className="text-xs text-muted-foreground">{subject.description}</p>

              {summary ? (
                <>
                  <MasteryBar score={summary.mastery_score} />
                  <div className="flex items-center justify-between">
                    <Link
                      href={`/analytics?subject=${subject.id}`}
                      className="text-xs text-muted-foreground underline underline-offset-2"
                    >
                      View analytics
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
          </Card>
        );
      })}
    </div>
  );
}
