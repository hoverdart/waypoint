import { afterEach, describe, expect, it, vi } from "vitest";
import { fireEvent, render, screen } from "@testing-library/react";
import { AnimatedLoginLink } from "./AnimatedLoginLink";

const push = vi.fn();

vi.mock("next/navigation", () => ({ useRouter: () => ({ push }) }));

describe("AnimatedLoginLink", () => {
  afterEach(() => vi.useRealTimers());

  it("keeps an accessible href and starts navigation after the click animation", () => {
    vi.useFakeTimers();
    render(<AnimatedLoginLink>Log in</AnimatedLoginLink>);
    const link = screen.getByRole("link", { name: "Log in" });

    expect(link).toHaveAttribute("href", "/login");
    fireEvent.click(link);
    expect(push).not.toHaveBeenCalled();
    vi.advanceTimersByTime(160);
    expect(push).toHaveBeenCalledWith("/login");
  });
});
