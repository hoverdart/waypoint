export type UserMode = "professional" | "gamified";

export interface User {
  id: number;
  auth_provider_id: string;
  email: string;
  display_name: string | null;
  mode: UserMode;
}

export interface Topic {
  id: number;
  unit_id: number;
  name: string;
  description: string | null;
  skill_tags: string[];
  display_order: number;
}

export interface Unit {
  id: number;
  subject_id: number;
  name: string;
  description: string | null;
  ap_weight_min: number;
  ap_weight_max: number;
  display_order: number;
}

export interface UnitWithTopics extends Unit {
  topics: Topic[];
}

export interface Subject {
  id: number;
  name: string;
  ap_exam_code: string;
  description: string | null;
  is_active: boolean;
  display_order: number;
}

export interface SubjectDetail extends Subject {
  units: UnitWithTopics[];
}

export interface UserSubject {
  id: number;
  subject_id: number;
  target_score: number | null;
  exam_date: string | null;
  study_minutes_per_day: number;
  is_active: boolean;
}

export interface QuestionOption {
  id: number;
  label: string;
  text: string;
}

export type QuestionType = "mcq" | "frq";

export interface Question {
  id: number;
  subject_id: number;
  unit_id: number;
  topic_id: number;
  type: QuestionType;
  difficulty: number;
  prompt: string;
  options: QuestionOption[];
}

export interface AnswerInput {
  question_id: number;
  selected_option_id?: number | null;
  free_response_text?: string | null;
  time_seconds?: number;
  hints_used?: number;
  explanation_opened?: boolean;
  confidence_rating?: number | null;
}

export interface DiagnosticStartResponse {
  session_id: number;
  session_type: string;
  questions: Question[];
}

export interface DiagnosticSubmitResponse {
  session_id: number;
  correct_count: number;
  total_questions: number;
  score: number;
}

export interface PracticeStartResponse {
  session_id: number;
  session_type: string;
  questions: Question[];
}

export interface PracticeSessionDetail {
  session_id: number;
  session_type: string;
  subject_id: number;
  is_completed: boolean;
  questions: Question[];
}

export interface PracticeSubmitResponse {
  session_id: number;
  session_type: string;
  correct_count: number;
  total_questions: number;
  score: number;
}

export interface ExplanationRead {
  option_id: number | null;
  explanation: string;
  misconception_tag: string | null;
}

export interface AnswerBreakdownItem {
  question_id: number;
  prompt: string;
  type: QuestionType;
  is_correct: boolean;
  score: number;
  max_score: number;
  correct_answer: string;
  selected_option_id: number | null;
  free_response_text: string | null;
  explanations: ExplanationRead[];
}

export interface Badge {
  id: number;
  name: string;
  description: string | null;
  icon: string | null;
}

export interface PracticeResultsResponse {
  session_id: number;
  session_type: string;
  correct_count: number;
  total_questions: number;
  score: number;
  breakdown: AnswerBreakdownItem[];
  xp_earned: number;
  newly_earned_badges: Badge[];
}

export type PlanItemType = "review" | "weakness" | "calibration" | "frq" | "challenge";
export type PlanItemStatus = "pending" | "completed" | "skipped";

export interface DailyPlanItem {
  id: number;
  subject_id: number;
  unit_id: number;
  topic_id: number;
  item_type: PlanItemType;
  point_cost: number;
  priority_score: number;
  reason: string;
  status: PlanItemStatus;
}

export interface DailyPlan {
  id: number;
  plan_date: string;
  point_budget: number;
  status: string;
  items: DailyPlanItem[];
}

export interface TopicMastery {
  topic_id: number;
  topic_name: string;
  mastery_score: number;
  confidence_score: number;
  retention_score: number;
  topic_timer: number;
  attempts_count: number;
  last_practiced_at: string | null;
}

export interface UnitMastery {
  unit_id: number;
  unit_name: string;
  mastery_score: number;
  confidence_score: number;
  topics: TopicMastery[];
}

export interface SubjectMastery {
  subject_id: number;
  subject_name: string;
  mastery_score: number;
  confidence_score: number;
  predicted_ap_score: number;
  units: UnitMastery[];
}

export interface WeeklyCoachReport {
  id: number;
  week_start: string;
  week_end: string;
  summary: string;
  biggest_win: string | null;
  biggest_weakness: string | null;
  next_week_priorities: Array<{ topic_id: number; topic_name: string; subject_name: string; reason: string }>;
  projected_score_note: string | null;
}

export interface DashboardSubjectSummary {
  subject_id: number;
  subject_name: string;
  mastery_score: number;
  predicted_ap_score: number;
  exam_date: string | null;
  target_score: number | null;
}

export interface Dashboard {
  user: User;
  subjects: DashboardSubjectSummary[];
  today_plan: DailyPlan | null;
  latest_weekly_report: WeeklyCoachReport | null;
  total_xp: number;
  streak_days: number;
  earned_badges: Badge[];
}

export type ExplainAction =
  | "explain_differently"
  | "analogy"
  | "easier_example"
  | "harder_example"
  | "why_wrong"
  | "compare_concepts";

export interface AIExplainResponse {
  explanation: string;
  free_used: number;
  premium_used: number;
  max_allowed: number;
}

export interface AIUsage {
  free_used: number;
  premium_used: number;
  max_allowed: number;
  period_start: string;
  period_end: string;
}

export interface QuestionReport {
  id: number;
  question_id: number;
  reason: string;
  details: string | null;
  status: string;
  created_at: string;
}

export interface AdminQuestion {
  id: number;
  subject_id: number;
  unit_id: number;
  topic_id: number;
  type: QuestionType;
  difficulty: number;
  prompt: string;
  correct_answer: string;
  rubric_json: Record<string, unknown> | null;
  skill_tags: string[];
  misconception_tags: string[];
  source: string;
  validation_status: "draft" | "approved" | "rejected" | "needs_review";
  version: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface AdminQuestionOption {
  label: string;
  text: string;
  is_correct: boolean;
}

export interface AdminQuestionDetail extends AdminQuestion {
  options: AdminQuestionOption[];
  reports: QuestionReport[];
}
