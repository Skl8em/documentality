---
title: "Phase 08 — Refactor to the refounded vocabulary & the producer shelf"
force: orient
register: know
intention: locate
view: diachronic
provenance: { type: project, id: phase-08-refactor }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: in-progress
---

Phase I's refactor phase: bring the product and the source into the refounded vocabulary, and make the source the producer's shelf.

What has landed so far:

- the **producer shelf** — `docs/` dissolved into `steering/` + `imagine/` + root `phases/`, root axis `provenance` / dominant `contributor` (ADR-024, enacting ADR-018);
- the **govern model** — a govern-document is classed by the *domain it governs*, not by its register; `steering` is the activity whose domain is the project itself; the transversal/vertical governance tension is named as irreducible and given a procedure and a `concerns` coordinate (ADR-025).

What remains: refound the v3 vocabulary (perlocution → intention floor, force cells, know/do/govern gloss) across `write/` and `structure/`; migrate the nine `_legacy/` forces and retire `_legacy/`; retire `structure/applied.md`; add `steering/open-questions.md`; group `phases/` by era; reconcile the naming mismatch (`write/`↔`writing`, `structure/`↔`structuring`).

- [ADR-024 — producer shelf: dissolve `docs/`, provenance at root](ADR-024-producer-shelf.md)
- [ADR-025 — govern by domain governed; the transversal/vertical tension and the `concerns` coordinate](ADR-025-governance-axis.md)
- [ADR-026 — the perlocution/intention floor value is `state`, not `none`](ADR-026-floor-value-state.md)
