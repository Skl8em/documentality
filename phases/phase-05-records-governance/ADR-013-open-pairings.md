---
title: "ADR-013 — force × perlocution pairings are open, not constrained"
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

ADR-002 introduced the `perlocution` typology and, with it, a validation rule that *constrained* perlocution by force (`orient→locate`, …, "any other pairing is an error"), softened by one "sanctioned drift" (`account`+`model` for a postmortem). Naming a single sanctioned exception is self-defeating: it implies the rule enumerates every possible pairing, which is exactly the **definitiveness** the theory rejects. Illocutionary force and perlocutionary aim are **independent coordinates**; every combination is conceivable, some merely awkward. An `account` that explains, a `describe` that means to convince — these are legitimate, not violations.

## Options considered

- **Keep the hard constraint** — consequence: over-closes the model, contradicts "saturated, not closed", and forces genuine documents to be mislabelled.
- **Keep it but list more exceptions** — consequence: the same error, deferred; you can never enumerate the awkward-but-valid pairings.
- **Make the mapping a default, not a constraint** — consequence: the force still suggests a typical perlocution (useful for tooling and writers), but any pairing is allowed and meaningful.

## Decision

The force→perlocution mapping is a **default expectation**, not a rule. `perlocution` is an independent coordinate; **any pairing is permitted**. A validator may *surface* an unusual pairing for review; it never rejects one. We do not maintain a table of which pairings are possible. This refines — does not supersede — ADR-002 (the typology stands; only its constraint is loosened).

## Entail — what follows

- `write/frontmatter.md`: the validation rule is rewritten from "constrained / error / sanctioned drift" to "default expectation / surfaced, never rejected."
- `write/concepts.md`: the perlocution table's "Host forces" column is marked as *typical homes, not a whitelist*.
- No "sanctioned drift" language remains in maintained files; the frozen ADR-002 keeps its original wording (freeze discipline).
- General principle reaffirmed for future coordinates: state defaults and smells, not closed compatibility tables — be definitive only where a formal closure exists (e.g. direction of fit), never by fiat.
