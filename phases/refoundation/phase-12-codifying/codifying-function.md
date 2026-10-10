---
title: "Decision — `codifying` is the seventh function, the account of the tooling"
id: 01M35RZS00B23QEMBV4ZC947QX
slug: codifying-function
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-12-codifying }
constitutive: yes
concerns: [steering, operationalizing, structuring, codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:c4b20f9544f3b925b3293a497427d87ef323cb7005881b85720537b0c1eead50
---

## Status

accepted — 2026-09-23.
Refines the function set of [ADR-033](../phase-10-schema/operationalizing-function.md) and completes the chain it drew; ADR-033 stands, its count of six is what this record moves to seven.
Written before the shelf it adopts, which is the order `CONTRIBUTING` requires and the reverse of ADR-033's.

## Context and forces in play *(justify)*

[ADR-033](../phase-10-schema/operationalizing-function.md) drew a chain and named its last link:

```text
theorising → operationalizing → structuring / writing → designing → IT tools
```

Every other link has a shelf.
"IT tools" has never had a folder, an owning function, or an account of why it is built the way it is.
`scripts/`, `schema/frontmatter-rules.yaml`, `docsys.yaml` and the gate that runs them are real apparatus, argued nowhere.
The operationalizing fiches defer to it by pointing: the check that a coordinate holds "live[s] in the IT tools … not here".
A pointer to a place that holds no explanation is a dead end.

The cost showed twice.
Phase 10 caught itself, mid-close, leaving the product describing an old model, and fixed it as a named departure.
Phase 11 made a larger change to the same apparatus — a closed vocabulary, a real YAML parser, a schema authored in YAML, referential integrity — and closed with none of it explained: no closing README, and none of the three ADRs its own plan named as owed.
The plan for this phase reads that as a pattern.
It is a pattern with a plausible cause, not a proven one: nothing in the process ever asked whether a mechanism got explained, and there was nowhere for the explanation to go.

Filing the account in an existing shelf fails, each in its own way.

- **`operationalizing`** explains why a *coordinate* was reified.
  Its orient fixes that a fiche stays conceptual and that "the *implementation* of that work lives with the IT tools, not here".
  Housing the gate's architecture there would turn a shelf about the corpus's conventions into one about a program.
- **`steering`** explains the repository's layout and the project's direction, for a reader who needs to change the *repo*.
  The tooling's reasoning is a different body of knowledge, read by a reader who must hold it before touching the code.
- **`writing` and `structuring`** are the product, addressed to someone documenting their own project.
  Nothing in them asks that reader to understand a YAML/JSON compile step.

The apparatus also has a boundary of its own, which the first two steps of this phase surfaced.
[`community-map.md`](community-map.md) found that explaining it means naming a second mobilised field — tooling engineering, beside the theory — and a reader who must be initiated in that field before acting, or a change corrupts the corpus silently.
[`engine-config-seam.md`](engine-config-seam.md) found that the tooling separates, by rate of change, into an engine, the methodology's schema, and this repository's instance.
A body of knowledge with its own reader, its own field and its own seam is what the other shelves already are.

## Decision

1. **`codifying` is adopted as a seventh function**, giving `theorising` · `operationalizing` · `writing` · `structuring` · `codifying` · `steering` · `imagining`.

2. **Its domain is the account of the apparatus that enforces the theory's coordinates**: `scripts/`, `schema/`, `docsys.yaml` and the gate — how each part is built, why it is built that way, and what it does not establish.
   The account, not the code.

3. **It takes the last link of ADR-033's chain**, in place of the name "IT tools".
   `designing` stays what ADR-033 left it, unadopted; this record does not rule on it.

4. **The code stays where it is.**
   `scripts/` holds executables and no frontmatter, and frozen records name its paths, so moving it would strand them.
   The function owns the code by provenance — `scripts/**`, `schema/**` and `docsys.yaml` are `codifying`'s — and shelves its account in `codifying/`, one folder at the root, gerund-named per ADR-027, with `provenance: { type: function, id: codifying }`.

5. **The boundary with `operationalizing` is by subject.**
   A document about a *coordinate or convention of the corpus* — what it means, why it was reified — is operationalizing.
   A document about a *mechanism that checks, generates or runs* — how the check works, why it is built so — is codifying.
   A fiche is not a decision, as ADR-033 said: the shelf's fiches are maintained and `synchronic`, the records that decide them frozen and `diachronic`.

6. **The fiches are written for the maintainer, and the gate's messages for everyone else.**
   Per [`community-map.md`](community-map.md): a gate-runner needs to fix a failure, and the failing message is the whole interaction, so no fiche serves them; a maintainer must know before acting, and the fiches are theirs.
   `maintainer` is the project's refinement of `contributor` for anyone whose distance is judged in the tooling-engineering field; it stays a project-local role, not a schema enumeration, and the fiches carry `audience: [contributor]`.
   A document says which field its `distance` is measured in whenever it is not the theory.

## Entail — what follows

- `codifying/` holds its orient and three fiches: the gate's architecture, the YAML-source/generated-JSON split, and referential integrity.
- The function set is seven wherever it is enumerated — `steering/foundation.md`, `CONTRIBUTING`'s shelving and provenance rules, `steering/ARCHITECTURE.md`'s provenance map, the root `README.md` — and the audience reference gains this project's `maintainer` row.
  `foundation.md` §3's collapse of `user` and `contributor` is qualified rather than reversed: it holds for roles and was derived for the theory's field alone, so it no longer covers everything the repository mobilises.
- Frozen records that count six functions — ADR-033, Phase 10's README, the Phase 07 self-application record — are not edited; this record is what refines them.
- A fiche is filed by the boundary test above.
  Where a mechanism's account leans on a coordinate's meaning, it points to the operationalizing fiche and does not restate it.
- **Not entailed here:** an obligation that a change to `scripts/` or `schema/` be paired with a change to a shelf a human reads.
  That is the paired-change check of this phase's T3, and it earns its own record when it is decided.

## Honest limit

A seventh function is one more place a contributor must decide between, and the boundary with `operationalizing` is thin.
The referential-integrity fiche already shows it: why supersession must be symmetric is a claim about what `supersedes` *means*, which belongs upstream, and the upstream fiche for it is one of the apports the operationalizing orient lists as still unwritten.
The codifying fiche carries the claim until that one exists.

The boundary is drawn from one instance of one repository's tooling.
`engine-config-seam.md` says the same of the seam, and the same holds here: nothing tests that the shelf is divided along the right line until a second consumer or a second phase of use does.

The account is written by the party that built what it explains, and no maintainer has read it cold.
The structuring tutorial was hardened against two blind tests; these fiches have had none.
Until one, they describe the apparatus as its author understands it, which is the weakest form of evidence that a stranger could act on them.

And the obligation that would keep the shelf true is not yet installed.
Until the paired-change check exists, `codifying/` can go stale exactly as `writing/frontmatter.md` did — the failure this function was adopted against.
That is a real gap between this record and its purpose, closed by a later one, not by this.
