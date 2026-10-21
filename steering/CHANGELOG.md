---
title: "Changelog of the system"
force: account
verb: report-against
intention: state
view: diachronic
provenance: { type: function, id: steering }
constitutive: yes
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
---

History of the documentation system itself.
Append-only; each entry is dated-fixed.
Design rationale for each line lives in the matching ADR — listed in the register [`ADR.md`](ADR.md), written in full in its [`phases/`](../phases/README.md) folder.

## [v4.0-alpha.45] — The engine writes what its checks verify

- **Added:** four `docsys` commands for the author: `docsys id` mints a ULID, `docsys seal` writes a frozen record's `hash:`, `docsys rename` moves a file or folder and rewrites every relative link to it, and `docsys slugify` names each document after its slug; the reference is [`codifying/docsys-commands.md`](../codifying/docsys-commands.md).
  `seal` replaces a seal that no longer matches only with `--reseal`; `rename` and `slugify` list each sealed record whose links they rewrote, since the rewrite breaks its seal.
- **Changed:** `rename` also rewrites a link to a folder inside a moved folder, which `scripts/rename_doc.py` left pointing at the old place, and `slugify` leaves alone a `<slug>-<id>` name that the slug check accepts, which `scripts/slugify_names.py` renamed.
- **Moved:** `migrate_ids.py` to the engine's `legacy/`, unchanged, with a README saying that it does not run and why it is kept; the scripts it replaces stay in `scripts/` until the gate switches.

## [v4.0-alpha.44] — Every Markdown file is a document

- **Changed:** a document is any Markdown file under the workspace but inside `.git`; git's index and `.gitignore` are no longer consulted, so a build folder or a virtual environment is left out by a `scope.exclude` entry with its reason, and a workspace outside a git repository is accepted.
  `docsys report` prints one line per exclusion with its reason and the number of documents it leaves out, and `--documents` lists the documents; the reference is [`codifying/docsys-configuration.md`](../codifying/docsys-configuration.md).
- **Parked:** excluding submodules from the documents by default, with an explicit opt-in, after the MVP; until then a submodule's files are documents, so that the engine falls under this repository's rules.

## [v4.0-alpha.43] — A branch is rebased on its destination before it is merged

- **Added:** a rule in [`CONTRIBUTING.md`](CONTRIBUTING.md): a branch is kept rebased on the branch it will be merged into — at the start of each session, whenever the destination moves, and last before it is presented — and checked on its tip, since no hook runs during a rebase; the `--no-ff` merge is then a fast-forward recorded as a merge commit, which groups the steps without squashing them.
  A track is rebased with `--rebase-merges`, so its tasks' merges stay; only branches never pushed are rebased.
- **Changed:** the rule on the engine's mirror: a rebase is made in the engine first, and every pointer commit here is moved to the engine's rebased commit.
  The skill `branch-and-commit` gives the procedure, and a command that finds a pointer left at a replaced commit.

## [v4.0-alpha.42] — Short names for the levels of a plan

- **Changed:** branches and commit subjects name the levels of a plan `ph`, `ws`, `tr`, `ts` and `sp`, with no `feature/` prefix ([`CONTRIBUTING.md`](CONTRIBUTING.md)): the phase branch is `ph14-adoption` in both repositories, the track that set up continuous integration `ph14-ws2-tr1-ci`, its tasks `ph14-ws2-tr1-ts1-ci-engine-shell`, `-ts2-ci-engine-workflow` and `-ts3-ci-documentality`; a subject starts with its branch's name less `ph<NN>-`, or with `ph<NN>:` on the phase branch.
  Older branches keep the names they were merged under.
  The skill `branch-and-commit` follows it.
- **Changed:** Phase 14's workstreams are labelled ws1 to ws5 in the [plan](../phases/rush-to-mvp/phase-14-adoption/plan.md), and the closing plan of ws2 is [`ws2-closing.md`](../phases/rush-to-mvp/phase-14-adoption/ws2-closing.md); the entries below keep the labels they were written with.

## [v4.0-alpha.41] — A plan divides into workstreams, tracks, tasks and steps

- **Ruled:** a phase's plan divides into workstreams, which may run side by side and have no branch; tracks, each a branch merged into the phase branch; tasks, each sized for one agent session, each a branch merged into its track's; and steps, each one commit; work at every level is numbered when it starts, never before, as ADR-038 says of phases; Phase 14 applies it as far as its plan allows, and every plan after Phase 14 is divided by it ([plan](../phases/rush-to-mvp/phase-14-adoption/plan.md), *Rulings*).
- **Changed:** the rule in [`CONTRIBUTING.md`](CONTRIBUTING.md) on branches follows it: a branch per track and per task, none per workstream; Phase 14's names are `feature/ph<NN>-t<N>-ws<N>-<track>` and `…-tsk<N>-<task>`, `t<N>` numbering the workstream, `ws<N>` the track and `tsk<N>` the task, each given when the work starts; presentation, standing acceptance and the engine's mirror are by task and track.
  The skill `branch-and-commit` follows it, and [Closing T2](../phases/rush-to-mvp/phase-14-adoption/ws2-closing.md) is divided into tracks and tasks, numbering only the started ones.
- **Parked:** dividing a plan into any number of levels, until after the MVP ([roadmap](roadmap.md), *Parked*).

## [v4.0-alpha.40] — What the switch to `docsys` retires

- **Ruled:** before this repository's gate becomes `docsys check`, the accounts of the extracted checks move to the engine, the engine's link check allows a frozen record's link to a retired file with a reason, and the author tools of `scripts/` are ported to the engine, but for `migrate_ids.py`, which goes to its `legacy/` folder; `schema/` retires with `scripts/`, by an ADR to come that supersedes ADR-037 ([plan](../phases/rush-to-mvp/phase-14-adoption/plan.md), *Rulings*).
- **Ruled:** every Markdown file under the workspace is a document, whatever git knows of it; an exclusion, a virtual environment's included, is written in `scope.exclude` with its reason, and the worktree check retires instead of being ported.
- **Planned:** [closing T2](../phases/rush-to-mvp/phase-14-adoption/ws2-closing.md), step by step: continuous integration of both repositories first, pushed and verified, then every Markdown file a document, the link check's allowance, the author tools in the engine, and the switch; T1's remaining defects follow T2.
- **Parked:** what a freeze may cover (only what the record owns, not what it links to), under the life cycle; a utility for renaming documents and migrating identifiers; moving markdownlint past 0.17.2; and, first once the MVP closes, `docsys explain <rule>`, which explains a rule from the installed package ([roadmap](roadmap.md), *Parked*).

## [v4.0-alpha.39] — The engine mirrors the phase's branches

- **Changed:** the rule in [`CONTRIBUTING.md`](CONTRIBUTING.md) on the engine's repository: work that changes both repositories runs on the same phase, workstream and item branches in each, merged with `--no-ff` at the same level and at the same time, each merge here followed by a pointer at its counterpart there; work on the engine alone needs no mirror.
- **Added:** a rule in [`CONTRIBUTING.md`](CONTRIBUTING.md): `main` is left alone until a phase closes, and then receives the phase branch as one `--no-ff` merge, in each repository the phase changed.
  The skill `branch-and-commit` follows both.

## [v4.0-alpha.38] — Work in nested branches, committed in steps

- **Added:** a rule in [`CONTRIBUTING.md`](CONTRIBUTING.md): a branch per workstream and per item, merged with `--no-ff` once the project owner has accepted the item; an item committed in optional steps (specify, red, implement, document, integrate, review global docs); the same branch names in the engine's repository.
- **Added:** the project skill `branch-and-commit` (`.claude/skills/`), the agent's procedure for that rule; `.claude/` is outside the documents the gate checks ([the gate](../codifying/gate.md)).

## [v4.0-alpha.37] — The editor shows what the gate shows

