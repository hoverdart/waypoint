import { Textarea } from "@/components/ui/textarea";

export function FrqQuestionForm({
  value,
  onChange,
}: {
  value: string;
  onChange: (text: string) => void;
}) {
  return (
    <Textarea
      value={value}
      onChange={(e) => onChange(e.target.value)}
      rows={8}
      placeholder="Write your response here..."
      className="min-h-44 rounded-2xl border-border bg-card px-4 py-3.5 text-base leading-relaxed text-ink transition-all duration-200 focus-visible:border-blue focus-visible:ring-3 focus-visible:ring-blue/40 md:text-base"
    />
  );
}
