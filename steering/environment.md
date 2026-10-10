---
title: "Development environment — the reproducible tooling shell"
force: instruct
verb: walk-through
intention: state
view: synchronic
provenance: { type: function, id: steering }
constitutive: no
audience: [contributor]
reader: H+M
status: draft
---

The project's tooling (the markdown linter, Node, Python, `uv`) is **pinned per project** in a Nix `devShell`, not installed globally.
This gives every contributor — and CI — the same bit-for-bit toolchain, so a check that passes locally passes everywhere.
Follow this to get the environment; the reasoning is in the Phase-09 [`plan.md`](../phases/refoundation/phase-09-tooling/plan.md) §Part 0.

## Prerequisites

- **Nix** with flakes enabled (`experimental-features = nix-command flakes`).
- Nothing else: the shell provides `markdownlint-cli2`, `nodejs`, `python3` with `pyyaml`, and `uv`.
  Run everything below inside it; a tool of the same name installed elsewhere on the machine is not the pinned one.

## Enter the shell

```sh
nix develop
```

This drops you into a shell with the pinned tools on `PATH`.
The exact versions are frozen in [`../flake.lock`](../flake.lock); the same lock is used in CI.

If you use **direnv** (with `nix-direnv`), the committed [`../.envrc`](../.envrc) enters the shell automatically on `cd`; run `direnv allow` once.

## Run the checks

```sh
python3 scripts/check.py     # the full gate: markdownlint + frontmatter + ULID + links
```

Our own validators under [`../scripts/`](../scripts/) are Python, and every one that reads frontmatter parses it as real YAML with `pyyaml`, pinned in the shell next to its interpreter.
`markdownlint-cli2` needs the shell too (it is a Node binary), because its version is part of the contract with our custom rules.
`check.py` never runs from a stray global copy: started outside the shell, it re-runs itself under `nix develop`, and without nix it fails rather than run on other versions.

In VS Code, the task `docs: run the gate` (*Terminal › Run Task*) runs the same command and puts each failure in the Problems pane, on the file and line it names.

## Enable the pre-commit hook (optional)

To run the gate automatically before each commit, point git at the committed hooks directory once:

```sh
git config core.hooksPath .githooks
```

The [`../.githooks/pre-commit`](../.githooks/pre-commit) hook then runs `scripts/check.py` and blocks a commit that fails the gate.

## Work on the engine, `docsys/`

The engine is its own Python project, a git submodule.
The flake pins `uv` and the interpreter; the engine's own `uv.lock` pins its Python packages, basedpyright and ruff among them.
Inside the shell, `uv` builds every `.venv` on the flake's interpreter and downloads none (`UV_PYTHON`, `UV_PYTHON_DOWNLOADS=never`, set by the shell).

```sh
nix develop
git submodule update --init
uv sync --locked                    # this repository's .venv: docsys installed editable
cd docsys
uv sync --locked                    # the engine and its tools, in docsys/.venv
uv run pytest                       # its tests, which also run basedpyright and ruff
```

`--locked` fails rather than rewrite a `uv.lock` that no longer matches its `pyproject.toml`; a change of dependencies is locked deliberately, with `uv lock`, inside the shell.
A `.venv` points at the flake's interpreter by its Nix store path: after `nix flake update`, or a garbage collection that removed that path, run the two `uv sync` again.

In VS Code, open [`../documentation-system.code-workspace`](../documentation-system.code-workspace) rather than the folder, and install the extensions it recommends, basedpyright and Ruff.
Each folder of the workspace names its interpreter, the `.venv` above, so the editor needs no global Python.
The `docsys` folder runs the copies of basedpyright and ruff in `docsys/.venv`, with the engine's `pyproject.toml`, so the editor reports what `uv run pytest` reports.
basedpyright turns Pylance's own checking off.

## Lint Markdown in the editor

The markdownlint extension (`DavidAnson.vscode-markdownlint`) reads the same configuration and custom rule as the gate, but cannot run the devShell's `markdownlint-cli2`: it runs the copy it bundles.
So the extension is held at the release that bundles the version `flake.lock` pins, today **0.59.0**, which bundles `markdownlint-cli2` 0.17.2:

```sh
"/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" \
  --install-extension davidanson.vscode-markdownlint@0.59.0 --force
```

(`code`, if it is on your `PATH`.)
Installing a given version pins the extension: VS Code stops updating it.
The pin is VS Code's, not the project's, so it applies to every folder you open.
The gate's `editor-markdownlint` check fails when the extension bundles another version than the flake's, and names both; the `dependencies` of an extension release's `package.json` say which `markdownlint-cli2` it bundles.

## Update the toolchain

Bumping a tool is a deliberate, reviewed act — not a side effect of a global update:

```sh
nix flake update            # bump nixpkgs (and thus the pinned tools)
```

Commit the changed `flake.lock` in its own change, and re-run the checks, especially the markdown lint — a `markdownlint-cli2` major bump can shift the custom-rule API.
If `markdownlint-cli2` moves, `editor-markdownlint` then fails until the extension is moved to the release that bundles the new version.

## Why pinned per project (not home-manager)

Because the linter runs **custom rules we author and maintain**, the binary version is part of their contract: a rule written today can silently break under a future major.
Freezing `markdownlint-cli2` in this repo's `flake.lock` keeps that contract stable and decoupled from unrelated environment updates.
A project with only default linting would not need this — pin when the exact version is part of the behaviour you want to freeze.
