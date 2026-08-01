---
title: "ADR register — every decision, taken on record"
force: decide
verb: enact
intention: convince
view: diachronic
provenance: { type: function, id: steering }
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
---

This is the **central register** — the *act* face of deciding: it takes each decision on record, dated, in one line. It does not argue and it does not unfold consequences. The **motivation (`justify`)** and the **implications (`entail`)** of each decision live in its **phase folder** under [`phases/`](../phases/README.md) — because a decision belongs with the effort that produced it (its provenance), not in a pile of all decisions.

Append-only: a row is never edited. A superseding decision is a new row and a new record that sets `supersedes`.

| # | Decision | Phase | Date | Status |
| --- | --- | --- | --- | --- |
| [001](../phases/naive-sketch/phase-01-foundation/ADR-001-inscribed-act.md) | A document is an inscribed act with a `force` | 01-foundation | 2026-07-11 | superseded by 014 |
| [002](../phases/naive-sketch/phase-02-theory/ADR-002-perlocution-typology.md) | `perlocution` is an open typology; `prove`/`decide` are `convince` | 02-theory | 2026-07-11 | superseded by 015 |
| [003](../phases/naive-sketch/phase-02-theory/ADR-003-recommend-force.md) | Add `recommend` as the twelfth force | 02-theory | 2026-07-11 | accepted |
| [004](../phases/naive-sketch/phase-02-theory/ADR-004-drop-diataxis.md) | Drop the `diataxis` field; derive it | 02-theory | 2026-07-11 | accepted |
| [005](../phases/naive-sketch/phase-02-theory/ADR-005-verb-soft-summary.md) | `verb` is a soft summary; store only when it diverges | 02-theory | 2026-07-11 | accepted |
| [006](../phases/naive-sketch/phase-03-reorganization/ADR-006-audience-model.md) | Audience = roles × `reader`; audience lives in `structure/` | 03-reorganization | 2026-07-11 | superseded by 017 (for this project) |
| [007](../phases/naive-sketch/phase-03-reorganization/ADR-007-fractal-reorg.md) | Self-similar reorg: `write/` + `structure/`, forces by door | 03-reorganization | 2026-07-11 | accepted |
| [008](../phases/naive-sketch/phase-03-reorganization/ADR-008-tree-axis-declaration.md) | Declare `axis` + `dominant-community` at each tree root | 03-reorganization | 2026-07-11 | accepted |
| [009](../phases/naive-sketch/phase-03-reorganization/ADR-009-teach-onramp.md) | Add a `teach` on-ramp; enforce obligations by validation | 03-reorganization | 2026-07-11 | accepted |
| [010](../phases/naive-sketch/phase-04-disentanglement/ADR-010-product-vs-docs.md) | Disentangle product (users) from `docs/` (contributors) | 04-disentanglement | 2026-07-11 | accepted |
| [011](../phases/naive-sketch/phase-05-records-governance/ADR-011-entail-face.md) | `decide` gains a forward `entail` face (act / justify / entail) | 05-records-governance | 2026-07-12 | accepted |
| [012](../phases/naive-sketch/phase-05-records-governance/ADR-012-decisions-by-phase.md) | Group decision records by phase; `steering` function; this register | 05-records-governance | 2026-07-12 | accepted |
| [013](../phases/naive-sketch/phase-05-records-governance/ADR-013-open-pairings.md) | force × perlocution pairings are open defaults, not a constraint | 05-records-governance | 2026-07-12 | accepted |
| [014](../phases/refoundation/phase-06-refoundation/ADR-014-adopt-refoundation.md) | Adopt the Ferraris-grounded refoundation of the theory | 06-refoundation | 2026-07-21 | accepted |
| [015](../phases/refoundation/phase-06-refoundation/ADR-015-perlocution-floor.md) | Perlocution has no zero; forces are recognized cells | 06-refoundation | 2026-07-21 | accepted |
| [016](../phases/refoundation/phase-06-refoundation/ADR-016-force-space.md) | know/do/govern is a gloss; recommend & entail are extensions | 06-refoundation | 2026-07-21 | accepted |
| [017](../phases/refoundation/phase-06-refoundation/ADR-017-audience.md) | Audience: roles collapse, distance is the live axis, human/machine orthogonal | 06-refoundation | 2026-07-21 | accepted |
| [018](../phases/refoundation/phase-06-refoundation/ADR-018-shelf.md) | Source shelf vs generated surface; the catalogue is the pivot | 06-refoundation | 2026-07-21 | accepted |
| [019](../phases/refoundation/phase-06-refoundation/ADR-019-restart.md) | Restart strategy: front-end first, principles now, reorg in Phase 08 | 06-refoundation | 2026-07-21 | accepted |
| [020](../phases/refoundation/phase-06-refoundation/ADR-020-scope-phase-i.md) | Scope Phase I; defer and re-found Phase II | 06-refoundation | 2026-07-21 | accepted |
| [021](../phases/refoundation/phase-06-refoundation/ADR-021-line-breaks.md) | Semantic line breaks (one sentence per line) in Markdown source | 06-refoundation | 2026-07-21 | accepted |
| [022](../phases/refoundation/phase-07-structuring-tutorial/ADR-022-functions-first.md) | Front-end correction: functions first, distance per community, mutable groupings & eras | 07-structuring-tutorial | 2026-07-21 | accepted |
| [023](../phases/refoundation/phase-07-structuring-tutorial/ADR-023-tutorial-rewrite.md) | Tutorial rewrite: relevance not recurrence, `imagine`, organize-for-author, fractal explicit, conventional docs as examples | 07-structuring-tutorial | 2026-07-24 | accepted |
| [024](../phases/refoundation/phase-08-refactor/ADR-024-producer-shelf.md) | Producer shelf: dissolve `docs/`, provenance at root (`steering/` `imagine/` `phases/`) | 08-refactor | 2026-07-25 | accepted |
| [025](../phases/refoundation/phase-08-refactor/ADR-025-governance-axis.md) | Govern by domain governed; transversal/vertical tension irreducible; `concerns` coordinate; generate-don't-move | 08-refactor | 2026-07-25 | accepted |
| [026](../phases/refoundation/phase-08-refactor/ADR-026-floor-value-state.md) | The perlocution/intention floor value is `state`, not `none` | 08-refactor | 2026-07-25 | accepted |
| [027](../phases/refoundation/phase-08-refactor/ADR-027-gerund-naming.md) | Function folders and provenance ids take the gerund form | 08-refactor | 2026-08-01 | accepted |

To add a decision: append a row here, and write its full record (context + `justify` + `entail`) in the current phase folder.
