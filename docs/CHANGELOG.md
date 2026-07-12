---
title: "Changelog of the system"
force: account
verb: report-against
perlocution: none
view: diachronic
provenance: { type: function, id: steering }
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
written-at: v3
valid-for: v3
---

History of the documentation system itself. Append-only; each entry is dated-fixed. Design rationale for each line lives in the matching ADR — listed in the register [`ADR.md`](ADR.md), written in full in its [`phases/`](phases/README.md) folder.

## [v3.2] — records & governance

- **Changed:** decision records regrouped **by phase** (`docs/phases/`) instead of a flat `decisions/` pile — provenance filing, not force filing. (ADR-012)
- **Added:** the central register `docs/ADR.md` (the `enact` act) and a permanent `steering` function owning the governance docs; frozen records now belong to their `phase-NN` project. (ADR-012)
- **Changed:** `provenance` on `docs/` split into `steering` (maintained) and `phase-NN` (frozen), replacing `maintenance`/`v3-redesign`. (ADR-012)
- **Added:** `decide` now has a forward **`entail`** face (act / justify / entail); the stance and template carry an explicit Entail section. (ADR-011)
- **Deprecated:** `docs/decisions/` — redirected, not erased.

## [v3.1] — content / docs disentangled

- **Changed:** split the *product* (content for users) from `docs/` (the repo's own internals for contributors). Root `dominant-community` corrected from `contributor` to `user`. (ADR-010)
- **Changed:** the product's axis renamed from `activity` to **scope** (one document vs the whole corpus). (ADR-010)
- **Changed:** `provenance` now names the maintaining function (`onboarding`/`writing`/`structuring`/`maintenance`) instead of a blanket `doc-system`. (ADR-010)
- **Added:** `docs/` with `ARCHITECTURE`, `CONTRIBUTING`, `CHANGELOG`, and this decision log.

## [v3] — self-similar reorganization

- **Changed:** flat `writing.md` / `structure.md` replaced by `write/` and `structure/`, each split by force (explain / instruct / recommend / mandate / describe). (ADR-007)
- **Added:** forces grouped under three doors in `write/forces/{know,do,govern-and-record}/`. (ADR-007)
- **Added:** `tutorial.md` — a `teach` on-ramp; obligations enforced by validation, not reading order. (ADR-009)
- **Added:** `axis` / `dominant-community` declared at each tree root. (ADR-008)
- **Moved:** the audience model into `structure/` (premise of the communication system). (ADR-006)

## [v2] — theory sharpening

- **Changed:** `formative: true|false` replaced by the `perlocution` typology (`locate`/`model`/`enable`/`convince`/`none`); `prove` and `decide` reclassified as `convince`. (ADR-002)
- **Added:** `recommend` as the twelfth force, on the deontic gradient instruct → recommend → mandate. (ADR-003)
- **Removed:** the `diataxis` frontmatter field — re-derived from `force` × `perlocution`. (ADR-004)
- **Clarified:** `verb` is a soft summary of the coordinate tuple; stored only when it diverges. (ADR-005)

## [v1] — foundation

- **Added:** the inscribed-act reframe — a document is an act with a `force`, and the force generates the writing. Eleven forces, move structures, readability patterns, frontmatter catalogue. (ADR-001)