- **Added:** the VS Code task `docs: run the gate` reads the gate's output through two problem matchers, so each failure lands in the Problems pane on the file, and line, it names; `problem-matcher` (`scripts/test_problem_matcher.py`) pins which lines they read and which they leave alone ([the gate](../codifying/gate.md), *The output contract*).
- **Added:** `editor-markdownlint` (`scripts/editor_markdownlint.py`, with its fixtures) fails when the editor's markdownlint extension bundles another `markdownlint-cli2` than the one `flake.lock` pins; the extension is held at 0.59.0, the release that bundles 0.17.2 ([`environment.md`](environment.md), *Lint Markdown in the editor*).

## [v4.0-alpha.36] — Everything through the devShell

- **Changed:** the devShell provides `uv` (0.7.22, from the nixpkgs `flake.lock` already pins) and makes it build every `.venv` on the flake's Python, downloading none; both `.venv`s are rebuilt on it, and this repository's `uv.lock` is relocked by that `uv`.
- **Changed:** the gate runs only inside the devShell: started outside it, `scripts/check.py` re-enters it even when the calling interpreter can import `pyyaml`, and without `nix` it stops before any check ([the gate](../codifying/gate.md)); a fixture in `scripts/test_check.py` shows the refusal.
- **Fixed:** the editor's root folder names its interpreter, this repository's `.venv`, instead of falling back to a global Python ([`environment.md`](environment.md)).

## [v4.0-alpha.35] — Scope by exclusion, and one set of Python tools for the editor and the tests

- **Ruled:** every document is in scope by default; an exclusion takes documents out with its reason, and an inclusion brings them back; the exclusions are the documents still owed, and `docsys init` will write them ([plan](../phases/rush-to-mvp/phase-14-adoption/plan.md), *Rulings* and *Strictness*).
  How a project uses and configures `docsys` is documented in `codifying/`; how the engine works inside, in `docsys/docs/`, as each check is ported.
  basedpyright and ruff are the Python tools; `ty` is to be evaluated later.
- **Changed:** `docsys` reads the scope that way, and checks its Python with basedpyright (strict, `Any` refused) and ruff, from its tests and from the editor at the same locked versions.
- **Moved:** the `docsys.yaml` reference, from the engine to [`codifying/docsys-configuration.md`](../codifying/docsys-configuration.md).
- **Added:** [`documentation-system.code-workspace`](../documentation-system.code-workspace), which opens the engine as a folder of its own so the editor applies its configuration, and the section of [`environment.md`](environment.md) on working on the engine.

## [v4.0-alpha.34] — The engine is strictly typed

- **Changed:** every function of `docsys`, its tests included, carries a full signature, checked by `mypy --strict` from the engine's own test suite, so an unannotated function fails it; the configuration is returned as one typed structure per section, and the package ships `py.typed`.
  Narrowing the configuration by type adds four refusals: a register, table or status path that is not a string, and a key that is not a name.
- **Progress:** Phase 14's [plan](../phases/rush-to-mvp/phase-14-adoption/plan.md) records T2's state.

## [v4.0-alpha.33] — The engine reads its configuration

- **Added:** `docsys` reads `docsys.yaml` in format version 1, listed key by key in the engine's [`docsys.yaml` reference](https://github.com/Skl8em/docsys/blob/main/codifying/configuration.md): a required `version`, a required `scope` of `include` and `exclude` patterns, a `root_document` that defaults to `README.md`, and `register`, `paired_change` and `phases` as optional sections whose checks run only when they are present.
  `docsys check` refuses a malformed file with exit 2, naming the key and the fix.
- **Not yet:** this repository's `docsys.yaml` is still in the shape `scripts/` reads, so `uv run docsys check` refuses it; it moves to format version 1 when the gate switches to `docsys check`.
  Written in format version 1, its scope selects the same 127 of 157 tracked Markdown files as the current ignore lists.
- **Fixed:** the headings of v4.0-alpha.30 and v4.0-alpha.31, which lost their version when the next entry was inserted above them.
- **Progress:** Phase 14's [plan](../phases/rush-to-mvp/phase-14-adoption/plan.md) records T2's state and its next steps.

## [v4.0-alpha.32] — The engine is mounted, and consumed like any adopter's

