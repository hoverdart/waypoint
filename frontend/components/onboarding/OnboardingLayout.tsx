import { ReactNode } from "react";

/** Onboarding shell. The ambient aura now lives globally in the root layout,
 * so this only handles measure and vertical rhythm. */
export function OnboardingLayout({ children }: { children: ReactNode }) {
  return (
    <div className="relative isolate flex-1 py-12 sm:py-16">
      <div className="relative mx-auto w-full max-w-2xl px-6">{children}</div>
    </div>
  );
}
