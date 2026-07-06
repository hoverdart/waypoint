import { ReactNode } from "react";
import { AnimatedPathBackground } from "@/components/brand/AnimatedPathBackground";
import { FloatingStudySignals } from "@/components/brand/FloatingStudySignals";

export function OnboardingLayout({ children }: { children: ReactNode }) {
  return (
    <div className="relative isolate flex-1 overflow-hidden py-10 sm:py-14">
      <AnimatedPathBackground />
      <FloatingStudySignals />
      <div className="relative mx-auto w-full max-w-2xl px-4">{children}</div>
    </div>
  );
}
