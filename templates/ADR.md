---
title: "ADR-<NNN> — <decision title>"
force: decide
verb: justify
formative: false
view: diachronic
provenance: { type: project, id: <project-id> }
distance: near
power: none
audience: [developer, architect, AI]
status: stable
retention: permanent
supersedes: <ADR-XXX or null>
superseded-by: null
---

<!--
TEMPLATE — force `decide` (verb: justify). See writing.md §I > Decide.
Stake: the REASONING, not the verdict. The decision is one line; the whole value is the
record of WHY, for a future reader (you included) when the context is forgotten.
Failure: recording the verdict and discarding the reasoning (the log that's useless once
anyone asks why).
SPECIAL PROPERTY: dated-fixed. NEVER edit it to reflect a later choice; a decision that
supersedes another is a NEW ADR (fill `supersedes`/`superseded-by`).
Write to be read by someone who does not yet agree.
-->

## Status

<proposed | accepted | superseded by ADR-YYY> — Date: YYYY-MM-DD

## Context and forces in play

<The situation and the constraints that bear on it. The tensions to arbitrate.>

## Options considered

<The options GENUINELY considered, treated fairly. Without them, this is not a justification
but an assertion.>

- **Option A:** … — consequences: …
- **Option B:** … — consequences: …

## Decision

<The choice, in one line. Then: why this one rather than the others.>

## Consequences accepted

<What this choice implies, including the UNWELCOME consequences you accept.>
