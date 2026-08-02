import { cn } from "@/lib/utils";

/** Tone thresholds match MasteryChip so a bar and a chip never disagree
 * about whether a topic is weak, developing or strong. */
function fillClass(score: number) {
  if (score < 0.4) return "bg-accent-coral";
  if (score < 0.7) return "bg-accent-amber";
  return "bg-accent-green";
}

export function MasteryBar({ score, className }: { score: number; className?: string }) {
  const percent = Math.round(score * 100);
  return (
    <div className={cn("space-y-1.5", className)}>
      <div
        className="h-2 w-full overflow-hidden rounded-full bg-muted"
        role="progressbar"
        aria-valuenow={percent}
        aria-valuemin={0}
        aria-valuemax={100}
      >
        <div
          className={cn("h-full rounded-full transition-all duration-500", fillClass(score))}
          style={{ width: `${percent}%` }}
        />
      </div>
      <p className="text-xs text-muted-foreground tabular-nums">{percent}% mastery</p>
    </div>
  );
}
