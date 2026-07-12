---
title: "ADR-011 — decide gains a forward entail face (act / justify / entail)"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: phase-05-records-governance }
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
supersedes: null
superseded-by: null
written-at: v3
valid-for: v3
---

## Status

accepted — 2026-07-12

## Context and forces in play *(justify — backward)*

`decide` was modelled with a single generative verb, `justify` — the backward view that motivates a choice from its settled context. But a decision also *unrolls forward*: it changes things, commits us, and imposes work. That forward face was squeezed into a thin "Consequences accepted" section and easily left implicit, so readers could not tell what a decision required of them. The parent theory already names this shape — the classical act has **recitals** (whereas… = justify) and a **dispositif** (the operative provisions = the forward face) — and its own integral/derivative asymmetry: backward one *integrates* a settled past; forward one *differentiates* into future changes, which do not accumulate and are therefore more tentative.

## Options considered

- **Keep one verb (`justify`)** — consequence: the forward implications stay a weak afterthought.
- **Make implications a separate force** — consequence: over-fragments; the implications belong *to* the decision.
- **Give `decide` three named faces** (act / justify / entail), one force with three verbs — consequence: matches the theory's own "one force, several verbs" (ADR-005) and the recitals/dispositif structure.

## Decision

`decide` has three faces, each a verb: **`enact`** (the act — take the choice on record, e.g. the central register), **`justify`** (backward — motivate from context and options), **`entail`** (forward — unfold what the decision changes, commits, and requires). A decision record carries `justify` and `entail`; the register carries `enact`.

## Entail — what follows

- The `decide` stance (`../../../write/forces/govern-and-record/decide/README.md`) and its template must name the three faces and add an explicit **Entail** section (this ADR is written in that shape).
- `entail`'s failure mode is now nameable: leaving implications implicit, so no one knows what the decision requires of them — distinct from justify's failure (recording the verdict without the reasoning).
- The `entail` section is where a decision spawns downstream `commit`/`mandate`/`instruct`, or reopens a `propose`; those links start here.
- Because the future does not accumulate, an `entail` is a projection, not a proof — write it as defeasible, not as settled fact.
