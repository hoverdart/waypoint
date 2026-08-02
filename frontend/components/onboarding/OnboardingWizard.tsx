"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { AnimatePresence, motion, useReducedMotion } from "framer-motion";
import { Compass, Sparkles } from "lucide-react";
import { ApiError, OnboardingSubjectInput, Subject, UserMode, submitOnboarding } from "@/lib/api";
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

// Every toggle in the wizard - subject, target score, study minutes - is the
// same pill, so the selected/unselected treatment lives in one place.
const TOGGLE = "rounded-full border text-sm font-medium outline-none transition-colors focus-visible:ring-3 focus-visible:ring-blue/40";
const TOGGLE_ON = "border-blue bg-blue-soft/60 text-ink";
const TOGGLE_OFF = "border-border/70 bg-card text-ink-soft hover:border-blue/40 hover:bg-blue-soft/40";

type Step = OnboardingStep;

interface SubjectDraft {
  target_score: number;
  exam_date: string;
  study_minutes_per_day: number;
}

function defaultDraft(): SubjectDraft {
  return { target_score: 4, exam_date: "", study_minutes_per_day: 20 };
}

const HERO_COPY: Record<Step, { title: string; body: string }> = {
  mode: {
    title: "Build your AP study path",
    body: "WayPoint will adapt your dashboard, daily plan, and progress feedback around this style.",
  },
  subjects: {
    title: "Which AP exams are you taking?",
    body: "Select every class you're in - WayPoint plots a separate mastery route for each one.",
  },
  details: {
    title: "A few details per subject",
    body: "Your target score and exam date shape how aggressively WayPoint paces your daily plan.",
  },
};

