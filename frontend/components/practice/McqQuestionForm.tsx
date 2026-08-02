import { cn } from "@/lib/utils";
import { Question } from "@/lib/api";

export function McqQuestionForm({
  question,
  selectedOptionId,
  onSelect,
}: {
  question: Question;
  selectedOptionId: number | null | undefined;
  onSelect: (optionId: number) => void;
}) {
  return (
    <div className="space-y-2.5">
      {question.options.map((option) => {
        const isSelected = selectedOptionId === option.id;
        return (
          <button
            key={option.id}
            type="button"
            aria-pressed={isSelected}
            onClick={() => onSelect(option.id)}
            className={cn(
              "flex w-full items-baseline gap-3 rounded-2xl border p-4 text-left text-[0.9375rem] leading-relaxed",
              "outline-none transition-all duration-200 focus-visible:ring-3 focus-visible:ring-blue/40",
              isSelected
                ? "border-blue bg-blue-soft/60 text-ink"
                : "border-border bg-card text-ink hover:border-ink/15 hover:bg-blue-soft/30"
            )}
          >
            <span className={cn("shrink-0 font-medium", isSelected ? "text-blue" : "text-ink-soft")}>
              {option.label}.
            </span>
            <span>{option.text}</span>
          </button>
        );
      })}
    </div>
  );
}
