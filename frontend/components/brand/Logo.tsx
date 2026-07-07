import Image from "next/image";
import { cn } from "@/lib/utils";

/** Compact icon-only crop of the compass/cap/road mark - used anywhere space
 * is tight (nav, badges). The source JPG has a near-white background that
 * blends into the app's warm off-white surfaces at these sizes. */
export function LogoMark({ size = 32, className }: { size?: number; className?: string }) {
  return (
    <span
      className={cn(
        "inline-flex shrink-0 items-center justify-center overflow-hidden rounded-lg ring-1 ring-navy/10",
        className
      )}
      style={{ width: size, height: size }}
    >
      <Image src="/logo-mark.jpg" alt="" width={size * 2} height={size * 2} className="h-full w-full object-cover" priority />
    </span>
  );
}

/** Full icon+wordmark lockup, for hero/brand moments where the vertical
 * lockup shape has room to breathe. */
export function LogoFull({ className, height = 96 }: { className?: string; height?: number }) {
  return (
    <Image
      src="/logo.jpg"
      alt="WayPoint"
      width={height * 1.375}
      height={height}
      className={cn("mix-blend-multiply select-none", className)}
      priority
    />
  );
}

/** Icon mark + live "WayPoint" text - the default lockup for nav bars and
 * anywhere the brand name should stay real, accessible text. Pass
 * `variant="light"` on dark surfaces (the navy header) so the wordmark
 * stays legible instead of rendering navy-on-navy. */
export function LogoLockup({
  size = 30,
  variant = "dark",
  className,
}: {
  size?: number;
  variant?: "dark" | "light";
  className?: string;
}) {
  return (
    <span className={cn("inline-flex items-center gap-2", className)}>
      <LogoMark size={size} />
      <span
        className={cn(
          "text-base font-semibold tracking-tight",
          variant === "light" ? "text-navy-foreground" : "text-navy"
        )}
      >
        WayPoint
      </span>
    </span>
  );
}
