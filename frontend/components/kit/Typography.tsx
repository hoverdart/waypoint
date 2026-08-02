import type { CSSProperties, ReactNode } from "react";
import { cn } from "@/lib/utils";

/** Marker-pen highlight behind a phrase. The signature emphasis device of
 * this design language - used instead of bold or colored text for the one
 * phrase that matters most in a headline. */
export function Highlight({
  children,
  tone = "blue",
  animated = false,
  className,
}: {
  children: ReactNode;
  tone?: "blue" | "violet" | "amber" | "green";
  /** Draw the marker in after its surrounding copy has entered. */
  animated?: boolean;
  className?: string;
}) {
  const TONE = {
    blue: "var(--blue-pale)",
    violet: "var(--accent-violet-pale)",
    amber: "var(--accent-amber)",
    green: "var(--accent-green)",
  } as const;

  // A background gradient, rather than padding or an absolutely positioned
  // child, follows every line fragment without changing the heading's line
  // box. That keeps a wrapped highlight from crowding the surrounding copy.
  return (
    <span
      style={{ "--highlight-color": TONE[tone] } as CSSProperties}
      className={cn(
        "highlight-marker",
        animated && "highlight-marker--animate",
        className
      )}
    >
      {children}
    </span>
  );
}

/** Small uppercase label that sits above a heading. */
export function Eyebrow({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <p className={cn("text-xs font-semibold tracking-[0.14em] text-blue uppercase", className)}>{children}</p>
  );
}

/** Centered or left-aligned section header: eyebrow, big display title, and
 * an optional muted subline. Keeps section rhythm identical everywhere. */
export function SectionHeading({
  eyebrow,
  title,
  sub,
  align = "center",
  className,
}: {
  eyebrow?: string;
  title: ReactNode;
  sub?: ReactNode;
  align?: "center" | "left";
  className?: string;
}) {
  return (
    <div className={cn("max-w-2xl", align === "center" && "mx-auto text-center", className)}>
      {eyebrow && <Eyebrow className="mb-3">{eyebrow}</Eyebrow>}
      <h2 className="font-display text-balance-display text-3xl text-ink sm:text-4xl md:text-[2.75rem]">{title}</h2>
      {sub && <p className="mt-4 text-base leading-relaxed text-muted-foreground sm:text-lg">{sub}</p>}
    </div>
  );
}
