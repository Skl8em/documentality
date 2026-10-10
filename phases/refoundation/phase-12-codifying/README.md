---
title: "Phase 12 — Codifying"
force: orient
intention: formative
view: diachronic
provenance: { type: project, id: phase-12-codifying }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
hash: sha256:652653a953be91d68ca073b429b1a487e65b80fdc7ac4b8918222c41f58c9165
---

The last phase of Phase I, and of the refoundation era.
Phase 11 had hardened the tooling and left it unexplained; this phase gave the tooling a shelf, closed Phase 11's account, and made the same failure detectable by the gate.
It closed on 2026-10-09 by the project owner's ruling, which also closed Phase I and opened the rush to MVP ([ADR-042](../../rush-to-mvp/phase-13-design/rush-to-mvp.md)).

What landed (detailed in [`plan.md`](plan.md), one workstream per bullet):

- **T1 — `codifying` is the seventh function.**
  A community map of who reads about the tooling, the engine/config seam drawn so that `scripts/` knows nothing of this repository (`docsys.yaml` holds what it does), and the [`codifying/`](../../../codifying/README.md) shelf with fiches for the gate, the schema pipeline and referential integrity ([ADR-035](codifying-function.md)).
  An audit of the gate's messages for a reader with no context came out of it.
- **T2 — Phase 11's account is closed.**
  Its three unwritten decisions became ADR-036 to ADR-038, written after the fact and dated when recorded; its README was written from the commits; `writing/frontmatter.md` and `steering/ARCHITECTURE.md` were brought in line with it.
- **T3 — a change to the tooling that explains nothing fails the gate.**
  The paired-change rule examines each commit since an anchor ([ADR-039](paired-change-rule.md)), and fails only where work lands ([ADR-040](paired-change-where-it-fails.md)).
- **T4 — the debts T1 recorded were paid or kept on purpose.**
  Supersession cycles and self-supersession are rejected, an empty register match fails, three validators' messages are fixtured, and the frozen-record definition stays in code with a guard against the schema.
- **T6 — the current phase is declared once.**
  A ledger, [`steering/phases.yaml`](../../../steering/phases.yaml), and a `phase-state` check that verifies every other place against it ([ADR-041](phase-ledger.md)).
- **T5 — the close**, this record.

Records:

- [plan.md — the detailed plan](plan.md)
- [community map](community-map.md), [engine/config seam](engine-config-seam.md), [error-message audit](error-message-audit.md)
- [ADR-035 — `codifying` is the seventh function](codifying-function.md)
- [ADR-039 — a change to the tooling that explains nothing fails the gate](paired-change-rule.md)
- [ADR-040 — where the paired-change rule fails](paired-change-where-it-fails.md)
- [ADR-041 — the current phase is declared once, in a ledger](phase-ledger.md)

Verification, against the plan's definition of done, at close:

- The gate is green, through the ledger flip that closes this phase.
- **The phase-close re-read is the project owner's**: the `codifying/` fiches (open point 4) and `steering/foundation.md` were re-read and judged good enough for the next era, on 2026-10-09.
  It is a judgment, recorded as one, not a checklist pass.
- **The merge is not yet observed** (open point 2): this branch has not been merged.
  The rule's cost at merge time is still unmeasured, and is recorded when the merge happens.
- **The changelog's convention**, which T5 was to state: a phase's closing entry *supplements* the per-task entries already written, and does not supersede them.
  The log is append-only, so the per-task entries stand as written.
- **Three items of the definition of done were overtaken, not met.**
  The roadmap no longer names a deployment phase after this one: ADR-042 absorbs it into the rush to MVP.
  The items this plan deferred to it — cold readers for the fiches, the adopter community, the extraction triggers — go to that era's two phases; extraction is no longer deferred, since the rush packages the engine.
  The closure rule went to the life-cycle phase, which is now parked.

Departures and gaps, recorded rather than hidden.
The phase grew by T6, a workstream inserted mid-phase, and by a planned phase ahead of deployment that it did not run.
It added roughly 1,400 lines of Python and fixtures to keep the repository's mentions of its own phase consistent; the external review read that as the project optimising what its method could see, and ADR-042's moratorium on self-referential checks is the answer the project owner chose.
The review also found defects that the gate could not see and this phase did not look for: the root README's front door had been broken since 2026-07-25, and the product pages disagree on where documents go.
The adoption phase fixes those first ([plan](../../rush-to-mvp/phase-14-adoption/plan.md), T1).
