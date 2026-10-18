# Tasks.md

**Audience:** coding agents and the builder.
**Last updated:** 2026-10-18

The actionable backlog. The Roadmap says *when and why*; each task says *what to do and how to verify it*.

**Rules**
- Work on one task at a time, in dependency order.
- Only **Stage 0** is detailed. Later stages are placeholders on purpose; detail is added when the previous stage closes, using what was learned.
- Status values: `Not started`, `In progress`, `Blocked`, `Done`.
- A task is `Done` only when it meets the definition of done in `Conventions.md`, and its verification was run with real output.
- Tasks marked **[Builder]** need a human decision or action in AWS or GitHub; agents prepare and explain but do not guess.

**Task format:** Goal, Scope, Depends on, Acceptance criteria, Verification, Status.

---

## Stage 0: Foundation and walking skeleton

### T-0.1 Repository baseline
- **Goal:** a clean, protected repo with the standard layout and local quality checks.
- **Scope:** README, folder layout from `Conventions.md`, `.gitignore`, pre-commit (format, lint, secret scan), the seven project documents, `docs/decisions/`, `docs/runbooks/`, `docs/devlog/`. No application code.
- **Depends on:** Prerequisites section A (tools).
- **Acceptance criteria:**
  - `main` is protected: PR required, CI check required (placeholder allowed until T-0.10), no force-push. **[Builder]**
  - Pre-commit blocks a test commit containing a fake secret.
  - Documents are in the repo; `Vision.md` is present under that exact name.
- **Verification:** attempt to commit a fake secret and show it is blocked; show branch protection settings; `pre-commit run --all-files` passes.
- **Status:** Not started

### T-0.2 Settle the open Stage 0 decisions
- **Goal:** record decisions that block infrastructure work.
- **Scope:** ADRs for: repo layout (ADR-0001), compute shape (ADR-0002), database hosting RDS vs container (ADR-0003), IaC tool (ADR-0004), migration tool (ADR-0005), secrets store (ADR-0006), AWS region, run trigger, alert channel. Each ADR lists options, trade-offs including cost, and the decision. The builder decides; agents draft options.
- **Depends on:** T-0.1.
- **Acceptance criteria:** each ADR has status `Accepted`; `Architecture.md` decision register updated to match.
- **Verification:** the builder can explain each decision and its main alternative in a few sentences.
- **Status:** Not started

### T-0.3 AWS account safety
- **Goal:** the AWS account is safe and cost-limited before anything is created.
- **Scope:** MFA on root and admin identity; no root use; budget alert with email notification; chosen region; resource tagging standard (`project`, `env`, `owner`).
- **Depends on:** T-0.2 (region).
- **Acceptance criteria:** budget alert exists and a test notification was received; root has MFA; an admin identity with MFA is used for work. **[Builder]**
- **Verification:** screenshots or CLI output for budget and MFA status; `aws sts get-caller-identity` shows the non-root identity.
- **Status:** Not started

### T-0.4 Infrastructure bootstrap
- **Goal:** remote Terraform state and a first environment (`dev`) created from code.
- **Scope:** remote state with locking; networking; the compute resource and security groups per ADR-0002; tagging; no application yet. `prod` is added in T-0.15 from the same modules.
- **Depends on:** T-0.2, T-0.3.
- **Acceptance criteria:**
  - `terraform plan` is clean after apply (no drift).
  - The database is not publicly reachable.
  - Everything is tagged.
  - No state file or secret is committed.
- **Verification:** show `plan` output before apply and a clean plan after; show the security group rules; run a destroy-and-recreate of `dev` and record the time and issues in the devlog.
- **Status:** Not started

