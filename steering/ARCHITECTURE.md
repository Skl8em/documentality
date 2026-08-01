---
title: "Architecture of the documentation system"
force: explain
verb: illuminate
register: know
intention: model
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor, decider]
reader: H+M
status: draft
note: "Refounded in Phase 08 to the provenance-first shelf and the intention vocabulary; the schema is reconciled in Phase 10 (Phase 09 tooling readies it)."
---

This explains how the repository is laid out and *why* it is shaped this way, so a contributor can change it without breaking its logic.
If you only want to *use* the system, read the product (`../writing/`, `../structuring/`) instead; this is about the repo as a maintained artifact.

## The question this answers

Why is the source shelved by **function** — `theorising/`, `writing/`, `structuring/`, `steering/`, `imagining/`, plus a frozen `phases/` — rather than by topic, scope, or a product-vs-docs split?

## The model: the repo eats its own theory

The system's core claim is that a document is an **act** with a **force**, made to live through time, and that its coordinates belong in a **catalogue** (the frontmatter) from which readable surfaces are *generated*.
The repo applies that claim to itself, which fixes three structural decisions.

1. **The source is the producer's shelf, shelved by provenance.** A **provenance** is who produced and maintains an item; a **function** is a permanent responsibility (one kind of provenance), a **project** a bounded effort (the other).
   Each standing function is one root folder; the project's own governance (`steering`) and its intended-but-unbuilt work (`imagining`) are functions like any other; the frozen construction records are a bounded `project` provenance under `phases/`.
   The root declares `axis: provenance`, `dominant-community: contributor` (ADR-018, ADR-024).
   Folder names are the **gerund** of the activity (ADR-027).

2. **The reader surface is generated, not a second tree.** The shelf gives each item one place; the user's reading order — by the functions served, by door, by whatever a reader needs — is *derived* from the catalogue, never hand-carved.
   The one tension that could arise, source (provenance) vs. surface (functions served), is dissolved by generation: we hand-maintain only the source.
   Because here contributor ≈ user, the source shelf doubles as an acceptable reading surface for now, so surface generation is deferred (`foundation.md` §6).

3. **Governance is placed by the domain it governs, not by its register (ADR-025).** `steering` is not "the govern register"; it is the activity whose *domain is the project itself*, and like any activity it carries all three registers — `foundation` is its `know`, `CONTRIBUTING` its `do`, the ADR register its `govern`.
   A rule that binds the *user's* writing is product content (`writing/`); the same force binding *contribution to the project* is `steering/CONTRIBUTING.md`.
   A decision and the rule it installs are two documents joined at the state/change seam.
   The activity a document *bears on* is a separate coordinate, `concerns` (one ⇒ vertical/locally ownable; several ⇒ transversal); the per-activity view is **generated** from it, records are never relocated to satisfy proximity.

## Forces, doors, and the register gloss

The twelve forces sit under three **doors** — **know** (`orient`, `explain`, `describe`), **do** (`instruct`, `teach`, `recommend`), **govern & record** (`mandate`, `commit`, `propose`, `decide`, `prove`, `account`).
The doors are a **register** gloss over `force` (know / do / govern) — a reading convenience *derived* from the force, **not** the shelf axis (ADR-016). `writing/forces/{know,do,govern-and-record}/<force>/` is split by door only because it is itself a generated-style surface; the source everywhere else is shelved by provenance.
Each force folder carries a stance (`README.md`, an `explain`) and a skeleton (`template.md`, an `instruct`).

## The metadata backbone

Every file carries frontmatter (`../writing/frontmatter.md`): `force`, `intention`, `view`, `provenance`, `audience`, `reader`, `status` are required. `intention` is the perlocutionary coordinate — a constitutive floor (`state`) with an optional aim above it (`locate`/`model`/`enable`/`convince`, grouping into `formative`/`suasive`/`affective`; ADR-015/026).
Derivable facts — **door/register**, direction of fit, diataxis (`force` × `intention`) — are **generated, never stored**.
Tree roots additionally carry `axis` and `dominant-community`; governance records may carry `concerns`.
This catalogue is what lets a validator, and later a writing AI, operate on the corpus.
The full schema reconciliation (coarse-vs-fine `intention`, whether `register` is stored, `distance`/`power` values) is Phase 10, on the lint harness Phase 09 stands up.

## Provenance map (how this repo is owned)

| Area | provenance |
| --- | --- |
| root `README.md` | function `steering` (served: onboarding) |
| `theorising/**` | function `theorising` |
| `writing/**` | function `writing` |
| `structuring/**` | function `structuring` |
| `steering/**` governance (`foundation`, `roadmap`, `ARCHITECTURE`, `CONTRIBUTING`, `CHANGELOG`, `ADR.md` register, `open-questions`) | function `steering` |
| `imagining/**` | function `imagining` (Phase II, parked) |
| `phases/<era>/<phase>/**` (records) | project `phase-NN` (frozen, grouped by era) |

## In short

The repo is the theory applied to itself: a **producer's shelf** ordered by provenance (one gerund-named folder per function, plus frozen `phases/` by era), from which reader surfaces are *generated*; governance placed by the domain it governs, with `concerns` as its relational coordinate; forces glossed into three doors as a register view over `force`; and every design choice frozen as an ADR.
