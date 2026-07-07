import { ComponentProps } from "react";
import { ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

type WayPointButtonVariant = "primary" | "secondary" | "ghost";

/** The one button system for every redesigned surface - primary is the
 * navy-to-blue gradient CTA treatment, secondary is an outlined pill, ghost
 * is a plain text action. Onboarding's PrimaryButton/SecondaryButton are
 * thin aliases onto this so there's a single implementation. */
type WayPointButtonProps = Omit<ComponentProps<typeof Button>, "variant"> & {
  variant?: WayPointButtonVariant;
  showArrow?: boolean;
};

export function WayPointButton({
  variant = "primary",
  showArrow = variant === "primary",
  className,
  children,
  ...props
}: WayPointButtonProps) {
  if (variant === "primary") {
    return (
      <Button
        size="lg"
        className={cn(
          "group/wp rounded-full bg-gradient-to-r from-navy to-blue px-5 text-navy-foreground shadow-md shadow-navy/20 hover:from-navy hover:to-blue hover:opacity-95",
          className
        )}
        {...props}
      >
        {children}
        {showArrow && (
          <ArrowRight
            className="size-4 transition-transform duration-200 group-hover/wp:translate-x-0.5"
            aria-hidden="true"
          />
        )}
      </Button>
    );
  }

  if (variant === "secondary") {
    return (
      <Button
        variant="outline"
        size="lg"
        className={cn("rounded-full border-border/80 px-4 hover:border-blue/40 hover:bg-blue-soft/50", className)}
        {...props}
      >
        {children}
      </Button>
    );
  }

  return (
    <Button variant="ghost" size="lg" className={cn("px-4 text-muted-foreground", className)} {...props}>
      {children}
    </Button>
  );
}
