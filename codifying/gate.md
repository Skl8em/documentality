---
title: "The gate — one property, in a deliberate order"
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

**Read this before** adding, removing or reordering a check, or before trusting one line of the gate's output as a verdict on the corpus.
It is written for the maintainer, initiated in tooling engineering; the theory it enforces is [`operationalizing/`](../operationalizing/README.md)'s.

## What the gate is

One command, `python3 scripts/check.py`, and one exit status.
The same command runs in the opt-in pre-commit hook (`git config core.hooksPath .githooks`) and in CI (`nix develop --command python3 scripts/check.py`).
Phase 09's plan states the intent — every check reachable from one command that runs in pre-commit and in CI, and that also serves as the phase-close gate — and pairs it with a pinned toolchain, so local and CI run the same binaries ([Phase 09 plan](../phases/refoundation/phase-09-tooling/plan.md), *Guiding principles*).

The property it establishes is a **conjunction**: the gate is green if and only if every check is green.
It is not *the first failure stops the run*, and this was checked rather than assumed — [`scripts/test_check.py`](../scripts/test_check.py) pins that a failing check does not stop the ones after it.
The reason is the reader: a maintainer or an agent fixing a corpus wants every failure from one run, not one per run.

Red must mean *wrong*, never *unsettled*.
Phase 09 built this in as a rule:

> A linter that flags an open question trains people to ignore it.
> Contested rules warn; settled rules fail.

What the schema still leaves open is a warning and never fails the gate (`still_open` in the schema source); the gate's authority rests on that discipline, and one check that fails on an undecided question would spend it.

## What the order means

The checks run in the order [`docsys.yaml`](../docsys.yaml) lists them, and each entry carries, as a comment, the reason for its place.
Four reasons recur.

1. **What git cannot see goes first.**
   Every corpus check reads `git ls-files`, so an untracked file passes all of them silently; the `worktree` check exists to notice it.
   Modified tracked files do not fail it, because the gate is run on work in progress.
2. **The gate's own integrity before the checks that rely on it** — the `seam` and `runner` fixtures, which fail if the config is malformed, an instance value leaks into the engine, or the runner misattributes output.
3. **A generated input is verified before its consumers.**
   `schema-drift` runs before anything that loads `frontmatter-rules.json`.
4. **A check's fixtures run before the corpus run they gate** — `frontmatter-parser`, `ulid-test`, `md100`.
   A green corpus says nothing if the check has stopped detecting anything, so proof that it still detects comes first.

**The order is diagnostic, not protective.**
Because the runner does not stop at the first failure, an earlier failure does not prevent a later check from running on bad input.
This is easy to get wrong, so it was tried: the schema source was edited without regenerating the JSON, and the gate run.
`schema-drift` failed; `frontmatter` still ran against the stale JSON and printed `Frontmatter OK`; the summary named `schema-drift` alone.

So a green line is conditional.
It is a verdict on the corpus only when every check above it that it depends on is green too.
The order puts the root cause first in the output; it does not make later greens trustworthy.
`docsys.yaml` expresses order and nothing else — there is no way to say that one check *needs* another.

## The three kinds of entry, and why the runner is a separate thing

