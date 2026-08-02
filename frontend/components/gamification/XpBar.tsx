const XP_PER_LEVEL = 100;

export function XpBar({ totalXp }: { totalXp: number }) {
  const level = Math.floor(totalXp / XP_PER_LEVEL) + 1;
  const xpIntoLevel = totalXp % XP_PER_LEVEL;

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <span className="font-display text-lg text-ink">Level {level}</span>
        <span className="text-sm text-muted-foreground tabular-nums">
          {xpIntoLevel}/{XP_PER_LEVEL} XP · {totalXp} total
        </span>
      </div>
      {/* Hand-rolled track rather than the shadcn Progress: that one carries
       * its own radius and primary fill, which have to be overridden at the
       * call site to reach this design language's hairline pill bar. */}
      <div
        className="h-2 w-full overflow-hidden rounded-full bg-muted"
        role="progressbar"
        aria-valuenow={xpIntoLevel}
        aria-valuemin={0}
        aria-valuemax={XP_PER_LEVEL}
      >
        <div
          className="h-full rounded-full bg-blue transition-all duration-500"
          style={{ width: `${xpIntoLevel}%` }}
        />
      </div>
    </div>
  );
}
