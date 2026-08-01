---
title: "ADR-006 — Audience = roles × reader flag; audience lives in structure"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: phase-03-reorganization }
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

accepted — 2026-07-11

## Context and forces in play

Audience was underspecified — a flat list mixing human roles and "AI". We needed a model generic enough to apply to any project, and a home for it in the tree.

## Options considered

- **One flat list including `AI`** — consequence: conflates *who* (role) with *what kind of reader* (human/machine).
- **Two orthogonal axes: role × reader kind** — consequence: expressive; roles align with the three doors, the reader flag reconnects to the H/M/H+M patterns.
- **Place the audience model in `write/` (register) vs `structure/` (dominant community)** — the dominant-community decision that orders the tree is structural.

## Decision

Audience has two orthogonal fields: `audience` = generic roles `{user, contributor, decider}` (project-refinable), and `reader ∈ {H, M, H+M}` (agent sub-kinds only when needed). The audience model document lives in **`structure/`**, because choosing whom the corpus serves is a structural (communication-system) decision; `write/` only consumes it for register.

## Entail — what follows

- Two fields instead of one; both required on non-ephemeral docs.
- `distance`/`power` remain separate (they set scaffolding/armor); audience answers *who*, not *how much*.
