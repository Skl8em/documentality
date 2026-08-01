---
title: "Decision — ULID + slug identifiers (scheme, and a deferred migration)"
id: 01KYYTENT6PXHBZCGVGJ9YN9YX
slug: ulid-identifiers
force: decide
register: govern
intention: suasive
view: diachronic
provenance: { type: project, id: phase-09-tooling }
concerns: [steering, writing, structuring, theorising, imagining]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
---

## Status

accepted — 2026-08-01.
This is the first record to carry the scheme it decides: it is named `<ulid>-<slug>.md` and carries `id`/`slug`.

## Context and forces in play *(justify)*

Records were identified by a **sequential count** — `ADR-027`, `phase-08` — in their filenames, titles, and cross-references.
A count is a coordination bottleneck and a merge-conflict magnet, and it bakes ordering into the name, so re-ordering (as when Phase 09 was inserted before the schema phase) forces a renumber.
We want a stable, coordination-free identifier that pairs with a human slug.

Two record kinds mean *order* differently (settled with the maintainer):

- **ADRs are append-only and chronological** — creation order *is* their order.
- **Phases carry an intentional order we rearrange** — a wall-clock identifier would fix the wrong order.

## Decision

1. **Canonical identity is a ULID** carried as `id:` in the frontmatter, with a human `slug:` (D-a).
   A ULID is 128 bits — a 48-bit timestamp prefix (sortable) plus 80 bits of randomness — encoded as 26 Crockford-base32 characters.
2. **Two minting modes** (D-e): ADRs mint from the real creation time (chronological); phases mint from an explicit `order` sort-key stored in frontmatter, gap-spaced so a phase can be inserted at a midpoint (`x < z < y`).
3. **On-disk target is `<ulid>-<slug>.md`** — the count leaves the filename entirely (the maintainer's call).
   The display ordinal a human still wants ("the 28th decision") is **generated** from ULID order, never stored (D-c).
4. **References**: human relative links for reading (they resolve and pass `linkcheck`), with `id` as the stable machine key a generated index can map to a path (D-d).
5. **The migration of existing records is deferred.** Renaming every `ADR-NNN`/`phase-NN` file and folder is a large link-rewriting event; we do it only once a trusted **safe-rename refactoring script** exists (built later this phase).
   Until then: **new documents are created as `<ulid>-<slug>.md`; existing count-named records are left in place and tracked as technical debt.**

## Entail — what follows

- `scripts/ulid.py` (mint, two modes) and `scripts/ulid_check.py` (a safe-starter verifier: it validates ULID-named records and *notes*, without failing on, legacy count-named ones) are added.
- This decision and the technical-debt tracker are the **first ULID-named records**; further new records follow suit.
- The ADR register's ordinal becomes a generated display number; new rows link to the ULID file.
- The mass migration is tracked in [`../../../steering/technical-debt`](../../../steering/01KYYTENWN3TWF5VC2A8CC1VYP-technical-debt.md) and unblocked by `scripts/rename_doc.py` (the safe-rename capacity).

## Honest limit

For a while the corpus carries **both** naming schemes — new records as `<ulid>-<slug>`, legacy records as `ADR-NNN`/`phase-NN`.
That mixed state is the cost of deferring the rename until it can be done safely, and it is the debt the tracker exists to keep visible.
