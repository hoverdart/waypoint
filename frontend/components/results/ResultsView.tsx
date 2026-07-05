import { PracticeResultsResponse, UserMode } from "@/lib/api";
import { ProfessionalResults } from "./ProfessionalResults";
import { GamifiedResults } from "./GamifiedResults";

export function ResultsView({ results, mode }: { results: PracticeResultsResponse; mode: UserMode }) {
  return mode === "gamified" ? <GamifiedResults results={results} /> : <ProfessionalResults results={results} />;
}
