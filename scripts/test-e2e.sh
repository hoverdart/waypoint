#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
backend_dir="$repo_root/backend"
frontend_dir="$repo_root/frontend"

if [[ ! -x "$backend_dir/.venv/bin/python" ]]; then
  echo "Missing backend/.venv. Run the setup steps in docs/README.md first." >&2
  exit 1
fi
if [[ ! -d "$frontend_dir/node_modules" ]]; then
  echo "Missing frontend/node_modules. Run npm ci in frontend first." >&2
  exit 1
fi
if [[ ! -f "$frontend_dir/.env.local" ]]; then
  echo "Missing frontend/.env.local. Copy frontend/.env.example and add Clerk keys." >&2
  exit 1
fi

cd "$backend_dir"
.venv/bin/python -m alembic upgrade head
.venv/bin/python -m scripts.seed

cd "$frontend_dir"
exec npm run test:e2e -- "$@"
