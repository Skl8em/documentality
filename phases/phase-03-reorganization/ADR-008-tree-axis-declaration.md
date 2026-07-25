---
title: "ADR-008 — Declare axis and dominant-community at each tree root"
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

The rule "the shelf's axis serves a dominant community" existed, but nowhere did our own repo *state* its axis, and the rule did not say *where* the declaration should live. A reader could not find the answer, and a reviewer could not check it — a dog-fooding gap caught in review.

## Options considered

- **Prose only, no fixed location** — consequence: unfindable and unenforceable (the original defect).
- **Prose in the root README under a fixed heading** — consequence: findable by humans (the README is always the front door), but not machine-checkable.
- **Prose + frontmatter fields `axis`/`dominant-community` on the tree root** — consequence: findable *and* validatable, at the cost of two fields that exist only on tree roots.

## Decision

Every tree declares its axis and dominant community in its **root orient document**, both as a self-naming prose section and as `axis`/`dominant-community` frontmatter — required on the tree root only, forbidden elsewhere.

## Entail — what follows

- Two root-only fields; a validator flags a root missing them or a non-root carrying them.
- Nested trees (e.g. `docs/`) each carry their own declaration, making multiple dominant communities in one repo explicit.
