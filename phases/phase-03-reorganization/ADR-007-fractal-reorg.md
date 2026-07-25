---
title: "ADR-007 — Self-similar reorganization: write/ + structure/, forces by door"
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

The flat version crammed explain + instruct + recommend + mandate into single files (`writing.md`, `structure.md`), violating the system's own "one force per file" rule. The system did not eat its own dog food, and a reader could not route by need.

## Options considered

- **Keep two big guides** — consequence: simplest to write, but self-contradictory and hard to navigate.
- **One flat folder of twelve force files** — consequence: no self-similarity; twelve peers with no grouping.
- **A self-similar tree**: each area split by the forces it needs, forces grouped under three doors — consequence: more files, but the repo becomes a worked example of its own theory.

## Decision

Reorganize into `write/` and `structure/`, each split into `explain`/`instruct`/`recommend`/`mandate`/`describe` as needed, with the twelve forces as folders under `write/forces/{know,do,govern-and-record}/`, each folder holding a stance (`README.md`) and a template.

## Entail — what follows

- ~25+ files instead of a handful; migration of nine forces is staged from `_legacy/`.
- The tree itself is now the primary demonstration of the theory (`structure/applied.md`).
