---
title: "ADR-024 — Producer shelf: dissolve `docs/`, provenance at root"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-08-refactor }
constitutive: yes
concerns: [structuring, steering]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:4e00f27b50c843ce0726fbb2e1ecdbeda3ef43e04eefa4d21fdb986cb74e8324
---

## Status

accepted — 2026-07-25

## Context and forces in play *(justify)*

The self-application ([`../phase-07-structuring-tutorial/self-application.md`](../phase-07-structuring-tutorial/self-application.md)) derived that our source is the **producer's shelf**, shelved by provenance (ADR-018), with a *generated* user surface.
But the tree still carried a generic `docs/` bucket, which is **not a provenance** — it was a scope/genre container from the pre-refoundation model (ADR-010).
If the shelf axis is provenance, then each standing function is a root folder, and the project's own governance (`steering`) and its intended work (`imagine`) are functions like any other; the frozen construction records are a bounded `project` provenance.

## Decision

Dissolve `docs/`.
The root is now one folder per function — `theory/`, `write/`, `structure/`, `steering/`, `imagine/` — plus `phases/` for the frozen `project` records.
The root declares `axis: provenance`, `dominant-community: contributor`.
The `onboarding` provenance is retired: it was a *served* reading order, not a producing function; the front doors (`README`, the on-ramps) belong to their author-functions (`steering`, `writing`, `structuring`).

## Entail — what follows

`docs/{ADR,ARCHITECTURE,CHANGELOG,CONTRIBUTING,README,foundation,roadmap}` moved to `steering/`; `docs/phases/` moved to root `phases/`; `imagine/` created with an orient.
Inbound references across the live docs were updated (root `README`, `steering/ARCHITECTURE`, `steering/README`, `CONTRIBUTING`, `write/**` pointers, `foundation`, `roadmap`); a link check reports zero move-related breakage.
Frozen ADR records and historical changelog entries are left as-is (they describe the state at their time).
This **enacts** ADR-018 (producer shelf) and **refines** ADR-010 (the product-vs-project split is now one provenance shelf, not two trees) and ADR-008 (the root axis is `provenance`, not `scope`).
Deferred to the rest of Phase 08: the naming mismatch (`write/`↔`writing`, `structure/`↔`structuring`), the v3 vocabulary refactor, the `_legacy/` migration, and grouping `phases/` by era.
