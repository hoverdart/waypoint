import { Progress } from "@/components/ui/progress";

const XP_PER_LEVEL = 100;

export function XpBar({ totalXp }: { totalXp: number }) {
  const level = Math.floor(totalXp / XP_PER_LEVEL) + 1;
  const xpIntoLevel = totalXp % XP_PER_LEVEL;

  return (
    <div className="space-y-1.5">
      <div className="flex items-center justify-between text-sm">
        <span className="font-medium">Level {level}</span>
        <span className="text-muted-foreground">
          {xpIntoLevel}/{XP_PER_LEVEL} XP · {totalXp} total
        </span>
      </div>
      <Progress value={xpIntoLevel} max={XP_PER_LEVEL} />
    </div>
  );
}
