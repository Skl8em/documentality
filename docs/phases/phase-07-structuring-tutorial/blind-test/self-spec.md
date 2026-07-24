---
title: "This project — a short spec, for the blind test"
status: draft
note: "A neutral summary of the documentation-system project itself, written so it can be handed to a fresh reader. It deliberately does not pre-answer the structuring tutorial."
---

# The documentation-system project — specification

## 1. Purpose and scope

The project is a **system for documenting software (and other) projects**, in two layers.

- A **theory**: an account of what an organizational document *is* — not a container of information sorted by subject, but a *typified communicative act* with an illocutionary *force* (what it does: orient, explain, describe, prove, account, instruct, teach, recommend, mandate, commit, propose, decide) and a perlocutionary *intention* (what it seeks in the reader), addressed to a recipient across *distance* and *power*. The theory is set out in three essays (an "inscribed act" coordinate theory, a "rhetoric" of the writer's stances, and a "documentary system" of how a corpus is kept). It is grounded philosophically on Ferraris's *documentality* (a social object *is* an inscribed act).
- An **operational product** built on the theory: guidance, templates, and a metadata schema (YAML frontmatter) that let someone *write* individual documents (by naming a document's force and following its move structure) and *structure* a whole corpus (by provenance, life cycle, and a readable tree), for human readers and, eventually, for a machine.

Two horizons are declared. **Phase I** is the operational system just described. **Phase II** (named, not yet built) would make it machine-operational: AI instructions, git hooks, validation and generation driven by the frontmatter. Current work is Phase I.

## 2. What it is made of

- The **theory** essays (the intellectual basis the product depends on).
- **Writing** guidance: one stance per force (its generative verb, move structure, failure mode) plus reusable templates, and a set of readability patterns for humans and language models.
- **Structuring** guidance: how a corpus is organized (a source shelf ordered by provenance vs a generated reader surface), the state/change seam, scale/recursion, and this tutorial.
- A **metadata schema** (the frontmatter): the machine-readable catalogue of coordinates on every file.
- **Governance and records**: the project documents its own construction as dated decision records grouped into phases, with a central register and a changelog.

## 3. Intended readers and use

The product is read by someone who wants to document *their own* project well.
The project is also maintained and extended by whoever develops the system itself.
Later, an AI is meant to *operate* the system (generate, validate) from the same metadata.
The whole thing is meant to be, itself, a worked example of its own theory.

## 4. State and constraints

Small: essentially one maintainer, a tight readership, a single repository, Markdown source under git.
It has recently been **refounded** (the theory reworked and the front-end — purpose, audiences, functions, provenance — laid out explicitly for the first time), and it is mid-refactor: some parts still carry older vocabulary.
The source is kept tool-agnostic (plain Markdown, convertible by Pandoc); any published reading surface is to be generated, not hand-maintained.

## 5. Non-goals (for now)

- Not yet the computational/AI layer (that is Phase II, deliberately deferred).
- Not a hosted website or app; the deliverable is source files a reader or a generator consumes.
- Not tied to any one documentation generator or wiki.
