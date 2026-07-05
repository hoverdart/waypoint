#!/bin/sh
set -e

alembic upgrade head

if [ "$RUN_SEED_ON_BOOT" = "true" ]; then
  python -m scripts.seed
fi

exec "$@"
