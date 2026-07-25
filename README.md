---
title: "Project documentation system — start here"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: steering }
axis: provenance       # the source is the producer's shelf: one folder per function (theory/ write/ structure/ steering/ imagine/) + phases/
dominant-community: contributor
audience: [user, contributor]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This repository is a **system for writing, structuring, and keeping project documentation** — a product you read to learn how to document *your own* project. It is written according to its own rules, so its file tree is the first worked example of the theory. Every file declares its **force** in its frontmatter; this page is an `orient`, so its only job is to situate you and route you onward.

**New here?** 

You want to read if this approach would make sense to you>
Go to `structure/*to be defined*`
You start with your project and want to write the first documentation?
Go to [writing tutorial`](writing/tutorial.md)
You wand to sort your new or existing documentation and want to create a structure for it?
Start with the [Structure Tutorial](structure/tutorial.md).
Already have a document in mind but don't know where to start?
Go to ...

Come back here once you know what you need; this page routes by need, not as a course to read in order.

## The one idea

A document is not a container of information sorted by subject. It is an **act** performed from a definite position — *what* it does (its force) and *toward whom* (its audience, at some distance and power) — and made to live through time. Name the act correctly and the form follows; misname it and no polish recovers the wrong centre of gravity.

## What's in here — one folder per function

The source is the **producer's shelf**: each top-level folder is a standing **function** (a provenance), and the user-facing reading order is *generated* from the frontmatter rather than hand-kept as a folder.

- `theory/` — the inscribed-act theory the product rests on (the three essays + readability patterns).
- **[`write/`](write/README.md)** — how to write *one document*: its force, move structure, readability patterns, and the **frontmatter** schema; one folder per force, grouped by the three doors.
- **[`structure/`](structure/README.md)** — how to keep *the whole corpus*: topology, provenance, life cycle, the **audience model** ([`structure/audience.md`](structure/audience.md)), and the structuring tutorial.
- **[`steering/`](steering/README.md)** — the project's own governance: foundation, roadmap, architecture, contribution rules, changelog, and the decision register (ADRs).
- **[`imagine/`](imagine/README.md)** — what is only *intended* yet (Phase II), parked so it is neither lost nor mistaken for current work.
- **[`phases/`](phases/README.md)** — the frozen records of each construction phase (a `project` provenance), grouped by era.

Keeping the *product* (`write/`, `structure/`) legible to a **user** and the project's *own* governance (`steering/`, `phases/`) legible to a **contributor** is the theory working — but both are shelved the same way, by the function that maintains them; the two reading orders are generated, not two hand-kept trees.

## How this tree is organized

*(This is the axis-and-dominant-community declaration that `structure/rules.md` requires a tree root to carry — you are reading it, and it lives in the root README.)*

- **Axis: by provenance.** The source is shelved by the **function** that produces and maintains each area (`theory`, `writing`, `structuring`, `steering`, `imagine`), plus the bounded `project` records under `phases/`. Inside `write/forces/` the sub-axis is **by door** (know / do / govern-and-record).
- **Dominant community: `contributor`** — the shelf is ordered for whoever writes and maintains the docs, their first reader. The `user`'s reading order is *generated* from the frontmatter, not carved into this tree.

## The three doors (how the forces group)

- **[know](write/forces/know/README.md)** (savoir) — `orient`, `explain`, `describe`. Understand where you are, why, and the facts.
- **[do](write/forces/do/README.md)** (savoir-faire) — `instruct`, `teach`, `recommend`. Execute, learn, or take advice — a deontic gradient: *here is how* → *you should* → *you must* (that last is `mandate`, next door).
- **[govern & record](write/forces/govern-and-record/README.md)** — `mandate`, `commit`, `propose`, `decide`, and the evidence/memory forces `prove`, `account`. A project's own acts: rules, promises, deliberation, decisions, proof, history.

## The rule that governs everything else

A corpus serves two incompatible masters: **be found and read now** (communication) and **stand as evidence over time** (archive). No single order serves both. This system keeps them apart — the readable tree on one side, frozen provenance on the other — and stitches them at one point: *the frozen record of a change becomes the current state you maintain*. `structure/concepts.md` develops it.

## Status

**v3.1** — the product (content, for users) is disentangled from `docs/` (the repo's own internals, for contributors); provenance now names the maintaining function (`writing`, `structuring`, `onboarding`, `maintenance`) instead of a blanket id. The frame and one exemplar force per door are built (`orient`, `instruct`, `decide`); the remaining nine forces are being migrated from `_legacy/`.
