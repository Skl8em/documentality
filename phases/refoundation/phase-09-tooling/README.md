---
title: "Phase 09 — Tooling: enforce the conventions, ready the catalogue"
force: orient
intention: formative
view: diachronic
provenance: { type: project, id: phase-09-tooling }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
hash: sha256:5a2cd78053ef898cf71f3de311dc061db2cfb993748a705b68bcc8d2a7e4fd52
---

Phase I's tooling phase: stand up the machinery that **enforces the conventions we have already decided** and makes the schema work of Phase 10 efficient and meaningful.
It is deliberately placed *before* the schema reconciliation: the lint harness built here is what Phase 10 fills in.

What landed (detailed in [`plan.md`](plan.md)):

- **Reproducible environment** — a Nix `devShell` (`flake.nix`/`flake.lock`) pinning `markdownlint-cli2`, node, python, and git; install/usage in [`../../../steering/environment.md`](../../../steering/environment.md).
- **Unified markdownlint** — one ruleset shared by the CLI and the VSCode (David Anson) extension: title in the frontmatter (never `# …`), a custom `sentence-per-line` rule for ADR-021, and a deliberate take-over of the defaults; the corpus was reflowed to zero violations.
- **Frontmatter linting (a safe starter)** — `scripts/frontmatter_lint.py` + `schema/frontmatter.schema.json`: errors on the settled invariants, warns on the contested ones (→ Phase 10).
- **ULID + slug identifiers** — the scheme is [decided](ulid-identifiers.md) (ADR-028): the ULID is the frontmatter `id` (minted by `scripts/ulid.py`, verified by `scripts/ulid_check.py`), filenames stay `<slug>.md` (linted by `scripts/slug_check.py`).
  The convention is kept open with tools both ways — `scripts/slugify_names.py` (→ `<slug>.md`) and `scripts/migrate_ids.py` (→ `<slug>-<ulid>.md`) — both on the safe-rename core (`scripts/rename_doc.py`).
- **One gate** — `scripts/check.py` runs all five checks (always the pinned markdownlint), wired into a pre-commit hook and CI.

- [plan.md — the detailed plan](plan.md)
- [ADR-028 — ULID + slug identifiers](ulid-identifiers.md)

Verification: `python3 scripts/check.py` passes (markdownlint 0, frontmatter clean, ULID valid, links resolve), both inside and outside the devShell.
The two open ⚑ (intention coarse/fine, register stored/derived) are handed to Phase 10 on this harness.
