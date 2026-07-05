import { Dashboard } from "@/lib/api";
import { ProfessionalDashboard } from "./ProfessionalDashboard";
import { GamifiedDashboard } from "./GamifiedDashboard";

/** Single mode-switch point: fetches nothing itself, just decides which
 * presentational variant to render from already-fetched data. */
export function DashboardView({ data }: { data: Dashboard }) {
  return data.user.mode === "gamified" ? (
    <GamifiedDashboard data={data} />
  ) : (
    <ProfessionalDashboard data={data} />
  );
}
