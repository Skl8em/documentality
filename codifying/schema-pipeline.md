---
title: "The schema pipeline — YAML source, generated JSON"
force: explain
intention: formative
view: synchronic
provenance: { type: function, id: codifying }
constitutive: no
distance: initiated
audience: [contributor]
reader: H+M
status: draft
---

**Read this before** editing `schema/frontmatter-rules.yaml` or anything that loads the schema.
It is written for the maintainer, initiated in tooling engineering.
What each frontmatter coordinate *means* is [`operationalizing/`](../operationalizing/README.md)'s; this is about the file that declares them and how it reaches the linter.

## The shape

There are two files and they carry identical data.

- [`schema/frontmatter-rules.yaml`](../schema/frontmatter-rules.yaml) is the **source of truth**, edited by hand.
  It declares the required fields, the enums, the derived fields, the direction-of-fit table, and every optional field with the reason it exists.
- `schema/frontmatter-rules.json` is **generated** from it by [`scripts/generate_schema.py`](../scripts/generate_schema.py), and is what [`scripts/frontmatter_lint.py`](../scripts/frontmatter_lint.py) actually loads.

The edit loop is: change the YAML, run `python3 scripts/generate_schema.py`, commit both.
The gate's `schema-drift` check regenerates the JSON in memory, compares it to the committed file text for text, and fails with a diff on any difference.
It runs before anything that loads the JSON, so a schema edit cannot go unenforced because the generated file was left stale.
Editing the JSON by hand fails the same check, from the other side.

The `docsys` engine, mounted at `docsys/`, ships the same vocabulary as `docsys/src/docsys/schema/frontmatter-rules.yaml` and reads that YAML itself, with no generated JSON, so the vocabulary exists twice while the gate still runs `scripts/`.
A change to what a verdict depends on (a required field, an enum, an optional field, the root-only fields, the direction of fit, the hash pattern) is made in both; the engine's tests compare them when run from this repository and fail on a difference.
The rationales and the comments are the engine's own prose and are not compared.

Where the two files live is instance configuration (`schema:` in [`docsys.yaml`](../docsys.yaml)); what they declare is the *methodology's*, shared by any project that adopts the vocabulary.
[`engine-config-seam.md`](../phases/refoundation/phase-12-codifying/engine-config-seam.md) draws that line.

## Why YAML is the source

The schema used to be JSON.
JSON cannot carry a comment, and the vocabulary is exactly the kind of file where the *reason* for a line matters more than the line: the file had grown a `"//"` key as a comment substitute.
The file's name, `frontmatter.schema.json`, also claimed a JSON Schema dialect that the hand-written validator never implemented, so no standard tool could consume it.

YAML fixes the first and the rename fixes the second.
The reason is enforced, not hoped for: every key of `optional_fields` must carry a non-empty rationale string, and the linter refuses to load the schema if one does not.
A field cannot be declared without being justified, because the two are the same act.

## Why there is still a JSON file

The stated reason, from Phase 11's plan, is that both runtimes can read a dependency-free artifact: Python's `json` module and Node's need no YAML parser, and the plan records that no YAML parser is reachable from a markdownlint custom rule.
The design intent is an interchange artifact — YAML for the human who edits, JSON for programs — and [ADR-037](../phases/refoundation/phase-11-tooling-hardening/yaml-source-generated-json.md) records it, with the ruling that follows.

**Read that reason sceptically.**
Only one program reads the JSON today, `frontmatter_lint.py`, and it already requires `pyyaml` to parse every document's frontmatter.
No Node consumer of the schema exists; the one custom rule, `sentence-per-line.js`, is pure regex and never reads it.
The dependency-free reader is a capability kept in reserve, not one in use.
The case for a YAML *source* stands on its own; the case for a second, generated file rests on a reader that has not appeared, and is the pipeline's weakest joint.
[Medium confidence: this reads the repository as it is now.]
ADR-037 rules that the JSON **stays for now**, because the reader it is kept for — a generator, or a non-Python tool reading the schema — does not exist yet, and because keeping costs one green check.
The answer lapses when the design of the agent machinery closes with no non-Python reader — in practice, at the end of the rush to MVP — or when the drift check fails for any reason other than a forgotten regeneration; collapsing to one file, loaded through the strict loader below, would then remove the drift check and the whole class of failure it guards.
The cross-package API proposed in [`imagining/multi-ecosystem-distribution.md`](../imagining/multi-ecosystem-distribution.md) has every package load the YAML methodology unchanged, which weakens the JSON's case further.

## The trap the pipeline already fell into

YAML 1.1 reads bare `yes` and `no` as booleans.
Compiled with a plain `yaml.safe_load`, `error_enums.constitutive: [yes, no]` became `[true, false]`, which silently broke that enum.
It is the same trap that frontmatter *documents* carry, reappearing in the schema's own source.

The generator therefore loads through `StrictLoader` in [`scripts/yaml_frontmatter.py`](../scripts/yaml_frontmatter.py): scalars stay strings and only `null` resolves, and a duplicate key is an error at any depth, since `pyyaml` would otherwise keep the last one silently.
The loader is shared by the document reader and the generator, so the fix is made once.
The rule for a maintainer: **never load this vocabulary through a bare `safe_load`**, in a new script or a test.

## What the linter still knows that the schema does not say

The schema is data, but not all of what the linter enforces is in it.
The linter's *code* encodes that the direction-of-fit table must partition `force` exactly, that `register` is derived and never stored, that the root README alone carries `axis` and `dominant-community`, and how a composite force `a+b` is read.
Changing the vocabulary is an edit to the YAML; changing what the vocabulary is *allowed to express* is an edit to code.
The schema-load refusals (a partition that does not cover the forces, an optional field without a reason) exist because those code-level assumptions can be broken from the data side.

One duplication sits outside this pipeline and is named so a maintainer is not surprised by it: `hash_seal.py` decides which `status` words make a record *frozen*, and the schema declares which words exist.
The definition stays in code, deliberately: the schema lists its status vocabulary among the questions it still leaves open, and a `frozen` declaration in it would rule on part of that question by side effect.
`hash_seal.py` therefore classifies every status word twice over, `FROZEN_STATUSES` and `OPEN_STATUSES`, and `scripts/test_hash_check.py` fails the gate when the two lists together stop matching `warn_enums.status` — a word added to the schema and classified nowhere, a word the schema dropped, a word in both.
So a schema edit that adds a status is met at the gate with the edit that clears it, not discovered as a record that silently never gets sealed.
The definition moves into the schema when the status vocabulary is ruled.

## What the pipeline does not establish

- **That the schema is right.**
  It checks that the JSON matches the YAML and that the schema is internally coherent, not that its vocabulary is the correct one.
  What is still open is listed in the schema's own `still_open`.
- **That a consumer reads the schema through the pipeline.**
  A script that loaded the YAML directly, or hard-coded a value, would not be caught by `schema-drift`.
- **That the closed vocabulary stays closed.**
  The linter rejects an undeclared field and refuses a reason-less optional field, and neither rule has a fixture, so weakening either turns no test red ([technical debt](../steering/technical-debt.md)).
