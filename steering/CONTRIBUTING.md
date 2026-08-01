---
title: "Contributing to the system"
force: mandate
verb: require
intention: state
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor]
reader: H+M
status: stable
---

Binding rules for changing this repository (the system itself), not for using it. Rules for documents you write *with* the system are in the product ([`../write/rules.md`](../writing/rules.md), [`../structure/rules.md`](../structuring/rules.md)); this file governs contributions *to* the system.

## Rules

- You **must** give every new file a valid frontmatter and a single dominant `force` — the system must obey its own [`../write/rules.md`](../writing/rules.md). A contribution that violates the product's own rules is rejected.

- You **must** record any **design decision** that changes the theory, the schema, the force repertoire, or the tree shape by appending a row to the register [`ADR.md`](ADR.md) *and* writing the full record (context + `justify` + `entail`) in the **current phase** under [`phases/`](../phases/README.md); add a line to [`CHANGELOG.md`](CHANGELOG.md). Consequence: an undocumented design change is reverted — the ADR *is* the decision.

- You **must not** edit an existing ADR to reflect a later choice. A superseding decision is a **new** ADR that sets `superseded-by`/`supersedes`. ADRs are `view: diachronic`, frozen. Consequence: a rewritten ADR erases the design memory and is reverted.

- You **must** shelve content by its **provenance** — the function that maintains it: `theorising/`, `writing/`, `structuring/`, the project's governance in `steering/`, intended work in `imagining/`, and frozen records under `phases/`. Do not mix a function's content into another's shelf; the user's reading order across `writing/` and `structuring/` is a *generated* surface, not a folder to hand-carve.

- You **must** keep `provenance` meaningful: use the maintaining function (`theorising`/`writing`/`structuring`/`steering`/`imagining`) or the owning project (`phase-NN`), never a blanket id.

- You **may** propose larger changes as an RFC (`propose`) before writing the ADR; for small, obvious fixes an ADR alone suffices.
