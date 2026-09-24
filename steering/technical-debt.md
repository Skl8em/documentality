---
title: "Technical debt — known gaps, tracked so they are not forgotten"
id: 01KYYTENWN3TWF5VC2A8CC1VYP
slug: technical-debt
force: describe
verb: specify
intention: state
view: synchronic
provenance: { type: function, id: steering }
constitutive: no
audience: [contributor, decider]
reader: H+M
status: draft
---

Known technical debt: things we chose to defer, each with *why* and *how to resolve*.
This is a **current** register (a debt is removed when it is paid), distinct from [`open-questions`](open-questions.md) (undecided questions) and the roadmap (planned phases).

## Legacy count-named records

**What:** existing records still use sequential-count names — the ADRs (`ADR-001`…`ADR-027`) and the phase folders (`phase-01-foundation`…`phase-09-tooling`) — while new records follow the [ULID identifiers decision](../phases/refoundation/phase-09-tooling/ulid-identifiers.md): a `<slug>.md` filename with a ULID `id` in frontmatter.
The corpus therefore carries two naming schemes at once.

**Why left open:** the decision (ADR-028) deliberately keeps the naming convention open, rather than forcing a corpus-wide rename now.
Adopting `id`/`slug` on the legacy records — and choosing whether their filenames become `<slug>.md` or `<slug>-<ulid>.md` — is a per-record judgement, not a debt that must be paid on a schedule.

**How to resolve (when we choose):** add `id`/`slug` to a record's frontmatter (mint with `scripts/ulid.py` — ADRs chronological, phases ordinal via an `order` key), then normalise its filename with `scripts/slugify_names.py` (→ `<slug>.md`) or `scripts/migrate_ids.py` (→ `<slug>-<ulid>.md`); both rewrite all references via the safe-rename core, gated by `linkcheck` + `slug_check` + `ulid_check`.

## Linter-grandfathered content

**What:** `phases/naive-sketch/**` (pre-ADR-021 records), `imagining/**` (informal Phase-II notes), and the blind-test transcripts are excluded from markdownlint / the frontmatter linter.

**Why:** they predate the current conventions or are not authored prose; forcing them into compliance would be churn without value.

**How to resolve:** bring a file into the catalogue (frontmatter + one-sentence-per-line) and remove it from the ignore lists when it stops being historical/informal — case by case, not in bulk.
There are two lists: `frontmatter:` in [`docsys.yaml`](../docsys.yaml) for the linter, and `.markdownlint-cli2.jsonc` for markdownlint, which reads only its own config; nothing checks that they agree.

## Unsealed frozen records

**What:** `scripts/hash_check.py --unsealed` lists frozen records that carry no `hash:` fixity seal (ADR-031).
The naive-sketch era (phases 01–05) is the bulk of it.

**Why left open:** sealing is an act performed *at freeze*, and those records were frozen before the seal existed.
Back-sealing them fixes their *current* content, not the content they had when they closed — which is an honest thing to do, but it should be a deliberate act rather than a bulk sweep.

**How to resolve:** `python3 scripts/hash_seal.py <path>` per record, or `--frozen` for all unsealed ones at once.
Note that sealing a record makes any later edit to it fail the gate until it is consciously re-sealed — that is the point, and the cost.

## Paid

- **Reorg leftovers (untracked on-disk zombies)** — the three untracked directories the Phase-08 renames left on disk (`theory/`, `write/`, a top-level `phases/phase-07-structuring-tutorial/` husk) are gone, and the root `.gitignore` stops the `.DS_Store` files that blocked their deletion from coming back.
  The real lesson is paid too: `scripts/check.py` now asserts `git status --porcelain` is clean of untracked paths, so on-disk cruft can no longer pass a gate that reads only `git ls-files` (Phase 10).
- **Duplicated round-2 blind-test transcripts** — the `weft-blindtest-round2/` directory was byte-identical to the `blind-test/weft-{response,review}-round2.md` copies and was deleted; the `blind-test/` copies stay, sitting with round 1 (Phase 10).

## Engine/config seam residue

