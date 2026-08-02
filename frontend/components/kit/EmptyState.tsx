import { ReactNode } from "react";
import { cn } from "@/lib/utils";

/** Shared empty state. Pass `icon` as a rendered element (not a component
 * reference) so this stays usable from Server Components - bare functions
 * aren't serializable across that boundary. */
export function EmptyState({
  icon,
  title,
  description,
  action,
  className,
}: {
  icon?: ReactNode;
  title: string;
  description?: string;
  action?: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={cn(
        "flex flex-col items-center gap-3 rounded-surface border border-dashed border-border bg-muted/30 px-6 py-12 text-center",
        className
      )}
    >
      {icon && (
        <span className="flex size-11 items-center justify-center rounded-full bg-blue-soft text-blue">{icon}</span>
      )}
      <p className="font-display text-lg text-ink">{title}</p>
      {description && <p className="max-w-sm text-sm leading-relaxed text-muted-foreground">{description}</p>}
      {action && <div className="mt-1">{action}</div>}
    </div>
  );
}

/** Route-shaped loading placeholder. */
export function LoadingRows({ rows = 3, className }: { rows?: number; className?: string }) {
  return (
    <div className={cn("space-y-3", className)} role="status" aria-label="Loading">
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="h-20 animate-pulse rounded-surface bg-muted/60" />
      ))}
    </div>
  );
}
