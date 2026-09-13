---
title: "ADR-020 — Scope Phase I; defer and re-found Phase II"
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
hash: sha256:60ba27790a232817dc29762214cc96cacd1d9ed40cb1b3eabc7f4669f1fa57ac
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

The system has two horizons: an operational system (Phase I) and a computational model — AI instructions, hooks, generation (Phase II).
Phase II is not a mere continuation.
It brings a genuinely new discourse community — the AI's technical baggage — with its own functions, governance, and maintenance, which we cannot specify well before Phase I is done.

## Options considered

- Plan Phase II now — consequence: planning a community and functions we do not yet understand.
- Name Phase II, build only Phase I, and design Phase II later — consequence: honest sequencing; the front-end is re-run for the new community when we can see it.

## Decision

Current work is restricted to **Phase I**.
Phase II is named but only **designed at Phase 10**, once Phase I is complete, by re-running the structuring front-end for the AI discourse community.

## Entail — what follows

The roadmap stops committing content past Phase 10; the computational model itself is left blank until its design phase.
Phase I keeps the frontmatter clean and machine-readable so it *can* become the Phase-II interface, without yet being one.
