import { ReactNode } from "react";
import { CalendarClock } from "lucide-react";
import { cn } from "@/lib/utils";

type Tone = "neutral" | "blue" | "violet" | "amber" | "green" | "coral";

const TONE: Record<Tone, string> = {
  neutral: "bg-muted text-ink-soft",
  blue: "bg-blue-soft text-blue",
  violet: "bg-accent-violet-pale/50 text-accent-violet",
  amber: "bg-accent-amber/20 text-accent-amber",
  green: "bg-accent-green/15 text-accent-green",
  coral: "bg-accent-coral/15 text-accent-coral",
};

/** Small rounded label. The one badge shape used across the app. */
export function Chip({
  children,
  tone = "neutral",
  dot = false,
  className,
}: {
  children: ReactNode;
  tone?: Tone;
  dot?: boolean;
  className?: string;
}) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-medium",
        TONE[tone],
        className
      )}
    >
      {dot && <span className="size-1.5 shrink-0 rounded-full bg-current" aria-hidden="true" />}
      {children}
    </span>
  );
}

function masteryTone(score: number): Tone {
  if (score < 0.4) return "coral";
  if (score < 0.7) return "amber";
  return "green";
}

/** Mastery as a tone-coded percentage. Pass `label` to lead with a topic or
 * unit name instead of the generic tier word. */
export function MasteryChip({
  score,
  label,
  className,
}: {
  score: number;
  label?: string;
  className?: string;
}) {
  const tier = score < 0.4 ? "Weak" : score < 0.7 ? "Developing" : "Strong";
  return (
    <Chip tone={masteryTone(score)} className={className}>
      {label ?? tier} · {Math.round(score * 100)}%
    </Chip>
  );
}

/** Draws the eye to something that needs work. */
export function WeakSpotChip({ label = "Needs attention", className }: { label?: string; className?: string }) {
  return (
    <Chip tone="coral" dot className={className}>
      {label}
    </Chip>
  );
}

function daysUntil(examDate: string): number {
  const target = new Date(`${examDate}T00:00:00`);
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  return Math.ceil((target.getTime() - today.getTime()) / 86_400_000);
}

/** Days-to-exam chip. Renders nothing when no exam date is set. */
export function ExamCountdown({
  examDate,
  tone = "blue",
  className,
}: {
  examDate: string | null;
  tone?: Tone;
  className?: string;
}) {
  if (!examDate) return null;
  const days = daysUntil(examDate);
  const label =
    days < 0 ? "Exam date passed" : days === 0 ? "Exam is today" : `${days} ${days === 1 ? "day" : "days"} to exam`;

  return (
    <Chip tone={tone} className={className}>
      <CalendarClock className="size-3.5" aria-hidden="true" />
      {label}
    </Chip>
  );
}