### T-0.5 Database provisioning and roles
- **Goal:** a PostgreSQL instance in `dev` with the three roles and schemas.
- **Scope:** database per ADR-0003; schemas `pipeline`, `content`, `web` (**Proposed**); roles `devlar_owner`, `pipeline_rw`, `web_ro`; grants as in `Architecture.md` Section 4. Local Docker Compose database mirrors the same roles.
- **Depends on:** T-0.4.
- **Acceptance criteria:** `web_ro` can read `content` and **cannot** write to it; `pipeline_rw` cannot alter schema; permissions are defined in code, not by hand.
- **Verification:** run test statements as each role and show allowed and denied outcomes.
- **Status:** Not started

### T-0.6 First migration and data model
- **Goal:** the minimal tables with idempotency designed in.
- **Scope:** migration tool per ADR-0005; tables `sources`, `runs`, `stage_runs` (see `Architecture.md` Section 4); unique constraints for idempotency; `timestamptz` columns; documented stable ID rule.
- **Depends on:** T-0.5.
- **Acceptance criteria:** migration applies on an empty database and is tested; inserting the same source twice results in one row; status values constrained by schema.
- **Verification:** run migration on a fresh container database and on `dev`; show the duplicate-insert test.
- **Status:** Not started

### T-0.7 Pipeline skeleton service
- **Goal:** a Python service that fetches one fixed URL and records a run.
- **Scope:** typed settings loaded at startup and validated; fetcher with timeout, size limit, `https` only; idempotent write to `sources`; a stub stage that writes `runs` and `stage_runs`; structured JSON logs with `run_id` and `stage`; explicit error handling per `Conventions.md`. No LLM calls.
- **Depends on:** T-0.6.
- **Acceptance criteria:** repeated runs on the same content create no duplicates; a failed fetch ends in a recorded `failed` state with a reason; logs contain the required fields; no secrets in logs.
- **Verification:** unit tests and integration tests with a real PostgreSQL container, including timeout, oversized response, and duplicate-delivery cases; show sample log lines.
- **Status:** Not started

### T-0.8 Web skeleton service
- **Goal:** a minimal service that reads and displays the latest run record, and exposes a health check.
- **Scope:** Node/Express service connecting as `web_ro`; one read endpoint and one health endpoint; a minimal page; structured logs.
- **Depends on:** T-0.6.
- **Acceptance criteria:** service cannot write to `content`; health endpoint reports database connectivity; no secrets in code or logs.
- **Verification:** automated test showing a write attempt as `web_ro` fails; health check output.
- **Status:** Not started

### T-0.9 Containerize both services
- **Goal:** reproducible, non-root images.
- **Scope:** one Dockerfile per service; minimal base images; non-root user; tagged with commit SHA; Docker Compose file for local development including PostgreSQL.
- **Depends on:** T-0.7, T-0.8.
- **Acceptance criteria:** images build reproducibly; container runs as non-root; no secrets in image layers; local `docker compose up` runs the skeleton end to end.
- **Verification:** `docker compose up` run with real output; inspect image for user and layers.
- **Status:** Not started

### T-0.10 Continuous integration
- **Goal:** every pull request is checked automatically.
- **Scope:** GitHub Actions workflow: lint, format check, type check, unit and integration tests, migration test on a fresh database, image build, dependency and image vulnerability scan, secret scan.
- **Depends on:** T-0.9.
- **Acceptance criteria:** CI is a required check on `main`; a deliberately failing test blocks merge; a deliberately added fake secret is caught.
- **Verification:** show a passing run and a deliberately failing run, then revert the failure.
- **Status:** Not started

### T-0.11 Secrets and configuration in AWS
- **Goal:** deployed services get configuration and secrets without `.env` files.
- **Scope:** secrets in the store per ADR-0006; per-component IAM roles with minimum permissions; services read configuration at startup.
- **Depends on:** T-0.4, T-0.9.
- **Acceptance criteria:** no `.env` file exists on the deployed host; each component's role can read only its own secrets; a missing required setting makes the service fail fast with a clear log.
- **Verification:** show the IAM policies, show service startup failure with a missing setting, and show it starting correctly with settings present.
- **Status:** Not started

