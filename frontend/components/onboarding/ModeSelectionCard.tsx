"use client";

import { ReactNode } from "react";
import { motion, useReducedMotion, type Variants } from "framer-motion";
import { Check, type LucideIcon } from "lucide-react";
import { cn } from "@/lib/utils";

export function ModeSelectionCard({
  title,
  description,
  icon: Icon,
  selected,
  onSelect,
  preview,
  index = 0,
}: {
  title: string;
  description: string;
  icon: LucideIcon;
  selected: boolean;
  onSelect: () => void;
  preview: ReactNode;
  index?: number;
}) {
  const reduceMotion = useReducedMotion();

  const cardVariants: Variants = {
    hidden: { opacity: 0, y: reduceMotion ? 0 : 16 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: reduceMotion ? 0 : 0.45, delay: reduceMotion ? 0 : 0.15 * index, ease: "easeOut" },
    },
  };

  return (
    <motion.button
      type="button"
      role="radio"
      aria-checked={selected}
      onClick={onSelect}
      variants={cardVariants}
      initial="hidden"
      animate="visible"
      whileHover={reduceMotion ? undefined : { y: -4 }}
      whileTap={reduceMotion ? undefined : { y: -1 }}
      transition={{ type: "spring", stiffness: 400, damping: 28 }}
      className={cn(
        "group relative flex w-full flex-col gap-4 rounded-3xl border bg-card p-6 text-left shadow-sm outline-none transition-colors",
        "focus-visible:ring-3 focus-visible:ring-blue/50",
        selected
          ? "border-blue/60 shadow-[0_0_0_1px_var(--blue),0_16px_40px_-16px_var(--blue)]"
          : "border-border hover:border-blue/30 hover:shadow-md"
      )}
    >
      {selected && (
        <motion.span
          initial={{ scale: 0, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ type: "spring", stiffness: 500, damping: 22 }}
          className="absolute -top-2.5 -right-2.5 flex size-7 items-center justify-center rounded-full bg-blue text-blue-foreground shadow-sm"
        >
          <Check className="size-4" strokeWidth={3} aria-hidden="true" />
          <span className="sr-only">Selected</span>
        </motion.span>
      )}

      <div className="flex items-center gap-3">
        <span
          className={cn(
            "flex size-10 shrink-0 items-center justify-center rounded-xl transition-colors",
            selected ? "bg-blue text-blue-foreground" : "bg-blue-soft text-navy"
          )}
        >
          <Icon className="size-5" aria-hidden="true" />
        </span>
        <div>
          <p className="font-heading text-base font-semibold text-navy">{title}</p>
        </div>
      </div>

      <p className="text-sm leading-relaxed text-muted-foreground">{description}</p>

      <div className="rounded-2xl border border-border/70 bg-muted/50 p-4">{preview}</div>
    </motion.button>
  );
}
