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
    <div className="space-y-1.5">
      <p className="text-xs text-muted-foreground">How confident are you?</p>
      <div className="flex flex-wrap gap-2">
        {LEVELS.map((level) => (
          <button
            key={level.value}
            type="button"
            aria-pressed={value === level.value}
            onClick={() => onChange(level.value)}
            className={cn(
              "rounded-full border px-2.5 py-1 text-xs font-medium outline-none transition-colors",
              "focus-visible:ring-3 focus-visible:ring-blue/50",
              value === level.value
                ? "border-blue bg-blue text-blue-foreground"
                : "border-border hover:border-blue/40 hover:bg-blue-soft/50"
            )}
          >
            {level.label}
          </button>
        ))}
      </div>
    </div>
  );
}
