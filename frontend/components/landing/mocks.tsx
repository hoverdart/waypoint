import { ReactNode } from "react";
import { Check, Compass, Sparkles } from "lucide-react";
import { cn } from "@/lib/utils";

/** Stylised WayPoint UI shown in marketing surfaces. Deliberately static and
 * hook-free so these stay server-renderable and can be passed as JSX slots
 * into client components like ScrollScene. */
function AppFrame({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div
      className={cn(
        "w-full max-w-sm rounded-surface border border-border/70 bg-card p-5 shadow-lift",
        className
      )}
    >
      <div className="mb-4 flex items-center gap-1.5" aria-hidden="true">
        <span className="size-2 rounded-full bg-accent-coral/50" />
        <span className="size-2 rounded-full bg-accent-amber/50" />
        <span className="size-2 rounded-full bg-accent-green/50" />
      </div>
      {children}
    </div>
  );
}

const PLAN_ROWS = [
  { topic: "Implicit differentiation", reason: "Your mastery dropped", pts: "25 pts", done: true },
  { topic: "Related rates", reason: "High-frequency on the exam", pts: "25 pts", done: false },
  { topic: "Unit 3 free response", reason: "You haven't practiced recently", pts: "40 pts", done: false },
];

/** The product's core artefact: today's plan, with the reason behind each pick. */
export function PlanMock() {
  return (
    <AppFrame>
      <p className="text-[0.65rem] font-semibold tracking-[0.14em] text-blue uppercase">Today&apos;s route</p>
      <p className="font-display mt-1 text-lg text-ink">3 stops · 90 pts</p>

      <ul className="mt-4 space-y-2">
        {PLAN_ROWS.map((row) => (
          <li key={row.topic} className="flex items-start gap-2.5 rounded-2xl border border-border/60 bg-muted/40 p-3">
            <span
              className={cn(
                "mt-0.5 flex size-5 shrink-0 items-center justify-center rounded-full",
                row.done ? "bg-accent-green text-white" : "border-2 border-border"
              )}
              aria-hidden="true"
            >
              {row.done && <Check className="size-3" strokeWidth={3} />}
            </span>
            <span className="min-w-0">
              <span className="block truncate text-[0.8rem] font-medium text-ink">{row.topic}</span>
              <span className="block truncate text-[0.7rem] text-muted-foreground">{row.reason}</span>
            </span>
            <span className="ml-auto shrink-0 text-[0.7rem] text-muted-foreground">{row.pts}</span>
          </li>
        ))}
      </ul>
    </AppFrame>
  );
}

/** A diagnostic question, mid-answer. */
export function DiagnoseMock() {
  const options = ["Hydrolysis", "Dehydration synthesis", "Condensation", "Phosphorylation"];
  return (
    <AppFrame>
      <div className="flex items-center justify-between text-[0.7rem] text-muted-foreground">
        <span className="rounded-full bg-blue-soft px-2 py-0.5 font-medium text-blue">Diagnostic</span>
        <span>Question 4 of 20</span>
      </div>
      <div className="mt-3 h-1 w-full overflow-hidden rounded-full bg-muted">
        <div className="h-full w-1/5 rounded-full bg-blue" />
      </div>

      <p className="mt-4 text-[0.8rem] leading-relaxed text-ink">
        A macromolecule breaks into subunits when water is added. This process is best described as:
      </p>

      <ul className="mt-3 space-y-1.5">
        {options.map((opt, i) => (
          <li
            key={opt}
            className={cn(
              "rounded-xl border p-2.5 text-[0.78rem]",
              i === 0 ? "border-blue bg-blue-soft/60 text-ink" : "border-border text-ink-soft"
            )}
          >
            <span className="mr-1.5 font-medium text-ink">{String.fromCharCode(65 + i)}.</span>
            {opt}
          </li>
        ))}
      </ul>
    </AppFrame>
  );
}

const UNITS = [
  { name: "Limits", score: 0.86 },
  { name: "Derivatives", score: 0.64 },
  { name: "Integrals", score: 0.31 },
];

/** Mastery rolling up per unit, with a readiness read-out. */
export function MasteryMock() {
  return (
    <AppFrame>
      <div className="flex items-center gap-4">
        <div className="relative size-20 shrink-0">
          <svg viewBox="0 0 80 80" className="-rotate-90" aria-hidden="true">
            <circle cx="40" cy="40" r="34" fill="none" stroke="var(--border)" strokeWidth="8" />
            <circle
              cx="40"
              cy="40"
              r="34"
              fill="none"
              stroke="var(--blue)"
              strokeWidth="8"
              strokeLinecap="round"
              strokeDasharray={2 * Math.PI * 34}
              strokeDashoffset={2 * Math.PI * 34 * (1 - 0.68)}
            />
          </svg>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="font-display text-base text-ink">68%</span>
            <span className="text-[0.55rem] text-muted-foreground">ready</span>
          </div>
        </div>
        <div>
          <p className="text-[0.7rem] font-semibold tracking-[0.14em] text-blue uppercase">Predicted</p>
          <p className="font-display text-2xl text-ink">4</p>
          <p className="text-[0.7rem] text-muted-foreground">32 days to exam</p>
        </div>
      </div>

      <ul className="mt-4 space-y-2">
        {UNITS.map((unit) => (
          <li key={unit.name}>
            <div className="flex items-center justify-between text-[0.72rem]">
              <span className="text-ink">{unit.name}</span>
              <span className="text-muted-foreground">{Math.round(unit.score * 100)}%</span>
            </div>
            <div className="mt-1 h-1.5 w-full overflow-hidden rounded-full bg-muted">
              <div
                className={cn(
                  "h-full rounded-full",
                  unit.score < 0.4 ? "bg-accent-coral" : unit.score < 0.7 ? "bg-accent-amber" : "bg-accent-green"
                )}
                style={{ width: `${unit.score * 100}%` }}
              />
            </div>
          </li>
        ))}
      </ul>
    </AppFrame>
  );
}

/** Small side-by-side of the two personality modes. */
export function ModesMock() {
  return (
    <div className="grid w-full max-w-sm gap-3 sm:grid-cols-2">
      {[
        { icon: <Compass className="size-4" aria-hidden="true" />, name: "Professional", note: "Mastery analytics" },
        { icon: <Sparkles className="size-4" aria-hidden="true" />, name: "Gamified", note: "XP, streaks, quests" },
      ].map((mode) => (
        <div key={mode.name} className="rounded-2xl border border-border/70 bg-card p-4 shadow-hairline">
          <span className="flex size-8 items-center justify-center rounded-full bg-blue-soft text-blue">
            {mode.icon}
          </span>
          <p className="font-display mt-3 text-sm text-ink">{mode.name}</p>
          <p className="text-[0.7rem] text-muted-foreground">{mode.note}</p>
        </div>
      ))}
    </div>
  );
}
