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
    <div className="space-y-2">
      {question.options.map((option) => (
        <button
          key={option.id}
          type="button"
          onClick={() => onSelect(option.id)}
          aria-pressed={selectedOptionId === option.id}
          className={cn(
            "w-full rounded-xl border p-3 text-left text-sm outline-none transition-colors",
            "focus-visible:ring-3 focus-visible:ring-blue/50",
            selectedOptionId === option.id
              ? "border-blue bg-blue-soft/60"
              : "border-border hover:border-blue/30 hover:bg-blue-soft/30"
          )}
        >
          <span className="mr-2 font-medium text-navy">{option.label}.</span>
          {option.text}
        </button>
      ))}
    </div>
  );
}
