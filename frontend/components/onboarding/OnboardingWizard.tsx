"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { ApiError, OnboardingSubjectInput, Subject, UserMode, submitOnboarding } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";

const STUDY_TIME_PRESETS = [10, 20, 45, 60];
const TARGET_SCORES = [3, 4, 5];

type Step = "mode" | "subjects" | "details";

interface SubjectDraft {
  target_score: number;
  exam_date: string;
  study_minutes_per_day: number;
}

function defaultDraft(): SubjectDraft {
  return { target_score: 4, exam_date: "", study_minutes_per_day: 20 };
}

export function OnboardingWizard({ subjects }: { subjects: Subject[] }) {
  const router = useRouter();
  const getToken = useApiToken();

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

  return (
    <Card>
      <CardHeader>
        <CardTitle>
          {step === "mode" && "How do you want WayPoint to feel?"}
          {step === "subjects" && "Which AP exams are you taking?"}
          {step === "details" && "A few details per subject"}
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        {step === "mode" && (
          <div className="grid gap-3 sm:grid-cols-2">
            {(
              [
                { value: "professional" as const, title: "Professional", body: "Clean dashboard, mastery, analytics." },
                { value: "gamified" as const, title: "Gamified", body: "Same engine, plus XP, streaks, and badges." },
              ]
            ).map((option) => (
              <button
                key={option.value}
                type="button"
                onClick={() => setMode(option.value)}
                className={cn(
                  "rounded-lg border p-4 text-left transition-colors",
                  mode === option.value ? "border-primary bg-primary/5" : "hover:bg-muted"
                )}
              >
                <p className="font-medium">{option.title}</p>
                <p className="text-sm text-muted-foreground">{option.body}</p>
              </button>
            ))}
          </div>
        )}

        {step === "subjects" && (
          <div className="flex flex-wrap gap-2">
            {subjects.map((subject) => (
              <button
                key={subject.id}
                type="button"
                onClick={() => toggleSubject(subject.id)}
                className={cn(
                  "rounded-full border px-3 py-1.5 text-sm transition-colors",
                  selectedIds.includes(subject.id)
                    ? "border-primary bg-primary text-primary-foreground"
                    : "hover:bg-muted"
                )}
              >
                {subject.name}
              </button>
            ))}
          </div>
        )}

        {step === "details" &&
          selectedIds.map((id) => {
            const subject = subjects.find((s) => s.id === id);
            const draft = drafts[id] ?? defaultDraft();
            return (
              <div key={id} className="space-y-3 rounded-lg border p-4">
                <p className="font-medium">{subject?.name}</p>

                <div className="grid gap-3 sm:grid-cols-2">
                  <div className="space-y-1.5">
                    <Label>Target score</Label>
                    <div className="flex gap-2">
                      {TARGET_SCORES.map((score) => (
                        <button
                          key={score}
                          type="button"
                          onClick={() => updateDraft(id, { target_score: score })}
                          className={cn(
                            "size-9 rounded-full border text-sm",
                            draft.target_score === score
                              ? "border-primary bg-primary text-primary-foreground"
                              : "hover:bg-muted"
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
                        onClick={() => updateDraft(id, { study_minutes_per_day: minutes })}
                        className={cn(
                          "rounded-full border px-3 py-1.5 text-sm",
                          draft.study_minutes_per_day === minutes
                            ? "border-primary bg-primary text-primary-foreground"
                            : "hover:bg-muted"
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

        {error && <p className="text-sm text-destructive">{error}</p>}

        <div className="flex justify-between pt-2">
          <Button
            variant="ghost"
            disabled={step === "mode"}
            onClick={() => setStep(step === "details" ? "subjects" : "mode")}
          >
            Back
          </Button>

          {step !== "details" && (
            <Button
              disabled={step === "subjects" && selectedIds.length === 0}
              onClick={() => setStep(step === "mode" ? "subjects" : "details")}
            >
              Continue
            </Button>
          )}
          {step === "details" && (
            <Button disabled={submitting} onClick={handleSubmit}>
              {submitting ? "Setting up..." : "Start studying"}
            </Button>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
