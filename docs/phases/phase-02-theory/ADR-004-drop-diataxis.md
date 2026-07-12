---
title: "ADR-004 — Drop the diataxis field; derive it from force × perlocution"
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

Early frontmatter carried a `diataxis` field (`tutorial|how-to|reference|explanation`). But the theory re-derives Diátaxis exactly as `direction-of-fit × perlocution` for the know/do doors. Storing it duplicates a fact `force` already fixes.

## Options considered

- **Keep `diataxis`** for familiarity — consequence: two sources of truth that can disagree; extra field to validate.
- **Drop it and generate it** — consequence: one source of truth; readers who want the Diátaxis label get it computed.

## Decision

Remove `diataxis` from the schema. Treat it (and `door`, and direction of fit) as **derivable views generated from `force`**, never stored.

## Entail — what follows

- The schema stays minimal; nothing derivable from `force` is stored.
- Tooling must generate the Diátaxis label when a project wants it. This established the general rule "store only hard coordinates that are not derivable from one another."
