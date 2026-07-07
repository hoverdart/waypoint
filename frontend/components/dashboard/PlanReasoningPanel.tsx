"use client";

import { useState } from "react";
import { AnimatePresence, motion, useReducedMotion } from "framer-motion";
import { ChevronDown, Lightbulb } from "lucide-react";
import { DailyPlanItem } from "@/lib/api";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { ITEM_TYPE_LABEL } from "@/lib/planItemLabels";
import { cn } from "@/lib/utils";

/** "Why this plan?" transparency panel - collapsible, driven entirely by
 * the reason strings the planner already returns per item. */
export function PlanReasoningPanel({
  items,
  topicNames,
}: {
  items: DailyPlanItem[];
  topicNames: Record<number, string>;
}) {
  const [open, setOpen] = useState(false);
  const reduceMotion = useReducedMotion();

  if (items.length === 0) return null;

  return (
    <WayPointCard className="overflow-hidden">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        className="flex w-full items-center justify-between gap-3 px-5 py-4 text-left outline-none focus-visible:ring-3 focus-visible:ring-blue/50"
      >
        <span className="flex items-center gap-2 font-heading text-sm font-semibold text-navy">
          <Lightbulb className="size-4 text-blue" aria-hidden="true" />
          Why this plan?
        </span>
        <ChevronDown
          className={cn("size-4 text-muted-foreground transition-transform duration-200", open && "rotate-180")}
          aria-hidden="true"
        />
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: reduceMotion ? 0 : 0.25, ease: "easeOut" }}
          >
            <ul className="space-y-2.5 border-t border-border/70 px-5 py-4">
              {items.map((item) => (
                <li key={item.id} className="text-sm">
                  <span className="font-medium text-navy">{topicNames[item.topic_id] ?? "Topic"}</span>
                  <span className="text-muted-foreground"> ({ITEM_TYPE_LABEL[item.item_type]}) — {item.reason}</span>
                </li>
              ))}
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </WayPointCard>
  );
}
