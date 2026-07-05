"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
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
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold tracking-tight">Question #{question.id}</h1>
        <Badge>{question.validation_status}</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Content</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
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
                  <li key={opt.label} className={opt.is_correct ? "font-medium text-primary" : ""}>
                    {opt.label}. {opt.text}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <Button disabled={saving} onClick={handleSave}>
            {saving ? "Saving..." : "Save changes"}
          </Button>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Validation status</CardTitle>
        </CardHeader>
        <CardContent className="flex gap-2">
          {STATUS_TRANSITIONS[question.validation_status].map((status) => (
            <Button key={status} variant="outline" disabled={statusChanging} onClick={() => handleStatusChange(status)}>
              Mark {status.replace("_", " ")}
            </Button>
          ))}
        </CardContent>
      </Card>

      {question.reports.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Student reports ({question.reports.length})</CardTitle>
          </CardHeader>
          <CardContent className="space-y-2">
            {question.reports.map((report) => (
              <div key={report.id} className="rounded-md border p-3 text-sm">
                <p className="font-medium">{report.reason}</p>
                {report.details && <p className="text-muted-foreground">{report.details}</p>}
              </div>
            ))}
          </CardContent>
        </Card>
      )}
    </div>
  );
}
