import { cn } from "@/lib/utils";

const LEVELS = [
  { value: 1, label: "Guessed" },
  { value: 2, label: "Unsure" },
  { value: 3, label: "Fairly sure" },
  { value: 4, label: "Confident" },
];

export function ConfidenceRatingInput({
  value,
  onChange,
}: {
  value: number | null | undefined;
  onChange: (rating: number) => void;
}) {
  return (
    <div className="space-y-2.5">
      <p className="text-xs font-medium text-muted-foreground">How confident are you?</p>
      <div className="flex flex-wrap gap-2">
        {LEVELS.map((level) => {
          const isSelected = value === level.value;
          return (
            <button
              key={level.value}
              type="button"
              aria-pressed={isSelected}
              onClick={() => onChange(level.value)}
              className={cn(
                "rounded-full border px-3.5 py-1.5 text-xs font-medium",
                "outline-none transition-all duration-200 focus-visible:ring-3 focus-visible:ring-blue/40",
                isSelected
                  ? "border-blue bg-blue-soft/60 text-blue"
                  : "border-border bg-card text-ink-soft hover:border-ink/15 hover:bg-muted"
              )}
            >
              {level.label}
            </button>
          );
        })}
      </div>
    </div>
  );
}
