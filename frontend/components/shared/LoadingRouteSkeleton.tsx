import { cn } from "@/lib/utils";

/** Shared loading placeholder for route-shaped content (plan lists, subject
 * grids, mastery tables) - a handful of pulsing bars instead of every view
 * hand-rolling its own. */
export function LoadingRouteSkeleton({ rows = 3, className }: { rows?: number; className?: string }) {
  return (
    <div className={cn("space-y-3", className)} role="status" aria-label="Loading">
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="h-20 animate-pulse rounded-2xl bg-muted/60" />
      ))}
    </div>
  );
}
