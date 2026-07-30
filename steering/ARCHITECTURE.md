---
title: "Architecture of the documentation system"
force: explain
verb: illuminate
perlocution: model
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This explains how the repository is laid out and *why* it is shaped this way, so a contributor can change it without breaking its logic. If you only want to *use* the system, read the product (`../write/`, `../structure/`) instead; this is about the repo as a maintained artifact.

> **Note (Phase 07).** The shelf is now **provenance-first**: one folder per function — `theory/`, `write/`, `structure/`, `steering/`, `imagine/` — plus the frozen `phases/`, which **dissolves the earlier `docs/` tree** and the "scope / two dominant communities" framing kept below. The current derivation is [`../phases/phase-07-structuring-tutorial/self-application.md`](../phases/refoundation/phase-07-structuring-tutorial/self-application.md); the v3 rationale in the rest of this file is retained until the Phase-08 vocabulary refactor.

## The question this answers

Why is a documentation *system* itself split into `write/`, `structure/`, and `docs/`, with forces nested under three doors — rather than a flat set of guides?

## The model: the repo eats its own theory

The system's core claim is that a document is an **act** with a **force**, and that naming the force generates the writing. The repo applies that claim to itself, which forces three structural decisions:

1. **Product vs. project-docs (two dominant communities).** The *content* is a product for **users** (people documenting their own projects). The repo's *own* documentation — this folder — is for **contributors**. Two communities cannot share one shelf axis, so they are two trees. See [`ADR-010`](../phases/naive-sketch/phase-04-disentanglement/ADR-010-product-vs-docs.md).

2. **Product axis = scope.** The product cuts into `write/` (one document) and `structure/` (the whole corpus). Everything about producing a single artifact — its force, phrasing, and frontmatter — is in `write/`; everything about the collection — topology, provenance, life cycle, audience-as-dominant-community, export — is in `structure/`.

3. **Forces grouped by door.** The twelve forces are not a flat list; they sit in `write/forces/{know,do,govern-and-record}/`, each as a folder with a stance (`README.md`, an `explain`) and a skeleton (`template.md`, an `instruct`). See [`ADR-007`](../phases/naive-sketch/phase-03-reorganization/ADR-007-fractal-reorg.md).

## The metadata backbone

Every file carries frontmatter (`../write/frontmatter.md`): `force`, `perlocution`, `view`, `provenance`, `audience`, `reader`, `status` are required. Derivable facts (door, direction of fit, diataxis) are **generated, never stored**. Tree roots additionally carry `axis` and `dominant-community`. This is what will let a validator and, later, a writing AI operate on the corpus.

## Provenance map (how this repo is owned)

| Area | provenance |
| --- | --- |
| root `README.md` | function `steering` (served: onboarding) |
| `theory/**` | function `theory` |
| `write/**` | function `writing` |
| `structure/**` | function `structuring` |
| `steering/**` governance (`foundation`, `roadmap`, `ARCHITECTURE`, `CONTRIBUTING`, `CHANGELOG`, `ADR.md` register) | function `steering` |
| `imagine/**` | function `imagine` (Phase II, parked) |
| `phases/<phase>/**` (records) | project `phase-NN` (frozen) |

## The legacy folder

`_legacy/` holds the previous flat version (`writing.md`, `structure.md`, the old `templates/`). It is kept only as the source for migrating the nine not-yet-built force folders, and will be deleted once migration completes. Do not link into it from the product.

## In short

The repo is the theory applied to itself: a product for users (split by scope into write/structure, forces by door) plus a separate `docs/` for contributors (split by genre), with provenance naming the maintaining function and every design choice frozen as an ADR.
