import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";
import { AccountActions } from "./AccountActions";
const { open, signOut } = vi.hoisted(() => ({ open: vi.fn(), signOut: vi.fn() }));
vi.mock("@clerk/nextjs", () => ({ useClerk: () => ({ openUserProfile: open, signOut }) }));
it("opens account management and signs out through Clerk", async () => {
  signOut.mockResolvedValueOnce(undefined);
  render(<AccountActions />);
  await userEvent.click(screen.getByRole("button", { name: "Manage account" }));
  expect(open).toHaveBeenCalled();
  await userEvent.click(screen.getByRole("button", { name: "Sign out" }));
  expect(signOut).toHaveBeenCalledWith({ redirectUrl: "/" });
});
it("allows retry when sign-out fails", async () => {
  signOut.mockRejectedValueOnce(new Error("offline"));
  render(<AccountActions />);
  await userEvent.click(screen.getByRole("button", { name: "Sign out" }));
  expect(await screen.findByRole("alert")).toHaveTextContent("try again");
  expect(screen.getByRole("button", { name: "Sign out" })).toBeEnabled();
});
