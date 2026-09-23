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
The fixtures of `frontmatter_lint.py` and `ulid_check.py` enforce the `fix:` clause; three validators build their messages inline and are not fixture-covered ([the audit](../phases/refoundation/phase-12-codifying/error-message-audit.md) and [technical debt](../steering/technical-debt.md) say which).

## What the gate does not establish

- **That the documents are good.**
  It checks structure — frontmatter, links, identifiers, fixity seals, one-sentence-per-line — not whether a document's force is the right one, or its claims true.
- **That a fix is correct**, only that one is stated.
- **That the checks cover what matters.**
  The gate can only be as broad as the list; a whole class of failure with no check is invisible to it, which is the reason `plan.md` gives for T3.
- **Fixity for every frozen record.**
  Frozen records that predate the seal carry none; the gate counts them and does not fail on them (`hash_check.py --unsealed` lists them).

## Alternatives not built

Neither was recorded as decided in any phase, so what follows is the trade-off, not a history.
**Fail fast** would make the order protective and the run shorter, at the price of one failure per run.
**Explicit dependencies** (`needs:` between checks) would let a green line mean the same thing regardless of what is above it, at the price of a small scheduler the gate does not otherwise need.
Neither has been asked for yet; the conditional green described above is the case for the second.
