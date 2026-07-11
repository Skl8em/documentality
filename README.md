---
title: "Project documentation system — start here"
force: orient
verb: situate
formative: true
diataxis: explanation
view: synchronic
audience: [developer, AI, maintainer]
status: stable
written-at: v1
valid-for: v1
---

This repository holds a **system for writing, structuring, and keeping project documentation**.
It does not explain *your* project; it explains how to document any project so that it is legible to a hurried human *and* to an LLM.
It is itself written by the rules it states: every file declares its **force** in its frontmatter, and this page is an `orient` — its only job is to situate you and route you onward.

## What you're holding

The system rests on one idea: a document is not a container of information to be sorted by subject, it is an **act** performed from a definite position (what it does, toward whom) and made to live through time.
Three practical questions follow, one per file:

- **What to write, and how to phrase it** → `writing.md`. The eleven *forces* (orient, explain, describe, prove, account, instruct, teach, mandate, commit, propose, decide), each with its generative verb, move structure, and failure mode — fused with the writing patterns that lower cognitive load for both human and LLM.
- **Where to put it, and how to keep it** → `structure.md`. The topology (docs living with the project vs. a separate docs repo with submodules), the reading tree, provenance (function vs. project), the state/change seam, life cycle and retention, export.
- **How to tag it for the machine** → `frontmatter.md`. The YAML metadata schema that makes each file self-describing: its force, type, view, provenance, audience, status.

Plus a `templates/` folder: one skeleton per force, with its move structure already wired in.
Copy, fill, done.

## Where to enter, by need

You're **starting the docs for a new project** → read `structure.md` (topology and tree sections), lay down the skeleton, then copy `templates/README.md` and `templates/ARCHITECTURE.md`.

You **need to write one specific document** (a decision, a proposal, a procedure…) → go straight to `writing.md`, find the force, take the matching template in `templates/`.

You **have several projects to federate** → read `structure.md` (docs repo + submodules section): that's where exact per-commit anchoring is settled.

You **don't know which force your document has** → `writing.md` opens with a short five-question interrogation that gives you the dominant force in a minute.

You're **preparing for AI use** (generation, validation, RAG) → the `frontmatter.md` + `templates/` pair is the raw material; the frontmatter becomes the spec, the moves become the prompts.
This step is deliberately left for later, but everything here is built to make it direct.

## The rule that governs everything else

A corpus serves two incompatible masters: **be found and read now** (communication) and **stand as evidence over time** (archive).
No single order serves both. Almost every failed doc conflates them.
This system keeps them apart — the readable tree on one side, frozen provenance on the other — and stitches them at a single point: *the frozen record of a change becomes the current state you maintain*.
If you remember one thing, remember that one; `structure.md` develops it.

## In short

Three guidance files (structure, write, tag) + templates.
Every document you produce answers three questions: *what does it do?* (its force → `writing.md`), *where does it live and for how long?* (its provenance and view → `structure.md`), *how does the machine read it?* (its frontmatter → `frontmatter.md`).
