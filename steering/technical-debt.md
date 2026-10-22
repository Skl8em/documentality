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

**How to resolve (when we choose):** add `id`/`slug` to a record's frontmatter (mint with `docsys id` — ADRs chronological, phases ordinal via an `order` key), then normalise its filename with `docsys slugify` (→ `<slug>.md`), which rewrites every link to it and leaves the link, slug and identifier checks to verify the result ([`docsys-commands.md`](../codifying/docsys-commands.md)).
The other direction, `<slug>-<ulid>.md`, has no command: `migrate_ids.py` is parked, unported, in the engine's `legacy/`.

## Linter-grandfathered content

**What:** `phases/naive-sketch/**` (pre-ADR-021 records), `imagining/**` (proposals and informal notes), and the blind-test transcripts are excluded from markdownlint, and all but `imagining/**` from the engine's checks.

**Why:** they predate the current conventions or are not authored prose; forcing them into compliance would be churn without value.

**How to resolve:** bring a file into the catalogue (frontmatter + one-sentence-per-line) and remove it from the ignore lists when it stops being historical/informal — case by case, not in bulk.
There are two lists: `scope.exclude` in [`docsys.yaml`](../docsys.yaml) for the engine's checks, and `.markdownlint-cli2.jsonc` for markdownlint, which reads only its own config; nothing checks that they agree.

## Unsealed frozen records

**What:** frozen records that carry no `hash:` fixity seal (ADR-031); the rule that reports them, `hashes/unsealed`, is off by default, and `rules:` in `docsys.yaml` turns it on.
The naive-sketch era (phases 01–05), which the scope excludes, is the bulk of it.

**Why left open:** sealing is an act performed *at freeze*, and those records were frozen before the seal existed.
Back-sealing them fixes their *current* content, not the content they had when they closed — which is an honest thing to do, but it should be a deliberate act rather than a bulk sweep.

**How to resolve:** `docsys seal <path>` per record, or `docsys seal --frozen` for every frozen record of the scope at once.
Note that sealing a record makes any later edit to it fail the gate until it is consciously re-sealed — that is the point, and the cost.

## Paid

- **Reorg leftovers (untracked on-disk zombies)** — the three untracked directories the Phase-08 renames left on disk (`theory/`, `write/`, a top-level `phases/phase-07-structuring-tutorial/` husk) are gone, and the root `.gitignore` stops the `.DS_Store` files that blocked their deletion from coming back.
  The real lesson is paid too: the gate reads every Markdown file on disk, tracked or not, so on-disk cruft cannot pass it unseen.
- **Duplicated round-2 blind-test transcripts** — the `weft-blindtest-round2/` directory was byte-identical to the `blind-test/weft-{response,review}-round2.md` copies and was deleted; the `blind-test/` copies stay, sitting with round 1 (Phase 10).
- **Referential integrity: cycles and self-supersession pass** — the ULID check rejects a record that names itself in `supersedes` or `superseded-by`, and a loop along `superseded-by`, each with a fixture that was red first; the [referential-integrity fiche](../docsys/docs/referential-integrity.md) states it (Phase 12 T4).
- **A register whose row shape matches nothing passed** — the register check fails when it finds no decision rows, with fixtures for an empty register, a wrong column count and a non-matching ordinal; the [referential-integrity fiche](../docsys/docs/referential-integrity.md) states it (Phase 12 T4).
- **Gate messages without their fix** — every finding of the engine carries its `fix:` clause, and its conformance suite fails a finding that lacks one; the two sources that had no fixture, the schema's drift message and the old runner's own, retired with `scripts/` (ADR-044).
- **Closed vocabulary without a fixture** — the engine's frontmatter check has a case for an undeclared field (`frontmatter/vocabulary`), and its vocabulary refuses to load an optional field without its reason, with a test for each.
- **A renamed integration branch silently disarmed the paired-change rule** — the rule fails, on every run, when no branch in `enforce_on` exists locally or on a remote, with fixtures for a stale list and a remote-only branch; the [paired-change fiche](../docsys/docs/paired-change.md) states it (Phase 12 T6(b)).

## Engine/config seam residue

**What:** the engine reads every path, prefix and register format from `docsys.yaml`, a seam drawn from a single instance, this repository ([Phase 12 T1(b)](../phases/refoundation/phase-12-codifying/engine-config-seam.md)).
And the definition of a *frozen* record lives in the engine's code (`FROZEN_STATUSES` in its fixity check), where it duplicates a fact the vocabulary also states, its status vocabulary, guarded by a test that fails when a declared status is classified neither frozen nor open.

**Why left open:** the single-instance boundary cannot be tested without a second consumer.
The frozen definition belongs in the vocabulary in principle, but declaring it there widens the vocabulary and rules on part of what its `still_open` list calls the status vocabulary — a ruling, not a refactor, and not one this debt should take by side effect.

