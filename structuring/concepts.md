---
title: "Two systems, provenance, and the life of a document"
force: explain
verb: illuminate
intention: model
view: synchronic
provenance: { type: function, id: structuring }
audience: [user]
reader: H+M
status: stable
---

This document builds the model behind where documents live and how they age, so the rules and defaults elsewhere read as consequences. The binding statements are in [`rules.md`](rules.md); the procedures in [`setup.md`](setup.md).

## Two systems, never one

Documentation is pulled in two incompatible directions. **Communication**: a hurried, non-expert reader must *find* what they came for. Beneficiary: a present reader; horizon: now. **Evidence**: someone must later produce what was decided, when, by whom, on what grounds. Beneficiary: a future examiner; horizon: the long term.

These command opposite orders. The order that lets you *browse* by the shape of your need scatters the traces of one activity across the tree; the order that keeps those traces together buries what the reader came to find. So "organize the docs" is two tasks: the **communication system** (a readable tree) and the **archival system** (provenance). Conflating them is the root failure of most wikis.

## Provenance: what belongs together

Ask *which documents belong together*. Not "those about the same subject" — **those that are traces of the same activity**. A change request, the decision it triggers, the test that validates it, the report on it share a **provenance**; their juxtaposition *is* the evidence. The operable distinction:

- **Function** — a permanent responsibility (reporting, security). It does not end. Docs are **synchronic**: kept current.
- **Project** — a bounded effort (a migration). It closes. Docs are **diachronic**: they freeze when it closes.

A change touching three functions is not filed three times: its provenance is the *project* that produced it; its bearing on the functions is a *relation*, not a location.

## Govern, and where it lives

Governing is not a third place; it is a *face* every activity carries. A govern-document is placed by the **domain it governs**, not by its register: a rule binding the user's writing is product content (in the `writing` function); the same force binding contribution to the project is the project's governance. `steering` is simply the activity whose domain is the project itself, so it holds its own know/do/govern.

A decision and the rule it installs are two documents, joined at the state/change seam below: the decision freezes with the effort that made it; the rule stays current with the activity it binds; the rule cites the decision.

Whether a decision that concerns only one activity is filed centrally or with that activity is the **transversal-vs-vertical** fork — irreducible, and fractal (a sub-project takes its governance with it). Declare a **governance axis** at the root — `central` or `local` — the way you declare the shelf axis, and record which activities a decision `concerns`. That bearing is a relation, not a location: the per-activity view is *generated* from `concerns`, never carved by moving frozen records.

## The topology carries the distinction

The two contexts you work in are the material projection of the two systems:

- **Docs in the project (in-repo)** — the project's provenance (frozen records) plus its local synchronic surface (README, architecture, reference).
- **Separate docs repo + submodules** — the cross-project communication tree, organized by business function, above the projects. A **submodule pinned to an exact commit *is* the archival bond** (provenance + fixity) made material: it ties a maintained reference to a frozen, dated project state.

## Shelf and catalogue

The reading surface needs **one intelligible tree** (the shelf — each item one place, ordered for browsing) *and* a **catalogue** over it (many access points — the frontmatter, read by the machine to *generate* indexes, never the reader's interface). A shelf admits one order, so the whole difficulty is choosing its **axis**, which must fit the mental map of the **dominant community**: business function for a cross-project repo, component/builder's path for in-repo code.

## The state/change seam

Almost every domain runs two artifacts in parallel: the document that states the present **state** (synchronic, belongs to the function, kept current) and the record that fixes a **change** (diachronic, belongs to the project, frozen). A change *updates* the state document and *is filed with* its project. Backward, the current state *is* the integral of past changes and can be re-derived; forward it fails — a proposal over open futures is the integral of nothing. The central discipline: **keep the derived state honest to its authoritative changes** — when you change a state, record the change (ADR, changelog) and never erase it.

## The life cycle

Coordinates engender trajectory: what **decides** freezes and is archived; what **commits** is re-issued in versions; what **describes** is maintained; what **proves** is re-run against preserved inputs. A record is never truly finished — an audit can requisition a note written to coordinate colleagues. (So do *not* pre-arm routine documents "for court": it destroys the innocence that would give them evidential value.) Retention defaults live in [`defaults.md`](defaults.md).

## In short

Two systems (communication tree, archival provenance), joined at the state/change seam. Provenance splits into function (synchronic, maintained) and project (diachronic, frozen). The topology embodies it: in-repo for the project, docs repo + pinned submodules for the cross-project layer. Choose the tree's axis for the dominant community; keep the derived state honest to its frozen changes.
