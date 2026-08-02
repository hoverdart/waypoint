import { ComponentProps } from "react";
import { PillButton } from "@/components/kit/PillButton";
import { cn } from "@/lib/utils";

/** The wizard's forward action: a solid ink pill that always carries the
 * arrow, so "keep going" reads the same on every step. */
export function PrimaryButton({ className, children, ...props }: ComponentProps<typeof PillButton>) {
  return (
    <PillButton size="lg" arrow className={cn("px-6", className)} {...props}>
      {children}
    </PillButton>
  );
}

export function SecondaryButton({ className, ...props }: ComponentProps<typeof PillButton>) {
  return <PillButton variant="ghost" size="lg" className={cn("px-4", className)} {...props} />;
}
