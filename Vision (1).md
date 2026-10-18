# THE DEVLAR: Vision

> **A technology research and learning platform built to turn the noise of technological change into understanding.**

**Document type:** Foundational vision
**Status:** Revised. Meant to evolve through deliberate reflection.
**Project:** THE DEVLAR

---

## The Vision on One Page

**What it is.** A news-driven platform that investigates important technology developments, grounds its explanations in evidence, connects them to existing knowledge, and teaches them in plain, precise language.

**The four verbs.**
- **Discover** what matters.
- **Investigate** what is true.
- **Connect** what belongs together.
- **Teach** what is worth understanding.

**Three commitments.**
1. Research comes before explanation, and evidence limits what an article may claim.
2. Learning comes first and the product second. There is no deadline; the project takes as long as the learning needs.
3. Complexity must earn its place, either by solving a real problem or by serving a deliberate learning goal.

**The decision filter.** Before adding anything, ask the ten questions in Section 15.

**The test of success.** Feed it a recent announcement, inspect how it was researched, trace the important claims to source passages, and receive an article that is published only because it passed its quality gate.

---

## 1. The Founding Idea

Technology does not stand still long enough for anyone to understand it once and be finished. Models are announced, frameworks change, tools are released and deprecated, research is published. A single announcement can hold several layers of meaning: what happened, how it works, what it depends on, why it matters, and what remains uncertain.

The information is available, but understanding is not automatic. A headline says that something happened. An announcement says what its creator wants us to know. A summary compresses the announcement. None of these necessarily helps a reader build a reliable mental model.

**The Devlar exists to close the gap between being informed and understanding.**

It starts from current developments, investigates the evidence behind them, connects them to relevant ideas and earlier developments, and turns the investigation into an explanation that helps a person learn. It is not a stream of content produced because content is easy to produce. Research precedes explanation, evidence constrains claims, and explanation serves understanding.

Its central question is not only *"What happened in technology today?"* but also *"What does this development actually mean, how do we know, and what should a curious person understand because of it?"*

---

## 2. Why It Should Exist

### 2.1 The problem is not a shortage of information

There is an abundance of announcements, documentation, papers, release notes, opinions, and commentary. The reader is left to assemble the fragments alone. One source explains the feature but not the concept. Another has depth but assumes too much. A third is confident but does not separate fact from speculation.

Information has become easy to obtain, while establishing context, checking claims, and forming a coherent understanding has stayed difficult. The Devlar should help with that work. It does not replace curiosity, judgment, or further reading; it makes the path from curiosity to informed understanding more direct, transparent, and useful.

### 2.2 News is the entry point, not the end product

News gives the Devlar its starting point and its sense of relevance. But a story is not valuable merely because it is recent. A good article helps the reader understand the development and, where relevant, the technical ideas beneath it.

Depth should follow the story. A small release does not need to become a textbook chapter, and a consequential announcement should not be reduced to generic paragraphs to publish quickly.

**News provides the question. Research establishes what can be said. Explanation turns the findings into learning.**

### 2.3 What the reader should leave with

A useful article helps the reader answer some combination of these:
- What happened, and who announced it? What is the primary source?
- What is actually new?
- How does the relevant technology work, and what should be understood first?
- What evidence supports the important claims?
- What are the limits, uncertainties, trade-offs, and open questions?
- Why might it matter beyond today's headline?
- Where can the reader investigate further?

Not every article answers every question. Each gets the depth its subject warrants, not a fixed formula.

---

## 3. What The Devlar Is

The Devlar is an **autonomous technology research and learning platform** whose reader-facing output is a stream of researched, explanatory articles. It is three things at once:

- **A product** that helps people discover significant developments and understand them through evidence-backed explanations.
- **An engineering inquiry** into how software can discover information, retrieve context, examine claims, challenge its own conclusions, preserve relationships between ideas, and produce explanations under explicit quality constraints.
- **A learning project** that gives its builder a real system with real failure modes for studying AI research systems, retrieval, knowledge representation, workflow orchestration, data integrity, reliability, and deployment.

These reinforce one another. The learning ambition should raise the product's quality, and the product's needs should give the learning a concrete purpose.

### What it is not

