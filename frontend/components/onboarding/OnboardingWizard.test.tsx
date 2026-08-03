import { beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { OnboardingState, Subject } from "@/lib/api";
import { OnboardingWizard } from "./OnboardingWizard";

const mocks = vi.hoisted(() => ({
  replace: vi.fn(),
  saveOnboardingDraft: vi.fn(),
  completeOnboarding: vi.fn(),
}));

vi.mock("next/navigation", () => ({
  useRouter: () => ({ replace: mocks.replace, refresh: vi.fn() }),
}));

vi.mock("@/lib/hooks/useApiToken", () => ({
  useApiToken: () => "test-token",
}));

vi.mock("@/lib/api", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/api")>();
  return { ...actual, saveOnboardingDraft: mocks.saveOnboardingDraft, completeOnboarding: mocks.completeOnboarding };
});

const subjects: Subject[] = [
  { id: 1, name: "AP Biology", ap_exam_code: "biology", description: null, is_active: true, display_order: 0 },
  { id: 2, name: "AP Calculus AB", ap_exam_code: "calculus-ab", description: null, is_active: true, display_order: 1 },
];

function makeState(overrides: Partial<OnboardingState> = {}): OnboardingState {
  return {
    user: {
      id: 1,
      auth_provider_id: "user_1",
      email: "student@example.com",
      display_name: null,
      grade_level: null,
      onboarding_step: "profile",
      diagnostic_status: "pending",
      mode: "professional",
    },
    user_subjects: [],
    onboarding_step: "profile",
    diagnostic_status: "pending",
    ...overrides,
  };
}

describe("OnboardingWizard", () => {
  beforeEach(() => vi.clearAllMocks());

  it("saves profile and AP goals before advancing", async () => {
    const user = userEvent.setup();
    mocks.saveOnboardingDraft.mockResolvedValue(makeState());
    render(<OnboardingWizard subjects={subjects} initialState={makeState()} />);

    await user.type(screen.getByLabelText("What should we call you?"), "Ada");
    await user.click(screen.getByRole("radio", { name: "11th grade" }));
    await user.click(screen.getByRole("button", { name: "Continue" }));

    await waitFor(() => expect(mocks.saveOnboardingDraft).toHaveBeenCalledWith(
      { display_name: "Ada", grade_level: 11, onboarding_step: "courses" },
      "test-token"
    ));
    expect(await screen.findByText("Set your AP goals")).toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: "AP Biology" }));
    await user.click(screen.getByRole("radio", { name: "5" }));
    await user.click(screen.getByRole("button", { name: "Continue" }));

    await waitFor(() => expect(mocks.saveOnboardingDraft).toHaveBeenLastCalledWith(
      {
        subjects: [{ subject_id: 1, target_score: 5, exam_date: null, study_minutes_per_day: 20 }],
        onboarding_step: "diagnostic",
      },
      "test-token"
    ));
    expect(await screen.findByText("Diagnostic coming soon")).toBeInTheDocument();
  });

  it("resumes at the diagnostic and completes the skipped-baseline path with the selected mode", async () => {
    const user = userEvent.setup();
    mocks.saveOnboardingDraft.mockResolvedValue(makeState());
    mocks.completeOnboarding.mockResolvedValue(makeState({ onboarding_step: "complete" }));
    const diagnosticView = render(
      <OnboardingWizard
        subjects={subjects}
        initialState={makeState({
          onboarding_step: "diagnostic",
          diagnostic_status: "pending",
          user_subjects: [{ id: 1, subject_id: 1, target_score: 4, exam_date: null, study_minutes_per_day: 20, is_active: true }],
        })}
      />
    );

    expect(screen.getByText("Diagnostic coming soon")).toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Skip for now" }));
    await waitFor(() => expect(mocks.saveOnboardingDraft).toHaveBeenCalledWith(
      { diagnostic_status: "skipped", onboarding_step: "tour" },
      "test-token"
    ));

    // AnimatePresence intentionally keeps the prior step mounted through its
    // visual exit; mount the persisted tour state to test a real resume too.
    diagnosticView.unmount();
    render(
      <OnboardingWizard
        subjects={subjects}
        initialState={makeState({
          onboarding_step: "tour",
          diagnostic_status: "skipped",
          user_subjects: [{ id: 1, subject_id: 1, target_score: 4, exam_date: null, study_minutes_per_day: 20, is_active: true }],
        })}
      />
    );

    await user.click(screen.getByRole("button", { name: "Continue" }));
    await user.click(screen.getByRole("button", { name: "Continue" }));
    await user.click(screen.getByRole("radio", { name: /Gamified/i }));
    await user.click(screen.getByRole("button", { name: "Start studying" }));

    await waitFor(() => expect(mocks.completeOnboarding).toHaveBeenCalledWith(
      { mode: "gamified", diagnostic_status: "skipped" },
      "test-token"
    ));
    expect(mocks.replace).toHaveBeenCalledWith("/dashboard");
  });

  it("renders saved course choices when onboarding resumes", () => {
    render(
      <OnboardingWizard
        subjects={subjects}
        initialState={makeState({
          onboarding_step: "courses",
          user_subjects: [{ id: 1, subject_id: 1, target_score: 3, exam_date: "2027-05-12", study_minutes_per_day: 45, is_active: true }],
        })}
      />
    );

    expect(screen.getByRole("button", { name: "AP Biology" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByRole("radio", { name: "3" })).toHaveAttribute("aria-checked", "true");
    expect(screen.getByDisplayValue("2027-05-12")).toBeInTheDocument();
  });
});
