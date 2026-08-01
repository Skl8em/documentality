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
status: done
---

Phase I's refactor phase: bring the product and the source into the refounded vocabulary, and make the source the producer's shelf.

What landed:

- the **producer shelf** — `docs/` dissolved into `steering/` + `imagining/` + root `phases/`, root axis `provenance` / dominant `contributor` (ADR-024, enacting ADR-018);
- the **govern model** — a govern-document is classed by the *domain it governs*, not by its register; `steering` is the activity whose domain is the project itself; the transversal/vertical governance tension is named as irreducible and given a procedure and a `concerns` coordinate (ADR-025);
- the **floor value** — the perlocution/intention floor is `state`, not `none` (ADR-026);
- the **gerund naming rule** — function folders and `provenance.id` take the gerund form; `theory→theorising`, `write→writing`, `structure→structuring`, `imagine→imagining` (ADR-027);
- the **refounded vocabulary** — `perlocution → intention` (floor + aim), forces as recognized cells, know/do/govern as a register gloss, `recommend`/`entail` as extensions, the machine as the recipient relation at its limit — carried across `writing/` and `structuring/`;
- the **nine forces** migrated from `_legacy/` (all twelve now built), `_legacy/` retired, `structuring/applied.md` retired, `steering/open-questions.md` added, `phases/` grouped physically by era, and the `theory` nested repo absorbed via a history-preserving subtree merge.

Verification: `scripts/linkcheck.py` reports zero broken relative links; no live document carries the v3 `perlocution` field. The two schema forks it surfaced (coarse-vs-fine `intention`, stored-vs-derived `register`) are tracked in [`../../../steering/open-questions.md`](../../../steering/open-questions.md) and routed to Phase 09.

- [workstreams.md — the nine workstreams A–I (plan and execution)](workstreams.md)
- [ADR-024 — producer shelf: dissolve `docs/`, provenance at root](ADR-024-producer-shelf.md)
- [ADR-025 — govern by domain governed; the transversal/vertical tension and the `concerns` coordinate](ADR-025-governance-axis.md)
- [ADR-026 — the perlocution/intention floor value is `state`, not `none`](ADR-026-floor-value-state.md)
- [ADR-027 — function folders and provenance ids take the gerund form](ADR-027-gerund-naming.md)
