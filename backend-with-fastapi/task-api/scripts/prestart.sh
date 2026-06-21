#!/usr/bin/env bash
# Pre-start script — wait for DB and run migrations (used in Docker)

set -e

echo "Running database migrations..."
alembic upgrade head
echo "Migrations complete."
