import { redirect } from "next/navigation";
import { User } from "@/lib/api";

/**
 * The absence of onboarding metadata is deliberately treated as a completed
 * legacy account. It keeps deployed users working while the backend migration
 * is rolled out, while every newly provisioned account receives an explicit
 * non-complete step and is routed through onboarding.
 */
export function requireCompletedOnboarding(user: User): void {
  if (user.onboarding_step && user.onboarding_step !== "complete") {
    redirect("/onboarding");
  }
}
