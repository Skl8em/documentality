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
phase: 12-codifying
---

The working plan, revisable.
It names the **construction phases** (how *we* build the system).
**Current work is restricted to Phase I** (an operational system, per [`foundation.md`](foundation.md)); **Phase II is named, but not designed until we tackle it** — its design is thought to become the first phase of that era, once Phase I is complete — because it introduces a new discourse community (the AI's technical baggage) and must be re-founded, not merely executed.
Phases 01–05 are past and recorded in [`phases/`](../phases/README.md); this roadmap looks forward from 06.

| Phase | Aim | Outputs |
|---|---|---|
| **06 — Refoundation & front-end** *(done)* | Absorb the Ferraris-grounded theory; lay the foundation flat; name the plan; record the founding decisions. | `foundation.md`, this roadmap, phase-06 ADRs (014–021) |
| **07 — Structuring tutorial & front-end correction** *(done)* | Write the generic *structuring* teach functions-first; correct the front-end it exposed; harden the tutorial against two blind tests. | `structuring/tutorial.md`; reconciled `foundation.md`; ADR-022, ADR-023; blind-test records |
| **08 — Refactor product & source to the refounded vocabulary** *(done)* | Perlocution = floor + intention; forces = recognized cells; know/do/govern as register gloss; recommend/entail as extensions; machine as recipient-at-limit. Producer shelf (`docs/` dissolved → `steering/` + `imagining/` + root `phases/`); refounded vocabulary across `writing/` + `structuring/`; nine `_legacy/` forces migrated and `_legacy/` retired; `structuring/applied.md` retired; `steering/open-questions.md` added; `phases/` grouped by era; gerund naming rule (folders = gerund ids). | refactored `writing/` + `structuring/`; all twelve forces; producer-organized tree; ADR-024–027 |
| **09 — Tooling: enforce the conventions, ready the catalogue** *(done)* | Stand up the tooling that makes the schema work efficient and meaningful: a **unified markdownlint** where CLI and the VSCode (David Anson) extension apply one ruleset — title in frontmatter (never `# …`), the semantic-line-break rule (ADR-021), and a deliberate take-over of the default rules; a **frontmatter-lint harness** started on the *safe* invariants only (as examples that scaffold Phase 10); and **ULID + slug identifiers** replacing sequential counts (`ADR-NNN`, `phase-NN`), with minting and verification tooling. | `.markdownlint-cli2.jsonc`; `scripts/` validators (markdownlint config + Python frontmatter/ULID checks); ULID scheme + migration; pre-commit / CI wiring; this phase's [`plan.md`](../phases/refoundation/phase-09-tooling/plan.md) |
| **10 — Reconcile governance & the frontmatter schema** *(done)* | Reconcile the schema (fields, allowed values, validation) to the refounded model, *using* the Phase-09 lint harness; settle the two open ⚑ (intention coarse-vs-fine, register stored-vs-derived); realign the `steering/` + `phases/` records. Keep the catalogue clean and machine-ready — this *prepares* Phase II without committing it. | reconciled `schema/frontmatter.schema.json` + promoted linter; the corpus swept; ADR-030–033; fixity tooling; this phase's [`plan.md`](../phases/refoundation/phase-10-schema/plan.md) |
| **11 — Tooling hardening** *(done — account closed in Phase 12)* | Close the gaps Phase 10's enforcement left: a **closed frontmatter vocabulary** (a field earns its place by carrying a reason), **real YAML parsing** in place of the hand-rolled subset, the rules **authored in YAML** with a generated JSON artifact, and a **referential validator** so an identifier pointing nowhere fails the gate. | closed vocabulary; `pyyaml` + parser fixtures; `frontmatter-rules.yaml` → generated JSON + drift check; referential integrity in `ulid_check.py`; ADR-036–038, written afterwards by Phase 12; this phase's [`README.md`](../phases/refoundation/phase-11-tooling-hardening/README.md) and [`plan.md`](../phases/refoundation/phase-11-tooling-hardening/plan.md) |
| **12 — Codifying: shelve the tooling, close Phase 11's account** *(in progress — T1–T4 done, T6 under way)* | Give the tooling a shelf: adopt **codifying** as the seventh function — the "IT tools" link ADR-033's own chain names but never gave a home — with an ADR, an orient, and fiches for the gate, the YAML/JSON split, and referential integrity. Close Phase 11's unfinished account: its three promised ADRs, its closing README, the vocabulary-closure fact retrofitted into `writing/frontmatter.md`. Make the gap **self-detecting**: a `scripts/`/`schema/` change with no paired documentation change fails the gate, and the current phase is **declared once** in a ledger against which the gate checks the roadmap, the index, the folders and the `phase:` fields. | `codifying/` shelf (ADR, README, fiches); Phase 11's backlogged ADRs + README; reconciled `writing/frontmatter.md` + `ARCHITECTURE.md`; a paired-change gate check; a **phase ledger** (`steering/phases.yaml`) declaring where the project is, and a `phase-state` gate check verifying every place that speaks of it (enforcing ADR-038); this phase's [`plan.md`](../phases/refoundation/phase-12-codifying/plan.md) |
| **Deployment** *(unnumbered — see below)* | Ask how the current content is **exposed** and made **usable by third parties**: who they are (the adopter community Phase 12's map named and cut), what they would install or read, in what form, and what must be true of the tooling — the engine/config seam, the `codifying/` fiches — for a stranger to act on it. Includes **cold readers**: someone who did not build the tooling reads the fiches, and someone outside the project reads the product, before either is claimed to work. A question first; its outputs are not decided here. | a deployment plan; cold-reader records |
| **Design of Phase II** *(unnumbered — see below)* | Phase I complete: **re-run the structuring front-end** for the incoming AI discourse community — its communities, functions, governance, maintenance — and produce the Phase II plan. Design, not execution. | a Phase-II `foundation` + `roadmap` |

**A phase takes its number when we tackle it, not before.**
Until then we know the work but not its position, because anything inserted ahead of it moves it — which has now happened twice, each time invalidating every forward reference that had named a number.
So work we have not begun is **named and ordered here, never numbered**, and forward references say *what follows what* rather than *which number it will be*.
This is the move the ADR register already makes: the ordinal is a generated display label, and the identity lives elsewhere (ADR-028).

Everything past that design (generators, hooks, AI operating instructions — the computational model itself) is deliberately left blank: it is the *subject* of that design, planned when we have a better idea, not committed now.

## Plan changes

Changing the plan is a recorded decision, not a silent edit — but a *sequencing* decision obliges nobody once executed, so it is held here and in the changelog rather than in the ADR register (ADR-032).

- **The addition of a phase ledger to Phase 12 (T6)** — recorded by this edit, the [Phase-12 plan](../phases/refoundation/phase-12-codifying/plan.md), and the changelog entry.
  The current phase was implied in a dozen places — the roadmap's markers and `phase:`, the phases index, the root README, `foundation.md`, the folders, the register — and nothing tied them together, which is why Phases 10 and 11 each closed with some of them stale.
  Phase 12 now declares it once, in a ledger, and the gate verifies the rest against it; the forward-numbering check briefly planned for T3 is subsumed by it.
  The ledger itself installs a standing obligation and earns an ADR when T6 decides it; the plan change is only the sequencing, so it is recorded here.
  The ledger was first assumed to live in `docsys.yaml`; the project owner ruled in T6 that it is its own file, `steering/phases.yaml`, because it is the project's state and changes by a ruling, where `docsys.yaml` is the tooling's configuration.
- **The addition of a deployment phase after Phase 12** — recorded by this edit, the [Phase-12 plan](../phases/refoundation/phase-12-codifying/plan.md), and the changelog entry.
  Phase 12 shelves the tooling for the people who build it; nothing yet asks how the content reaches anyone else.
  The deployment phase takes that question, and with it three things Phase 12 could not settle alone: cold readers for the `codifying/` fiches (ADR-035 states their absence as a limit), the adopter community Phase 12's map cut for lack of a second consumer, and the extraction triggers its plan named.
  It is **unnumbered**, per the rule above: named and ordered after Phase 12 and before the Phase-II design, and it takes its number when we tackle it.
  Whether it precedes the Phase-II design or sits inside Phase I is an assumption made here, not a ruling.
  Phase 12's own plan gained two workstreams in the same edit, absorbing the open points its first workstream handed on.
- **The insertion of Phase 12 (codifying)** — recorded by this edit, the [Phase-12 plan](../phases/refoundation/phase-12-codifying/plan.md), and the changelog entry.
  Phase 11 hardened the tooling but explained none of it: no shelf argues why the gate, the parser, or the schema pipeline are built the way they are, and the phase closed with three promised ADRs unwritten, no closing README, and this roadmap still reading it as *(next)*.
  This is the second time a phase has closed leaving the product describing an old model — Phase 10 caught itself mid-close and fixed it as a departure; Phase 11 didn't catch it at all — so Phase 12 both pays that debt and builds a gate check so a mechanism change without a paired explanation can no longer pass silently.
- **The restart strategy (Phase 06).**
  Coming out of the refoundation we chose to rebuild **front-end first**: lay the principles down immediately (`foundation.md`, this roadmap) and defer the tree reorganization to Phase 08, rather than reorganize and then discover the principles had moved.
  Originally recorded as ADR-019; demoted to this note in Phase 10, its frozen record kept at [`../phases/refoundation/phase-06-refoundation/ADR-019-restart.md`](../phases/refoundation/phase-06-refoundation/ADR-019-restart.md).
- **The insertion of Phase 11 (tooling hardening)** — recorded by this edit, the [Phase-11 plan](../phases/refoundation/phase-11-tooling-hardening/plan.md), and the changelog entry.
  Phase 10 reconciled the schema and enforced it, but enforcement stops at the nine required fields and six enums: the vocabulary is open (two undeclared fields are already in the corpus), the YAML parser is hand-rolled, and no identifier is checked to point at anything.
  Hardening is placed *before* the Phase-II design because Phase II generates *from* the frontmatter, and generation inherits every weakness the catalogue still carries.
  This insertion is also what prompted the numbering convention above: it moved a forward reference for the second time, and the fix is to stop numbering unstarted work rather than to keep sweeping up after it.
- **The insertion of Phase 09 (tooling)**, and the renumbering of the schema and Phase-II-design phases to 10 and 11 — recorded by this edit, the [Phase-09 plan](../phases/refoundation/phase-09-tooling/plan.md), and the changelog entry.
  Tooling was placed *before* the schema so the lint harness would make Phase 10 efficient.

Frozen records from earlier phases keep their-time phase numbers.

Verification runs *within* each phase, not as a final gate: a phase closes only when its outputs pass their own checks (links, schema validity, self-consistency).

Two standing debts, both **closed in Phase 08**: the nine not-yet-built force folders were migrated from `_legacy/`, and `_legacy/` was retired.

This roadmap is maintained: as a phase closes, its row is marked done and its records freeze in `phases/`.
Changing the plan is a recorded decision, not a silent edit.
