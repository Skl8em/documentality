---
title: "Structure your project's documentation — a guided start"
force: teach
verb: bring-along
intention: formative
view: synchronic
provenance: { type: function, id: structuring }
constitutive: no
distance: far
audience: [user]
reader: H
status: draft
note: "Ferraris-grounded vocabulary; relevance-based functions, fractal method, organized for the author. The frontmatter schema and the generated reader surface are their own (planned) tutorial; this one stops at the source."
---

This is a guided first run, not a reference.
By the end you will have a documentation structure that came *out of* your project — derived from what your project actually is, not a template dropped on top — and that can grow and be regrouped later without a rebuild.
We do not start by choosing folders.
We start by naming what people *do* with the project, and let the structure fall out of that.
Keep a scratch file open: you will make real notes about a project of your own as we go.
Throughout, we will also carry one small worked example — `prep`, an internal command-line tool a few teammates use to prepare data files — so that every abstract move has a concrete one beside it.

Three things to hold before we start, because they change how you should read everything below.

*This is not deterministic, and that is fine.* Two people who run this on the same project will produce different structures, and neither has to be wrong.
We are not handing you a map with your answer on it; we are handing you a light to find your own path.
Several times you will reach a fork the text does not draw — and when you do, you have our explicit permission to take it, using the same logic one level down.
The reasoning extends; the examples do not exhaust it.

*You are organizing for the author first — for yourself.* The source tree you build here is organized for the person who *writes and maintains* the documents, who is also their first reader: you.
It is not, yet, organized for outside readers.
When and if outside readers arrive, you expose to them a *generated* view that follows their reading order, not your filing order — and that generation is a separate tutorial (see the end).
So whenever you are unsure "who is this for," answer *the author*, and keep the tree clean for the person holding the pen.

*Assume you will be incomplete, and make the holes visible.* You cannot document everything, and documentation is usually where a project is thinnest.
The goal of this run is not a full corpus; it is a structure in which you can *see* what is missing.
A named gap is a success, not a failure — it is the difference between a hole you chose and a hole you never noticed.

One method runs through all five steps: it is **fractal**.
The same few partitions apply at every scale — the whole project, a folder, a single document.
Start coarse, keep any list you make to roughly **three to seven items**, and refine a level only when a real need makes the coarse version hurt.
If you find yourself with more than about seven of anything, you are already too fine — group them into a smaller number of broader things, and keep the fine ones for a later pass.

A last orientation before Step 1: how much is already **written**?
This is a question about your documents, not your code — a project can have no code at all and still have a great deal written, and it is that written material you are structuring here.

- *Greenfield* — little or nothing is written yet.
  Run the steps **forward**, as a generator.
- *Existing* — you already have documents, or one large document with its own internal sections, or a project someone already split into parts.
  Run the same steps **backward**, as an audit: name what the structure *implies*, then check it against what follows.

The two often mix: a project with no code but one big design document is *greenfield in code and existing in prose* — so generate its activities forward, and audit that document backward, both at once.
Most projects that come looking for a structuring tutorial already have something written, so we treat the existing case as first-class, not an afterthought.

## Step 1 — Name the activities that matter around your project

This is the step that decides all the others, and it is the one almost no project does out loud.
What a project is *for* — the things people do with it and to it — usually stays tacit, assumed, never written.
So this step asks a real mental effort: to make explicit what you have only ever felt.

A **function** is an *activity of relevance* that someone carries out in relation to your project.
Not a topic, not a technology — an activity: a verb, with a doer, that is worth thinking and talking about.
What makes an activity relevant is not how often it happens but how much it matters — that it is *important enough to warrant thinking and talking about it*.

Recurrence is only one sign of that importance, and leaning on it alone will make you miss the activities that matter most.

- Some activities recur: a user runs `prep` again and again — clearly a function.
- Some happen once *per person* but for many people: adopting the tool is done once by each team that picks it up, yet making that first hour go well is exactly what decides whether they stay.
- Some happen once, ever, and are still the point: a data analysis for a scientific paper is run once, but it is the most important activity of its project — and the claim that it is *reproducible* needs documentation that makes it true whether or not anyone ever reproduces it.
- Some you hope never happen at all: a disaster-recovery or rollback procedure is defensive, documented for a worst case everyone hopes never comes.

