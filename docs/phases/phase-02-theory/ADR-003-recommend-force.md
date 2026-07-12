---
title: "ADR-003 — Add recommend as the twelfth force"
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

The repertoire had `instruct` (neutral steps) and `mandate` (binding rule) but nothing between them for *non-binding advice* — best-practices, guidelines, style suggestions. That is a real, common genre with a distinct move structure and failure mode.

## Options considered

- **Fold advice into `mandate` with a deontic flag** (`binding: must|should`) — consequence: economical, but hides a distinct stance and its own failure modes in a parameter.
- **Fold advice into `explain`** — consequence: loses the actionable, directive character.
- **Add `recommend` as a distinct force** (verb *advise*) — consequence: completes the deontic gradient `instruct → recommend → mandate`, at the cost of a twelfth entry.

## Decision

Add `recommend` (verb *advise*, `perlocution: none`) as the twelfth force, in the `do` door, on the gradient *here is how* → *you should* → *you must*.

## Entail — what follows

- The repertoire is twelve, not eleven — still "saturated, not closed."
- Its symmetric failure modes are named: hardening into `mandate` (false obligation) or dissolving into `explain` (advice with no actionable form).
