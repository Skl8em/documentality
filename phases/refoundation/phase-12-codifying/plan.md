---
title: "Phase 12 codifying — the detailed plan"
force: propose
verb: argue
intention: suasive
view: synchronic
provenance: { type: project, id: phase-12-codifying }
constitutive: no
concerns: [steering, operationalizing, writing, codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

Phase 11 hardened the tooling and left it unexplained.
This phase gives the tooling a shelf, closes the account Phase 11 opened and never paid, and makes the failure self-detecting so it cannot happen a third time.

## Why this phase exists

This is the second time, not the first.

[Phase 10's own closing README](../phase-10-schema/README.md) records catching itself mid-close: "a schema change that leaves `writing/frontmatter.md` describing the old model makes the product lie about itself, so the guidance was realigned with the schema" — an unplanned departure, named and fixed before the phase closed.

Phase 11 made a larger operational change — closed the frontmatter vocabulary, replaced the hand-rolled parser, moved the schema's source of truth from JSON to YAML, added referential integrity — and did not run that check.
Verified, not suspected:

- [`writing/frontmatter.md`](../../../writing/frontmatter.md), the user-facing spec (`audience: [user]`), never states the vocabulary is now closed, never says an optional field needs a rationale to exist, and still doesn't point at `schema/frontmatter-rules.yaml` as the real source of truth.
- [`steering/ARCHITECTURE.md`](../../../steering/ARCHITECTURE.md), the contributor-facing "why is it built this way," still says schema reconciliation *is* Phase 10 and never mentions Phase 11 — not the YAML/JSON split, not why referential integrity needed its own workstream.
  Its provenance map is stale even for `operationalizing`, adopted two phases earlier.
- [`steering/CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md) has no mention of `scripts/`, the gate, or how a maintainer extends any of it.
- Phase 11 closed with no `README.md` narrating what landed and why — every phase from 08 on has one — no consolidated closing changelog entry (four scattered T-task entries instead, the pattern every earlier phase avoided), and none of the three ADRs its own plan named as owed at close.
- `steering/roadmap.md` still tags Phase 11 *(next)*.

Twice is a pattern: the plan's workstreams and its verification checklist were both pure mechanism, so nothing in the process ever asked whether the mechanism got explained, and nothing caught its absence.

The immediate trigger for this phase: naming what shelf *should* have explained the tooling surfaced that [ADR-033](../phase-10-schema/operationalizing-function.md) already named the missing piece and never built it.
Its own chain diagram —

```text
theorising → operationalizing → structuring / writing → designing → IT tools
```

— has a fourth downstream link, "IT tools," that has never had a folder, a provenance owner, or an account of its own reasoning. `scripts/`, `schema/`, and the gate are real apparatus, argued nowhere, owned by no function. `operationalizing/view.md`'s own closing line says as much: the check that a coordinate holds "live[s] in the IT tools (the frontmatter linter) — not here."

## Workstreams

| # | Workstream | Output |
|---|---|---|
| **T1** *(done)* | **Adopt `codifying`**, in three ordered steps. **(a) Map its communities** — run the structuring front-end on the tooling itself: who reads about it, what each needs, at what `distance`. Candidates, to be confirmed or cut rather than assumed: the author who only runs the gate and must decode an error; the maintainer who extends a validator; the adopter who installs and configures it in another project (real only once a second consumer exists); the machine that runs the gate and reads its output (`reader: M`, so messages must be self-sufficient). Roles are mostly one person wearing hats, so `distance` (newcomer vs veteran) drives the split, not identity. Decide whether a refined `audience` role such as `maintainer` is declared in `schema/frontmatter-rules.yaml` or left as the warning the linter already emits, and revisit the "contributor ≈ user" premise behind the deferred reader surface (`ARCHITECTURE.md`, `foundation.md` §6). **(b) Draw the engine/config seam** — classify every script as generic engine or repo-specific, and move the specifics (`IGNORE_PREFIXES` in `frontmatter_lint.py`, `REGISTER_PATH` and the ADR-register format assumed by `ulid_check.py`, the hard-coded check list in `check.py`) into the rules file or a small config, so the tooling could be extracted later at low cost. **(c) Adopt and explain** — a seventh function, same shape as ADR-033: its own ADR, a `codifying/README.md` orient, and fiches split by the audiences step (a) settled, for apparatus that has never been argued in prose: the gate's architecture (why `check.py` sequences every check into one property, the thing Phase 09 built and nothing since has explained), the YAML-source/generated-JSON split, and referential integrity (why supersession must be symmetric, why a dangling pointer is a hard error). Update the function set everywhere it's enumerated: `foundation.md`, `CONTRIBUTING.md`'s shelving rule, `ARCHITECTURE.md`'s provenance map. | [community map](community-map.md), [engine/config seam](engine-config-seam.md), [ADR-035](codifying-function.md) with the [`codifying/`](../../../codifying/README.md) orient and three fiches, the function set at seven — and, from the machine-reader check the definition of done asks for, an [audit of the gate's messages](error-message-audit.md) |
| **T2** *(done)* | **Close Phase 11's account.** The three candidate ADRs Phase 11's plan named at close and never wrote (closed vocabulary + reason-per-field; YAML-as-source/JSON-as-generated; unstarted-work-never-numbered), each checked against the ADR-032 tiering test; `phases/refoundation/phase-11-tooling-hardening/README.md` narrating what landed and why, on the model of Phase 10's; `writing/frontmatter.md` rewritten to state the vocabulary is closed and name `schema/frontmatter-rules.yaml` as the source of truth — a real paragraph, not a silent field-table edit; the roadmap row flipped and its `phase:` field bumped. **Also, from T1's hand-off:** `steering/ARCHITECTURE.md`'s prose reconciled — it still says schema reconciliation is Phase 10 and never mentions Phase 11 or points at `codifying/`, and no other workstream owned it; and the `phases/README.md` index row for Phase 11 corrected. The YAML-source ADR must also answer a question T1's schema fiche raised: does the generated JSON earn its keep? Its only reader is `frontmatter_lint.py`, which already needs `pyyaml`, so collapsing to one file loaded through `StrictLoader` is a live option, not a settled loss. | three ADRs in Phase 11's folder — [ADR-036](../phase-11-tooling-hardening/closed-frontmatter-vocabulary.md), [ADR-037](../phase-11-tooling-hardening/yaml-source-generated-json.md), [ADR-038](../phase-11-tooling-hardening/unstarted-work-unnumbered.md) — each passing the ADR-032 test, ADR-037 ruling the generated JSON stays and saying when that lapses; [the Phase 11 README](../phase-11-tooling-hardening/README.md); `writing/frontmatter.md` and `steering/ARCHITECTURE.md` reconciled; roadmap and index flipped. Found on the way and left as debt: the closed-vocabulary rule has no fixture |
| **T3** | **Make the gap self-detecting.** Both failures were the same shape: a change to `scripts/` or `schema/` landed with no paired change to anything a human reads for understanding, and nothing noticed. Extend `check.py` with a structural check: a diff touching `scripts/**` or `schema/**` and none of `writing/`, `structuring/`, `operationalizing/`, `codifying/`, `steering/ARCHITECTURE.md` fails the gate. This workstream is itself an act of codifying — the rule this phase argues for, applied to itself before the phase closes. **Also, from T1's hand-off:** `steering/CONTRIBUTING.md` still says nothing about `scripts/`, the gate, or how a maintainer extends either (the Phase 11 gap `plan.md` named, which T1(c) touched only for the shelving rule). The paired-change rule is a binding rule, so it lands there, stated once, together with the two things a contributor needs to comply: run the gate before committing, and where a new check is registered (`docsys.yaml`) and what it must bring (fixtures, a `fix:` clause). | a paired-change gate check; `CONTRIBUTING.md` states the rule and how to extend the tooling |
| **T4** | **Pay the debts T1 recorded** in [`technical-debt.md`](../../../steering/technical-debt.md) — the holes the `codifying/` fiches now state in their "does not establish" sections, so leaving them open leaves the shelf describing a known weakness. (i) `ulid_check.py` accepts a cycle and a self-supersession: two failing fixtures first, then the check. (ii) A register whose configured row shape matches nothing passes silently: it must fail, with a fixture. (iii) `slug_check.py`, `linkcheck.py` and `hash_check.py` build their messages inline in `main()`: extract pure functions, add fixtures, assert the `fix:` clause. (iv) The frozen-record definition in `hash_seal.py` duplicates the schema's status list: either rule it into the schema (widening the vocabulary — a ruling, checked against ADR-032) or keep it in code with a fixture that fails when the two lists disagree; not silently either. Each fix updates its fiche and its debt entry in the same change, which is the first real use of the pairing rule T3 installs. | four debts closed or explicitly kept, each with fixtures; fiches and debt register in step |
| **T5** | **Close the phase.** `phases/refoundation/phase-12-codifying/README.md` on the model of Phase 10's; the ledger's Phase 12 entry flipped to `done`, and whatever `phase-state` then flags fixed rather than silenced; the roadmap row flipped; the `phases/README.md` index gains Phase 12; the root `README.md` status paragraph, which still reads "Phase 10 complete… Next: Phase 11" (rewritten in T6, which pulls it forward because its check reads it; T5 re-reads it at close); `steering/foundation.md`'s `phase:` field bumped only after the whole document is re-read for staleness, not on the strength of the sections T1 touched. **Decide the changelog's shape:** T1 landed as one entry for the whole workstream; this plan criticises Phase 11's scattered per-task entries, so state whether a closing entry supersedes or supplements the ones already written, and apply that to T2–T4 rather than by accident. | phase README, roadmap/index/status reconciled, a stated changelog convention |
| **T6** | **Declare where the project is, and verify everything against it.** Today the current phase is implied in a dozen places that can each go stale: the roadmap's status markers and its `phase:` field, the `phases/README.md` index, the root README's status paragraph, `foundation.md`'s `phase:`, the phase folders, the ADR register's phase column. T2 and T5 exist because nothing tied them together. Declare it once, and make the gate check every other place against the declaration. **(a) The ledger.** A `phases:` section in [`docsys.yaml`](../../../docsys.yaml) — assumed there because it is instance configuration read through `docsys_config.py`, and the seam check already fails if the engine hard-codes an instance value; revisit in the ADR if a file of its own under `steering/` reads better. An ordered list, each entry an id, an era and a status of `done`, `current` or `planned`. A planned phase carries a name and **no number**, so the ledger is [ADR-038](../phase-11-tooling-hardening/unstarted-work-unnumbered.md) made structural; starting a phase is one edit that gives it a number and marks it `current`. Exactly one phase is `current`. The ledger holds only what is checkable: the roadmap's aim and outputs stay prose, because a second copy of them would be the drift this workstream removes. **(b) The check**, a new `phase-state` entry in the gate, fixtures written red first, each derived rule demonstrated failing on a synthetic mismatch and passing once corrected: a `done` or `current` phase has its folder under `phases/<era>/`, and no phase folder exists that the ledger does not list; the roadmap row and the `phases/README.md` index row for each phase carry the status marker the ledger says (the row format is configuration, as the register's is, not hard-coded); a `planned` phase is unnumbered in every table; no tracked document names an arabic-numbered phase above the highest numbered in the ledger, with fixtures for what it must not flag (a frozen record naming a phase that has since started, the era name "Phase II"); the root README's status paragraph names the current phase; a `done` phase has a README with `status: done`, and its records are sealed. **(c) `phase:` in frontmatter.** It means *current as of*, so a document may legitimately lag and the check is `phase` ≤ current, not equality. Equality is required only at close: a phase cannot be marked `done` while a document bearing `phase:` is behind it, unless the ledger lists that document as allowed to lag, with a reason each, on the model of [ADR-036](../phase-11-tooling-hardening/closed-frontmatter-vocabulary.md). This automates T5's rule that a `phase:` is bumped only after the whole document is re-read, by making a skipped re-read visible; it does not make the re-read happen. **(d) It lands green.** The root README status paragraph and any document the check flags on its first run are corrected in this workstream, which pulls that part of T5 forward. Phase 11's own plan is still `status: draft` although the phase is `done`, so the closure rule will flag it: expect a red first run, fix it as a closing act and say so in the changelog rather than exempting it. This **subsumes** the forward-numbering check the plan briefly held for T3 ([changelog alpha.19](../../../steering/CHANGELOG.md)), which inferred the current phase from folders instead of reading it. The check verifies that the places agree, not that any of them is true: a status paragraph can name the right phase and still describe it wrongly, so T5's re-read stays a human act. | a phase ledger in `docsys.yaml`; a `phase-state` gate check with fixtures; the stale places it flagged corrected; an ADR for the ledger; ADR-038 enforced |

Within T1, (a) before (c): the community map decides how the fiches are divided, so writing them first would fix the split by accident.
(b) can run beside (a), and must finish before (c) so the fiches describe the seam as it is, not as it was.
T1 before T2: writing Phase 11's backlogged ADRs is easier once the shelf they'd naturally reference (`codifying`) exists.
T4 can run beside T2, and both before T3: T4 edits `scripts/` and the fiches, and is the natural first exercise of the pairing rule, which T3 then turns into a check.
T3 is the last piece of mechanism: it needs T1's shelf to name as an acceptable pairing, and it is the check this phase should itself be unable to fail.
T6 is also mechanism, and can run beside T4: it reads `docsys.yaml` and the roadmap, not the fiches, and both come before T3.
T6 must land before T5, which becomes largely "flip the ledger and fix what the gate flags".
T5 is last: it narrates and reconciles what the others did, and cannot be written before they land.

## Verification / definition of done

- A written community map for `codifying` exists, each community carrying a declared `distance`, and each fiche names the audience it serves; the `maintainer` role question is ruled on, not left as an unexamined warning.
- No repo-specific path, prefix or register format is hard-coded in `scripts/*.py`: each lives in the rules file or config, and a grep for the old constants comes back empty.
- The gate's error messages are checked against the machine reader: each names the file, the rule and the fix without needing the surrounding context.
- `codifying/`'s ADR is accepted and in the register; `codifying/README.md` plus the three named fiches exist.
- The function set reads seven wherever it's enumerated — grepped, not assumed.
- Phase 11's three candidate decisions each have an ADR, or an explicit written ruling that they don't clear ADR-032's bar — not silently dropped either way.
- `phases/refoundation/phase-11-tooling-hardening/README.md` exists; `steering/roadmap.md` marks both Phase 11 and Phase 12 correctly; `phase:` bumped to `12-codifying`.
- `writing/frontmatter.md` states the closed vocabulary and points at `schema/frontmatter-rules.yaml`.
- The paired-change check exists and is demonstrated failing on a synthetic scripts-only diff, then passing once a docs file is added to it.
- The current phase is declared once, in the ledger in `docsys.yaml`; a ledger with two `current` phases, a numbered `planned` phase, or a `done` phase with no folder fails, each with a `fix:` clause.
- `phase-state` is demonstrated failing, red first, on each of: a folder the ledger does not list; a roadmap or index marker that disagrees with the ledger; a numbered mention of a phase above the last numbered one; a root README status that does not name the current phase; a `phase:` ahead of the current phase; a `done` phase with a lagging document not on the exception list; a `done` phase without its README or with an unsealed record.
  Each passes once corrected, and the fixtures pin what it must not flag.
- ADR-038 stays as written and frozen; the changelog says its "no check enforces this" limit is closed, and the ledger's own record is in the register.
- `steering/ARCHITECTURE.md` mentions Phase 11, points at `codifying/` for the tooling, and no longer says schema reconciliation is upcoming; `phases/README.md` marks Phase 11 correctly.
- `steering/CONTRIBUTING.md` states the paired-change rule, that the gate is run before committing, and where a new check is registered and what it must bring.
- A cycle and a self-supersession each fail the gate, demonstrated by fixtures that were red first; an empty register match fails; the three inline-message validators have fixtures asserting `fix:`; the frozen-record definition is either in the schema or guarded by a fixture that catches drift.
  Each closed debt is removed from `technical-debt.md` and its fiche's "does not establish" section updated in the same change.
- The YAML-source ADR states whether the generated JSON stays, with the reason.
- The root `README.md` status paragraph, the `phases/README.md` index and `steering/foundation.md`'s `phase:` field describe the repository as it is, and the changelog's convention for this phase is stated.
- The roadmap names a deployment phase after this one, and the items this plan defers to it (below) are recorded there, not lost.
- `python3 scripts/check.py` is green.

## Explicitly out of scope

- **The Phase-II design** — still the next era, not this phase.
- **Extracting the tooling into its own project.**
  Considered and deferred: one consumer means the boundary would be drawn from a single example, and a second repo would make the paired-change check (T3) span two repos.
  Step T1(b) makes extraction cheap; it does not perform it.
  Triggers to revisit: a second project wants the pipeline, or the engine/config seam holds unchanged for a full phase.
  The deployment phase named in the roadmap after this one is where a second consumer might become real; it, not this phase, reopens the question.
- **Cold readers, and exposing the content to third parties.**
  The `codifying/` fiches have been read only by the party that wrote them, which [ADR-035](codifying-function.md) states as a limit; a blind test needs a reader who did not build the tooling, and the product has the same need for someone outside the project.
  Both belong to the deployment phase, whose question is how the current content is exposed and made usable by third parties.
  Until then the limit stands, and no fiche is to be described as tested.
- **A separate agent-integration project.**
  It is the Phase-II design, parked in `imagining/`; whether it is a separate project is decided there, not here.
- **A rule against adding records to a closed phase's folder.**
  The ledger cannot see *new*: that needs the diff form T3 builds, and it must allow what T2 did, filling Phase 11's account forward, which is why a closed phase's ledger entry may need to say who filled it.
  Deferred until T3's diff machinery exists, and recorded rather than dropped.
- **Generating the roadmap and index status markers from the ledger.**
  Consistent with "generate, never store", but it adds machinery; T6 verifies first and generates only if verifying proves burdensome.
- **Rewriting any already-closed phase's frozen records** — supersede, never edit; Phase 11's gaps are filled forward, not corrected in place.
- **`distance`/`power` value sets, the shape of `concerns`** — still genuinely open per `schema/frontmatter-rules.yaml`'s own `still_open` list; this phase does not rule on them.

## Candidate records

Two decisions here install standing obligations and earn an ADR under the ADR-032 test, named now rather than assumed: **`codifying` is adopted as the seventh function**, and **a mechanism change without a paired documentation change fails the gate**.
Phase 11's three backlogged decisions belong to Phase 11's own provenance and are written under its project id even though this phase is what writes them.
Two more may surface and are checked against ADR-032 when they do, not assumed: whether the generated JSON stays, and whether the frozen-record definition moves into the schema (T4) — the second widens the schema's vocabulary, which is a ruling.
The first surfaced in T2 and was answered inside ADR-037, because it is the same decision seen a phase later, not a new obligation.
T2 also checked the strict-loader ruling from Phase 11's T2 against the test and held it inside ADR-037 too, for the reason that record gives.
T6 adds a third decision of the same kind: **a phase transition is an edit to the ledger, and the gate verifies every other place against it**, which earns an ADR in T6 and is checked against ADR-032 when written; the ledger's home in `docsys.yaml` is part of it.
Enforcing ADR-038 is execution of a record already on the register, so it is a changelog line.
