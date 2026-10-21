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

This walks ws2, a workstream of Phase 14, to its close: this repository's gate switched to `docsys check` with `scripts/` and `schema/` retired, the engine checking itself, and both phase branches pushed and green.
Continuous integration of both repositories, every Markdown file a document, the link check's allowance and the author tools are done; the engine has them, and the pages that state them are [`docsys-configuration.md`](../../../codifying/docsys-configuration.md), [`docsys-commands.md`](../../../codifying/docsys-commands.md) and the engine's fiches in `docsys/docs/`.
The rulings it carries out are in [Rulings](rulings.md); ws1's remaining defects come after it.

## Before you start

- Run every command inside the devShell (`nix develop`, or the shell direnv enters); `uv` locks only there.
- Branch, commit, rebase and merge by [`CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md) and the skill `branch-and-commit`: each track below is a branch cut from `ph14-adoption`, each task a branch cut from its track, carried out in one session and committed in steps, mirrored in `docsys/` when the task changes the engine.
  A track or a task is numbered when its branch is cut, with the next number at its level (the next track is `ph14-ws2-tr5-…`); until then this page names it by its slug (`switch-gate`).
  A track with no tasks listed is carried out as a single task of the same slug, on a task branch of its own like any other.
- Present each task to the project owner before merging it.
- Push only with the project owner's word, which *Close ws2* asks for.
- Before changing a check, read its fiche in the engine's `docs/`.

## The order

| Track | Repositories | Done when |
| --- | --- | --- |
| `switch` | both | this repository's gate is `docsys check`, and `scripts/` and `schema/` are gone |
| close | both | the plan says ws2 is done, and both phase branches are pushed and green |

The switch comes after the link allowance and the author tools because it deletes `scripts/`: frozen records' links into it need their allowance first, and the switch reseals ADR-037 with `docsys seal`.

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
3. Rewrite `gate.md` for the new gate: one command, the checks and their order the engine's, their fixtures run by the engine's CI, the tools, the environment, the output contract; the commands are those of [`docsys-commands.md`](../../../codifying/docsys-commands.md), which it points to rather than repeats.
4. Check: `docsys check` passes, and `docsys report` lists the exclusions.

Open: whether the submodule pointer `docsys` is mechanism.
Listed, every pointer commit would need an account in the same commit, or fail when the phase lands on `main`; left out, the engine's changes are paired with their accounts in the engine's repository, once `switch-engine-self-check` runs `docsys` there.
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

This closes [open point 6](open-points.md); if the project owner prefers, it moves to ws4, beside `weft`.

## Close ws2

1. Bring ws2 to *done* in the plan and in [Workstreams](workstreams.md), and add the changelog entry.
2. Merge any track still open into `ph14-adoption`, the engine first.
3. Push both phase branches with the project owner's word, the engine first and this repository after: CI here checks the submodule out at the commit the pointer names, which must already be on the engine's remote.
4. Check: `gh run list -R Skl8em/docsys` and `gh run list` show a green run on each pushed commit.
   On a red run, read `gh run view <id> --log-failed`, fix it in a new task, and push again.

The links from this repository to the engine's fiches and to its `main` point at a branch that receives the phase only when the phase closes: they stay dead on GitHub until then, and the link check does not read web links.

## When something fails

- **CI is red but the gate passes locally:** a fixture depends on the machine (a default branch, a tool on the `PATH`); reproduce it with `GIT_CONFIG_GLOBAL` or a shell without your profile.
- **The hook refuses a commit in the middle of the switch:** the commit must pass the gate it installs; split it so that each commit passes the gate in force.
- **`uv.lock` changes revision:** it was locked outside the devShell; lock again inside it.
- **A commit fails the paired-change rule only on `main`:** it changed the mechanism without its account; amend it with its account before the merge, or move `paired_change.since` past it with a reason.
