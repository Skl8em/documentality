---
title: "Closing ws2 — from continuous integration to the switch"
force: instruct
intention: state
view: synchronic
provenance: { type: project, id: phase-14-adoption }
constitutive: no
distance: initiated
audience: [contributor]
reader: H+M
status: draft
---

This walks ws2, a workstream of Phase 14, to its close: both repositories verified by continuous integration, every Markdown file a document, the link check's allowance, the author tools in the engine, and this repository's gate switched to `docsys check` with `scripts/` and `schema/` retired.
The rulings it carries out are in the [plan](plan.md), *Rulings*; ws1's remaining defects come after it.

## Before you start

- Run every command inside the devShell (`nix develop`, or the shell direnv enters); `uv` locks only there.
- Branch, commit and merge by [`CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md) and the skill `branch-and-commit`: each track below is a branch cut from `ph14-adoption`, each task (1.1, 1.2…) a branch cut from its track, carried out in one session and committed in steps, mirrored in `docsys/` when the task changes the engine.
  A track or a task is numbered when its branch is cut, with the next number at its level; until then this page names it by its slug (`documents`, `switch-gate`).
  A track with no tasks listed is carried out as a single task of the same slug, on a task branch of its own like any other.
- Present each task to the project owner before merging it.
- Push only with the project owner's word; it is given for *Push and verify*, to verify continuous integration.
- Before changing a check, read its fiche in the engine's `docs/`.

## The order

| Track | Repositories | Done when |
| --- | --- | --- |
| `ph14-ws2-tr1-ci` | both | both repositories' CI is green on the pushed phase branches |
| `documents` | engine; the configuration reference here | every `.md` under the workspace is a document unless an exclusion names it |
| `link-allowance` | engine; the configuration reference here | a dead link can be allowed, with its reason, and a stale allowance is reported |
| `author-tools` | engine; a commands reference here | `docsys` mints identifiers, seals, renames and slugifies; `migrate_ids.py` is in the engine's `legacy/` |
| `switch` | both | this repository's gate is `docsys check`, and `scripts/` and `schema/` are gone |
| close | both | the plan says ws2 is done, and both phase branches are pushed and green |

CI comes first because every later step is verified by it, and neither repository has a working one: this repository's has failed since 2026-10-10 on a fixture that assumes git's default branch is `main`, and the engine has none.
The allowance and the author tools come before the switch because the switch deletes `scripts/`: frozen records' links into it need their allowance first, and the switch reseals ADR-037 with `docsys seal`.

## Continuous integration, then push (`ph14-ws2-tr1-ci`)

### `ph14-ws2-tr1-ts1-ci-engine-shell` (engine)

1. Add `flake.nix` and `flake.lock` to the engine, pinning the nixpkgs this repository's flake pins (`nixos-25.05`): Python 3, `uv`, `nodejs`, `markdownlint-cli2` and `git`, with `UV_PYTHON` set to the flake's interpreter and `UV_PYTHON_DOWNLOADS=never`, as here.
   The engine is its own project and pins its own development tools; an adopter installs the package and needs none of them.
2. Add `.envrc` (`use flake`) and `.githooks/pre-commit`, which runs `uv run --locked pytest`, entering `nix develop` first when `DOCSYS_DEVSHELL` is unset.
3. Check: `nix develop --command uv run --locked pytest` passes, and `reuse lint` covers the new files.

### `ph14-ws2-tr1-ts2-ci-engine-workflow` (engine)

1. Add `.github/workflows/checks.yml`, run on push and on pull request: `actions/checkout` and `DeterminateSystems/nix-installer-action` pinned to released tags (`v7.0.1` and `v23` are the latest on 2026-10-21; check with `gh api repos/<owner>/<action>/releases/latest`), then `nix develop --command uv sync --locked` and `nix develop --command uv run --locked pytest`.
2. Check: `reuse lint` passes.

### `ph14-ws2-tr1-ts3-ci-documentality` (this repository)

1. Make `scripts/test_paired_change.py` create each throwaway repository with `git init -q -b main`, so the fixtures stop depending on the machine's `init.defaultBranch`.
   Run it red first: with `GIT_CONFIG_GLOBAL` pointing at a file that sets `init.defaultBranch = master`, it fails as CI does.
   It is a test file, so the paired-change rule asks for no account.
2. In `.github/workflows/checks.yml`, check the submodule out (`submodules: true`) and pin both actions to the engine's tags; pinning the Nix installer fixes ws1's defect (vi) on the way.
3. Check: the gate passes.

### Push and verify (both)

1. Merge the tasks into `ph14-ws2-tr1-ci`, then the track into `ph14-adoption`, the engine first and the pointer after.
2. Push the engine's `ph14-adoption` first, then this repository's: CI here checks the submodule out at the commit the pointer names, which must already be on the engine's remote.
3. Check: `gh run list -R Skl8em/docsys` and `gh run list` show a green run on each pushed commit.
   On a red run, read `gh run view <id> --log-failed`, fix it in a new task, and push again.

The links from this repository to the engine's fiches point at the engine's `main`, which receives the phase only when the phase closes: they stay dead on GitHub until then, and the link check does not read web links.

## Every Markdown file a document (`documents`, engine)

The ruling: a document is a `.md` file anywhere under the workspace but inside `.git`; `.gitignore` is not consulted, and anything left out is left out by `scope.exclude`, with its reason.

1. **Specify and red.**
   In `tests/test_documents.py`, and in a conformance case where the case format can express the files: an ignored `.md` is a document; one inside `.git` is not; an untracked one still is; one under a folder `scope.exclude` covers is not; a symlinked folder is not followed; a submodule's files are documents unless excluded.
2. **Implement.**
   `documents.files` walks the disk, skipping `.git` folders, following no symlink, and not entering a folder an exclusion covers wholly when no inclusion reaches into it, so a large `.venv/` costs nothing.
   Its callers follow: the phase-state check's folders (a folder exists when any file is in it), the register check's message about a path that is "not a tracked document", and the module's docstring.
3. **Settle at the presentation** (recommendations):
   - a workspace outside git is accepted, since documents no longer need git, and only the paired-change check, when configured, refuses it;
   - `docsys report` prints one line per exclusion with its reason and its count, and lists the documents only with `--documents`, since a `.venv/` exclusion would otherwise print hundreds of lines (the engine's own `.venv/` holds 201 `.md` files).
4. **Document.**
   The *scope* section of [`docsys-configuration.md`](../../../codifying/docsys-configuration.md), and the engine's README, which says what a document is.
5. **Check.**
   The engine's suite passes; on a copy of this repository with the engine-shaped configuration of `switch-gate`, `docsys check` reports nothing new.

## The link check's allowance (`link-allowance`, engine)

1. **Specify and red,** in `conformance/links.yaml`:

   ```yaml
   links:
     allow:
       - document: phases/refoundation/phase-09-tooling/plan.md
         target: ../../../scripts/linkcheck.py
         reason: retired with scripts/ when the gate moved to docsys; the record is frozen
   ```

   An allowed link that does not resolve is not reported.
   An allowance whose link resolves, or whose document no longer holds that link, is reported (`links/allowance`), so the list cannot outlive its reason, like `lagging:` in the phase ledger.
   An allowance without a reason is refused.
2. **Implement** the section in `config.py` and the rule in `checks/links.py`.
   The format stays version 1: no version of the package has been released.
3. **Document** the section in [`docsys-configuration.md`](../../../codifying/docsys-configuration.md), and write the engine's fiche on the link check (`docs/links.md`): its scope, and why an allowance carries a reason.

## The author tools (`author-tools`)

The commands proposed; their names and options are confirmed by the project owner before the first test is written:

| Command | From | Does |
| --- | --- | --- |
| `docsys id [--at DATE \| --order N] [--slug SLUG]` | `scripts/ulid.py` | prints a new ULID, chronological or ordinal |
| `docsys seal [PATH ...] [--frozen] [--reseal] [--print]` | `scripts/hash_seal.py` | writes a frozen record's `hash:` seal, in the fixity check's canonical form |
| `docsys rename OLD NEW [--dry-run]` | `scripts/rename_doc.py` | moves a file or folder and rewrites every relative link to it in the workspace's documents, with `git mv` when git tracks it |
| `docsys slugify [--dry-run]` | `scripts/slugify_names.py` | renames each document that declares a `slug` to `<slug>.md`, through `rename` |

1. One task per command, in this order (`seal` and `rename` are what the switch needs): `author-tools-id`, `author-tools-seal`, `author-tools-rename`, `author-tools-slugify`.
   Each ports the fixtures of `scripts/` as tests (red), implements the command typed and linted, and wires it into the CLI.
2. `author-tools-legacy`: `migrate_ids.py` goes unchanged to the engine's `legacy/`, with a README saying it does not run as it stands (it imports modules of `scripts/`) and why it is kept (the [roadmap](../../../steering/roadmap.md), *Parked*); `legacy/` stays out of basedpyright and ruff, and `reuse lint` covers it.
3. `author-tools-sentence-per-line`: the rule's test reads the severity word `markdownlint-cli2` prints after 0.17.2; check it under the pinned version and under 0.21.0.
4. Document: a commands reference here, `codifying/docsys-commands.md`, covering `check`, `report` and the four commands (how a project uses `docsys`), and the engine's fiche on the author tools.

## The switch (`switch`)

Every commit passes the gate in force at that commit: the pre-commit hook is read from the working tree, so the commit that changes the gate is verified by the new one.

### `switch-adr`

1. Write ADR-044, superseding ADR-037: the engine's YAML is the one vocabulary, read directly; `schema/` and its generated JSON retire with `scripts/`; its case against the JSON is ADR-037's own sceptical reading in [`schema-pipeline.md`](../../../codifying/schema-pipeline.md) (a reader kept in reserve that never appeared).
2. Set ADR-037's `superseded-by`, and reseal it with `docsys seal --reseal`.
3. Add the row to [`ADR.md`](../../../steering/ADR.md) and a changelog line.

### `switch-own-checks`

1. Move `editor_markdownlint.py`, its fixtures and `test_problem_matcher.py` from `scripts/` to `tools/`, this repository's own checks, and point their `checks:` entries there.
2. Rewrite the VS Code task's problem matchers for the engine's output (`path:line: rule: message — fix: …`, and the lines a tool prints under `=== name ===`), with their test first.

### `switch-gate`

One commit, paired with its account in [`gate.md`](../../../codifying/gate.md):

1. `docsys.yaml` in the engine's shape:
   - `version: 1`;
   - `scope.exclude`, each with its reason: `theorising/`, `phases/naive-sketch/`, `.claude/`, `"**/blind-test/"`, `docsys/` (another repository, checked by its own CI), `.venv/` and `.direnv/`;
   - `register` and `phases` unchanged;
   - `paired_change.mechanism`: `docsys.yaml`, `tools/`, `.githooks/`, `.github/workflows/`, `flake.nix`; `exempt`: `tools/test_`; `since`: the commit before this one, since the new mechanism list would otherwise fail every earlier commit that touched those paths;
   - `tools`: `markdownlint`, then this repository's own checks of `switch-own-checks`.
2. `.githooks/pre-commit`, CI and the VS Code task run `uv run --locked docsys check`, entering `nix develop` first when outside it; CI runs `uv sync --locked` before it.
3. Rewrite `gate.md` for the new gate: one command, the checks and their order the engine's, their fixtures run by the engine's CI, the tools, the environment, the output contract.
4. Check: `docsys check` passes, and `docsys report` lists the exclusions.

Open: whether the submodule pointer `docsys` is mechanism.
Listed, every pointer commit would need an account in the same commit, or fail when the phase lands on `main`; left out, the engine's changes are paired with their accounts in the engine's repository, once step 5.5 runs `docsys` there.
The recommendation is to leave it out; the project owner rules.

### `switch-retire`

1. Delete `scripts/` and `schema/`.
2. Allow, in `links.allow`, the links from frozen records that no longer resolve: the plans of Phases 09 and 11, `engine-config-seam.md` (two), and ADR-037's link to `schema-pipeline.md`; the gate lists any other.
3. Repoint the living pages' links: `writing/frontmatter.md` and `steering/open-questions.md` to the engine's vocabulary, and `steering/CHANGELOG.md` and `steering/external-review/external-review.md` to this repository at the last commit that holds `scripts/`, by URL.
4. Delete `codifying/schema-pipeline.md`, and bring every page that names `scripts/` or `schema/` to the present (`git grep -n -e scripts/ -e schema/ -- ':!phases/'`): the root README, `codifying/README.md`, `codifying/docsys-configuration.md`, `CONTRIBUTING.md` (the gate's command, and the rule on adding a check, which now goes to the engine, or to `tools:` when only this repository needs it), `ARCHITECTURE.md`, `environment.md`, `technical-debt.md`, `open-questions.md`, `roadmap.md`, `structuring/audience.md`, `imagining/theory-of-the-code.md`.
5. Update `pyproject.toml` (exclusions and comments), `REUSE.toml`, the flake's welcome text, and `.markdownlint-cli2.jsonc` if a path it names is gone.
6. Check: the gate passes, and `git grep -e scripts/ -e schema/` outside `phases/` names only the history.

### `switch-engine-self-check` (engine)

1. Give the engine a `docsys.yaml`: `.venv/` excluded, `paired_change` with `src/` as mechanism and `docs/` and `README.md` as understanding, enforced on `main`.
2. Its root document, the README, then needs `axis` and `dominant-community`: the project owner chooses them.
3. Run `docsys check` in the engine's hook and CI.

This closes open point 6 of the plan; if the project owner prefers, it moves to ws4, beside `weft`.

## Close ws2

1. Bring the plan's ws2 progress to *done*, and add the changelog entry.
2. Merge any track still open into `ph14-adoption`, the engine first.
3. Push both phase branches with the project owner's word, and check both CI runs are green.

## When something fails

- **CI is red but the gate passes locally:** a fixture depends on the machine (a default branch, a tool on the `PATH`); reproduce it with `GIT_CONFIG_GLOBAL` or a shell without your profile.
- **The hook refuses a commit in the middle of the switch:** the commit must pass the gate it installs; split it so that each commit passes the gate in force.
- **`uv.lock` changes revision:** it was locked outside the devShell; lock again inside it.
- **A commit fails the paired-change rule only on `main`:** it changed the mechanism without its account; amend it with its account before the merge, or move `paired_change.since` past it with a reason.
