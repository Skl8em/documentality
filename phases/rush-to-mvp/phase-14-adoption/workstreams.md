---
title: "Phase 14 adoption — the workstreams"
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

What each workstream of Phase 14 covers, what it delivers, and, for ws2, where it stands.
The [plan](plan.md) lists the workstreams with a status of a few words; a change of state is made here, in the paragraph or bullet it changes, never as a growing row of a table.

## ws1 — Fix what the kit will teach

An agent applies a page literally, so these are fixed before the kit is built from them.

1. The root README's "New here?" block, broken since 2026-07-25.
2. The layout ruling applied: `structuring/setup.md` section A and `structuring/defaults.md`'s in-repo axis rewritten to it, the tutorial's rule extended with sub-function and force, and the CHANGELOG's register made consistent (the tutorial says `govern`, `setup.md` says `account`).
3. The orient template and step 3 of the writing tutorial stop producing the "suspect pair" (`synchronic` under a project's provenance).
4. `writing/forces/know/describe/README.md` declares `force: explain, verb: illuminate` — its own stance, mislabelled.
5. The *Validation rules* of `writing/frontmatter.md` say which rule the gate enforces and which it does not.
6. CI's Nix installer pinned rather than `@main`.

Prose that narrates its own history ([`imagining/reader-first-writing.md`](../../../imagining/reader-first-writing.md)):

1. The rule and its revision test added to [`writing/rules.md`](../../../writing/rules.md) — a synchronic document states the present for its declared reader, and the account of a change goes to the commit, the changelog or the reply.
2. A cold-reader pass — a subagent with no conversation history, given one page and its declared audience — over the pages the kit is built from (the root README, the writing and structuring tutorials, `writing/frontmatter.md`, the force stances and templates).
3. The pages it flags rewritten, starting with those edited when this phase opened (the root README's status paragraph, `steering/foundation.md` §1, `imagining/README.md`).

Each case the project owner finds is added to the casebook and fixed the same way, until the project owner judges the result satisfying.

Delivers: the six defects fixed; the rule in `writing/rules.md`; a cold-reader record per page passed; the casebook grown; the gate green.

## ws2 — The engine as a Python package, `docsys`

An adopter declares it as a development dependency in its `pyproject.toml`, pinned to a git tag and locked by its own lockfile; this repository installs it the same way, editable (`pip install -e` or the `uv` equivalent), so it is its own first consumer.
Fixtures first, against a throwaway adopter repository built by the test — the second consumer the seam lacks.

1. **The workspace is explicit**, on `weft`'s model: the CLI finds it as the nearest ancestor holding `docsys.yaml`, the way `make` finds its control file, or takes `--workspace`; the library takes it as a parameter; nothing is changed or read from the current directory at import.
2. **Strictness is configurable** — see *Strictness* in the [rulings](rulings.md).
3. The `register`, `paired_change` and `phases` sections of `docsys.yaml` become optional, and their checks run only when configured.
4. The root document is configurable, defaulting to `README.md`.
5. `pyyaml` comes with the package, so Nix is optional; markdownlint and its custom rule stay available, opt-in, since they need Node.
6. A `docsys` CLI: `docsys check` runs the configured gate, `docsys report` lists the documents not yet compliant.
   The schema ships inside the package.
7. **The cross-package API is honoured from the start**, since every later package must read the same files ([`imagining/multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md)): `docsys.yaml` carries a format version, every finding carries a rule identifier beside its `fix:` clause, and the fixtures for the methodology's rules are data files (input documents and expected findings) rather than Python test code.

Delivers: the `docsys` package, in its own repository, with fixtures; this repository consuming it; `codifying/` fiches updated in step.

### Where ws2 stands

Each bullet states what holds now; a step that changes it rewrites its bullet.
The steps still to take are walked in [Closing ws2](ws2-closing.md).

- **Where the engine is.**
  [`Skl8em/docsys`](https://github.com/Skl8em/docsys), mounted here at `docsys/` and declared in this repository's `pyproject.toml` as an editable development dependency.
- **Workspace and configuration.**
  The workspace is the nearest directory holding `docsys.yaml`, or `--workspace`; exit codes are 0, 1 and 2.
  The configuration loader reads the format version, the scope, the root document and the optional `register`, `paired_change` and `phases` sections, listed key by key in [`codifying/docsys-configuration.md`](../../../codifying/docsys-configuration.md).
- **Documents.**
  The documents are the Markdown files anywhere under the workspace but inside `.git`, filtered by the scope; git's index and `.gitignore` are not consulted, and the walk follows no symlink and skips a folder the scope leaves out wholly.
  A workspace need not be a git repository.
- **Checks.**
  Every check of `scripts/` that belongs to the engine is extracted, and each is stated case by case in `docsys/conformance/<check>.yaml`, which the package's tests run:

  | Check | Rules | Conformance file |
  | --- | --- | --- |
  | links | `links/resolve` | `links.yaml` |
  | slugs | `slugs/type`, `form`, `filename` | `slugs.yaml` |
  | ULIDs | `ulids/form`, `unique`, `resolve`, `self`, `symmetric`, `cycle`, `register` | `ulids.yaml` |
  | fixity | `hashes/seal`, `hashes/unsealed` (off by default) | `hashes.yaml` |
  | phase ledger | `ledger/missing`, `yaml`, `shape`, `form`, `number`, `unique`, `current`, `order`, `lagging` | `ledger.yaml` |
  | phase state | `phase-state/ledger`, `folder`, `table`, `mention`, `status`, `field`, `lagging` | `phase-state.yaml` |
  | paired change | `paired-change/unpaired`, `advisory`, `anchor`, `branches` | `paired-change.yaml` |
  | frontmatter | `frontmatter/yaml`, `missing-block`, `required`, `provenance`, `enum`, `register`, `hash`, `audience`, `audience-role`, `root-only`, `open`, `vocabulary` | `frontmatter.yaml` |

- **Runner.**
  `docsys check` runs, in a fixed order, the checks the configuration turns on, gives each finding the severity its rule has (the methodology's default, or the one `rules:` in `docsys.yaml` sets: `error`, `warning` or `off`), prints what is not off and exits 0, 1 or 2.
  A finding is a path, a line, a rule identifier and a message ending in a `fix:` clause.
- **Report.**
  `docsys report` lists each exclusion with its reason and the number of documents it leaves out, and counts the documents in scope; `--documents` lists the excluded documents.
- **Author tools.**
  `docsys id` mints a ULID, chronological (`--at`), ordinal (`--order`) or as a filename stem (`--slug`), outside any workspace; `docsys seal` writes a frozen record's `hash:` and refuses to replace a seal that no longer matches without `--reseal`; `docsys rename` moves a file or folder and rewrites the links to it, in the documents of the scope; `docsys slugify` names each slugged document after its slug, through `rename`.
  They are listed in [`codifying/docsys-commands.md`](../../../codifying/docsys-commands.md) and explained in the engine's [fiche](https://github.com/Skl8em/docsys/blob/main/docs/author-tools.md); `migrate_ids.py`, which does not run, is kept in the engine's `legacy/`.
  A rewrite of a sealed record's links breaks its seal, so the tools list each record they rewrote with the command that renews it.
- **Vocabulary.**
  The engine ships the frontmatter vocabulary as `src/docsys/schema/frontmatter-rules.yaml` and reads it itself, without the generated JSON; the schema exists twice until the gate switches, and a test of the engine compares them.
  The engine classifies every status word as frozen or open, and its suite fails when the classification and the vocabulary disagree.
- **Types.**
  Every function, tests included, is checked by basedpyright and ruff from the test suite and from the editor at the same versions.
- **Opt-in tools.**
  `docsys.yaml` names external commands under `tools`; `docsys check` runs them after its own checks and reports `tools/failed` or `tools/missing`.
  The engine ships the sentence-per-line markdownlint rule, which this repository's markdownlint loads from the submodule; its test reads markdownlint-cli2's output under the pinned 0.17.2 and under 0.21.0.
- **Fiches.**
  The engine's fiches on the ULID check, [referential integrity](https://github.com/Skl8em/docsys/blob/main/docs/referential-integrity.md), the [paired-change rule](https://github.com/Skl8em/docsys/blob/main/docs/paired-change.md), the [phase ledger and the phase-state check](https://github.com/Skl8em/docsys/blob/main/docs/phase-state.md) and the [vocabulary and its reader](https://github.com/Skl8em/docsys/blob/main/docs/vocabulary.md) and the [author tools](https://github.com/Skl8em/docsys/blob/main/docs/author-tools.md) are in `docsys/docs/`; `codifying/gate.md` and `codifying/schema-pipeline.md` keep what is this repository's.
  This repository links to the engine's fiches by URL.
- **Parity with `scripts/`.**
  Run from a copy of this repository with a `docsys.yaml` in the engine's shape (the scope taken from the frontmatter ignore list; the register, paired-change and phases sections unchanged), `docsys check` reports no finding but the paired-change rule's own on the uncommitted configuration.

## ws3 — The guided install

`docsys init` writes:

- `docsys.yaml` with every document already in the repository excluded, each with the reason "predates docsys; awaiting review", so the adopter includes each back once revised;
- the root README's frontmatter (`axis`, `dominant-community`);
- the first level of the layout (one folder per function the adopter names);
- the pre-commit hook.

`docsys new <force> <path>` writes a document from the force's template with `id` and `slug` minted and the force's defaults filled, so a person chooses the force and the rest follows.
Fields that need the theory to fill — `intention`, `constitutive` for an existing document — are not asked in a questionnaire: `new` proposes the force's default, and classifying documents that already exist is the agent kit's job, checked by the gate.

Delivers: `init` and `new`, with fixtures; the structuring and writing tutorials point at them.

## ws4 — Install on `weft`

One command, gate green on the scaffold; `weft_spec.md` given its frontmatter by hand with `docsys new`'s defaults as a guide.
Every friction met is recorded, not smoothed over in the moment.

Delivers: an adoption record in this folder: what was run, what failed, what was changed because of it.

## ws5 — Close the phase

A README, the ledger, the roadmap and the index.

Delivers: the phase README.
