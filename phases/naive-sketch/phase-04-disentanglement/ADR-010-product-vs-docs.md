---
title: "ADR-010 — Disentangle the product (users) from docs/ (contributors); axis = scope; provenance by function"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: phase-04-disentanglement }
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

The repo conflated three distinct things. (1) Its **core output** — guidance for people documenting their own projects — with its **own internal docs** (how this repo is built and maintained). (2) The audience: the README called the content's dominant community `contributor` when the content is for **users**; contributors are the people who write *in this repo*. (3) Provenance: 23 of 25 files carried the identical `{ function, doc-system }`, so provenance distinguished nothing.

## Options considered

- **Leave it self-contained and uniform** — consequence: contributors' concerns leak into the product; audience mislabelled; provenance dead.
- **Disentangle** the product from a `docs/` folder, correct the audience, and make provenance name the maintaining function — consequence: more structure, but each of the three problems is fixed and the result is a live example of two dominant communities in one repo.

## Decision

1. **Product vs docs.** `write/` + `structure/` are the product, for **users** (dominant-community `user`). A new `docs/` holds the repo's own internals (ARCHITECTURE, CONTRIBUTING, CHANGELOG, decisions) for **contributors/deciders** (dominant-community `contributor`) — a separate nested tree, shelved by genre.
2. **Axis = scope.** The product's axis is scope: `write/` = one document, `structure/` = the whole corpus. It does not propagate into `docs/`.
3. **Provenance by function.** Ids name the maintaining function: `onboarding` (root, tutorial), `writing` (write/**), `structuring` (structure/**), `maintenance` (docs/**); ADRs are the `v3-redesign` **project**, frozen.

## Entail — what follows

- Audience across the product flips to `user`; `docs/` is `contributor`/`decider`.
- Provenance becomes queryable, and `docs/decisions/` visibly shows shelf ≠ provenance (an ADR is shelved in `docs/` but owned by the `v3-redesign` project).
- The design history of the system is now itself documented, as this set of ADRs.
