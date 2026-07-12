---
title: "Project documentation system — start here"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: onboarding }
axis: scope            # the product's shelf axis: write/ = one document · structure/ = the whole corpus
dominant-community: user
audience: [user, contributor]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This repository is a **system for writing, structuring, and keeping project documentation** — a product you read to learn how to document *your own* project. It is written according to its own rules, so its file tree is the first worked example of the theory. Every file declares its **force** in its frontmatter; this page is an `orient`, so its only job is to situate you and route you onward.

**New here?** Start with the guided [`tutorial.md`](tutorial.md) — you'll write your first real document in about ten minutes and meet the pieces in context. Come back here once you know what you need; this page routes by need, not as a course to read in order.

## The one idea

A document is not a container of information sorted by subject. It is an **act** performed from a definite position — *what* it does (its force) and *toward whom* (its audience, at some distance and power) — and made to live through time. Name the act correctly and the form follows; misname it and no polish recovers the wrong centre of gravity.

## What's in here — the product, and the project's own docs

Two things live side by side, and keeping them apart is itself the theory working (two sub-trees, two dominant communities):

- **The product** — for **you, the user**, documenting your own project:
  - **[`write/`](write/README.md)** — how to write *one document*: find its force, follow the move structure, apply the readability patterns. Holds the **frontmatter** schema (you fill it while writing) and one folder per force, grouped by the three doors.
  - **[`structure/`](structure/README.md)** — how to keep *the whole corpus*: topology, provenance, life cycle, export, and the **audience model** ([`structure/audience.md`](structure/audience.md)) both halves reference.
- **[`docs/`](docs/README.md)** — the documentation of *this repository itself*, for **contributors and deciders** who maintain and extend the system: its architecture, contribution rules, changelog, and the decision records (ADRs) behind every design choice. Different readers, different dominant community — so it is a tree of its own.

## How this tree is organized

*(This section is the axis-and-dominant-community declaration that `structure/rules.md` requires every tree to carry at its root — you are reading it. It always lives in the root README, so that is where to look for any project. `docs/` is a nested tree and carries its own declaration.)*

- **Axis: by scope.** The product splits into `write/` (everything about producing *one document*) and `structure/` (everything about the *whole corpus*). Inside `write/forces/` the sub-axis is **by door** (know / do / govern-and-record).
- **Dominant community: `user`** — someone using the system to document their own project. The product's shelf is ordered for them. Contributors and deciders who maintain the system itself are served by `docs/`, whose dominant community is `contributor`.

## The three doors (how the forces group)

- **[know](write/forces/know/README.md)** (savoir) — `orient`, `explain`, `describe`. Understand where you are, why, and the facts.
- **[do](write/forces/do/README.md)** (savoir-faire) — `instruct`, `teach`, `recommend`. Execute, learn, or take advice — a deontic gradient: *here is how* → *you should* → *you must* (that last is `mandate`, next door).
- **[govern & record](write/forces/govern-and-record/README.md)** — `mandate`, `commit`, `propose`, `decide`, and the evidence/memory forces `prove`, `account`. A project's own acts: rules, promises, deliberation, decisions, proof, history.

## The rule that governs everything else

A corpus serves two incompatible masters: **be found and read now** (communication) and **stand as evidence over time** (archive). No single order serves both. This system keeps them apart — the readable tree on one side, frozen provenance on the other — and stitches them at one point: *the frozen record of a change becomes the current state you maintain*. `structure/concepts.md` develops it.

## Status

**v3.1** — the product (content, for users) is disentangled from `docs/` (the repo's own internals, for contributors); provenance now names the maintaining function (`writing`, `structuring`, `onboarding`, `maintenance`) instead of a blanket id. The frame and one exemplar force per door are built (`orient`, `instruct`, `decide`); the remaining nine forces are being migrated from `_legacy/`.
