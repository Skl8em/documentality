---
title: "Project documentation system — start here"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: doc-system }
axis: activity            # primary shelf axis (sub-axis in forces/: by door)
dominant-community: contributor
audience: [user, contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This repository is a **system for writing, structuring, and keeping project documentation** — and it is written according to its own rules, so its file tree is the first worked example of the theory. Every file declares its **force** in its frontmatter; this page is an `orient`, so its only job is to situate you and route you onward.

**New here?** Start with the guided [`tutorial.md`](tutorial.md) — you'll write your first real document in about ten minutes and meet the pieces in context. Come back to this page once you know what you need; it routes by need, not as a course to read in order.

## The one idea

A document is not a container of information sorted by subject. It is an **act** performed from a definite position — *what* it does (its force) and *toward whom* (its audience, at some distance and power) — and made to live through time. Name the act correctly and the form follows; misname it and no polish recovers the wrong centre of gravity.

## Two activities, one shape

There are only two things you ever do here, so there are two top-level folders — and each is itself documented by the forces it needs (an `explain` of the concepts, an `instruct` for the procedure, a `recommend` for the defaults, a `mandate` for the rules). The system is **self-similar**: the same twelve forces organize the guidance about the forces.

- **[`write/`](write/README.md)** — how to write one document: find its force, follow the move structure, apply the readability patterns. Holds the **frontmatter** schema (you need it *while* writing) and one folder per force under the three doors.
- **[`structure/`](structure/README.md)** — where documents live, how the tree is organized, how long they are kept, how the whole thing is exported, and the **audience model** ([`structure/audience.md`](structure/audience.md), generic roles × reader kind) that both activities reference — because who the tree serves is a structural decision.

## How this tree is organized

*(This section is the axis-and-dominant-community declaration that `structure/rules.md` requires every tree to carry at its root — you are reading it. It always lives in the root README, so that is where to look for any project.)*

- **Axis: by activity.** The top level splits into `write/` and `structure/` — the two things you ever do here — and inside `write/forces/` the sub-axis is **by door** (know / do / govern-and-record).
- **Dominant community: `contributor`** (someone using the system to author docs), with `decider` (convention owner) second. `user` meets the system only through the projects that adopt it, so the shelf is ordered for authors, not end-readers.

## The three doors (how a newcomer navigates)

The forces group into three doors, and `write/forces/` is split along them:

- **[know](write/forces/know/README.md)** (savoir) — `orient`, `explain`, `describe`. Understand where you are, why, and the facts.
- **[do](write/forces/do/README.md)** (savoir-faire) — `instruct`, `teach`, `recommend`. Execute, learn, or take advice. Read as a deontic gradient: *here is how* → *you should* → *you must* (that last one is `mandate`, next door).
- **[govern & record](write/forces/govern-and-record/README.md)** — `mandate`, `commit`, `propose`, `decide`, and the evidence/memory forces `prove`, `account`. The project's own acts: rules, promises, deliberation, decisions, proof, history.

## The rule that governs everything else

A corpus serves two incompatible masters: **be found and read now** (communication) and **stand as evidence over time** (archive). No single order serves both. This system keeps them apart — the readable tree on one side, frozen provenance on the other — and stitches them at one point: *the frozen record of a change becomes the current state you maintain*. `structure/concepts.md` develops it.

## Status

This is **v3**, a reorganization into the self-similar shape above. The frame and one exemplar force per door are built (`orient`, `instruct`, `decide`); the remaining nine forces are still being migrated from `_legacy/` (the previous flat version, kept as source until migration completes).
