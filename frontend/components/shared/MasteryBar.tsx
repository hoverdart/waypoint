import { cn } from "@/lib/utils";

export function MasteryBar({ score, className }: { score: number; className?: string }) {
  const percent = Math.round(score * 100);
  return (
    <div className={cn("space-y-1", className)}>
      <div className="h-2 w-full overflow-hidden rounded-full bg-muted">
        <div
          className="h-full rounded-full bg-primary transition-all"
          style={{ width: `${percent}%` }}
        />
      </div>
      <p className="text-xs text-muted-foreground">{percent}% mastery</p>
    </div>
  );
}