**What:** [Phase 12 T1(b)](../phases/refoundation/phase-12-codifying/engine-config-seam.md) moved every path, prefix and register format out of `scripts/` into `docsys.yaml`, and named what it left in code.
Three of those are debts rather than design: the definition of a *frozen* record in `hash_seal.py` duplicates the schema's status vocabulary and can drift from it; a decision register whose configured row shape matches nothing still passes `ulid_check.py` silently; and the seam is drawn from a single instance.

**Why left open:** the frozen-record definition belongs in the schema, and moving it widens the schema's vocabulary — a ruling, not a refactor.
The empty-register case is a hardening for the gate's next pass.
The single-instance boundary cannot be tested without a second consumer.

**How to resolve:** declare what "frozen" means in `schema/frontmatter-rules.yaml` and have `hash_seal.py` read it; make `ulid_check.py` fail when the register yields no decision rows; revisit the seam when a second project wants the pipeline, or when it has held unchanged for a full phase.

## Gate messages: three validators unfixtured

**What:** the gate's failure messages now each carry a `— fix:` clause ([Phase 12 T1(c)](../phases/refoundation/phase-12-codifying/error-message-audit.md)), and the two validators with fixtures (`frontmatter_lint.py`, `ulid_check.py`) fail a fixture whose message lacks one.
`slug_check.py`, `linkcheck.py` and `hash_check.py` build theirs inline in `main()`, so nothing tests them.

**Why left open:** testing them means extracting the message-building into pure functions first; that is a refactor of three working validators, not a side effect of a message edit.

**How to resolve:** extract, on the model of `ulid_check.check_referential_integrity`, add fixtures, and assert the `fix:` clause in each.

## Closed vocabulary: the rule has no fixture

**What:** `frontmatter_lint.py` rejects any field outside `required` ∪ `optional_fields` ∪ `root_only_fields`, and `load_schema()` refuses an optional field with no rationale ([ADR-036](../phases/refoundation/phase-11-tooling-hardening/closed-frontmatter-vocabulary.md)).
Both were demonstrated by running them on 2026-09-24, but `scripts/test_frontmatter_lint.py` has no case for either.
The one fixture that mentions an undeclared field fails on invalid YAML, not on the vocabulary rule.

**Why left open:** found while closing Phase 11's account, whose task was documentation; adding fixtures is a change to the validator's tests, not to that account.

**How to resolve:** add a lint case with an undeclared field that must fail with the `closed frontmatter vocabulary` message and a `fix:` clause, and a schema-load case with an empty rationale that must stop `load_schema()`; run each red against a linter with the rule removed first.

## Referential integrity: cycles and self-supersession pass

**What:** [`ulid_check.py`](../scripts/ulid_check.py) accepts a pair of records that supersede each other, and a record that supersedes itself: each satisfies the resolve and symmetry rules trivially.
Found while writing [the referential-integrity fiche](../codifying/referential-integrity.md) and confirmed against `check_referential_integrity` with two synthetic records.

**Why left open:** the fiche's job was to state what the check does not establish; closing the hole is a change to the validator, with its own fixtures, outside the adoption of `codifying`.

**How to resolve:** add two fixture cases (a mutual pair, a self-reference) that must fail, then reject a record whose `supersedes` or `superseded-by` names itself and any cycle along the `superseded-by` chain.

## Paired-change: what the rule does not see

**What:** the [paired-change rule](../phases/refoundation/phase-12-codifying/paired-change-rule.md) (ADR-039) has three gaps.
It checks that a file explaining the tooling was edited, not that the edit is true.
The pre-commit hook that would stop a violating commit is opt-in (`git config core.hooksPath .githooks`), so on a clone that has not opted in the violation is found by CI after the commit exists; once it is shared, the only remedy is moving `paired_change.since`.
And a change confined to `docsys.yaml` or `tools/markdownlint/`, which are apparatus, is in neither list.

**Why left open:** the first is what any co-occurrence rule costs and only a reader can close it; the second is a property of git hooks, which are not versioned into a clone; the third was left out on purpose, because `docsys.yaml` will hold the phase ledger of T6, whose edits nothing on the shelves explains.

**How to resolve:** for the third, either split the ledger from the gate's configuration or list `docsys.yaml` with a carve-out for that section; for `tools/markdownlint/`, list it when a change to it first goes unexplained.
For the second, CI already runs the check; treat a red `paired-change` on a shared branch as a reason to move the anchor with a stated cause in the commit message, not to re-run it.
