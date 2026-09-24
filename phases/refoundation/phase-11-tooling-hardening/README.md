---
title: "Phase 11 — Tooling hardening"
force: orient
intention: formative
view: diachronic
provenance: { type: project, id: phase-11-tooling-hardening }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
hash: sha256:49e43400b5fd03314c7472d0258cb9db2d50b55d24abcbe28c90eceb70a7d476
---

Phase I's hardening phase: close the gaps Phase 10's enforcement left, before Phase II starts generating from the frontmatter and inherits every weakness the catalogue still carries.
Phase 10 had made the nine required fields and the six enums hard errors, and left everything else unchecked.

This record was **written after the phase**, by [Phase 12's T2](../phase-12-codifying/plan.md), which is why it is dated later than the work it narrates.
Phase 11 closed without a README, without a closing changelog entry and without the three ADRs its own plan named as owed at close; that account is what Phase 12 paid, and this is its centrepiece.
The narration below is from the commits, the changelog and the code as they stand, not from the phase's own hand.

What landed (detailed in [`plan.md`](plan.md), one workstream per bullet):

- **T1 — the vocabulary is closed.**
  A field is legal only if it is required, declared in `optional_fields`, or root-only, and every optional field carries its own reason; the schema refuses to load without one.
  The four cases the gate could not see were ruled on the documents that define the vocabulary: `pin` and `phase` declared and justified, `note`, `review` and `order` dropped ([ADR-036](closed-frontmatter-vocabulary.md)).
- **T2 — YAML is parsed as YAML.**
  Three hand-rolled comma-and-colon splitters were replaced by one shared reader on `pyyaml`, pinned in the devShell.
  Two departures from `yaml.safe_load` were ruled, each against a failure it would otherwise introduce: scalars stay strings, because YAML 1.1 reads `constitutive: no` as a boolean, and a duplicate key is an error, because `pyyaml` keeps the last one silently.
  The fixtures catch nine cases the old parser got wrong, and were written to fail against it.
  The one value the old parser had misread in the corpus was the root README's `axis`, which carried its trailing `# comment` inside the value, and nothing had checked it.
- **T3 — the schema's source is YAML.**
  The rules are authored in `schema/frontmatter-rules.yaml`, where a comment can carry each field's reason, and compiled to a generated JSON artifact; the gate regenerates and diffs, and fails on drift.
  The file left the `.schema.json` name, which promised a standard it did not implement.
  Compiling with a plain `safe_load` turned `constitutive: [yes, no]` into `[true, false]`, the same trap T2 had fixed for documents, and the generator now shares the strict loader ([ADR-037](yaml-source-generated-json.md)).
- **T4 — identifiers point at something.**
  `ulid_check.py` validates `supersedes` and `superseded-by` corpus-wide: every reference resolves, supersession is symmetric, and every register row agrees with the record it points at.
  It found three real asymmetries rather than suspected ones: ADR-001, ADR-002 and ADR-006 each carried `superseded-by: null` although their superseding records already named them.
- **Unstarted work stopped being numbered.**
  The insertion of this phase moved a forward reference for the second time, so the roadmap now names and orders what it has not begun and gives it a number only when tackled ([ADR-038](unstarted-work-unnumbered.md)).
  The convention arrived with the insertion, not with a workstream.

Records:

- [plan.md — the detailed plan](plan.md)
- [ADR-036 — the frontmatter vocabulary is closed, and a field earns its place by carrying a reason](closed-frontmatter-vocabulary.md)
- [ADR-037 — the schema's source is YAML and its JSON is a generated artifact](yaml-source-generated-json.md)
- [ADR-038 — unstarted work is never referred to by number](unstarted-work-unnumbered.md)

Verification, against the plan's definition of done, checked at close on 2026-09-24:

- An undeclared field fails the gate, and a schema entry with no rationale stops the schema loading.
  Both were demonstrated by running them; neither has a fixture.
- The four vocabulary cases are each ruled on, in the changelog and in ADR-036.
- The parser fixtures fail against the old parser.
  This was recorded when they were written, and was not re-run for this record.
- No comment claims "stdlib only" for code that imports `pyyaml`: four comments still make the claim (`check.py`, `ulid.py`, `rename_doc.py`, the MD100 harness).
  The last three import only the standard library; `check.py` does at module level and reaches `pyyaml` only after re-entering the devShell, which its own comment says.
- A dangling `supersedes` fails the gate, by fixture in `test_ulid_check.py`.
- The generated JSON cannot drift from its source unnoticed: the `schema-drift` check fails on a difference.
- `python3 scripts/check.py` is green.

Departures and gaps, recorded rather than hidden.
The phase closed leaving the product describing an old model: `writing/frontmatter.md` never said the vocabulary was closed, `steering/ARCHITECTURE.md` still put schema reconciliation in Phase 10, and the roadmap still read this phase as *(next)*.
The plan's T2 row listed `ulid.py` and `rename_doc.py` among the files whose "stdlib only" comment had to be reworded, though neither touches YAML; the changelog corrected it, and the plan's row still carries the error, since a phase's records are filled forward, not corrected in place.
The plan named four vocabulary cases and a fifth, `phase`, surfaced.
The plan's definition of done asked that a dangling reference fail, and did not ask about a cycle or a record superseding itself; both pass `ulid_check.py`, found only when Phase 12 wrote the fiche that had to state what the check does not establish.
And the plan's headline rule, the closed vocabulary, was shipped without a fixture that would go red if it were weakened.
Each of these is now in [`technical-debt.md`](../../../steering/technical-debt.md) or in the record that owns it; none is fixed by writing this README.

Whether the generated JSON earns its keep was not asked during the phase, only afterwards, when Phase 12 wrote the fiche that explains it; [ADR-037](yaml-source-generated-json.md) answers it, and its answer can lapse.
