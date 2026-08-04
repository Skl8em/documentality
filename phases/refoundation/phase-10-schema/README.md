---
title: "Phase 10 — Reconcile governance & the frontmatter schema"
force: orient
intention: formative
view: diachronic
provenance: { type: project, id: phase-10-schema }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
hash: sha256:592511fe1881879b252c0f6ca3396eb646eff86115021560ffdbcb0a5245c074
---

Phase I's schema phase: reconcile the frontmatter to the refounded model, and enforce it on the Phase-09 lint harness.
It was in honest terms a **rewrite pass** — nearly every frontmatter in the catalogue changed — plus a **governance cleanup**.

What landed (detailed in [`plan.md`](plan.md)):

- **The two open ⚑ are closed.** `intention` is stored as the **coarse** family (`state` · `formative` · `suasive` · `affective`); `register` is **derived, never stored**.
  Both are now lint errors rather than warnings.
- **`register` re-founded** — `constitutive ? govern : direction-of-fit(force)`, with a new required, stored `constitutive: yes|no` carrying the markedness the old triad hid.
  The three `writing/forces/` doors are unchanged; only their foundation is ([ADR-030](register-derived-constitutive.md)).
- **The corpus swept** — 89 of 93 catalogued documents rewritten: fine `intention` → coarse, stored `register` removed, `constitutive` judged per document (21 `yes`, 72 `no`).
- **Content-hash fixity** — an optional `hash:` seals a frozen record; `scripts/hash_seal.py` mints, `scripts/hash_check.py` verifies, and the gate enforces ([ADR-031](content-hash-fixity.md)).
- **ADR tiering** — a decision earns an ADR only by installing a **standing obligation**; `CONTRIBUTING` relaxed accordingly, the register reviewed by receivability, ADR-019 demoted to a roadmap plan-changes note ([ADR-032](adr-tiering.md)).
- **`operationalizing` recorded** — the sixth function, ratified and enacted in the previous commit but never written to the register ([ADR-033](operationalizing-function.md)).
- **The gate grew two checks** — fixity, and a `git status --porcelain` assertion so untracked on-disk cruft can no longer pass a gate that reads only `git ls-files`.

Records:

- [plan.md — the detailed plan](plan.md)
- [ADR-029 — hosting: Codeberg canonical, GitHub mirror](hosting-codeberg-github-mirror.md)
- [ADR-030 — `register` derived, `constitutive` stored](register-derived-constitutive.md)
- [ADR-031 — content-hash fixity](content-hash-fixity.md)
- [ADR-032 — ADR tiering](adr-tiering.md)
- [ADR-033 — `operationalizing`, the sixth function](operationalizing-function.md)

Verification: `python3 scripts/check.py` passes — worktree clean, links resolve, frontmatter valid against the promoted schema, ULIDs valid and unique, filenames match slugs, every seal verifies, markdownlint zero.

Two departures from the plan, recorded rather than hidden.
The plan listed `operationalizing` as out of scope on the grounds that it was "still open, not ruled on" — but it had been ratified *and enacted* in the same commit that added the plan, so the shelf existed with no record, which `CONTRIBUTING` forbids; ADR-033 catches the register up.
And the plan did not mention the product prose, but a schema change that leaves `writing/frontmatter.md` describing the old model makes the product lie about itself, so the guidance was realigned with the schema.
