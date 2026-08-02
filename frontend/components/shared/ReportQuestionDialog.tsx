"use client";

import { useState } from "react";
import { PillButton } from "@/components/kit/PillButton";
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { reportQuestion } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

const REASONS = [
  { value: "wrong_answer", label: "The marked correct answer looks wrong" },
  { value: "confusing_prompt", label: "The question is confusing or ambiguous" },
  { value: "typo", label: "Typo or formatting issue" },
  { value: "other", label: "Something else" },
];

export function ReportQuestionDialog({ questionId }: { questionId: number }) {
  const getToken = useApiToken();
  const [open, setOpen] = useState(false);
  const [reason, setReason] = useState(REASONS[0].value);
  const [details, setDetails] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  async function handleSubmit() {
    setSubmitting(true);
    try {
      await reportQuestion(questionId, { reason, details }, getToken);
      setSubmitted(true);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <Dialog
      open={open}
      onOpenChange={(next) => {
        setOpen(next);
        if (!next) setSubmitted(false);
      }}
    >
      <DialogTrigger render={<PillButton variant="ghost" size="sm" />}>Report question</DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle className="font-display text-lg text-ink">Report this question</DialogTitle>
        </DialogHeader>
        {submitted ? (
          <p className="text-sm leading-relaxed text-muted-foreground">Thanks - our team will take a look.</p>
        ) : (
          <div className="space-y-4">
            <div className="space-y-2">
              <Label className="text-ink">Reason</Label>
              <Select value={reason} onValueChange={(value) => value && setReason(value)}>
                <SelectTrigger className="rounded-xl border-border">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent className="rounded-2xl">
                  {REASONS.map((r) => (
                    <SelectItem key={r.value} value={r.value}>
                      {r.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label className="text-ink">Details (optional)</Label>
              <Textarea
                value={details}
                onChange={(e) => setDetails(e.target.value)}
                rows={3}
                className="rounded-xl border-border px-3.5 py-2.5 leading-relaxed text-ink focus-visible:border-blue focus-visible:ring-blue/40"
              />
            </div>
          </div>
        )}
        <DialogFooter>
          {!submitted && (
            <PillButton disabled={submitting} onClick={handleSubmit}>
              Submit report
            </PillButton>
          )}
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
