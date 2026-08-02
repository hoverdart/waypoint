import { redirect } from "next/navigation";
import { getDashboard } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { DashboardView } from "@/components/dashboard/DashboardView";

export default async function DashboardPage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");

  const data = await getDashboard(token);
  return (
    <div className="mx-auto w-full max-w-6xl px-6 py-10">
      <DashboardView data={data} />
    </div>
  );
}
