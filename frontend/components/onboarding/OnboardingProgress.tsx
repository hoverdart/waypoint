"use client";

import { motion } from "framer-motion";
import { Check } from "lucide-react";
import { cn } from "@/lib/utils";

const STEPS = [
  { key: "mode", label: "Study Style" },
  { key: "subjects", label: "AP Classes" },
  { key: "details", label: "Plan Details" },
] as const;

export type OnboardingStep = (typeof STEPS)[number]["key"];

export function OnboardingProgress({ step }: { step: OnboardingStep }) {
  const currentIndex = STEPS.findIndex((s) => s.key === step);
  const percent = (currentIndex / (STEPS.length - 1)) * 100;

  return (
    <div>
      {/* Compact mobile version */}
      <div className="sm:hidden">
        <p className="mb-2 text-xs font-medium text-muted-foreground">
          Step {currentIndex + 1} of {STEPS.length} · {STEPS[currentIndex].label}
        </p>
        <div className="h-1.5 w-full overflow-hidden rounded-full bg-secondary">
          <motion.div
            className="h-full rounded-full bg-blue"
            initial={false}
            animate={{ width: `${percent}%` }}
            transition={{ duration: 0.4, ease: "easeOut" }}
          />
        </div>
      </div>

      {/* Full stepper */}
      <div className="hidden items-center sm:flex" role="list" aria-label="Onboarding progress">
        {STEPS.map((s, i) => {
          const isComplete = i < currentIndex;
          const isActive = i === currentIndex;
          return (
            <div key={s.key} className="flex flex-1 items-center last:flex-none" role="listitem">
              <div className="flex flex-col items-center gap-1.5">
                <span
                  className={cn(
                    "flex size-7 items-center justify-center rounded-full border-2 text-xs font-semibold transition-colors",
                    isComplete && "border-blue bg-blue text-blue-foreground",
                    isActive && "border-blue bg-background text-blue",
                    !isComplete && !isActive && "border-border bg-background text-muted-foreground"
                  )}
                  aria-current={isActive ? "step" : undefined}
                >
                  {isComplete ? <Check className="size-3.5" strokeWidth={3} aria-hidden="true" /> : i + 1}
                </span>
                <span
                  className={cn(
                    "text-xs font-medium whitespace-nowrap",
                    isActive || isComplete ? "text-navy" : "text-muted-foreground"
                  )}
                >
                  {s.label}
                </span>
              </div>
              {i < STEPS.length - 1 && (
                <div className="mx-2 mb-4 h-0.5 flex-1 overflow-hidden rounded-full bg-border">
                  <motion.div
                    className="h-full rounded-full bg-blue"
                    initial={false}
                    animate={{ width: i < currentIndex ? "100%" : "0%" }}
                    transition={{ duration: 0.4, ease: "easeOut" }}
                  />
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
