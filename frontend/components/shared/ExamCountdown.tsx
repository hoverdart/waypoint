import { CalendarClock } from "lucide-react";
import { cn } from "@/lib/utils";

function daysUntil(examDate: string): number {
  const target = new Date(`${examDate}T00:00:00`);
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  return Math.ceil((target.getTime() - today.getTime()) / (1000 * 60 * 60 * 24));
}

/** Days-to-exam pill, reused in the header, dashboard, and course-detail
 * page. Renders nothing if the subject has no exam date set yet. */
export function ExamCountdown({
  examDate,
  subjectName,
  tone = "light",
  className,
}: {
  examDate: string | null;
  subjectName?: string;
  tone?: "light" | "dark";
  className?: string;
}) {
  if (!examDate) return null;
  const days = daysUntil(examDate);
  const label = days < 0 ? "Exam date passed" : days === 0 ? "Exam is today" : `${days} ${days === 1 ? "day" : "days"} to exam`;

  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-medium",
        tone === "dark" ? "bg-white/10 text-navy-foreground" : "bg-blue-soft text-navy",
        className
      )}
    >
      <CalendarClock className="size-3.5" aria-hidden="true" />
      {subjectName ? `${subjectName} · ${label}` : label}
    </span>
  );
}
