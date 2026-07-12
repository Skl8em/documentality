---
title: "ADR-009 — Add a teach on-ramp; enforce obligations by validation, not reading order"
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

Two questions surfaced in review. (1) The split files were being read as a sequence explain→instruct→recommend→mandate, which the system does not intend — they are routed by need. (2) A newcomer who does not yet know their need is served by neither `explain` nor a menu; and putting `mandate` last risks it being skipped (F-pattern, progressive disclosure, lost-in-the-middle).

## Options considered

- **Reorder so mandate comes first** — consequence: fights the exposition logic and still relies on reading order.
- **Add a `teach` entry, and stop relying on order**: surface obligations in context (templates, links) and enforce them by validation — consequence: a newcomer on-ramp plus a real enforcement path.

## Decision

Add a root `tutorial.md` (`teach`, `perlocution: enable`) as the newcomer on-ramp. State everywhere that the split files are entry points routed by need, not a sequence. Make obligations independent of reading order: they are surfaced in the templates a writer fills and enforced by frontmatter validation.

## Entail — what follows

- The meta-system gains the one door it lacked (`teach`).
- Compliance no longer depends on anyone reading `rules.md` in order — the backstop is the validator.