- **Added:** [`Skl8em/docsys`](https://github.com/Skl8em/docsys) as a submodule at `docsys/`, and a `pyproject.toml` that declares it as an editable development dependency (`uv sync`; `uv run docsys check`).
  The engine has its skeleton, its workspace discovery, its exit codes, the frontmatter reader and ULID minting, with 41 tests; it ports no check yet, so the gate is still `scripts/check.py`.
- **Changed:** markdownlint leaves `docsys/` to the engine's own gate; `REUSE.toml` files the new build files with the code; `.venv/` is ignored.
- **Progress:** Phase 14's [plan](../phases/rush-to-mvp/phase-14-adoption/plan.md) records T2's state and its next steps.

## [v4.0-alpha.31] — Phase 13 closes; Phase 14, adoption, opens

- **Closed:** Phase 13, design, with its [README](../phases/rush-to-mvp/phase-13-design/README.md).
  The agent-kit plan it was to write moves to the agent-kit phase, which plans itself when it starts.
- **Opened:** Phase 14, adoption; its [plan](../phases/rush-to-mvp/phase-14-adoption/plan.md) moves from the design folder into the phase's own, by `scripts/rename_doc.py`, which rewrote nine links.
  One of them is in the sealed Phase 12 README, which is resealed for that link path alone.
- **Created:** the engine's repository, [`Skl8em/docsys`](https://github.com/Skl8em/docsys), public, with its README and the licensing of ADR-043; it is mounted here as a submodule at `docsys/` when its first code lands.
- **Ruled:** the provenance rule shelves documentation only; tooling and configuration folders carry no function (`steering/CONTRIBUTING.md`).
  The plan gains an open point on working across two repositories.

## [v4.0-alpha.30] — Licensing by kind of artefact

- **Decided:** [ADR-043](../phases/rush-to-mvp/phase-13-design/licensing.md) — GPL-3.0-or-later for the engine's code, AGPL-3.0-or-later for a component that runs as a service, CC0-1.0 for what an adopter copies into its own repository, CC BY-SA 4.0 for the prose.
- **Added:** [`REUSE.toml`](../REUSE.toml) maps every tracked file to one licence, and `LICENSES/` holds the three texts; `reuse lint` (reuse 6.2.0) reports the repository compliant with the REUSE specification 3.3, 200 of 200 files covered.
  It is run by hand, not by the gate.
- **Changed:** `steering/CONTRIBUTING.md` binds contributions to the licence `REUSE.toml` assigns; the root README states the scheme.
- **Settled:** the design plan's licensing point, which blocked creating the `docsys` repository.

## [v4.0-alpha.29] — Phase 13 design: rulings, and the present described without Phase I and II

- **Changed:** living documents describe the project by its current era, the rush to MVP, without the Phase I / Phase II framing: the roadmap, `steering/foundation.md` §1 and §7, the phases index, the ledger's comment, the design plan, the schema-pipeline fiche, the debt register and the structuring tutorial's example.
  Frozen records, the changelog and the external review keep the words of their time.
  The roadmap and the phases index state how eras are named: the current one to coordinate the work, a closed one's boundaries drawn once it is history.
- **Ruled:** the theory of the code is two documents, a constitutive lexicon and an `explain` of the grain and limits, recommended and never required ([proposal](../imagining/theory-of-the-code.md#rulings)); the engine's repository is `docsys`, public, on GitHub ([design plan](../phases/rush-to-mvp/phase-13-design/plan.md)).
- **Open:** licensing, which blocks creating that repository.
- **Observed:** Phase 12's merge into `main` passes the paired-change rule at commit level, 22 changes since the anchor, none needing an account; examining each commit cost nothing at merge time on that branch (Phase 12, open point 2).

## [v4.0-alpha.28] — The root README routes a newcomer again

- **Fixed:** the "New here?" block of the root README, broken since 2026-07-25, routes to four pages that exist: the one idea and `structuring/concepts.md` to judge the approach, the writing tutorial, the structuring tutorial, and `writing/choosing.md`.
  Its `theorising/` line names the shelf's contents as they are.

## [v4.0-alpha.27] — Two debts recorded

- **Recorded:** [`technical-debt.md`](technical-debt.md) gains *Synchronic documents that narrate their own history* — pages declared `synchronic` that describe the changes producing them, and teach that style to every agent that reads them — and *Decision records that are plans* — ADR-020, and ADR-042 for its points 1 to 4.
  Neither is fixed now; each entry says how it will be.

## [v4.0-alpha.26] — Phase 12 closes, and Phase I with it; the rush to MVP opens

- **Decided:** [ADR-042](../phases/rush-to-mvp/phase-13-design/rush-to-mvp.md), superseding [ADR-020](../phases/refoundation/phase-06-refoundation/ADR-020-scope-phase-i.md).
  Phase I closes by the project owner's ruling, not by a completeness test.
  The next era, the **rush to MVP**, has two deliverables — adoption by an external project, and the agent kit — and ends on an observable condition on `weft`.
  No new gate check about the project's own state is added meanwhile.
  ADR-020 gains its `superseded-by` link and is resealed; its register row reads "superseded by 042".
- **Closed:** Phase 12, with its [README](../phases/refoundation/phase-12-codifying/README.md).
  The phase-close re-read of the `codifying/` fiches and of `foundation.md` was the project owner's (open point 4); the merge is still to be observed (open point 2).
  **Convention, as T5 was to state:** a phase's closing entry supplements its per-task entries and does not supersede them.
- **Opened:** Phase 13, *design*, in a new era folder, `phases/rush-to-mvp/` ([plan](../phases/rush-to-mvp/phase-13-design/plan.md)): it plans the era's two delivery phases, adoption ([plan](../phases/rush-to-mvp/phase-14-adoption/plan.md)) and the agent kit, both unnumbered.
- **Parked:** the life-cycle phase, with the external review's proposal to reframe it around the records continuum attached; the deployment phase, absorbed by the era; the design of Phase II, superseded ([roadmap](roadmap.md)).
- **Ruled, for the adoption phase:** the engine is a Python package in its own repository, included here as a submodule; adopters declare it as a development dependency; an adopter's docs are laid out by function, then sub-function, then register, then force, each split made only when needed; legacy documents enter through a baseline that only shrinks; the defaults an adopter gets.
- **Revised:** `steering/foundation.md` §1 says how Phase I closed and what replaced the design of Phase II, and its `phase:` is raised; the ledger's `lagging:` list is empty; the root README's status paragraph describes the era.
- **Noted:** the [external review](external-review/external-review.md)'s claim that `linkcheck.py` cannot link `theorising/the_life_of_projects.md` does not reproduce.

## [v4.0-alpha.25] — Three proposals for what comes after Phase I

- **Added**, in [`imagining/`](../imagining/README.md):
  - [`theory-of-the-code.md`](../imagining/theory-of-the-code.md) — a position on Naur, answering the external review's finding 1a: what a project's documentation must carry about its code (concepts, relations, states, invariants, the grain, the limits), and how code and theory are held together;
  - [`reader-first-writing.md`](../imagining/reader-first-writing.md) — the defect of synchronic documents that narrate their own history, why an agent writer falls into it, seven tools against it, and a casebook of the cases found;
  - [`multi-ecosystem-distribution.md`](../imagining/multi-ecosystem-distribution.md) — one package per language ecosystem, all bound to one API: the configuration, the methodology, the baseline, the CLI, the findings, and a conformance suite.
- **Rewritten:** `imagining/README.md` lists the proposals the shelf holds — its own casebook entry, rewritten as state.

## [v4.0-alpha.24] — Phase 12 T6: where the project is, declared once and checked

- **Decided:** [ADR-041](../phases/refoundation/phase-12-codifying/phase-ledger.md).
  The current phase is declared once, in a ledger of its own, [`steering/phases.yaml`](phases.yaml) — the project owner ruled it out of `docsys.yaml`, which only points at it, because it is the project's state and not the tooling's configuration.
  A phase transition is an edit to the ledger, and the gate checks every other place against it.
  It executes [ADR-038](../phases/refoundation/phase-11-tooling-hardening/unstarted-work-unnumbered.md), whose "no check enforces this" limit is closed; that record stays as written.
- **Added:** `phase-ledger` (`scripts/phase_ledger.py`) checks the ledger's own rules, and `phase-state` (`scripts/phase_state.py`) checks the folders, the roadmap and index rows, forward-numbered mentions, the root README's status line and the `phase:` fields against it; `lagging:` lets a document's `phase:` wait, with a reason, and fails once it no longer waits.
  `docsys.yaml` gains a `phases:` section, validated by `docsys_config.py` and covered by the seam test.
  The fixtures — 29 for the ledger, 32 for the state — ran red first; the real ledger and roadmap were also broken by hand.
- **Fixed, flagged by the first run:** the root README's status paragraph, which said Phase 10; the phases index, which had no markers on the naive-sketch rows and no row for Phase 12.
  `foundation.md` lags at Phase 07 by the ledger's leave, until T5 re-reads it.
- **Settled:** open point 3 — `docsys.yaml` joins the paired-change mechanism list with no carve-out; open point 5 — `paired_change.py` fails when no `enforce_on` branch exists locally or on a remote, with fixtures; open point 11 — moving `since` keeps its account, judged at its first real use.
- **Planned:** a **life-cycle phase**, unnumbered, before deployment ([roadmap](roadmap.md)).
  T6's closure rule — a closed phase's README and records frozen and sealed — conflicted with ADR-031 and rests on a `status` vocabulary nobody has ruled, so it moves there with open point 12; the project owner named the cost of placing it ahead of deployment.
  `operationalizing/view.md` said the linter checks `synchronic ⇒ function`; it does not, and every phase plan breaks it — corrected, and handed to the same phase.
- **Recorded, not fixed:** `migrate_ids.py` names the phase root as a bare literal the seam's leak check cannot see ([`technical-debt.md`](technical-debt.md)).
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.23] — Phase 12 T4: the debts T1 recorded are paid, or kept on purpose

- **Fixed:** `ulid_check.py` rejects a record that names itself in `supersedes` or `superseded-by`, and a cycle along `superseded-by`; and it fails when the register's configured row shape matches no row, where it used to pass for want of anything to compare.
  Each has fixtures that were red first.
- **Added:** `slug_check.py`, `linkcheck.py` and `hash_check.py` build their messages in pure functions, with `test_slug_check.py`, `test_linkcheck.py` and `test_hash_check.py` registered in the gate ahead of each check; each fails a message that lacks its `fix:` clause, which was tried by removing the clause from each.
  `ulid_check.py`'s own `main()` had the same inline shape, so its messages were extracted too.
- **Decided, not recorded as an ADR:** the frozen-record definition **stays in `hash_seal.py`**, guarded.
  `FROZEN_STATUSES` and a new `OPEN_STATUSES` classify every word of the schema's `warn_enums.status`, and a fixture fails the gate when they stop matching it.
  Moving the definition into the schema would rule on the status vocabulary, which the schema's `still_open` list leaves open; it moves when that is ruled.
  It installs a guard, not a norm about the methodology, so it does not clear ADR-032's test.
- **Recorded, not fixed:** the drift message of `generate_schema.py --check` and the runner's own messages are still unfixtured ([`technical-debt.md`](technical-debt.md)).
  The `codifying/` fiches for the gate, referential integrity and the schema pipeline, the audit and the seam record state the new behaviour, and the debt register moves three entries to Paid and narrows a fourth.
  One commit per fix, code and fiche together, so the paired-change rule found nothing to flag.
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.22] — Phase 12 T3, refined: the rule fails where work lands

- **Decided:** [ADR-040](../phases/refoundation/phase-12-codifying/paired-change-where-it-fails.md), refining ADR-039 (which stands) on the project owner's ruling.
  The paired-change rule **fails** only on `main`, `develop` and a detached checkout (a pull request's merge commit in CI), and **warns** on any other branch; a test-only or comment-only change needs no account.
  The unit is still the commit.
  This moves the cost ADR-039 charged at commit time to merge time, on purpose, and says so.
- **Changed:** `docsys.yaml`'s `paired_change:` gains `exempt` and `enforce_on`, validated by `docsys_config.py` and covered by the seam test.
  `paired_change.py` decides comment-only by comparing a Python file's syntax tree before and after, docstrings set aside; fixtures cover it, the branch decision, and one violation on a feature branch, on `main` and on a detached HEAD.
  `CONTRIBUTING.md`, `ARCHITECTURE.md` and `codifying/gate.md` state the refinement.
- **Planned:** the open points T3 left are scheduled against tasks in the [plan](../phases/refoundation/phase-12-codifying/plan.md#open-points-and-when-each-is-settled), with a **blocking rule**: a point that blocks a task stops it, the tree goes back to the last state that stands without the point, and the point is reported rather than worked around.
  Two of them land in T6 (the `docsys.yaml` gap and a stale `enforce_on`), one in T5 (Phase 12's own merge is the first test of commit-level at merge time), one is the project owner's before T4 (the opt-in hook).
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.21] — Phase 12 T3: a change to the tooling that explains nothing fails the gate

- **Decided:** [ADR-039](../phases/refoundation/phase-12-codifying/paired-change-rule.md).
  The unit of the rule is a **commit**, plus the uncommitted work that will become the next, not the branch.
  The plan said "a diff" and left the unit open; it was settled against the history.
  A branch-level rule passes Phase 11 — the phase touched `steering/ARCHITECTURE.md`, `writing/frontmatter.md` and `structuring/tutorial.md` incidentally, and on a phase-long branch any such edit pairs every script edit — while a commit-level rule fires on four of the five Phase 11 commits that touched the tooling.
- **Added:** the `paired-change` gate check (`scripts/paired_change.py`) and its fixtures, which run it against throwaway git repositories: a scripts-only commit fails and passes once a docs file joins it; uncommitted work; deletes and moves out of `scripts/`; merge commits; an unresolvable or shallow-clone anchor is refused, not passed.
  It is registered in `docsys.yaml` like any validator; `check.py` was not extended, as the plan first said, because it is only the runner.
  Its `paired_change:` section — the anchor, the mechanism and the explaining paths — is validated by `docsys_config.py` and covered by the seam test, which now also catches a path prefix hard-coded in the engine.
- **Added:** [`CONTRIBUTING.md`](CONTRIBUTING.md) states the pairing rule, that the gate is run before committing, and where a check is registered and what it must bring.
  `ARCHITECTURE.md` names the decision; `codifying/gate.md` explains the check; CI fetches full history so the anchor exists.
- **Recorded, not fixed:** the rule verifies that an account was edited, not that it is right; the pre-commit hook is opt-in, so a violation may first surface in CI; a change confined to `docsys.yaml` or `tools/markdownlint/` is invisible to it ([`technical-debt.md`](technical-debt.md)).
  The rule starts after the commit before this one, so earlier history is not re-judged.
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.20] — Phase 12 plan: a phase ledger, T6

- **Planned:** **T6**, a phase ledger — the current phase declared once in `docsys.yaml`, with a `phase-state` gate check that verifies the folders, the roadmap and index markers, the root README's status, forward phase numbers and the `phase:` fields against it.
  The problem it answers: the current phase was implied in a dozen places with nothing tying them together, which is what left Phases 10 and 11 closing with stale ones.
  It **supersedes** the forward-numbering check alpha.19 planned for T3, which inferred the phase from folders instead of reading it; T3 is back to the paired-change rule alone.
  ADR-038 is still enforced by the result, so its "no check enforces this" limit closes when T6 lands, and it stays unedited.
  T5 shrinks to flipping the ledger and fixing what the gate flags; the ledger's own decision earns an ADR when T6 makes it.
  A sequencing decision, so held here and in the roadmap (ADR-032).
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.19] — Phase 12 plan: ADR-038 gets a check

- **Planned:** T3 gains a second gate check that enforces [ADR-038](../phases/refoundation/phase-11-tooling-hardening/unstarted-work-unnumbered.md): a tracked document may not name an arabic-numbered phase above the highest one under `phases/`, and a roadmap row may not carry a number for a phase with no folder.
  ADR-038 recorded that no check enforced it and that the rule held by attention; this is what closes that limit, so it is a changelog line, not a record.
  The definition of done and the roadmap row grow to match.
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.18] — Phase 12 T2: Phase 11's account closed