### T-0.12 Continuous deployment to `dev`
- **Goal:** merging to `main` deploys to `dev` with no manual steps.
- **Scope:** GitHub OIDC trust to AWS (no stored keys); deployment workflow that pushes images and updates the running services; migrations applied as a controlled step before the new version starts; rollback procedure documented.
- **Depends on:** T-0.10, T-0.11.
- **Acceptance criteria:** a code change reaches `dev` through the pipeline only; no long-lived AWS keys exist in GitHub; a failed deployment leaves the previous version running.
- **Verification:** show a successful deploy run, a deliberately failing deploy and its recovery, and the OIDC trust configuration.
- **Status:** Not started

### T-0.13 Observability and a verified alert
- **Goal:** logs and an alert that actually works.
- **Scope:** ship JSON logs to the log service; a small set of metrics (run success/failure count, duration); one alarm for failed runs routed to the channel chosen in T-0.2; a runbook for that alarm.
- **Depends on:** T-0.12.
- **Acceptance criteria:** a deliberate failure produces an alert that was received; logs can be queried by `run_id`; the runbook says what to check and how to recover.
- **Verification:** trigger the failure, show the log trail and the received alert, and have someone else follow the runbook if possible.
- **Status:** Not started

### T-0.14 Backup and restore test
- **Goal:** prove the database can be restored.
- **Scope:** backup mechanism per ADR-0003; restore into a fresh instance; check data integrity; runbook with exact steps and time taken; define when the test is repeated.
- **Depends on:** T-0.12.
- **Acceptance criteria:** a restore was completed and the data matched; the runbook was followed as written.
- **Verification:** record row counts before and after restore and the time taken.
- **Status:** Not started

### T-0.15 Create `prod` from the same code
- **Goal:** a second environment built from the same infrastructure code, with approval-gated deployment.
- **Scope:** `prod` environment via Terraform; deployment to `prod` only after a manual approval in the pipeline; environment-specific differences documented.
- **Depends on:** T-0.12, T-0.13, T-0.14.
- **Acceptance criteria:** `prod` runs the same images as `dev` with its own secrets and data; promotion requires approval; a database backup exists in `prod`.
- **Verification:** show a promotion run with the approval step; show the `terraform plan` is clean for both environments.
- **Status:** Not started

### T-0.16 Stage 0 exit review
- **Goal:** close the stage with evidence and lessons.
- **Scope:** walk the Phase 0 evidence list in `Roadmap.md`; record actual cost against estimate; write the devlog; update `Architecture.md`; draft Stage 1 tasks from what was learned.
- **Depends on:** T-0.15.
- **Acceptance criteria:** every evidence item has proof; cost recorded; Stage 1 task list drafted; the builder can explain the system's boundaries, failure modes, and decisions.
- **Verification:** the builder walks through the system end to end without notes.
- **Status:** Not started

---

## Stage 1: Traceable article (placeholder)

Detailed tasks are written after Stage 0 closes. Expected themes, not tasks:

- Choose the LLM provider and wrap it thinly; enforce cost cap and timeouts.
- Pick one real announcement; hand-label its important claims.
- Record a baseline from the simplest approach.
- Model claims, evidence, and source passages.
- Build the traceable article path and the evaluation runner; run evals in CI.

## Stage 2: Knowledge layer (placeholder)

Source storage, keyword and vector retrieval measured on reviewed examples, entities and relationships with provenance.

## Stage 3: Iterative research (placeholder)

Resumable bounded workflow compared against the single-pass baseline.

## Stage 4: Reliability and quality gate (placeholder)

Claim and citation checks, failure-injection tests, security review.

## Stage 5: Reader-facing journal (placeholder)

Discovery, article storage, website with inline explanation and handoff, gated publication.

---

## Task change log

| Date | Change |
|---|---|
| 2026-10-18 | Initial Stage 0 backlog drafted. |
