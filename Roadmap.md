# Roadmap.md

**Audience:** primarily the builder (Vishnu).
**Last updated:** 2026-10-18
**Nature of this document:** a phased plan for *when* and *why* to introduce each engineering practice. It is **not** a promise that every technology will be used, and it has **no deadlines**. Progress is measured by evidence, not by dates (Vision Section 16).

**In plain words:** build a tiny working system and put it online first. Then grow it one capability at a time. Each phase teaches specific skills and ends with proof that you learned them.

---

## How to read this roadmap

Each phase lists:

- **Objective:** what the system can do at the end.
- **Learning goals:** what you should be able to explain and do.
- **Practices introduced, and why now.**
- **Evidence of completion:** what must exist before the phase is closed.
- **Cost considerations:** what can cost money, and the guardrail.
- **Decision points:** choices to settle with a short ADR, using evidence.

Phase 0 is new work that sits **before** Vision Milestone 1. It adds the deployment and operations foundation your "production-grade from day one" goal requires. Phases 1 to 5 map to Vision Milestones 1 to 5. If the order needs to change as you learn, change it, and record why.

---

## Phase 0: Foundation and walking skeleton

**Objective:** a trivial end-to-end slice, deployed to AWS (`dev` and `prod`) through an automated pipeline, with logging, a tested alert, safe database practices, and a restore test.

**Learning goals**
- Provision cloud infrastructure from code and recreate it from scratch.
- Build, scan, and ship Docker images through CI/CD with short-lived credentials.
- Design a small database with migrations, roles, and idempotent writes.
- Operate what you built: read logs, trigger an alert, restore a backup.

**Practices introduced, and why now**

| Practice | Why it belongs here |
|---|---|
| Git workflow, branch protection, pre-commit | Cheapest to set up before there is code to protect. |
| Docker + Compose | Every later service needs a repeatable runtime. |
| AWS account safety (MFA, budget alarm, no root use) | Cost and security mistakes are most likely at the beginning. |
| Terraform with remote state | Rebuilding from code is the main skill. Console clicks leave no record. |
| `dev` and `prod` environments | Teaches promotion and isolation before there is anything to lose. |
| GitHub Actions CI/CD with OIDC | Stops "works on my machine." No stored cloud keys. |
| Database migrations and roles | Schema mistakes are hardest to fix later. |
| Secrets management | No habit of `.env` in production is ever formed. |
| Structured logs, run and stage IDs, one alert | You cannot debug or trust what you cannot see. |
| Backup and restore test | A backup that was never restored is a hope. |

**Evidence of completion**
- A push to `main` runs CI, deploys to `dev`, and (after approval) to `prod`, with no manual steps.
- Destroying and recreating `dev` from code succeeds. Time and problems recorded.
- A deliberately broken run produces a log trail with `run_id` and fires an alert you actually received.
- A database backup was restored into a fresh instance and checked.
- A repeated run does not create duplicate rows.
- ADRs and runbooks exist for each decision and alert.

**Cost considerations**
- Main costs: compute for two environments, database, logs, data transfer. Check current AWS pricing before choosing sizes; record the estimate and actual monthly bill in the devlog.
- Guardrails: AWS budget alert before any resource is created; stop or destroy `dev` when not in use if it saves money; use the smallest instance sizes that work.

**Decision points**
- Database hosting: RDS vs container on EC2 (ADR-0003).
- Terraform vs another IaC tool (ADR-0004).
- Migration tool (ADR-0005).
- Run trigger: manual, scheduled on host, or scheduled workflow.
- Alert channel.

---

## Phase 1: Traceable article (Vision Milestone 1)

**Objective:** take one real announcement and produce an article where every important claim traces to a source passage, compared against a hand-labeled claim set and a recorded simple baseline.

**Learning goals**
- Write evaluation datasets and run them like tests.
- Call LLMs reliably: structured output, validation, timeouts, retries, cost tracking.
- Model claims, evidence, and source passages in a database.
- Understand why fluent text is not proof.

