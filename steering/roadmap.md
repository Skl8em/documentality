---
title: "Roadmap — the phases we mean to traverse"
force: propose
register: govern
intention: suasive
view: synchronic
provenance: { type: function, id: steering }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
phase: 06-refoundation
---

The working plan, revisable.
It names the **construction phases** (how *we* build the system).
**Current work is restricted to Phase I** (an operational system, per [`foundation.md`](foundation.md)); **Phase II is named but only *designed* at Phase 10**, once Phase I is complete — because it introduces a new discourse community (the AI's technical baggage) and must be re-founded, not merely executed.
Phases 01–05 are past and recorded in [`phases/`](../phases/README.md); this roadmap looks forward from 06.

| Phase | Aim | Outputs |
|---|---|---|
| **06 — Refoundation & front-end** *(done)* | Absorb the Ferraris-grounded theory; lay the foundation flat; name the plan; record the founding decisions. | `foundation.md`, this roadmap, phase-06 ADRs (014–021) |
| **07 — Structuring tutorial & front-end correction** *(done)* | Write the generic *structuring* teach functions-first; correct the front-end it exposed; harden the tutorial against two blind tests. | `structure/tutorial.md`; reconciled `foundation.md`; ADR-022, ADR-023; blind-test records |
| **08 — Refactor product & source to the refounded vocabulary** *(current)* | Perlocution = floor + intention; forces = recognized cells; know/do/govern as register gloss; recommend/entail as extensions; machine as recipient-at-limit. **The producer-shelf move is done** (`docs/` dissolved → `steering/` + `imagine/` + root `phases/`, root axis `provenance`); what remains is the refounded vocabulary in the v3 files, migrating the nine `_legacy/` forces, retiring `_legacy/`, and grouping `phases/` by era. | refactored `write/` + `structure/`; producer-organized tree |
| **09 — Reconcile governance & the frontmatter schema** | Reconcile the schema (fields, allowed values, validation) to the refounded model; realign the `steering/` + `phases/` records. Keep the catalogue clean and machine-ready — this *prepares* Phase II without committing it. | schema spec; validation rules |
| **10 — Design of Phase II** | Phase I complete: **re-run the structuring front-end** for the incoming AI discourse community — its communities, functions, governance, maintenance — and produce the Phase II plan. Design, not execution. | a Phase-II `foundation` + `roadmap` |

Everything past Phase 10 (generators, hooks, AI operating instructions — the computational model itself) is deliberately left blank: it is the *subject* of Phase 10, planned when we have a better idea, not committed now.

Verification runs *within* each phase, not as a final gate: a phase closes only when its outputs pass their own checks (links, schema validity, self-consistency).

Two standing debts, tracked so they are not forgotten: migrate the nine not-yet-built force folders from `_legacy/` (folded into Phase 08), and retire `_legacy/` once migration completes.

This roadmap is maintained: as a phase closes, its row is marked done and its records freeze in `phases/`.
Changing the plan is a recorded decision, not a silent edit.
