import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";
import { ModeToggle } from "./ModeToggle";
vi.mock("@/lib/api", () => ({ updateMe: vi.fn().mockRejectedValue(new Error("offline")) }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ refresh: vi.fn() }) }));
it("restores the previous mode when saving fails", async () => {
  render(<ModeToggle initialMode="professional" />);
  await userEvent.click(screen.getByRole("switch"));
  expect(await screen.findByRole("alert")).toHaveTextContent("try again");
  expect(screen.getByRole("switch")).not.toBeChecked();
});
