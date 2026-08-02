"use client";

import { ReactNode, useState } from "react";
import { useMotionValueEvent, useScroll } from "framer-motion";
import { cn } from "@/lib/utils";

/** Chrome for the site header. Sits flush and transparent at the top of the
 * page, then detaches into a floating rounded island with blur and a soft
 * shadow once you start scrolling.
 *
 * The morph is a CSS transition on class changes rather than a layout
 * animation - it survives resizes and never fights the sticky positioning. */
export function HeaderShell({ children }: { children: ReactNode }) {
  const { scrollY } = useScroll();
  const [scrolled, setScrolled] = useState(false);

  useMotionValueEvent(scrollY, "change", (y) => {
    // Hysteresis: different thresholds for engaging and releasing so the
    // header can't flicker when a scroll settles right on the boundary.
    setScrolled((prev) => (prev ? y > 24 : y > 56));
  });

  return (
    <header
      className={cn(
        "sticky top-0 z-40 transition-all duration-500 ease-out",
        scrolled ? "px-3 pt-3" : "px-0 pt-0"
      )}
    >
      <div
        className={cn(
          "mx-auto flex items-center justify-between gap-4 transition-all duration-500 ease-out",
          scrolled
            ? "h-14 max-w-3xl rounded-full border border-border/70 bg-card/80 px-4 shadow-float backdrop-blur-xl"
            : "h-16 max-w-6xl rounded-none border border-transparent px-6"
        )}
      >
        {children}
      </div>
    </header>
  );
}
