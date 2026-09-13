---
title: "Decision — `operationalizing` is the sixth function, between theory and product"
id: 01KZ2EQ400JPNSHSSJT0RHM57T
slug: operationalizing-function
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-10-schema }
constitutive: yes
concerns: [steering, structuring, theorising, operationalizing]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:b1755d62eae80984fa4e93a1822da0b5521b7f9e05ba6174f448720cc3386ccd
---

## Status

accepted — 2026-08-03.
Records a decision that was ratified and **already enacted** — the `operationalizing/` shelf exists — but had no record.
Refines the function set derived in ADR-022 and the shelf rule of ADR-024.

## Context and forces in play *(justify)*

Between "what a document *is*" and "how you write one" sat a layer with nowhere to live.

`theorising` says a document is an inscribed act with a force, an intention, and a recipient at some distance and power.
`writing` and `structuring` tell an author what to do.
But between them are the **operational apports** — the coordinates we *chose to reify* so that the theory becomes workable, checkable, and machine-ready: `view`, `constitutive`, `register`, `reader`, `id`/`slug`, `hash`, `concerns`, `status`, `retention`, `pin`.

None of these is in the theory.
The theory grounds the state/change seam; putting a `view:` field on every file is our choice.
The theory grounds the constitutive distinction; storing `constitutive: yes|no` is our choice.
Each carving is defensible, and each *needed its reasons written down somewhere* — otherwise the schema looks like a list of arbitrary fields, and the next contributor cannot tell which are theory and which are convention.

Filing them elsewhere failed in a specific way each time.
In `theorising` they would pass for theory, which is exactly the confusion to avoid.
In `writing`/`structuring` they would be buried in guidance, stated as rules rather than argued as choices.
In `steering` they would sit with project direction, which is not what they are.
And the schema file itself records *what* was carved, never *why*.

In VSM terms the shelves were already a system: `steering` is System 5 (direction), `imagining` System 4 (the future), the product Systems 1–2.
The missing shelf is **System 3** — the operational layer that turns policy into something the units can actually run.

## Decision

1. **`operationalizing` is adopted as a sixth function**, giving `theorising` · `operationalizing` · `writing` · `structuring` · `steering` · `imagining`.

2. **Its domain is the operational apports**: for each reified coordinate, what it operationalizes, why we carved it this way, what alternatives were rejected, and what work it does.

3. **Its place in the chain is fixed**, upstream of the product and of the tooling:

   ```text
   theorising → operationalizing → structuring / writing → designing → IT tools
   ```

4. **It is a shelf like any other** — `provenance: { type: function, id: operationalizing }`, gerund-named per ADR-027, one folder at the root.

5. **A fiche is not a decision**.
   `operationalizing/register.md` explains the derived register; [`register-derived-constitutive.md`](register-derived-constitutive.md) decides it.
   The fiche is maintained and `synchronic`; the record is frozen and `diachronic`.
   This is the same state/change seam the system applies everywhere, and it is why adopting the shelf does not make the register redundant.

## Entail — what follows

- `operationalizing/` holds its orient plus the first fiches: `view`, `constitutive`, `register`.
- The function set is six wherever it is enumerated — `steering/foundation.md`, `CONTRIBUTING`'s shelving rule, `phases/refoundation/phase-07-structuring-tutorial/self-application.md` (as a later addition to a frozen derivation, noted not rewritten).
- Every future field added to the schema wants a fiche, not just a schema line — the schema says what, the fiche says why.
- The remaining apports (`reader`, `id`/`slug`, `hash`, `concerns`, `status`, `retention`, `pin`) have no fiche yet; the shelf is opened, not filled.

## Honest limit

A sixth function is a real cost: one more place a contributor must decide between, and the boundary with `theorising` is genuinely thin.
Whether "the state/change seam" is theory and "putting a `view:` field on it" is operationalization is a distinction that will be argued case by case, and some fiches will be filed wrongly.

We are also recording this *after* enacting it, which inverts the order `CONTRIBUTING` requires.
The decision was ratified in `open-questions` and the shelf was built in the same commit; this record catches the register up rather than authorizing anything.
Noting it here is the honest version of an inconsistency we would otherwise have hidden.
