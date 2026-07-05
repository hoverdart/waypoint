import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { WeeklyCoachReport } from "@/lib/api";

export function WeeklyCoachReportCard({ report }: { report: WeeklyCoachReport | null }) {
  if (!report) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Weekly coach report</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            Your first report lands after your first full week of practice.
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Weekly coach report</CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        <p className="text-sm">{report.summary}</p>
        {report.biggest_win && (
          <p className="text-sm">
            <span className="font-medium text-emerald-600">Biggest win: </span>
            {report.biggest_win}
          </p>
        )}
        {report.biggest_weakness && (
          <p className="text-sm">
            <span className="font-medium text-amber-600">Focus area: </span>
            {report.biggest_weakness}
          </p>
        )}
        {report.projected_score_note && (
          <p className="text-sm text-muted-foreground">{report.projected_score_note}</p>
        )}
      </CardContent>
    </Card>
  );
}
