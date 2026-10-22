---
title: "The gate — one command, every check, one verdict"
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

One command, `uv run --locked docsys check`, run inside the Nix devShell, and one exit status.
The same command runs in the opt-in pre-commit hook (`git config core.hooksPath .githooks`), in CI, and in the VS Code task `docs: run the gate`; the hook and the task enter the devShell first when they are started outside it.
This repository runs [`docsys`](https://github.com/Skl8em/docsys) as an adopter does, installed from the submodule `docsys/` at the commit it pins; [`docsys-commands.md`](docsys-commands.md) is the reference for this command and the others, and [`docsys-configuration.md`](docsys-configuration.md) for every key of [`docsys.yaml`](../docsys.yaml).

The property it establishes is a **conjunction**: the gate is green if and only if no finding is an error.
A failing check does not stop the ones after it, nor a failing tool the next; the reader, a maintainer or an agent fixing a corpus, wants every failure from one run, not one per run.
The engine's [runner fiche](https://github.com/Skl8em/docsys/blob/main/docs/runner.md) says how a run is made and what makes it fail.

Red must mean *wrong*, never *unsettled*.
Phase 09 built this in as a rule:

> A linter that flags an open question trains people to ignore it.
> Contested rules warn; settled rules fail.

What the vocabulary still leaves open is a warning and never fails the gate (`frontmatter/open`); a rule the methodology states as a heuristic is a warning too; and the gate's authority rests on that discipline, since one check that failed on an undecided question would spend it.
This repository changes no rule's severity: `docsys.yaml` has no `rules:` section.

## What it checks, and in what order

The engine's checks run first, in the engine's order: links, frontmatter, identifiers, slugs, fixity, the paired-change rule, the phase ledger, the phase state.
The order is a reading order, not a dependency: no check relies on another having run, and one defect is reported once, by the check that owns it.
Which of them run is this repository's choice, made by the sections `docsys.yaml` carries: the register, the paired-change rule and the phases are all configured here, so every check runs.

Their fixtures are the engine's: its conformance suite and its tests run in the engine's own CI and hook, and not in this gate.
A green run here trusts the engine at the commit the submodule pins; a pointer moved to an engine commit whose own checks are red would not turn this gate red.

Then the tools run, in the order `docsys.yaml` lists them under `tools:`, each one's output printed under its name:

1. **`markdownlint`** — `markdownlint-cli2`, with one shared ruleset and the custom one-sentence-per-line rule (ADR-021), which the engine ships in `docsys/src/docsys/markdownlint/` and tests in its own suite.
   Its configuration is its own, [`.markdownlint-cli2.jsonc`](../.markdownlint-cli2.jsonc), with its own list of what it skips.
2. **`problem-matcher`** — the fixtures of the editor's problem matchers (*The output contract*, below).
3. **`editor-markdownlint-test`**, then **`editor-markdownlint`** — the fixtures, then the check that the editor's markdownlint is the gate's (*The environment*, below).
   It runs last, because it judges this machine's editor and not the corpus.

A check's fixtures run before it, because a green check says nothing if it has stopped detecting anything.

To add a check, ask who needs it.
A check that every project adopting the system needs goes to the engine, with its conformance cases written red first, and is paired there with its account.
A check that only this repository needs is a program in [`tools/`](../tools/), this repository's own checks, with its fixtures listed ahead of it under `tools:`, and an account here.

## What it reads

Every Markdown file under the workspace is a document, tracked by git or not, unless `scope.exclude` in `docsys.yaml` leaves it out, with its reason: the upstream essays of `theorising/`, the pre-refoundation records of `phases/naive-sketch/`, the agent's `.claude/`, raw agent transcripts, the engine's submodule `docsys/`, which is another repository checked by its own CI, and the folders uv and direnv build.
`docsys report` lists the exclusions with their reasons and counts.
Because the gate reads the disk and not git's index, an untracked file is checked like a tracked one, and no separate check for untracked files is needed.

## The environment it enters

The devShell pins the interpreter, `uv`, Node, `markdownlint-cli2` and the `git` through which the paired-change rule reads the history, through `flake.lock`; `uv.lock` pins `docsys`, installed editable from the submodule, and its Python dependencies, and `--locked` refuses to run on a lockfile that no longer matches `pyproject.toml`.
CI enters the devShell, runs `uv sync --locked`, then the gate.
`docsys` does not pin the tools it runs: it runs what the `PATH` finds, and inside the devShell under `uv run`, `markdownlint-cli2` is the flake's and `python3` the virtual environment's.
The pinned versions are part of the contract: markdownlint's version is part of the contract with the custom rule it loads, and a YAML parser from another environment could read a frontmatter differently.
[`environment.md`](../steering/environment.md) says how to enter the devShell.

The editor lints Markdown as well, through its markdownlint extension, and that extension cannot be pointed at the devShell's binary: it runs the `markdownlint-cli2` it bundles.
`editor-markdownlint` (`tools/editor_markdownlint.py`) compares the two on the machine it runs on, and fails when the extension bundles another version than the one `flake.lock` pins, or when two copies of it are installed; it refuses, with a fix, a VS Code `extensions.json` or extension manifest of a shape it does not know, rather than guess.
Where VS Code has no extensions (CI) it passes and says there is nothing to compare; `environment.md` names the release of the extension that matches the flake.

## The output contract

`docsys check` prints its error findings, one per line, as `path:line: rule: message — fix: the edit that clears it`; then, under `warnings (N), reported without failing the run:`, its warning findings, the same line indented by two spaces; then each tool's output under `=== name ===`; then one line, `docsys check passed` or `docsys check failed`, with the counts.
A refused `docsys.yaml` stops the run before any check, with one line, `docsys: docsys.yaml: message — fix: …`, and exit `2`.
Every finding names its file, its line, its rule and, after `fix:`, the edit that clears it; the engine's checks build their messages that way, and its conformance suite fails a finding without its fix.
The lines of a tool are the tool's own; this repository's checks follow the same rule, and their fixtures enforce the `fix:` clause.

The editor reads the same output.
VS Code's task `docs: run the gate` ([`.vscode/tasks.json`](../.vscode/tasks.json)) reads the output of `docsys check` through four problem matchers, which put each failure in the Problems pane on the file and line it names, with its rule: an error finding, `path:line: rule: message — fix: …`; a warning finding, the same line indented by two spaces; a line of `markdownlint-cli2`, `path:line[:column] rule/alias message`; and a refused `docsys.yaml`, `docsys: docsys.yaml: message`, which names the file only.
So the shape of a line is part of the contract: a failure on a file starts with its path, which holds no whitespace, in one of those forms, and no other line may, a green summary least of all.
`problem-matcher` (`tools/test_problem_matcher.py`) runs the four patterns over lines of each shape, copied from real runs, and over the lines that must stay out of the pane.

## The rule that keeps this shelf true

The paired-change rule ([ADR-039](../phases/refoundation/phase-12-codifying/paired-change-rule.md), refined by [ADR-040](../phases/refoundation/phase-12-codifying/paired-change-where-it-fails.md)) fails a commit that changes the mechanism and touches no file under `writing/`, `structuring/`, `operationalizing/` or `codifying/` and not `steering/ARCHITECTURE.md`.
This fiche is one of the files that satisfies it, which is why a change to the gate lands with an edit here.
How the rule works — the commit as the unit, what needs no account, where it fails rather than warns, the anchor, and what it does not establish — is explained with the engine's check, in [the paired-change fiche](https://github.com/Skl8em/docsys/blob/main/docs/paired-change.md).

What is this repository's is the configuration, `paired_change:` in `docsys.yaml`:

- **The mechanism** is what decides what the gate runs and how: `docsys.yaml`, this repository's own checks in `tools/`, the hook in `.githooks/`, the CI workflows in `.github/workflows/`, and the devShell's `flake.nix`.
  `docsys.yaml` includes moving `since`, which accepts a commit and so needs an account like any other change.
- **The tests of `tools/`** (`tools/test_`) are exempt: they explain themselves.
- **The submodule pointer `docsys` is not mechanism.**
  The engine's changes are paired with their accounts in the engine's repository; listed here, every pointer commit would need an account of its own in the same commit.
- **The anchor, `since`**, is the last commit before the gate became `docsys check`: the commits before it answered to the old mechanism list, `scripts/`, `schema/` and `docsys.yaml`, and the new list would fail every one that touched those paths.
- **The rule fails on `main` and `develop`**, and on a detached checkout, which is how CI sees a pull request; anywhere else it warns, so work in progress is not blocked.
  CI fetches the full history, since an anchor it cannot reach is an error.
- **The phase ledger is kept out of `docsys.yaml`**: it lives in `steering/phases.yaml`, `phases.ledger` points at it, and a phase transition is a ruling the roadmap explains, not a change to the tooling.
- **The hook is opt-in**, so a clone that has not opted in meets a violation only in CI, after the commit exists.

## Where the project is: the ledger and the phase-state check

The current phase is declared once, in the ledger [`steering/phases.yaml`](../steering/phases.yaml): an ordered list of phases, each `done`, `current` or `planned`, the planned ones unnumbered (ADR-038).
It is the project's state, kept with steering; `phases:` in `docsys.yaml` only says where it is and how to read every other place that speaks of the current phase.
The phase-ledger check verifies the ledger's own rules, and the phase-state check every other place against it; what each rule verifies, and why, is explained with the engine's checks, in [the phase-ledger and phase-state fiche](https://github.com/Skl8em/docsys/blob/main/docs/phase-state.md).

What is this repository's is where those places are: the phase folders under `phases/<era>/`, the phase rows of the [roadmap](../steering/roadmap.md) and of the [phases index](../phases/README.md) with their markers (`done`, `in progress`, `unnumbered`; the text after a ` — ` is free), the status line of the root `README.md`, and the `phase:` fields.
The root `README.md` is also the root document, the one that carries the tree's `axis` and `dominant-community`.

What the gate does not check yet: that a closed phase's README says `done` and its records are sealed.
That rule, as planned, conflicts with ADR-031's choice to leave the naive-sketch era unsealed and rests on a `status` vocabulary nobody has ruled, so it was handed to the life-cycle phase ([roadmap](../steering/roadmap.md); open point 12 in the [Phase 12 plan](../phases/refoundation/phase-12-codifying/plan.md#open-points-and-when-each-is-settled)).

Starting a phase is one edit to the ledger, and the gate then names every place still describing the old one.

## What the gate does not establish

- **That the documents are good.**
  It checks structure — frontmatter, links, identifiers, fixity seals, one-sentence-per-line — not whether a document's force is the right one, or its claims true.
- **That a fix is correct**, only that one is stated.
- **What lies outside the scope.**
  An excluded document is not checked at all; `.claude/`, the agent's own configuration and skills, is not documentation, and the contributing rules a skill applies are written in [`CONTRIBUTING.md`](../steering/CONTRIBUTING.md), which the gate does check.
- **That the engine still detects what it claims to.**
  Its fixtures run in its own repository, not here.
- **That the checks cover what matters.**
  The gate can only be as broad as its checks; a whole class of failure with no check is invisible to it.
  The paired-change rule exists because one such class, the tooling changing unexplained, went unseen twice.
- **That an account of the tooling is true.**
  The paired-change rule establishes that a change to the mechanism came with an edit to a file that explains it, not that the edit says what the code now does.
- **That a place which agrees with the ledger is true.**
  The phase-state check verifies that the roadmap, the index and the status line name the right phase, not that what they say of it is right.
- **That VS Code shows what the gate prints.**
  `problem-matcher` tests the patterns with Python's `re`, which reads them as JavaScript does only because they use nothing the two read differently; VS Code's own reading of them is not tested.
- **Fixity for every frozen record.**
  Frozen records that predate the seal carry none, and the rule that reports them, `hashes/unsealed`, is off by default.
