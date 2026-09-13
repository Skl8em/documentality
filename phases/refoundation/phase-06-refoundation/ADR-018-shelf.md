---
title: "ADR-018 — Source shelf vs generated surface; the catalogue is the pivot"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-06-refoundation }
constitutive: yes
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:fdb771359b24760da4ff773250424d714b3016eb1bf51e1994083fc59817134d
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

We had kept trying to make one folder tree serve both the reader's browsing and the producer's maintenance.
Before computing, the tree *was* the reader's shelf; the two could not be separated.
They can now: the theory says the **shelf** gives each item one place, while the **catalogue** (the frontmatter) exists to *generate* readable surfaces.
So one source can carry several generated reading surfaces.

## Options considered

- One hand-built tree serving both — consequence: the contortion we kept hitting.
- Source = the producer's shelf; the reader's surface = generated from the catalogue — consequence: each is organized for its own community, and the frontmatter becomes the single pivot (and the Phase-II machine interface).

## Decision

The source folder tree is the **contributor/producer's shelf**, organized by our ways of working, one place per item.
The user's reading surface is **generated** from the catalogue, ordered by functions served, and may re-order the source freely.
The catalogue is the single pivot.

## Entail — what follows

This refines ADR-010: its "scope axis (write/structure), dominant = user" described a *generated surface*, not the source.
The physical reorg of the source around the producer is deferred to Phase 08 (approach a).
Because contributor = user here, the source shelf serves as an acceptable reading surface for now, so surface generation waits for Phase II.
