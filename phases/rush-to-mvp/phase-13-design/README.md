---
title: "Phase 13 — Design"
force: orient
intention: formative
view: diachronic
provenance: { type: project, id: phase-13-design }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
hash: sha256:d868f2f7faa887008e70f4743c5c5949ace811c987de3cf12ba3db0c6dd9cc77
---

The first phase of the rush to MVP: it bounded the era and planned its first delivery phase, and built nothing.
It ran from 2026-10-09 to 2026-10-10.

What it settled (detailed in [`plan.md`](plan.md)):

- **The era and its stopping rule** — [ADR-042](rush-to-mvp.md): two delivery phases, adoption and the agent kit, and an observable condition on `weft` that ends the era.
- **The adoption plan** — now [Phase 14's plan](../phase-14-adoption/plan.md): fix first what an agent will read and copy; extract the engine as a Python package, `docsys`, that adopters declare as a development dependency; `docsys init` and `docsys new`; legacy documents admitted through a baseline that only shrinks; install on `weft`.
- **The engine's repository** — [`Skl8em/docsys`](https://github.com/Skl8em/docsys), public, mounted here as a submodule.
- **Licensing by kind of artefact** — [ADR-043](licensing.md): GPL-3.0-or-later for code, AGPL-3.0-or-later for services, CC0-1.0 for what an adopter copies, CC BY-SA 4.0 for prose, mapped in `REUSE.toml`.
- **Three proposals** the delivery phases rest on, in `imagining/`: the [theory of the code](../../../imagining/theory-of-the-code.md), ruled (two documents, a constitutive lexicon, recommended and never required); [reader-first writing](../../../imagining/reader-first-writing.md), with its casebook; [one package per ecosystem bound to one API](../../../imagining/multi-ecosystem-distribution.md).

Records:

- [plan.md — the plan](plan.md)
- [ADR-042 — the rush to MVP](rush-to-mvp.md)
- [ADR-043 — licensing by kind of artefact](licensing.md)

Against the plan's definition of done:

- The adoption plan has no blocking open point left except those its own tasks settle.
- **The agent-kit plan was not written.**
  The project owner moved it to the agent-kit phase, which plans itself when it starts, once the package exists to generate the kit from.
- The proposals both plans depend on are ruled, except reader-first writing and the multi-ecosystem API, which the adoption plan assumes as stated.
- The gate is green.