- **Decided:** the three decisions Phase 11 took and never recorded, now on the register with the phase's provenance — [ADR-036](../phases/refoundation/phase-11-tooling-hardening/closed-frontmatter-vocabulary.md) (the vocabulary is closed and a field earns its place by carrying a reason), [ADR-037](../phases/refoundation/phase-11-tooling-hardening/yaml-source-generated-json.md) (the schema's source is YAML, its JSON generated) and [ADR-038](../phases/refoundation/phase-11-tooling-hardening/unstarted-work-unnumbered.md) (unstarted work is never referred to by number).
  Each was checked against ADR-032 and clears it; ADR-038 is the thinnest, since nothing but attention enforces it.
  The dates are the day they were recorded; the decisions were taken on 2026-09-15, 2026-09-17 and 2026-09-13.
- **Ruled:** the generated schema JSON **stays**, in ADR-037.
  Its only reader is `frontmatter_lint.py`, which already needs `pyyaml`, so it is a capability in reserve; it is kept because Phase II's generators are the reader it is for and are not yet designed, and it lapses if that design closes with no non-Python reader.
  The strict-loader rule was checked against ADR-032 as a possible fourth record and held inside ADR-037.
- **Added:** [the Phase 11 README](../phases/refoundation/phase-11-tooling-hardening/README.md), the closing record the phase never had, written afterwards and saying so; it lists what the plan got wrong and left open.
- **Changed:** `writing/frontmatter.md` states that the vocabulary is closed, that an optional field needs a reason and that `schema/frontmatter-rules.yaml` is the source of truth.
  Its field table is reconciled to the schema: `id`, `slug` and `concerns` were declared and never listed, the pre-refoundation `written-at` and `valid-for` are named as not in the vocabulary, and the `distance`, `power` and `status` rows say their value sets are current practice and still open.
- **Changed:** `steering/ARCHITECTURE.md` no longer places schema reconciliation in the future, names Phase 11's four standing decisions and points at `codifying/` for the tooling; `phases/README.md` and the roadmap mark Phase 11 done.
- **Recorded, not fixed:** the closed-vocabulary rule and the reason requirement are enforced and have no fixtures, so weakening either turns no test red ([`technical-debt.md`](technical-debt.md)).
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.17] — Phase 12 plan extended; deployment named

