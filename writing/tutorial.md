---
title: "Getting started — write your first document with the system"
force: teach
verb: bring-along
perlocution: enable
view: synchronic
provenance: { type: function, id: onboarding }
audience: [user]
reader: H
distance: far
power: none
status: stable
written-at: v3
valid-for: v3
---

This is a guided first run, not a reference.
In about ten minutes you will produce two real documents and, along the way, meet the pieces of the system in the order you actually need them.
Don't read the theory first — do this, and the theory will make sense afterwards.
You only need a text editor and one small real thing to document (a script, a repo, a folder you own).

## Step 1 — Pick the smallest real thing you owe a doc

Choose something concrete you could describe in three sentences: a repo without a README, a script nobody else can run, a folder whose purpose is unclear.
Small and real beats big and hypothetical.
Write its name on a scratch line.
That's your subject for the whole tutorial.

## Step 2 — Give it a front door (your first `orient`)

Almost every first document is an **orient** — it situates a newcomer.
You don't need to know the theory to write one; just answer four questions.

1. Open [`writing/forces/know/orient/template.md`](forces/know/orient/template.md) and copy it to `README.md` next to your subject.
2. Fill the four blanks: *what is this* (one line), *where you are*, *why it concerns you*, *where to go next*. Resist adding install steps or architecture — an orient hands off, it doesn't hold.

Done?
You now have a working front door.
That is a real, useful document — notice it took minutes because the template already knew its shape.

## Step 3 — Tag it so the system can see it

At the top of your `README.md`, the template left a frontmatter block.
Set five things (the rest are optional):

```yaml
force: orient
perlocution: locate
view: synchronic
provenance: { type: project, id: <your-subject> }
audience: [user, contributor]
reader: H+M
status: draft
```

You just used the catalogue. You don't need to understand every field yet — [`writing/frontmatter.md`](frontmatter.md) explains them when you're curious.

## Step 4 — Record one decision (meet a frozen record)

Think of one choice you made about your subject ("I used SQLite, not Postgres, because…"). Write it down as a **decide** document — a different door entirely, and one that *freezes*.

1. Copy [`writing/forces/govern-and-record/decide/template.md`](forces/govern-and-record/decide/template.md) to `decisions/ADR-001.md`.
2. Fill context → options you considered → the decision → consequences you accept. Write the *why* for someone who disagrees; that reasoning is the whole point.

Notice the difference you just felt: the orient was maintained and reader-facing; the ADR is dated, frozen, and written for the future. That contrast — maintained *state* vs frozen *record* — is the spine of the whole system.

## Step 5 — Stand back

In ten minutes you have: a maintained `orient` (the **know** door) and a frozen `decide` (the **govern & record** door), both tagged for the catalogue. You have touched two of the three doors, two templates, and the frontmatter — the machinery the rest of the docs merely explain.

## Where to go now

- The *why* behind what you just did → [`writing/concepts.md`](concepts.md).
- Writing a different kind of document → find its force via [`writing/choosing.md`](choosing.md), then its folder in [`writing/forces/`](forces/README.md).
- Where these files should actually live, and for how long → [`structuring/README.md`](../structuring/README.md).
- Who you're writing for → [`structuring/audience.md`](../structuring/audience.md).

You are no longer new. From here, [the root `README.md`](../README.md) routes by need — use it as a menu, not a course.
