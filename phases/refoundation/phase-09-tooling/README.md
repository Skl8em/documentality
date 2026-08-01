---
title: "Phase 09 — Tooling: enforce the conventions, ready the catalogue"
force: orient
register: know
intention: locate
view: diachronic
provenance: { type: project, id: phase-09-tooling }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

Phase I's tooling phase: stand up the machinery that **enforces the conventions we have already decided** and makes the schema work of Phase 10 efficient and meaningful.
It is deliberately placed *before* the schema reconciliation: the lint harness built here is what Phase 10 fills in.

Three parts (detailed in [`plan.md`](plan.md)):

1. **Unified markdownlint** — one ruleset shared by the CLI and the VSCode (David Anson) extension: title in the frontmatter (never `# …`), the semantic-line-break rule (ADR-021), and a deliberate take-over of the default markdownlint rules.
2. **Frontmatter linting (a safe starter)** — a validator harness that checks only the *settled* invariants now, as examples; the contested schema questions are left for Phase 10 to fill into the same harness.
3. **ULID + slug identifiers** — replace the sequential counts (`ADR-NNN`, `phase-NN`, …) with a ULID plus a human slug, with tooling to mint and to verify them.

Everything is wired into one aggregated check (the phase-close gate), a pre-commit hook, and CI.
Markdownlint runs on Node (the shared engine with the editor); our own validators stay Python (per [`../../../scripts/`](../../../scripts/) and the project's validation-tooling convention).

- [plan.md — the detailed plan](plan.md)

Status: **planned** (next after Phase 08).
No decisions are frozen yet; the open forks are named in the plan.
