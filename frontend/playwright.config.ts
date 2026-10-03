import { defineConfig, devices } from "@playwright/test";
import path from "path";
import { config as loadEnv } from "dotenv";

// The Playwright process is separate from the Next.js dev/build process, so
// it doesn't get .env.local for free the way `next dev`/`next build` do -
// CLERK_SECRET_KEY in particular is needed here for the authenticated spec.
loadEnv({ path: [path.resolve(__dirname, ".env.local"), path.resolve(__dirname, ".env")], quiet: true });

// Dedicated ports keep browser checks away from unrelated local applications.
const frontendPort = Number(process.env.E2E_FRONTEND_PORT || 3109);
const backendPort = Number(process.env.E2E_BACKEND_PORT || 8109);
if (![frontendPort, backendPort].every(port => Number.isInteger(port) && port > 1024 && port < 65536)) {
  throw new Error("E2E ports must be integers between 1025 and 65535");
}
const frontendUrl = `http://localhost:${frontendPort}`;
const backendUrl = `http://localhost:${backendPort}`;

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
    baseURL: frontendUrl,
    trace: "on-first-retry",
    screenshot: "only-on-failure",
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
  webServer: [
    {
      // Tests against the production build, per Next.js's own testing guidance.
      command: `npm run build && npm run start -- --port ${frontendPort}`,
      url: frontendUrl,
      env: { NEXT_PUBLIC_API_BASE_URL: backendUrl },
      reuseExistingServer: false,
      timeout: 180_000,
      stdout: "pipe",
    },
    {
      command: `./.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port ${backendPort}`,
      cwd: path.resolve(__dirname, "../backend"),
      url: `${backendUrl}/health`,
      env: { CORS_ALLOWED_ORIGINS: JSON.stringify([frontendUrl]) },
      reuseExistingServer: false,
      timeout: 60_000,
      stdout: "pipe",
    },
  ],
});
