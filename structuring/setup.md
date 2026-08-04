---
title: "Lay down the tree and topology"
force: instruct
verb: walk-through
intention: state
view: synchronic
provenance: { type: function, id: structuring }
constitutive: no
audience: [user]
reader: H+M
status: stable
---

Follow this when starting docs for a project, or a docs repo over several projects.
The reasoning is in [`concepts.md`](concepts.md); the defaults you'll apply are in [`defaults.md`](defaults.md).

## A. Docs living with one project (in-repo)

1. **Choose the tree axis** and write it at the top of `docs/`.
   Default for code: component / builder's path (`defaults.md`).
2. **Create the shelf** — one place per document:

   ```text
   README.md                 # orient — front door
   docs/
     architecture.md         # explain — the why
     reference/              # describe — current state, kept current (synchronic)
     guides/                 # instruct — how-tos, runbooks
     guidelines/             # recommend — best practices, non-binding
     tutorials/              # teach — learning paths
     decisions/              # decide — ADRs, frozen (diachronic)
     CHANGELOG.md            # account — frozen, append-only (diachronic)
   CONTRIBUTING.md           # mandate — the rules
   ```

3. **Copy the starting genres** from `../writing/forces/`: `orient` → `README.md`, `explain` → `docs/architecture.md`.
4. **Set frontmatter** on each (`../writing/frontmatter.md`): `force`, `intention`, `view`, `provenance`, `audience`, `reader`, `status`.

## B. A docs repo over several projects

1. **Choose the axis: business function** (the shared language), not implementation.
2. **Create the cross-project shelf:**

   ```text
   README.md                       # orient — map of functions and projects
   functions/                      # synchronic — current state per function
   projects/                       # provenance — one pinned submodule per project
     migration-2026/    (submodule -> exact commit)
   archive/                        # diachronic — closed records, frozen
   catalog/                        # indexes generated from frontmatters (do not hand-edit)
   ```

3. **Add each project as a pinned submodule** under `projects/` — `git submodule add <url>` then commit the pin.
   The pin is the fixity bond; never replace it with a copy or a moving link.
4. **Reference, never duplicate:** a function page cites the project's exact state via its submodule pin (`pin:` in frontmatter), it does not copy the content.

## C. Export (any topology)

The source is Markdown / Quarto.
Every target (site, wiki, docx, pptx, pdf) is a derived package.
Stay tool-agnostic; the minimal contract is Pandoc: keep standard Markdown so `pandoc source.md -o target.{docx,pptx,pdf,html}` works without a specific generator. **Never edit in the export target** — fix the source and re-export, or the derived state drifts from its authority.

## Verify

You are done when: every file has one place on the shelf and a valid frontmatter; every cross-project reference is a pinned submodule; the tree's axis is written at its root; and nothing is edited anywhere but the source.
Run the checks in [`rules.md`](rules.md).
