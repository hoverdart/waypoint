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

  test("onboarding -> dashboard -> daily plan -> practice -> results", async ({ page }, testInfo) => {
    const serverErrors: string[] = [];
    page.on("response", response => {
      if (response.status() >= 500) serverErrors.push(`${response.status()} ${new URL(response.url()).pathname}`);
    });
    await page.goto("/");
    await clerk.signIn({ page, emailAddress: testUser.email });

    await page.goto("/onboarding");
    await expect(page.getByText("Build your AP study path")).toBeVisible();
    await page.getByRole("radio", { name: /Professional/ }).click();
    await page.getByRole("button", { name: "Continue" }).click();

    await expect(page.getByText("Which AP exams are you taking?")).toBeVisible();
    await page.getByRole("button", { name: "AP Biology", exact: true }).click();
    await page.getByRole("button", { name: "Continue" }).click();

    await expect(page.getByText("A few details per subject")).toBeVisible();
    await page.getByRole("button", { name: "Start studying" }).click();

    await expect(page).toHaveURL(/\/dashboard/);
    // "AP Biology" appears twice on the dashboard (the ProgressCompass legend
    // and the CourseReadinessCard tile) - scope to the course card link.
    await expect(page.getByRole("link", { name: /AP Biology/ })).toBeVisible();

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
    await expect(page.getByText("Your answer", { exact: true }).first()).toBeVisible();
    await page.screenshot({ path: testInfo.outputPath("results-desktop.png"), fullPage: true });

    await page.goto("/subjects");
    await page.getByText("AP Biology", { exact: true }).locator("../..").getByRole("link", { name: "Open course" }).click();
    await expect(page.getByRole("region", { name: "Course curriculum" })).toBeVisible();
    await page.getByLabel("Session length").selectOption("5");
    await page.getByRole("button", { name: "Practice the whole course" }).click();
    await expect(page).toHaveURL(/\/practice\/session\/\d+/);
    const practiceUrl = page.url();
    const firstAnswer = page.locator("main button").filter({ hasText: /^[A-D]\./ }).first();
    const answerText = await firstAnswer.textContent();
    await firstAnswer.click();
    await page.getByRole("button", { name: "Save & exit" }).click();
    await expect(page).toHaveURL(/\/practice$/);
    await page.goto(practiceUrl);
    await expect(page.getByRole("button", { pressed: true }).filter({ hasText: answerText! })).toBeVisible();
    await answerEntirePracticeSession(page);
    await expect(page).toHaveURL(/\/practice\/results\/\d+/);

    await page.goto("/daily-plan");
    await page.getByRole("button", { name: "Start", exact: true }).first().click();
    await expect(page).toHaveURL(/planItemId=/);
    await answerEntirePracticeSession(page);
    await expect(page).toHaveURL(/\/practice\/results\/\d+/);
    await page.goto("/daily-plan");
    await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
    await page.goto("/settings");
    await page.getByRole("button", { name: "Manage account", exact: true }).click();
    await expect(page.locator(".cl-userProfile-root")).toBeVisible();
    await page.reload();
    const minutes = page.getByLabel("Daily minutes for AP Biology");
    await minutes.fill("35");
    await page.getByRole("button", { name: "Save course preferences" }).click();
    await expect(page.getByRole("status")).toContainText("Course preferences saved");
    await page.reload();
    await expect(page.getByLabel("Daily minutes for AP Biology")).toHaveValue("35");
    await expect(page.getByText(/@unknown.local/)).toHaveCount(0);
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: "instant" }));
    await page.screenshot({ path: testInfo.outputPath("settings-desktop.png"), fullPage: true });
    await page.getByRole("checkbox", { name: "AP Biology", exact: true }).uncheck();
    await page.getByRole("button", { name: "Save course preferences" }).click();
    await expect(page.getByRole("status")).toContainText("Course preferences saved");
    await page.goto("/subjects");
    await expect(page.getByRole("link", { name: "Add it in Settings" }).first()).toHaveAttribute("href", "/settings");
    await page.goto("/practice");
    await expect(page.getByRole("link", { name: /Review/ }).first()).toBeVisible();
    await page.goto("/settings");
    await page.getByRole("checkbox", { name: "AP Biology", exact: true }).check();
    await page.getByRole("button", { name: "Save course preferences" }).click();
    await expect(page.getByRole("status")).toContainText("Course preferences saved");
    await page.emulateMedia({ reducedMotion: "reduce" });
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/dashboard");
    await expect(page.getByRole("link", { name: /AP Biology/ })).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(390);
    await expect(page.getByRole("heading", { name: /Welcome back/ })).toBeVisible();
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: "instant" }));
    const mobileNav = page.getByRole("navigation", { name: "Mobile navigation" });
    await expect(mobileNav).toBeVisible();
    const navBounds = await mobileNav.boundingBox();
    expect(navBounds!.y).toBeGreaterThan(750);
    expect(navBounds!.y + navBounds!.height).toBeLessThanOrEqual(844);
    await page.screenshot({ path: testInfo.outputPath("dashboard-mobile.png"), fullPage: true });
    await page.getByRole("link", { name: "Account", exact: true }).click();
    await page.getByRole("button", { name: "Sign out", exact: true }).click();
    await expect(page).toHaveURL(/\/$/);
    await page.goto("/dashboard");
    await expect(page).toHaveURL(/\/login/);
    expect(serverErrors).toEqual([]);
  });
});

/** Handles both MCQ (click an option) and FRQ (type a response) questions,
 * answering every question in the session until the final "Finish" click. */
async function answerEntirePracticeSession(page: Page) {
  for (let guard = 0; guard < 25; guard++) {
    const progress = page.getByRole("progressbar");
    const current = Number(await progress.getAttribute("aria-valuenow"));
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
    await expect(progress).toHaveAttribute("aria-valuenow", String(current + 1));
  }
  throw new Error("Practice session did not finish within the expected number of questions");
}
