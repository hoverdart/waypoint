import { ReactNode } from "react";
import { cn } from "@/lib/utils";

/** Shared empty-state treatment - pass the icon as a rendered JSX element
 * (not a bare component reference) since this can be used from Server
 * Components and raw function props aren't serializable across that
 * boundary. */
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
        "flex flex-col items-center gap-2 rounded-2xl border border-dashed border-border/70 bg-muted/30 px-6 py-10 text-center",
        className
      )}
    >
      {icon && (
        <span className="flex size-10 items-center justify-center rounded-full bg-blue-soft text-navy">{icon}</span>
      )}
      <p className="font-heading text-base font-semibold text-navy">{title}</p>
      {description && <p className="max-w-sm text-sm text-muted-foreground">{description}</p>}
      {action}
    </div>
  );
}
