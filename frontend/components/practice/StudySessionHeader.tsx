import { Progress } from "@/components/ui/progress";

/** Replaces QuestionProgressIndicator - same question-count/progress-bar
 * logic, plus subject/topic context and (when launched from a plan item)
 * the reason it was scheduled, so "why am I doing this" carries into the
 * session itself. */
export function StudySessionHeader({
  current,
  total,
  isDiagnostic,
  subjectName,
  topicName,
  reason,
}: {
  current: number;
  total: number;
  isDiagnostic: boolean;
  subjectName?: string;
  topicName?: string;
  reason?: string;
}) {
  return (
    <div className="space-y-2">
      <div className="flex flex-wrap items-center justify-between gap-2 text-sm">
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded-full bg-blue-soft px-2.5 py-0.5 text-xs font-medium text-navy">
            {isDiagnostic ? "Diagnostic" : "Practice"}
          </span>
          {(subjectName || topicName) && (
            <span className="font-medium text-navy">
              {subjectName}
              {subjectName && topicName ? " · " : ""}
              {topicName}
            </span>
          )}
        </div>
        <span className="text-muted-foreground">
          Question {current} of {total}
        </span>
      </div>
      <Progress value={(current / total) * 100} />
      {reason && <p className="text-xs text-muted-foreground">Why this question: {reason}</p>}
    </div>
  );
}
