---
title: "The system lived — this repo, and a generic IT project"
force: explain
verb: illuminate
perlocution: model
view: synchronic
provenance: { type: function, id: structuring }
audience: [user]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

The best proof of the model is that this repository *is* an instance of it. This document reads our own tree as an example, then shows how a generic IT project would instantiate the same shape — so you can see the theory lived, not just described.

## This repository, read as an instance

The repo holds two things with **two dominant communities**, kept apart on purpose:

```text
# THE PRODUCT — for users (people documenting their own project). dominant: user
README.md              orient    onboarding   — the front door (declares axis: scope)
tutorial.md            teach      onboarding   — guided first-document on-ramp
write/                 …          writing      — how to write ONE document
  concepts.md          explain
  choosing.md          instruct · patterns.md recommend · rules.md mandate
  frontmatter.md       describe   — the catalogue schema
  forces/<door>/<force>/  README.md (explain, the stance) + template.md (instruct)
structure/             …          structuring  — how to keep the WHOLE corpus
  concepts.md          explain  · setup.md   instruct · defaults.md recommend · rules.md mandate
  audience.md          describe   — who the corpus serves
  applied.md           explain    — this file

# THE PROJECT'S OWN DOCS — for contributors/deciders maintaining the system. dominant: contributor
docs/                  …          steering (maintained) — declares its own axis: genre
  ARCHITECTURE.md      explain  · CONTRIBUTING.md mandate · CHANGELOG.md account
  ADR.md               decide     — the register (the act: one line per decision)
  phases/<phase>/      …          project: phase-NN (frozen) — records with justify + entail
```

What this demonstrates:

- **Content ≠ the project's own docs.** The product teaches *users* to document their projects (`dominant-community: user`); `docs/` documents *this repo* for *contributors* (`dominant-community: contributor`). Conflating them was the mistake earlier versions made.
- **Axis by scope.** The product cuts into *one document* (`write/`) vs *the whole corpus* (`structure/`). That is why the frontmatter schema (per-document) sits in `write/` and the audience model (who the corpus serves) sits in `structure/`. `docs/` does not inherit this axis — it is cut by genre, for its own community.
- **Provenance now means something.** Maintaining functions — `onboarding`, `writing`, `structuring`, `steering` — plus one bounded **project per construction phase** (`phase-01…05`) that owns the records it produced. "Show me everything `writing` owns" returns a real, distinct set.
- **Shelf ≠ provenance, visibly.** A decision record lives on the shelf at `docs/phases/<phase>/` and its provenance is that phase project; the maintained governance docs and the register are owned by `steering`. Reading place and producing activity diverge — the distinction the system preaches, shown rather than asserted.
- **Self-similarity.** Each area is documented by the forces it needs (explain / instruct / recommend / mandate / describe), and `docs/` records its own construction as frozen ADRs.

## A generic IT project, read as an instance

Take a service with a public API, maintained by a small team, audited yearly. Its **own** documentation (produced by *applying* our product) — note the audiences here are the project's, not ours:

```text
README.md              orient    [user, contributor] / H+M
docs/
  architecture.md      explain   [contributor] / H+M       — references ADRs
  reference/api.md     describe  [user, contributor] / H+M — RAG-indexed
  guides/deploy.md     instruct  [contributor] / H
  guidelines/style.md  recommend [contributor] / H+M
  tutorials/quickstart teach     [user] / H
  decisions/ADR-*.md   decide    [decider, contributor] / H+M — frozen, per project
  CHANGELOG.md         account   [user, contributor] / H+M
CONTRIBUTING.md        mandate   [contributor] / H+M
```

Provenance there: the maintained surface (`reference`, `architecture`) belongs to permanent **functions** (e.g. `api`, `reporting`); the ADRs and the yearly **audit dossier** (`prove`, `[decider]/H`, `retention: legal:7y`) are diachronic **project** records in `archive/`. If the service joins a cross-project docs repo, it is added under `projects/` as a **pinned submodule**, and a `functions/…` page references its exact state via the pin. Role sub-refinement: `user` → end-user / integrator, `contributor` → developer / reviewer / SRE, `decider` → tech lead / product owner / auditor.

## What the two instances share

Same twelve forces, same three doors, same seam between maintained state and frozen record, same two-axis audience. What differs is which cells are occupied and who the dominant community is. That is the model working: *not every cell is populated, and the empty ones are as informative as the full ones.*
