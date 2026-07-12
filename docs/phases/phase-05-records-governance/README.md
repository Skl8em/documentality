---
title: "Phase 05 — Records & governance"
force: orient
verb: situate
perlocution: locate
view: diachronic
provenance: { type: project, id: phase-05-records-governance }
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

Fixed how the system records its *own* construction. Decision records were being piled by force in one `decisions/` folder — the very subject-classification the theory rejects. They are now grouped **by phase** (provenance), with a central register (`ADR.md`) for the act and a permanent `steering` function above the bounded phases. This phase also extended the theory: `decide` gained a forward **`entail`** face.

- [ADR-011 — `decide` gains an `entail` face](ADR-011-entail-face.md)
- [ADR-012 — group decisions by phase; `steering`; the register](ADR-012-decisions-by-phase.md)
