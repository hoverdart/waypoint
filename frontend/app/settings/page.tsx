import { redirect } from "next/navigation";
import { getDashboard, getSubjects, getMySubjects } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { AccountActions } from "@/components/settings/AccountActions";
import { SubjectPreferences } from "@/components/settings/SubjectPreferences";
import { ModeToggle } from "@/components/settings/ModeToggle";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function SettingsPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const [dashboard, subjects, enrolled] = await Promise.all([getDashboard(token), getSubjects(), getMySubjects(token)]);

  return (
    <div className="mx-auto w-full max-w-2xl space-y-6 px-4 py-8">
      <h1 className="text-2xl font-semibold tracking-tight">Settings</h1>

      <ModeToggle initialMode={dashboard.user.mode} />

      <Card id="account">
        <CardHeader>
          <CardTitle>Account</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            {!dashboard.user.email.endsWith("@unknown.local") && <span className="block mb-2">{dashboard.user.email}</span>}
            Manage your profile, sign-in details, and account security.
          </p>
          <AccountActions />
        </CardContent>
      </Card>

      <SubjectPreferences subjects={subjects} enrolled={enrolled} />
    </div>
  );
}
