import { Surface } from "@/components/kit/Surface";
import { Chip } from "@/components/kit/Pills";
import { PillLink } from "@/components/kit/PillButton";
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
          // Not-yet-added subjects drop the card fill instead of fading out:
          // they read as de-emphasised without dimming their text.
          <Surface
            key={subject.id}
            tone={summary ? "default" : "quiet"}
            className="flex h-full flex-col gap-4 p-6"
          >
            <div className="flex items-start justify-between gap-3">
              <p className="font-display text-base leading-snug text-ink">{subject.name}</p>
              {summary && (
                <Chip tone="blue" className="shrink-0 font-semibold tabular-nums">
                  {summary.predicted_ap_score}
                </Chip>
              )}
            </div>
            <p className="text-sm leading-relaxed text-muted-foreground">{subject.description}</p>

            {summary ? (
              <div className="mt-auto space-y-4 pt-1">
                <MasteryBar score={summary.mastery_score} />
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <PillLink href={`/analytics?subject=${subject.id}`} variant="ghost" size="sm">
                    View analytics
                  </PillLink>
                  <DiagnosticStartButton subjectId={subject.id} />
                </div>
              </div>
            ) : (
              <p className="mt-auto text-xs text-muted-foreground">
                Not added yet - visit onboarding to add this subject.
              </p>
            )}
          </Surface>
        );
      })}
    </div>
  );
}
