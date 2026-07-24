---
title: "Structure your project's documentation — a guided start"
force: teach
verb: bring-along
register: do
intention: formative
view: synchronic
provenance: { type: function, id: structuring }
distance: far
audience: [user]
reader: H
status: draft
note: "New (Ferraris-grounded) vocabulary; the frontmatter schema is reconciled in Phase 09."
---

This is a guided first run, not a reference.
By the end you will have a documentation structure that fits *your* project — derived from what your project actually is, not a template dropped on top — and that can grow and be regrouped later without a rebuild.
We do not start by choosing folders.
We start by naming what people *do* with the project, and let the structure fall out of that.
Keep a scratch file open: you will make a few real notes about a project of your own as we go.

## Step 1 — Name the activities your project takes part in

This is the step that decides all the others, and it is the one almost no project does out loud.
What a project is *for* — the things people actually do with it and to it — usually stays tacit, assumed, never written.
So this step asks a real mental effort: to make explicit what you have only ever felt.
It repays the effort more than any other, because everything downstream — who reads, what they need, where it goes — is derived from this list.

A **function** is a recurring *activity* someone carries out in relation to your project.
Not a topic, not a technology — an activity: a verb, with a purpose and a doer, that happens again and again.
The test is simple: if you can say "*someone* wants to **⟨verb⟩** ⟨the project or a part of it⟩, repeatedly," it is a function.
"Python", "the database", "biology" are **not** functions — they are bodies of knowledge that some activity *draws on*; the function is "extend the parser", "operate the database", "validate the assay".

Because these are easy to under-see, here is a wide net — most projects have several of these, and usually more than first come to mind:

- **use** it — run it, call it, query it, read its output, get an answer from it;
- **make it available** — publish, package, release, host, distribute it;
- **install, deploy, operate** it — set it up, run it in an environment, keep it running;
- **integrate** it — call it from other software, embed it, wire it into a pipeline;
- **extend or contribute** to it — add a feature, write a plugin, change its internals;
- **maintain** it — fix bugs, upgrade dependencies, keep it alive over time;
- **audit, review, verify** it — check its correctness, security, licence, compliance;
- **learn or teach** it — onboard a newcomer, train a team, explain it;
- **decide or steer** it — set direction, choose between options, own its conventions;
- **adopt, fund, or evaluate** it — bet on it, pay for it, weigh it against an alternative.

Now write *your* list.
Go past the obvious three; the ones you almost forgot are usually where documentation is most missing.
Beside each activity, note the **body of knowledge** it draws on — the field someone would need to be at home in to do it.
That pairing — activity, and the knowledge it mobilizes — is the spine of everything that follows.

## Step 2 — Derive who performs each activity, and what they already know

Now, and only now, the people — and you read them *off* the list, you do not invent them.
Each activity is performed by someone, and the same project meets different people through different activities.
Whoever *uses* it may know its domain deeply and nothing of its internals; whoever *installs* it may know the tooling and nothing of why the first person wants it; whoever *extends* it needs the design and the past decisions.
These are different audiences, set by the activity they meet the project through, not by one label.
For each activity, name the person (a role, not a name) and the knowledge they bring.

Then judge the **distance** for each: is that person *initiated* in the activity's field, sharing its vocabulary, or *novice*, needing its concepts spelled out?
Distance is per activity and per field: a reader can be initiated in your Python and a novice in your statistics.
And your project need not teach a whole field from scratch — it may reasonably address the *initiated* of a domain, if that is who meets it there.

## Step 3 — Derive what each person needs

For each activity × person, ask the plain question: do they need to **know** something, **do** something, or see a **decision**?
Let the need pick the document, rather than reaching for a fixed list.
Consider the most ordinary case, yourself returning to a personal project after three months.
Your first need is not a how-to; it is an **orient** — what was I doing, where did I stop, what comes next.
Then the **why** — the design, the old decisions, the vision and where you are against it.
The how-tos come *last*, for the first outsider or for the step you always re-forget.
Someone arriving only to install it wants the opposite order: the how-to first.
Write, next to each activity × person, the one or two things they most need — and in what order they need them.

## Step 4 — Start with everything together, then split along the seams

Open one README and, for now, let it hold whatever your project needs said.
A single file is a complete documentation system; do not scatter before there is anything to scatter.
Split a piece out only when a real seam appears:

- when one document has grown too big to hold at once;
- when two things inside it have **divergent lives** — a decision that should freeze versus a reference you keep editing;
- when a distinct community needs a piece on its own.

Cut only along those seams, and only when they actually bite.
Most small projects never need more than a README, a how-to or two, an explanation of the design, and a short log of decisions.

## Step 5 — Now, and only now, where things go

This is where the folder question belongs — and it has a rule.
A document lives in the source by its **provenance**: the activity that produces and maintains it — one of the activities you named in Step 1.
That same provenance tells you its life: a *permanent* activity (using, operating, maintaining) keeps its docs **current**; a *bounded* effort (a migration, a redesign) **freezes** its records when it ends.
So "where do I put it?" is answered by "which activity does it belong to, and does that activity ever end?" — not by a folder chosen in advance.
The reader's *browsing* order is a separate thing: it follows the activities and needs of Steps 1–3, and on a real project it can be **generated** from the files rather than dictating the folders.
While you are your own only reader, the folder is also the view — so keep it clean for *you*, the maintainer, and let a reader's view be generated later if one is ever needed.
Root versus a `docs/` subfolder, then, is a consequence: your project's own surface (its README, its how-tos) sits where its users meet it, while its internal records (decisions, history) sit apart, because they belong to a different activity and a different reader.

## What you have, and that it can change

You now have a structure that came *out of* your project: its activities named, the people each one meets, what they need and in what order, each document with one home decided by its provenance, and a sense of what stays current versus what freezes.
None of it is fixed.
As you understand the project better you will **regroup** — merge activities that turned out to be one, split one that hid two, and roll many small records up into a few coarse eras so the map stays readable.
Coarse and honest beats fine and overwhelming.

To write any single document well, use the writing on-ramp, [`../tutorial.md`](../tutorial.md), and the force templates in [`../write/forces/`](../write/forces/README.md).
To go deeper — several projects under one docs repo, or the metadata that lets a machine read your corpus — read [`concepts.md`](concepts.md) and [`setup.md`](setup.md).
