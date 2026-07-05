import { redirect } from "next/navigation";
import { syncUser, getSubjects } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { OnboardingWizard } from "@/components/onboarding/OnboardingWizard";

export default async function OnboardingPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  // Idempotent: safe to call every time a user lands here.
  await syncUser(token);
  const subjects = await getSubjects();

  return (
    <div className="mx-auto w-full max-w-2xl px-4 py-12">
      <OnboardingWizard subjects={subjects} />
    </div>
  );
}