- A news aggregator that republishes headlines.
- A generic AI summarizer that compresses whatever page it receives.
- A static wiki of timeless definitions.
- A knowledge graph built to display connected nodes.
- A collection of agents whose activity is mistaken for research quality.
- A content factory that values volume over correctness.
- A wrapper around an LLM that treats fluent language as evidence of understanding.

It may use summaries, reference material, graphs, multiple AI roles, and familiar web interfaces. Those are means, not the identity of the project.

---

## 4. Discover, Investigate, Connect, Teach

### 4.1 Discover

Discovery starts from official announcements, release notes, engineering blogs, papers, advisories, and repositories. It is a selection problem, not a collection problem: the system should tell a meaningful development from duplicate coverage, routine noise, and recycled claims. The aim is not to capture everything but to find developments worth understanding.

### 4.2 Investigate

An announcement is a starting source, not a guarantee that every claim in it is complete, independently verified, or free of promotional framing. Research should look for primary evidence, technical documentation, historical context, and credible independent material, and should identify what a source directly establishes, what it merely asserts, what can be corroborated, and what is unknown.

Investigation may take more than one pass. Initial findings can reveal gaps, conflicts, or ambiguous terms that change the interpretation, and a capable system should recognize them and continue within defined limits.

### 4.3 Connect

A development rarely exists in isolation. It may depend on a protocol, extend an earlier model, compete with an established approach, or change the significance of an existing tool. The Devlar should preserve useful relationships between entities, claims, concepts, products, organizations, papers, and events.

A connection is not asserted simply because two entities appear in the same article. Its meaning, provenance, and time context matter.

### 4.4 Teach

Teaching takes what the research supports and explains it so a reader can build a mental model. The goal is to make complexity navigable, not to make every subject sound simple. A good explanation introduces prerequisites when needed, uses examples that clarify a mechanism, defines terms at the right moment, and distinguishes a useful analogy from the literal behavior of a system.

---

## 5. Truth and Evidence

The Devlar's credibility must come from how it handles evidence, not from how confident its writing sounds.

### 5.1 Fluency is not proof

Language models can produce coherent explanations with unsupported claims, wrong details, misleading analogies, or invented references. A multi-step workflow can repeat those errors at greater length. The Devlar must not treat eloquence, model confidence, repetition, or agreement between agents as evidence of correctness.

### 5.2 Claims should be traceable

Important factual claims should trace to source material, and a reviewer should be able to check that the evidence supports the exact claim made. The system preserves the links between:
- the source and the relevant passage,
- the evidence extracted from it,
- the claim that evidence supports or challenges,
- the article passage where the claim appears,
- the research run and the decisions that led to publication.

A citation must do more than exist. It must be relevant, reachable where possible, and genuinely supportive.

### 5.3 Sources have different roles

An official announcement is often the best source for what an organization says it launched. It is not automatically independent evidence that its performance claims, comparisons, or forecasts are true. Documentation shows intended behavior. A paper supports a result under particular conditions. A repository shows implementation but not necessarily real-world performance. Sources are judged against the question being asked, not through one fixed hierarchy.

### 5.4 Uncertainty is part of an honest explanation

Where relevant, the system distinguishes:
- verified or directly documented facts,
- claims made by a source,
- independently corroborated findings,
- reasonable interpretations and inferences,
- predictions and opinions,
- unresolved questions and missing evidence.

Uncertainty is proportionate. The goal is neither uncritical acceptance nor reflexive skepticism, but to say what the evidence supports, no more and no less.

### 5.5 Publication is a decision

A candidate does not become an article just because generation finished. Publication depends on defined criteria: source integrity, claim support, citation validity, relevance, sufficient context, unresolved contradictions, and editorial completeness. Some candidates need more research, some need revision, and some should be rejected. No automated gate can guarantee truth; its job is to catch known classes of failure, make decisions consistent, and give a basis for improvement.

**The Devlar should prefer an honest limitation to a confident invention.**

---

## 6. Explanation

### 6.1 Explain the mechanism, not just the vocabulary

A definition is often only the first step. Readers may also need to know what a concept does, why it exists, how its parts interact, and where it breaks down. Move from labels to mechanisms whenever the subject warrants it.

### 6.2 Simplicity is a form of precision

Use plain language where it works, and avoid jargon that only performs expertise. But simplicity must not erase distinctions that matter. If two technologies behave differently, say so. If an analogy breaks down in a way that affects understanding, say so. The goal is the least unnecessary difficulty between the reader and the idea.

