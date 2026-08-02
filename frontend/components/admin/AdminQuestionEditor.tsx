"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { PillButton } from "@/components/kit/PillButton";
import { Surface } from "@/components/kit/Surface";
import { Chip } from "@/components/kit/Pills";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { AdminQuestionDetail, updateAdminQuestion, updateQuestionStatus } from "@/lib/api";
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
  const [saving, setSaving] = useState(false);
  const [statusChanging, setStatusChanging] = useState(false);

  async function handleSave() {
    setSaving(true);
    try {
      await updateAdminQuestion(question.id, { prompt, correct_answer: correctAnswer }, getToken);
      router.refresh();
    } finally {
      setSaving(false);
    }
  }

  async function handleStatusChange(status: string) {
    setStatusChanging(true);
    try {
      await updateQuestionStatus(question.id, status as AdminQuestionDetail["validation_status"], getToken);
      router.refresh();
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

      <Surface className="p-6">
        <h2 className="font-display mb-5 text-lg text-ink">Content</h2>
        <div className="space-y-4">
          <div className="space-y-1.5">
            <Label>Prompt</Label>
            <Textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={4} />
          </div>
          <div className="space-y-1.5">
            <Label>Correct answer</Label>
            <Input value={correctAnswer} onChange={(e) => setCorrectAnswer(e.target.value)} />
          </div>

          {question.options.length > 0 && (
            <div className="space-y-1.5">
              <Label>Options</Label>
              <ul className="space-y-1 text-sm">
                {question.options.map((opt) => (
                  <li key={opt.label} className={opt.is_correct ? "font-medium text-blue" : "text-ink-soft"}>
                    {opt.label}. {opt.text}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <PillButton disabled={saving} onClick={handleSave}>
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
              disabled={statusChanging}
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
