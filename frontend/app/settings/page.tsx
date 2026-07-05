import { redirect } from "next/navigation";
import { getDashboard } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { ModeToggle } from "@/components/settings/ModeToggle";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function SettingsPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const dashboard = await getDashboard(token);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-6 px-4 py-8">
      <h1 className="text-2xl font-semibold tracking-tight">Settings</h1>

      <ModeToggle initialMode={dashboard.user.mode} />

      <Card>
        <CardHeader>
          <CardTitle>Account</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            {dashboard.user.email} - manage sign-in details and security from the account menu in the
            top-right corner.
          </p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Subjects &amp; study time</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            To add subjects or change your daily study time, revisit{" "}
            <a href="/onboarding" className="underline underline-offset-2">
              onboarding
            </a>
            .
          </p>
        </CardContent>
      </Card>
    </div>
  );
}
