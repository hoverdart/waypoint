import { test, expect } from "@playwright/test";

test.describe("Unauthenticated visitors", () => {
  test("landing page states the core promise and links to signup/login", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("heading", { level: 1 })).toContainText(
      "Every day, we tell you exactly what to study next"
    );
    // The design-system PillLink is a plain Next <Link>, so these are real
    // links with the default link role - unlike the old Base UI button-styled
    // anchors, which set role="button" explicitly. Scoped to the hero region
    // since the nav header has its own "Log in" link and the final CTA section
    // has its own "Get started free" link.
    const hero = page.getByRole("region", { name: "Hero" });
    await expect(hero.getByRole("link", { name: "Get started free" })).toHaveAttribute("href", "/signup");
    await expect(hero.getByRole("link", { name: "Log in" })).toHaveAttribute("href", "/login");
  });

  test("landing page lists the priority AP subjects", async ({ page }) => {
    await page.goto("/");
    // Scoped to the subject showcase region - subject names also appear as
    // decorative floating signals and in the hero preview card elsewhere on
    // the page.
    const showcase = page.getByRole("region", { name: "Priority AP subjects" });
    for (const subject of ["AP Calculus AB", "AP Biology", "AP Psychology", "AP US History", "AP Chemistry", "AP Computer Science A"]) {
      await expect(showcase.getByText(subject, { exact: true })).toBeVisible();
    }
  });

  test("/login renders Clerk's sign-in form", async ({ page }) => {
    await page.goto("/login");
    // Clerk's widget does a live round-trip to Clerk's own servers to load,
    // which can be slower than a same-app navigation - especially against a
    // free/dev Clerk instance, which Clerk's own docs note has strict rate
    // limits under heavy use.
    await expect(page.locator(".cl-rootBox")).toBeVisible({ timeout: 15_000 });
  });

  test("/signup renders Clerk's sign-up form", async ({ page }) => {
    await page.goto("/signup");
    // Clerk's widget does a live round-trip to Clerk's own servers to load,
    // which can be slower than a same-app navigation - especially against a
    // free/dev Clerk instance, which Clerk's own docs note has strict rate
    // limits under heavy use.
    await expect(page.locator(".cl-rootBox")).toBeVisible({ timeout: 15_000 });
  });

  test("visiting a protected route redirects to the app's own /login page", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page).toHaveURL(/\/login/);
  });

  test("every app route other than / /login /signup redirects unauthenticated visitors to login", async ({ page }) => {
    for (const route of ["/subjects", "/daily-plan", "/analytics", "/settings", "/admin/questions"]) {
      await page.goto(route);
      await expect(page).toHaveURL(/\/login/);
    }
  });
});
