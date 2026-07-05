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
          className={cn(
            "w-full rounded-lg border p-3 text-left text-sm transition-colors",
            selectedOptionId === option.id ? "border-primary bg-primary/5" : "hover:bg-muted"
          )}
        >
          <span className="mr-2 font-medium">{option.label}.</span>
          {option.text}
        </button>
      ))}
    </div>
  );
}
