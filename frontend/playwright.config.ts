import { defineConfig, devices } from "@playwright/test";
import path from "path";
import { config as loadEnv } from "dotenv";

// The Playwright process is separate from the Next.js dev/build process, so
// it doesn't get .env.local for free the way `next dev`/`next build` do -
// CLERK_SECRET_KEY in particular is needed here for the authenticated spec.
loadEnv({ path: path.resolve(__dirname, ".env.local") });

const isCI = !!process.env.CI;

export default defineConfig({
  testDir: "./e2e",
  globalSetup: require.resolve("./e2e/global-setup.ts"),
  fullyParallel: true,
  forbidOnly: isCI,
  // Clerk's own dev-instance banner warns of "strict usage limits" on
  // free/dev instances - a retry absorbs an occasional slow/rate-limited
  // widget load rather than failing the whole suite on external flakiness.
  retries: isCI ? 2 : 1,
  workers: isCI ? 1 : undefined,
  reporter: isCI ? "github" : "html",
  timeout: 30_000,
  use: {
    baseURL: "http://localhost:3000",
    trace: "on-first-retry",
    screenshot: "only-on-failure",
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
  webServer: [
    {
      // Tests against the production build, per Next.js's own testing guidance.
      command: "npm run build && npm run start",
      url: "http://localhost:3000",
      reuseExistingServer: !isCI,
      timeout: 180_000,
      stdout: "pipe",
    },
    {
      command: "./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000",
      cwd: path.resolve(__dirname, "../backend"),
      url: "http://localhost:8000/health",
      reuseExistingServer: !isCI,
      timeout: 60_000,
      stdout: "pipe",
    },
  ],
});
