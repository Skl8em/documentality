---
title: "ADR-019 — Restart strategy: front-end first, principles now, reorg in Phase 08"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-06-refoundation }
constitutive: yes
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:cea8ef8184aa6e4c5e7ff85d4bf3cac4720fafd63e89c28256c6c8c998cd4872
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

The refoundation deepens and corrects the built system rather than discarding it, so a greenfield rebuild would waste recoverable content.
But we had also never laid the front-end flat, which is why we kept re-deciding the same things.

## Options considered

- Greenfield: archive v3, rebuild from scratch — consequence: needless loss, the content mostly survives.
- Direct refactor: skip the formal front-end — consequence: repeats the original mistake of building before deciding.
- Front-end first, then refactor — consequence: decisions are recorded once and structure the rest; more upfront, less churn.

## Decision

We take approach (a): lay the front-end flat now (`foundation.md`, `roadmap.md`), **decide the principles now**, and defer the physical reorganization of the tree to Phase 08.
The current tree is kept meanwhile.

## Entail — what follows

Phase 06 records these founding decisions; Phase 07 authors the structuring tutorial; Phase 08 refactors and moves files.
"Act the principle now" means the decisions bind from today even though the files have not moved yet.
