import { test, expect } from "@playwright/test";

test.describe("Unauthenticated visitors", () => {
  test("landing page states the core promise and links to signup/login", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("heading", { level: 1 })).toContainText(
      "Every day, we tell you exactly what to study next"
    );
    // These render as <a> tags styled as buttons - the shadcn/Base UI build
    // this app uses sets role="button" explicitly on them, so they're queried
    // as buttons rather than links despite being real anchor elements. Scoped
    // to <main> since the nav header has its own "Log in" link too.
    const hero = page.getByRole("main");
    await expect(hero.getByRole("button", { name: "Get started free" })).toHaveAttribute("href", "/signup");
    await expect(hero.getByRole("button", { name: "Log in" })).toHaveAttribute("href", "/login");
  });

  test("landing page lists the priority AP subjects", async ({ page }) => {
    await page.goto("/");
    for (const subject of ["AP Calculus AB", "AP Biology", "AP Psychology", "AP US History", "AP Chemistry", "AP Computer Science A"]) {
      await expect(page.getByText(subject, { exact: true })).toBeVisible();
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