export function OnboardingWizard({ subjects }: { subjects: Subject[] }) {
  const router = useRouter();
  const getToken = useApiToken();
  const reduceMotion = useReducedMotion();

  const [step, setStep] = useState<Step>("mode");
  const [mode, setMode] = useState<UserMode>("professional");
  const [selectedIds, setSelectedIds] = useState<number[]>([]);
  const [drafts, setDrafts] = useState<Record<number, SubjectDraft>>({});
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function toggleSubject(id: number) {
    setSelectedIds((prev) => (prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]));
  }

  function updateDraft(id: number, patch: Partial<SubjectDraft>) {
    setDrafts((prev) => ({ ...prev, [id]: { ...defaultDraft(), ...prev[id], ...patch } }));
  }

  async function handleSubmit() {
    setSubmitting(true);
    setError(null);
    try {
      const payloadSubjects: OnboardingSubjectInput[] = selectedIds.map((id) => {
        const draft = drafts[id] ?? defaultDraft();
        return {
          subject_id: id,
          target_score: draft.target_score,
          exam_date: draft.exam_date || null,
          study_minutes_per_day: draft.study_minutes_per_day,
        };
      });
      await submitOnboarding({ mode, subjects: payloadSubjects }, getToken);
      router.push("/dashboard");
    } catch (e) {
      setError(e instanceof ApiError ? e.detail : "Something went wrong - please try again.");
    } finally {
      setSubmitting(false);
    }
  }

  const hero = HERO_COPY[step];

  return (
    <motion.div
      initial={{ opacity: 0, y: reduceMotion ? 0 : 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: reduceMotion ? 0 : 0.5, ease: "easeOut" }}
      className="space-y-8"
    >
      <OnboardingProgress step={step} />

      <PageHeader title={hero.title} sub={hero.body} />

      <Surface tone="raised">
        <div className="space-y-7 p-5 sm:p-7">
          <AnimatePresence mode="wait">
            <motion.div
              key={step}
              initial={{ opacity: 0, x: reduceMotion ? 0 : 12 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: reduceMotion ? 0 : -12 }}
              transition={{ duration: reduceMotion ? 0 : 0.25, ease: "easeOut" }}
            >
              {step === "mode" && (
                <div className="grid gap-4 sm:grid-cols-2" role="radiogroup" aria-label="Study style">
                  <ModeSelectionCard
                    title="Professional"
                    description="Clean dashboard, mastery analytics, exam-readiness tracking, and focused review."
                    icon={Compass}
                    selected={mode === "professional"}
                    onSelect={() => setMode("professional")}
                    index={0}
                    preview={
                      <div className="space-y-3">
                        <div className="flex items-center gap-3">
                          <MiniMasteryRing value={72} />
                          <div className="space-y-1">
                            <p className="text-xs font-semibold text-ink">Exam Readiness</p>
                            <p className="text-xs text-muted-foreground">Weak Topics: 3</p>
                            <p className="text-xs text-muted-foreground">Next Review: Unit 4 FRQ</p>
                          </div>
                        </div>
                        <MiniAnalyticsPreview />
                      </div>
                    }
                  />
                  <ModeSelectionCard
                    title="Gamified"
                    description="Same study engine, plus XP, streaks, badges, and daily quests."
                    icon={Sparkles}
                    selected={mode === "gamified"}
                    onSelect={() => setMode("gamified")}
                    index={1}
                    preview={<MiniQuestPreview />}
                  />
                </div>
              )}

              {step === "subjects" && (
                <div className="flex flex-wrap gap-2">
                  {subjects.map((subject) => (
                    <button
                      key={subject.id}
                      type="button"
                      aria-pressed={selectedIds.includes(subject.id)}
                      onClick={() => toggleSubject(subject.id)}
                      className={cn(
                        TOGGLE,
                        "px-4 py-2",
                        selectedIds.includes(subject.id) ? TOGGLE_ON : TOGGLE_OFF
                      )}
                    >
                      {subject.name}
                    </button>
                  ))}
                </div>
              )}

              {step === "details" && (
                <div className="space-y-4">
                  {selectedIds.map((id) => {
                    const subject = subjects.find((s) => s.id === id);
                    const draft = drafts[id] ?? defaultDraft();
                    return (
                      <div key={id} className="space-y-4 rounded-2xl border border-border/60 bg-muted/40 p-5">
                        <p className="font-display text-base text-ink">{subject?.name}</p>

                        <div className="grid gap-4 sm:grid-cols-2">
                          <div className="space-y-1.5">
                            <Label>Target score</Label>
                            <div className="flex gap-2">
                              {TARGET_SCORES.map((score) => (
                                <button
                                  key={score}
                                  type="button"
                                  aria-pressed={draft.target_score === score}
                                  onClick={() => updateDraft(id, { target_score: score })}
                                  className={cn(
                                    TOGGLE,
                                    "size-10 tabular-nums",
                                    draft.target_score === score ? TOGGLE_ON : TOGGLE_OFF
                                  )}
                                >
                                  {score}
                                </button>
                              ))}
                            </div>
                          </div>

                          <div className="space-y-1.5">
                            <Label htmlFor={`exam-date-${id}`}>Exam date</Label>
                            <Input
                              id={`exam-date-${id}`}
                              type="date"
                              value={draft.exam_date}
                              onChange={(e) => updateDraft(id, { exam_date: e.target.value })}
                            />
                          </div>
                        </div>

                        <div className="space-y-1.5">
                          <Label>Minutes per day</Label>
                          <div className="flex gap-2">
                            {STUDY_TIME_PRESETS.map((minutes) => (
                              <button
                                key={minutes}
                                type="button"
                                aria-pressed={draft.study_minutes_per_day === minutes}
                                onClick={() => updateDraft(id, { study_minutes_per_day: minutes })}
                                className={cn(
                                  TOGGLE,
                                  "px-4 py-2",
                                  draft.study_minutes_per_day === minutes ? TOGGLE_ON : TOGGLE_OFF
                                )}
                              >
                                {minutes} min
                              </button>
                            ))}
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </motion.div>
          </AnimatePresence>

          {error && (
            <p className="rounded-2xl bg-destructive/10 p-4 text-sm text-destructive">{error}</p>
          )}

          <div className="flex items-center justify-between border-t border-border/60 pt-6">
            <SecondaryButton
              disabled={step === "mode"}
              onClick={() => setStep(step === "details" ? "subjects" : "mode")}
            >
              Back
            </SecondaryButton>

            {step !== "details" && (
              <PrimaryButton
                disabled={step === "subjects" && selectedIds.length === 0}
                onClick={() => setStep(step === "mode" ? "subjects" : "details")}
              >
                Continue
              </PrimaryButton>
            )}
            {step === "details" && (
              <PrimaryButton disabled={submitting} onClick={handleSubmit}>
                {submitting ? "Setting up..." : "Start studying"}
              </PrimaryButton>
            )}
          </div>
        </div>
      </Surface>
    </motion.div>
  );
}
