import { clerkSetup } from "@clerk/testing/playwright";

/** Runs once before the whole E2E suite. Fetches a Clerk Testing Token (to
 * bypass bot detection) whenever real Clerk credentials are available; the
 * authenticated golden-path spec skips itself when they aren't. */
export default async function globalSetup() {
  if (!process.env.CLERK_SECRET_KEY) {
    console.log("[e2e] CLERK_SECRET_KEY not set - skipping Clerk testing-token setup.");
    return;
  }
  await clerkSetup();
}
