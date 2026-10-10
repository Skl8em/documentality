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

**What:** `phases/naive-sketch/**` (pre-ADR-021 records), `imagining/**` (proposals and informal notes), and the blind-test transcripts are excluded from markdownlint / the frontmatter linter.

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
- **Referential integrity: cycles and self-supersession pass** — `ulid_check.py` now rejects a record that names itself in `supersedes` or `superseded-by`, and a loop along `superseded-by`, each with a fixture that was red first; the [referential-integrity fiche](../codifying/referential-integrity.md) states it (Phase 12 T4).
- **A register whose row shape matches nothing passed** — `ulid_check.check_register` now fails when it finds no decision rows, with fixtures for an empty register, a wrong column count and a non-matching ordinal; the [referential-integrity fiche](../codifying/referential-integrity.md) states it (Phase 12 T4).
- **Gate messages: three validators unfixtured** — `slug_check.py`, `linkcheck.py` and `hash_check.py` build their messages in pure functions, with fixtures (`test_slug_check.py`, `test_linkcheck.py`, `test_hash_check.py`, registered in the gate ahead of each check) that fail a message lacking its `fix:` clause, shown by removing the clause from each; the same extraction was needed in `ulid_check.py`'s own `main()` (Phase 12 T4).
- **A renamed integration branch silently disarmed the paired-change rule** — `paired_change.py` now fails, on every run, when no branch in `enforce_on` exists locally or on a remote, with fixtures for a stale list and a remote-only branch; the [gate fiche](../codifying/gate.md) states it (Phase 12 T6(b)).

## Engine/config seam residue

**What:** [Phase 12 T1(b)](../phases/refoundation/phase-12-codifying/engine-config-seam.md) moved every path, prefix and register format out of `scripts/` into `docsys.yaml`, and named what it left in code.
Three of those remain debts rather than design.
The seam is drawn from a single instance.
`migrate_ids.py`, the Phase 09 identifier migration, still names the phase root as a bare literal (`git ls-files phases`): the leak check reads the root as the prefix `phases/`, because the bare word is also the ledger's and the config's own key, so this literal passes it (found in T6(b)).
And the definition of a *frozen* record lives in `hash_seal.py`, where it duplicates a fact the schema also states (its status vocabulary): **kept there on purpose since T4**, guarded by a fixture in `test_hash_check.py` that fails when the two disagree, not moved.

**Why left open:** the single-instance boundary cannot be tested without a second consumer.
The frozen definition belongs in the schema in principle, but declaring it there widens the schema's vocabulary and rules on part of what the schema's `still_open` list calls the status vocabulary — a ruling, not a refactor, and not one this debt should take by side effect.

**How to resolve:** revisit the seam when a second project wants the pipeline, or when it has held unchanged for a full phase.
Read the root from `phases.root` in `migrate_ids.py`, or retire the script once no record awaits migration.
Move the frozen definition into `schema/frontmatter-rules.yaml`, have `hash_seal.py` read it and retire the guard, when the status vocabulary is ruled.

## Gate messages: two still unfixtured

**What:** the gate's failure messages each carry a `— fix:` clause, and the validators whose messages are built in pure functions fail a fixture that lacks one.
Two sources are outside that: the drift message of `generate_schema.py --check` says what to run and to commit but not under the `fix:` marker, and no fixture runs it; and the runner's own messages (`check.py`) are pinned only for order and attribution.

**Why left open:** found while paying the three-validator debt; each is small, and neither was in the debt as recorded.

**How to resolve:** extract the drift message into a function with a fixture asserting the marker, as for the validators; decide whether the runner's unavailable-tool and summary messages need the marker or are a different kind of message.

## Closed vocabulary: the rule has no fixture

**What:** `frontmatter_lint.py` rejects any field outside `required` ∪ `optional_fields` ∪ `root_only_fields`, and `load_schema()` refuses an optional field with no rationale ([ADR-036](../phases/refoundation/phase-11-tooling-hardening/closed-frontmatter-vocabulary.md)).
Both were demonstrated by running them on 2026-09-24, but `scripts/test_frontmatter_lint.py` has no case for either.
The one fixture that mentions an undeclared field fails on invalid YAML, not on the vocabulary rule.

**Why left open:** found while closing Phase 11's account, whose task was documentation; adding fixtures is a change to the validator's tests, not to that account.

**How to resolve:** add a lint case with an undeclared field that must fail with the `closed frontmatter vocabulary` message and a `fix:` clause, and a schema-load case with an empty rationale that must stop `load_schema()`; run each red against a linter with the rule removed first.

