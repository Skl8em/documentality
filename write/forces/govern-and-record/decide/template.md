---
title: "ADR-<NNN> — <decision title>"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: <phase-or-project-id> }
audience: [decider, contributor]
reader: H+M
distance: near
power: none
status: stable
retention: permanent
supersedes: <ADR-XXX or null>
superseded-by: null
---

<!--
TEMPLATE — force `decide` (three faces: enact / justify / entail). Stance: ./README.md
- enact: the one-line act belongs in the central register (e.g. steering/ADR.md), not here.
- justify (this record, backward): motivate from context + options. Write for a reader who
  does not yet agree. Fail = record the verdict, discard the reasoning.
- entail (this record, forward): unfold what the decision changes/commits/requires. Write it
  as defeasible (the future does not accumulate). Fail = leave implications implicit.
Dated-fixed: NEVER edit to reflect a later choice; a superseding decision is a NEW record.
-->

## Status

<proposed | accepted | superseded by ADR-YYY> — Date: YYYY-MM-DD

## Context and forces in play *(justify — backward)*

<The situation, the constraints, the tensions to arbitrate.>

## Options considered

<The options GENUINELY considered, treated fairly. Without them this is an assertion, not a justification.>

- **Option A:** … — consequences: …
- **Option B:** … — consequences: …

## Decision

<The choice, in one line. Then: why this one rather than the others.>

## Entail — what follows *(forward)*

<What the decision changes, commits us to, and requires going forward. Name the downstream
`mandate`/`commit`/`instruct` it spawns, or the `propose` it reopens. Write as projection, not proof.>
