---
title: "Decision — a change to the tooling that explains nothing fails the gate"
id: 01M39RTC22XJWZ10DJZQ2PQEF6
slug: paired-change-rule
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
hash: sha256:6d3f3c86ed9e8a9a42435effc417c8de13e520fb0a9fb50490a38e84b7b2197a
---

## Status

accepted — 2026-09-24.
Named as owed in [Phase 12's plan](plan.md) before it was written; implemented by its T3, whose retro-test of the first draft of the rule changed the rule and is recorded below.
It clears the [ADR-032](../phase-10-schema/adr-tiering.md) test: it installs a standing obligation on every later change to `scripts/` and `schema/`, and the gate verifies it.

## Context and forces in play *(justify)*

Two phases in a row closed with the product describing a model the tooling had left behind.
Phase 10 caught itself mid-close and repaired `writing/frontmatter.md` as an unplanned departure; Phase 11 did not catch it at all, and Phase 12's T2 paid the account afterwards.
Both failures had one shape: a change to the mechanism landed with no change to anything a human reads to understand it, and nothing in the process noticed.
The plan's workstreams and its checklist were pure mechanism, so a step that explained the mechanism was never a line item, and the gate could not see an absence.

The rule is easy to state — *a diff touching `scripts/**` or `schema/**` and none of the shelves that explain them fails* — and the whole decision is what "a diff" is.
That was checked against the history the rule exists for, not chosen a priori.

**Branch-level fails.**
Phase 11's branch, taken whole against the point it left `main`, touched `scripts/` and `schema/` heavily and also touched `steering/ARCHITECTURE.md`, `writing/frontmatter.md` and `structuring/tutorial.md`.
The three were incidental — two `note:` fields moved into the body, and a `phase` row and two legacy annotations added to the field table — and none stated what Phase 11 had changed.
A branch-level rule passes on Phase 11.
The repository works in phase-long branches, so any document edit anywhere in the phase pairs every script edit in it.

**Commit-level catches it.**
Phase 11's commits touching `scripts/` or `schema/` were five; four of them touched no explaining shelf (`parse YAML with YAML`, `YAML source, generated JSON`, `Referential Integrity`, and a chore).
The fifth, `close the vocabulary`, did.
The rule fires on exactly the commits that produced the gap.

**What commit-level costs.**
Two earlier Phase 12 commits, the seam move (`T1(b)`) and the gate-output fix (`T1(c)`), put the mechanism in one commit and its account in a later one, so a commit-level rule would have failed both.
That is the rule working as designed and costing what it should: the account goes in the same commit as the change, or the commit is not made.

## Decision

1. **The unit is a commit, and the uncommitted work that will become the next one.**
   A unit that touches the mechanism and touches nothing that explains it fails the gate.
   Merge commits are not units; the history they bring in is that history's own.
   Renames count as a delete and an add, so moving a script out of `scripts/` is a change to the mechanism.

2. **The mechanism** is `scripts/` and `schema/`.
   **What explains it** is any file under `writing/`, `structuring/`, `operationalizing/` or `codifying/`, or `steering/ARCHITECTURE.md`.
   The changelog and the phase records are not on the list: they record *that* something changed, and the failures were of a reader's understanding of *what is true now*.
   Both lists are instance configuration in `docsys.yaml`, not literals in the engine.

3. **The rule starts at an anchor.**
   `paired_change.since` in `docsys.yaml` names a commit; only commits after it, and the pending work, are examined.
   History before it predates the rule and is not re-judged.
   Moving the anchor forward past a commit is how an already-made commit is accepted: a visible edit to a tracked file, in the diff, rather than a silent exemption.
   An anchor that cannot be resolved — a shallow clone, a commit not in this history — fails loud rather than checking nothing.

## Entail — what follows

- Every change to `scripts/` or `schema/` carries, in the same commit, an edit to a file that explains it.
  In practice the fiche for what was touched, [`codifying/`](../../../codifying/README.md), which is the shelf built to receive it.
- CI must fetch full history (`fetch-depth: 0`): the rule reads commits, and a shallow checkout would otherwise be a vacuous pass.
- [`CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md) states the rule, and how a check is registered and what it must bring, once.
- The rule is itself a mechanism change, so its own commit is subject to it from the first.

## Honest limit

**It verifies co-occurrence, not adequacy.**
A one-word edit to a fiche satisfies it, and a fiche edited for another reason satisfies it for a change it does not describe.
Someone unwilling to write the account will write the smallest edit that passes, and the gate cannot tell.
It removes the *silent* case, which is what happened twice; it does not make the account true.
Whether the fiche still says what the code does stays a human reading, and the phase-close re-read is where that lives.

**It is enforced only where the gate runs.**
The pre-commit hook is opt-in (`git config core.hooksPath .githooks`), and a clone that has not opted in learns of a violation in CI, after the commit exists.
Because a commit cannot be amended once shared, the remedy then is the anchor move, which is the escape hatch the rule provides and the first thing a hurried contributor will reach for.
Every use of it is in the diff, which is the only protection.

**It has false positives by construction.**
A commit that changes only `scripts/test_*.py`, or a comment, or a rename with no behaviour change, touches the mechanism and explains nothing because there is nothing to explain.
No exemption was written, because each would be a category a contributor could argue into; the cost is a one-line edit to the relevant fiche, or an honest anchor move.
If that cost becomes routine, the list of exemptions is the thing to revisit, from evidence and not before.

**It is drawn from two failures.**
The retro-test is the party that wrote the rule reading the history that motivated it.
It says the rule would have fired on the commits that caused the gap; it says nothing about the failures no one has had yet.

**It does not see all the mechanism.**
`docsys.yaml` and `tools/markdownlint/` are apparatus and are not in the list: a change confined to them passes.
`docsys.yaml` was left out because a routine edit to it — a phase transition, once T6's ledger lives there — is not something the shelves explain.
The gap is real and is recorded, not closed.
