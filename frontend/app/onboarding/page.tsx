import { redirect } from "next/navigation";
import { getOnboardingState, getSubjects, syncUser } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { OnboardingWizard } from "@/components/onboarding/OnboardingWizard";
import { OnboardingLayout } from "@/components/onboarding/OnboardingLayout";

export default async function OnboardingPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  // Idempotent: safe to call every time a user lands here.
  await syncUser(token);
  const [subjects, initialState] = await Promise.all([getSubjects(), getOnboardingState(token)]);
  if (initialState.onboarding_step === "complete") redirect("/dashboard");

  return (
    <OnboardingLayout>
      <OnboardingWizard subjects={subjects} initialState={initialState} />
    </OnboardingLayout>
  );
}
