import { test, expect, type Page } from "@playwright/test";
import { clerk } from "@clerk/testing/playwright";
import { createTestUser } from "./fixtures/testUser";

test.describe("Authenticated golden path", () => {
  test.skip(!process.env.CLERK_SECRET_KEY, "requires CLERK_SECRET_KEY to create/sign in a test user");
  // A full diagnostic can run up to DIAGNOSTIC_QUESTION_COUNT (20) questions.
  test.describe.configure({ timeout: 90_000 });

  let testUser: Awaited<ReturnType<typeof createTestUser>>;

  test.beforeAll(async () => {
    testUser = await createTestUser();
  });

  test.afterAll(async () => {
    await testUser?.remove();
  });

  test("onboarding -> dashboard -> daily plan -> practice -> results", async ({ page }) => {
    await page.goto("/");
    await clerk.signIn({ page, emailAddress: testUser.email });

    await page.goto("/onboarding");
    await expect(page.getByText("How do you want WayPoint to feel?")).toBeVisible();
    await page.getByRole("button", { name: /Professional/ }).click();
    await page.getByRole("button", { name: "Continue" }).click();

    await expect(page.getByText("Which AP exams are you taking?")).toBeVisible();
    await page.getByRole("button", { name: "AP Biology", exact: true }).click();
    await page.getByRole("button", { name: "Continue" }).click();

    await expect(page.getByText("A few details per subject")).toBeVisible();
    await page.getByRole("button", { name: "Start studying" }).click();

    await expect(page).toHaveURL(/\/dashboard/);
    await expect(page.getByText("AP Biology")).toBeVisible();

    // A daily-plan item is scoped to a single random topic, and this seed
    // data is intentionally demo-scale (a handful of questions spread across
    // many topics) - so a lot of individual topics have zero questions. The
    // diagnostic pulls from across the whole subject instead, which is far
    // more robust for this exact reason.
    await page.goto("/daily-plan");
    const generateButton = page.getByRole("button", { name: "Generate today's plan" });
    if (await generateButton.isVisible()) {
      await generateButton.click();
    }
    await expect(page.getByText("point budget")).toBeVisible({ timeout: 15_000 });

    await page.goto("/subjects");
    await page.getByRole("button", { name: "Take diagnostic" }).first().click();

    await expect(page).toHaveURL(/\/practice\/session\/\d+/);
    await answerEntirePracticeSession(page);

    await expect(page).toHaveURL(/\/practice\/results\/\d+/);
    await expect(page.getByText("Baseline established")).toBeVisible();
  });
});

/** Handles both MCQ (click an option) and FRQ (type a response) questions,
 * answering every question in the session until the final "Finish" click. */
async function answerEntirePracticeSession(page: Page) {
  for (let guard = 0; guard < 25; guard++) {
    const textarea = page.getByPlaceholder("Write your response here...");
    if (await textarea.isVisible().catch(() => false)) {
      await textarea.fill("This is a placeholder free-response answer for E2E testing.");
    } else {
      await page.locator("main button").filter({ hasText: /^[A-D]\./ }).first().click();
    }

    const nextOrFinish = page.getByRole("button", { name: /^(Next|Finish|Submitting\.\.\.)$/ });
    const label = await nextOrFinish.textContent();
    await nextOrFinish.click();
    if (label === "Finish") return;
  }
  throw new Error("Practice session did not finish within the expected number of questions");
}
