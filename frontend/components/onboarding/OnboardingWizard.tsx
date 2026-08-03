"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { AnimatePresence, motion, useReducedMotion } from "framer-motion";
import { BarChart3, Compass, ListChecks, Sparkles, Target } from "lucide-react";
import {
  ApiError,
  completeOnboarding,
  OnboardingState,
  OnboardingSubjectInput,
  saveOnboardingDraft,
  Subject,
  UserMode,
} from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Surface } from "@/components/kit/Surface";
import { PageHeader } from "@/components/kit/PageHeader";
import { cn } from "@/lib/utils";
import { OnboardingProgress, type OnboardingStep } from "./OnboardingProgress";
import { ModeSelectionCard } from "./ModeSelectionCard";
import { MiniMasteryRing } from "./MiniMasteryRing";
import { MiniAnalyticsPreview } from "./MiniAnalyticsPreview";
import { MiniQuestPreview } from "./MiniQuestPreview";
import { PrimaryButton, SecondaryButton } from "./OnboardingButtons";

const STUDY_TIME_PRESETS = [10, 20, 45, 60];
const TARGET_SCORES = [3, 4, 5];
const GRADES = [9, 10, 11, 12];
const TOGGLE = "rounded-full border text-sm font-medium outline-none transition-colors focus-visible:ring-3 focus-visible:ring-blue/40";
const TOGGLE_ON = "border-blue bg-blue-soft/60 text-ink";
const TOGGLE_OFF = "border-border/70 bg-card text-ink-soft hover:border-blue/40 hover:bg-blue-soft/40";

interface SubjectDraft {
  target_score: number;
  exam_date: string;
  study_minutes_per_day: number;
}

const TOUR_PANELS = [
  {
    title: "Start from an honest baseline",
    body: "A short diagnostic will soon show what you already know, so WayPoint never mistakes an unknown topic for a weak one.",
    icon: Target,
  },
  {
    title: "Get one plan sized to your day",
    body: "Your AP goals, exam dates, and available study time shape a clear next step instead of a giant to-do list.",
    icon: ListChecks,
  },
  {
    title: "Watch readiness move",
    body: "Every finished session updates mastery, confidence, and retention to make tomorrow's plan more useful.",
    icon: BarChart3,
  },
] as const;

function defaultDraft(): SubjectDraft {
  return { target_score: 4, exam_date: "", study_minutes_per_day: 20 };
}

function initialDrafts(state: OnboardingState): Record<number, SubjectDraft> {
  return Object.fromEntries(
    state.user_subjects
      .filter((subject) => subject.is_active)
      .map((subject) => [
        subject.subject_id,
        {
          target_score: subject.target_score ?? 4,
          exam_date: subject.exam_date ?? "",
          study_minutes_per_day: subject.study_minutes_per_day,
        },
      ])
  );
}

function subjectPayload(selectedIds: number[], drafts: Record<number, SubjectDraft>): OnboardingSubjectInput[] {
  return selectedIds.map((id) => {
    const draft = drafts[id] ?? defaultDraft();
    return {
      subject_id: id,
      target_score: draft.target_score,
      exam_date: draft.exam_date || null,
      study_minutes_per_day: draft.study_minutes_per_day,
    };
  });
}

function formatGrade(grade: number | null): string {
  return grade ? `${grade}${grade === 9 ? "th" : grade === 10 ? "th" : grade === 11 ? "th" : "th"} grade` : "";
}

