---
title: "Phase 14 adoption — the plan"
force: propose
verb: argue
intention: suasive
view: synchronic
provenance: { type: project, id: phase-14-adoption }
constitutive: no
concerns: [steering, codifying, structuring, writing]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

The first delivery phase of the rush to MVP ([ADR-042](../phase-13-design/rush-to-mvp.md)): an external project can install the machinery and is guided through populating what the framework needs to run.
The agent-kit phase follows it; the two together end the era on the condition ADR-042 states.
The plan was drafted in Phase 13, the design phase, where its rulings were taken.

## Why this phase exists

Nothing in the repository runs anywhere but here.
Phase 12 drew the engine/config seam from one instance and said so: the seam "cannot be tested without a second consumer" ([engine/config seam](../../refoundation/phase-12-codifying/engine-config-seam.md)).
Checked on 2026-10-08, four things stop a second project from running the gate at all, none of them named by the external review:

- **Every section of `docsys.yaml` is mandatory** (`docsys_config.py`), so an adopter must invent a phase ledger and a decision register to lint a single file.
- **The frontmatter linter covers every tracked `.md` minus an ignore list**, so adoption cannot be incremental in a code repository whose existing Markdown carries no frontmatter.
- **The root document is the literal `README.md`** (`frontmatter_lint.py`), which also contradicts [ADR-008](../../naive-sketch/phase-03-reorganization/ADR-008-tree-axis-declaration.md).
- **Nix is assumed**: without `pyyaml` the gate re-executes itself under `nix develop`, which an adopter without Nix cannot follow.

And the pages an adopter or an agent reads first contradict each other or themselves (T1).

## Rulings

- **A package, not a vendored copy** (project owner, 2026-10-09).
  One engine that adopters pin, rather than a copy forked into each project.
- **The layout default for an adopter's docs** (project owner, 2026-10-09): by **function** first, then by **sub-function**, then by **register** (`know` / `do` / `govern`), then by **force** — each split made only when the level above has grown enough to need it, fractally.
  This extends what the [structuring tutorial](../../../structuring/tutorial.md) already says (function first, register inside it) and contradicts `structuring/setup.md`, which lays docs out by force at the top.
