---
title: "ADR-012 — Group decision records by phase; steering function; central register"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: phase-05-records-governance }
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
supersedes: null
superseded-by: null
written-at: v3
valid-for: v3
---

## Status

accepted — 2026-07-12

## Context and forces in play *(justify — backward)*

The previous `docs/decisions/` folder held all ADRs together. That is **classification by force** (all `decide` in one pile) — precisely the subject-style filing the system rejects in favour of **provenance** (traces of the same activity belong together). A proposal, the decision it triggers, and the account of what it delivered are one effort; scattering them by genre hurts discovery. Separately, tagging every ADR `project: v3-redesign` was version-centric and wrong: each construction effort is its own bounded project, while the *responsibility* for governing the design is permanent.

## Options considered

- **Keep the flat `decisions/` pile** — consequence: force-classification, poor for discovery, contradicts our own rules.
- **One `project` id for all decisions** — consequence: provenance distinguishes nothing.
- **Group by phase (bounded projects) under a permanent `steering` function, plus a central register** — consequence: provenance done right; a decision reads with its effort; the register still gives the global act view.

## Decision

Decision records are grouped **by phase** in `docs/phases/<phase>/`, each phase a `project` (frozen). A permanent **`steering`** function owns the maintained governance docs (`ARCHITECTURE`, `CONTRIBUTING`, `CHANGELOG`) and the central register **`ADR.md`** — the *act* face that lists every decision in one line. Motivation (`justify`) and implications (`entail`) live in the phase record, not the register.

## Entail — what follows

- The ten existing ADRs move into their phase folders; their provenance becomes their phase project.
- `ADR.md` (register) and `phases/README.md` are added; the old `decisions/` folder is deprecated with a redirect (superseded, not erased).
- Shelf ≠ provenance becomes visible: a record is shelved in `docs/phases/…` and owned by that phase project, while the maintained governance docs are owned by `steering`.
- New rule for contributors: a decision is appended to `ADR.md` **and** written in full in the current phase folder; no more flat decision pile.
- A future real project using this system gets the same pattern: phases co-locate propose/decide/account; a register lists the acts.
