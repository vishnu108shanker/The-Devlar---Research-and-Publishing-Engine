# The Devlar

Retired or retained as a historical planning artifact

A technology research and learning platform. It investigates important technology developments, grounds its explanations in evidence, and publishes articles only when they pass a quality gate. It is also a deliberate engineering education in DevOps, backend, and AI engineering.

- **Purpose, values, non-goals:** `Vision.md`
- **Decisions and system shape:** `Architecture.md`
- **Engineering rules and definition of done:** `Conventions.md`
- **Setup requirements:** `Prerequisites.md`
- **Backlog:** `Tasks.md`
- **Long-term plan:** `Roadmap.md`
- **Instructions for coding agents:** `AGENTS.md`

**Status:** Stage 0 (foundation and walking skeleton). Nothing described below as "later" exists yet.

---

## 1. Principles behind the structure

1. **Organize by responsibility.** The research pipeline, the reader-facing website, database migrations, infrastructure, and documentation each have one obvious home. Someone should find a responsibility without searching the whole repository.
2. **Make boundaries explicit.** There are two independent applications connected only through PostgreSQL: a Python production side and a PERN website. The folders mirror that boundary. A folder is **not** automatically a separate microservice.
3. **Separate application code from infrastructure.** Terraform, CI/CD workflows, migrations, application code, tests, and operational docs are distinguishable, so you can tell what a change affects and what the pipeline must validate.
4. **Make testing and security first-class.** Unit, integration, migration, and evaluation tests have fixed places from day one. Secret scanning, configuration validation, and container checks are part of the structure, not afterthoughts. No real secrets, cloud credentials, Terraform state, or production data are ever committed.
5. **Keep it understandable.** Clear names, predictable locations, shallow nesting (aim for at most four levels below the repo root for source folders). No dumping grounds.
6. **Grow only when needed.** Folders for later stages are **not created in advance**. They appear when their task begins.

> The structure is **Proposed** (see decision D-07 in `Architecture.md`). Change it through an ADR when real work shows a better shape.

---

## 2. Folder structure

Items marked *(later)* are intentionally absent in Stage 0. Create them only when a task in `Tasks.md` needs them.

```
devlar/
├── README.md                     This file: orientation and structure
├── Vision.md                     Purpose, values, non-goals
├── Roadmap.md                    Phased learning and delivery plan
├── Architecture.md               Current decisions: Accepted / Proposed / Deferred
├── Conventions.md                Engineering rules, definition of done
├── Prerequisites.md              Tools and access required, by stage
├── Tasks.md                      Actionable backlog
├── AGENTS.md                     Entry point for coding agents
├── .gitignore
├── .pre-commit-config.yaml       Format, lint, secret-scan checks run before commit
├── .env.example                  Fake values only; real .env is git-ignored
├── docker-compose.yml            Local development stack (app services + PostgreSQL)
│
├── .github/
│   └── workflows/                CI and CD pipeline definitions
│       ├── ci.yml                Lint, type check, tests, migration test, scans
│       └── deploy.yml            Deploy to dev, approval-gated promotion to prod
│
├── services/
│   ├── pipeline/                 PRODUCTION SIDE (Python)
│   │   ├── Dockerfile
│   │   ├── pyproject.toml        Dependencies and tool config
│   │   ├── src/devlar_pipeline/
│   │   │   ├── config/           Typed settings, validated at startup
│   │   │   ├── db/               Connections and queries for the pipeline role
│   │   │   ├── collectors/       Fetch and store raw sources
│   │   │   ├── stages/           Stage runner, status transitions, stub stage
│   │   │   ├── observability/    Structured logging, run and stage context
│   │   │   ├── research/         (later) Research engine
│   │   │   ├── editorial/        (later) Article synthesis
│   │   │   ├── quality/          (later) Quality gate
│   │   │   └── publisher/        (later) Publish passed articles
│   │   └── tests/
│   │       ├── unit/             Fast, no network, no database
│   │       └── integration/      Real PostgreSQL in a container
│   │
│   └── web/                      READER-FACING SITE (PERN)
│       ├── Dockerfile
│       ├── package.json
│       ├── src/
│       │   ├── config/           Validated settings
│       │   ├── db/               Read-only access for the web role
│       │   ├── routes/           HTTP endpoints, including /health
│       │   ├── observability/    Structured logging
│       │   └── client/           (later) react front end
│       └── tests/
│           ├── unit/
│           └── integration/      Includes: web role cannot write to content
│
├── db/                           THE DURABLE CONTRACT
│   ├── migrations/               Versioned schema changes (the only way to change schema)
│   ├── roles/                    Role and permission definitions (owner, pipeline_rw, web_ro)
│   └── tests/                    Migration tests: fresh database, upgrade path, role permissions
│
├── infra/                        INFRASTRUCTURE AS CODE (Terraform)
│   ├── modules/                  Reusable pieces: network, compute, database, iam, observability
│   ├── envs/
│   │   ├── dev/                  Root configuration for dev
│   │   └── prod/                 Root configuration for prod (same modules)
│   └── bootstrap/                Remote state setup, GitHub OIDC trust
│
├── evals/                        (later) Reviewed example sets and evaluation runners
│
├── scripts/                      Small, named operational scripts (see rules below)
│
└── docs/
    ├── decisions/                ADRs: 0001-..., 0002-..., append-only
    ├── runbooks/                 One file per alert or known failure mode
    └── devlog/                   Dated entries: what was done, what failed, what changed
```

