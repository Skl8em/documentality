---
title: "Decision — the schema's source is YAML and its JSON is a generated artifact"
id: 01M39G4VTECMXE57PBSCKYKW66
slug: yaml-source-generated-json
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-11-tooling-hardening }
constitutive: yes
concerns: [codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:73777f86e95ff02588d05a1574ca291ef875143b344d1137cf47fbda8f73d029
---

## Status

accepted — 2026-09-24, recording a decision Phase 11 took on 2026-09-17 (`phase 11 - T3 YAML source, generated JSON`) and never wrote down.
Written by [Phase 12's T2](../phase-12-codifying/plan.md), so it carries Phase 11's provenance and a later date.
Passes the [ADR-032](../phase-10-schema/adr-tiering.md) test: it obliges anyone editing the schema, from now on, and the gate verifies it.
It also rules on a question Phase 12's first workstream raised against it — whether the generated file earns its place — and answers *keep*, with the reason and the condition under which that answer lapses.

## Context and forces in play *(justify)*

The schema was a JSON file, and two things were wrong with that.

**JSON cannot carry a comment.**
The vocabulary is the kind of file where the reason for a line matters more than the line, and the file had grown a `"//"` key as a substitute.
[The closed vocabulary](closed-frontmatter-vocabulary.md) makes it worse: every optional field must now carry a reason, and the reason is prose.

**The name lied.**
`frontmatter.schema.json` promised a JSON Schema dialect; the validator reading it was hand-written and implemented no such standard, so no standard tool could consume the file.

Two designs were on the table.
Author the schema in YAML and let the linter read the YAML directly, or author it in YAML and compile a JSON file that the linter reads instead.
Phase 11's plan chose the second and gave one reason: a JSON artifact "both runtimes can read dependency-free", because no YAML parser is reachable from a markdownlint custom rule.
Its own argument for keeping validation in Python rested on that fact.

The design intent is therefore an **interchange artifact**: YAML is the file a human edits, and the JSON is what programs read without carrying a YAML parser.

## Decision

1. **`schema/frontmatter-rules.yaml` is the source of truth**, edited by hand, comments allowed.
   It declares the required fields, the enums, the derived fields, the direction-of-fit table and each optional field's reason.

2. **`schema/frontmatter-rules.json` is generated from it** by `scripts/generate_schema.py` and is never edited.
   The edit loop is: change the YAML, regenerate, commit both.

3. **The gate fails on drift.**
   `schema-drift` regenerates the JSON in memory, compares it text for text with the committed file, and fails with a diff on any difference.
   It runs before every check that loads the JSON, so a schema edit cannot go unenforced because the artifact was left stale.
   Editing the JSON by hand fails the same check from the other side.

4. **The file is renamed off `.schema.json`**, so its name stops promising a standard it does not implement.

5. **The generated JSON stays.**
   This is a ruling on the question raised after the fact, not a restatement of Phase 11's choice, and it rests on evidence checked on 2026-09-24.
   Its only reader is `scripts/frontmatter_lint.py`, which already needs `pyyaml` to parse every document's frontmatter, so it could load the YAML directly through the strict loader.
   No Node or other consumer of the schema exists anywhere in the repository, and the one custom markdownlint rule, `sentence-per-line.js`, is pure regex and never reads it.
   The dependency-free reader is a capability in reserve, not one in use.
   It stays for three reasons.
   - The reader it is kept for is the one the phase exists to serve: Phase II generates *from* the catalogue, and its runtime is not yet designed.
     Collapsing now decides against a reader before that design has said what it needs.
   - The cost of keeping is bounded and already paid: one gate check, one extra commit-both step, both green and exercised.
     The cost of collapsing later is the same as collapsing now, so waiting forfeits nothing.
   - Collapsing is a code change to a working validator, the generator, the gate and the config, and not what a record closing an account should smuggle in.
   The answer **lapses** if the Phase-II design closes with no non-Python reader of the schema, or if the drift check ever fails for a reason other than a forgotten regeneration.
   Either is a reason to write the superseding record that removes the JSON.

## Entail — what follows

- Any load of this vocabulary goes through `StrictLoader` in `scripts/yaml_frontmatter.py`, never a bare `safe_load`.
  YAML 1.1 reads bare `yes` and `no` as booleans; compiled plainly, `constitutive: [yes, no]` became `[true, false]` and silently broke the enum.
  The same trap bites frontmatter *documents*, and Phase 11's T2 had already fixed it there once; the generator now shares that loader so it is fixed once.
  The two departures from `safe_load` — scalars stay strings, and a duplicate key is an error — were checked against ADR-032 when this record was written and are held here, not in a record of their own: the obligation binds only where the vocabulary is loaded, one shared loader enforces it by construction, and this record is the place a maintainer looks when the schema is loaded.
- A maintainer editing the schema edits the YAML and regenerates; the fiche [the schema pipeline](../../../codifying/schema-pipeline.md) says how, and is where the weakest joint below is stated.
- A second reader of the JSON, if one appears, confirms this record; a change to where the two files live is instance configuration (`docsys.yaml`), not this decision.

## Honest limit

**"Less bad" is not "correct."**
Keeping a generated file for a reader that does not exist is speculative generality, the thing a simplest-thing rule forbids, and the cost above is the price of a hedge.
The whole failure class the drift check guards — a stale generated file — exists only because there are two files.
If the honest test is what the repository needs today, one file loaded through `StrictLoader` is simpler and would remove the check.
This record keeps the JSON because the reader it is for has not yet been designed away, which is a bet on Phase II and not a fact about now.

The claim that no other reader exists was checked by search on one date, in one repository.
It says nothing about a reader outside it.

The interchange role was Phase 11's stated intent, but nothing in the repository tests it: no non-Python consumer has ever loaded the file, so "readable without a YAML parser" is true of JSON in general and unproven of this artifact.

And the schema is data, not all of the rules.
What the linter enforces is partly in its code — the direction-of-fit partition, that `register` is never stored, how a composite force is read — so a change to what the vocabulary may *express* is an edit to code that the YAML alone will not show.
