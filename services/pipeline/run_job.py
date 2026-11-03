import json
import os
import sys
import time
from datetime import datetime, timezone
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()


def get_db_connection(user: str | None = None, password: str | None = None) -> psycopg2.extensions.connection:
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    dbname = os.getenv("POSTGRES_DB", "devlar")
    user = user or os.getenv("POSTGRES_USER", "postgres")
    password = password or os.getenv("POSTGRES_PASSWORD", "postgres_dev_password")

    return psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password,
        connect_timeout=5,
    )


def record_run(run_key: str, user: str | None = None, password: str | None = None) -> dict:
    start_time = time.perf_counter()
    conn = get_db_connection(user=user, password=password)
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Insert if not exists
                cur.execute(
                    """
                    INSERT INTO runs (run_key, status)
                    VALUES (%s, 'pending')
                    ON CONFLICT (run_key) DO NOTHING
                    RETURNING id, run_key, status, started_at;
                    """,
                    (run_key,),
                )
                row = cur.fetchone()
                if row:
                    inserted = True
                    run_id = str(row["id"])
                else:
                    inserted = False
                    cur.execute(
                        "SELECT id, run_key, status, started_at FROM runs WHERE run_key = %s;",
                        (run_key,),
                    )
                    existing = cur.fetchone()
                    run_id = str(existing["id"]) if existing else None

        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
        log_payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": "INFO",
            "service": "pipeline",
            "env": os.getenv("ENV", "development"),
            "event": "run_recorded",
            "message": f"Run {run_key} processed (inserted={inserted})",
            "run_id": run_id,
            "run_key": run_key,
            "inserted": inserted,
            "duration_ms": duration_ms,
        }
        return log_payload
    finally:
        conn.close()


def main():
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    run_key = sys.argv[1] if len(sys.argv) > 1 else f"hello-{date_str}"
    log_payload = record_run(run_key)
    print(json.dumps(log_payload))


if __name__ == "__main__":
    main()
