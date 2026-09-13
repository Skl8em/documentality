---
title: "ADR-022 — Front-end correction: functions first, distance per community, mutable groupings & eras"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-07-structuring-tutorial }
constitutive: yes
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:3dad4da06b8024e42ad26a3f73e2ba9045b4907b947e2a195f37211d958eb7f3
---

## Status

accepted — 2026-07-21

## Context and forces in play *(justify)*

The first structuring tutorial, and the foundation behind it, put communities before functions and asked "what does the project do *for its readers*."
That presupposes the reader, imposes one project's decomposition, and never reaches placement.
Three corrections follow from the refounded theory.
First, a project *touches* things, and each thing mobilizes a body of knowledge — a discourse community; who reads what is *derived* from that, not given.
Second, "novice" is relative to a community, so `distance` is per discourse community (per domain), not one beginner/initiated axis: a reader can be initiated in code and novice in biology.
Third, both the function set and the provenance grouping are mutable — refined or coarsened as understanding matures — and a coarse grouping gives a far better overview than many microscopic ones.

## Options considered

- Keep communities-first with a single distance axis — consequence: presupposes the reader, hides that audiences are domain-relative, imposes a shape.
- Functions first, communities and per-community distance derived, groupings kept coarse and re-groupable — consequence: fits the theory (Swales' discourse community; Simon's near-decomposability applied to the classification itself) and finally reaches placement.

## Decision

Lay the **functions flat first** — what the project touches and the knowledge each mobilizes — and **derive the communities** and their **per-community `distance`** from them.
Treat the function and provenance groupings as **mutable**: refine or coarsen them as understanding matures.
Adopt **three macro-eras** over our micro-phases — *naive sketch* (01–05), *refoundation* (06–09), *phase II* (later) — the era being the coarse orient of the record.

## Entail — what follows

The structuring tutorial is rewritten functions-first, reaching placement (source by provenance; surface by functions served).
`foundation.md` is reconciled: functions before communities, `distance` per community, provenance clarified (a function *is* a provenance; `synchronic ⇒ function`, `diachronic ⇒ its producer — a project or a function's change-stream`), groupings re-groupable.
This refines ADR-017 (distance is per-community, not a single axis) and ADR-012 (phases nest under eras).
The physical era-folders wait for Phase 08; for now the eras are a coarse map in `phases/README.md`.
