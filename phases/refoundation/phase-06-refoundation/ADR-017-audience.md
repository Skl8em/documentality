---
title: "ADR-017 — Audience: roles collapse, distance is the live axis, human/machine orthogonal"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-06-refoundation }
constitutive: yes
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: ADR-006-audience-model
superseded-by: null
hash: sha256:fec2743f8139a1dc0a60e759989b8db8b0878785b4bce02516b7ae7bd2f22b6a
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

ADR-006 gave audience two axes: generic roles (user / contributor / decider) and a reader flag (H / M / H+M).
For *this* project that model over-fits.
The user and the contributor are one discourse community — same code, same language — so the role split has almost nothing to arbitrate here.
What actually varies is familiarity with the theory, which is `distance` (shared code), not a role.

## Options considered

- Keep the full role model — consequence: three roles that barely differ for a tight one-person community.
- Foreground `distance` (beginner / initiated) and keep human/machine as an orthogonal flag — consequence: fits the real variation, and matches the refoundation's treatment of the machine as the recipient relation at its limit, not a role.

## Decision

For this project the roles collapse.
The live axis is `distance` — **beginner vs initiated** (how much theory background to spell out).
Human vs machine is **orthogonal**: the machine may hold the *function* of user or contributor but never decider, and "being a machine" is a separate flag, not a role.

## Entail — what follows

Our documents foreground `distance`; a beginner-facing doc explicates concepts, an initiated-facing one presumes them.
The general product still offers the full role model to the projects that adopt it — this decision is scoped to *our* corpus.
Phase II will introduce a genuinely new discourse community (the AI's technical baggage); that is a Phase-II front-end, not this one.
