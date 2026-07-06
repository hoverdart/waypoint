import { redirect } from "next/navigation";
import { syncUser, getSubjects } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { OnboardingWizard } from "@/components/onboarding/OnboardingWizard";
import { OnboardingLayout } from "@/components/onboarding/OnboardingLayout";

export default async function OnboardingPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  // Idempotent: safe to call every time a user lands here.
  await syncUser(token);
  const subjects = await getSubjects();

  return (
    <OnboardingLayout>
      <OnboardingWizard subjects={subjects} />
    </OnboardingLayout>
  );
}
