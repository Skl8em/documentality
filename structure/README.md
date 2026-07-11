---
title: "Structure & keep — start here"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: doc-system }
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This folder answers **where documents live, how they are organized, how long they are kept, and how they are exported**. Like `write/`, it is split by force so each concern is its own file.

## Route by what you need

- **Understand the model** (two systems, provenance, the state/change seam, the life cycle) → [`concepts.md`](concepts.md) *(explain)*
- **Lay down the tree and topology** for a new project or a docs repo → [`setup.md`](setup.md) *(instruct)*
- **The recommended defaults** (tree axis, retention) → [`defaults.md`](defaults.md) *(recommend)*
- **The binding structural rules** → [`rules.md`](rules.md) *(mandate)*
- **See it lived** — how this repo applies it, and how a generic IT project would → [`applied.md`](applied.md) *(explain)*
- **Who the docs are for** (the audience model — roles × reader — that both activities reference) → [`audience.md`](audience.md) *(describe)*. It lives here because choosing who the tree serves is a structural decision.
- The metadata that makes the tree navigable is a `write/` concern (you fill it while writing): [`../write/frontmatter.md`](../write/frontmatter.md).

> These are **entry points routed by need, not a reading order.** `rules.md` (mandate) is binding even though it sits in the list like the rest: its rules are surfaced in [`setup.md`](setup.md) and enforced by `../write/frontmatter.md` validation, so you meet them whether or not you read this list top to bottom.

## The one distinction

A corpus serves two masters that no single order satisfies: a **present reader** who must *find* things now (communication → a readable tree), and a **future examiner** who must *trust* things later (archive → provenance). Keep them apart, and stitch them at one seam — the frozen record of a change becomes the maintained statement of a state. `concepts.md` is the whole of it.
