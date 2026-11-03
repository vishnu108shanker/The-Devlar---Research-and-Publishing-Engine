"""create_database_roles

Revision ID: 21dd431de4e6
Revises: ee23a1bde755
Create Date: 2026-11-02 19:48:06.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21dd431de4e6'
down_revision: Union[str, Sequence[str], None] = 'ee23a1bde755'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create roles if they don't exist
    op.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'devlar_pipeline') THEN
                CREATE ROLE devlar_pipeline WITH LOGIN PASSWORD 'pipeline_secret_password';
            END IF;
            IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'devlar_web') THEN
                CREATE ROLE devlar_web WITH LOGIN PASSWORD 'web_secret_password';
            END IF;
        END
        $$;
        """
    )
    # Grant permissions:
    # devlar_pipeline: can read and write (SELECT, INSERT, UPDATE, DELETE)
    op.execute("GRANT CONNECT ON DATABASE devlar TO devlar_pipeline;")
    op.execute("GRANT USAGE ON SCHEMA public TO devlar_pipeline;")
    op.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO devlar_pipeline;")
    op.execute("ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO devlar_pipeline;")

    # devlar_web: read-only (SELECT)
    op.execute("GRANT CONNECT ON DATABASE devlar TO devlar_web;")
    op.execute("GRANT USAGE ON SCHEMA public TO devlar_web;")
    op.execute("GRANT SELECT ON ALL TABLES IN SCHEMA public TO devlar_web;")
    op.execute("ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO devlar_web;")


def downgrade() -> None:
    op.execute("REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM devlar_web;")
    op.execute("REVOKE USAGE ON SCHEMA public FROM devlar_web;")
    op.execute("REVOKE CONNECT ON DATABASE devlar FROM devlar_web;")
    op.execute("DROP ROLE IF EXISTS devlar_web;")

    op.execute("REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM devlar_pipeline;")
    op.execute("REVOKE USAGE ON SCHEMA public FROM devlar_pipeline;")
    op.execute("REVOKE CONNECT ON DATABASE devlar FROM devlar_pipeline;")
    op.execute("DROP ROLE IF EXISTS devlar_pipeline;")
