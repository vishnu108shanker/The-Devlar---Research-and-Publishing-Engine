# Prerequisites.md

**Audience:** coding agents and the builder.
**Last updated:** 2026-10-18

This lists what must exist **before** work starts, split by stage. Only the current stage's requirements are blocking. If a required item is missing, **stop and report it**; do not work around it.

Versions below are minimums or "current stable." Pin the exact versions you use in a version file (for example `.tool-versions` or `pyproject.toml`) when the repo is created, and record the decision.

---

## A. Required now (Stage 0: Foundation and walking skeleton)

### Tools on the builder's machine

| Tool | Why | Verify |
|---|---|---|
| Git | Version control | `git --version` |
| GitHub account, SSH or token access | Repo, CI/CD | `ssh -T git@github.com` |
| Docker and Docker Compose | Containers, local database | `docker --version` and `docker compose version` |
| Python 3.12 or newer | Pipeline service | `python3 --version` |
| `uv` (**Proposed**) | Python dependency and environment management | `uv --version` |
| Node.js (current LTS) and npm | Web service | `node --version` and `npm --version` |
| PostgreSQL client (`psql`) | Inspect and test the database | `psql --version` |
| AWS CLI v2 | Interact with AWS | `aws --version` |
| Terraform (**Proposed**) | Infrastructure as code | `terraform version` |
| `pre-commit` | Local quality checks | `pre-commit --version` |

### AWS access

- An AWS account you control, with:
  - MFA enabled on the root user, and the root user **not** used for daily work.
  - An administrative IAM identity (or IAM Identity Center user) with MFA for setup work.
  - A **budget alert** created before any paid resource exists.
  - A chosen primary region (record it in an ADR).
- AWS CLI configured for that identity. Verify: `aws sts get-caller-identity` shows the expected account.
- Permission to create: VPC/networking, EC2, IAM roles and OIDC provider, SSM parameters, CloudWatch logs and alarms, SNS, and (if chosen) RDS. Record any permission gap.

### GitHub setup

- A repository with `main` protected (pull requests required, CI required, no force-push).
- GitHub Actions enabled.
- An OIDC trust between GitHub and AWS (created during Stage 0 tasks), so **no long-lived AWS keys** are stored in GitHub.

### Local environment variables (local development only)

Provide a `.env.example` with fake values. Real `.env` is git-ignored and never deployed.

| Variable | Purpose | Needed |
|---|---|---|
| `APP_ENV` | `local`, `dev`, or `prod` | Stage 0 |
| `DATABASE_URL` | Connection string for the current role | Stage 0 |
| `LOG_LEVEL` | Logging verbosity | Stage 0 |
| `FETCH_TARGET_URL` | The fixed URL for the skeleton fetcher | Stage 0 |
| `AWS_REGION` | Region | Stage 0 |

In deployed environments, configuration comes from the environment and secrets from SSM, not from `.env`.

### Database (local)

- A PostgreSQL container started via Docker Compose.
- Three roles available locally to match deployed environments (see `Architecture.md` Section 4): owner, pipeline read-write, web read-only.
- Verify: `psql "$DATABASE_URL" -c "select 1;"` returns a row.

### Understanding required before starting (read, do not master)

- What a container image and a container are.
- What a database migration is and why schema is never edited by hand.
- What IAM roles and policies are, and what "least privilege" means.
- What idempotent means (repeating an operation gives the same result).
- What structured logging is.

If a concept is unclear, ask for a short explanation before starting the task that needs it.

---

## B. Required later (do **not** set up now)

| Stage | Requirement | Verify when needed |
|---|---|---|
| Phase 1 | LLM provider account, API key stored in SSM, spending cap configured | A test call succeeds; cap enforced in code |
| Phase 1 | A hand-labeled claim set for one announcement | File exists in `evals/` and was reviewed by the builder |
| Phase 2 | pgvector available in the chosen PostgreSQL environment | `select * from pg_extension where extname = 'vector';` |
| Phase 2 | Embedding model access | Test embedding call succeeds |
| Phase 3 | Decision on orchestration approach (ADR) | ADR accepted |
| Phase 4 | Alert channel with escalation; failure-injection tooling | Test alert received |
| Phase 5 | Domain name and TLS plan; rate-limiting approach | ADR accepted |
| Phase 6 | Anything experimental (Redis, Kafka, Kubernetes, etc.) | Only with an approved experiment write-up |

---

## C. Verification script for Stage 0

Before starting any Stage 0 task, an agent should confirm (and report results):

```
git --version
docker --version && docker compose version
python3 --version
node --version
psql --version
aws --version && aws sts get-caller-identity
terraform version
pre-commit --version
```

If any command fails, report the failure and stop. Do not install or change tools without being asked.

---

## D. What agents must not assume

- Do not assume AWS credentials exist in the sandbox. Ask.
- Do not assume `prod` may be touched. It may not, unless a task says so.
- Do not assume any paid service is approved. Ask before using one.
