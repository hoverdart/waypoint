"use client";

import { motion, useReducedMotion } from "framer-motion";
import { Check } from "lucide-react";
import { cn } from "@/lib/utils";

/** Small checkmark/progress-tick used for plan-item completion states and
 * the course-detail route timeline. */
export function AnimatedCheckpoint({ done, className }: { done: boolean; className?: string }) {
  const reduceMotion = useReducedMotion();

  return (
    <motion.span
      initial={false}
      animate={{ scale: done ? 1 : 0.85, opacity: done ? 1 : 0.5 }}
      transition={{ duration: reduceMotion ? 0 : 0.25, type: "spring", stiffness: 400, damping: 24 }}
      className={cn(
        "flex size-6 shrink-0 items-center justify-center rounded-full",
        done ? "bg-accent-green text-white" : "border-2 border-border bg-transparent",
        className
      )}
    >
      {done && <Check className="size-3.5" strokeWidth={3} aria-hidden="true" />}
    </motion.span>
  );
}
