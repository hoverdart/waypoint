import { ComponentProps, ReactNode } from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { cn } from "@/lib/utils";

type Variant = "primary" | "secondary" | "ghost" | "inverse";
type Size = "sm" | "md" | "lg";

const VARIANT: Record<Variant, string> = {
  primary: "bg-ink text-primary-foreground hover:bg-ink/90 shadow-hairline",
  secondary: "bg-card text-ink border border-border hover:border-blue/40 hover:bg-blue-soft/40",
  ghost: "text-ink-soft hover:bg-ink/5 hover:text-ink",
  inverse: "bg-card text-ink hover:bg-card/90 shadow-float",
};

const SIZE: Record<Size, string> = {
  sm: "h-8 px-3.5 text-[0.8rem] gap-1",
  md: "h-10 px-4 text-sm gap-1.5",
  lg: "h-12 px-6 text-base gap-2",
};

/** Every button in this design language is a pill. Deliberately built on a
 * native <button>/<a> rather than the Base UI shadcn Button - that one
 * carries its own radius/size/variant system that has to be fought at every
 * call site to reach this shape. */
export function pillClass(variant: Variant, size: Size, className?: string) {
  return cn(
    "group/pill inline-flex shrink-0 items-center justify-center rounded-full font-medium whitespace-nowrap",
    "outline-none transition-all duration-200 focus-visible:ring-3 focus-visible:ring-blue/40",
    "disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50",
    VARIANT[variant],
    SIZE[size],
    className
  );
}

function Arrow() {
  return (
    <ArrowRight
      className="size-4 transition-transform duration-200 group-hover/pill:translate-x-0.5"
      aria-hidden="true"
    />
  );
}

export function PillButton({
  variant = "primary",
  size = "md",
  arrow = false,
  className,
  children,
  ...props
}: ComponentProps<"button"> & { variant?: Variant; size?: Size; arrow?: boolean }) {
  return (
    <button type="button" className={pillClass(variant, size, className)} {...props}>
      {children}
      {arrow && <Arrow />}
    </button>
  );
}

export function PillLink({
  href,
  variant = "primary",
  size = "md",
  arrow = false,
  className,
  children,
  ...props
}: Omit<ComponentProps<typeof Link>, "href"> & {
  href: string;
  variant?: Variant;
  size?: Size;
  arrow?: boolean;
  children: ReactNode;
}) {
  return (
    <Link href={href} className={pillClass(variant, size, className)} {...props}>
      {children}
      {arrow && <Arrow />}
    </Link>
  );
}