**Practices introduced, and why now**
- **Testing in depth** (unit, integration with real PostgreSQL, failure paths): real logic now exists to test.
- **Evaluation sets and regression checks in CI:** AI quality must be measurable from the first real output.
- **LLM cost and latency tracking, spend cap:** the first paid API call is the first chance to overspend.
- **Prompt versioning:** prompts are code and need history.

**Evidence of completion**
- One article from one announcement, with each important claim linked to a source passage.
- A hand-labeled claim set for that case.
- A baseline from the simplest possible approach (for example a single prompt), with scores recorded.
- Evals run in CI; a deliberate regression is caught.

**Cost considerations:** LLM tokens are the main cost. Cap per-run and total spend in code. Prefer a small set of reviewed examples over many unreviewed runs.

**Decision points:** LLM provider and interface; claim and evidence schema; how to score "claim supported by source."

---

## Phase 2: Knowledge layer (Vision Milestone 2)

**Objective:** persistent source storage with keyword and vector retrieval, measured against reviewed examples, plus extracted entities and relationships that keep provenance.

**Learning goals**
- Full-text and vector search in PostgreSQL (pgvector).
- Chunking, embeddings, and how to measure retrieval quality.
- Entities and relationships with source and time context.
- Honest comparison: does the knowledge layer help, or just add complexity?

**Practices introduced, and why now**
- **pgvector and indexing:** retrieval needs a stored corpus, which now exists.
- **Retrieval evaluation:** measure before claiming improvement.
- **Schema evolution via migrations on real data:** practice changing a live schema safely.

**Evidence of completion:** retrieval results scored on the reviewed set for keyword, vector, and combined approaches; a written comparison; entities and relationships with provenance stored and queryable.

**Cost considerations:** embedding calls cost tokens; database storage and index size grow. Watch instance memory and disk.

**Decision points:** embedding model; chunking strategy; whether to add relationships beyond a basic set. Per Vision Section 7, do not compare graph vs plain retrieval until there is enough material.

---

## Phase 3: Iterative research (Vision Milestone 3)

**Objective:** a resumable research workflow with bounded iteration, compared to the single-pass baseline.

**Learning goals**
- Workflow orchestration, checkpoints, and resuming after failure.
- Bounded loops: budgets, retry limits, stopping conditions.
- Separating roles (planner, investigator, reviewer) only where evaluation shows a need.

**Practices introduced, and why now**
- **Checkpointed, resumable stages:** research is expensive; losing work is unacceptable.
- **A job-queue or orchestration decision:** introduce only if a real problem appears (for example work that must survive restarts or run in parallel). A database-backed queue may be enough; Redis or a framework must justify itself with evidence.
- **Agent frameworks:** evaluate against a hand-written workflow on the same cases.

**Evidence of completion:** same cases run through single-pass and iterative workflows with recorded results on what each added stage did and did not improve; a forced mid-run crash resumes without duplicating work.

**Cost considerations:** iteration multiplies LLM cost. Enforce per-run budgets and stop conditions.

**Decision points:** orchestration approach (own code vs framework); whether Redis or a queue is justified; number of roles.

---

## Phase 4: Reliability and quality gate (Vision Milestone 4)

**Objective:** claim-level checks, citation validation, budgets, retry limits, and structured run logs. The system survives crashes, broken sources, and contradictory evidence without publishing partial or unsupported output.

**Learning goals**
- Failure injection and recovery testing.
- Designing a publish/revise/reject gate and measuring it.
- Monitoring that tells you what is wrong, not only that something is.
- Security hardening and threat thinking for a system that reads hostile web content.

**Practices introduced, and why now**
- **Chaos-style tests** (kill workers, break sources, feed contradictions): there is finally something worth breaking.
- **Dashboards and meaningful alerts:** enough run history exists to define "normal."
- **Security review:** prompt-injection from sources, SSRF in fetchers, IAM audit, dependency and image scanning thresholds.
- **Quality-gate evaluation:** check the gate (and any LLM judge) against human-reviewed cases.

