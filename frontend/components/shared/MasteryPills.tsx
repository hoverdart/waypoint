import { cn } from "@/lib/utils";

type MasteryTier = "weak" | "developing" | "strong";

function tierFor(masteryScore: number): MasteryTier {
  if (masteryScore < 0.4) return "weak";
  if (masteryScore < 0.7) return "developing";
  return "strong";
}

const TIER_STYLES: Record<MasteryTier, string> = {
  weak: "bg-accent-coral/15 text-accent-coral",
  developing: "bg-accent-amber/15 text-accent-amber",
  strong: "bg-accent-green/15 text-accent-green",
};

const TIER_LABEL: Record<MasteryTier, string> = {
  weak: "Weak",
  developing: "Developing",
  strong: "Strong",
};

/** Mastery-tier pill for a topic/unit/subject, replacing plain
 * `<Badge variant="outline">` usage across daily-plan and analytics. Pass
 * `label` to show a topic/unit name instead of the generic tier word
 * (e.g. in the course-detail route timeline). */
export function TopicMasteryPill({
  masteryScore,
  label,
  className,
}: {
  masteryScore: number;
  label?: string;
  className?: string;
}) {
  const tier = tierFor(masteryScore);
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium",
        TIER_STYLES[tier],
        className
      )}
    >
      {label ?? TIER_LABEL[tier]} · {Math.round(masteryScore * 100)}%
    </span>
  );
}

/** Flags a topic/unit as a weak spot needing attention - a distinct visual
 * from the general mastery-tier pill since it's meant to draw the eye. */
export function WeakSpotBadge({ label = "Needs attention", className }: { label?: string; className?: string }) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full bg-accent-coral/15 px-2.5 py-0.5 text-xs font-medium text-accent-coral",
        className
      )}
    >
      <span className="size-1.5 rounded-full bg-accent-coral" aria-hidden="true" />
      {label}
    </span>
  );
}
