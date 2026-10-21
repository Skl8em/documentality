---
title: "Phase 14 adoption — the rulings"
force: describe
intention: state
view: synchronic
provenance: { type: project, id: phase-14-adoption }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

The rulings the project owner has taken for Phase 14, each in full, with the date it was taken.
The [plan](plan.md) lists them in a line each; this page is where one is read, and where a ruling is amended in place.

## A package, not a vendored copy

Project owner, 2026-10-09.
One engine that adopters pin, rather than a copy forked into each project.

## The layout default for an adopter's docs

Project owner, 2026-10-09.
By **function** first, then by **sub-function**, then by **register** (`know` / `do` / `govern`), then by **force** — each split made only when the level above has grown enough to need it, fractally.
This extends what the [structuring tutorial](../../../structuring/tutorial.md) already says (function first, register inside it) and contradicts `structuring/setup.md`, which lays docs out by force at the top.

## `weft` is the first adopter

Its repository was initialised on 2026-10-08.

## The engine is `Skl8em/docsys`

Project owner, 2026-10-10.
[`Skl8em/docsys`](https://github.com/Skl8em/docsys) is public, licensed by kind of artefact ([ADR-043](../phase-13-design/licensing.md)); it is mounted in this repository as a git submodule at `docsys/`, beside `scripts/`, which it replaces.
The provenance rule shelves documentation; tooling and configuration folders — `scripts/`, `docsys/`, `LICENSES/`, `.githooks/` — are not shelves.

## The scope

Project owner, 2026-10-10.
Every document is in scope by default; an exclusion takes documents out and carries the reason, so it can be read and argued; an inclusion brings back documents an exclusion took out.
Both are lists in `docsys.yaml`, both optional.
The excluded documents are the ones still owed: see *Strictness* below.

## Where the engine's documentation lives

Project owner, 2026-10-10.
How a project uses `docsys` and configures it is documented here, in `codifying/`; how the engine works inside is documented in `docsys/docs/`, each fiche moving there when the check it explains is ported, since until then it explains `scripts/`.

## The tools for Python

Project owner, 2026-10-10.
basedpyright checks types and ruff lints and formats, at the versions the engine's lockfile pins, run by its test suite and by the editor alike; `ty`, Astral's type checker, is to be evaluated later as an option.

## The checks that are not the engine's

Project owner, 2026-10-20.
They run as opt-in tools: a `tools` section of `docsys.yaml` names external commands, and `docsys check` runs them after its own checks.

## What precedes the switch, and what it retires

Project owner, 2026-10-20 and 2026-10-21.
The accounts of the extracted checks move to `docsys/docs/` first.
A link from a frozen record to a file the switch removes is allowed by the engine's link check, from a list in `docsys.yaml` that gives each allowance its reason, rather than by editing the record or turning the rule down.
The author tools of `scripts/` (`hash_seal.py`, `rename_doc.py`, `slugify_names.py`, `ulid.py`) are ported to the engine before the switch, not kept here; `migrate_ids.py` goes unchanged to a `legacy/` folder of the engine, as a lead for a utility after the MVP.
`schema/` is retired with `scripts/`, the engine's copy becoming the one vocabulary, by an ADR that supersedes [ADR-037](../../refoundation/phase-11-tooling-hardening/yaml-source-generated-json.md).

## Every Markdown file is a document, whatever git knows of it

Project owner, 2026-10-21.
A document is a `.md` file anywhere under the workspace but inside `.git`; `.gitignore` is not consulted, so a virtual environment, a dependency folder or a submodule leaves the scope only through `scope.exclude`, with its reason, like any other exclusion.
A submodule's files are documents too, on purpose: the engine, mounted here as `docsys/`, falls under this repository's rules.
After the MVP a submodule is to be excluded by default and opted in explicitly ([roadmap](../../../steering/roadmap.md), *Parked*).
The worktree check of `scripts/` is retired with it, not ported: it existed because `scripts/` read only tracked files.
The engine's test of the sentence-per-line rule reads the output of any `markdownlint-cli2` version; moving the pinned version past 0.17.2 is parked until after the MVP, since staying breaks nothing.

## Closing ws2

Project owner, 2026-10-21.
ws2 is finished before ws1's remaining defects, and continuous integration of both repositories comes first, pushed to verify it.
The engine gets its own CI and pre-commit hook, rather than this repository's gate running its suite; this repository's own checks (the editor's markdownlint version, the VS Code task's problem matchers) run as `tools:` entries from a folder here; after the switch the paired-change rule's mechanism is `docsys.yaml`, that folder, `.githooks/`, `.github/workflows/` and `flake.nix`, the submodule pointer still to rule; the hook and CI run `uv run --locked docsys check` inside the devShell.
The steps are in [Closing ws2](ws2-closing.md).

## How a plan is divided

Project owner, 2026-10-21.
A phase into **workstreams** (ws1–ws5), which may run side by side and have no branch; a workstream into **tracks**, each a branch merged into the phase branch, so the tracks of different workstreams land in any order; a track into **tasks**, each sized for one agent session without running out of context, each a branch merged into its track's; a task into **steps**, each one commit.
In branch names and commit subjects the levels are `ph`, `ws`, `tr`, `ts` and `sp`, and no branch carries a `feature/` prefix.
Work at every level is numbered when it starts, never before, as [ADR-038](../../refoundation/phase-11-tooling-hardening/unstarted-work-unnumbered.md) says of phases; a step, being a commit, takes no number.
This phase applies it as far as its plan allows: its workstreams keep the numbers this plan gave them, and [Closing ws2](ws2-closing.md) is divided by it; every phase after Phase 14 is planned by it.
The binding rule is in [`CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md); dividing a plan into any number of levels is parked until after the MVP ([roadmap](../../../steering/roadmap.md), *Parked*).

## Strictness

An adopter's existing documentation does not become compliant at once, and the gate must not demand it; it must also not let a document slip back out once it is in.

- **Every document is in scope by default**, so a new project needs no configuration for the gate to check everything.
- **An exclusion takes documents out, with its reason**: `scope.exclude` in `docsys.yaml` maps a pattern to why the documents it matches are not checked.
  The reason is required, so each exclusion can be read and argued in review.
  `docsys init` excludes every document already in the repository, with the reason "predates docsys; awaiting review".
- **An inclusion brings a document back**: a pattern in `scope.include` wins over an exclusion.
  A legacy document is adopted by including it once revised, an edit visible in review; a new document is in scope from the start.
- **The gap is accounted for**: `docsys report` lists the exclusions with their reasons and counts, and `--documents` the excluded documents, and prints their count, so the reduction is visible over time.
- **Each rule has a severity** — error, warning or off — configurable per rule in `docsys.yaml`, with the methodology's defaults.
  A rule the methodology states as a heuristic (the sentence-per-line rule, the "suspect pair") defaults to a warning.
