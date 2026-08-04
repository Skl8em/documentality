---
title: "Roadmap — the phases we mean to traverse"
force: propose
intention: suasive
view: synchronic
provenance: { type: function, id: steering }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
phase: 08-refactor
review: 10-schema
---

The working plan, revisable.
It names the **construction phases** (how *we* build the system).
**Current work is restricted to Phase I** (an operational system, per [`foundation.md`](foundation.md)); **Phase II is named but only *designed* at Phase 11**, once Phase I is complete — because it introduces a new discourse community (the AI's technical baggage) and must be re-founded, not merely executed.
Phases 01–05 are past and recorded in [`phases/`](../phases/README.md); this roadmap looks forward from 06.

| Phase | Aim | Outputs |
|---|---|---|
| **06 — Refoundation & front-end** *(done)* | Absorb the Ferraris-grounded theory; lay the foundation flat; name the plan; record the founding decisions. | `foundation.md`, this roadmap, phase-06 ADRs (014–021) |
| **07 — Structuring tutorial & front-end correction** *(done)* | Write the generic *structuring* teach functions-first; correct the front-end it exposed; harden the tutorial against two blind tests. | `structuring/tutorial.md`; reconciled `foundation.md`; ADR-022, ADR-023; blind-test records |
| **08 — Refactor product & source to the refounded vocabulary** *(done)* | Perlocution = floor + intention; forces = recognized cells; know/do/govern as register gloss; recommend/entail as extensions; machine as recipient-at-limit. Producer shelf (`docs/` dissolved → `steering/` + `imagining/` + root `phases/`); refounded vocabulary across `writing/` + `structuring/`; nine `_legacy/` forces migrated and `_legacy/` retired; `structuring/applied.md` retired; `steering/open-questions.md` added; `phases/` grouped by era; gerund naming rule (folders = gerund ids). | refactored `writing/` + `structuring/`; all twelve forces; producer-organized tree; ADR-024–027 |
| **09 — Tooling: enforce the conventions, ready the catalogue** *(done)* | Stand up the tooling that makes the schema work efficient and meaningful: a **unified markdownlint** where CLI and the VSCode (David Anson) extension apply one ruleset — title in frontmatter (never `# …`), the semantic-line-break rule (ADR-021), and a deliberate take-over of the default rules; a **frontmatter-lint harness** started on the *safe* invariants only (as examples that scaffold Phase 10); and **ULID + slug identifiers** replacing sequential counts (`ADR-NNN`, `phase-NN`), with minting and verification tooling. | `.markdownlint-cli2.jsonc`; `scripts/` validators (markdownlint config + Python frontmatter/ULID checks); ULID scheme + migration; pre-commit / CI wiring; this phase's [`plan.md`](../phases/refoundation/phase-09-tooling/plan.md) |
| **10 — Reconcile governance & the frontmatter schema** *(done)* | Reconcile the schema (fields, allowed values, validation) to the refounded model, *using* the Phase-09 lint harness; settle the two open ⚑ (intention coarse-vs-fine, register stored-vs-derived); realign the `steering/` + `phases/` records. Keep the catalogue clean and machine-ready — this *prepares* Phase II without committing it. | reconciled `schema/frontmatter.schema.json` + promoted linter; the corpus swept; ADR-030–033; fixity tooling; this phase's [`plan.md`](../phases/refoundation/phase-10-schema/plan.md) |
| **11 — Design of Phase II** | Phase I complete: **re-run the structuring front-end** for the incoming AI discourse community — its communities, functions, governance, maintenance — and produce the Phase II plan. Design, not execution. | a Phase-II `foundation` + `roadmap` |

Everything past Phase 11 (generators, hooks, AI operating instructions — the computational model itself) is deliberately left blank: it is the *subject* of Phase 11, planned when we have a better idea, not committed now.

## Plan changes

Changing the plan is a recorded decision, not a silent edit — but a *sequencing* decision obliges nobody once executed, so it is held here and in the changelog rather than in the ADR register (ADR-032).

- **The restart strategy (Phase 06).** Coming out of the refoundation we chose to rebuild **front-end first**: lay the principles down immediately (`foundation.md`, this roadmap) and defer the tree reorganization to Phase 08, rather than reorganize and then discover the principles had moved.
  Originally recorded as ADR-019; demoted to this note in Phase 10, its frozen record kept at [`../phases/refoundation/phase-06-refoundation/ADR-019-restart.md`](../phases/refoundation/phase-06-refoundation/ADR-019-restart.md).
- **The insertion of Phase 09 (tooling)**, and the renumbering of the schema and Phase-II-design phases to 10 and 11 — recorded by this edit, the [Phase-09 plan](../phases/refoundation/phase-09-tooling/plan.md), and the changelog entry.
  Tooling was placed *before* the schema so the lint harness would make Phase 10 efficient.

Frozen records from earlier phases keep their-time phase numbers.

Verification runs *within* each phase, not as a final gate: a phase closes only when its outputs pass their own checks (links, schema validity, self-consistency).

Two standing debts, both **closed in Phase 08**: the nine not-yet-built force folders were migrated from `_legacy/`, and `_legacy/` was retired.

This roadmap is maintained: as a phase closes, its row is marked done and its records freeze in `phases/`.
Changing the plan is a recorded decision, not a silent edit.