### 6.3 Respect different levels of prior knowledge

A beginner should not meet a wall at every unfamiliar term, and an experienced reader should find mechanism, trade-offs, and evidence without wading through basics. This is served by explaining concepts in context, linking to deeper material, and offering explanations at different levels directly in the reader's flow (see Section 11), not by forcing every article into rigid layers.

### 6.4 Context should serve the current story

Ask: *what does a reader need to understand this story accurately, and what additional context would materially deepen that understanding?* Everything else is shortened, linked, or omitted.

### 6.5 Preserve the reader's agency

An article does not demand agreement with its interpretation. It gives readers enough context and evidence to reason for themselves, makes meaningful alternatives and trade-offs visible, and offers further reading that leads somewhere.

---

## 7. Knowledge: A Living Map, Not a Warehouse

A document store preserves what a source said. Retrieval brings relevant passages into a task. A knowledge graph represents relationships among technologies, organizations, models, concepts, claims, and events. These answer different questions and should complement one another only where each helps.

- **Relationships need meaning and provenance.** "Uses," "replaces," "depends on," "competes with," and "announced by" are different relations and should not collapse into a generic edge. Relationships carry sources, dates, and qualification where appropriate. A technology that was current once is not silently presented as current forever.
- **Knowledge must be revisable.** Products are renamed, APIs deprecated, benchmarks superseded, plans changed. The system should preserve what was known, what source supported it, and what later changed the picture, so that updates do not erase the context needed to understand an earlier article.
- **Connections should create explanatory value.** A graph earns its place by improving retrieval, revealing context, supporting comparison, or identifying prerequisites. Its existence alone proves nothing. Its measure is what it helps the system retrieve, reason about, explain, and update.
- **Scale honestly.** A graph built from a handful of articles cannot be fairly compared with plain retrieval. The knowledge layer grows with the corpus, and comparisons between retrieval approaches wait until there is enough material to make them meaningful.

---

## 8. AI Research

Multiple research roles, iteration, retrieval, structured outputs, and orchestration are tools for improving the process, not ends in themselves.

### 8.1 Agents should have responsibilities

A planner defines questions and evidence requirements. An investigator gathers sources and extracts findings. A knowledge researcher retrieves historical context. An adversarial reviewer looks for unsupported claims and contradictions. An editorial synthesizer turns accepted findings into an article. These roles are useful only when their inputs, outputs, and evaluation criteria are clear. Adding agents does not by itself make a better researcher; each handoff adds latency, cost, and a place for errors. Start with the smallest set of roles that works and add one only when evaluation shows a specific failure it would fix.

### 8.2 Iterate when iteration adds value

A straightforward release note may need one pass. A consequential or ambiguous development may need more. The system should ask whether the evidence answers the planned questions, whether important claims are supported, whether contradictions remain, and whether another pass is likely to help. Iteration needs stopping conditions, budgets, retry limits, and explicit handling of unresolved gaps. Endless investigation is not rigor, and neither is premature completion.

### 8.3 Challenge conclusions, not merely wording

Adversarial review looks for substantive weaknesses: a source that does not support its claim, an alternative explanation, a missing prerequisite, a comparison without comparable conditions, a stale fact, a conclusion beyond the evidence. A reviewer that only rewrites sentences more cautiously is not doing the job.

### 8.4 Measure methods, not frameworks

Compare approaches on a fixed, reviewed set of examples and record the trade-offs in quality, cost, latency, maintainability, and failure recovery. A single well-structured workflow may beat a multi-agent one on simple questions; iteration may pay off when evidence is fragmented; graph retrieval may help some questions and add noise to others. Adopt a tool because it demonstrably helps or serves a deliberate learning objective, not because it is fashionable.

---

## 9. Engineering

The Devlar continues the engineering direction set in DevByte Engine: modular responsibilities, idempotent operations, explicit boundaries, recoverable workflows, and the willingness to understand infrastructure instead of hiding behind it.

### 9.1 Modularity means meaningful independence

A component has a clear responsibility and a defined contract, and does not need to know the internals of the others. Boundaries should reduce the impact of change, not add indirection. A logical stage, a process, and a container are different kinds of boundary, and each is chosen deliberately.

### 9.2 Idempotency protects work

