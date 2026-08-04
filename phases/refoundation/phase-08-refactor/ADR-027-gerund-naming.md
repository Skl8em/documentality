---
title: "ADR-027 — Function folders and provenance ids take the gerund form"
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-08-refactor }
constitutive: yes
concerns: [theorising, writing, structuring, steering, imagining]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:b696fcf66f57194bcdfd05207472a0bbc11acd6c79de4b7925dfc1825d07db06
---

## Status

accepted — 2026-08-01

## Context and forces in play *(justify)*

The roadmap carried a standing mismatch to reconcile: the source folders were `write/` and `structure/`, but their `provenance.id` values were `writing` and `structuring` (ADR-024 deferred the fix to Phase 08).
Looking across all five functions, the names were inconsistent in *form*: two imperatives (`write`, `structure`), one bare noun (`theory`), one imperative (`imagine`), and one gerund (`steering`).

A `provenance.id` names a **standing activity** — a permanent responsibility that does not end (`foundation.md` §4).
The grammatical form that names an ongoing activity is the **gerund** (the *-ing* form): *steering*, *writing*, *structuring* — the doing, not a command (`write`) nor the object of the doing (`theory`).
So the mismatch was not "which of folder-name or id is right" but that the *form* should be the gerund throughout, and the folder should equal the id (one name per function, since a function *is* a provenance).

## Decision

1. **Function folders and their `provenance.id` take the gerund form**, and the folder name equals the id.
2. Enact the renames: `theory → theorising`, `write → writing`, `structure → structuring`, `imagine → imagining`; `steering` already conforms.
3. This resolves the roadmap's `write/↔writing`, `structure/↔structuring` mismatch by moving the folders to the ids (not the reverse), because the gerund id is the correct name.

## Entail — what follows

- The five function folders are renamed and every `provenance.id` and inbound path/link updated across the live tree; the link gate (`scripts/linkcheck.py`) reports zero broken relative links.
- `theory/` was a **nested git repository**; it is absorbed into the main repo by a **history-preserving subtree merge** (`git merge -s ours --allow-unrelated-histories` + `read-tree --prefix=theorising/`), so the essays' five-commit evolution is kept, and the inner `.git` is removed.
- The rule is stated as convention in `steering/CONTRIBUTING.md` (the provenance-id rule) and reflected in `steering/ARCHITECTURE.md`.
- Frozen phase records had their *path targets* updated to survive the moves (link preservation), but no substantive wording changed; this follows ADR-025's honest limit that reorganisations rot links, met here by fixing them as one coarse aligned move.

Refines ADR-024 (which deferred this naming mismatch) and ADR-018 (the producer shelf: a function is a provenance, so its folder and id are one name).
