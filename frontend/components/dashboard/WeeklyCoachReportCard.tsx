import { Surface } from "@/components/kit/Surface";
import { WeeklyCoachReport } from "@/lib/api";

export function WeeklyCoachReportCard({ report }: { report: WeeklyCoachReport | null }) {
  if (!report) {
    return (
      <Surface className="flex h-full flex-col gap-2 p-6 sm:p-7">
        <h2 className="font-display text-lg text-ink">Weekly coach report</h2>
        <p className="text-sm leading-relaxed text-muted-foreground">
          Your first report lands after your first full week of practice.
        </p>
      </Surface>
    );
  }

  return (
    <Surface className="flex h-full flex-col gap-4 p-6 sm:p-7">
      <h2 className="font-display text-lg text-ink">Weekly coach report</h2>
      <div className="space-y-3">
        <p className="text-sm leading-relaxed text-ink">{report.summary}</p>
        {report.biggest_win && (
          <p className="text-sm leading-relaxed text-ink">
            <span className="font-medium text-accent-green">Biggest win: </span>
            {report.biggest_win}
          </p>
        )}
        {report.biggest_weakness && (
          <p className="text-sm leading-relaxed text-ink">
            <span className="font-medium text-accent-amber">Focus area: </span>
            {report.biggest_weakness}
          </p>
        )}
        {report.projected_score_note && (
          <p className="text-sm leading-relaxed text-muted-foreground">{report.projected_score_note}</p>
        )}
      </div>
    </Surface>
  );
}
