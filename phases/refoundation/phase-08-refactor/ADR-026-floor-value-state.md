---
title: "ADR-026 — The perlocution/intention floor value is `state`, not `none`"
force: decide
register: govern
intention: suasive
view: diachronic
provenance: { type: project, id: phase-08-refactor }
concerns: [theory, writing, structuring, steering]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
---

## Status

accepted — 2026-07-25

## Context and forces in play *(justify)*

ADR-015 established that perlocution has **no zero**: every inscription carries a constitutive floor, and an *intention* may rise above it.
But the value we gave that floor — `none` — misnames it as *absence*, which is exactly what ADR-015 denies.
The floor is not nothing.
Even at its minimum the act **establishes a state** in the reader: an uptake, a representation the reader now holds that was not held before.
And by selecting what it says, it **casts a shadow on the unsaid** — the silences that are themselves part of the act (Bowker & Star).
`none` invites the reader of the schema to think "the reader is untouched"; `state` invites them to think "a state was set, nothing more was aimed at" — which is what the floor actually is.

## Decision

Rename the floor value from `none` to **`state`**.
The refounded `intention` set is `state` · `formative` · `suasive` · `affective`, where **`state`** = the floor is established and no aim rises above it (the act serves; it does not try to move the reader).
The v3 `perlocution: none` floor maps to `state` under the vocabulary refactor.

## Entail — what follows

Updated now: the frontmatter schema draft (`intention` value, description, and Decision 1's coarse set become `{state, formative, suasive, affective}`) and the derived vocabulary in `self-application.md`.
Deferred to the Phase-08 vocabulary pass: the twelve v3 `perlocution: none` frontmatters and the typology prose in `write/concepts.md`, `write/frontmatter.md`, `write/choosing.md`, and the force `README`s — they convert field-and-value together (`perlocution: none` → `intention: state`).
Left untouched: `power: none`, a different zero (no sanction), not the perlocutionary floor.
This **refines** ADR-015 (the floor concept is unchanged; only its label) and clarifies Decision 1's coarse option (the floor now has an honest name).

Note a soft collision to watch: `state` here (the perlocutionary floor) is not the *synchronic maintained state* of `view` and the state/change seam.
Different sense, same word.
If it proves confusing in practice, revisit with an alternative (`posit`, `imprint`, `ground`) — but `state` is adopted for now, per the maintainer's call.
