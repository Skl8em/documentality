---
title: "Decision — the paired-change rule fails where work lands, and skips what has nothing to explain"
id: 01M39TP1C5J1QG6C9SSRKRJP7T
slug: paired-change-where-it-fails
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
hash: sha256:097a097af30f79592920294321a76f10dde19f8fc81bcc992d8adc49a5e6469a
---

## Status

accepted — 2026-09-24, the day [ADR-039](paired-change-rule.md) was recorded.
Refines it; ADR-039 stands, and what this record moves is its "no exemption was written" limit and, implicitly, *where* the rule fails, which it left at "the gate".
The unit (a commit), the anchor and the two path lists are ADR-039's and are not touched.
It clears the [ADR-032](../phase-10-schema/adr-tiering.md) test: it changes what every contributor must do, and the gate verifies it.

## Context and forces in play *(justify)*

ADR-039's first implementation failed on every branch, and it listed its false positives as a cost the rule would carry: a test-only commit, a comment-only commit, a rename with no behaviour change.
The project owner ruled that cost wrong for two of them, and wrong for the place it was charged.
A test-only commit and a comment-only commit are acceptable on a feature branch, and the rule belongs on `main` and `develop`, where work lands.

Two forces pull against each other, and the record does not hide it.
The rule earned its unit, the commit, by being the only unit that catches Phase 11 ([ADR-039](paired-change-rule.md)); a unit coarser than a commit passes that phase.
But a commit-level rule that blocks a feature branch blocks exactly the work-in-progress rhythm this repository has, where a mechanism commit is followed by the commit that explains it.
The resolution is to keep the unit and move the *consequence*: the commit is still what is examined, and it is examined everywhere, but a failure only fails where the work is about to become the project's.

## Decision

1. **The rule fails only on the branches listed in `paired_change.enforce_on` (here `main`, `develop`) and on a detached HEAD.**
   A detached HEAD is what CI checks out for a pull request, the merge commit, so a pull request into an integration branch is checked in full.
   On any other branch the same findings print as a `WARNING` that names the branch and where the rule is enforced, and the exit status is 0.

2. **A change with nothing to explain is not a change to the mechanism.**
   That is a file under a `paired_change.exempt` prefix (here `scripts/test_`, the tests), or a Python file whose syntax tree, docstrings set aside, is unchanged: comments, docstrings and formatting.
   A version that does not parse is never comment-only; a file added or deleted is never comment-only.
   These apply on every branch.

3. **ADR-039's unit and anchor are unchanged.**
   The commit is examined, on a feature branch too, so the warning is exact rather than approximate.

## Entail — what follows

- On a feature branch a mechanism commit may precede the commit that explains it; the gate warns and passes.
  When that branch is opened as a pull request, every commit since the anchor is examined and the earlier one fails.
  It must be amended, or squashed with its account, before it lands.
  The cost that ADR-039 charged at commit time is now charged at merge time, on purpose.
- The two exemptions are the only categories.
  Anything else that "has nothing to explain" — a rename, a refactor with no behaviour change — is not exempt until it recurs enough to name.
- `enforce_on` is instance configuration, validated to be non-empty, and read through `docsys_config.py`.

## Honest limit

**Moving the failure to merge time moves the discovery to where repair is dearest.**
A warning that only bites at the pull request is a warning a contributor learns to skim, and the amend-or-squash it then asks for is a history rewrite.
This is the price of not blocking work in progress; whether it is affordable on a phase-long branch is untested, and Phase 12's own merge is the first case.

**The comment-only test is a heuristic on the tree, not on intent.**
A docstring edit is exempt, and a docstring can carry the very behaviour description a fiche was meant to track; an edit that only adds a docstring to a changed function is not saved by it, since the function's code changed, but a docstring that *replaces* the description of unchanged behaviour is invisible to the rule.
Only Python is examined: a comment-only edit to the schema's YAML still asks for an account.

**Enforcement is only as good as the branch list.**
If the integration branch is renamed and `enforce_on` is not, the rule silently becomes a warning everywhere but detached checkouts, and nothing in the gate says so.

**"Detached means enforce" over-reaches locally.**
A developer who checks out an old commit to look at it gets the enforced rule on a history they are not changing.
That is noise, not a hole.
