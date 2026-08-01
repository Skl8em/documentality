---
title: "Development environment — the reproducible tooling shell"
force: instruct
verb: walk-through
register: do
intention: state
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor]
reader: H+M
status: draft
---

The project's tooling (the markdown linter, Node, Python) is **pinned per project** in a Nix `devShell`, not installed globally.
This gives every contributor — and CI — the same bit-for-bit toolchain, so a check that passes locally passes everywhere.
Follow this to get the environment; the reasoning is in the Phase-09 [`plan.md`](../phases/refoundation/phase-09-tooling/plan.md) §Part 0.

## Prerequisites

- **Nix** with flakes enabled (`experimental-features = nix-command flakes`).
- Nothing else: the shell provides `markdownlint-cli2`, `nodejs`, and `python3`.

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

Our own validators under [`../scripts/`](../scripts/) are **stdlib-only Python**, so they also run outside the shell.
`markdownlint-cli2` is the one tool that needs the shell (it is a Node binary), because its version is part of the contract with our custom rules.

## Update the toolchain

Bumping a tool is a deliberate, reviewed act — not a side effect of a global update:

```sh
nix flake update            # bump nixpkgs (and thus the pinned tools)
```

Commit the changed `flake.lock` in its own change, and re-run the checks, especially the markdown lint — a `markdownlint-cli2` major bump can shift the custom-rule API.

## Why pinned per project (not home-manager)

Because the linter runs **custom rules we author and maintain**, the binary version is part of their contract: a rule written today can silently break under a future major.
Freezing `markdownlint-cli2` in this repo's `flake.lock` keeps that contract stable and decoupled from unrelated environment updates.
A project with only default linting would not need this — pin when the exact version is part of the behaviour you want to freeze.
