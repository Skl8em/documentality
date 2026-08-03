---
title: "operationalizing — the operational apports, between theory and product"
force: orient
intention: formative
view: synchronic
provenance: { type: function, id: operationalizing }
constitutive: no
audience: [contributor, decider]
reader: H+M
status: draft
---

This shelf holds the **operational apports**: the coordinates and conventions we *chose to reify* so that the theory becomes a workable, checkable, machine-ready system.
They are not the theory, and they are not the tooling.
They sit at a distinct layer:

`theorising → operationalizing → structuring / writing → designing → IT tools`

`theorising` says what a document *is* (an inscribed act, with a force, an intention, a recipient at some distance and power).
`operationalizing` decides *which handles we carve onto that* to make it operable — a `view` flag, a `constitutive` mark, a derived `register` — and *why we carve them this way*.
`structuring` and `writing` then *use* those handles; `designing` and the `IT tools` (linters, ULID minting, hooks) merely *enforce* them.

**Keep this layer conceptual.**
A fiche here explains what an apport is, what theory-notion it operationalizes (if any), why it was reified this way, the alternatives, and the work it does.
The *implementation* of that work lives with the IT tools, not here — a fiche points to the tool, it does not become one.

## The complete inventory

Every frontmatter coordinate, sorted by where it comes from.
"Theory" = given by the essays.
"Apport" = a reification decision that is *ours* — the subject of this shelf.

| Coordinate | Theory root | Operational apport? |
|---|---|---|
| `force` | inscribed act (essays 1–2) | no — a theory primitive, stored as-is |
| `intention` (+ floor `state`) | perlocution (essays 1–2) | no in concept; the *coarse* encoding is a small choice |
| `distance` | recipient relation | no |
| `power` | recipient sanction | no |
| `audience` | the recipient (theory) | **partly** — the *role* typology (`user`/`contributor`/`decider`) is ours |
| `provenance` | documentary system (essay 3): respect des fonds | **partly** — the `{type, id}`, `function`/`project` encoding is ours |
| **`view`** | state/change seam (essay 3) | **yes** — reified as `synchronic`/`diachronic` → [`view`](view.md) |
| **`register`** | direction of fit (theory) + `constitutive` | **yes** — a derived navigation gloss → [`register`](register.md) |
| **`constitutive`** | Ferraris/Searle (theory-rooted) | **yes** — a stored conscious mark → [`constitutive`](constitutive.md) |
| `reader` (`H`/`M`/`H+M`) | machine = recipient-at-limit | **yes** — a system affordance for the machine |
| `verb` | — | **yes** — a soft-summary convenience over the tuple |
| `concerns` | "relation, not location" (essay 3) | **yes** — the transversal/vertical relation |
| `status` | — | **yes** — lifecycle bookkeeping |
| `retention` | archival practice (essay 3) | **yes** — reified retention rule |
| `supersedes` / `superseded-by` | supersede-not-edit (essay 3) | **yes** — record chaining |
| `pin` | fixity / the archival bond (essay 3) | **yes** — a VCS fixity mechanism |
| `hash` | fixity (essay 3) | **yes** — a per-record fixity seal (new) |
| `id` (ULID) / `slug` | — | **yes** — the identity scheme (no theory root) |
| `axis` / `dominant-community` | shelf/catalogue (essay 3) | **yes** — the tree-root shelf declaration |
| `written-at` / `valid-for` | — | **yes** — production vs validity phase |

The pattern: the **theory** gives `force`, `intention`, `distance`, `power`, and the recipient; **operationalizing** adds everything needed to *keep, check, and generate* a corpus of such acts.
Essay 3 (the documentary system) is the richest source of apports — it names the notions (provenance, state/change, shelf, fixity), and this shelf records the *reifications* of them.

## First fiches

- [`view`](view.md) — maintained state vs frozen change, made a coordinate.
- [`constitutive`](constitutive.md) — does the act posit a social object, or serve a reader.
- [`register`](register.md) — the derived `know`/`do`/`govern` gloss.

Still to write (the inventory above lists them): `reader`, `concerns`, `verb`, `status`, `retention`, `supersedes`, `pin`, `hash`, `id`/`slug`, `axis`/`dominant-community`, and the operational halves of `provenance` and `audience`.
