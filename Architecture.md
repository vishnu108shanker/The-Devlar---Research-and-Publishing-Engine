# Architecture.md

**Audience:** the builder and coding agents.
**Last updated:** 2026-10-18
**Rule of this document:** it describes what is decided and what is not. Every decision is labeled:

- **Accepted**: agreed; build on it. Change only through an ADR.
- **Proposed**: the current best idea; may change when Stage 0 work gives evidence.
- **Deferred**: intentionally undecided; do not design or build it yet.

Do not describe unbuilt components as if they exist. Do not fill in Deferred areas on your own.

---

## 1. Purpose and constraints

The Devlar investigates technology developments, traces claims to evidence, and publishes explanatory articles only when they pass a quality gate. See `Vision.md`.

Constraints taken from the Vision (**Accepted**):

- Evidence limits what an article may claim. Publication is a decision made by a quality gate, not a by-product of generation finishing.
- The system is two independent applications: a **production side** (research and article lifecycle) and a **reader-facing website**, connected through **PostgreSQL** as a durable contract.
- The production side owns the research and article lifecycle. The website has **read-only** access to article content.
- The research engine is written in Python. The website is a PERN stack (PostgreSQL, Express, React, Node).
- Complexity must earn its place (Vision Section 15). No dedicated graph database, no Kubernetes, no public launch in early stages.

---

## 2. Components

| Component | Responsibility | Status |
|---|---|---|
| **Collectors** | Find candidate developments from official announcements, release notes, blogs, papers, repos. Fetch and store raw sources. | Stage 0: a single fixed-URL fetcher (**Accepted** as skeleton). Real discovery logic: **Deferred**. |
| **Research engine** | Plan questions, gather evidence, extract claims, iterate within limits. | **Deferred.** Design begins at Phase 1 (Milestone 1). |
| **Editorial synthesis** | Turn accepted findings into an article. | **Deferred.** |
| **Quality gate** | Decide publish, revise, research more, or reject. Claim and citation checks. | **Deferred** (Milestone 4). Interface to the database is **Proposed** (see Section 4). |
| **Publisher** | Move a passed article into the published content area. | **Deferred.** |
| **Reader website** | Serve published articles; later, inline explanation and handoff. | Stage 0: a minimal read-only page (**Proposed**). Real site: **Deferred** (Milestone 5). |
| **PostgreSQL (with pgvector later)** | Durable contract and system of record. | **Accepted** as the contract. pgvector use: **Deferred** to Milestone 2. |

---

## 3. System context (target shape, high level)

```
 External sources                Production side                         Reader side
 (announcements,   --fetch-->  Collectors -> Research -> Editorial ->     Website (PERN)
  docs, papers)                    |            |          |   Quality        ^
                                   v            v          v     gate         | read-only
                              +-------------------------------------+        |
                              |   PostgreSQL (the durable contract) |--------+
                              +-------------------------------------+
                                   ^
                                   | LLM provider (external)
```

This diagram is the **direction**, not a design. Only the Collectors, PostgreSQL, and a minimal website exist in Stage 0.

---

## 4. Data contract

**Accepted principle:** PostgreSQL is the boundary between production and website. Shared storage is never an excuse for arbitrary cross-component writes.

**Proposed** organization:

- Schemas: `pipeline` (internal research and run state), `content` (published articles, read-only for the web), `web` (user-specific features owned by the website).
- Roles: `devlar_owner` (migrations only), `pipeline_rw`, `web_ro` (read-only on `content`), and a web-owned role for the `web` schema.
- Migrations are the only way schema changes, in one place (`db/migrations/`), owned by the production side.

**Proposed** Stage 0 tables (minimal; extend through migrations):

- `sources`: one row per fetched source. Stable `source_id` derived from canonical URL and content hash; raw content or a pointer; fetch metadata; unique constraint for idempotency.
- `runs`: one row per pipeline run. `run_id`, idempotency key, status, start/end, cost fields.
- `stage_runs`: one row per stage within a run: stage name, status, attempts, duration, failure reason.

**Deferred:** claim, evidence, article, entity, and relationship tables. These are designed at the milestone that needs them, from real examples.

---

## 5. Data flow

**Stage 0 flow (Proposed):**

1. A scheduled or manual trigger starts a run for one fixed URL.
2. The fetcher retrieves the page (with timeout and size limit) and writes a `sources` row idempotently.
3. A stub stage writes a `runs` and `stage_runs` record with status and cost fields (zero cost for the stub).
4. The website reads the record through the read-only role and displays it.
5. Logs from each step are structured and include `run_id` and `stage`.

