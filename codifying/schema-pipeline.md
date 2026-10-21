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
Why the vocabulary is YAML, the strict loader every file goes through, what the frontmatter check knows beyond the schema, and which statuses close a record are explained with the engine, in [the vocabulary fiche](https://github.com/Skl8em/docsys/blob/main/docs/vocabulary.md); `scripts/` follows the same choices on this repository's copy.
In `scripts/`, the loader is `StrictLoader` in [`scripts/yaml_frontmatter.py`](../scripts/yaml_frontmatter.py), and the frozen statuses are `FROZEN_STATUSES` and `OPEN_STATUSES` in `hash_seal.py`, guarded against the schema by `scripts/test_hash_check.py`.

Where the two files live is instance configuration (`schema:` in [`docsys.yaml`](../docsys.yaml)); what they declare is the *methodology's*, shared by any project that adopts the vocabulary.
[`engine-config-seam.md`](../phases/refoundation/phase-12-codifying/engine-config-seam.md) draws that line.

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
The answer lapses when the design of the agent machinery closes with no non-Python reader — in practice, at the end of the rush to MVP — or when the drift check fails for any reason other than a forgotten regeneration; collapsing to one file, loaded through the strict loader, would then remove the drift check and the whole class of failure it guards.
The cross-package API proposed in [`imagining/multi-ecosystem-distribution.md`](../imagining/multi-ecosystem-distribution.md) has every package load the YAML methodology unchanged, which weakens the JSON's case further.
The project owner ruled on 2026-10-20 that `schema/` retires with `scripts/` when this repository's gate becomes `docsys check`, by an ADR that supersedes ADR-037 ([Phase 14 plan](../phases/rush-to-mvp/phase-14-adoption/plan.md), *Rulings*); until then ADR-037 stands.

## What the pipeline does not establish

- **That the schema is right.**
  It checks that the JSON matches the YAML and that the schema is internally coherent, not that its vocabulary is the correct one.
  What is still open is listed in the schema's own `still_open`.
- **That a consumer reads the schema through the pipeline.**
  A script that loaded the YAML directly, or hard-coded a value, would not be caught by `schema-drift`.
- **That the closed vocabulary stays closed.**
  `frontmatter_lint.py` rejects an undeclared field and refuses a reason-less optional field, and neither rule has a fixture in `scripts/`, so weakening either turns no test red there ([technical debt](../steering/technical-debt.md)); the engine's check has a case for each.