An entry in `checks:` is exactly one of `python:` (a script, run under the gate's interpreter), `builtin:` (a check implemented in `check.py` itself — today only `worktree`), or `tool:` (an external command).
`check.py` is only the runner; it holds no list of its own to drift out of step, and `test_seam.py` fails if a check's script name or path is ever hard-coded into the engine.
That is the seam — [`engine-config-seam.md`](../phases/refoundation/phase-12-codifying/engine-config-seam.md) — applied to the gate: which checks, and in what order, is *this repo's* instance; running them and reporting is the engine's.

To add a check: write the script and its fixtures, add the fixtures' entry *ahead of* the check's, and give each entry its reason as a comment.
The fixtures being in the gate is the point, not tidiness.

## The environment it enters

The gate needs `pyyaml` and a pinned `markdownlint-cli2`, both from the Nix devShell.
If `pyyaml` is not importable, the runner re-executes itself under `nix develop --command`; with neither, it stops with an instruction.
A `tool:` entry always prefers the pinned version, because the version is part of the contract with the custom rule the tool loads.

There is one soft spot, and a reader should know it.
When the devShell is not entered but a `pyyaml` or a tool is on the path, the gate proceeds with a `WARNING` line, and a warning does not fail it.
The gate can therefore go green on an unpinned markdownlint.
A human sees the warning; a machine reader must be told to treat it as material.

## The output contract

Each check is announced by a `=== name ===` header, flushed before the check runs.
When the output is a pipe — which is how CI and any agent see it — an unflushed header would arrive after the check's own lines and misattribute them; the runner fixes it and `runner` guards it.
Each failure line names the file, the rule and, after `fix:`, the edit that clears it.
The fixtures of `frontmatter_lint.py`, `ulid_check.py`, `paired_change.py`, `slug_check.py`, `linkcheck.py` and `hash_check.py` enforce the `fix:` clause: each builds its messages in a pure function, so a case can fail a message that lacks one.
Two are not covered: the drift message of `generate_schema.py --check`, which states its fix (`Run … and commit the result`) but not under the marker and has no fixture, and the runner's own messages; [technical debt](../steering/technical-debt.md) records both.

## The rule that keeps this shelf true

`paired-change` (`scripts/paired_change.py`, decided in [ADR-039](../phases/refoundation/phase-12-codifying/paired-change-rule.md) and refined by [ADR-040](../phases/refoundation/phase-12-codifying/paired-change-where-it-fails.md)) fails a change to `scripts/`, `schema/` or `docsys.yaml` that touches no file under `writing/`, `structuring/`, `operationalizing/` or `codifying/` and not `steering/ARCHITECTURE.md`.
Its lists — mechanism, understanding, what needs no account, the branches it is enforced on, and the anchor — are `paired_change:` in `docsys.yaml`, so the engine names none of them.
This fiche is one of the files that satisfies it, which is why a change to the gate lands with an edit here.

Four properties are easy to get wrong when touching it.

**The unit is the commit, not the branch.**
It examines every non-merge commit after `paired_change.since`, and the uncommitted work that will become the next one, each on its own.
A branch-level rule was tried against Phase 11 first and passes it: the phase touched three explaining documents incidentally, and on a phase-long branch any such edit pairs every script edit.
So a later docs commit never pairs an earlier scripts commit, and the account goes in the same commit as the change.

**Two kinds of change are not a change to the mechanism.**
A file under an `exempt` prefix (`scripts/test_`) and a Python edit whose syntax tree, docstrings set aside, is unchanged — comments, docstrings, formatting — have nothing to explain, so they need no account, on any branch.
The second is a comparison of the file before and after, so it is a heuristic on the tree and not on intent: a docstring that replaces the description of unchanged behaviour passes, and only Python is examined.
A version that does not parse, or a file added or deleted, is never comment-only.

**It fails only where work lands.**
On a branch in `enforce_on` (`main`, `develop`) and on a detached HEAD — which is what CI checks out for a pull request — a finding fails the gate.
On any other branch the same finding is a `WARNING` naming the branch and where it is enforced, and the exit status is 0, so a mechanism commit may precede the commit that explains it while the work is in progress.
The cost moved, it did not vanish: the pull request examines every commit since the anchor, so the earlier commit fails there and has to be amended or squashed with its account.
If the integration branch is renamed and `enforce_on` is not, the rule quietly becomes a warning, and nothing in the gate says so.

**The anchor is the only exemption from history, and it shows in a diff.**
Commits before `since` are not examined.
A violating commit that is already made cannot be repaired by adding docs afterwards; moving `since` past it is the way to accept it, and that is an edit to a tracked file that a reviewer sees.
An anchor that cannot be resolved (a shallow clone; a commit not in this history) is an error, never a pass, and that is why CI fetches full history.

**It reads git, so it depends on where it runs.**
Run by hand or from the opt-in hook it sees the working tree; in CI it sees the commits pushed.
A clone that has not opted into the hook meets the failure only in CI, after the commit exists.

It checks co-occurrence, and a one-word edit to a fiche passes; what it removes is the silent case.
`docsys.yaml` is in the mechanism list since Phase 12 T6: it decides what the gate runs and where the rule bites, so a change to it is a change to the tooling.
That includes moving `since`, which accepts a commit and so needs an account like any other change.
The phase ledger is kept out of `docsys.yaml` for this reason: it lives in `steering/phases.yaml`, `phases.ledger` points at it, and a phase transition is a ruling the roadmap explains, not a change to the tooling.
A change confined to `tools/markdownlint/` is still invisible to the rule.

## What the gate does not establish

- **That the documents are good.**
  It checks structure — frontmatter, links, identifiers, fixity seals, one-sentence-per-line — not whether a document's force is the right one, or its claims true.
- **That a fix is correct**, only that one is stated.
- **That the checks cover what matters.**
  The gate can only be as broad as the list; a whole class of failure with no check is invisible to it.
  The paired-change check below exists because one such class, the tooling changing unexplained, went unseen twice.
- **That an account of the tooling is true.**
  `paired-change` establishes that a change to the mechanism came with an edit to a file that explains it, not that the edit says what the code now does.
- **Fixity for every frozen record.**
  Frozen records that predate the seal carry none; the gate counts them and does not fail on them (`hash_check.py --unsealed` lists them).

## Alternatives not built

Neither was recorded as decided in any phase, so what follows is the trade-off, not a history.
**Fail fast** would make the order protective and the run shorter, at the price of one failure per run.
**Explicit dependencies** (`needs:` between checks) would let a green line mean the same thing regardless of what is above it, at the price of a small scheduler the gate does not otherwise need.
Neither has been asked for yet; the conditional green described above is the case for the second.
