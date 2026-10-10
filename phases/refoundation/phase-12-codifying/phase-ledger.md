---
title: "Decision — the current phase is declared once, in a ledger, and the gate checks every other place against it"
id: 01M4BWR5KWAXSC6F1BFDXGMH3X
slug: phase-ledger
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-12-codifying }
constitutive: yes
concerns: [steering, codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:b52c469de163e733263e9ba8d49e7db93c3d666ded95b41613fe3a8f3ac651eb
---

## Status

accepted — 2026-10-07, at the end of Phase 12's T6.
It clears the [ADR-032](../phase-10-schema/adr-tiering.md) test: it changes what every contributor must do when a phase starts or closes, and the gate verifies it.
It executes [ADR-038](../phase-11-tooling-hardening/unstarted-work-unnumbered.md), which stays as written and frozen; that record's "no check enforces this" limit is what this one closes.

## Context and forces in play *(justify)*

Where the project stands was said in a dozen places — the roadmap's status markers and its `phase:` field, the phases index, the root README's status paragraph, `steering/foundation.md`'s `phase:`, the phase folders, the register's phase column — and nothing tied them together.
Each could go stale on its own, and did: when Phase 12 started, the root README still said Phase 10 was complete and Phase 11 next, the roadmap had tagged Phase 11 *(next)* after it closed, the index had no row for the phase in progress, and `foundation.md` was current as of Phase 07, five phases back.
Phases 10 and 11 each closed with some of these stale, which is why Phase 12 exists.

Three forces shaped the answer.

**Declare once, but only what can be checked.**
A second copy of the roadmap's aims and outputs would be the drift this removes, so the declaration holds the ordered phases and their status, and the prose stays prose.

**State is not configuration.**
The plan first assumed the declaration would be a section of `docsys.yaml`, the gate's instance configuration.
The project owner ruled otherwise: which phase is current is the project's state, changed at phase boundaries by a ruling, where `docsys.yaml` says what the tooling is pointed at and changes when the tooling does.
Keeping them apart also let `docsys.yaml` count as mechanism for the paired-change rule with no carve-out ([ADR-039](paired-change-rule.md)).

**A check that can never be cleared is noise.**
The gate's authority rests on red meaning *wrong* (Phase 09's rule, restated in `codifying/gate.md`).
Two rules the plan named would have broken it as first written: a forward-number check reading frozen records, which cannot be edited and of which ADR-038 itself quotes a forward-numbered sentence as its example; and a closure rule demanding that every closed phase's records be `done` and sealed, which met eighteen records ADR-031 leaves unsealed on purpose and a `status` vocabulary nobody has ruled.

## Decision

1. **The ledger, [`steering/phases.yaml`](../../../steering/phases.yaml), declares where the project is.**
   It is an ordered list of phases, each a `name`, an `era` and a `status` of `done`, `current` or `planned`.
   A `done` or `current` phase has a `number`, counting from 1 without a gap; a `planned` phase has none, so ADR-038 is structural.
   Exactly one phase is `current`, and the list runs every `done`, then the `current`, then every `planned`.
   Its own rules are checked by `phase-ledger` (`scripts/phase_ledger.py`).

2. **A phase transition is an edit to the ledger.**
   Starting a phase gives the first planned entry the next number and marks it `current`; closing one marks it `done`.
   Inserting work ahead of a planned phase is adding an unnumbered entry, and nothing that names it is renumbered.

3. **The ledger is steering's; `docsys.yaml` only says where it is and how to read the places that speak of it** (`phases:`), as `register:` does for the decision register.

4. **The gate checks every other place against it** (`phase-state`, `scripts/phase_state.py`, after `phase-ledger`):
   - a numbered phase has its folder, `phases/<era>/phase-<NN>-<name>`, and no phase folder is unlisted;
   - each phase row of the roadmap and the phases index carries the marker of the ledger's status, a row numbering a phase the ledger has not numbered fails, the current phase has a row, and a row pattern that matches nothing fails;
   - no living document names a phase by a number the ledger has not given;
   - the root README's one status line names the current phase;
   - a `phase:` field names a numbered phase and is not behind the last closed one.

5. **A document may lag only by the ledger's leave.**
   `lagging:` lists the documents whose `phase:` may stay behind the last closed phase, each with a reason that is not empty.
   An allowance whose document has caught up fails, so the list cannot outlive its reasons.

6. **Two scopes are part of the decision, not of its implementation.**
   A frozen record is not read for forward numbers: it says what was true when it froze, and it cannot be corrected.
   The closure rule — a closed phase's README and records frozen and sealed — is not decided here: it rests on the life cycle of a document, which the life-cycle phase rules first ([roadmap](../../../steering/roadmap.md)).

## Entail — what follows

- Closing or starting a phase is one edit to `steering/phases.yaml`; the gate then names, file by file, every place still describing the old state, and the phase does not land until each is corrected.
- A document carrying `phase:` is re-read whole and raised when a phase closes, or listed under `lagging:` with why it waits and when it will be re-read; the gate makes a skipped re-read visible, and does not make the re-read happen.
- Unstarted work is named, never numbered, in every living document, and the gate now says so where it is broken.
- A new place that speaks of the phase — another table, another status line — is a `phases:` edit in `docsys.yaml`, read by the engine without a code change.
- `docsys.yaml` is mechanism for the paired-change rule, so a change to it, moving `paired_change.since` included, carries an account in the same commit ([plan](plan.md), open point 11).

## Honest limit

**Agreement is not truth.**
The check verifies that the roadmap, the index and the status line name the right phase, not that what they say of it is right; a status paragraph can name the current phase and describe it wrongly, and the phase-close re-read stays a human act.

**The closure rule is missing.**
Until the life-cycle phase builds it, a closed phase's README can still say `in-progress` and its working plan stay a `draft`, and the gate says nothing; the inventory of such records is in the Phase 12 plan, open point 12.

**The readers are patterns.**
A status marker is the first words of an italic parenthesis, matched against three configured words, and the free text after ` — ` is not read.
A forward number is found by a regular expression: "Phases 10 and 11" yields only the first number, and a number spelt in words or another language is not seen.

**A reason is checked to exist, not to be good.**
A `lagging:` entry with a perfunctory reason passes, as a perfunctory edit to a fiche passes the paired-change rule.

**The ledger's planned entries carry assumptions.**
That the life-cycle and deployment phases belong to the refoundation era, and that Phase II's era is spelt `phase-ii`, are written in the ledger as assumptions, not rulings; the order of the planned phases is a ruling.
