---
title: "ADR-015 — Perlocution has no zero; forces are recognized cells"
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
supersedes: ADR-002-perlocution-typology
superseded-by: null
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

We modelled perlocution as a value welded to each force, with `none` for the served case.
The refoundation shows both moves are wrong.
Every inscription carries a **constitutive floor** — it poses its content as the world and silences what it omits — so there is no zero; "served" means *no intention above the floor*, never "reader untouched".
And force and perlocutionary intention are **largely independent**, so the named forces are not primitives but **recognized cells**: conjunctions of a direction of fit with an intention, reified into genres.

## Options considered

- Keep `perlocution` as a per-force value with a `none` — consequence: denies the floor, welds axes that are independent.
- Model the floor as universal and the intention as a separate, open axis (formative / suasive / affective) — consequence: truer to the theory, and it makes our old "open pairings" rule (ADR-013) a *consequence*, not a patch.

## Decision

`perlocution` is replaced by two things: a **constitutive floor** that every document carries, and an **intention** above it, one of `formative` / `suasive` / `affective` (or none-above-floor).
Forces are recognized cells, not a flat repertoire.

## Entail — what follows

The frontmatter schema drops `perlocution: none|locate|model|enable|convince` for the floor-plus-intention model; reconciled in Phase 09.
ADR-013 (open pairings) is reframed: pairings are open *because* the axes are independent, not because a constraint was relaxed.
`prove` and `decide` keep their suasive intention, now grounded rather than stipulated.
