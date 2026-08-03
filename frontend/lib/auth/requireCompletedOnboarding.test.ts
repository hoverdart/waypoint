import { beforeEach, describe, expect, it, vi } from "vitest";
import { requireCompletedOnboarding } from "./requireCompletedOnboarding";

const mocks = vi.hoisted(() => ({ redirect: vi.fn() }));
vi.mock("next/navigation", () => ({ redirect: mocks.redirect }));

const user = {
  id: 1,
  auth_provider_id: "user_1",
  email: "student@example.com",
  display_name: "Ada",
  mode: "professional" as const,
};

describe("requireCompletedOnboarding", () => {
  beforeEach(() => vi.clearAllMocks());

  it("routes an incomplete student through onboarding", () => {
    requireCompletedOnboarding({ ...user, onboarding_step: "courses" });
    expect(mocks.redirect).toHaveBeenCalledWith("/onboarding");
  });

  it("keeps complete and legacy accounts accessible", () => {
    requireCompletedOnboarding({ ...user, onboarding_step: "complete" });
    requireCompletedOnboarding(user);
    expect(mocks.redirect).not.toHaveBeenCalled();
  });
});
