import "@testing-library/jest-dom/vitest";
import { afterEach, vi } from "vitest";
import { cleanup } from "@testing-library/react";

/**
 * jsdom doesn't implement IntersectionObserver, and framer-motion constructs
 * one unguarded in `render/dom/viewport/index.mjs` - the
 * `typeof IntersectionObserver === "undefined"` check only covers its update
 * path. Without this stub, any component using `whileInView` (i.e. anything
 * wrapped in `<Reveal>`) throws a ReferenceError the moment it mounts.
 *
 * The stub is deliberately inert: it never invokes the callback, so nothing
 * schedules a React state update outside `act()`. Elements still mount and
 * render their children, so text, role and interaction queries behave
 * normally - the content just sits at its `initial` style, which assertions
 * don't inspect.
 */
class IntersectionObserverStub implements IntersectionObserver {
  readonly root: Element | Document | null = null;
  readonly rootMargin: string = "";
  readonly thresholds: ReadonlyArray<number> = [];

  observe(): void {}
  unobserve(): void {}
  disconnect(): void {}
  takeRecords(): IntersectionObserverEntry[] {
    return [];
  }
}

vi.stubGlobal("IntersectionObserver", IntersectionObserverStub);

/**
 * jsdom also has no `matchMedia`. Components guard for its absence, but
 * providing an inert "no preference" implementation means media-query-driven
 * code takes its normal branch under test instead of its fallback.
 */
vi.stubGlobal("matchMedia", (query: string): MediaQueryList => {
  const noop = () => {};
  return {
    matches: false,
    media: query,
    onchange: null,
    addEventListener: noop,
    removeEventListener: noop,
    addListener: noop,
    removeListener: noop,
    dispatchEvent: () => false,
  } as unknown as MediaQueryList;
});

afterEach(() => {
  cleanup();
});
