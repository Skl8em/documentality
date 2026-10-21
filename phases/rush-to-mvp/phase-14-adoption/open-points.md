---
title: "Phase 14 adoption — the open points"
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

The questions Phase 14 leaves open or has settled, each with what settles it.
The [plan](plan.md) lists them with a status of a few words; the reasoning is here.

The blocking rule of the [Phase 12 plan](../../refoundation/phase-12-codifying/plan.md) carries over unchanged: a point that blocks a planned task stops it, and the tree goes back to the last state that stands without the point.

## 1. Where the package lives

Settled by the project owner, 2026-10-09.
The package has its own repository, included here as a git submodule and installed editable.
An agent session on the engine does not load the theory corpus; this repository consumes the engine exactly as an adopter does.
How the engine works inside is documented with it, in `docsys/docs/`, so the paired-change rule still pairs code and explanation inside one repository, while how a project uses and configures it stays in `codifying/` here.
Costs accepted with it: four links from frozen phase records into `scripts/` and `schema/` stop resolving and are allowed by the link check, each with its reason; the schema, authored with the engine, is explained by `writing/frontmatter.md` across the repository boundary.
Blocking: no.

## 2. Non-Python adopters

Out of the era.
The Python package covers `weft`; a project in another ecosystem installs it as a tool (`uv tool install`) or through the flake, unpinned by its own lockfile.
The long-term answer is in [`imagining/multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md).
Blocking: no.

## 3. What an adopter gets by default

Settled by the project owner, 2026-10-09.
Frontmatter, links, identifiers, slugs and fixity are on; the decision register is on when `init` is told where it is; the paired-change rule is off until the adopter names its mechanism and understanding paths (the agent kit will propose turning it on for the theory of the code, see [`imagining/theory-of-the-code.md`](../../../imagining/theory-of-the-code.md)); the phase checks are off.
Blocking: no.

## 4. The adopter's frontmatter when the vocabulary changes

Out of the era unless `weft` forces it.
The adopter's frontmatter is pinned to the package's version for now; there is no migration tool.
Blocking: no.

## 5. `weft`'s functions and its provenance map

Settled by ws4, by the project owner.
Its owner names them; `init` does not guess.
Blocking: it blocks ws4.

## 6. Working across two repositories

Settled by ws2.
This repository consumes the engine through a submodule, as any adopter would through its lockfile.
To settle as ws2 meets them:

- CI checks out the submodule;
- a document here that cites the engine's code cites it at the submodule's pinned commit (the `pin:` field, until now unused);
- each `codifying/` fiche that explains the engine's inside moves to `docsys/docs/` with the check it explains, so the paired-change rule still pairs them inside one repository, and `docsys` is checked by `docsys` like any adopter.

Blocking: no.
