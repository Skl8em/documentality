---
title: "Foundation — what this project is, for whom, and how it is shelved"
force: explain
intention: formative
view: synchronic
provenance: { type: function, id: steering }
constitutive: no
distance: initiated
audience: [contributor]
reader: H+M
status: draft
phase: 07-structuring-tutorial
note: "New (Ferraris-grounded) vocabulary; the frontmatter schema is reconciled in Phase 10 (Phase 09 tooling readies it)."
---

This is the project laid flat: the front-end we skipped when we started, now written down so it structures the rest instead of living in a chat.
It is the *structuring tutorial applied to ourselves* — its sections follow that tutorial's steps, in order.
It rests on the refounded theory (the three revised essays: `The Inscribed Act`, `A Rhetoric of Organizational Genres`, `The Documentary System`, grounded on Ferraris's documentality — *object = inscribed act*).
Where a claim below is a committed choice, it is marked **[decided]** and is recorded as an ADR.
**Scope: this foundation is Phase-I only.**

## 1. Intention — what we are building

Two horizons, but we work on the first.

- **Phase I — an operational system.** Guidance, templates, and a metadata schema that let someone *structure* and *write* a project's documentation according to the inscribed-act theory, legible to humans and to a machine.
- **Phase II — a computational model** *(named, not yet planned)*.
  Later, the system made machine-operational: AI instructions, hooks, validation and generation driven by the frontmatter.
  We **restrict current work to Phase I** and design Phase II only once Phase I is complete — because Phase II adds a new function that mobilizes a **new body of knowledge** (LLM and agent tooling), and so a **new discourse community** with its own functions, governance, and maintenance, for which the whole front-end will be **re-run**.
  What Phase I commits is only that the frontmatter stay clean, complete, and machine-readable, so it *can* become that interface — not yet that it is one.
  **[decided: Phase I keeps the catalogue machine-ready; Phase II is deferred and re-founded]**

## 2. Functions — what the project touches

Functions come first, because who reads and what they must be told is *derived* from them, not the reverse.

Two faces of "function" matter, and they are not the same.

- **What the project touches, and the knowledge it mobilizes.** This project touches the *documentation theory* (philosophy of language, archival science, information architecture), the *practice of writing* documents (the forces and their moves), the *practice of structuring* a corpus (topology, provenance, life cycle), and light *tooling* (Markdown, git).
  The knowledge these mobilize is essentially one: the inscribed-act theory, plus ordinary Markdown and git.
  That near-single domain is *why* our communities collapse below — a derived fact, not an assumption.
- **The producer's ways of working** (which order the source by provenance): maintaining the theory/foundation, authoring the writing guidance, authoring the structuring guidance, onboarding, and steering.

The refoundation is explicit that both mirror "function," but not the same one: the reader's surface mirrors the *functions served* to whoever meets the project; the source mirrors the *producer's ways of working* (Conway = respect des fonds), the stable activities rather than any org chart.

## 3. Communities and audiences — derived from the functions

Because our functions sit in essentially one domain, the audiences nearly collapse.
`user` (documents their own project) and `contributor` (writes in this repo) are **one discourse community** — the same code, the same language — and `decider` is us.
The role split therefore has little to arbitrate here; that is a *result* of §2, not a starting assumption.
Two axes carry the real variation:

- **Distance — per community, here novice vs initiated in the theory.** In general `distance` is per discourse community: a reader can be initiated in one aspect's field and a novice in another, and a project may reasonably address the initiated of a domain rather than teach it from scratch.
  Our project has essentially one field — the theory — so distance reduces to *how much of the theory a reader already holds*.
  A beginner-facing document (the tutorials, an orient) spells the concepts out; an initiated-facing one (the rules, the schema) presumes them.
  **[decided]**
- **Human vs machine — orthogonal.** The machine is not a role.
  It can occupy the *function* of `user` or `contributor` (it reads and it writes) but never `decider` (it does not set conventions).
  "Being a machine" is a separate dimension — operationally a `reader: H|M` flag; in the theory, the recipient relation pushed to its limit (maximum distance and a quiet power).
  **[decided]**

## 4. Provenance — and why there is no function-versus-provenance tension

A **function is one of the two types of provenance**, so "by function" and "by provenance" are not rival axes; the source is shelved by provenance, full stop.

- **Function** — a permanent responsibility (maintaining the theory, the writing guidance, the structuring guidance, onboarding, steering).
  It does not end.
- **Project** — a bounded effort (a construction phase).
  It closes.

The relation to `view` is real but asymmetric.
`synchronic ⇒ function`: only a permanent responsibility is kept current, so a maintained state always belongs to a function.
`diachronic ⇏ project`: a frozen record belongs to *whatever produced it* — a bounded project, **or** a function's own stream of frozen changes (our `CHANGELOG` is `diachronic` and `provenance: steering`, a function).

The groupings are **mutable**: functions and provenance alike are refined or coarsened as understanding matures.
We keep the provenance log coarse with three **eras** — *naive sketch* (phases 01–05), *refoundation* (06–10), *phase II* (later) — each nesting its micro-phases, because a coarse map reads better than twenty microscopic records.

## 5. Scale

Small, and honest about it.
One person, one tight community; a single modest tree, one docs repo.
We are past the degree-zero single README but nowhere near needing deep sub-branches.
The rule (System §4) is to **deepen only as complexity compels** — add a scale when a team, a function, or a process multiplies — and not before.
We resist the failure of "setting up documentation properly" three scales too high.

## 6. Shelf — source vs. generated surface

Before computing, the folder tree *was* the reader's shelf; the two could not be separated.
They can now, and the theory says so: the **shelf** gives each item one place; the **catalogue** (the frontmatter) exists to *generate* readable surfaces.
So: **[decided]**

- **The source folder tree is the contributor/producer's shelf** — organized by provenance (§4).
  One place per item.
- **The user's reading surface is generated** from the catalogue, ordered by the functions served.
  It may re-order or break the source structure freely, because it is *derived*, not authoritative.
  Several surfaces are affordable.
- **The catalogue (frontmatter) is the single pivot**: it generates the reader surfaces *and* (in Phase II) is the interface the machine will operate.
- The one place a tension could arise is source (provenance) versus surface (functions served); it is dissolved by generation, since we hand-maintain only the source and derive the surface — never a second tree by hand.
- Because here contributor = user, the source shelf doubles as an acceptable reading surface *for now*, so surface generation is deferred — but we stop contorting the folder tree to please a reader who is not here yet.

Consequence for our own tree: the earlier "scope axis (write/structure), dominant = user" (ADR-010) described a *generated surface*, not the source.
The **source** is organized for the **contributor** (producer), shelved by provenance — one folder per function (`theorising/`, `operationalizing/`, `writing/`, `structuring/`, `steering/`, `imagining/`) plus the frozen `phases/`.
`operationalizing/` was added later, in Phase 10 (ADR-033): between the theory and the guidance sits the layer that decides *which handles we carve onto the theory* — `view`, `constitutive`, `register`, `hash` — and why we carve them that way.
The generic `docs/` bucket is **dissolved** (its governance is `steering/`, its records `phases/`); the root axis is now `provenance` / dominant `contributor`, and `write`/`structure` are the order of a *generated* view.
This structural move is **done**, and Phase 08 has since completed the rest: the refounded vocabulary carried across the product, the nine `_legacy/` forces migrated (all twelve now built), `_legacy/` retired, and the function folders renamed to their gerund ids (ADR-027).
**[decided]**

## 7. Founding decisions on record

Recorded as ADRs, several superseding or refining older ones:

- Adopt the **Ferraris-grounded refoundation** of the theory (ADR-014; supersedes the v1–v3 basis).
- **Perlocution has no zero**: a constitutive floor + an intention (formative / suasive / affective); forces are **recognized cells**, not primitives (ADR-015; supersedes ADR-002).
- **know / do / govern** is a gloss; `recommend` and `entail` are extension examples (ADR-016).
- **Audience derived from functions**: functions first, communities and per-community `distance` derived; human/machine orthogonal (ADR-017, ADR-022).
- **Shelf**: source = producer shelf by provenance, reader surface = generated; a function *is* a provenance; `synchronic ⇒ function` (ADR-018, refines ADR-010; ADR-022).
- **Groupings are mutable**; three eras over the micro-phases (ADR-022).
- **Restart strategy (a)**; **scope Phase I; defer and re-found Phase II** (ADR-019, ADR-020).

## 8. Where this leads

The plan and named phases are in [`roadmap.md`](roadmap.md).
This foundation is the reference the rest is built against; when it changes, the change is recorded, not silently overwritten.
