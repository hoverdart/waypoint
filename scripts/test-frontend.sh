#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
frontend_dir="$repo_root/frontend"

if [[ ! -d "$frontend_dir/node_modules" ]]; then
  echo "Missing frontend/node_modules. Run npm ci in frontend first." >&2
  exit 1
fi

cd "$frontend_dir"
npm run lint
npx next typegen
npx tsc --noEmit
npm run test -- "$@"
