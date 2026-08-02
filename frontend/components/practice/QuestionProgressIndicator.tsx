import { Eyebrow } from "@/components/kit/Typography";

export function QuestionProgressIndicator({
  current,
  total,
  isDiagnostic,
}: {
  current: number;
  total: number;
  isDiagnostic: boolean;
}) {
  const percent = (current / total) * 100;

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between gap-3">
        <Eyebrow>{isDiagnostic ? "Diagnostic" : "Practice"}</Eyebrow>
        <span className="text-xs text-muted-foreground tabular-nums">
          Question {current} of {total}
        </span>
      </div>
      {/* Hand-rolled track rather than the shadcn Progress, matching XpBar:
       * that one carries its own radius and primary fill, which have to be
       * overridden at the call site to reach this design language's bar. */}
      <div
        className="h-2 w-full overflow-hidden rounded-full bg-muted"
        role="progressbar"
        aria-valuenow={current}
        aria-valuemin={0}
        aria-valuemax={total}
      >
        <div
          className="h-full rounded-full bg-blue transition-all duration-500"
          style={{ width: `${percent}%` }}
        />
      </div>
    </div>
  );
}
