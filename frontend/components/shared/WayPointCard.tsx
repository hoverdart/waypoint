import { ComponentProps } from "react";
import { Card } from "@/components/ui/card";
import { cn } from "@/lib/utils";

/** The rounded-3xl + soft navy shadow card treatment already established in
 * onboarding, extracted so redesigned surfaces share one card primitive
 * instead of bare shadcn Card. */
export function WayPointCard({
  className,
  elevated = false,
  ...props
}: ComponentProps<typeof Card> & { elevated?: boolean }) {
  return (
    <Card
      className={cn(
        "rounded-3xl border border-border/80",
        elevated && "shadow-[0_20px_60px_-30px_var(--navy)]",
        className
      )}
      {...props}
    />
  );
}
