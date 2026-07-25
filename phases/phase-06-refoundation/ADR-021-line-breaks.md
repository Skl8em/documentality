---
title: "ADR-021 — Semantic line breaks (one sentence per line) in Markdown source"
force: decide
register: govern
intention: suasive
view: diachronic
provenance: { type: project, id: phase-06-refoundation }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

Markdown reflowed as full paragraphs makes `git diff` mark a whole paragraph changed when a single sentence moved.
The reviewer then cannot see, at a glance, where meaning actually changed.

## Options considered

- Reflow at a fixed column width — consequence: any edit reshuffles the wrap and pollutes the diff.
- One sentence per line (semantic line breaks) — consequence: a diff shows exactly the sentences that changed; rendering is unaffected, since Markdown joins adjacent lines into one paragraph.

## Decision

Markdown source is written **one sentence per line**.
Line breaks carry no rendered meaning; they exist for the diff.

## Entail — what follows

This convention applies to everything written in this repo from now on, including these records.
It is surface craft, so in Phase 08 it moves into the writing rules / `CONTRIBUTING`, not the theory.
A future formatter or hook may enforce it (Phase II).