### Why `evals/` is top-level and not inside the pipeline

Evaluation data is reviewed by a human, and it may test the whole system rather than one service. It also gets its own CI job. Keeping it separate makes "what do we measure" easy to find. Revisit this if evals turn out to belong to a single service.

### Why there is no shared code folder

The two applications are connected **only** through the database contract. They do not share code. If both seem to need the same logic, the logic probably belongs behind the database or in one service. Do not create a shared package without an ADR.

---

## 3. What belongs where

| If you are changing... | It lives in... | The pipeline must validate it with... |
|---|---|---|
| Fetching, research, editorial, quality logic | `services/pipeline/` | Python lint, types, unit and integration tests |
| What readers see or the web API | `services/web/` | JS lint, unit and integration tests |
| A table, column, constraint, or permission | `db/migrations/`, `db/roles/` | Migration test on a fresh database; role permission tests |
| A cloud resource | `infra/` | `terraform fmt`, `validate`, reviewed `plan` |
| How code is built, tested, or deployed | `.github/workflows/` | The workflow itself, tested on a branch |
| An AI quality measurement | `evals/` | Evaluation run in CI |
| A decision, a failure, or an alert response | `docs/` | Review: required by the definition of done |

---

## 4. Rules for keeping the structure healthy

**No dumping grounds.** Do not create `utils/`, `common/`, `helpers/`, `misc/`, or `shared/`. Name modules after what they do (`retry.py`, `hashing.py`, `url_canonicalization.py`) and place them in the component that uses them. If code is truly needed by two components inside one service, create a specifically named module in that service.

**One responsibility per folder.** If you cannot describe a folder in one sentence, split it or rename it.

**Tests live next to the thing they test.** Each service has its own `tests/`. Database tests are in `db/tests/`. Infrastructure is validated through plans, not by mocking.

**Scripts are small and named.** `scripts/` holds short operational helpers (for example `scripts/restore-check.sh`). Anything with real logic belongs in a service and gets tests. Every script starts with a comment stating what it does and when to run it.

**Do not create empty future folders.** Add `research/`, `quality/`, `evals/`, and others when the task that needs them starts. Add a short note to `Architecture.md` when you do.

**Security by structure.**

- `.gitignore` covers: `.env`, Terraform state and plan files, virtual environments, `node_modules`, build output, local database data, editor files.
- Never commit: real secrets, cloud credentials, state files, production data, or raw downloaded sources beyond small, reviewed test fixtures.
- Test fixtures that come from real sources must be small, labeled as such, and respect source terms. Synthetic fixtures are labeled synthetic.
- Secret scanning runs in pre-commit and in CI.

**Naming.** Folders and files use lowercase with hyphens or underscores as the language convention requires (`snake_case` for Python packages, `kebab-case` for scripts and docs, per `Conventions.md`). ADRs are numbered: `0001-repo-layout.md`.

---

## 5. Getting started

Work happens through tasks, in order. The first real step is `T-0.1` in `Tasks.md`.

1. Read `Vision.md`, then `Architecture.md`.
2. Check `Prerequisites.md` (Section C) and confirm your tools.
3. Open `Tasks.md` and take the first task whose dependencies are done.
4. Follow `Conventions.md`, including the definition of done.

Coding agents: start at `AGENTS.md`.
