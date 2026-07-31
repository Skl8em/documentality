---
title: "Find the force of your document"
force: instruct
verb: walk-through
perlocution: none
view: synchronic
provenance: { type: function, id: writing }
audience: [user]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

Run this before writing anything. It takes a minute and it decides the structure, tone, and length of what you are about to write. If you skip it, you will write a `describe` where an `orient` was needed and wonder why the page does not work. The concepts behind each step are in [`concepts.md`](concepts.md).

## Steps

1. **Know or do?** Does the document convey *how things are* (savoir → the **know** door) or aim at *action* (savoir-faire → the **do** door)? If it instead sets a rule, makes a promise, opens a deliberation, or records a decision or evidence, it is the **govern & record** door. Pick the door, then the force within it (see the door's `README.md` in [`forces/`](forces/README.md)).

2. **Name the generative verb.** One word for what the document is *for* — often not the force name (a decision is written to *justify*). Hold it in mind; let it order everything. If the verb differs from the force only because of *who* you write toward, do not rename — set `distance`/`power` (step 4).

3. **Read the intention.** Is the document meant to *move* the reader above the floor (`locate` / `model` / `enable` / `convince`) or merely *serve* them at it (`state`)? If it moves the reader, organize by the reader's likely state — where they are, what confuses them — not by the subject's structure, and judge success by the reader's change, not by correctness.

4. **Fix the recipient.** Who is the audience (role: user / contributor / decider; see [`../structuring/audience.md`](../structuring/audience.md)), and what is the recipient relation? `distance` = how much code they share → sets the scaffolding. `power` = whether they can sanction you → sets the armor. Also set `reader: H | M | H+M`. Pay each cost where owed, nowhere else.

5. **Name the failure mode.** Every force fails by drifting into a neighbour (a reference that starts explaining; a mandate that softens into advice). Read it in the force's `README.md`, name it before you start, and watch for the drift as you write.

## Verify

You have found the force when you can fill this sentence without hedging:

> This document **<verb>s** for a **<role>** who **<shares / does not share>** my code and **<can / cannot>** sanction me; it **<changes / serves>** them, and it fails if it turns into **<neighbouring force>**.

If more than one force fits, you have two documents, or one document with a dominant force and the other subordinate inside it. Split, or pick the centre of gravity and demote the rest.

## Then

Open [`forces/<door>/<force>/`](forces/README.md): the `README.md` gives the move structure, the `template.md` a skeleton to fill. Apply [`patterns.md`](patterns.md) as you write, obey [`rules.md`](rules.md), tag with [`frontmatter.md`](frontmatter.md).
