---
title: "Open questions — live deliberations awaiting a decision"
force: propose
verb: argue
intention: state
view: synchronic
provenance: { type: function, id: steering }
constitutive: no
concerns: [theorising, writing, structuring, steering]
audience: [contributor, decider]
reader: H+M
status: draft
---

This is the project's **current** deliberation register: questions that are open, each carried on the *current* side until it is decided, at which point it **decants** into a frozen `decide` record under `phases/` (the state/change seam — a current `govern` document becoming a frozen one).
It is dogfood: the round-2 rule says a deliberation is exactly this, and we have it.

Derived in the Phase-07 self-application ([`self-application.md`](../phases/refoundation/phase-07-structuring-tutorial/self-application.md) §Pending); the schema forks below are routed to Phase 10, on the lint harness Phase 09 stands up.

## Open

Nothing is currently open.
The two schema forks (⚑ Decision 1 and 2) closed in Phase 10; what remains undecided is not a deliberation but a set of fields we have deliberately not ruled on yet — they are listed as `still_open` in [`../schema/frontmatter.schema.json`](../schema/frontmatter.schema.json) (the `distance`/`power` value sets, the `status` vocabulary, the shape of `concerns`, and the deferred `force × power` derivation of `constitutive`).
A question opens here when someone needs it answered.

## From the design dialogue — ratified 2026-08-02

Reached by reasoning in conversation, then ruled on by the maintainer.
All of these **decanted in Phase 10** — each into the frozen record linked below — except the working convention, which went to `ways-of-working` rather than the register.
They are kept here as the deliberation's own trace: the record says what was decided, this says how it was reached.

### Register — derived from `constitutive`, then direction of fit **[decanted]**

The `know / do / govern` triad is **kept, but re-founded** — no ripple to the `writing/forces/` doors.
`register` is **derived**: `constitutive: yes` ⇒ `govern`; otherwise the force's direction of fit ⇒ `know` (word→world) / `do` (world→word).
The third bin is not a third direction of fit; it is the *constitutive* one.

- **Ratified:** register derived (settles ⚑ Decision 2); a new **stored** field `constitutive: yes|no`.
- **Decanted:** ADR-030 — [`register-derived-constitutive`](../phases/refoundation/phase-10-schema/register-derived-constitutive.md), superseding the register part of ADR-016 and refining that of ADR-025.

### `constitutive` — a conscious choice for now (force × power deferred) **[decanted]**

A `recommend` from the Quai d'Orsay, or a binding `instruct` (an ISO procedure), *constitutes*; the same forces with no authority merely serve — so `constitutive` could one day derive from **force × `power`**.

- **Ratified:** for now `constitutive` is a *conscious, stored* `yes|no`; the force × `power` derivation is **deferred**, revisited once we see it used.
- **Decanted:** ADR-030, which carries the deferral and names it as an honest limit.

### A name for the non-constitutive pole — **resolved: none**

- **Ratified:** no name.
  We store the boolean `constitutive: yes|no`; the complement stays the unmarked default.
- **Decanted:** ADR-030, point 6.

### `operationalizing` — a sixth function (VSM System 3) **[decanted]**

For the **operational apports** — the coordinates and conventions we *chose to reify* to make the theory a workable, checkable, machine-ready system (`view`, `constitutive`, `register`, `reader`, `id`/`slug`, `hash`, `concerns`, `status`, `retention`, `pin`, …) — distinct from `steering` (System 5, direction) and `imagining` (System 4, future), and *upstream* of the IT tooling (`theorising → operationalizing → structuring/writing → designing → IT tools`).

- **Ratified:** adopt, giving six functions (`theorising` `writing` `structuring` `operationalizing` `steering` `imagining`).
- **Enacted:** the `operationalizing/` shelf is created with its orient and first fiches (`view`, `constitutive`, `register`).
- **Decanted:** ADR-033 — [`operationalizing-function`](../phases/refoundation/phase-10-schema/operationalizing-function.md); the function set is reconciled in `foundation.md` and `CONTRIBUTING`.

### ADR tiering — reserve ADRs for durable commitments **[decanted]**

Not every decision deserves an ADR.
An ADR is warranted only when the decision installs a **standing obligation to verify and apply** (a constitutive-durable norm); a **punctual** action (moving a folder, renaming a file) is a changelog line, no ADR.

- **Ratified:** adopt the test; relax `CONTRIBUTING`'s trigger to "any decision that creates a standing obligation → ADR"; and **review the register by *receivability*** — keep the receivable records (even where we later changed our mind), demote the non-receivable (see the Phase-10 ADR review).
- **Decanted:** ADR-032 — [`adr-tiering`](../phases/refoundation/phase-10-schema/adr-tiering.md); the review demoted ADR-019 and kept three borderlines.

### VCS ↔ governance topology

Git's branches (parallel, mutable, losable) sit uneasily under governance (one fact, valid for all, preserved).
The clean mapping: a **feature branch = a proposal** (`propose`, provisional); **merge to the trunk = the enacting `decide`** (a decision is valid when it reaches the trunk, not while it lives on a branch); an **orphan branch is forgotten by design** unless recorded to the trunk.
So governance lives on the **singular line** (trunk), or in a separate governance repo referencing code by `pin`.

- **Ratified as a working convention, not an ADR:** branch = proposal, merge to the trunk = the enacting `decide`, orphan branch = forgotten by design; governance on the trunk.
  No impact on the project itself → it lives in `ways-of-working`, not the register.

### Content-hash fixity seal (complement to the ULID) — **[decanted]**

ULID = *identity* (which record); a per-record **content hash** = *fixity* (this exact frozen content, tamper-evident, and portable across repos — unlike a git SHA).
The record-level `pin`.

- **Ratified:** add an optional `hash:` sealing each frozen record at close.
- **Decanted:** ADR-031 — [`content-hash-fixity`](../phases/refoundation/phase-10-schema/content-hash-fixity.md); `scripts/hash_seal.py` mints, `scripts/hash_check.py` verifies, and the gate runs it.

## Closed

- **⚑ Decision 1 — encode `intention` coarse or fine:** store the **coarse** family `state` · `formative` · `suasive` · `affective`, not the fine value.
  **Decided coarse** (2026-08-02, on ADR-026's floor value), **executed in Phase 10**: the corpus was swept fine → coarse (`locate`/`model`/`enable` → `formative`, `convince` → `suasive`), and the coarse set is now a lint **error** in [`../schema/frontmatter.schema.json`](../schema/frontmatter.schema.json).
  The fine values remain in the guidance as *readings* of a coarse value, not as storable ones.
- **⚑ Decision 2 — store `register`, or derive it from `force`:** **decided derived** (2026-08-02), **executed in Phase 10**: stored `register` is removed from the corpus and is now a lint error, and the value is computed as `constitutive ? govern : direction-of-fit(force)`.
  Decanted into ADR-030 — [`register-derived-constitutive`](../phases/refoundation/phase-10-schema/register-derived-constitutive.md).
- **The `_legacy/` migration debt** (migrate the nine not-yet-built forces; retire `_legacy/`) — **closed in Phase 08**: all twelve forces are built under `writing/forces/`, and `_legacy/` is retired.
  (Roadmap standing debts.)
- **The gerund naming rule** (function folders and `provenance.id` take the gerund form) — **decided in Phase 08**, ADR-027; enacted `theory→theorising`, `write→writing`, `structure→structuring`, `imagine→imagining`.

Each open question closes into a frozen ADR when decided; this document holds the *current* side until then.
