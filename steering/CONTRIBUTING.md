---
title: "Contributing to the system"
force: mandate
verb: require
perlocution: none
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

Binding rules for changing this repository (the system itself), not for using it. Rules for documents you write *with* the system are in the product ([`../write/rules.md`](../write/rules.md), [`../structure/rules.md`](../structure/rules.md)); this file governs contributions *to* the system.

## Rules

- You **must** give every new file a valid frontmatter and a single dominant `force` — the system must obey its own [`../write/rules.md`](../write/rules.md). A contribution that violates the product's own rules is rejected.

- You **must** record any **design decision** that changes the theory, the schema, the force repertoire, or the tree shape by appending a row to the register [`ADR.md`](ADR.md) *and* writing the full record (context + `justify` + `entail`) in the **current phase** under [`phases/`](../phases/README.md); add a line to [`CHANGELOG.md`](CHANGELOG.md). Consequence: an undocumented design change is reverted — the ADR *is* the decision.

- You **must not** edit an existing ADR to reflect a later choice. A superseding decision is a **new** ADR that sets `superseded-by`/`supersedes`. ADRs are `view: diachronic`, frozen. Consequence: a rewritten ADR erases the design memory and is reverted.

- You **must** shelve content by its **provenance** — the function that maintains it: `theory/`, `write/`, `structure/`, the project's governance in `steering/`, intended work in `imagine/`, and frozen records under `phases/`. Do not mix a function's content into another's shelf; the user's reading order across `write/` and `structure/` is a *generated* surface, not a folder to hand-carve.

- You **must** keep `provenance` meaningful: use the maintaining function (`theory`/`writing`/`structuring`/`steering`/`imagine`) or the owning project (`phase-NN`), never a blanket id.

- You **may** propose larger changes as an RFC (`propose`) before writing the ADR; for small, obvious fixes an ADR alone suffices.

## Working with `_legacy/`

`_legacy/` is read-only source for migration. You **may** copy from it into the new tree; you **must not** link the product to it or add new content there.
