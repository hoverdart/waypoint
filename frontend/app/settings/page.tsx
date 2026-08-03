import { redirect } from "next/navigation";
import { getDashboard } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { ModeToggle } from "@/components/settings/ModeToggle";
import { ProfileSettings } from "@/components/settings/ProfileSettings";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { requireCompletedOnboarding } from "@/lib/auth/requireCompletedOnboarding";

export default async function SettingsPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const dashboard = await getDashboard(token);
  requireCompletedOnboarding(dashboard.user);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-6 px-4 py-8">
      <h1 className="text-2xl font-semibold tracking-tight">Settings</h1>

      <ModeToggle initialMode={dashboard.user.mode} />

      <ProfileSettings initialName={dashboard.user.display_name} initialGrade={dashboard.user.grade_level} />

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
            Your AP goals were set during onboarding. Course changes will be available here soon.
          </p>
        </CardContent>
      </Card>
    </div>
  );
}