- **Planned:** [Phase 12's plan](../phases/refoundation/phase-12-codifying/plan.md) absorbs the open points T1 handed on, so none lives only in a hand-off message.
  T2 gains the `ARCHITECTURE.md` reconciliation and the question of whether the generated JSON stays; T3 gains the `CONTRIBUTING.md` rule and how to extend the tooling; **T4** pays the four debts T1 recorded; **T5** closes the phase, including the stale root-README status and phases index and a stated changelog convention.
  The definition of done grows to match.
- **Named:** a **deployment phase** after Phase 12, unnumbered per the roadmap's own rule: how the current content is exposed and made usable by third parties, with cold readers for the `codifying/` fiches and the product.
  It takes the adopter community Phase 12's map cut and the extraction triggers the plan named.
  A sequencing decision, so held here and in the roadmap rather than in the ADR register (ADR-032).

## [v4.0-alpha.16] — Phase 12 T1: codifying adopted

- **Decided:** **`codifying` is the seventh function**, the account of the tooling — [ADR-035](../phases/refoundation/phase-12-codifying/codifying-function.md).
  It takes the last link of [ADR-033](../phases/refoundation/phase-10-schema/operationalizing-function.md)'s chain, "IT tools".
  The code stays in `scripts/`, `schema/` and `docsys.yaml`; the account is shelved in `codifying/`.
  The boundary with `operationalizing` is by subject: a coordinate of the corpus is operationalizing, a mechanism that checks, generates or runs is codifying.
  ADR-033's count is refined, not superseded.
- **Added:** the [`codifying/`](../codifying/README.md) shelf — an orient and three fiches for the maintainer: [the gate](../codifying/gate.md), [the schema pipeline](../codifying/schema-pipeline.md) and [referential integrity](https://github.com/Skl8em/docsys/blob/main/docs/referential-integrity.md).
  Each states what it does not establish; none has been read cold by anyone but its author.
- **Ruled:** [the community map](../phases/refoundation/phase-12-codifying/community-map.md) — gate-runner, maintainer and machine, with the adopter named and cut until a second consumer exists.
  `maintainer` is `contributor`, refined, for a distance judged in the tooling field; it stays the linter's warning rather than a schema enum.
  `user ≈ contributor` holds for roles and is qualified for distance, in `foundation.md` §3.
- **Changed:** every repo-specific value in `scripts/` — the linter's out-of-scope prefixes, the schema's paths, the register's path and row shape, the gate's check list — moved to [`docsys.yaml`](../docsys.yaml), read only through `scripts/docsys_config.py`.
  `check.py` is now only the runner, and `scripts/test_seam.py` is a gate check that fails if an instance value is ever hard-coded back ([the seam](../phases/refoundation/phase-12-codifying/engine-config-seam.md)).
- **Fixed:** the runner printed each check's header into a buffer while the check wrote straight to the shared descriptor, so piped output — CI, an agent — put every header after every check's output and failures could not be attributed.
  Found auditing the gate's messages against the machine reader; pinned by `scripts/test_check.py`, which was run red against the unflushed runner first.
  Two smaller findings from the seam work: sibling scripts were addressed by a repo-relative path, and `ulid_check.py` skipped the register cross-check when the register was not a tracked file.
- **Changed:** every validator failure line now ends `— fix: <the edit that clears it>`; the fixtures for `frontmatter_lint.py` and `ulid_check.py` fail a message without one ([the audit](../phases/refoundation/phase-12-codifying/error-message-audit.md)).
- **Changed:** the function set reads seven in `foundation.md`, `CONTRIBUTING.md`, `ARCHITECTURE.md` and the root README.
  `ARCHITECTURE.md`'s provenance map had never gained `operationalizing` either.
- **Recorded, not fixed:** cycles and self-supersession pass `ulid_check.py`; three validators build their messages inline and are unfixtured; the frozen-record definition in `hash_seal.py` duplicates the schema's status list; an empty register match passes.
  All four are in [`technical-debt.md`](technical-debt.md).
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))

## [v4.0-alpha.15] — Phase 12 inserted: codifying

- **Planned:** **Phase 12 — codifying**, inserted before the Phase-II design.
  Phase 11 hardened the tooling and explained none of it: `writing/frontmatter.md` never states the vocabulary is now closed, `ARCHITECTURE.md` never mentions Phase 11 at all, `CONTRIBUTING.md` has no word on `scripts/`, and the phase closed with no README, no consolidated changelog entry, and none of the three ADRs its own plan named as owed at close.
  This is the second time: Phase 10 caught itself mid-close leaving the product describing an old model and fixed it as a named departure ([`phase-10-schema/README.md`](../phases/refoundation/phase-10-schema/README.md)); Phase 11 made a larger change the same way and didn't catch it.
  A sequencing decision, so it is held here and in the roadmap rather than in the ADR register (ADR-032).
  ([plan](../phases/refoundation/phase-12-codifying/plan.md))
- **Named:** **`codifying`**, the seventh function — the "IT tools" link [ADR-033](../phases/refoundation/phase-10-schema/operationalizing-function.md)'s own chain (`theorising → operationalizing → structuring/writing → designing → IT tools`) already named and never gave a shelf.
  Adopting it — the ADR, the orient, the first fiches — is this phase's T1.
- **Changed:** Phase 11's roadmap row marked *(open — closure folded into Phase 12)* rather than *(next)*; its account is paid by this phase's T2.

## [v4.0-alpha.14] — Phase 11 T4: referential integrity

- **Added:** `scripts/ulid_check.py` now validates `supersedes`/`superseded-by` corpus-wide, not just `id`.
  Three checks: every non-null reference resolves to some record's `id` or filename stem (the pre-ULID reference form, e.g. `supersedes: ADR-001-inscribed-act`); supersession is symmetric, matching what `schema/frontmatter-rules.yaml` already documented (`superseded-by` as "the inverse of `supersedes`, kept symmetric") but never enforced; and every row of the central register ([`steering/ADR.md`](ADR.md)) agrees with the `superseded-by` of the record its link points at.
  A `<...>` placeholder (a force template's SPECIMEN frontmatter) is not a reference and is skipped, the same test `hash_seal.is_frozen` already used for a specimen `provenance.id`.
- **Fixed:** three real asymmetric references, found by the new check, not suspected: ADR-001, ADR-002 and ADR-006 (`phases/naive-sketch/`) each carried `superseded-by: null` although the register and their superseding record (ADR-014, ADR-015, ADR-017) had already recorded the other direction.
  Retrofitted `superseded-by` on the three, the same way [`hosting-codeberg-github-mirror.md`](../phases/refoundation/phase-10-schema/hosting-codeberg-github-mirror.md) already had it added when [`hosting-github-canonical.md`](../phases/refoundation/phase-10-schema/hosting-github-canonical.md) superseded it — the pointer is kept live, only the decision's own reasoning is dated-fixed.
- **Added:** [`scripts/test_ulid_check.py`](../scripts/test_ulid_check.py), fixtures on the same model as `test_frontmatter_lint.py` — a dangling reference, a broken symmetry, a register disagreement, a `<...>` placeholder, a list-valued reference — run by the gate (`ulid-test`) before the corpus check it gates.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.13] — Phase 11 T3: YAML source, generated JSON

- **Changed:** the schema's source of truth is now [`schema/frontmatter-rules.yaml`](../schema/frontmatter-rules.yaml) — hand-edited, `#` comments allowed, replacing the `"//"` key JSON used as a comment substitute.
  [`scripts/generate_schema.py`](../scripts/generate_schema.py) compiles it to `schema/frontmatter-rules.json`, the artifact `frontmatter_lint.py` and any other dependency-free reader actually loads; the two files carry identical data.
  This retires `schema/frontmatter.schema.json`, whose name claimed a JSON Schema dialect the hand-written validator never implemented.
- **Added:** a drift check — `scripts/generate_schema.py --check` regenerates the JSON in memory and diffs it against the committed file, failing loud on any mismatch.
  Wired into `check.py` as `schema-drift`, run before anything that loads the generated file, so a schema edit can never go unenforced because the generated artifact was left stale.
- **Fixed:** compiling the YAML source with a plain `yaml.safe_load` turned `error_enums.constitutive: [yes, no]` into `[true, false]` — YAML 1.1's implicit bool resolution, the exact failure mode Phase 11 T2 fixed for frontmatter *documents*, reappearing in the schema's own source.
  `scripts/generate_schema.py` now loads through `yaml_frontmatter.StrictLoader` (renamed from the module-private `_Loader`, now an explicit shared export) — the same string-only, duplicate-key-errors loader `yaml_frontmatter.py` already used, so this class of bug is fixed once, not twice.
- **Changed:** the two `still_open` cross-references in [`steering/open-questions.md`](open-questions.md) now point at `schema/frontmatter-rules.yaml`.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.12] — Phase 11 T2: parse YAML with YAML

- **Changed:** frontmatter is parsed as **real YAML**, through one shared reader, [`scripts/yaml_frontmatter.py`](../scripts/yaml_frontmatter.py), on `pyyaml` pinned in the devShell (`python3.withPackages`, no new flake input).
  It replaces three hand-rolled comma-and-colon splitters: the one in `frontmatter_lint.py`, and the one duplicated in `slug_check.py` and `ulid_check.py` (which `slugify_names.py` imported).
  `hash_seal.is_frozen` reads its three fields through it too; the seal's line-based canonical form is untouched, and every seal still verifies.
- **Ruled:** two departures from `yaml.safe_load`, each for a failure it would otherwise introduce.
  Scalars stay strings and only `null` resolves, because YAML 1.1 reads `constitutive: no` as a boolean, an all-digit ULID as an integer and a date as a date — against a schema whose vocabulary is strings.
  Duplicate keys are errors at any depth, because pyyaml silently keeps the last one.
