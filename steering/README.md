---
title: "Contributing to and maintaining this system — start here"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: steering }
axis: genre            # internal docs are shelved by genre, not by the product's scope axis
dominant-community: contributor
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This folder is the **`steering` function** — the project governing *itself*, not the product. The product (`../write/`, `../structure/`) teaches *users* to document their own projects; this folder is for the **contributors and deciders** who maintain and extend the system: its foundation, roadmap, architecture, contribution rules, changelog, and decision register. The frozen records each decision produces live under `../phases/`.

*(The root axis is `provenance`; `steering/` is one function on that shelf, not a tree of its own. This folder groups the governance genres — architecture, contribution rules, history, the register — for the `contributor` community.)*

## Route by need

- **How the repo is laid out and why** → [`ARCHITECTURE.md`](ARCHITECTURE.md) *(explain)*
- **How to contribute to the system** (the binding rules for changing it) → [`CONTRIBUTING.md`](CONTRIBUTING.md) *(mandate)*
- **What changed and when** → [`CHANGELOG.md`](CHANGELOG.md) *(account)*
- **Every decision, listed** (the register) → [`ADR.md`](ADR.md) *(decide — the act)*
- **Why each choice was made, and what it entails** → [`phases/`](../phases/README.md) — records grouped by the construction phase that produced them, each with its `justify` and `entail`.

## Why this is separate from the product

Keeping the project's own docs out of the product is the disentanglement recorded in [`ADR-010`](../phases/phase-04-disentanglement/ADR-010-product-vs-docs.md). It is also a live demonstration: two dominant communities in one repo, each with its own tree and axis — exactly what the theory predicts, and what the product's `../structure/applied.md` reads back.
