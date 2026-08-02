import { ReactNode } from "react";
import { cn } from "@/lib/utils";

/** Standard in-app page header: a big display title, a muted subline, and
 * an optional right-hand action cluster. Gives every app screen the same
 * opening rhythm. */
export function PageHeader({
  title,
  sub,
  actions,
  className,
}: {
  title: ReactNode;
  sub?: ReactNode;
  actions?: ReactNode;
  className?: string;
}) {
  return (
    <div className={cn("flex flex-wrap items-start justify-between gap-4", className)}>
      <div className="min-w-0">
        <h1 className="font-display text-balance-display text-3xl text-ink sm:text-4xl">{title}</h1>
        {sub && <p className="mt-2 text-base text-muted-foreground">{sub}</p>}
      </div>
      {actions && <div className="flex shrink-0 flex-wrap items-center gap-2">{actions}</div>}
    </div>
  );
}
