---
title: "Phase 08 — workstreams A–I (plan and execution)"
force: account
verb: report-against
register: govern
intention: state
view: diachronic
provenance: { type: project, id: phase-08-refactor }
concerns: [theorising, writing, structuring, steering, imagining]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
---

The record of *how* Phase 08 was carried out: the nine workstreams the refactor was cut into (A–I), each landed as one commit, reported against the plan.
The *why* of each decision is in the ADRs ([024](ADR-024-producer-shelf.md), [025](ADR-025-governance-axis.md), [026](ADR-026-floor-value-state.md), [027](ADR-027-gerund-naming.md)); the summary of what changed is the phase [`README.md`](README.md); this document is the execution log.

## Decisions locked during execution

Three forks were settled with the maintainer before or during the work:

- **Naming (gerund rule).** Move the folders to their gerund `provenance.id` (not the reverse): `write→writing`, `structure→structuring`, and also `theory→theorising`, `imagine→imagining`. Recorded as [ADR-027](ADR-027-gerund-naming.md).
- **`theory/` was a nested git repo.** Absorbed into the main repo by a **history-preserving subtree merge** (`git merge -s ours --allow-unrelated-histories` + `read-tree --prefix=theorising/`), so the essays' five-commit history is kept; the inner `.git` was removed.
- **Intention conversion depth.** Rename the field `perlocution → intention` and `none → state` only, **keeping** the fine values `locate/model/enable/convince`. The coarse-vs-fine encoding is ⚑ Decision 1, routed to Phase 09.

## Scope boundary (Phase 08 vs 09)

Phase 08 did the *conceptual* refounding in prose + the committed value conversion (`none → state`, ADR-026) + the structural moves.
It did **not** collapse `intention` to the coarse set, add a stored `register` field to the v3 files, or re-spec `distance`/`power` values — those, with the two open ⚑ (intention coarse/fine; register stored/derived), are Phase 09.
The forks are tracked in [`../../../steering/open-questions.md`](../../../steering/open-questions.md).

## The nine workstreams

Each was one commit on the `phase-08-refactor` branch (A spans three: the folder/phase moves, the theory subtree merge, and the `imagine` rename).

| # | Workstream | What landed |
|---|---|---|
| **A** | Structural moves | Rename the five function folders to gerund ids; nest `phases/` under `naive-sketch/` (01–05) and `refoundation/` (06–08); absorb the `theory` nested repo under `theorising/`, preserving history. |
| **B** | Link + folder-name fix | Add `scripts/linkcheck.py` (the phase-close link gate); rewrite link targets and current-tense inline folder mentions for the renames + era nesting, including depth-sensitive relatives inside moved phase folders; fix a few pre-existing broken links in `writing/tutorial.md`. |
| **C** | Refound the guidance vocabulary | `perlocution → intention` (floor + aim) across the product prose; forces as recognized cells; know/do/govern as a register gloss; `recommend`/`entail` as extensions; the machine as the recipient relation at its limit; full `steering/ARCHITECTURE.md` rewrite. |
| **D** | Frontmatter conversion | Convert the `perlocution` field to `intention` (`none → state`) on the live docs; drop stale `written-at`/`valid-for` v3 markers; fix stale provenance ids (`onboarding → writing`, `imagine → imagining`). |
| **E** | The nine remaining forces | Author `explain`, `describe`, `teach`, `recommend`, `mandate`, `commit`, `propose`, `prove`, `account` under `writing/forces/` (stance `README.md` + `template.md`); all twelve forces now built. |
| **F** | Retire `_legacy/` | Remove the migration source and the obsolete "Working with `_legacy/`" section from `CONTRIBUTING`. |
| **G** | Retire `structuring/applied.md` | Remove the stale v3 self-reading (superseded by `self-application.md`); repoint its two live references. |
| **H** | Add `steering/open-questions.md` | The live deliberation register (⚑ intention coarse/fine, ⚑ register stored/derived → Phase 09; the `_legacy`/nine-forces debt and the gerund rule closed). |
| **I** | Close-out | Record ADR-027; mark Phase 08 done across the roadmap, changelog (v4.0-alpha.4), phase README, eras map, and the ADR register. |

## Verification (the phase-close gate)

- **Links:** `scripts/linkcheck.py` reports zero broken relative links.
- **Vocabulary:** no live document carries the `perlocution` frontmatter field; no `intention: none` remains.
- **Forces:** all twelve force folders exist with `README.md` + `template.md`.
- **Retirements:** `_legacy/` and `structuring/applied.md` gone; `steering/open-questions.md` present; `theory/` replaced by `theorising/` with history intact.
- **Tree:** eras are physical folders; function folders are the gerund ids.

## Honest limit

Reorganising documentation rots links and displaces records (ADR-025's honest limit, felt again here).
The two physical moves — the folder renames and the era nesting — broke links **inside frozen phase records** as well as live ones.
Per the maintainer's call, *path targets* were fixed repo-wide, including inside frozen records (link preservation, not a rewrite of any record's claims), so the corpus stays internally consistent and passes its own link gate — one coarse aligned move rather than scattered edits.