**Evidence of completion:** documented forced-failure tests with results; a gate that rejects known-bad candidates; a security review with findings and fixes recorded; runbooks for each alert.

**Cost considerations:** monitoring and log volume grow; set retention policies. Review the monthly bill against the plan.

**Decision points:** gate thresholds; which failures block versus warn; log retention and alert routing.

---

## Phase 5: Reader-facing journal (Vision Milestone 5)

**Objective:** discovery, article storage, the website with inline explanation and conversational handoff, and publication gated by the quality gate.

**Learning goals**
- A PERN service with strict read-only access to published content.
- Streaming responses, with all model access mediated by the backend.
- Operating a public-facing service: TLS, rate limiting, abuse control, uptime.

**Practices introduced, and why now**
- **Public-facing hardening:** only now is there something to expose.
- **Rate limiting and caching** for the explain feature; **DNS and TLS** for a real domain.
- **Reuse of the existing browser-extension code** as in Vision Section 11, behind the site's backend.

**Evidence of completion:** articles appear on the site only after passing the gate; the site cannot write article content (verified by test); explain feature works with no secret key in the browser; rate limiting verified.

**Cost considerations:** public traffic and LLM calls from readers can spike costs. Set per-user and global limits before any public launch.

**Decision points:** whether to launch publicly at all (a non-goal until earlier phases are met); caching approach; load balancer or CDN only if traffic demands.

---

## Phase 6: Optional experiments (not committed)

Pursue only if a real problem appears or you deliberately want the learning. Each must be written up as a scoped experiment with a question, a success measure, and a stop condition.

| Experiment | Question it answers | Trigger |
|---|---|---|
| Managed container service (ECS/Fargate) | Is operating the server by hand now the bottleneck? | Deployment pain or scaling need |
| Redis or a message broker | Does the pipeline need durable async work beyond the database? | Evidence from Phase 3 |
| Kafka | Is there an event-streaming need that a queue cannot meet? | Clear streaming requirement, otherwise learning-only |
| Kubernetes | What does orchestration teach, and does anything need it? | Learning goal, clearly labeled |
| Graph database or full temporal knowledge graph | Does a graph beat relational retrieval on reviewed cases? | Enough corpus and measured need |
| Personal learning paths, monetization, accounts at scale | Vision non-goals | Only after earlier phases are met |

---

## When each technology is introduced (summary)

| Technology / practice | Phase | Status |
|---|---|---|
| Git workflow, pre-commit, branch protection | 0 | Committed |
| Docker, Docker Compose | 0 | Committed |
| AWS (EC2 or equivalent, IAM, SSM, CloudWatch, budgets) | 0 | Committed |
| Terraform | 0 | Proposed |
| GitHub Actions CI/CD with OIDC | 0 | Committed |
| PostgreSQL, migrations, roles | 0 | Committed |
| Structured logging, alert, runbooks | 0 | Committed |
| Backup and restore testing | 0 | Committed |
| Evals in CI, LLM cost tracking | 1 | Committed |
| pgvector, retrieval evaluation | 2 | Committed |
| Workflow orchestration, checkpoints | 3 | Committed; framework Deferred |
| Failure injection, dashboards, security review | 4 | Committed |
| Public hardening, rate limiting, TLS, caching | 5 | Committed |
| Redis, Kafka, Kubernetes, graph DB, ECS | 6 | Optional, evidence-driven |

---

## Phase review ritual

At the end of each phase:

1. Check the evidence list. Anything missing keeps the phase open.
2. Write a devlog entry: what worked, what failed, what you would change.
3. Update `Architecture.md` statuses and `Tasks.md`.
4. Record the actual cost against the estimate.
5. Revisit this roadmap and adjust the next phase based on what you learned.
