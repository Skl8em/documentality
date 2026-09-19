---
title: "Phase 12 codifying — the detailed plan"
force: propose
verb: argue
intention: suasive
view: synchronic
provenance: { type: project, id: phase-12-codifying }
constitutive: no
concerns: [steering, operationalizing, writing, codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

Phase 11 hardened the tooling and left it unexplained.
This phase gives the tooling a shelf, closes the account Phase 11 opened and never paid, and makes the failure self-detecting so it cannot happen a third time.

## Why this phase exists

This is the second time, not the first.

[Phase 10's own closing README](../phase-10-schema/README.md) records catching itself mid-close: "a schema change that leaves `writing/frontmatter.md` describing the old model makes the product lie about itself, so the guidance was realigned with the schema" — an unplanned departure, named and fixed before the phase closed.

Phase 11 made a larger operational change — closed the frontmatter vocabulary, replaced the hand-rolled parser, moved the schema's source of truth from JSON to YAML, added referential integrity — and did not run that check.
Verified, not suspected:

- [`writing/frontmatter.md`](../../../writing/frontmatter.md), the user-facing spec (`audience: [user]`), never states the vocabulary is now closed, never says an optional field needs a rationale to exist, and still doesn't point at `schema/frontmatter-rules.yaml` as the real source of truth.
- [`steering/ARCHITECTURE.md`](../../../steering/ARCHITECTURE.md), the contributor-facing "why is it built this way," still says schema reconciliation *is* Phase 10 and never mentions Phase 11 — not the YAML/JSON split, not why referential integrity needed its own workstream.
  Its provenance map is stale even for `operationalizing`, adopted two phases earlier.
- [`steering/CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md) has no mention of `scripts/`, the gate, or how a maintainer extends any of it.
- Phase 11 closed with no `README.md` narrating what landed and why — every phase from 08 on has one — no consolidated closing changelog entry (four scattered T-task entries instead, the pattern every earlier phase avoided), and none of the three ADRs its own plan named as owed at close.
- `steering/roadmap.md` still tags Phase 11 *(next)*.

Twice is a pattern: the plan's workstreams and its verification checklist were both pure mechanism, so nothing in the process ever asked whether the mechanism got explained, and nothing caught its absence.

The immediate trigger for this phase: naming what shelf *should* have explained the tooling surfaced that [ADR-033](../phase-10-schema/operationalizing-function.md) already named the missing piece and never built it.
Its own chain diagram —

```text
theorising → operationalizing → structuring / writing → designing → IT tools
```

— has a fourth downstream link, "IT tools," that has never had a folder, a provenance owner, or an account of its own reasoning. `scripts/`, `schema/`, and the gate are real apparatus, argued nowhere, owned by no function. `operationalizing/view.md`'s own closing line says as much: the check that a coordinate holds "live[s] in the IT tools (the frontmatter linter) — not here."

## Workstreams

| # | Workstream | Output |
|---|---|---|
| **T1** | **Adopt `codifying`.** A seventh function, same shape as ADR-033: its own ADR, a `codifying/README.md` orient, and first fiches for apparatus that has never been argued in prose — the gate's architecture (why `check.py` sequences every check into one property, the thing Phase 09 built and nothing since has explained), the YAML-source/generated-JSON split, and referential integrity (why supersession must be symmetric, why a dangling pointer is a hard error). Update the function set everywhere it's enumerated: `foundation.md`, `CONTRIBUTING.md`'s shelving rule, `ARCHITECTURE.md`'s provenance map. | `codifying/` ADR + README + fiches, function set at seven |
| **T2** | **Close Phase 11's account.** The three candidate ADRs Phase 11's plan named at close and never wrote (closed vocabulary + reason-per-field; YAML-as-source/JSON-as-generated; unstarted-work-never-numbered), each checked against the ADR-032 tiering test; `phases/refoundation/phase-11-tooling-hardening/README.md` narrating what landed and why, on the model of Phase 10's; `writing/frontmatter.md` rewritten to state the vocabulary is closed and name `schema/frontmatter-rules.yaml` as the source of truth — a real paragraph, not a silent field-table edit; the roadmap row flipped and its `phase:` field bumped. | 3 ADRs, phase-11 README, reconciled `writing/frontmatter.md`, flipped roadmap |
| **T3** | **Make the gap self-detecting.** Both failures were the same shape: a change to `scripts/` or `schema/` landed with no paired change to anything a human reads for understanding, and nothing noticed. Extend `check.py` with a structural check: a diff touching `scripts/**` or `schema/**` and none of `writing/`, `structuring/`, `operationalizing/`, `codifying/`, `steering/ARCHITECTURE.md` fails the gate. This workstream is itself an act of codifying — the rule this phase argues for, applied to itself before the phase closes. | a paired-change gate check |

T1 before T2: writing Phase 11's backlogged ADRs is easier once the shelf they'd naturally reference (`codifying`) exists.
T3 last: it needs T1's shelf to name as an acceptable pairing, and it is the check this phase should itself be unable to fail.

## Verification / definition of done

- `codifying/`'s ADR is accepted and in the register; `codifying/README.md` plus the three named fiches exist.
- The function set reads seven wherever it's enumerated — grepped, not assumed.
- Phase 11's three candidate decisions each have an ADR, or an explicit written ruling that they don't clear ADR-032's bar — not silently dropped either way.
- `phases/refoundation/phase-11-tooling-hardening/README.md` exists; `steering/roadmap.md` marks both Phase 11 and Phase 12 correctly; `phase:` bumped to `12-codifying`.
- `writing/frontmatter.md` states the closed vocabulary and points at `schema/frontmatter-rules.yaml`.
- The paired-change check exists and is demonstrated failing on a synthetic scripts-only diff, then passing once a docs file is added to it.
- `python3 scripts/check.py` is green.

## Explicitly out of scope

- **The Phase-II design** — still the next era, not this phase.
- **Rewriting any already-closed phase's frozen records** — supersede, never edit; Phase 11's gaps are filled forward, not corrected in place.
- **`distance`/`power` value sets, the shape of `concerns`** — still genuinely open per `schema/frontmatter-rules.yaml`'s own `still_open` list; this phase does not rule on them.

## Candidate records

Two decisions here install standing obligations and earn an ADR under the ADR-032 test, named now rather than assumed: **`codifying` is adopted as the seventh function**, and **a mechanism change without a paired documentation change fails the gate**.
Phase 11's three backlogged decisions belong to Phase 11's own provenance and are written under its project id even though this phase is what writes them.
