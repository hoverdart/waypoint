import { afterEach, describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import { AuthContinuation } from "./AuthContinuation";

const replace = vi.fn();
vi.mock("next/navigation", () => ({ useRouter: () => ({ replace }) }));

describe("AuthContinuation", () => {
  afterEach(() => vi.useRealTimers());

  it("confirms successful sign-in before routing", () => {
    vi.useFakeTimers();
    render(<AuthContinuation destination="/onboarding" />);
    expect(screen.getByText("You’re in")).toBeInTheDocument();
    vi.advanceTimersByTime(420);
    expect(replace).toHaveBeenCalledWith("/onboarding");
  });
});
