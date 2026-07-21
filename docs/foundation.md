---
title: "Foundation — what this project is, for whom, and how it is shelved"
force: explain
register: know
intention: model
view: synchronic
provenance: { type: function, id: steering }
distance: initiated
audience: [contributor]
reader: H+M
status: draft
phase: 06-refoundation
note: "New (Ferraris-grounded) vocabulary; the frontmatter schema is reconciled in Phase 08–09."
---

This is the project laid flat: the front-end we skipped when we started, now written down so it structures the rest instead of living in a chat.
It is the *structuring tutorial applied to ourselves* — its sections are that tutorial's steps.
It rests on the refounded theory (the three revised essays: `The Inscribed Act`, `A Rhetoric of Organizational Genres`, `The Documentary System`, grounded on Ferraris's documentality — *object = inscribed act*).
Where a claim below is a committed choice, it is marked **[decided]** and will be recorded as an ADR.

## 1. Intention — what we are building

Two horizons.

- **Phase I — an operational system.** Guidance, templates, and a metadata schema that let someone *structure* and *write* a project's documentation according to the inscribed-act theory, legible to humans and to a machine.
- **Phase II — a computational model.** The same system made machine-operational: AI instructions, hooks, validation and generation driven by the frontmatter.
  The frontmatter therefore stops being a mere catalogue convenience and becomes **the machine interface** of the system. **[decided]**

## 2. Communities and audiences

For *this* project the audience roles nearly collapse.
`user` (documents their own project) and `contributor` (writes in this repo) are **one discourse community** — same code, same language; `decider` is us.
A small project means a tight community.
So the role split has little to arbitrate here. Two axes carry the real variation:

- **Distance — beginner vs initiated.**
  What actually differs between readers is familiarity with the *theory*: how much background, vocabulary, and concept must be spelled out.
  This is the theory's `distance` coordinate (shared code), not a role.
  A beginner-facing document (a tutorial, an orient) explicates the concepts; an initiated-facing one (the rules, the schema) presumes them.
  **[decided]**
- **Human vs machine — orthogonal.**
   The machine is not a role.
   It can occupy the *function* of `user` or `contributor` (it reads and it writes) but never `decider` (it does not set conventions).
   "Being a machine" is a separate dimension — operationally a `reader: H|M` flag; in the theory, the recipient relation pushed to its limit (maximum distance + a quiet power).
   **[decided]**

## 3. Functions — two faces

- **Functions served to the reader** (the *communication* face): *write a document* and *structure a corpus* — the two things a user does.
  These order the reader's surface.
- **The producer's ways of working** (the *archival* face): how we build and maintain the system — the foundation we depend on, the product we author, the governance we keep.
  These order provenance, and therefore the source.

The refoundation is explicit that both mirror "function," but not the same one: the reader's surface mirrors *functions served*; the archive/source mirrors the *producer's ways of working* (Conway = respect des fonds), stable functions rather than the org chart.

## 4. Provenance

- **Functions** (permanent responsibilities, synchronic, maintained): the theory/foundation, the writing guidance, the structuring guidance, onboarding, steering.
- **Projects / phases** (bounded, diachronic, frozen): each construction effort, including this refoundation (`phase-06`). Records belong to their phase.

## 5. Scale

Small, and honest about it.
One person, one tight community; a single modest tree, one docs repo.
We are past the degree-zero single README but nowhere near needing deep sub-branches.
The rule (System §4) is to **deepen only as complexity compels** — add a scale when a team, a function, or a process multiplies — and not before.
We resist the failure of "setting up documentation properly" three scales too high.

## 6. Shelf — source vs. generated surface (the key architectural decision)

Before computing, the folder tree *was* the reader's shelf; the two could not be separated.
They can now, and the theory says so: the **shelf** gives each item one place; the **catalogue** (the frontmatter) exists to *generate* readable surfaces.
So: **[decided]**

- **The source folder tree is the contributor/producer's shelf** — organized by our ways of working (provenance).
  One place per item.
- **The user's reading surface is generated** from the catalogue, ordered by functions served.
  It may re-order or break the source structure freely, because it is *derived*, not authoritative. Several surfaces are affordable.
- **The catalogue (frontmatter) is the single pivot**: it generates the reader surfaces *and* it is the interface the Phase-II machine operates.
  The shelf insight and the computational intention are the same bet.
- Because here contributor = user, the source shelf doubles as an acceptable reading surface *for now* — so surface generation is deferred to Phase II — but we stop contorting the folder tree to be the user's ideal browse order.

Consequence for our own tree: the earlier "scope axis (write/structure), dominant = user" (ADR-010) described a *generated user surface*, not the source.
The **source** is organized for the **contributor** (producer); `write`/`structure` become the order of a generated view.
Per approach, we **act this principle now and move files in Phase 08**, keeping the current tree meanwhile.
**[decided]**

## 7. Founding decisions to record

Each becomes an ADR in `phase-06`, several superseding older ones:

- Adopt the **Ferraris-grounded refoundation** of the theory (supersedes the v1–v3 theory basis).
- **Perlocution has no zero**: a constitutive floor + an intention (formative / suasive / affective); forces are **recognized cells** (direction-of-fit × intention), not primitives (supersedes ADR-002's `formative` boolean and reframes ADR-013's open pairings as a *consequence*, not a relaxed rule).
- **know / do / govern** is a gloss over the three active direction-of-fit families; `govern` is marked, not a third primitive.
- **recommend** and **entail** are worked examples of the extension method, not core categories.
- **Audience model for this project**: roles collapse; `distance` (beginner/initiated) is the live axis; human/machine orthogonal (supersedes ADR-006 for this project).
- **Shelf**: source = producer shelf, reader surface = generated; catalogue is the pivot (refines ADR-010's scope/user axis).
- **Restart strategy**: front-end first, principles acted now, physical reorg in Phase 08.

## 8. Where this leads

The plan and named phases are in [`roadmap.md`](roadmap.md). This foundation is the reference the rest is built against; when it changes, the change is recorded, not silently overwritten.
