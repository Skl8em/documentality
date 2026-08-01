---
title: "Open questions — live deliberations awaiting a decision"
force: propose
verb: argue
register: govern
intention: state
view: synchronic
provenance: { type: function, id: steering }
concerns: [theorising, writing, structuring, steering]
audience: [contributor, decider]
reader: H+M
status: draft
---

This is the project's **current** deliberation register: questions that are open, each carried on the *current* side until it is decided, at which point it **decants** into a frozen `decide` record under `phases/` (the state/change seam — a current `govern` document becoming a frozen one). It is dogfood: the round-2 rule says a deliberation is exactly this, and we have it.

Derived in the Phase-07 self-application ([`self-application.md`](../phases/refoundation/phase-07-structuring-tutorial/self-application.md) §Pending); the schema forks below are routed to Phase 10, on the lint harness Phase 09 stands up.

## Open

### ⚑ Decision 1 — encode `intention` coarse or fine

Store `intention` as the **coarse** family `state` · `formative` · `suasive` · `affective` (ADR-026), or as the **fine** value `state` · `locate` · `model` · `enable` · `convince`?

- **Proposed:** coarse.
- **Status:** open → **Phase 10** (schema reconciliation), on the lint harness Phase 09 stands up.
- **Current practice:** the fine values are used in the frontmatter and guidance for now (e.g. `intention: model`), pending the decision. See [`frontmatter-schema-draft.md`](../phases/refoundation/phase-07-structuring-tutorial/frontmatter-schema-draft.md).

### ⚑ Decision 2 — store `register`, or derive it from `force`

`register` (know / do / govern) is a gloss over `force`. Store it in the frontmatter, or generate it?

- **Proposed:** derive.
- **Status:** open → **Phase 10**.
- **Current practice:** steering records carry `register` explicitly; the product v3 files do not. The inconsistency is what Phase 10 resolves.

## Closed

- **The `_legacy/` migration debt** (migrate the nine not-yet-built forces; retire `_legacy/`) — **closed in Phase 08**: all twelve forces are built under `writing/forces/`, and `_legacy/` is retired. (Roadmap standing debts.)
- **The gerund naming rule** (function folders and `provenance.id` take the gerund form) — **decided in Phase 08**, ADR-027; enacted `theory→theorising`, `write→writing`, `structure→structuring`, `imagine→imagining`.

Each open question closes into a frozen ADR when decided; this document holds the *current* side until then.
