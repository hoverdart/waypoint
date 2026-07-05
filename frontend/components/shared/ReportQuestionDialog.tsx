"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
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
      <DialogTrigger render={<Button variant="ghost" size="sm" />}>Report question</DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Report this question</DialogTitle>
        </DialogHeader>
        {submitted ? (
          <p className="text-sm text-muted-foreground">Thanks - our team will take a look.</p>
        ) : (
          <div className="space-y-4">
            <div className="space-y-1.5">
              <Label>Reason</Label>
              <Select value={reason} onValueChange={(value) => value && setReason(value)}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {REASONS.map((r) => (
                    <SelectItem key={r.value} value={r.value}>
                      {r.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-1.5">
              <Label>Details (optional)</Label>
              <Textarea value={details} onChange={(e) => setDetails(e.target.value)} rows={3} />
            </div>
          </div>
        )}
        <DialogFooter>
          {!submitted && (
            <Button disabled={submitting} onClick={handleSubmit}>
              Submit report
            </Button>
          )}
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