Research is expensive. A worker may crash after finishing, a write may succeed while the caller times out, a workflow may retry after an uncertain result. Repeating an operation must not create duplicate stories, duplicate publications, or inconsistent state. Stable identities, safe writes, explicit transitions, and designed retry behavior are core concerns.

### 9.3 Reliability is more than a successful run

A pipeline that succeeds once is a demonstration. A system explains its failures, retries safely, resumes from checkpoints, avoids duplicate effects, and makes its state observable: stage status, duration, retries, source failures, model usage, quality-gate decisions, and reasons for rejection or delay. The goal is not to eliminate failure but to make it bounded, understandable, and recoverable.

### 9.4 Data contracts matter

The production pipeline and the reader-facing website are independent applications connected through PostgreSQL as a durable contract. The production side owns the research and article lifecycle. The website serves published content and manages user-specific features, and has read-only access to article content. Shared storage must never become an excuse for arbitrary cross-component writes. Exact schemas, job coordination, container boundaries, and messaging choices remain engineering decisions to research and test.

### 9.5 Infrastructure is learned through real requirements

Docker, PostgreSQL, Redis, Kafka, cloud deployment, observability, and Kubernetes each teach important ideas, but none is added just to make an architecture diagram look advanced. Understand the problem first, then introduce infrastructure when it solves that problem or enables a deliberate experiment.

---

## 10. The Relationship to DevByte Engine

The Devlar grows from the experience and broader ambitions of DevByte Engine without erasing them. DevByte explores automated content production and distribution; the Devlar focuses on discovery, evidence-based investigation, knowledge relationships, and explanatory articles. They can be separate codebases and products while sharing a philosophy: modularity, idempotency, reliable pipelines, observability, and disciplined deployment. Integration should rest on real contracts and useful shared capabilities, not forced coupling. In time, Devlar research may supply material for other formats, or the systems may share infrastructure; neither is a prerequisite for the first implementation.

**A separate codebase does not require a separate engineering philosophy.**

---

## 11. Explanation at the Point of Reading

Learning often begins at the exact moment a reader meets something they do not understand. The Devlar therefore builds a quick explanation feature directly into its website: a reader selects an unfamiliar term, invokes it with a keyboard shortcut, and gets an explanation at a chosen level of detail (naive, standard, or expert). The same feature can summarize a selected passage or a whole article.

This feature comes from our earlier browser extension, whose working code is reused rather than rewritten. It lives inside the site because that is where the articles are, and because publishing a browser extension is not required for the platform to work. The extension may continue to exist as a personal tool, but it is not part of the product's critical path.

The explain feature and the research platform serve different purposes:
- The explain feature gives immediate, local-context help, optimized for speed and streaming.
- The research platform investigates deeply, preserves evidence, builds context, and produces an editorially reviewed result.

The explain feature does not depend on the research pipeline, and its model access is always mediated by the site's own backend so that no secret key ever reaches the browser. When a reader wants to go further, the site offers a handoff to a general conversational assistant, with the article's context and sources prefilled, so the conversation can continue there.

---

## 12. The Reader Experience

The ideal experience begins with curiosity, not obligation. A reader arrives at a current development. The article makes clear what happened, separates the source's claims from the available evidence, and explains the concepts needed to follow the story. Sources are reachable, related ideas lead somewhere, and unknowns are not hidden behind confident prose.

The reader can go deeper without losing the thread: inspect sources, explore related concepts, ask for a simpler or more technical explanation, or hand the article's context to another tool. Over time the platform should leave readers less dependent on superficial summaries, with better mental models and better routes into primary material. Success is not time spent on the site. It is a clearer understanding, better questions, and a stronger ability to evaluate the next development.

---

## 13. Quality

Quality is multi-dimensional. A fluent article with broken citations is not high quality. A correct article the target reader cannot follow is incomplete. A strong result that vanishes after a worker crash is an engineering failure.

**Research quality:** the selected development is significant; the important questions are covered; sources are appropriate and varied; conflicting or incomplete evidence is handled correctly; source claims, evidence, and inference are kept distinct.

**Factual and citation quality:** important claims are supported by the cited evidence; citations resolve to the intended source and passage; dates, names, versions, and details are accurate; stale or contradicted information is detected; uncertainty is proportionate.

