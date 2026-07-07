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
      className="rounded-xl border-border/80 focus-visible:ring-blue/50"
    />
  );
}