## Paired-change: what the rule does not see

**What:** the [paired-change rule](../phases/refoundation/phase-12-codifying/paired-change-rule.md) (ADR-039, refined by [ADR-040](../phases/refoundation/phase-12-codifying/paired-change-where-it-fails.md)) has these gaps, each scheduled in the [Phase 12 plan](../phases/refoundation/phase-12-codifying/plan.md#open-points-and-when-each-is-settled):

- It checks that a file explaining the tooling was edited, not that the edit is true; a docstring that replaces the description of unchanged behaviour is exempt, and only Python is examined for comment-only edits.
- The pre-commit hook is opt-in (`git config core.hooksPath .githooks`): a local setting no clone inherits.
  It was enabled in the author's clone on 2026-09-25; elsewhere a violation is found at the pull request, after the commit exists, and once shared the only remedy is moving `paired_change.since`.
  On a feature branch the hook shows the warning but does not block a paired-change violation (ADR-040); it blocks on every other check.
- On a feature branch a violation is only a warning, so a mechanism commit followed by its account passes there and fails at the pull request, which examines every commit since the anchor.
  How costly that is on a phase-long branch is unmeasured.
- A change confined to `tools/markdownlint/`, which is apparatus, is in neither list.
  `docsys.yaml` joined the mechanism list in T6, once the phase ledger was ruled out of it; moving `paired_change.since` now needs an account in the same commit, and no explaining file is an obvious home for one.
- A rename or a behaviour-free refactor still asks for an account; only tests and comment-only edits are exempt.

**Why left open:** the first is what any co-occurrence rule costs and only a reader can close it; the second is a property of git hooks, which are not versioned into a clone (a clone must opt in); the third is the price of not blocking work in progress, chosen in ADR-040; the fourth: `tools/markdownlint/` was never scheduled, and the cost of accounting for a moved `since` is new and unmeasured; the last awaits evidence.

**How to resolve:** the plan's table names the step for each — the hook is enabled in the author's clone, and T4 (its first real use) showed it ran the gate on every commit and blocked nothing, so it has not yet been seen to catch a violation — the project owner's verdict on it is still open; the merge-time cost is observed on Phase 12's own merge in T5; the `docsys.yaml` gap is closed (T6 split the ledger into `steering/phases.yaml` and listed `docsys.yaml` as mechanism); `tools/markdownlint/` can join the list the same way, with its explaining file named first; the account for a moved `since` is open point 11 in the plan; `enforce_on` is settled (T6(b) fails when no listed branch exists); the first is a phase-close re-read by a person.

## Synchronic documents that narrate their own history

**What:** many documents declared `view: synchronic` — the root README, `steering/roadmap.md`, `steering/foundation.md`, the `codifying/` fiches, `writing/frontmatter.md`, the comments in `docsys.yaml` and `steering/phases.yaml` — describe the changes that produced their content rather than the content: which phase did what, which ruling moved what, what a section used to say.
To a newcomer, they read as accounts under an `orient` or `describe` label.
They are also the style an agent imitates when it writes here, so each such page teaches the defect again.

**Why left open:** each page needs a judgment about what its declared reader needs, not a mechanical sweep; and the pages an adopter or an agent will read first matter more than the rest.

**How to resolve:** the rule, the revision test and the cold-reader pass are planned in [the adoption plan's T1](../phases/rush-to-mvp/phase-14-adoption/plan.md), starting with the pages the agent kit is built from; the long-term tools and the casebook of cases found are in [`imagining/reader-first-writing.md`](../imagining/reader-first-writing.md).
A page is paid when a cold-reader pass on it finds nothing it cannot place.

## Decision records that are plans

**What:** [ADR-020](../phases/refoundation/phase-06-refoundation/ADR-020-scope-phase-i.md) records a sequencing choice — which phase comes before which — and installs no standing obligation on how the system behaves, which [ADR-032](../phases/refoundation/phase-10-schema/adr-tiering.md) places in the roadmap, not the register.
[ADR-042](../phases/rush-to-mvp/phase-13-design/rush-to-mvp.md) inherits the defect by superseding it: its points 1 to 4 are sequencing, and only point 5, no new gate check on the project's own state, is a standing obligation.

**Why left open:** demoting a frozen record costs a register note and a reasoned exception for little gain while the era runs; the project owner chose not to fix it now.

**How to resolve:** demote ADR-020 the way ADR-019 was demoted (its record stays frozen; the register carries a note; the ordinal is retired), and either demote ADR-042 the same way with its moratorium moved into a record of its own, or let the moratorium lapse with the era.