**Target flow:** **Deferred.** It will be written when Milestone 1 research design begins.

---

## 6. External dependencies

| Dependency | Use | Status |
|---|---|---|
| AWS | Compute, database, secrets, logging, alerts | **Accepted** as the cloud. Specific services: see Section 7. |
| GitHub + GitHub Actions | Source control, CI/CD | **Accepted** |
| LLM provider | Research and explanation | **Deferred** to Phase 1. Keep any wrapper thin so the provider can change. |
| Embedding model / pgvector | Retrieval | **Deferred** to Milestone 2. |
| Source websites | Evidence | Treat as untrusted input at all times. |

---

## 7. Deployment shape

**Proposed:**

- Two AWS environments from the start: `dev` and `prod`, created from the **same** infrastructure code.
- Compute: a small virtual server (EC2) running the services as Docker containers, managed with Docker Compose.
- Database: PostgreSQL. Whether it runs as a managed service (RDS) or as a container on the server with volume snapshots is an **open decision for Stage 0** (ADR needed). The choice must support pgvector later and a tested restore process.
- Infrastructure as code: Terraform. Remote state with locking.
- CI/CD: GitHub Actions. CI builds, tests, scans images. CD deploys to `dev`, then promotes to `prod` with a manual approval. CI authenticates to AWS using OIDC.
- Secrets: AWS SSM Parameter Store. No `.env` in deployed environments.
- Observability: structured JSON logs shipped to CloudWatch; a small set of metrics; at least one alert routed to a real notification channel and verified by a deliberate test failure.
- Cost guardrails: AWS budget alert from day one; LLM spending cap enforced in code from the first LLM call.

**Deferred:** ECS/Fargate, Kubernetes, load balancers beyond what is needed, CDN, multi-region, autoscaling, a managed queue, Kafka, Redis. Each needs a real requirement or a scoped learning experiment first.

---

## 8. Environments

| Environment | Purpose | Notes |
|---|---|---|
| `local` | Editing and running tests | Uses Docker for PostgreSQL. Work is not "done" until deployed to `dev` by the pipeline. |
| `dev` | Integration and verification | Safe to destroy and recreate. Real AWS. |
| `prod` | The live system | Changes arrive only through the pipeline, with approval. |

---

## 9. Security boundaries (**Accepted principles**, details Proposed)

- Least-privilege identities per component; no shared admin credentials.
- The database is not publicly reachable.
- Fetched content is untrusted and may contain hostile instructions. It is data, never instructions.
- The website cannot write to article content.
- Secrets never appear in code, images, logs, or Git history.

---

## 10. Decision register

| ID | Decision | Status | Where it gets settled |
|---|---|---|---|
| D-01 | PostgreSQL as durable contract between production side and website | Accepted | Vision Section 9.4 |
| D-02 | Python research engine; PERN website | Accepted | Vision Section 20 |
| D-03 | Walking skeleton deployed to AWS before real logic | Accepted | Roadmap Phase 0 |
| D-04 | Separate `dev` and `prod` from the start | Accepted | Roadmap Phase 0 |
| D-05 | Infrastructure as code from first commit | Accepted | Roadmap Phase 0 |
| D-06 | GitHub Actions as quality and deployment gate | Accepted | Roadmap Phase 0 |
| D-07 | Monorepo layout | Proposed | ADR-0001 |
| D-08 | EC2 + Docker Compose as initial compute | Proposed | ADR-0002 |
| D-09 | Database hosting: RDS vs container on EC2 | **Open** | ADR-0003 |
| D-10 | Terraform as IaC tool | Proposed | ADR-0004 |
| D-11 | Migration tool | Open | ADR-0005 |
| D-12 | SSM Parameter Store for secrets | Proposed | ADR-0006 |
| D-13 | LLM provider and interface | Deferred | Phase 1 |
| D-14 | Research engine design (agents, iteration, orchestration) | Deferred | Phase 1 and 3 |
| D-15 | Knowledge layer, retrieval strategy, pgvector | Deferred | Phase 2 |
| D-16 | Quality gate design | Deferred | Phase 4 |
| D-17 | Redis, Kafka, Kubernetes, graph database | Deferred | Only with a justified requirement |

---

## 11. Open questions

- Database hosting (D-09): managed convenience and backups vs. cost and learning value of operating it yourself.
- How will runs be triggered in Stage 0: manual command, scheduler on the host, or a scheduled workflow?
- Language for the web service: JavaScript or TypeScript?
- Alert channel: email via SNS, or another channel the builder will actually see?

Update this document as these are answered.
