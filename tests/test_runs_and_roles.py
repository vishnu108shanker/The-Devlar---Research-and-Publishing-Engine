import os
import psycopg2
import pytest
from services.pipeline.run_job import record_run, get_db_connection


def test_script_idempotency_real_postgres():
    """
    Step 5: Run the script twice with the same run_key and prove:
    1. First run reports inserted=True.
    2. Second run reports inserted=False and returns the same run_id.
    3. Exactly one row exists in the runs table for that run_key.
    """
    test_run_key = "test-idempotency-key-2026-11-02"

    # Cleanup if pre-existing
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM runs WHERE run_key = %s;", (test_run_key,))
    conn.close()

    # First run
    res1 = record_run(test_run_key)
    assert res1["inserted"] is True
    assert res1["run_id"] is not None
    run_id_first = res1["run_id"]

    # Second run
    res2 = record_run(test_run_key)
    assert res2["inserted"] is False
    assert res2["run_id"] == run_id_first

    # Verify directly via DB query that there is exactly one row
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT count(*) FROM runs WHERE run_key = %s;", (test_run_key,))
            count = cur.fetchone()[0]
            assert count == 1
    conn.close()


def test_database_roles_permissions():
    """
    Step 6: Two database roles:
    - devlar_pipeline (can write/insert)
    - devlar_web (read-only, fails on insert)
    """
    pipeline_key = "test-role-pipeline-key"
    web_key = "test-role-web-key"

    # 1. devlar_pipeline can insert
    conn_pipeline = get_db_connection(user="devlar_pipeline", password="pipeline_secret_password")
    with conn_pipeline:
        with conn_pipeline.cursor() as cur:
            cur.execute("DELETE FROM runs WHERE run_key = %s;", (pipeline_key,))
            cur.execute("INSERT INTO runs (run_key, status) VALUES (%s, 'pending');", (pipeline_key,))
    conn_pipeline.close()

    # 2. devlar_web can read (SELECT)
    conn_web = get_db_connection(user="devlar_web", password="web_secret_password")
    with conn_web:
        with conn_web.cursor() as cur:
            cur.execute("SELECT count(*) FROM runs WHERE run_key = %s;", (pipeline_key,))
            count = cur.fetchone()[0]
            assert count == 1
    conn_web.close()

    # 3. devlar_web FAILS when trying to INSERT
    conn_web_write = get_db_connection(user="devlar_web", password="web_secret_password")
    with pytest.raises(psycopg2.errors.InsufficientPrivilege) as exc_info:
        with conn_web_write:
            with conn_web_write.cursor() as cur:
                cur.execute("INSERT INTO runs (run_key, status) VALUES (%s, 'pending');", (web_key,))
    conn_web_write.close()

    assert "permission denied for table runs" in str(exc_info.value)
