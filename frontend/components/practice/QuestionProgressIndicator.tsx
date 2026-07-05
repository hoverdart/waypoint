import { Progress } from "@/components/ui/progress";

export function QuestionProgressIndicator({
  current,
  total,
  isDiagnostic,
}: {
  current: number;
  total: number;
  isDiagnostic: boolean;
}) {
  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between text-sm text-muted-foreground">
        <span>{isDiagnostic ? "Diagnostic" : "Practice"}</span>
        <span>
          Question {current} of {total}
        </span>
      </div>
      <Progress value={(current / total) * 100} />
    </div>
  );
}
