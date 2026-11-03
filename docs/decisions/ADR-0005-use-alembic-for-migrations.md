# ADR-0005: Use Alembic for Database Migrations

**Status:** Accepted
**Date:** 2026-11-02
**Context:** The Devlar pipeline and research platform requires version-controlled, repeatable schema migrations across development and production.
**Decision:** We choose Alembic because it is the standard Python migration tool, native to SQLAlchemy, and directly matches our Python pipeline stack.
**Consequences:** Schema revisions are tracked in Git under `db/migrations`, run reproducibly via CLI/code, and avoid mismatched toolchains across environments.
