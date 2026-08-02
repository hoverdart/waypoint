import { ComponentProps } from "react";
import { cn } from "@/lib/utils";

/** The single card primitive for the whole app: a large-radius white panel
 * with a hairline border and a shadow you can barely see. Depth reads from
 * the tinted page behind it, not from the shadow.
 *
 * `tone="raised"` adds a slightly stronger lift for hero-level panels;
 * `tone="quiet"` drops the fill for nested groupings inside a Surface. */
export function Surface({
  className,
  tone = "default",
  interactive = false,
  ...props
}: ComponentProps<"div"> & { tone?: "default" | "raised" | "quiet"; interactive?: boolean }) {
  return (
    <div
      className={cn(
        "rounded-surface border border-border/70",
        tone === "default" && "bg-card shadow-hairline",
        tone === "raised" && "bg-card shadow-lift",
        tone === "quiet" && "bg-muted/40",
        interactive &&
          "transition-all duration-300 hover:-translate-y-0.5 hover:border-blue/30 hover:shadow-lift",
        className
      )}
      {...props}
    />
  );
}