export function OnboardingWizard({ subjects, initialState }: { subjects: Subject[]; initialState: OnboardingState }) {
  const router = useRouter();
  const getToken = useApiToken();
  const reduceMotion = useReducedMotion();
  const [step, setStep] = useState<OnboardingStep>(initialState.onboarding_step === "complete" ? "profile" : initialState.onboarding_step);
  const [displayName, setDisplayName] = useState(initialState.user.display_name ?? "");
  const [gradeLevel, setGradeLevel] = useState<number | null>(initialState.user.grade_level ?? null);
  const [selectedIds, setSelectedIds] = useState<number[]>(
    initialState.user_subjects.filter((subject) => subject.is_active).map((subject) => subject.subject_id)
  );
  const [drafts, setDrafts] = useState<Record<number, SubjectDraft>>(() => initialDrafts(initialState));
  const [mode, setMode] = useState<UserMode>(initialState.user.mode ?? "professional");
  const [tourIndex, setTourIndex] = useState(0);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const isProfileValid = displayName.trim().length > 0 && gradeLevel !== null;

  function setNextStep(next: OnboardingStep) {
    setError(null);
    setStep(next);
  }

  function toggleSubject(id: number) {
    setSelectedIds((previous) => (previous.includes(id) ? previous.filter((value) => value !== id) : [...previous, id]));
  }

  function updateDraft(id: number, patch: Partial<SubjectDraft>) {
    setDrafts((previous) => ({ ...previous, [id]: { ...defaultDraft(), ...previous[id], ...patch } }));
  }

  async function persistProfile() {
    if (!isProfileValid || gradeLevel === null) return;
    setSubmitting(true);
    setError(null);
    try {
      await saveOnboardingDraft(
        { display_name: displayName.trim(), grade_level: gradeLevel, onboarding_step: "courses" },
        getToken
      );
      setNextStep("courses");
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "We couldn't save your profile. Please try again.");
    } finally {
      setSubmitting(false);
    }
  }

  async function persistCourses() {
    if (!selectedIds.length) return;
    setSubmitting(true);
    setError(null);
    try {
      await saveOnboardingDraft(
        { subjects: subjectPayload(selectedIds, drafts), onboarding_step: "diagnostic" },
        getToken
      );
      setNextStep("diagnostic");
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "We couldn't save your AP goals. Please try again.");
    } finally {
      setSubmitting(false);
    }
  }

  async function skipDiagnostic() {
    setSubmitting(true);
    setError(null);
    try {
      await saveOnboardingDraft({ diagnostic_status: "skipped", onboarding_step: "tour" }, getToken);
      setNextStep("tour");
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "We couldn't save that choice. Please try again.");
    } finally {
      setSubmitting(false);
    }
  }

  async function finishOnboarding() {
    setSubmitting(true);
    setError(null);
    try {
      await completeOnboarding({ mode, diagnostic_status: "skipped" }, getToken);
      router.replace("/dashboard");
      router.refresh();
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "We couldn't finish setting up WayPoint. Please try again.");
    } finally {
      setSubmitting(false);
    }
  }

  const currentTour = TOUR_PANELS[tourIndex];
  const TourIcon = currentTour.icon;

  return (
    <motion.div
      initial={{ opacity: 0, y: reduceMotion ? 0 : 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: reduceMotion ? 0 : 0.5, ease: "easeOut" }}
      className="space-y-8"
    >
      <OnboardingProgress step={step} />

      <AnimatePresence mode="wait">
        <motion.div
          key={step}
          initial={{ opacity: 0, x: reduceMotion ? 0 : 12 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: reduceMotion ? 0 : -12 }}
          transition={{ duration: reduceMotion ? 0 : 0.25, ease: "easeOut" }}
          className="space-y-6"
        >
          {step === "profile" && (
            <>
              <PageHeader title="Let’s make this yours" sub="A few details help WayPoint make your study path feel personal from day one." />
              <Surface tone="raised">
                <div className="space-y-6 p-5 sm:p-7">
                  <div className="space-y-1.5">
                    <Label htmlFor="onboarding-name">What should we call you?</Label>
                    <Input
                      id="onboarding-name"
                      autoComplete="name"
                      value={displayName}
                      onChange={(event) => setDisplayName(event.target.value)}
                      placeholder="Your first name"
                      aria-invalid={displayName.length > 0 && !displayName.trim()}
                    />
                  </div>
                  <fieldset className="space-y-2">
                    <legend className="text-sm font-medium text-ink">What grade are you in?</legend>
                    <div className="flex flex-wrap gap-2" role="radiogroup" aria-label="Grade level">
                      {GRADES.map((grade) => (
                        <button
                          key={grade}
                          type="button"
                          role="radio"
                          aria-checked={gradeLevel === grade}
                          onClick={() => setGradeLevel(grade)}
                          className={cn(TOGGLE, "px-4 py-2", gradeLevel === grade ? TOGGLE_ON : TOGGLE_OFF)}
                        >
                          {formatGrade(grade)}
                        </button>
                      ))}
                    </div>
                  </fieldset>
                </div>
              </Surface>
            </>
          )}

          {step === "courses" && (
            <>
              <PageHeader title="Set your AP goals" sub="Choose every AP you’re taking and the score you’re working toward in each one." />
              <Surface tone="raised">
                <div className="space-y-4 p-5 sm:p-7">
                  {subjects.map((subject) => {
                    const selected = selectedIds.includes(subject.id);
                    const draft = drafts[subject.id] ?? defaultDraft();
                    return (
                      <div key={subject.id} className={cn("rounded-2xl border p-4 transition-colors", selected ? "border-blue bg-blue-soft/30" : "border-border/60 bg-muted/30")}>
                        <div className="flex flex-wrap items-center justify-between gap-3">
                          <button
                            type="button"
                            aria-pressed={selected}
                            onClick={() => toggleSubject(subject.id)}
                            className={cn(TOGGLE, "px-4 py-2", selected ? TOGGLE_ON : TOGGLE_OFF)}
                          >
                            {subject.name}
                          </button>
                          {selected && (
                            <div className="flex items-center gap-2" role="radiogroup" aria-label={`${subject.name} target score`}>
                              <span className="text-sm text-muted-foreground">Target</span>
                              {TARGET_SCORES.map((score) => (
                                <button
                                  key={score}
                                  type="button"
                                  role="radio"
                                  aria-checked={draft.target_score === score}
                                  onClick={() => updateDraft(subject.id, { target_score: score })}
                                  className={cn(TOGGLE, "size-9 tabular-nums", draft.target_score === score ? TOGGLE_ON : TOGGLE_OFF)}
                                >
                                  {score}
                                </button>
                              ))}
                            </div>
                          )}
                        </div>
                        {selected && (
                          <div className="mt-4 grid gap-4 border-t border-border/60 pt-4 sm:grid-cols-2">
                            <div className="space-y-1.5">
                              <Label htmlFor={`exam-date-${subject.id}`}>Exam date <span className="text-muted-foreground">(optional)</span></Label>
                              <Input id={`exam-date-${subject.id}`} type="date" value={draft.exam_date} onChange={(event) => updateDraft(subject.id, { exam_date: event.target.value })} />
                            </div>
                            <div className="space-y-1.5">
                              <Label>Daily study time <span className="text-muted-foreground">(optional)</span></Label>
                              <div className="flex flex-wrap gap-2" role="radiogroup" aria-label={`${subject.name} daily study time`}>
                                {STUDY_TIME_PRESETS.map((minutes) => (
                                  <button key={minutes} type="button" role="radio" aria-checked={draft.study_minutes_per_day === minutes} onClick={() => updateDraft(subject.id, { study_minutes_per_day: minutes })} className={cn(TOGGLE, "px-3 py-1.5", draft.study_minutes_per_day === minutes ? TOGGLE_ON : TOGGLE_OFF)}>
                                    {minutes} min
                                  </button>
                                ))}
                              </div>
                            </div>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </Surface>
            </>
          )}

          {step === "diagnostic" && (
            <>
              <PageHeader title="Your baseline is next" sub="A short onboarding diagnostic is coming soon. It will calibrate each AP route before your first study plan." />
              <Surface tone="raised">
                <div className="space-y-5 p-5 sm:p-7">
                  <div className="rounded-2xl border border-blue/25 bg-blue-soft/35 p-5">
                    <p className="font-display text-lg text-ink">Diagnostic coming soon</p>
                    <p className="mt-2 text-sm leading-relaxed text-muted-foreground">We’ll let you know when this short baseline test is ready. Skipping today starts every selected topic from a neutral, unknown baseline—not a penalty.</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-ink">Your selected APs</p>
                    <ul className="mt-2 flex flex-wrap gap-2" aria-label="Selected AP subjects">
                      {selectedIds.map((id) => <li key={id} className="rounded-full bg-muted px-3 py-1.5 text-sm text-ink">{subjects.find((subject) => subject.id === id)?.name}</li>)}
                    </ul>
                  </div>
                </div>
              </Surface>
            </>
          )}

          {step === "tour" && (
            <>
              <PageHeader title="Welcome to WayPoint" sub="Here’s the loop that keeps your study time focused." />
              <Surface tone="raised">
                <div className="space-y-6 p-5 sm:p-7">
                  {tourIndex < TOUR_PANELS.length - 1 ? (
                    <div className="grid gap-6 sm:grid-cols-[auto_1fr] sm:items-start">
                      <span className="flex size-12 items-center justify-center rounded-2xl bg-blue-soft text-blue"><TourIcon className="size-6" aria-hidden="true" /></span>
                      <div>
                        <p className="text-xs font-semibold tracking-[0.14em] text-blue uppercase">Feature {tourIndex + 1} of {TOUR_PANELS.length}</p>
                        <h2 className="mt-2 font-display text-xl text-ink">{currentTour.title}</h2>
                        <p className="mt-3 max-w-lg leading-relaxed text-muted-foreground">{currentTour.body}</p>
                        {tourIndex === 0 && <div className="mt-5"><MiniMasteryRing value={50} /></div>}
                        {tourIndex === 1 && <div className="mt-5"><MiniQuestPreview /></div>}
                      </div>
                    </div>
                  ) : (
                    <div className="space-y-5">
                      <div className="flex items-start gap-4">
                        <span className="flex size-12 shrink-0 items-center justify-center rounded-2xl bg-blue-soft text-blue"><Compass className="size-6" aria-hidden="true" /></span>
                        <div>
                          <p className="text-xs font-semibold tracking-[0.14em] text-blue uppercase">Feature 3 of 3</p>
                          <h2 className="mt-2 font-display text-xl text-ink">{currentTour.title}</h2>
                          <p className="mt-2 leading-relaxed text-muted-foreground">{currentTour.body}</p>
                        </div>
                      </div>
                      <MiniAnalyticsPreview />
                      <div className="border-t border-border/60 pt-5">
                        <h3 className="font-display text-lg text-ink">Choose your experience</h3>
                        <p className="mt-1 text-sm text-muted-foreground">Both modes use the same study engine. You can change this any time in Settings.</p>
                        <div className="mt-4 grid gap-4 sm:grid-cols-2" role="radiogroup" aria-label="Study style">
                          <ModeSelectionCard title="Professional" description="Clean dashboard, mastery analytics, and focused review." icon={Compass} selected={mode === "professional"} onSelect={() => setMode("professional")} index={0} preview={<MiniAnalyticsPreview />} />
                          <ModeSelectionCard title="Gamified" description="The same study engine with XP, streaks, badges, and quests." icon={Sparkles} selected={mode === "gamified"} onSelect={() => setMode("gamified")} index={1} preview={<MiniQuestPreview />} />
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </Surface>
            </>
          )}
        </motion.div>
      </AnimatePresence>

      {error && <p role="alert" className="rounded-2xl bg-destructive/10 p-4 text-sm text-destructive">{error}</p>}

      <div className="flex items-center justify-between border-t border-border/60 pt-6">
        <SecondaryButton
          disabled={submitting || (step === "profile")}
          onClick={() => {
            if (step === "courses") setNextStep("profile");
            if (step === "diagnostic") setNextStep("courses");
            if (step === "tour") {
              if (tourIndex > 0) setTourIndex((index) => index - 1);
              else setNextStep("diagnostic");
            }
          }}
        >
          Back
        </SecondaryButton>

        {step === "profile" && <PrimaryButton disabled={!isProfileValid || submitting} onClick={persistProfile}>{submitting ? "Saving..." : "Continue"}</PrimaryButton>}
        {step === "courses" && <PrimaryButton disabled={!selectedIds.length || submitting} onClick={persistCourses}>{submitting ? "Saving..." : "Continue"}</PrimaryButton>}
        {step === "diagnostic" && <PrimaryButton disabled={submitting} onClick={skipDiagnostic}>{submitting ? "Saving..." : "Skip for now"}</PrimaryButton>}
        {step === "tour" && (tourIndex < TOUR_PANELS.length - 1 ? <PrimaryButton onClick={() => setTourIndex((index) => index + 1)}>Continue</PrimaryButton> : <PrimaryButton disabled={submitting} onClick={finishOnboarding}>{submitting ? "Setting up..." : "Start studying"}</PrimaryButton>)}
      </div>
    </motion.div>
  );
}
