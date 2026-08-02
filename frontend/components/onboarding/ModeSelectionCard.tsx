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
        // Transform is left to framer (whileHover/whileTap), so only the paint
        // properties get a CSS transition here.
        "relative flex w-full flex-col gap-4 rounded-surface border p-6 text-left shadow-hairline outline-none",
        "transition-[color,background-color,border-color,box-shadow] duration-300",
        "focus-visible:ring-3 focus-visible:ring-blue/40",
        selected ? "border-blue bg-blue-soft/60" : "border-border/70 bg-card hover:border-blue/30 hover:shadow-lift"
      )}
    >
      {selected && (
        <motion.span
          initial={{ scale: 0, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ type: "spring", stiffness: 500, damping: 22 }}
          className="absolute -top-2.5 -right-2.5 flex size-7 items-center justify-center rounded-full bg-blue text-blue-foreground shadow-hairline"
        >
          <Check className="size-4" strokeWidth={3} aria-hidden="true" />
          <span className="sr-only">Selected</span>
        </motion.span>
      )}

      <div className="flex items-center gap-3">
        <span
          className={cn(
            "flex size-10 shrink-0 items-center justify-center rounded-full transition-colors",
            selected ? "bg-blue text-blue-foreground" : "bg-blue-soft text-blue"
          )}
        >
          <Icon className="size-5" aria-hidden="true" />
        </span>
        <p className="font-display text-lg text-ink">{title}</p>
      </div>

      <p className="text-sm leading-relaxed text-muted-foreground">{description}</p>

      <div className="rounded-2xl border border-border/60 bg-card p-4">{preview}</div>
    </motion.button>
  );
}
