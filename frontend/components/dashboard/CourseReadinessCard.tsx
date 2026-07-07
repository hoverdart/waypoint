import Link from "next/link";
import { CardContent } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { TopicMasteryPill } from "@/components/shared/MasteryPills";
import { ExamCountdown } from "@/components/shared/ExamCountdown";
import { DashboardSubjectSummary } from "@/lib/api";

/** Renamed from DashboardSubjectCard to match the brief's naming - same
 * props, deep-links into /analytics?subject=X (the course-detail page). */
export function CourseReadinessCard({ subject }: { subject: DashboardSubjectSummary }) {
  return (
    <Link
      href={`/analytics?subject=${subject.subject_id}`}
      className="block h-full rounded-3xl outline-none focus-visible:ring-3 focus-visible:ring-blue/50"
    >
      <WayPointCard className="h-full transition-colors hover:border-blue/40 hover:shadow-md">
        <CardContent className="space-y-3 p-5">
          <div className="flex items-start justify-between gap-2">
            <p className="font-heading font-semibold text-navy">{subject.subject_name}</p>
            <span className="shrink-0 rounded-full bg-blue-soft px-2.5 py-0.5 text-sm font-semibold text-navy">
              {subject.predicted_ap_score}
            </span>
          </div>
          <TopicMasteryPill masteryScore={subject.mastery_score} />
          {subject.exam_date ? (
            <ExamCountdown examDate={subject.exam_date} />
          ) : (
            <p className="text-xs text-muted-foreground">No exam date set</p>
          )}
          {subject.target_score && (
            <p className="text-xs text-muted-foreground">Target score: {subject.target_score}</p>
          )}
        </CardContent>
      </WayPointCard>
    </Link>
  );
}
