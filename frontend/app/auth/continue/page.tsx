import { redirect } from "next/navigation";
import { AuthContinuation } from "@/components/auth/AuthContinuation";
import { getCurrentUser, syncUser } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";

function safeDestination(value: string | undefined): string {
  return value && value.startsWith("/") && !value.startsWith("//") && !value.startsWith("/\\") ? value : "/dashboard";
}

export default async function AuthContinuePage({ searchParams }: { searchParams: Promise<{ returnTo?: string }> }) {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  // The just-created Clerk user may not have an application row yet.
  await syncUser(token);
  const user = await getCurrentUser(token);
  const { returnTo } = await searchParams;
  const destination = user.onboarding_step && user.onboarding_step !== "complete" ? "/onboarding" : safeDestination(returnTo);

  return <AuthContinuation destination={destination} />;
}
