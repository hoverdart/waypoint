"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { PillButton } from "@/components/kit/PillButton";
import { Surface } from "@/components/kit/Surface";
import { Chip } from "@/components/kit/Pills";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { ApiError, AdminQuestionDetail, updateAdminQuestion, updateQuestionStatus } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

const STATUS_TRANSITIONS: Record<AdminQuestionDetail["validation_status"], string[]> = {
  draft: ["approved", "rejected", "needs_review"],
  needs_review: ["approved", "rejected"],
  approved: ["needs_review", "rejected"],
  rejected: ["needs_review"],
};

export function AdminQuestionEditor({ question }: { question: AdminQuestionDetail }) {
  const router = useRouter();
  const getToken = useApiToken();
  const [prompt, setPrompt] = useState(question.prompt);
  const [correctAnswer, setCorrectAnswer] = useState(question.correct_answer);
  const [options, setOptions] = useState(question.options);
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);
  const [statusChanging, setStatusChanging] = useState(false);

  async function handleSave() {
    setSaving(true);
    setError(null);
    try {
      const updated = await updateAdminQuestion(question.id, {
        prompt, correct_answer: correctAnswer,
        ...(question.type === "mcq" ? { options: options.map(option => ({ ...option, is_correct: option.label === correctAnswer })) } : {}),
      }, getToken);
      router.replace(`/admin/questions/${updated.id}`);
      router.refresh();
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "Could not save this question. Please try again.");
    } finally {
      setSaving(false);
    }
  }

  async function handleStatusChange(status: string) {
    setStatusChanging(true);
    setError(null);
    try {
      await updateQuestionStatus(question.id, status as AdminQuestionDetail["validation_status"], getToken);
      router.refresh();
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "Could not update the review status. Please try again.");
    } finally {
      setStatusChanging(false);
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between gap-4">
        <h1 className="font-display text-3xl text-ink">Question #{question.id}</h1>
        <Chip tone="blue">{question.validation_status}</Chip>
      </div>

      {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
      <p className="text-sm text-muted-foreground">Version {question.version}. Saving creates a new draft and archives this version, preserving student history.</p>
      {!question.is_active && <p role="status">This version is archived. Open the current version from the question list to edit it.</p>}
      <Surface className="p-6">
        <h2 className="font-display mb-5 text-lg text-ink">Content</h2>
        <div className="space-y-4">
          <div className="space-y-1.5">
            <Label htmlFor="question-prompt">Prompt</Label>
            <Textarea id="question-prompt" value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={4} />
          </div>
          <div className="space-y-1.5">
            <Label htmlFor="correct-answer">Correct answer</Label>
            {question.type === "mcq" ? <select id="correct-answer" className="w-full rounded-md border border-input bg-background p-2" value={correctAnswer} onChange={e => setCorrectAnswer(e.target.value)}>{options.map(option => <option key={option.label}>{option.label}</option>)}</select> : <Input id="correct-answer" value={correctAnswer} onChange={(e) => setCorrectAnswer(e.target.value)} />}
          </div>

          {question.options.length > 0 && (
            <div className="space-y-1.5">
              <Label>Options</Label>
              <ul className="space-y-1 text-sm">
                {options.map((opt, index) => (
                  <li key={opt.label} className={opt.is_correct ? "font-medium text-blue" : "text-ink-soft"}>
                    <Label htmlFor={`option-${opt.label}`}>Option {opt.label}</Label>
                    <Input id={`option-${opt.label}`} value={opt.text} onChange={e => setOptions(previous => previous.map((option, i) => i === index ? { ...option, text: e.target.value } : option))} />
                  </li>
                ))}
              </ul>
            </div>
          )}

          <PillButton disabled={saving || statusChanging || !question.is_active} onClick={handleSave}>
            {saving ? "Saving..." : "Save changes"}
          </PillButton>
        </div>
      </Surface>

      <Surface className="p-6">
        <h2 className="font-display mb-5 text-lg text-ink">Validation status</h2>
        <div className="flex flex-wrap gap-2">
          {STATUS_TRANSITIONS[question.validation_status].map((status) => (
            <PillButton
              key={status}
              variant="secondary"
              disabled={statusChanging || saving || !question.is_active}
              onClick={() => handleStatusChange(status)}
            >
              Mark {status.replace("_", " ")}
            </PillButton>
          ))}
        </div>
      </Surface>

      {question.reports.length > 0 && (
        <Surface className="p-6">
          <h2 className="font-display mb-5 text-lg text-ink">Student reports ({question.reports.length})</h2>
          <div className="space-y-2">
            {question.reports.map((report) => (
              <div key={report.id} className="rounded-2xl border border-border/60 p-4 text-sm">
                <p className="font-medium text-ink">{report.reason}</p>
                {report.details && <p className="text-muted-foreground">{report.details}</p>}
              </div>
            ))}
          </div>
        </Surface>
      )}
    </div>
  );
}
