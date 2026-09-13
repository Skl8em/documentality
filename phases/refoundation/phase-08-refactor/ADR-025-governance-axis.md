---
title: "ADR-025 — Govern by domain governed; the transversal/vertical tension and the `concerns` coordinate"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-08-refactor }
constitutive: yes
concerns: [steering, structuring]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:cda45693c8810c48f4d383ef016fb2fb60b60feeeb061932f58035b2abfcddae
---

## Status

accepted — 2026-07-25

## Context and forces in play *(justify)*

Two questions kept re-opening: where does a `govern` document live, and does it collide with the `steering` function?
They collide only in appearance.

**`steering` is not "the govern register."**
It is the activity whose *domain is the project itself*, and like any activity it carries all three registers — `foundation` is its `know`, `CONTRIBUTING` its `do`, the ADR register its `govern`.
So a govern-document is placed by **the domain it governs**, not by its register: a `mandate` that binds the *user's* writing is product content (`write/rules.md`, function `writing`); the *same force* binding *contribution to the project* is `steering/CONTRIBUTING.md`.
Same act, different activity, because a different domain is governed.

**Decision and rule are two documents, joined at the state/change seam.**
A *decision* (`decide`, frozen, diachronic) records that the project chose X; the *rule* it installs (`mandate`, current, synchronic) is the living convention.
The decision lives with the governance effort (a phase record, indexed by `steering`); the rule lives with the activity it binds; the rule cites the decision and the decision `entail`s the rule (ADR-011; `concepts.md`, the state/change seam).
So "a decision about how to write" is not one misfiled document but two well-placed ones.

**The residual tension is real and irreducible.**
Whether a decision that governs *only* structuring should sit centrally (one register + phase records) or locally (with `structure/`) is the **transversal-vs-vertical** tension — matrix organisation, cross-cutting concerns, federal-vs-local.
It is fractal: if `structuring` ever becomes a sub-project it takes its own governance with it (Beer's VSM recursion — every level has its own policy function), and inside it the same tension re-appears between its shared and its local decisions.
It cannot be settled *a priori*; it is a per-project, per-scale judgement.

## Decision

1. **Classify govern-documents by the domain governed**, not by register; `steering` is simply the activity whose domain is the project itself.
   A decision and the rule it installs are two documents (state/change seam), placed independently.

2. **Name the transversal/vertical tension as irreducible.** The system does not pick central or local for the user; it makes the fork explicit.

3. **A root governance-axis declaration**, alongside the shelf axis: *central* (one register + phase-provenance records) or *local* (each activity owns its decisions; only cross-cutting ones escalate), and where the line sits.
   Default for this project: **central register, phase-provenance records**.

4. **Procedure = subsidiarity / VSM recursion.** A decision is owned by the *lowest* activity or sub-project whose boundary contains all its consequences; a decision whose consequences cross siblings escalates to the level that contains them.

5. **Add a `concerns` coordinate** — the activity or activities a document *governs or bears on* — distinct from `provenance` (who *produced* it).
   One `concerns` ⇒ vertical (locally ownable); several ⇒ transversal (escalates).
   This makes concrete `concepts.md`'s line that a decision's bearing on the functions is *a relation, not a location*.

6. **Generate, do not move.** The per-activity view ("every decision that concerns structuring") is *generated* from `concerns`; the records stay shelved once by provenance, and the central register stays the transversal index.
   A worker's wish for proximity is a reader-surface need, served by generation — never by relocating frozen records.
   As a bonus, `concerns` **pre-tags** records for a clean cut if an activity later splits into a sub-project (with `pin` for the cross-project reference).

## Entail — what follows

`concerns` is added to the frontmatter schema draft (optional; primarily for records and govern-documents) and dogfooded on this ADR and ADR-024.
`concepts.md` gains a short section making the govern-by-domain rule and the transversal/vertical fork explicit.
The structuring tutorial will gain a brief **governance-axis** aside (with the lifecycle tutorial), parallel to the shelf-axis declaration.
Worked check on our own register: ADR-014 (refoundation) `concerns [theory, writing, structuring]`, ADR-021 (line breaks) all four, ADR-003 (recommend) `[theory, writing]` — transversal; ADR-023 (tutorial) and ADR-018 (shelf) `[structuring]` — vertical.
The coordinate separates them cleanly, and confirms our register is a genuine *mix*, which is why neither pure-central nor pure-local filing is right.

Refines ADR-016 (know/do/govern is a register gloss, not the shelf axis), ADR-018 (this is another face of source-vs-generated), and ADR-010 (product-vs-project = the domain-governed distinction).

## Honest limit

Documentation survives reorganisations poorly: every move rots links and displaces records (we felt it dissolving `docs/`).
Provenance-first shelving is the hedge, not a cure — it shelves by the *most stable* axis (activities change less than topics or scopes), so reorganisations are rare and, when they come, are coarse aligned moves of a whole subtree rather than scattered edits.
`generate-don't-move` follows directly: do not reorganise the source to satisfy a reading-proximity need that a generated view can meet.
