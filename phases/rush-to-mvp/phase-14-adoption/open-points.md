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
Costs accepted with it: links from frozen phase records into `scripts/` and `schema/` stop resolving, and the link check allows each, with its reason, in `docsys.yaml`'s `links.allow`, which `links/allowance` keeps from outliving its reasons; the schema, authored with the engine, is explained by `writing/frontmatter.md` across the repository boundary.
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

Settled by ws2, and by the project owner on 2026-10-22 for citations ([Rulings](rulings.md#citing-across-the-two-repositories)), but for the engine checking itself, which ws4 does.
This repository consumes the engine through a submodule, as any adopter would through its lockfile:

- CI checks out the submodule, at the commit its pointer names;
- each fiche on the engine's inside is in `docsys/docs/`, beside the check it explains, so the paired-change rule pairs them inside the engine's repository;
- a page that states the present links into the engine by a relative path into `docsys/`: it reads the engine this repository runs, and the link check fails when a move of the pointer breaks the link, where a link to the engine's `main` would read another engine, ahead of or behind the pointer, and break unseen, since the link check does not read web links;
- a record cites a file of either repository by a URL at a commit already on that repository's remote, and a record that cites one state of the engine names it in `pin:`; a phase's pages become records when it closes, so their relative links into `docsys/` become commit URLs then.

The binding rule is in [`CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md).
Cost accepted with it: GitHub's web view may not follow a relative link into a submodule; the reader of record is a checkout.
Left to ws4: the engine's links to this repository, which point at its `main`, since the engine holds no copy of it.
Blocking: no.
