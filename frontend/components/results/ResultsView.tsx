import { PracticeResultsResponse, UserMode } from "@/lib/api";
import { ProfessionalResults } from "./ProfessionalResults";
import { GamifiedResults } from "./GamifiedResults";

export function ResultsView({
  results,
  mode,
  subjectId,
}: {
  results: PracticeResultsResponse;
  mode: UserMode;
  subjectId?: number;
}) {
  return mode === "gamified" ? (
    <GamifiedResults results={results} subjectId={subjectId} />
  ) : (
    <ProfessionalResults results={results} subjectId={subjectId} />
  );
}
