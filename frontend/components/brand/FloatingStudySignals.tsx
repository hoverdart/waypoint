"use client";

import { motion, useReducedMotion } from "framer-motion";
import { BookOpen, Target, Sigma, ClipboardCheck, Map, Clock } from "lucide-react";
import { cn } from "@/lib/utils";

const SIGNALS = [
  { icon: BookOpen, label: "AP Biology", className: "left-[4%] top-[14%]" },
  { icon: Sigma, label: "AP Calculus AB", className: "right-[5%] top-[10%]" },
  { icon: Target, label: "Weak Topic · Cellular Respiration", className: "left-[2%] top-[58%]" },
  { icon: Clock, label: "Today · 42 min plan", className: "right-[3%] top-[46%]" },
  { icon: ClipboardCheck, label: "Review · Unit 3 FRQ", className: "left-[8%] top-[82%]" },
  { icon: Map, label: "Mastery Map", className: "right-[7%] top-[80%]" },
];

/** Decorative, low-opacity proof chips scattered around the onboarding card
 * to signal product depth. Hidden below `lg` - there's no room for them
 * once the card takes the full width, and the brief calls for simplifying
 * background motion on smaller screens. */
export function FloatingStudySignals() {
  const reduceMotion = useReducedMotion();

  return (
    <div className="pointer-events-none absolute inset-0 -z-10 hidden lg:block" aria-hidden="true">
      {SIGNALS.map(({ icon: Icon, label, className }, i) => (
        <motion.div
          key={label}
          className={cn("absolute flex items-center gap-2 rounded-xl border border-border/60 bg-card/80 px-3 py-2 shadow-sm backdrop-blur-sm", className)}
          initial={{ opacity: 0, y: 12 }}
          animate={{
            opacity: 0.55,
            y: reduceMotion ? 0 : [0, -8, 0],
          }}
          transition={{
            opacity: { duration: 0.6, delay: 0.5 + i * 0.1 },
            y: reduceMotion
              ? { duration: 0 }
              : { duration: 5 + i * 0.4, repeat: Infinity, ease: "easeInOut", delay: i * 0.3 },
          }}
        >
          <Icon className="size-3.5 text-navy/70" aria-hidden="true" />
          <span className="text-xs font-medium whitespace-nowrap text-navy/70">{label}</span>
        </motion.div>
      ))}
    </div>
  );
}
