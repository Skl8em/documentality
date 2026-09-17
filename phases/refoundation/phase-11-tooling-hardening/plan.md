---
title: "Phase 11 tooling hardening — the detailed plan"
force: propose
verb: argue
intention: suasive
view: synchronic
provenance: { type: project, id: phase-11-tooling-hardening }
constitutive: no
concerns: [steering, operationalizing, structuring]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

Phase 10 left the schema reconciled and enforced, but enforcement is narrower than the roadmap's wording suggests.
The nine required fields and six enums are hard errors; everything else is unchecked.
This phase closes that gap before Phase II is designed, because Phase II is the phase that starts *generating* from the frontmatter — and generation inherits every weakness the catalogue still has.

## Why this phase exists

Four holes, each verified rather than suspected.

- **The vocabulary is open.**
  Any field may be added to any document and the gate stays green.
  Two already have: `note` (4 documents) and `review` (1) are in the corpus today, declared nowhere.
  Meanwhile `order` and `pin` are declared and never used.
- **The YAML parser is hand-rolled.**
  [`frontmatter_lint.py`](../../../scripts/frontmatter_lint.py) splits strings on commas and colons rather than parsing YAML.
  The corpus happens to sit inside the subset it handles, so it works — but anything outside that subset (block sequences, multi-line strings, a quoted value containing a comma) **mis-parses and passes** instead of failing.
  That is the exact inversion of the fail-loud posture the rest of the tooling holds.
- **Nothing checks that an identifier points at anything.**
  `supersedes` and `superseded-by` are unvalidated.
  ADR-034's `supersedes` was verified by hand; a typo there would produce a dangling supersession pointer on a fully green gate, in the register that is meant to be the project's authoritative governance line.
- **The schema's edit surface is JSON, and its name lies.**
  `frontmatter.schema.json` is a bespoke dialect read by a hand-written validator, not JSON Schema — no standard tool can consume it — and JSON cannot carry the per-field rationale in comments.

## The rejected alternative — folding the validator into markdownlint

Worth recording, because it is the obvious idea and the reasons against it are not obvious.

A markdownlint custom rule *can* see the frontmatter: `params.frontMatterLines` hands it over.
But it arrives as **raw text**, and no YAML parser is reachable to parse it: in the devShell, `require("js-yaml")` and `require("yaml")` both fail, because markdownlint-cli2 arrives from Nix as a closed bundle exporting neither.

Adding one to the flake does not fix it.
[`.vscode/settings.json`](../../../.vscode/settings.json) wires custom rules into the **VSCode extension's own Node context**, which cannot see the devShell's modules.
A rule that requires an external module would pass in CI and fail in the editor, silently splitting the one-ruleset property Phase 09 exists to hold.
This is why `sentence-per-line.js` is pure regex: zero dependencies is a constraint there, not a style.

So the move would mean hand-rolling a YAML parser **in JavaScript** — reproducing the fragility this phase is deleting, in a language with no `pyyaml` to escape to.

There is a second, independent reason.
markdownlint rules are per-file by construction, and referential integrity is inherently corpus-level.
A rule could read the whole tree and cache an index, but it would go stale against unsaved editor buffers and make results depend on invocation order.

The per-file/corpus-level seam is real; it simply does not coincide with markdownlint's model.
Validation stays in Python.

## Workstreams

| # | Workstream | Output |
|---|---|---|
| **T1** | **Close the vocabulary.** `frontmatter_lint.py` errors on any field outside `required` ∪ `optional_fields` ∪ `root_only_fields`. Every optional field carries **its own** rationale string; the schema fails to load if one is missing, so "declared" and "justified" become the same act. Rule the four live cases: justify-and-declare or remove `note` and `review`; justify or drop the unused `order` and `pin`. | closed vocabulary, four rulings |
| **T2** | **Parse YAML with YAML.** Replace the hand-rolled parser with `pyyaml`, pinned in [`flake.nix`](../../../flake.nix). Fixtures modelled on the MD100 harness, pinning the cases the old parser silently got wrong. Then **reword the "stdlib only" comments** that stop being true (`check.py`, `frontmatter_lint.py`, `hash_check.py`, `slug_check.py`, `slugify_names.py`, `ulid_check.py`) plus [`flake.nix`](../../../flake.nix) line 28 — `ulid.py` and `rename_doc.py`, first listed here too, never touch YAML and keep a true claim. | real parser, fixtures, honest comments |
| **T3** | **YAML source, generated JSON.** Author the rules in YAML where comments carry each field's justification; generate the JSON artifact both runtimes can read dependency-free; the gate regenerates and diffs, failing on drift. Rename off `.schema.json`, which promises a standard the file does not implement. | `frontmatter-rules.yaml` → generated JSON + drift check |
| **T4** | **Referential integrity.** Extend `ulid_check.py`: every non-null `supersedes`/`superseded-by` resolves to an existing `id`; supersession is symmetric (if A supersedes B, B names A); every register row agrees with the record it points at. | a referential validator |

T1 is first because it is the smallest change that catches something real on day one.
T2 before T3, because generating a schema is not worth doing on top of a parser that can misread it.

## Verification / definition of done

- A document carrying an undeclared field **fails** the gate; a schema entry lacking a rationale **fails to load**.
- The four live vocabulary cases (`note`, `review`, `order`, `pin`) are each ruled on, not left standing.
- Fixtures exist for the YAML cases the hand-rolled parser mis-parsed, and they fail against the old parser.
- No comment in the tree claims "stdlib only" for code that imports `pyyaml`, directly or through a module it imports.
- A deliberately dangling `supersedes` fails the gate.
- The generated JSON cannot drift from its YAML source without the gate noticing.
- `python3 scripts/check.py` is green.

## Explicitly out of scope

- **Moving validation into markdownlint** — rejected above, on evidence.
- **Phase II design** — the next era, not this phase.
- **The legacy count-named records** (`ADR-NNN`, `phase-NN`) — an open naming convention, tracked as technical debt, not a debt this phase pays.
- **`status` vocabulary, `distance`/`power` value sets, the shape of `concerns`** — genuinely undecided, and still warnings by design; closing the *vocabulary* is not the same act as closing these *values*.

## Candidate records

Three decisions here look like they install standing obligations, and so earn an ADR under ADR-032 — to be written at close, not assumed now: **the frontmatter vocabulary is closed, and a field earns its place by carrying a reason**; **the schema's source of truth is YAML, its JSON a generated artifact**; and **unstarted work is never referred to by number**, the convention the roadmap now states.
T2 and T4 look like execution rather than decision, and would be changelog lines.
