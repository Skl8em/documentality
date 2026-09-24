---
title: "Decision — unstarted work is never referred to by number"
id: 01M39G4WWKHK6MP1MTM06BKPH8
slug: unstarted-work-unnumbered
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-11-tooling-hardening }
constitutive: yes
concerns: [steering]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:2296c87106c2482c207c91d0c7232ed7760b4baff17b88d411aee9ba92c471e9
---

## Status

accepted — 2026-09-24, recording a decision Phase 11's insertion took on 2026-09-13 (`plan: insert Phase 11 (tooling hardening); stop numbering unstarted phases`) and stated only in the roadmap and the changelog.
Written by [Phase 12's T2](../phase-12-codifying/plan.md), so it carries Phase 11's provenance and a later date.
It clears the [ADR-032](../phase-10-schema/adr-tiering.md) test, and it is the thinnest of the three records Phase 11 owed: the obligation is real, and nothing but attention enforces it.

## Context and forces in play *(justify)*

The roadmap numbered every phase it named, including the ones it had not begun.
Inserting a phase ahead of a numbered one moves the number, and every forward reference that named it goes stale.
That had happened twice: the Phase 09 insertion renumbered the schema and Phase-II-design phases to 10 and 11, and the Phase 11 insertion moved a forward reference a second time.
Each time the repair was a sweep across the README, the phase index, the roadmap and the plans.

The sweeps were the symptom.
The cause was giving unstarted work an ordinal it could not keep, because the ordinal encodes a *position*, and a position is exactly what an insertion changes.

The register had already made this move for decisions.
[ADR-028](../phase-09-tooling/ulid-identifiers.md) separated a record's identity, a ULID that never changes, from its ordinal, a generated display label that may.
Phases had no such separation, so their number did both jobs.

## Decision

1. **Work not yet begun is named and ordered, never numbered.**
   The roadmap says what follows what; a forward reference is to the work by name (*the deployment phase*, *the Phase-II design*), never by the number it might later take.

2. **A phase takes its number when it is tackled, not before.**
   The ordinal is assigned at the moment work starts, when its position is settled and no insertion can move it.

3. **A numbered phase keeps its number.**
   A frozen record from an earlier phase keeps the number it had in its own time; a later renumbering never edits it.

## Entail — what follows

- Inserting a phase ahead of unstarted work moves nothing: the unstarted work carries no number to invalidate.
- The roadmap, the phase index, the README's status paragraph and every plan refer to a future phase by name.
  A stale forward number is a defect to correct, not a convention to keep.
- A phase that has been named but not begun is *unnumbered* in every table it appears in, and takes its number in the same change that starts it.
- **Not decided here:** what a phase is called once it has a number, or how the era folders group it; the convention concerns forward references only.

## Honest limit

This is the only one of the three Phase 11 decisions that no check enforces.
The gate reads frontmatter, links, identifiers and seals; a sentence that says "Phase 13 will …" of work nobody has begun passes it.
The rule holds by attention, so it can be broken silently, and it will be exactly when a contributor is in a hurry.

The evidence that it works is one insertion.
Phase 12 went in ahead of the still-unnumbered Phase-II design with a new roadmap row, a plan, a changelog entry and a single-line `phase:` change, and no sweep across forward references.
That is what the rule predicts.
It is a sample of one, by the party that made the rule, and it says nothing about an insertion ahead of work that already carries a number.

Naming without numbering has a cost the record does not hide: a reader cannot say where an unnumbered phase falls without reading the roadmap's order, and "the deployment phase" is less compact than a digit.
The trade is deliberate, the price of not sweeping, and it has not been tested against a reader who dislikes it.
