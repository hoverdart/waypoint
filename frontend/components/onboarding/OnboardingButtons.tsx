import { ComponentProps } from "react";
import { ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

export function PrimaryButton({ className, children, ...props }: ComponentProps<typeof Button>) {
  return (
    <Button
      size="lg"
      className={cn(
        "group/primary rounded-full bg-gradient-to-r from-navy to-blue px-5 text-navy-foreground shadow-md shadow-navy/20 hover:from-navy hover:to-blue hover:opacity-95",
        className
      )}
      {...props}
    >
      {children}
      <ArrowRight className="size-4 transition-transform duration-200 group-hover/primary:translate-x-0.5" aria-hidden="true" />
    </Button>
  );
}

export function SecondaryButton({ className, ...props }: ComponentProps<typeof Button>) {
  return <Button variant="ghost" size="lg" className={cn("px-4 text-muted-foreground", className)} {...props} />;
}
