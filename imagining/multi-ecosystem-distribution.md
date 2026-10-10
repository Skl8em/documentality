---
title: "Distribution across ecosystems — one documentation system, installable from Python, Rust, JavaScript and R projects"
force: propose
intention: suasive
view: diachronic
provenance: { type: function, id: imagining }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

A proposal for how the tooling reaches projects that do not use Python.
The `docsys` package is Python, installed as a development dependency; a Rust crate, an R package or a JavaScript project has no natural place to declare it.

## The need

An adopter installs the tooling the way its own ecosystem installs development tools, pinned in its own lockfile:

| Ecosystem | Where a dev tool is declared | Lock |
| --- | --- | --- |
| Python | `pyproject.toml`, development dependency group | `uv.lock` |
| Rust | `Cargo.toml` (`[dev-dependencies]`), or a pinned `cargo install` | `Cargo.lock` |
| JavaScript | `package.json`, `devDependencies` | `package-lock.json` |
| R | `DESCRIPTION` (`Suggests`), with `renv` | `renv.lock` |

Nix covers all four through a flake input, for adopters who use it.

## The requirement: one package per ecosystem, one API

Each ecosystem gets its own package, installed the way that ecosystem installs development tools.
What a package uses inside — native code in its own language, or a shared engine it wraps — is that package's choice.
What every package must honour is one **API**, so that a project's documentation files and configuration mean the same thing whichever package reads them:

1. **The instance configuration**, `docsys.yaml`: the same keys, the same meaning, the same refusals.
   It carries a format version, so a package can say which versions it reads.
2. **The methodology**: the frontmatter vocabulary and its rules (`frontmatter-rules.yaml`), versioned as one artefact that every package loads unchanged.
3. **The baseline** of legacy documents, in the same format.
4. **The CLI surface**: the same commands (`check`, `report`, `init`, `new`), the same options, the same exit codes.
5. **The findings**: the same format — path, line, rule identifier, message, `fix:` clause — so an agent reads one package's output as it reads another's.
6. **A conformance suite**: each rule stated as input documents and expected findings, in data files, run by every package.
   The suite, not any one package, defines what a rule does; a package conforms when it passes it.

## Implementing a package

Two strategies, chosen per package rather than once for all:

- **Native**: the checks implemented in the ecosystem's own language, filling that ecosystem's gaps (a Markdown linter where none fits, the runner).
  Most inspectable and modifiable by that ecosystem's contributors; every rule change is one change per native package, which the conformance suite keeps honest but does not make free.
- **Wrapped**: the package ships or fetches a shared engine, compiled to a single binary — Rust, on this project's stated preferences — the way `ruff` reaches Python projects [packaging details: to verify].
  One implementation of each rule; less inspectable for an adopter who does not read the engine's language, which counts against it on the emancipation criterion.

The Python package is the reference implementation until a second package exists.
Its fixtures are written as data files from the start, so they can become the conformance suite without a rewrite.

## The runner and `weft`

The gate's runner sequences checks, runs fixtures before the checks they validate, and reports per check.
That is a task graph with preconditions — the problem `weft` exists to solve.
When `weft` exists, the runner is a candidate to become a `weft` registry rather than a second, ad hoc orchestrator.

## What this does not settle

- Which strategy each package takes; judged per ecosystem, on the first real case.
- How the methodology — the schema and its rationale — is versioned across packages, so that an adopter's frontmatter keeps its meaning when the vocabulary changes.