- **`weft` is the first adopter**; its repository was initialised on 2026-10-08.
- **The engine is [`Skl8em/docsys`](https://github.com/Skl8em/docsys)**, public, licensed by kind of artefact ([ADR-043](../phase-13-design/licensing.md)); it is mounted in this repository as a git submodule at `docsys/`, beside `scripts/`, which it replaces (project owner, 2026-10-10).
  The provenance rule shelves documentation; tooling and configuration folders — `scripts/`, `docsys/`, `LICENSES/`, `.githooks/` — are not shelves.
- **The scope** (project owner, 2026-10-10): every document is in scope by default; an exclusion takes documents out and carries the reason, so it can be read and argued; an inclusion brings back documents an exclusion took out.
  Both are lists in `docsys.yaml`, both optional.
  The excluded documents are the ones still owed: see *Strictness*.
- **Where the engine's documentation lives** (project owner, 2026-10-10): how a project uses `docsys` and configures it is documented here, in `codifying/`; how the engine works inside is documented in `docsys/docs/`, each fiche moving there when the check it explains is ported, since until then it explains `scripts/`.
- **The tools for Python** (project owner, 2026-10-10): basedpyright checks types and ruff lints and formats, at the versions the engine's lockfile pins, run by its test suite and by the editor alike; `ty`, Astral's type checker, is to be evaluated later as an option.

## Workstreams

| # | Workstream | Output |
|---|---|---|
| **T1** | **Fix what the kit will teach.** An agent applies a page literally, so these are fixed before the kit is built from them. (i) The root README's "New here?" block, broken since 2026-07-25. (ii) The layout ruling applied: `structuring/setup.md` section A and `structuring/defaults.md`'s in-repo axis rewritten to it, the tutorial's rule extended with sub-function and force, and the CHANGELOG's register made consistent (the tutorial says `govern`, `setup.md` says `account`). (iii) The orient template and step 3 of the writing tutorial stop producing the "suspect pair" (`synchronic` under a project's provenance). (iv) `writing/forces/know/describe/README.md` declares `force: explain, verb: illuminate` — its own stance, mislabelled. (v) The *Validation rules* of `writing/frontmatter.md` say which rule the gate enforces and which it does not. (vi) CI's Nix installer pinned rather than `@main`. **Prose that narrates its own history** ([`imagining/reader-first-writing.md`](../../../imagining/reader-first-writing.md)): (vii) the rule and its revision test added to [`writing/rules.md`](../../../writing/rules.md) — a synchronic document states the present for its declared reader, and the account of a change goes to the commit, the changelog or the reply; (viii) a cold-reader pass — a subagent with no conversation history, given one page and its declared audience — over the pages the kit is built from (the root README, the writing and structuring tutorials, `writing/frontmatter.md`, the force stances and templates); (ix) the pages it flags rewritten, starting with those edited when this phase opened (the root README's status paragraph, `steering/foundation.md` §1, `imagining/README.md`). Each case the project owner finds is added to the casebook and fixed the same way, until the project owner judges the result satisfying. | the six defects fixed; the rule in `writing/rules.md`; a cold-reader record per page passed; the casebook grown; the gate green |
| **T2** | **The engine as a Python package, `docsys`.** An adopter declares it as a development dependency in its `pyproject.toml`, pinned to a git tag and locked by its own lockfile; this repository installs it the same way, editable (`pip install -e` or the `uv` equivalent), so it is its own first consumer. Fixtures first, against a throwaway adopter repository built by the test — the second consumer the seam lacks. (i) **The workspace is explicit**, on `weft`'s model: the CLI finds it as the nearest ancestor holding `docsys.yaml`, the way `make` finds its control file, or takes `--workspace`; the library takes it as a parameter; nothing is changed or read from the current directory at import. (ii) **Strictness is configurable** — see *Strictness* below. (iii) The `register`, `paired_change` and `phases` sections of `docsys.yaml` become optional, and their checks run only when configured. (iv) The root document is configurable, defaulting to `README.md`. (v) `pyyaml` comes with the package, so Nix is optional; markdownlint and its custom rule stay available, opt-in, since they need Node. (vi) A `docsys` CLI: `docsys check` runs the configured gate, `docsys report` lists the documents not yet compliant. The schema ships inside the package. (vii) **The cross-package API is honoured from the start**, since every later package must read the same files ([`imagining/multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md)): `docsys.yaml` carries a format version, every finding carries a rule identifier beside its `fix:` clause, and the fixtures for the methodology's rules are data files (input documents and expected findings) rather than Python test code. | the `docsys` package, in its own repository, with fixtures; this repository consuming it; `codifying/` fiches updated in step |
| | **T2 progress.** In [`Skl8em/docsys`](https://github.com/Skl8em/docsys), mounted here at `docsys/` and declared in this repository's `pyproject.toml` as an editable development dependency: the package skeleton, the workspace (nearest `docsys.yaml`, or `--workspace`; nothing done to the current directory at import), the exit codes (0, 1, 2), the frontmatter reader and ULID minting; the configuration loader, with (vii) the format version, (ii) the scope (every document by default, `exclude` with a reason, `include` back), (iv) the root document defaulting to `README.md`, and (iii) `register`, `paired_change` and `phases` optional, listed key by key in [`codifying/docsys-configuration.md`](../../../codifying/docsys-configuration.md); every function, tests included, checked by basedpyright and ruff from the test suite and from the editor at the same versions; the documents, read from git (tracked or not yet added, never ignored, never in a submodule) and filtered by the scope; findings as path, line, rule identifier, message and `fix:`; the link check, `links/resolve`, stated case by case in `docsys/conformance/links.yaml`, which the package's tests run, and agreeing with `scripts/linkcheck.py` on this repository (158 documents, no finding); the slug check, `slugs/type`, `slugs/form` and `slugs/filename`, in `conformance/slugs.yaml`, agreeing with `scripts/slug_check.py` (17 slugged documents, no finding); the ULID check, `ulids/form`, `ulids/unique`, `ulids/resolve`, `ulids/self`, `ulids/symmetric`, `ulids/cycle` and `ulids/register`, in `conformance/ulids.yaml`, agreeing with `scripts/ulid_check.py` (no finding); the fixity check, `hashes/seal` and, off by default, `hashes/unsealed`, in `conformance/hashes.yaml`, which states the canonical form of a seal, agreeing with `scripts/hash_check.py` (38 seals verified, 18 frozen records unsealed); the phase-ledger check, `ledger/missing`, `yaml`, `shape`, `form`, `number`, `unique`, `current`, `order` and `lagging`, in `conformance/ledger.yaml`, agreeing with `scripts/phase_ledger.py` (15 phases, no finding), whose findings now carry the ledger's line, read by a YAML loader that locates every value; the phase-state check, `phase-state/ledger`, `folder`, `table`, `mention`, `status`, `field` and `lagging`, in `conformance/phase-state.yaml`, agreeing with `scripts/phase_state.py` on this repository and on three deliberate mutations of it; the paired-change check, `paired-change/unpaired`, `advisory`, `anchor` and `branches`, in `conformance/paired-change.yaml`, whose cases can now carry a git history (commits, branches, a merge, a detached HEAD), agreeing with `scripts/paired_change.py` on this repository and on a deliberate unpaired commit; the frontmatter check, `frontmatter/yaml`, `missing-block`, `required`, `provenance`, `enum`, `register`, `hash`, `audience`, `audience-role`, `root-only`, `open` and `vocabulary`, in `conformance/frontmatter.yaml`, judging documents by the vocabulary the package now ships as `src/docsys/schema/frontmatter-rules.yaml` and reads itself, without the generated JSON, agreeing with `scripts/frontmatter_lint.py` on this repository and on five mutations of it (the schema exists twice until the gate switches, and a test of the engine compares them); the runner: `docsys check` runs, in a fixed order, the checks the configuration turns on, gives each finding the severity its rule has (the methodology's default, or the one `rules:` in `docsys.yaml` sets: `error`, `warning` or `off`), prints what is not off and exits 0, 1 or 2; `docsys report` lists the documents the scope leaves out, each with its reason, and counts them; a reference may name a record the scope excludes, which the ULID check found when `docsys check` ran on this corpus under a single scope; 426 tests. **All the checks of `scripts/` that belong to the engine are extracted, and the engine runs them.** Run from a copy of this repository with a `docsys.yaml` in the engine's shape (the scope taken from the frontmatter ignore list; the register, paired-change and phases sections unchanged), `docsys check` reports no finding but the paired-change rule's own on the uncommitted configuration. What is left of T2 is this repository's switch. **Next:** the gate switched to `docsys check`, which leaves open where the checks that are not the engine's go (the worktree check, markdownlint and its sentence-per-line rule, the editor's markdownlint, the runner and problem-matcher fixtures); CI checking out the submodule; `scripts/` retired. Each fiche of `codifying/` that explains an extracted check moves to `docsys/docs/` with it (the link check had none). | |
| **T3** | **The guided install.** `docsys init` writes `docsys.yaml` with every document already in the repository excluded, each with the reason "predates docsys; awaiting review", so the adopter includes each back once revised, the root README's frontmatter (`axis`, `dominant-community`), the first level of the layout (one folder per function the adopter names), and the pre-commit hook. `docsys new <force> <path>` writes a document from the force's template with `id` and `slug` minted and the force's defaults filled, so a person chooses the force and the rest follows. Fields that need the theory to fill — `intention`, `constitutive` for an existing document — are not asked in a questionnaire: `new` proposes the force's default, and classifying documents that already exist is the agent kit's job, checked by the gate. | `init` and `new`, with fixtures; the structuring and writing tutorials point at them |
| **T4** | **Install on `weft`.** One command, gate green on the scaffold; `weft_spec.md` given its frontmatter by hand with `docsys new`'s defaults as a guide. Every friction met is recorded, not smoothed over in the moment. | an adoption record in this folder: what was run, what failed, what was changed because of it |
| **T5** | **Close the phase**: a README, the ledger, the roadmap and the index. | phase README |

T1 comes first because the package will ship these pages' templates.
T2 before T3: `init` writes a configuration the package must accept.
T4 is the definition of done; it may start as soon as T2 runs, and feed T3.

## Strictness

An adopter's existing documentation does not become compliant at once, and the gate must not demand it; it must also not let a document slip back out once it is in.

- **Every document is in scope by default**, so a new project needs no configuration for the gate to check everything.
- **An exclusion takes documents out, with its reason**: `scope.exclude` in `docsys.yaml` maps a pattern to why the documents it matches are not checked.
  The reason is required, so each exclusion can be read and argued in review.
  `docsys init` excludes every document already in the repository, with the reason "predates docsys; awaiting review".
- **An inclusion brings a document back**: a pattern in `scope.include` wins over an exclusion.
  A legacy document is adopted by including it once revised, an edit visible in review; a new document is in scope from the start.
- **The gap is accounted for**: `docsys report` lists the excluded documents with their reasons, and prints their count, so the reduction is visible over time.
- **Each rule has a severity** — error, warning or off — configurable per rule in `docsys.yaml`, with the methodology's defaults.
  A rule the methodology states as a heuristic (the sentence-per-line rule, the "suspect pair") defaults to a warning.

## Open points, and when each is settled

The blocking rule of the [Phase 12 plan](../../refoundation/phase-12-codifying/plan.md) carries over unchanged: a point that blocks a planned task stops it, and the tree goes back to the last state that stands without the point.

| # | Open point | Settled by | Blocking? |
| --- | --- | --- | --- |
| 1 | **Where the package lives.** *Ruled by the project owner, 2026-10-09:* its own repository, included here as a git submodule and installed editable. An agent session on the engine does not load the theory corpus; this repository consumes the engine exactly as an adopter does; how the engine works inside is documented with it, in `docsys/docs/`, so the paired-change rule still pairs code and explanation inside one repository, while how a project uses and configures it stays in `codifying/` here. Costs accepted with it: three links from sealed phase records into `scripts/` stop resolving and need an allowance in the link check; the schema, authored with the engine, is explained by `writing/frontmatter.md` across the repository boundary. | The project owner | Settled |
| 2 | **Non-Python adopters.** The Python package covers `weft`; a project in another ecosystem installs it as a tool (`uv tool install`) or through the flake, unpinned by its own lockfile. The long-term answer is in [`imagining/multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md). | Out of the era | No |
| 3 | **What an adopter gets by default.** *Ruled by the project owner, 2026-10-09:* frontmatter, links, identifiers, slugs and fixity on; the decision register when `init` is told where it is; the paired-change rule off until the adopter names its mechanism and understanding paths (the agent kit will propose turning it on for the theory of the code, see [`imagining/theory-of-the-code.md`](../../../imagining/theory-of-the-code.md)); the phase checks off. | The project owner | Settled |
| 4 | **The adopter's frontmatter when the vocabulary changes.** Pinned to the package's version for now; no migration tool. | Out of the era unless `weft` forces it | No |
| 5 | **`weft`'s functions and its provenance map.** Its owner names them; `init` does not guess. | T4, by the project owner | Blocks T4 |
| 6 | **Working across two repositories.** This repository consumes the engine through a submodule, as any adopter would through its lockfile. To settle as T2 meets them: CI checks out the submodule; a document here that cites the engine's code cites it at the submodule's pinned commit (the `pin:` field, until now unused); each `codifying/` fiche that explains the engine's inside moves to `docsys/docs/` with the check it explains, so the paired-change rule still pairs them inside one repository, and `docsys` is checked by `docsys` like any adopter. | T2 | No |

## Verification / definition of done

- `docsys check` is green in this repository, run through the installed package.
- On `weft`, the package is a development dependency in `pyproject.toml`; `docsys init` and `docsys check` are green on the scaffold, with `weft_spec.md` either in scope or excluded with its reason, and `docsys report` lists the exclusions.
- Each T2 and T3 behaviour has a fixture that was red first.
- The six T1 defects are fixed, and the root README routes a newcomer to a page that exists.

## Explicitly out of scope

- **The agent kit** — the phase after this one.
- **The life cycle of a document**, the records-continuum reframing the review proposes for it, and the closure rule: parked ([roadmap](../../../steering/roadmap.md)).
- **Generated reading surfaces**, an MCP server, integrations with issue trackers.
- **New gate checks on this repository's own state** ([ADR-042](../phase-13-design/rush-to-mvp.md), point 5).
- **Evaluating `ty`** as the engine's type checker: later, at the project owner's call.
