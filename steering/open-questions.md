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

This is the project's **current** deliberation register: questions that are open, each carried on the *current* side until it is decided, at which point it **decants** into a frozen `decide` record under `phases/` (the state/change seam — a current `govern` document becoming a frozen one).
It is dogfood: the round-2 rule says a deliberation is exactly this, and we have it.

Derived in the Phase-07 self-application ([`self-application.md`](../phases/refoundation/phase-07-structuring-tutorial/self-application.md) §Pending); the schema forks below are routed to Phase 10, on the lint harness Phase 09 stands up.

## Open

### ⚑ Decision 1 — encode `intention` coarse or fine

Store `intention` as the **coarse** family `state` · `formative` · `suasive` · `affective` (ADR-026), or as the **fine** value `state` · `locate` · `model` · `enable` · `convince`?

- **Proposed:** coarse.
- **Status:** **decided — coarse** (2026-08-02), accepted as a start even though it is another refactor. Executed in Phase 10 (a corpus sweep, fine → coarse).
- **Current practice:** the fine values are used in the frontmatter and guidance for now (e.g. `intention: model`), pending the decision.
  See [`frontmatter-schema-draft.md`](../phases/refoundation/phase-07-structuring-tutorial/frontmatter-schema-draft.md).

### ⚑ Decision 2 — store `register`, or derive it from `force`

`register` (know / do / govern) is a gloss over `force`.
Store it in the frontmatter, or generate it?

- **Proposed:** derive.
- **Status:** **decided — derived** (2026-08-02): `register` is *derived*, not stored — `constitutive ? govern : direction-of-fit(force)` → `{know, do, govern}` (see the ratified re-founding below). Executed in Phase 10 (remove stored `register` from the corpus).
- **Current practice:** steering records carry `register` explicitly; the product v3 files do not.
  The inconsistency is what Phase 10 resolves.

## From the design dialogue — ratified 2026-08-02

Reached by reasoning in conversation, then ruled on by the maintainer.
The decided ones decant into ADRs in **Phase 10**; the working convention goes to `ways-of-working`, not the register.

### Register — derived from `constitutive`, then direction of fit **[ratified]**

The `know / do / govern` triad is **kept, but re-founded** — no ripple to the `writing/forces/` doors.
`register` is **derived**: `constitutive: yes` ⇒ `govern`; otherwise the force's direction of fit ⇒ `know` (word→world) / `do` (world→word).
The third bin is not a third direction of fit; it is the *constitutive* one.

- **Ratified:** register derived (settles ⚑ Decision 2); a new **stored** field `constitutive: yes|no`.
- → Phase 10 (schema + a re-founding ADR superseding the register part of ADR-016 and ADR-025).

### `constitutive` — a conscious choice for now (force × power deferred) **[ratified]**

A `recommend` from the Quai d'Orsay, or a binding `instruct` (an ISO procedure), *constitutes*; the same forces with no authority merely serve — so `constitutive` could one day derive from **force × `power`**.

- **Ratified:** for now `constitutive` is a *conscious, stored* `yes|no`; the force × `power` derivation is **deferred**, revisited once we see it used.

### A name for the non-constitutive pole — **resolved: none**

- **Ratified:** no name. We store the boolean `constitutive: yes|no`; the complement stays the unmarked default.

### `operationalizing` — a sixth function (VSM System 3) **[ratified]**

For the **operational apports** — the coordinates and conventions we *chose to reify* to make the theory a workable, checkable, machine-ready system (`view`, `constitutive`, `register`, `reader`, `id`/`slug`, `hash`, `concerns`, `status`, `retention`, `pin`, …) — distinct from `steering` (System 5, direction) and `imagining` (System 4, future), and *upstream* of the IT tooling (`theorising → operationalizing → structuring/writing → designing → IT tools`).

- **Ratified:** adopt, giving six functions (`theorising` `writing` `structuring` `operationalizing` `steering` `imagining`).
- **Enacted:** the `operationalizing/` shelf is created with its orient and first fiches (`view`, `constitutive`, `register`).
- → Phase 10 also: a short ADR recording the function, and reconciling the function set in `foundation.md`, `self-application.md`, `CONTRIBUTING`, and the schema.

### ADR tiering — reserve ADRs for durable commitments

Not every decision deserves an ADR.
An ADR is warranted only when the decision installs a **standing obligation to verify and apply** (a constitutive-durable norm); a **punctual** action (moving a folder, renaming a file) is a changelog line, no ADR.

- **Ratified:** adopt the test; relax `CONTRIBUTING`'s trigger to "any decision that creates a standing obligation → ADR"; and **review the register by *receivability*** — keep the receivable records (even where we later changed our mind), demote the non-receivable (see the Phase-10 ADR review).
- → Phase 10.

### VCS ↔ governance topology

Git's branches (parallel, mutable, losable) sit uneasily under governance (one fact, valid for all, preserved).
The clean mapping: a **feature branch = a proposal** (`propose`, provisional); **merge to the trunk = the enacting `decide`** (a decision is valid when it reaches the trunk, not while it lives on a branch); an **orphan branch is forgotten by design** unless recorded to the trunk.
So governance lives on the **singular line** (trunk), or in a separate governance repo referencing code by `pin`.

- **Ratified as a working convention, not an ADR:** branch = proposal, merge to the trunk = the enacting `decide`, orphan branch = forgotten by design; governance on the trunk. No impact on the project itself → it lives in `ways-of-working`, not the register.

### Content-hash fixity seal (complement to the ULID) — **ratified**

ULID = *identity* (which record); a per-record **content hash** = *fixity* (this exact frozen content, tamper-evident, and portable across repos — unlike a git SHA). The record-level `pin`.

- **Ratified:** add an optional `hash:` sealing each frozen record at close.
- → Phase 10 (schema field + `scripts/hash_*`).

## Closed

- **The `_legacy/` migration debt** (migrate the nine not-yet-built forces; retire `_legacy/`) — **closed in Phase 08**: all twelve forces are built under `writing/forces/`, and `_legacy/` is retired.
  (Roadmap standing debts.)
- **The gerund naming rule** (function folders and `provenance.id` take the gerund form) — **decided in Phase 08**, ADR-027; enacted `theory→theorising`, `write→writing`, `structure→structuring`, `imagine→imagining`.

Each open question closes into a frozen ADR when decided; this document holds the *current* side until then.
