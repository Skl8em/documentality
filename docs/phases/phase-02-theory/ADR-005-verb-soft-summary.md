---
title: "ADR-005 — verb is a soft summary; store only when it diverges"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: phase-02-theory }
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

accepted — 2026-07-11

## Context and forces in play

`verb` initially duplicated `force` one-to-one in every template, which made it look redundant. But the verb's value is real when it *diverges* from the force name (decide→*justify*), and a force can host several verbs (account→*report-against*/*diagnose*/*log*).

## Options considered

- **Drop `verb`** — consequence: loses the generative handle that tells the writer the centre of gravity.
- **Keep one verb per force everywhere** — consequence: redundant when the verb equals the force.
- **Keep `verb` as the soft summary of the whole coordinate tuple, stored only when it diverges** — consequence: expressive and non-redundant.

## Decision

`verb` is the human-facing summary of the occupied cell in the coordinate space. Store it only when it diverges from the force name for a **perlocutionary** (a) or **illocutionary-internal** (b) reason. Do **not** store a verb for a mere recipient shift (c) — that is `distance`/`power`.

## Entail — what follows

- Some documents carry no `verb`; that is correct, not an omission.
- Recipient variants (prove→*attest*) do not spawn verbs — they are `distance`/`power`, avoiding a proliferation of near-synonyms.
