---
title: "Construction phases, grouped into eras"
force: orient
register: know
intention: locate
view: synchronic
provenance: { type: function, id: steering }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: stable
---

The system was built in **phases**, each a bounded effort that closed, holding the records it produced — its decisions (with their `justify` and `entail`), and any proposals or accounts — together, because they are traces of one activity.
To understand *why the system is shaped as it is*, read a phase end to end; do not reassemble scattered decisions.
The one-line act of each decision is in the register, [`../steering/ADR.md`](../steering/ADR.md).

Phases are grouped into three coarse **eras**, because a coarse map reads far better than twenty microscopic records (ADR-022).
The era is the orient of the record; the micro-phases are the detail beneath it.
The eras are now **physical folders** — `phases/naive-sketch/` and `phases/refoundation/` (Phase II's folder waits for its first record) — grouped as below.

## Era 1 — Naive sketch *(closed)*

The first version, built before the theory was refounded and before the front-end was ever laid flat.

| Phase | What it settled | Records |
|---|---|---|
| [01 — foundation](naive-sketch/phase-01-foundation/README.md) | the inscribed-act reframe | ADR-001 |
| [02 — theory](naive-sketch/phase-02-theory/README.md) | perlocution, recommend, drop diataxis, verb | ADR-002…005 |
| [03 — reorganization](naive-sketch/phase-03-reorganization/README.md) | fractal tree, doors, axis declaration, teach, audience | ADR-006…009 |
| [04 — disentanglement](naive-sketch/phase-04-disentanglement/README.md) | product vs docs, scope axis, provenance by function | ADR-010 |
| [05 — records & governance](naive-sketch/phase-05-records-governance/README.md) | decisions by phase, steering, the `entail` face, open pairings | ADR-011…013 |

## Era 2 — Refoundation *(current)*

Regrounding the theory on Ferraris and, at last, laying the front-end flat.

| Phase | What it settled | Records |
|---|---|---|
| [06 — refoundation & front-end](refoundation/phase-06-refoundation/README.md) *(done)* | Ferraris refoundation; perlocution floor & cells; the front-end; source-vs-generated shelf; Phase-I scope | ADR-014…021 |
| [07 — structuring tutorial & front-end correction](refoundation/phase-07-structuring-tutorial/README.md) *(done)* | functions-first; distance per community; mutable groupings & eras | ADR-022, ADR-023 |
| [08 — refactor product & source](refoundation/phase-08-refactor/README.md) *(done)* | refounded vocabulary (intention floor, register gloss); producer shelf; nine forces migrated & `_legacy/` retired; gerund naming; eras made physical | ADR-024…027 |
| [09 — tooling](refoundation/phase-09-tooling/README.md) *(done)* | reproducible Nix devShell; unified markdownlint (CLI + VSCode) + corpus reflow; a frontmatter-lint harness (safe invariants); ULID + slug identifiers, minting/verify tooling, and a safe-rename script; one gate (pre-commit + CI) | ADR-028 |
| 10 — reconcile schema *(next)* | the frontmatter schema as the machine-ready catalogue, on the Phase-09 lint harness | — |

## Era 3 — Phase II *(later)*

The computational model — designed only once Phase I closes, for the new discourse community it brings.
Not yet begun (roadmap Phase 11 onward; its design is Phase 11).
