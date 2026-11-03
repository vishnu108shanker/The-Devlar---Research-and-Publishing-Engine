#!/bin/sh
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Starting pipeline job..."
exec python services/pipeline/run_job.py "$@"
