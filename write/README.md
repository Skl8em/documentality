---
title: "Write a document — start here"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: doc-system }
audience: [contributor]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This folder answers **how to write one document well**. It is split by force, so each concern is a separate file — which is itself the system eating its own dog food: an `explain` for the theory, an `instruct` for the procedure, a `recommend` for the defaults, a `mandate` for the rules, a `describe` for the metadata.

## Route by what you need

- **Understand the model** (force, perlocution, verb, the three doors) → [`concepts.md`](concepts.md) *(explain)*
- **Find the force of the document in front of you** → [`choosing.md`](choosing.md) *(instruct)* — five questions.
- **Make the prose readable to humans and LLMs** → [`patterns.md`](patterns.md) *(recommend)*
- **The binding rules you must not break** → [`rules.md`](rules.md) *(mandate)*
- **Tag the file for the machine** → [`frontmatter.md`](frontmatter.md) *(describe)* — the catalogue schema, including `audience`/`reader`.
- **Write a specific genre** → pick the force's folder in [`forces/`](forces/README.md): its `README.md` is the stance, its `template.md` a ready skeleton.

> These are **entry points routed by need, not a reading order.** `rules.md` (mandate) is binding even though it sits in the list like the rest: its rules are surfaced in the `template.md` you actually fill and enforced by [`frontmatter.md`](frontmatter.md) validation, so you meet them whether or not you read this list top to bottom. If you are new and don't yet know your need, start with the root [`../tutorial.md`](../tutorial.md).

## The one move

Before writing anything, say in one word what the document is *for* — its force — and mean the right word. Everything else (structure, tone, length, how much to explain, how defensible to be) follows from that word plus who you write toward. `choosing.md` walks you through finding it; `concepts.md` explains why it works.