**Editorial and learning quality:** the article explains the development and not just a headline; mechanisms and prerequisites are clear; the level of detail fits the story; analogies clarify without misleading; limits and next steps are visible.

**Knowledge quality:** entities and relationships are meaningful, carry provenance and time context, and retrieval returns useful evidence rather than merely similar wording; the knowledge layer measurably helps investigation or explanation.

**Operational quality:** interrupted jobs recover safely; retries avoid duplicate side effects; errors and gate decisions are observable; cost, latency, and resource use are understood; changes can be checked against known examples without silent regression.

Automated metrics help, but they do not replace carefully reviewed examples and human judgment. Any model used as a judge must itself be checked against human-reviewed cases.

---

## 14. What The Devlar Should Refuse to Become

- **Publishing for volume.** More articles are not better if they are repetitive, shallow, or poorly supported.
- **Confusing speed with usefulness.** A short delay to resolve a material uncertainty can be worth it.
- **Treating generated text as research.** Writing is the end of an investigation, not a substitute for one.
- **Using complexity as decoration.** More agents, databases, services, or frameworks do not make a stronger system.
- **Hiding uncertainty.** Missing evidence must not be disguised as certainty to finish an article.
- **Letting sources dictate the narrative.** An organization's framing of its own announcement is not the platform's independent conclusion.
- **Letting automation remove accountability.** Enough provenance must remain to explain where a claim came from and why an article passed or failed.
- **Optimizing for a demo.** The system must survive ordinary operational reality, not just produce one impressive output.
- **Losing the learning objective.** Shipping matters, but this is also a sustained engineering education.

---

## 15. Principles for Future Decisions

When a feature, framework, architecture, or optimization is proposed, ask:

1. **Does it serve understanding?** Does it help readers understand a meaningful development or help the system produce a more reliable explanation?
2. **Does evidence constrain the result?** Can important claims be traced to support?
3. **Does it preserve intellectual honesty?** Can it represent uncertainty, contradiction, and missing information without inventing an answer?
4. **Does it improve meaningful context?** Does it connect ideas in ways that improve research or learning?
5. **Is the boundary clear?** Does the component have a coherent responsibility, contract, and ownership model?
6. **Can it fail safely?** Are retries, partial completion, persistence, and recovery understood?
7. **Can we evaluate its value?** Is there a test, reviewed example set, or observable outcome that shows whether it helps?
8. **Is the complexity justified?** Does it solve a real problem or serve a deliberate learning goal?
9. **Can the decision be revised?** Are alternatives and trade-offs documented so new evidence can change the choice?
10. **Does it fit the larger journey?** Does it build on the engineering principles and infrastructure learning from DevByte Engine?

These guide decisions without becoming a rigid checklist. Some ideas deserve a prototype precisely because their value is unknown.

---

## 16. The Builder's Philosophy: Learning First, Product Second

The Devlar is meant to be built, studied, questioned, and improved. It is not meant to be rushed into existence to claim completion.

**There is no deadline.** The project is not bound to a fixed timeline. The builder will invest as much time as the learning and development require, and no calendar will be allowed to cut a study phase, skip an experiment, or ship an unexamined design. Pace is set by understanding, not by a date.

The product provides the reason to learn, and the learning provides the depth to build the product well. That means researching competing approaches before choosing, running small experiments when trade-offs are unclear, documenting decisions, and revisiting assumptions when evidence changes.

The project should not avoid difficulty, but it should tell valuable difficulty from accidental complexity. Valuable difficulty teaches something important: durable workflow design, evidence provenance, entity resolution, retrieval evaluation, failure recovery, distributed behavior. Accidental complexity adds moving parts with no clear benefit or learning purpose.

A strong outcome is not a large codebase. It is a system whose builder can explain its boundaries, failure modes, design alternatives, evaluation methods, and reasons for existing.

### Progress is measured in milestones, not dates

Because there is no deadline, progress is marked by capabilities demonstrated, not time elapsed. Each milestone is complete only when its exit evidence exists.

**Milestone 1: Traceable article.** The system takes one real announcement and produces an article in which every important claim traces to a source passage, with a hand-labeled claim set to compare against and a recorded baseline from the simplest possible approach.

**Milestone 2: Knowledge layer.** Persistent source storage with keyword and vector retrieval, measured against the reviewed examples, plus extracted entities and relationships that retain provenance.

