---
title: "Structural rules (binding)"
force: mandate
verb: require
intention: state
view: synchronic
provenance: { type: function, id: structuring }
audience: [user]
reader: H+M
status: stable
---

Binding for any document kept in the system. Breaking one corrupts either navigability or the evidence chain. Defaults you may tune are in [`defaults.md`](defaults.md); the reasoning is in [`concepts.md`](concepts.md).

## The rules

- You **must** give each file **one place on the shelf** (one reading location) *and* a declared `provenance` (the activity that produced it). These are separate; do not conflate the tree with provenance. Consequence: a file filed by subject instead of provenance gets duplicated or lost.

- You **must** declare the tree's **axis and dominant community in its root orient document** — the `README.md` at the tree root — under a stated heading (e.g. *How this tree is organized*), and, where tooling checks it, as `axis` / `dominant-community` frontmatter on that file. A reader finds it because the README is always the front door; the declaration names itself as such so it is unmistakable. Consequence: without it, later contributors re-file the tree at every reorganization, and no one — human or machine — can tell whether a given document is correctly placed.

- You **must** reference an exact project state by a **pinned submodule**, never by copy or moving link. Consequence: an unpinned reference cannot serve as evidence and silently rots.

- You **must** keep **project records frozen** after closure (`view: diachronic`); a change is a *new* document via `supersedes`, never an in-place edit. Consequence: a rewritten record is a loss of memory and is reverted.

- You **must** keep the derived **state honest to its changes**: editing a synchronic state document requires recording the corresponding change (ADR, changelog entry). Consequence: an undocumented state change breaks the seam and the audit trail.

- You **must not edit in an export target** (wiki, docx, site). Fix the source, re-export. Consequence: the derived copy drifts from its authority.

- You **must** give each document type a **retention rule** (`retention`, or the default for its force). Consequence: without it the corpus sediments.

## Why so few

A structural rule earns its place only if breaking it silently corrupts navigation or evidence. Everything else is a default ([`defaults.md`](defaults.md)). A short mandate is an obeyed mandate.
