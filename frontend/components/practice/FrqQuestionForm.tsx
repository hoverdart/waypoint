import { useId } from "react";
import { Textarea } from "@/components/ui/textarea";

export function FrqQuestionForm({
  value,
  onChange,
}: {
  value: string;
  onChange: (text: string) => void;
}) {
  const id = useId();
  const words = value.trim() ? value.trim().split(/\s+/).length : 0;
  return (
    <div className="space-y-2">
      <label htmlFor={id} className="text-sm font-medium">Your response</label>
      <Textarea
        id={id}
        aria-describedby={`${id}-count`}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        rows={12}
        maxLength={20000}
        placeholder="Write your response here..."
        className="min-h-64 rounded-2xl border-border bg-card px-4 py-3.5 text-base leading-relaxed text-ink transition-all duration-200 focus-visible:border-blue focus-visible:ring-3 focus-visible:ring-blue/40 md:text-base"
      />
      <p id={`${id}-count`} className="text-xs text-muted-foreground">{words} {words === 1 ? "word" : "words"} · {value.length.toLocaleString()} / 20,000 characters</p>
    </div>
  );
}