**How to resolve:** revisit the seam when `weft` adopts the engine (ws4 of [Phase 14](../phases/rush-to-mvp/phase-14-adoption/plan.md)).
Move the frozen definition into the engine's vocabulary, and retire the guard, when the status vocabulary is ruled.

## Paired-change: what the rule does not see

**What:** the [paired-change rule](../phases/refoundation/phase-12-codifying/paired-change-rule.md) (ADR-039, refined by [ADR-040](../phases/refoundation/phase-12-codifying/paired-change-where-it-fails.md)) has these gaps, each scheduled in the [Phase 12 plan](../phases/refoundation/phase-12-codifying/plan.md#open-points-and-when-each-is-settled):

- It checks that a file explaining the tooling was edited, not that the edit is true; a docstring that replaces the description of unchanged behaviour is exempt, and only Python is examined for comment-only edits.
- The pre-commit hook is opt-in (`git config core.hooksPath .githooks`): a local setting no clone inherits.
  It was enabled in the author's clone on 2026-09-25; elsewhere a violation is found at the pull request, after the commit exists, and once shared the only remedy is moving `paired_change.since`.
  On a feature branch the hook shows the warning but does not block a paired-change violation (ADR-040); it blocks on every other check.
- On a feature branch a violation is only a warning, so a mechanism commit followed by its account passes there and fails at the pull request, which examines every commit since the anchor.
  How costly that is on a phase-long branch is unmeasured.
- `docsys.yaml` joined the mechanism list in T6, once the phase ledger was ruled out of it; moving `paired_change.since` now needs an account in the same commit, and no explaining file is an obvious home for one.
- A rename or a behaviour-free refactor still asks for an account; only tests and comment-only edits are exempt.

**Why left open:** the first is what any co-occurrence rule costs and only a reader can close it; the second is a property of git hooks, which are not versioned into a clone (a clone must opt in); the third is the price of not blocking work in progress, chosen in ADR-040; the fourth: the cost of accounting for a moved `since` is new and unmeasured; the last awaits evidence.

**How to resolve:** the plan's table names the step for each — the hook is enabled in the author's clone, and T4 (its first real use) showed it ran the gate on every commit and blocked nothing, so it has not yet been seen to catch a violation — the project owner's verdict on it is still open; the merge-time cost is observed on Phase 12's own merge in T5; the `docsys.yaml` gap is closed (T6 split the ledger into `steering/phases.yaml` and listed `docsys.yaml` as mechanism); the markdownlint rule is the engine's now, and is paired there; the account for a moved `since` is open point 11 in the plan; `enforce_on` is settled (T6(b) fails when no listed branch exists); the first is a phase-close re-read by a person.

## Synchronic documents that narrate their own history

**What:** many documents declared `view: synchronic` — the root README, `steering/roadmap.md`, `steering/foundation.md`, the `codifying/` fiches, `writing/frontmatter.md`, the comments in `docsys.yaml` and `steering/phases.yaml` — describe the changes that produced their content rather than the content: which phase did what, which ruling moved what, what a section used to say.
To a newcomer, they read as accounts under an `orient` or `describe` label.
They are also the style an agent imitates when it writes here, so each such page teaches the defect again.

**Why left open:** each page needs a judgment about what its declared reader needs, not a mechanical sweep; and the pages an adopter or an agent will read first matter more than the rest.

**How to resolve:** the rule, the revision test and the cold-reader pass are planned in [the adoption plan's ws1](../phases/rush-to-mvp/phase-14-adoption/plan.md), starting with the pages the agent kit is built from; the long-term tools and the casebook of cases found are in [`imagining/reader-first-writing.md`](../imagining/reader-first-writing.md).
A page is paid when a cold-reader pass on it finds nothing it cannot place.

## Decision records that are plans

**What:** [ADR-020](../phases/refoundation/phase-06-refoundation/ADR-020-scope-phase-i.md) records a sequencing choice — which phase comes before which — and installs no standing obligation on how the system behaves, which [ADR-032](../phases/refoundation/phase-10-schema/adr-tiering.md) places in the roadmap, not the register.
[ADR-042](../phases/rush-to-mvp/phase-13-design/rush-to-mvp.md) inherits the defect by superseding it: its points 1 to 4 are sequencing, and only point 5, no new gate check on the project's own state, is a standing obligation.

**Why left open:** demoting a frozen record costs a register note and a reasoned exception for little gain while the era runs; the project owner chose not to fix it now.

**How to resolve:** demote ADR-020 the way ADR-019 was demoted (its record stays frozen; the register carries a note; the ordinal is retired), and either demote ADR-042 the same way with its moratorium moved into a record of its own, or let the moratorium lapse with the era.
