import { DailyPlan, DashboardSubjectSummary, SubjectDetail, UserMode } from "@/lib/api";
import { ProfessionalDailyPlan } from "./ProfessionalDailyPlan";
import { GamifiedDailyPlan } from "./GamifiedDailyPlan";

export function DailyPlanView({
  plans,
  subjectDetails,
  enrolledSubjects,
  mode,
  streakDays,
}: {
  plans: DailyPlan[];
  subjectDetails: SubjectDetail[];
  enrolledSubjects: DashboardSubjectSummary[];
  mode: UserMode;
  streakDays: number;
}) {
  return mode === "gamified" ? (
    <GamifiedDailyPlan
      plans={plans}
      subjectDetails={subjectDetails}
      enrolledSubjects={enrolledSubjects}
      streakDays={streakDays}
    />
  ) : (
    <ProfessionalDailyPlan plans={plans} subjectDetails={subjectDetails} enrolledSubjects={enrolledSubjects} />
  );
}