**Milestone 3: Iterative research.** A resumable research workflow with bounded iteration, compared against the single-pass baseline on the same cases, with recorded results on what each added stage did and did not improve.

**Milestone 4: Reliability and the quality gate.** Claim-level checks, citation validation, budgets, retry limits, and structured run logs; the system survives forced crashes, broken sources, and contradictory evidence without publishing partial or unsupported output.

**Milestone 5: The reader-facing journal.** Discovery, article storage, the website with inline explanation and the conversational handoff, and publication gated by the quality gate.

The order may change as understanding grows. A milestone may be split, reordered, or dropped when evidence shows it should be.

### Explicit non-goals for the first milestones

Until the earlier milestones are met, the project is not trying to deliver: a public launch, user accounts at scale, monetization, a dedicated graph database, a full temporal knowledge graph across many domains, personal learning paths, or deployment on container-orchestration infrastructure. These may become goals later; they are not allowed to pull attention from the core research loop now.

---

## 17. A Long-Term Direction

The Devlar may grow from an automated research and article platform into a richer environment for following ideas across time. Possible directions:
- more sophisticated discovery and significance ranking,
- research workflows that plan, investigate, challenge, and revise,
- search combining lexical, semantic, and graph retrieval,
- a temporal knowledge graph linking technologies, organizations, papers, products, events, and concepts,
- article histories that preserve corrections and evolving understanding,
- better source inspection and claim-level provenance,
- personal learning paths built from concepts a reader wants to understand,
- comparisons that explain how competing approaches differ,
- reliable, observable production workflows and deployment infrastructure,
- new publication formats where evidence-backed research can be reused responsibly.

These are directions, not promises. Each must earn its place by improving understanding, research quality, or the engineering capabilities the project exists to develop. The ambition is not the maximum number of features but a platform whose ability to discover, investigate, connect, and explain improves systematically.

---

## 18. The Meaning of Success

**For the reader:** a development becomes more understandable, its evidence is inspectable, and further learning is easier.

**For knowledge quality:** relationships and historical context are preserved, not lost in a stream of isolated articles.

**For research quality:** the system gets better at finding relevant evidence, recognizing gaps, challenging claims, and staying within what the evidence supports.

**For engineering:** the pipeline becomes more reliable, observable, recoverable, and understandable as it grows.

**For the builder:** each stage deepens practical understanding of AI research systems and serious software engineering. The codebase is evidence of learning, not a substitute for it.

The strongest version of The Devlar does not claim to know everything. It has a disciplined way to discover what matters, investigate what can be established, explain what has been learned, and show where the limits remain.

---

## 19. The Founding Statement

The Devlar begins with a simple conviction:

**The world does not need more technological noise. It needs better ways to understand what is changing.**

We will begin with the developments that shape technology, but we will not stop at the headline. We will seek the sources, examine the claims, recover the context, connect the relevant ideas, and explain the findings in language that helps people think more clearly.

We will use AI not as a replacement for evidence, but as a system to be designed, evaluated, and constrained in service of research. We will treat knowledge as something that must retain its provenance and remain open to revision. We will treat engineering reliability as part of the product's integrity, because a research process that loses its work or obscures its failures cannot be trusted to support learning.

We will build deliberately, and we will take the time that understanding requires. We will compare approaches rather than follow fashions. We will welcome ambitious problems while resisting complexity that serves no purpose. We will measure improvement not only by what the system can generate, but by what it can substantiate, recover, explain, and help a person understand.

The Devlar is a continuing effort to turn technological change into lasting understanding, one investigation, one connection, and one well-supported explanation at a time.

---

## 20. A Note on This Document

This vision describes purpose, values, intended experience, and long-term direction. It is not a technical specification.

The current architectural direction is: a production side (collectors, a research engine, editorial and quality stages, and a publishing step) and a reader-facing PERN website, connected through PostgreSQL with pgvector as a durable contract, with the research engine written in Python. This is a design direction, not doctrine. Schemas, service boundaries, orchestration frameworks, retrieval strategies, and infrastructure should be settled through research, experiments, and documented decisions.

Revise this document when the underlying purpose or principles genuinely change. Record ordinary implementation decisions in architecture and decision documents rather than rewriting the vision to justify each new tool.

**The implementation may evolve substantially. The commitment to evidence, understanding, deliberate learning, and reliable engineering should remain at its center.**