- **Added:** [`scripts/test_frontmatter_lint.py`](../scripts/test_frontmatter_lint.py), fixtures on the MD100 harness model, run by the gate before the corpus checks.
  Nine of its ten lint cases fail against the old parser: five documents it wrongly passed (a field hidden by indentation, a plain scalar folded onto the next line, a duplicate key at the top level and inside an inline map, an unterminated quote), one it failed for the wrong reason, and three valid documents it rejected.
  The tenth pins the string-typing policy.
  In the corpus, the only value the old parser misread was the root README's `axis`, which carried its trailing `# comment` inside the value; nothing checked it, so nothing failed.
- **Changed:** `check.py` re-runs itself under `nix develop` when its interpreter lacks `pyyaml`, and fails loud without nix.
  The validators that import the parser no longer claim "stdlib only".
  `ulid.py`, `rename_doc.py` and the MD100 harness still make that claim, and still truthfully, so their comments are kept; the plan's T2 row listed them by mistake and is corrected.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.11] — Phase 11 T1: close the frontmatter vocabulary

- **Changed:** `frontmatter_lint.py` now **rejects any field outside `required` ∪ `optional_fields` ∪ `root_only_fields`**, and `load_schema()` refuses to start if an `optional_fields` entry has no rationale string — "declared" and "justified" are now the same act.
  `schema/frontmatter.schema.json`'s `optional_fields` is rewritten one key per field (it previously bundled several field names into a single description, e.g. `supersedes` silently covering `superseded-by`, `retention`, `pin`, `order`, and `phase`), each now carrying its own rationale.
- **Ruled:** the four vocabulary cases the gate could not see, checked against the two documents that actually define the intended vocabulary (`writing/frontmatter.md`'s field table and `operationalizing/README.md`'s coordinate inventory), not against corpus habit alone.
  `pin` is **declared and justified** — `writing/frontmatter.md` already names it as a real coordinate ("fixity anchor for a cross-project reference"); it is unused only because this repo is a single-project (topology A) instance and never instantiates the `projects/`-submodule topology it fixes a reference into.
  `phase` (2 documents, `steering/roadmap.md` and `steering/foundation.md`) is **declared and justified** and **added to `writing/frontmatter.md`'s field table**, which had drifted: `git log -p` shows the field is bumped forward as a steering document is reconciled to a later phase, not fixed at creation — a real, machine-checkable coordinate the reference document had simply never recorded.
  `note` (4 documents) is **dropped**, and reconsidered on stronger grounds than "undeclared": `writing/frontmatter.md` states the frontmatter carries only "hard coordinates not derivable from one another" and exists so "the machine" gets a document's coordinates "without a human reading them" — `note` is free prose nothing reads, present in neither canonical field list.
  Each of the 4 documents' `note:` value is moved into its own opening prose instead of dropped outright.
  `review` (1 use, `steering/roadmap.md`) is **dropped**: `git log -S"review:"` traces it to a single silent addition in the Phase-10 sweep commit, with no explanation anywhere and no field-table entry.
  `order` (0 uses) is dropped for the same absence of any documented rationale.
  The single `review: 10-schema` line is removed from `steering/roadmap.md`.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.10] — Phase 11 inserted: tooling hardening

- **Planned:** **Phase 11 — tooling hardening**, inserted before the Phase-II design.
  Phase 10 reconciled the schema and enforced it, but enforcement stops at the nine required fields and six enums: the vocabulary is open (`note` and `review` sit in the corpus declared nowhere, while `order` and `pin` are declared and unused), the YAML parser is hand-rolled and mis-parses silently instead of failing, and no identifier is checked to point at anything.
  Hardening is placed first because Phase II generates *from* the frontmatter, and generation inherits every weakness the catalogue carries.
  A sequencing decision, so it is held here and in the roadmap rather than in the ADR register (ADR-032).
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))
- **Changed:** **unstarted phases are no longer numbered.**
  Inserting this phase moved a forward reference for the second time (the Phase-09 insertion did it first), so the roadmap now names and orders work it has not begun rather than giving it an ordinal it cannot keep.
  A phase takes its number when we tackle it — the same move the ADR register already makes, where the ordinal is a generated display label and the identity lives elsewhere (ADR-028).
  Referring to unstarted work by number is what made both insertions a renumbering sweep; the sweeps were the symptom, the numbering was the cause.
- **Recorded:** folding the frontmatter validator into markdownlint was considered and **rejected on evidence** — a custom rule receives frontmatter as raw text, no YAML parser is reachable from it, and the VSCode extension loads custom rules in its own Node context, so any external dependency would pass in CI and fail in the editor.
  Referential integrity is also corpus-level, which markdownlint's per-file model cannot express.
- **Changed:** stale phase claims corrected, since a misleading comment is worse than none — the root `README` and `phases/README.md` both still announced Phase 10 as *next* and Phase 11 as the Phase-II design, and the roadmap's own `phase:` field still read `08-refactor`.

## [v4.0-alpha.9] — hosting reversed: GitHub canonical

