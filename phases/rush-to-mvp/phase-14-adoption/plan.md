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

And the pages an adopter or an agent reads first contradict each other or themselves (ws1).

## Rulings

Each is taken by the project owner and stated in full in [Rulings](rulings.md).

- **A package, not a vendored copy**: one engine that adopters pin.
- **The layout default**: by function, then sub-function, then register, then force.
- **`weft` is the first adopter.**
- **The engine is `Skl8em/docsys`**, a public repository mounted here as a submodule at `docsys/`.
- **The scope**: every document is in scope; an exclusion carries its reason; an inclusion brings one back.
- **Where the engine's documentation lives**: use and configuration in `codifying/`, the inside in `docsys/docs/`.
- **The tools for Python**: basedpyright and ruff, at the lockfile's versions.
- **Checks that are not the engine's** run as opt-in `tools`.
- **What precedes the switch**: accounts and author tools move to the engine, link allowances replace edits to frozen records, and `schema/` retires with `scripts/`.
- **Every Markdown file is a document**, whatever git knows of it.
- **Closing ws2** comes before ws1's remaining defects, CI first.
- **A plan is divided** into workstreams, tracks, tasks and steps, each numbered when it starts.
- **Strictness**: errors, warnings and exclusions are configurable, and the gap is reported.

## Workstreams

Scope and deliverables are in [Workstreams](workstreams.md).
A status is at most five words and replaces the previous one; anything longer goes to the workstream's own section.

| # | Workstream | Status |
| --- | --- | --- |
| ws1 | Fix what the kit will teach | not started |
| ws2 | The engine as a package, `docsys` | in progress |
| ws3 | The guided install | not started |
| ws4 | Install on `weft` | not started |
| ws5 | Close the phase | not started |

ws1 comes first because the package will ship these pages' templates.
ws2 before ws3: `init` writes a configuration the package must accept.
ws4 is the definition of done; it may start as soon as ws2 runs, and feed ws3.

## Open points

Each is argued in [Open points](open-points.md).
The blocking rule of the [Phase 12 plan](../../refoundation/phase-12-codifying/plan.md) carries over: a point that blocks a planned task stops it.

| # | Open point | Status |
| --- | --- | --- |
| 1 | Where the package lives | settled |
| 2 | Non-Python adopters | out of the era |
| 3 | What an adopter gets by default | settled |
| 4 | Adopter frontmatter when the vocabulary changes | out of the era |
| 5 | `weft`'s functions and provenance map | blocks ws4 |
| 6 | Working across two repositories | settled by ws2 |

## Verification / definition of done

- `docsys check` is green in this repository, run through the installed package.
- On `weft`, the package is a development dependency in `pyproject.toml`; `docsys init` and `docsys check` are green on the scaffold, with `weft_spec.md` either in scope or excluded with its reason, and `docsys report` lists the exclusions.
- Each ws2 and ws3 behaviour has a fixture that was red first.
- The six ws1 defects are fixed, and the root README routes a newcomer to a page that exists.

## Explicitly out of scope

- **The agent kit** — the phase after this one.
- **The life cycle of a document**, the records-continuum reframing the review proposes for it, and the closure rule: parked ([roadmap](../../../steering/roadmap.md)).
- **Generated reading surfaces**, an MCP server, integrations with issue trackers.
- **New gate checks on this repository's own state** ([ADR-042](../phase-13-design/rush-to-mvp.md), point 5).
- **Evaluating `ty`** as the engine's type checker: later, at the project owner's call.
- **Explaining a rule from the installed package** (`docsys explain <rule>`): the first work once the MVP closes ([roadmap](../../../steering/roadmap.md), *Parked*); this phase's adopters know the system.
