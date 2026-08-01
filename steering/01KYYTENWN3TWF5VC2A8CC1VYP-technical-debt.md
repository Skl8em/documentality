---
title: "Technical debt — known gaps, tracked so they are not forgotten"
id: 01KYYTENWN3TWF5VC2A8CC1VYP
slug: technical-debt
force: describe
verb: specify
register: govern
intention: state
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor, decider]
reader: H+M
status: draft
---

Known technical debt: things we chose to defer, each with *why* and *how to resolve*.
This is a **current** register (a debt is removed when it is paid), distinct from [`open-questions`](open-questions.md) (undecided questions) and the roadmap (planned phases).

## ULID migration of existing records

**What:** existing records still use sequential-count names — the ADRs (`ADR-001`…`ADR-027`) and the phase folders (`phase-01-foundation`…`phase-09-tooling`) — while new records are `<ulid>-<slug>.md` per the [ULID identifiers decision](../phases/refoundation/phase-09-tooling/01KYYTENT6PXHBZCGVGJ9YN9YX-ulid-identifiers.md).
The corpus therefore carries two naming schemes at once.

**Why deferred:** renaming every count-named file and folder rewrites cross-references corpus-wide — a large, link-rotting event.
We do it only once a trusted **safe-rename refactoring script** exists, so the rename is mechanical and verified, not hand-done.

**How to resolve:** with `scripts/rename_doc.py` (the safe-rename capacity built later in Phase 09), migrate each legacy record to `<ulid>-<slug>.md`: mint a ULID (ADRs chronological from first-commit time; phases ordinal from an `order` key), write `id`/`slug` into frontmatter, rename, and let the script rewrite all references; `linkcheck` + `ulid_check` gate it.

## Linter-grandfathered content

**What:** `phases/naive-sketch/**` (pre-ADR-021 records), `imagining/**` (informal Phase-II notes), and the blind-test transcripts are excluded from markdownlint / the frontmatter linter.

**Why:** they predate the current conventions or are not authored prose; forcing them into compliance would be churn without value.

**How to resolve:** bring a file into the catalogue (frontmatter + one-sentence-per-line) and remove it from the ignore lists when it stops being historical/informal — case by case, not in bulk.
