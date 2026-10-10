---
title: "Decision — the frontmatter vocabulary is closed, and a field earns its place by carrying a reason"
id: 01M39G4TR6R2DXH20091Q983GZ
slug: closed-frontmatter-vocabulary
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-11-tooling-hardening }
constitutive: yes
concerns: [operationalizing, codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:a65a819c4422b073a6f9790064af8bb10de68942e6a667cc3bc905ced796f238
---

## Status

accepted — 2026-09-24, recording a decision Phase 11 took on 2026-09-15 (`phase 11 - close the vocabulary`) and never wrote down.
Written by [Phase 12's T2](../phase-12-codifying/plan.md), which is why it carries this phase's provenance and a later date: the decision is Phase 11's, the record is late.
Passes the [ADR-032](../phase-10-schema/adr-tiering.md) test: it obliges everyone who adds a frontmatter field, from now on, and the gate verifies it.

## Context and forces in play *(justify)*

Phase 10 enforced the schema, but only its required fields and its enums.
Any other field could be added to any document and the gate stayed green.
Two already had been: `note` in four documents and `review` in one sat in the corpus, declared nowhere, while `order` and `pin` were declared and never used.
An open vocabulary fails in both directions, and the catalogue is what a later generator reads from ([Phase 11's plan](plan.md) gives that as the reason for the phase): a field that exists but is declared nowhere has no meaning anyone can consult, and a field declared but unused is a promise the corpus does not keep.

The vocabulary was also declared badly.
The schema's `optional_fields` bundled several names under one description — `supersedes` silently covered `superseded-by`, `retention`, `pin`, `order` and `phase` — so a field could be legal without anyone ever having said why it exists.

Closing the vocabulary alone would have fixed the first failure and left the second.
The alternative that fixes both is to make *declared* and *justified* one act, so that a field cannot enter the vocabulary without its reason being written down next to it.

## Decision

1. **The frontmatter vocabulary is closed.**
   A field is legal only if it is `required`, a key of `optional_fields`, or a `root_only_fields` entry in the schema.
   Any other field is a gate error, whichever document carries it and however plausible it looks.

2. **A field earns its place by carrying a reason.**
   Every key of `optional_fields` carries its own non-empty rationale string, one field to one reason, no bundling.
   The schema refuses to load if one is missing or empty, so a field cannot be declared without being justified.

3. **The four live cases were ruled on the documents that define the vocabulary, not on corpus habit.**
   `writing/frontmatter.md`'s field table and `operationalizing/README.md`'s coordinate inventory were the reference; how often a field appeared was not.
   - `pin` is declared and justified: the field table already named it, and it is unused only because this repository never instantiates the `projects/`-submodule topology it fixes a reference into.
   - `phase` — a fifth case the plan had not listed — is declared, justified, and added to the field table, which had drifted: it is bumped forward as a steering document is reconciled to a later phase.
   - `note` is dropped, its four values moved into each document's own prose: it was free text nothing reads, present in neither canonical list.
   - `review` and `order` are dropped: `review` traces to one unexplained addition in the Phase 10 sweep, `order` to no use and no documented reason.

4. **The source of the vocabulary is the schema, not any prose about it.**
   `writing/frontmatter.md` is the reading of `schema/frontmatter-rules.yaml`; where they disagree the schema is right and the prose is the defect.
   Which file is the schema's source is [its own decision](yaml-source-generated-json.md).

## Entail — what follows

- Adding a field is a schema edit with its reason, in the same change as the first document that carries it; a document that uses an undeclared field fails the gate with the edit that clears it.
- A field with no reason, or whose reason is empty, stops the frontmatter check outright rather than failing one document.
- The reason is a claim about *why the coordinate exists*, and is read by a person: the linter checks that it is present and not that it is good.
- `writing/frontmatter.md` states the closure and points at the schema, so the product's reader is told what the catalogue accepts.
  Phase 11 left that unsaid; Phase 12's T2 says it.
- **Not decided here:** the *values* of `distance`, `power` and `status`, and the shape of `concerns`.
  Closing the vocabulary is not closing these; they stay warnings, listed in the schema's `still_open`.

## Honest limit

The mechanism is real and demonstrated, and neither half of it has a fixture.
On 2026-09-24 a document carrying `note:` failed with the expected message, and a schema entry with an empty rationale stopped `load_schema()`; but `scripts/test_frontmatter_lint.py` has no case for either.
The one fixture that mentions an undeclared field, "undeclared field hidden by indentation", fails on invalid YAML, not on the vocabulary rule.
The rule is enforced and unpinned: someone can weaken it and no test goes red.
That is recorded in [`technical-debt.md`](../../../steering/technical-debt.md), not fixed here.

A reason string is the cheapest possible evidence that a field was thought about.
`pin`'s rationale admits the field has never been exercised here, and it passes; a fluent, empty justification would pass too.
The rule moves the cost of a field from zero to one sentence, which is friction, not a guarantee.

Two of the four rulings were judged by their authors against documents their authors also wrote.
`note` and `review` were dropped on the strength of a canonical field list that is itself part of the catalogue being closed.
No one outside the project has been asked whether a dropped field was doing work.
