---
title: "Decision — ULID + slug identifiers (ULID in frontmatter, `<slug>.md` filenames)"
id: 01KYYTENT6PXHBZCGVGJ9YN9YX
slug: ulid-identifiers
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-09-tooling }
constitutive: yes
concerns: [steering, writing, structuring, theorising, imagining]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:70f33ded451f193c33673e7cf1c71896708d77e011ee0259eee8cce85881919b
---

## Status

accepted — 2026-08-01.
This is among the first records to carry the scheme it decides: its identity is the ULID in frontmatter (`id`), and its filename is its `slug` (`ulid-identifiers.md`).

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
3. **Filenames stay `<slug>.md`** — the hyphenized slug, with the ULID in the frontmatter, *not* in the filename.
   Uniqueness is checked against the frontmatter `id`, and a lint (`scripts/slug_check.py`) enforces filename stem == `slug`.
   The count leaves the name (no `ADR-NNN`); the display ordinal a human still wants ("the 28th decision") is **generated** from ULID order, never stored (D-c).
4. **References**: human relative links for reading (they resolve and pass `linkcheck`), with `id` as the stable machine key a generated index can map to a path (D-d).
5. **The naming convention is kept open, with tooling in both directions.** `scripts/slugify_names.py` enforces the `<slug>.md` convention; `scripts/migrate_ids.py` produces `<slug>-<ulid>.md` (slug first) should global uniqueness *in the filename* ever be wanted.
   Existing count-named records (`ADR-NNN`, `phase-NN`) are left as-is for now; adopting `id`/`slug` on them is an optional, separate step.

## Entail — what follows

- `scripts/ulid.py` mints ULIDs (two modes); `scripts/ulid_check.py` validates that every frontmatter `id` is a valid, unique ULID; `scripts/slug_check.py` lints filename == `slug`.
- `scripts/slugify_names.py` (→ `<slug>.md`) and `scripts/migrate_ids.py` (→ `<slug>-<ulid>.md`) are the two naming-direction tools, both on the safe-rename core (`scripts/rename_doc.py`).
- This decision and the technical-debt tracker are the **first records to carry `id`/`slug`**, as `<slug>.md`; further records follow suit.
- The ADR register's ordinal becomes a generated display number.
- The open convention and the optional adoption of ids on legacy records are tracked in [`../../../steering/technical-debt`](../../../steering/technical-debt.md).

## Honest limit

For a while the corpus carries **two naming schemes** — new records as `<slug>.md` with an `id` in frontmatter, legacy records still `ADR-NNN`/`phase-NN`.
That mixed state is deliberate: the convention is kept open, and the tools exist to move any record either way when we choose.
