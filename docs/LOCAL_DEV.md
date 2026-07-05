# Local Development

Two ways to run WayPoint locally: **Docker-free** (the primary path used to build and verify
this project - Docker was not installed on the dev machine) and **Docker Compose** (for
portability / other machines). They use different ports for Postgres by default in some setups,
so don't run both against the same database at once.

## Docker-free (Postgres via Homebrew + local processes)

### 1. Postgres

```bash
brew services start postgresql@16
# if that reports an error, start it directly instead:
/opt/homebrew/opt/postgresql@16/bin/pg_ctl -D /opt/homebrew/var/postgresql@16 \
  -l /opt/homebrew/var/log/postgresql@16.log start

# confirm it's up
/opt/homebrew/opt/postgresql@16/bin/pg_isready

# one-time: create the app role and databases
/opt/homebrew/opt/postgresql@16/bin/createuser -s waypoint
/opt/homebrew/opt/postgresql@16/bin/psql postgres -c "ALTER USER waypoint WITH PASSWORD 'waypoint';"
/opt/homebrew/opt/postgresql@16/bin/createdb -O waypoint waypoint_dev
/opt/homebrew/opt/postgresql@16/bin/createdb -O waypoint waypoint_test
```

> If `brew services list` shows `postgresql@16` stuck in an `error` state with no process
> actually running, it's almost always a stale `postmaster.pid` lock file left over from an
> unclean shutdown. Confirm nothing is really running (`ps aux | grep postgres`), then remove
> `/opt/homebrew/var/postgresql@16/postmaster.pid` and start again.

### 2. Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

cp .env.example .env
# fill in CLERK_SECRET_KEY / ANTHROPIC_API_KEY when you have them - the app boots without
# them, but sign-in and the AI explain button won't work until they're set.

alembic upgrade head
python -m scripts.seed
uvicorn app.main:app --reload --port 8000
```

Run the test suite (uses `waypoint_test`, isolated per test via a savepoint):

```bash
pytest
```

### 3. Frontend

```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev
```

Then open `http://localhost:3000`. The frontend calls the backend at
`NEXT_PUBLIC_API_BASE_URL` (defaults to `http://localhost:8000`).

## Docker Compose

Requires real env files first (Compose reads `backend/.env` and `frontend/.env.local`
directly - the `.example` files are just templates):

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
cp .env.example .env   # Postgres creds + port overrides used by docker-compose.yml itself

docker compose up --build
```

This starts three services: `postgres`, `backend` (runs `alembic upgrade head` on boot, then
serves on :8000), and `frontend` (serves on :3000). Set `RUN_SEED_ON_BOOT=true` in
`backend/.env` if you want the seed script to run automatically on first boot.

This compose setup has been reviewed carefully but not run end-to-end on the machine this
project was built on, since Docker wasn't installed there - verify it on a machine that has
Docker before relying on it for deployment.
