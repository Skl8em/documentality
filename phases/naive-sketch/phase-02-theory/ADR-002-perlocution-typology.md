---
title: "ADR-002 — perlocution as an open typology; prove and decide are convince"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: phase-02-theory }
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

The original schema had a boolean `formative: true|false` (does the act aim to change the reader). It was too coarse: it lumped "reshape the reader's map" (orient), "…model" (explain), "…competence" (teach) into one bit, and it left the persuasive force of `justify` unnamed.

## Options considered

- **Keep the boolean** — consequence: cannot distinguish the kinds of reader-change; the verb alone carries the nuance, invisibly.
- **Enrich `formative` into an enum but keep `prove` non-formative** — consequence: cleaner, but denies that a dossier aims to convince.
- **A `perlocution` typology parallel to `force`, and fold `prove`/`decide` into a `convince` value** — consequence: names each reader-change; a mild but honest revision of the core.

## Decision

Replace `formative` with `perlocution ∈ {none, locate, model, enable, convince}`, an open saturated list parallel to `force`. `orient→locate`, `explain→model`, `teach→enable`, `prove`/`decide`→`convince`, all others `none`.

## Entail — what follows

- `prove` and `decide` are reclassified as perlocutionary (their convince-aim is instrumental, but real).
- The perlocution↔force pairing is constrained and machine-checkable, with one sanctioned drift: a postmortem under verb `diagnose` may be `account` + `model`.