So write down the activities that matter, whatever their cadence.

Include, on purpose, the ones you have not done yet.
There is an activity almost every project forgets because it points at the future rather than the past: **imagine**.
Dream about what could be done with the project, what could be extended from it, how it might be used — starting from what is here now.
Name those intended activities in the same list, mark them as intended, and give them a home to be pulled out of the moment the work actually starts.
This is where a stated roadmap, a planned capability, a "Phase II" lives: not nowhere, but under `imagine`, honestly labelled as not-yet-enacted.

Because these are easy to under-see, here is a wide net — but read it as a **hierarchy**, not a flat checklist.
Start from the handful of coarse meta-activities in **bold**; only open one into its finer verbs if your project genuinely needs the distinction.

- **use** it — run it, call it, query it, read its output, integrate it into other software;
- **provide** it — publish, package, release, host, distribute; install, deploy, operate it in an environment;
- **build** it — extend or contribute, add a feature or a plugin, fix bugs, upgrade dependencies, keep it alive;
- **govern** it — decide and steer, set conventions; audit, review, verify correctness, security, licence, compliance;
- **learn or teach** it — onboard a newcomer, train a team, explain it;
- **imagine** it — design, plan, and dream what is not built yet.

For `prep`, the honest coarse list is: *use* (teammates run it), *provide* (it installs from the internal registry), *build* (mostly you, occasionally a colleague), *govern* (you set its conventions and once made a config-format decision that stuck), *imagine* (a plugin API you keep meaning to add) — and one activity that hides under *use* but matters far more than daily use: the *year-end consolidation run*, done once a year, that absolutely must be right.

Now write *your* list, and use the fractal rule to know when to stop.

- Start with the coarse meta-activities, not the fine verbs.
- Stop when you cannot name an activity that is not already covered by something on the list.
- If you pass about seven, you are too fine — group some back into a broader activity, and keep an `orient` note at the top that points down into them (a `README.md` or `index.md` whose whole job is to orient someone around that level).
- You will forget one eventually; think hard, but do not overexert — a gap you find next month is cheap to add.

Beside each activity, note the **body of knowledge** it draws on — the field someone must be at home in to do it.
"Python", "the database", "biology" are not functions; they are knowledge that an activity *mobilizes* — the function is "extend the parser", "operate the database", "validate the assay".
That pairing — activity, and the knowledge it mobilizes — is the spine of everything that follows.

And mark, explicitly, the activities you are *not* going to document this pass.
Writing "adopt — not covered yet" is doing this step correctly; it turns an invisible hole into a visible one.

## Step 2 — Read off who you expect to perform each, and their distance

