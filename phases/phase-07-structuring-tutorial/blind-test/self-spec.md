---
title: "This project — a short spec, for the blind test"
status: draft
note: "A neutral summary of the documentation-system project itself, written so it can be handed to a fresh reader. It deliberately does not pre-answer the structuring tutorial: it states the project's facts and its genuine open questions, but not its activities, audiences, or folder tree."
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

These five names are how the maintainer currently *thinks* about the project.
Whether each is a committed source folder or a conceptual grouping a generator would present differently is exactly the kind of question the structuring work is meant to settle, so this spec does not fix it: the source is plain Markdown files under git, and how they are laid out on disk is not asserted here.

## 3. Intended readers and use

The product is read by someone who wants to document *their own* project well.
The project is also maintained and extended by whoever develops the system itself.
Today that developer and that reader are, in practice, **one person** — a single maintainer wearing several hats — and the project has **no second contributor yet**.
Onboarding one is a foreseeable need, deliberately deferred: it will be *built on* the writing, structuring, and frontmatter guidance once those exist, rather than designed separately now.
Later, an AI is meant to *operate* the system (generate, validate) from the same metadata.
The whole thing is meant to be, itself, a **worked example of its own theory** — an aspiration the maintainer checks by hand, on no fixed cadence, with no separate owner or process assigned to that check.

The intended readership is deliberately **wide**, even though the current writing is not.
The ambition is that the system serve someone documenting Photoshop or the G-Suite just as well as the solo author of a small personal CLI toy that will never leave their machine.
But its *current* discourse register is pitched at readers fluent in academic discourse, and the maintainer's own present need is what it is written for first; other registers and audiences would get their own tutorials later.
So "small" (one maintainer, a tight *present* readership) and "broad" (a general system for any project's documentation) are both true and describe different things — the team, and the ambition.

## 4. State and constraints

Small in team, not in ambition: essentially one maintainer, a tight present readership, a single repository, Markdown source under git.
It has recently been **refounded** (the theory reworked and the front-end — purpose, audiences, functions, provenance — laid out explicitly for the first time), and it is mid-refactor: some parts still carry older vocabulary.
The **metadata schema is not hand-authored and not yet settled**: it is meant to be *derived* by tooling, and writing that tooling is itself part of the project's work — so the schema stabilizes as the implementation produces it, rather than being fixed up front.
The source is kept tool-agnostic (plain Markdown, convertible by Pandoc); any published reading surface is to be **generated, not hand-maintained**.
The **README addresses people who find or clone the repository** (on GitHub, GitLab, or Confluence); the project is not otherwise released or versioned, and publishing it as a website or a book would be a separate restructuring for that surface's own intended audience, not the same source.

Its own construction is recorded as **dated decision records grouped into phases**, with a central append-only register and a changelog.
**Phase I is left when it reaches a minimal-viable-product state** — usable in practice, with the tools to derive what is still missing (for instance, how-tos and a tutorial for external contributors) in place; there is no mechanical rule beyond that judgment.
Decision records are **frozen once made**: a later reversal is written as a *new* record that supersedes the old one, and the old record is not edited — so "frozen" means append-and-supersede, never rewrite.
Phase II, though named in detail, has **no document of its own yet**; it is deliberately treated as future, intended work rather than given a current home.

## 5. Non-goals (for now)

- Not yet the computational/AI layer (that is Phase II, deliberately deferred).
- Not a hosted website or app; the deliverable is source files a reader or a generator consumes.
- Not tied to any one documentation generator or wiki.
- Not yet designed for a second contributor, an external adopter, or a formal release — each is a foreseeable need the project acknowledges but has not built for.
