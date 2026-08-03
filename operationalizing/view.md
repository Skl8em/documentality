---
title: "view — maintained state vs frozen change, made a coordinate"
force: explain
intention: formative
view: synchronic
provenance: { type: function, id: operationalizing }
constitutive: no
audience: [contributor, decider]
reader: H+M
status: draft
---

**The apport.**
`view: synchronic | diachronic`, one value per document.

**What it operationalizes.**
The *state/change seam* of the documentary system (essay 3): almost every domain runs two artifacts in parallel — a document that states the present **state** (kept current) and a record that fixes a **change** (frozen once made). The theory describes the seam; it does not, by itself, put a field on every file.

**Why we reified it.**
Placement, life cycle, and provenance all key off this one distinction, so making it explicit lets the rest be *derived* rather than guessed:

- `synchronic` = a maintained state → it stays **current**, and its provenance is a **function** (`synchronic ⇒ provenance.type: function`).
- `diachronic` = a frozen change → it **freezes** when its effort closes, and its provenance is *whatever produced it* (a project, or a function's change-stream).

**Alternatives considered.**
Infer the seam from `status` or from `provenance.type` — rejected: too implicit, and it hides the seam the theory says is load-bearing. A three-value `view` (adding "pending") — rejected: a deliberation is a *current* document that decants into frozen ones, so `synchronic` already covers it.

**The work it does.**
Gates freeze-vs-current; drives the split between the communication surface (current) and the archive (frozen); lets a generator know what may be re-ordered and what must be preserved.

The *check* that `synchronic ⇒ function`, and the freezing discipline, live in the IT tools (the frontmatter linter) — not here.
