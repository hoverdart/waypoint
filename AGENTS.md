<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

# Development rules

- Create or update tests for every feature change. Run the relevant tests and ensure they pass before pushing. If they fail, determine whether the platform or the test is wrong and fix the appropriate one.
- Keep changes within the part of the platform being worked on: frontend changes stay in `frontend/`, backend changes stay in `backend/`. If a request requires changes across multiple subfolders or platform areas, notify the user before proceeding.
- When work is explicitly scoped to one platform area, do not modify the other area. Coordinate any necessary cross-area contract changes with the developer working there.
- Maintain a root-level `CONTEXT.md` that records the current implementation context and completed changes. If it does not exist, create it before implementation; if it exists, update it as work progresses, including affected area, notable decisions, and verification performed.
- Reuse existing components and patterns. Create a new component only when it is genuinely necessary; prioritize scalability, functionality, and simplicity.
- Keep changes focused. After each implemented feature, provide a concise diff summary: files changed, feature delivered, limitations, and any relevant next steps.
- When a feature request is unclear, ask clarifying questions before implementing. Do not make assumptions unless the user explicitly authorizes them or later context answers the question. Outline the intended approach in the chat so developers can confirm it before work begins.
- Apply sound security practices throughout development. When a security risk or requirement is unclear, research it, ask the developer, or evaluate solutions before implementing. Warn the developer about vulnerabilities introduced or discovered in feature work, and ensure a practical fix can be built.
