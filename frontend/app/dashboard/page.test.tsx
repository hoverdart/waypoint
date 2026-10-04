import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  token: vi.fn(), sync: vi.fn(), dashboard: vi.fn(), subject: vi.fn(),
  redirect: vi.fn((path: string) => { throw new Error(`redirect:${path}`); }),
}));
vi.mock("next/navigation", () => ({ redirect: mocks.redirect }));
vi.mock("@/lib/auth/getServerAuthToken", () => ({ getServerAuthToken: mocks.token }));
vi.mock("@/lib/api", () => ({ syncUser: mocks.sync, getDashboard: mocks.dashboard, getSubject: mocks.subject }));
vi.mock("@/components/dashboard/DashboardView", () => ({ DashboardView: () => null }));
import DashboardPage from "./page";

describe("dashboard account synchronization", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.token.mockResolvedValue("session-token");
    mocks.sync.mockResolvedValue({ id: "user" });
    mocks.dashboard.mockResolvedValue({ subjects: [] });
  });
  it("awaits synchronization before requesting protected dashboard data", async () => {
    let release!: () => void;
    mocks.sync.mockImplementationOnce(() => new Promise<void>(resolve => { release = resolve; }));
    const page = DashboardPage();
    await vi.waitFor(() => expect(mocks.sync).toHaveBeenCalledWith("session-token"));
    expect(mocks.dashboard).not.toHaveBeenCalled();
    release();
    await page;
    expect(mocks.dashboard).toHaveBeenCalledWith("session-token");
  });
  it("redirects signed-out visitors without calling protected APIs", async () => {
    mocks.token.mockResolvedValueOnce(null);
    await expect(DashboardPage()).rejects.toThrow("redirect:/login");
    expect(mocks.sync).not.toHaveBeenCalled();
    expect(mocks.dashboard).not.toHaveBeenCalled();
  });
  it("does not load the dashboard if synchronization fails", async () => {
    mocks.sync.mockRejectedValueOnce(new Error("Authentication failed"));
    await expect(DashboardPage()).rejects.toThrow("Authentication failed");
    expect(mocks.dashboard).not.toHaveBeenCalled();
  });
});