Now, and only now, the people — and you read them *off* the list, you do not invent them.
Each activity is performed by someone, or by many, and the same project meets different people through different activities.
Whoever *uses* it may know its domain and nothing of its internals; whoever *provides* it may know the tooling and not why the first person wants it; whoever *builds* it needs the design and the past decisions.
One activity can even carry two very different doers: a user who must install it himself because no one will do it for him, and an IT specialist tasked to install it for a customer — so ask whether they need the same document or entirely different ones.
Usually you have a *primary* audience: you write for them, and the others live with it.
It costs little to show you know the others are there — a line or two in their direction where it matters most — and now and then a document has to be rewritten wholesale for one of them (an INSTALL in the customer's own language, for their IT).
For now, just be clear about what you think you will need, and keep it small.

Watch the very common case where one physical person performs every activity, wearing different hats on different days.
The fractal rule applies here too: ask only for the *minimal* granularity that earns its keep.
If you are the sole doer and the sole reader, you do not need three personas — and you certainly do not need this tutorial's full ceremony for a project only you will ever touch.
But if imagining yourself in three roles helps you keep the activities distinct, do it.
And if your only community really is *you*, say so **explicitly** — because that sentence is also a note to your future self about the work waiting the day a second person arrives.

Name, for each activity, the person as a **role** (not a name) and the knowledge they bring.

Then judge the **distance** — and distance is not only, or even mainly, how much someone knows.
It is the gap between the **habitus** of the people who write the repo and the habitus of the intended reader: their shared or unshared vocabulary, yes, but also their social codes, and the register and style each takes for granted.
You write differently for your future self, for the colleague you have paired with for ten years, and for an unknown user who just found your package on PyPI — even when all three *know* the same amount.
Domains carry their own nomenclature, their own conventions and expectations of style: a bank, a research lab, and a start-up read and write differently, and a document that ignores that reads as foreign no matter how correct it is.
So distance is measured between two habitus — the authors' and the intended reader's — across both what they know and the codes they share.
It is per activity and per field: a reader can be close to you in your Python and far in your statistics, close in code and far in the register of a regulated industry.
And your project need not close every distance; it may reasonably address the *initiated* of a domain, in that domain's own register, if that is who meets it there.

Two honest qualifications, because they will matter later without needing to slow you down now.
You almost never know who will *actually* read; you know who you *intend* to write for — so read "audience" as **intended audience** throughout, a design target, not an observation.
And your own future self is always in that intended audience: three months away from this project, you will be a returning novice to it, and writing for that person is rarely wasted.
(Distance and power are as rich as any human relationship, not really a binary, and the gap between the audience you intend and the one you observe deserves its own flag — but both are refinements for later, not for this first run.)

## Step 3 — Read off what each person needs: know, do, govern

For each activity × person, ask the plain question: do they need to **know** something, **do** something, or **govern** something?

- **know** — understand, compare, weigh the evidence, see why: an orientation, an explanation, a rationale.
- **do** — perform an action, follow a procedure: a how-to, a tutorial, a runbook.
- **govern** — set direction, record what freezes, account for what happened: a decision, a policy, an open question, a post-mortem.

You are *drawing the boxes here, not yet filing documents into them* — so if a need seems to sit between two boxes, do not force it; the tension resolves at placement in Step 5, where provenance — who authors and maintains the document — decides.
"Diagnosing a failed run" is the classic in-between: a guide on *how to* diagnose is plainly `do`; the *record* of a particular past diagnosis is `govern`, with a time-stamped provenance (the incident that produced it).
It only feels stuck because you are trying to file it before you have finished shaping the boxes.

Order matters as much as kind.
Consider the most ordinary case, yourself returning to a personal project after three months: your first need is not a how-to, it is an **orient** — what was I doing, where did I stop, what comes next — then the **why**, and the how-tos come *last*, for the first outsider or the step you always re-forget.
Someone arriving only to install it wants the opposite order: the how-to first.
Those are two orderings out of many; for an integrator, an auditor, or a prospective adopter you will have to derive the order yourself rather than copy either one.
Write, next to each activity × person, the one or two things they most need — and in what order.

## Step 4 — Start together, then split only at real seams

If you are **greenfield**, open one README and let it hold whatever your project needs said.
A single file is a complete documentation system; do not scatter before there is anything to scatter.

If you already have an **existing** pile or an inherited split, do the mirror image: take the split you already have and run the seam tests over it *backward*, as an audit — keep each division a real seam justifies, and merge back the ones that only exist by habit.

Either way, a piece earns its own document only when a real **seam** appears:

- when one document has grown too big to hold at once;
- when two things inside it have **divergent lives** — a decision that should freeze versus a reference you keep editing;
- when a distinct community needs a piece on its own.

None of these come with an exact threshold, and that is deliberate — the judgment is yours.
For "too big", borrow the working-memory heuristic (roughly three to seven sections before a document stops being holdable) and the surface-craft advice in [`../theorising/patterns-ecriture-documentation.md`](../theorising/patterns-ecriture-documentation.md).
When a split you are looking at fails all three tests, prefer merging it back: precedent is not a seam.

Two artifacts deserve to be named here rather than left for you to reinvent.

The place where **decisions that freeze** go is a *decision record* — an ADR (Architecture Decision Record) or an equivalent decision log: one dated, append-only entry per decision, each frozen the moment it is made even though the log as a whole keeps growing.
If you do not already have the pattern in your fingers, the `decide` stance gives you the format — see [`../writing/forces/govern-and-record/decide/README.md`](../writing/forces/govern-and-record/decide/README.md).
For `prep`, the config-format decision is exactly this: one frozen record, not a paragraph you keep editing.

**Generated, ephemeral artifacts** — `prep`'s per-run log, a coverage report, an export — are a *third category*, not authored documentation at all.
They are data produced by running the tool, not documents written by a person, so they do not belong to the current/frozen distinction below.
Here you document *how to read* them and where they land; you do not file the artifacts themselves into your documentation tree.
(Where and how to *generate* them well is a real question the theory can address — but as a separate use-case, not in this first structuring run.)

Most small projects never need more than a README, a how-to or two, an explanation of the design, and a short decision log.

## Step 5 — Where things go: provenance, and the fractal folder rule

Now the folder question, and it has a rule.
A document lives in the source by its **provenance**: the activity that produces and maintains it — one of the activities you named in Step 1.
That same provenance tells you its life: a *permanent* activity (using, operating, maintaining) keeps its docs **current**; a *bounded* effort (a migration, a redesign) **freezes** its records when it ends.
So "where do I put it?" is answered by "which activity does it belong to, and does that activity ever end?" — not by a folder chosen in advance.
(Hold this current/frozen split lightly: it is a working device we are pushing on until it either proves itself or breaks — treat it as useful scaffolding, not settled law.)

Provenance comes in two kinds, and so far we have leaned on one.
A *synchronic* provenance is a standing **function** — use, build, govern — and its documents stay **current**.
A *diachronic* provenance is a **bounded producer with a lifespan** — a phase, a migration, an incident — whose records **freeze** when it ends and accumulate as a change-stream (a decision log, a changelog).
This tutorial mostly places by function; the life of frozen records — phases, eras, what closes a bounded effort — is a real subject of its own, sketched only here and left to a dedicated lifecycle tutorial (pointed to at the end).

You will also meet a third life, and it needs no third rule.
An *open question* — a design fork not yet decided, a roadmap, an RFC — is not frozen (nothing is settled) and not a stable reference either.
Treat the **deliberation** as a **current** `govern` document you keep editing (an `open-questions.md`, a roadmap), which **decants into frozen records** one entry at a time as each question closes.
Deliberating is current; deciding freezes — so current/frozen still holds, with the open-questions document sitting on the current side until each of its questions leaves it for a frozen decision.

Remember whose tree this is: the source is organized for the **author**, the person writing and maintaining it.
The *reader's* browsing order — orient before how-to for one community, the reverse for another — is a different thing, and on a real project it is **generated** from the files rather than dictating the folders.
That generation, and the frontmatter that drives it, is its own tutorial, pointed to at the end; here we stop at the author's source.

This is also what settles the case Step 3 deferred — a document two activities seem to co-own.
Assign it by **who authors and maintains it, not who reads it**: that is its provenance in the strict sense.
A design rule that the *build* activity writes and keeps correct lives with `build`, even when a *user* must also follow it; the reader who only consumes it gets a short pointer or restatement in their own place, never a second copy — and on a generated reader surface, that cross-reference is exactly what generation supplies.

It helps to see the theory place the documents you already half-expect.
Take the conventional files of a code repository and let provenance and life sort them — these are suggestions the theory endorses, not the only valid answer:

- **README** — a `know`/orient document, produced by the providing-and-teaching activity; lives at the **root**, because an arriving user or installer must find it fast.
- **INSTALL** and how-tos — `do`, from the providing activity; root or `docs/` depending on how first-contact it is.
- **CONTRIBUTING** — `do` shading into `govern`, from the build activity; root by convention, because that is where a would-be contributor looks.
- **LICENSE** — a `govern` act (a commitment, close to a mandate), frozen; root by convention and because tooling expects it there.
- **ARCHITECTURE** / design notes — `know` (the why), from the build activity; `docs/`.
- **CHANGELOG** — `govern`, current and append-only; root by convention.
- **ADR** / decision records — `govern`, each entry frozen; `docs/decisions/` (or `docs/govern/`).

Then let the tree build itself, fractally, one threshold at a time — and keep one principle above the rest: **a function's documents stay together.** Provenance is the primary cut; the `know`/`do`/`govern` register is a split you make *inside* a function, or a temporary coarse cut before any single function is large.

- Pick a name for your documentation folder — `docs/`, `doc/`, `Dokumentation/`; any is fine if it is meaningful to you.
- Some files still go in `./` by convention or because an installer must find them fast (README, LICENSE, INSTALL).
- While the folder is small, a quick coarse cut into `know/`, `do/`, `govern/` is fine — it needs no per-function decision yet.
- But the moment one **function** has three-or-so documents scattered across those registers, pull the *whole function* out into `docs/<function>/`, and split the registers *inside* it: `docs/build/know/architecture.md`, `docs/build/do/contributing.md` — never `docs/know/build/` and `docs/do/build/`, which would tear one function's documents across two homes.
- `docs/know/`, `docs/do/`, `docs/govern/` then keep only the **transversal** documents — those belonging to no single function — plus any not yet migrated down.
- If complexity warrants it, add an `orient` at each new level that points down into it, and rinse and repeat, at every scale.
- The folders and documents are not static; they evolve with the project and with your understanding of it — but with use, they **sediment**, and the sedimented ones stop moving.

There is no single right tree, so here are three that are all correct, for three shapes of project — read them as proof that the *fit* is what matters, not the folder names.

*A solo tool (like `prep`, early):*

```text
README.md            # orient + how-to, everything at once
LICENSE
CHANGELOG.md
```

*A used library, mid-life:*

```text
README.md
LICENSE
CONTRIBUTING.md
docs/
  how-to-install.md          # do
  architecture.md            # know / why
  decisions/                 # govern, one frozen file per decision
    0001-config-format.md
```

*A data analysis for a paper — where the "documentation" is the deliverable itself:*

```text
README.md                    # orient: explain the objective of the paper, of the code and the repo structure
paper/
  method.tex                 # know: the analysis and its assumptions — it *is* part of the paper
supplementary-material/
  reproduce.tex              # do: the one-off run, made repeatable
decisions/
  0001-excluded-samples.md   # govern, frozen
results/                     # generated run outputs — not documented as prose
```

Notice this project has no `docs/` at all.
In total purity you might keep a provenance-ordered source and have a script emit whatever the journal's format demands.
But `paper/` and `supplementary-material/` are how the author already *thinks* the deliverable, so organizing that way is easier for them — and it still cuts along the project's functions (explain the method, enable reproduction, record what was decided), only along the delivery's own seams instead of a generic `docs/`.
That makes it a valid structure, not a compromise.

Root versus a documentation folder, then, is a consequence, not a first choice: your project's own surface (its README, its how-tos, or its `paper/`) sits where its readers first meet it, while its internal records (decisions, design history) sit apart, because they belong to a different activity and a different reader.

## What you have, and that it is partial and alive

You now have a structure that came *out of* your project: its activities named — including the ones you only intend and the ones you are deliberately skipping — the people each activity meets, what they need and in what order, each document with one home decided by its provenance, and a sense of what stays current versus what freezes.

It is deliberately partial, and that is the point: you can now *see* the holes you left.
Fill one when its absence becomes intolerable, not before — you have the keys to fill any of them, so an honest gap costs little.

None of it is fixed.
As you understand the project better you will **regroup** — merge activities that turned out to be one, split one that hid two, and roll many small records up into a few coarse eras so the map stays readable.
Every such move is a small refactor, and with practice the structure sediments into something stable.
Coarse and honest beats fine and overwhelming.

To write any single document well, use the writing on-ramp, [`../writing/tutorial.md`](../writing/tutorial.md), and the force templates in [`../writing/forces/`](../writing/forces/README.md).
To expose your source to outside readers in *their* reading order — the generated reader surface, driven by the frontmatter — read the frontmatter guidance in [`../writing/frontmatter.md`](../writing/frontmatter.md) (its own guided run is planned).
For the life of frozen records — the diachronic provenances, phases, and eras, what freezes and what closes a bounded effort — the state/change seam is sketched in [`concepts.md`](concepts.md), and a dedicated lifecycle tutorial is planned.
To go deeper — several projects under one docs repo, or the metadata that lets a machine read your corpus — read [`concepts.md`](concepts.md) and [`setup.md`](setup.md).