- **Decided:** the canonical repository is **GitHub**, and there is **no mirror** — superseding the Codeberg decision of alpha.7, which was recorded but never enacted (no Codeberg repository was ever created).
  Ground: Codeberg restricts predominantly AI-generated repositories and this one is substantially AI-assisted, so the sovereignty #029 sought there would have been borrowed tolerance, not sovereignty.
  The freedom argument is relocated, not withdrawn — it is deferred to a **self-hosted Forgejo instance**, which becomes canonical when it exists.
  ([decision](../phases/refoundation/phase-10-schema/hosting-github-canonical.md); register #034, supersedes #029)
- **Added:** host-independence as a **standing obligation** — no GitHub-only automation may move into `scripts/check.py`, so the eventual migration stays a remote change plus a CI port.
- **Fixed:** the `sentence-per-line` fixture harness matched nothing.
  Its violation regex expected a severity token between the column and the rule name that markdownlint-cli2 does not emit, so every positive fixture parsed as "no violations" and every negative one passed vacuously — the MD100 rule itself was correct all along (18/18 once the regex was fixed).
- **Removed:** `.github/instructions/mermaid.instructions.md` — vendor boilerplate that carried no catalogue frontmatter and failed the gate.

## [v4.0-alpha.8] — Phase 10 schema & governance reconciliation

- **Decided:** **`register` is derived, never stored** — `constitutive ? govern : direction-of-fit(force)` — and a new required, stored **`constitutive: yes|no`** carries the markedness the old know/do/govern triad hid (`govern` was never a third direction of fit).
  Settles ⚑ Decision 2; supersedes the register part of ADR-016, refines that of ADR-025; the three `writing/forces/` doors are unchanged.
  Deriving `constitutive` from `force × power` stays deferred.
  (ADR-030)
- **Changed:** `intention` is stored as the **coarse** family `state` · `formative` · `suasive` · `affective`; the fine aims (locate/model/enable/convince) remain in the guidance as *readings* of a stored value, not as values.
  Settles ⚑ Decision 1.
- **Changed:** the corpus swept to match — 89 of 93 catalogued documents rewritten (fine `intention` → coarse, stored `register` removed, `constitutive` judged per document: 21 `yes`, 72 `no`).
- **Changed:** `schema/frontmatter.schema.json` reconciled and `scripts/frontmatter_lint.py` **promoted** — coarse `intention`, absent `register`, and present `constitutive` are now **errors**, not warnings; the schema also encodes the direction-of-fit table (the linter refuses to load a table that does not partition the twelve forces exactly) and `frontmatter_lint.py --registers` computes the derived value.
- **Decided:** **content-hash fixity** — an optional `hash: sha256:…` seals each frozen record, with the canonical form defined exactly; `scripts/hash_seal.py` mints (`--frozen`, `--reseal`, `--print`) and `scripts/hash_check.py` verifies.
  Where `pin` fixes what a document *points at*, `hash` fixes what it *is*.
  (ADR-031)
- **Decided:** **ADR tiering** — a decision earns an ADR only by installing a **standing obligation to verify and apply**; a punctual action is a changelog line.
  `CONTRIBUTING`'s trigger relaxed from a four-subject list to that test; the register reviewed by receivability (27 of 28 kept, three borderlines named).
  (ADR-032)
- **Removed:** ADR-019 (restart strategy) from the register — a punctual sequencing decision.
  Its frozen record stays unedited; the plan content moves to a roadmap "plan changes" note; the generated ordinal absorbs the gap without renumbering.
- **Decided:** **`operationalizing` is the sixth function**, between theory and product — recording a decision ratified and enacted in alpha.7 but never written to the register; the function set is reconciled in `foundation.md`, `CONTRIBUTING`, and the root `README`.
  (ADR-033)
- **Changed:** the product guidance realigned with the schema — `writing/frontmatter.md` (the `constitutive` and `hash` fields, `register` as a derived view, the required set now eight), `writing/concepts.md` (the register re-founding, coarse-vs-fine made explicit), `writing/choosing.md` (a new step 4: judge whether the act constitutes).
- **Added:** two checks to the gate — fixity, and a `git status --porcelain` assertion, so untracked on-disk cruft can no longer pass a gate that reads only `git ls-files`.
- **Closed:** two technical debts — the untracked reorg zombies (gone, and the gate now notices) and the duplicated round-2 blind-test transcripts (byte-identical; the `weft-blindtest-round2/` copy deleted).
- **Closed:** Phase 10 — `steering/open-questions.md` now holds nothing open; the ratified deliberations are decanted into ADR-030–033, and what remains undecided is listed as `still_open` in the schema rather than as a live question.

## [v4.0-alpha.7] — hosting: Codeberg canonical + GitHub mirror

- **Decided:** the canonical repository is **Codeberg** (non-profit, EU, Forgejo), **mirrored to GitHub** for visibility; contributions land on the canonical, CI on the canonical or the mirror.
  Rationale: visibility (GitHub) + freedom/sovereignty (FSF/GNU rate GitHub `F`; SFC's *Give Up GitHub* recommends Codeberg/Forgejo; GNU Guix moved to Codeberg).
  ([decision](../phases/refoundation/phase-10-schema/hosting-codeberg-github-mirror.md); register #029)
- **Added:** a root `.gitignore` (`.DS_Store`, `__pycache__`, Nix outputs) — closes the untracked "zombie directory" gap; `git clean -fd` retires them.
- **Note:** the technical setup (Codeberg repo, remotes, push-mirror, CI port) is executed with Claude Code, per the ways-of-working division.

## [v4.0-alpha.6] — Phase 09 tooling (enforce the conventions, ready the catalogue)

- **Added:** a reproducible **Nix `devShell`** (`flake.nix`/`flake.lock`) pinning `markdownlint-cli2`, node, python, and git per project — so local and CI run the same bit-for-bit tools; install/usage in `steering/environment.md`.
- **Added:** a **unified markdownlint** ruleset shared by the CLI and the VSCode extension — title in frontmatter (no body `# H1`), a custom `sentence-per-line` rule enforcing ADR-021, defaults taken over explicitly; the corpus was reflowed to one sentence per line (286 splits + 48 joins, rendering-neutral) to zero violations.
- **Added:** a **frontmatter-lint** safe starter (`scripts/frontmatter_lint.py` + `schema/frontmatter.schema.json`) — errors on the settled invariants, warns on the contested ones (handed to Phase 10).
- **Decided:** **ULID + slug identifiers** (ADR-028) — canonical `id: <ULID>` in frontmatter, filenames stay `<slug>.md` (ULID *not* in the name), two minting modes (ADRs chronological, phases ordinal via an `order` key), generated display ordinal; `scripts/ulid.py` mints, `scripts/ulid_check.py` verifies ids, `scripts/slug_check.py` lints filename == slug.
The naming convention is kept **open**, with tools both ways — `scripts/slugify_names.py` (→ `<slug>.md`) and `scripts/migrate_ids.py` (→ `<slug>-<ulid>.md`), both on the safe-rename core `scripts/rename_doc.py`; legacy count-named records are left as-is for now.
- **Added:** one **gate** — `scripts/check.py` (markdownlint + frontmatter + ULID + links), always using the *pinned* markdownlint; wired into an opt-in pre-commit hook and a CI workflow.
- **Added:** `steering/technical-debt` (the deferred-work register) and `steering/environment.md`.

## [v4.0-alpha.5] — roadmap: insert Phase 09 (tooling), renumber

- **Changed:** the roadmap gains **Phase 09 — Tooling** (unified markdownlint sharing one ruleset between CLI and the VSCode extension; a *safe-starter* frontmatter-lint harness; ULID + slug identifiers replacing the sequential counts, with minting and verification).
  The former schema-reconciliation phase becomes **Phase 10**, and design-of-Phase-II becomes **Phase 11**; the *refoundation* era now spans phases 06–10. Tooling is placed *before* the schema so the lint harness makes Phase 10 efficient. A detailed plan lives in [`phases/refoundation/phase-09-tooling/plan.md`](../phases/refoundation/phase-09-tooling/plan.md). Frozen records from earlier phases keep their-time phase numbers; the live plan and governance docs are renumbered.

## [v4.0-alpha.4] — refounded vocabulary, the twelve forces, and the gerund shelf (Phase 08 complete)

- **Changed:** `perlocution` → `intention` across the product and catalogue — a constitutive floor (`state`) with an optional aim above it (`locate`/`model`/`enable`/`convince`, grouping into `formative`/`suasive`/`affective`); the field, the guidance prose (`writing/concepts.md`, `frontmatter.md`, `choosing.md`, the force stances), and the twelve v3 `perlocution: none` frontmatters all convert (`none` → `state`).
  (ADR-026; refines ADR-015)
- **Clarified:** know/do/govern named as a **register gloss** over `force` (a generated view, not the shelf axis); `recommend` and `entail` as extension examples; the **machine** as the recipient relation at its limit (maximum distance, quiet power) — a flag, never a role.
  (ADR-016; ADR-017/022)
- **Added:** the nine not-yet-built forces — `explain`, `describe`, `teach`, `recommend`, `mandate`, `commit`, `propose`, `prove`, `account` — authored under `writing/forces/` (stance `README.md` + `template.md`); all twelve forces are now built.
- **Removed:** `_legacy/` (the migration source) and `structuring/applied.md` (the stale v3 self-reading, superseded by `self-application.md`).
- **Renamed:** function folders and `provenance.id` to the **gerund** form — `theory→theorising`, `write→writing`, `structure→structuring`, `imagine→imagining` (`steering` already conformed); the `theory` nested git repo absorbed via a history-preserving subtree merge.
  (ADR-027)
- **Changed:** `phases/` grouped into **physical era folders** (`naive-sketch/`, `refoundation/`); stale `written-at`/`valid-for` v3 markers dropped from the live docs.
- **Added:** `steering/open-questions.md` — the live deliberation register (⚑ intention coarse-vs-fine, ⚑ register stored-vs-derived → Phase 10) — and `scripts/linkcheck.py`, the phase-close link gate (reports zero broken links).

## [v4.0-alpha.3] — provenance shelf & the govern model (Phase 08)

- **Changed:** the source is now shelved **provenance-first** — the generic `docs/` bucket is dissolved into `steering/` (governance) and root `phases/` (frozen records), and `imagine/` is added at root (Phase II, parked).
  One folder per function: `theory/` `write/` `structure/` `steering/` `imagine/`, plus `phases/`.
  (ADR-024)
- **Changed:** the root axis declaration moves from `scope` (dominant `user`) to `provenance` (dominant `contributor`); the root `README` provenance is `steering` — `onboarding` is a *served* reading order, not a producer function.
  (ADR-024)
- **Clarified:** a `govern` document is classed by the **domain it governs**, not by register; `steering` is the activity whose domain is the project itself (so it carries its own know/do/govern); a *decision* (frozen) and the *rule* it installs (current) are two documents joined at the state/change seam.
  (ADR-025)
- **Added:** the **transversal/vertical** governance tension named as irreducible, with a root **governance-axis** declaration (central vs local), a subsidiarity/VSM procedure, and a `concerns` coordinate (the activities a document governs, distinct from its `provenance`); per-activity views are **generated, not moved**.
  (ADR-025)
- **Renamed:** the perlocution/intention **floor value `none` → `state`** — the floor is not absence; the act establishes a state in the reader and shadows the unsaid.
  The coarse set is now `{state, formative, suasive, affective}`.
  Canonical vocabulary updated; the twelve v3 `perlocution: none` frontmatters convert with the vocabulary pass.
  (ADR-026; refines ADR-015)
- **Note:** references updated across the live docs (root `README`, `steering/ARCHITECTURE`, `steering/README`, `CONTRIBUTING`, `write/**` pointers, `foundation`, `roadmap`); frozen ADR records and historical changelog entries are left as-is.
  The refounded vocabulary in the v3 files and the `_legacy/` migration remain the rest of Phase 08.

## [v4.0-alpha.2] — tutorial rewrite from the blind test (Phase 07)

- **Added:** a blind test — a fresh agent followed the tutorial on this project and on `weft` (external), each with an adversarial review; artifacts kept under `phases/phase-07-structuring-tutorial/blind-test/`.
  (ADR-023)
- **Changed:** a **function** is now an activity *of relevance* (importance), not a *recurring* one — admitting one-off-but-central, once-per-person, and defensive activities.
  (ADR-023)
- **Added:** the **fractal method** made explicit — coarse-first, ~3–7 per level, group past 7, refine on intolerable gaps, see-your-holes — with an explicit licence to leave the path; the tutorial no longer pretends to be deterministic.
  (ADR-023)
- **Changed:** the source tree is organized **for the author** (first reader), not "the user"; the generated reader surface is deferred to a planned frontmatter tutorial.
  (ADR-023)
- **Added:** **`imagine`** as a first-class activity, homing intended/future (Phase-II-shaped) work.
  (ADR-023)
- **Added:** worked examples via the **conventional repo documents** (README, INSTALL, CONTRIBUTING, LICENSE, ARCHITECTURE, CHANGELOG, ADR) — named, classified, placed — plus two/three valid trees and a fractal folder rule; two entry-states (greenfield / existing-audit).
  (ADR-023)
- **Changed:** the neutral blind-test spec (`self-spec.md`) revised to close the state gaps the reviews surfaced, kept neutral on structure.
  (ADR-023)
- **Verified:** a second blind test (round 2, `weft`) validated the rewrite — four of five round-1 cold-stops resolved — and drove three folded refinements: entry-state keyed to what is *written* not code; a co-owned document assigned by who authors/maintains it (honoring the Step 3 → 5 promise); and the open-question/deliberation life (a *current* `govern` doc that decants into frozen records, refining current/frozen rather than breaking it).
  Artifacts under `blind-test/weft-*-round2.md`.
  (ADR-023)
- **Added:** `self-application.md` — the rewritten tutorial run on this project itself (dogfood), deriving our functions (`theory`/`writing`/`structuring`/`steering`/`imagine`), the controlled front-matter vocabulary, and our target source tree; supersedes the stale v3 `structure/applied.md`.
- **Proposed → Phase 08** *(enacted in alpha.3)*: root axis moves from `scope` (dominant `user`) to `provenance` (dominant `contributor`); `onboarding` provenance retired (a served order, not a producer function); add `steering/open-questions.md` (the pending deliberation: schema Decisions 1 & 2).
- **Closed:** Phase 07 — tutorial delivered and hardened, foundation reconciled, rewrite validated, system dogfooded on itself; records frozen.

## [v4.0-alpha.1] — front-end correction (Phase 07)

- **Changed:** the front-end is derived **functions-first** — a project's functions are laid flat, and its communities and their `distance` are derived from them, not assumed.
  (ADR-022; refines ADR-017)
- **Changed:** `distance` is **per discourse community** (per domain), not a single beginner/initiated axis.
- **Clarified:** a function *is* a provenance type — no function-vs-provenance tension; `synchronic ⇒ function`, `diachronic ⇒ its producer` (a project or a function's change-stream).
- **Added:** groupings are mutable; the phase log is grouped into three **eras** (naive sketch 01–05, refoundation 06–09, phase II later).
- **Changed:** the structuring tutorial (`structure/tutorial.md`) rewritten functions-first, now reaching placement; `foundation.md` reconciled.

## [v4.0-alpha] — refoundation & front-end (Phase 06)

- **Changed:** the theory is refounded on Ferraris's documentality; the three revised essays are the new basis (supersedes the v1–v3 basis).
  (ADR-014)
- **Changed:** perlocution has no zero — a constitutive floor plus an intention (formative/suasive/affective); forces are recognized cells, not primitives.
  (ADR-015; supersedes ADR-002)
- **Changed:** know/do/govern reframed as a register gloss; recommend & entail as extension-method examples.
  (ADR-016)
- **Changed:** audience for this project — roles collapse, `distance` (beginner/initiated) is the live axis, human/machine orthogonal.
  (ADR-017; supersedes ADR-006 for this project)
- **Decided:** source folder = producer's shelf; the reader surface is generated from the catalogue; the catalogue is the single pivot.
  (ADR-018; refines ADR-010)
- **Added:** the front-end laid flat — `foundation.md` and `roadmap.md` — and the restart strategy, Phase-I scope, and semantic line breaks.
  (ADR-019, ADR-020, ADR-021)
- **Note:** this is a refoundation in progress; the product refactors to the new vocabulary in Phase 08, the schema in Phase 09.

## [v3.2] — records & governance

- **Changed:** decision records regrouped **by phase** (`docs/phases/`) instead of a flat `decisions/` pile — provenance filing, not force filing.
  (ADR-012)
- **Added:** the central register `docs/ADR.md` (the `enact` act) and a permanent `steering` function owning the governance docs; frozen records now belong to their `phase-NN` project.
  (ADR-012)
- **Changed:** `provenance` on `docs/` split into `steering` (maintained) and `phase-NN` (frozen), replacing `maintenance`/`v3-redesign`.
  (ADR-012)
- **Added:** `decide` now has a forward **`entail`** face (act / justify / entail); the stance and template carry an explicit Entail section.
  (ADR-011)
- **Deprecated:** `docs/decisions/` — redirected, not erased.

## [v3.1] — content / docs disentangled

- **Changed:** split the *product* (content for users) from `docs/` (the repo's own internals for contributors).
  Root `dominant-community` corrected from `contributor` to `user`.
  (ADR-010)
- **Changed:** the product's axis renamed from `activity` to **scope** (one document vs the whole corpus).
  (ADR-010)
- **Changed:** `provenance` now names the maintaining function (`onboarding`/`writing`/`structuring`/`maintenance`) instead of a blanket `doc-system`.
  (ADR-010)
- **Added:** `docs/` with `ARCHITECTURE`, `CONTRIBUTING`, `CHANGELOG`, and this decision log.

## [v3] — self-similar reorganization

- **Changed:** flat `writing.md` / `structure.md` replaced by `write/` and `structure/`, each split by force (explain / instruct / recommend / mandate / describe).
  (ADR-007)
- **Added:** forces grouped under three doors in `write/forces/{know,do,govern-and-record}/`.
  (ADR-007)
- **Added:** `tutorial.md` — a `teach` on-ramp; obligations enforced by validation, not reading order.
  (ADR-009)
- **Added:** `axis` / `dominant-community` declared at each tree root.
  (ADR-008)
- **Moved:** the audience model into `structure/` (premise of the communication system).
  (ADR-006)

## [v2] — theory sharpening

- **Changed:** `formative: true|false` replaced by the `perlocution` typology (`locate`/`model`/`enable`/`convince`/`none`); `prove` and `decide` reclassified as `convince`.
  (ADR-002)
- **Added:** `recommend` as the twelfth force, on the deontic gradient instruct → recommend → mandate.
  (ADR-003)
- **Removed:** the `diataxis` frontmatter field — re-derived from `force` × `perlocution`.
  (ADR-004)
- **Clarified:** `verb` is a soft summary of the coordinate tuple; stored only when it diverges.
  (ADR-005)

## [v1] — foundation

- **Added:** the inscribed-act reframe — a document is an act with a `force`, and the force generates the writing.
  Eleven forces, move structures, readability patterns, frontmatter catalogue.
  (ADR-001)
