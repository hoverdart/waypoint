#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
backend_dir="$repo_root/backend"

if [[ ! -x "$backend_dir/.venv/bin/python" ]]; then
  echo "Missing backend/.venv. Run the setup steps in docs/README.md first." >&2
  exit 1
fi

cd "$backend_dir"
test_database_url="${TEST_DATABASE_URL:-postgresql+psycopg://waypoint:waypoint@localhost:5432/waypoint_test}"

if ! TEST_DATABASE_URL="$test_database_url" .venv/bin/python -c 'import os; from sqlalchemy import create_engine; connection = create_engine(os.environ["TEST_DATABASE_URL"]).connect(); connection.close()' >/dev/null 2>&1; then
  echo "Cannot connect to the backend test database." >&2
  echo "Start PostgreSQL, create the waypoint role and waypoint_test database, or set TEST_DATABASE_URL." >&2
  echo "See docs/README.md: First-time setup." >&2
  exit 1
fi

exec .venv/bin/python -m pytest "$@"
