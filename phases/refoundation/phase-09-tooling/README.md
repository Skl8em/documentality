---
title: "Phase 09 — Tooling: enforce the conventions, ready the catalogue"
force: orient
register: know
intention: locate
view: diachronic
provenance: { type: project, id: phase-09-tooling }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
---

Phase I's tooling phase: stand up the machinery that **enforces the conventions we have already decided** and makes the schema work of Phase 10 efficient and meaningful.
It is deliberately placed *before* the schema reconciliation: the lint harness built here is what Phase 10 fills in.

What landed (detailed in [`plan.md`](plan.md)):

- **Reproducible environment** — a Nix `devShell` (`flake.nix`/`flake.lock`) pinning `markdownlint-cli2`, node, python, and git; install/usage in [`../../../steering/environment.md`](../../../steering/environment.md).
- **Unified markdownlint** — one ruleset shared by the CLI and the VSCode (David Anson) extension: title in the frontmatter (never `# …`), a custom `sentence-per-line` rule for ADR-021, and a deliberate take-over of the defaults; the corpus was reflowed to zero violations.
- **Frontmatter linting (a safe starter)** — `scripts/frontmatter_lint.py` + `schema/frontmatter.schema.json`: errors on the settled invariants, warns on the contested ones (→ Phase 10).
- **ULID + slug identifiers** — the scheme is [decided](01KYYTENT6PXHBZCGVGJ9YN9YX-ulid-identifiers.md) (ADR-028): `scripts/ulid.py` mints, `scripts/ulid_check.py` verifies, new records are `<ulid>-<slug>.md`; the migration of existing count-named records is deferred (technical debt) behind `scripts/rename_doc.py`, the verified safe-rename tool.
- **One gate** — `scripts/check.py` runs all four checks (always the pinned markdownlint), wired into a pre-commit hook and CI.

- [plan.md — the detailed plan](plan.md)
- [ADR-028 — ULID + slug identifiers](01KYYTENT6PXHBZCGVGJ9YN9YX-ulid-identifiers.md)

Verification: `python3 scripts/check.py` passes (markdownlint 0, frontmatter clean, ULID valid, links resolve), both inside and outside the devShell.
The two open ⚑ (intention coarse/fine, register stored/derived) are handed to Phase 10 on this harness.
