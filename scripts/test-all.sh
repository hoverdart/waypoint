#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
run_e2e=false

if [[ "${1:-}" == "--e2e" ]]; then
  run_e2e=true
  shift
fi

if [[ $# -gt 0 ]]; then
  echo "Usage: scripts/test-all.sh [--e2e]" >&2
  exit 2
fi

"$repo_root/scripts/test-backend.sh"
"$repo_root/scripts/test-frontend.sh"

if "$run_e2e"; then
  "$repo_root/scripts/test-e2e.sh"
fi
