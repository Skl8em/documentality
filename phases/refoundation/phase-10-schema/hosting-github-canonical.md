---
title: "Decision — hosting: GitHub canonical, Codeberg deferred to a self-hosted Forgejo"
id: 01M29EKW00YBM4S6AGM1RVPJX7
slug: hosting-github-canonical
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-10-schema }
constitutive: yes
concerns: [steering]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: 01KZ2EQ400KNDBJ8A7BWDV7ZKQ
superseded-by: null
hash: sha256:a346de924ab342e2f48428ba00ca0db6bb22f6f472c23df2fe6d7fd17d0f2cfb
---

## Status

accepted — 2026-09-12.
Supersedes [the Codeberg decision](hosting-codeberg-github-mirror.md) (register #029), which was recorded but never enacted — no Codeberg repository was ever created.

## Context and forces in play *(justify)*

Register #029 ranked two forces — visibility and sovereignty — and resolved them by making Codeberg canonical and GitHub a derived mirror.
The ranking was sound; the host it landed on was not.

Two things that decision did not weigh:

- **Codeberg's acceptable-use stance on AI-generated repositories.**
  Codeberg restricts predominantly AI-generated content, and this repository is substantially AI-assisted by design.
  On our own reading of that policy, this project is not what that forge wants to host — and we would rather not find that out by being told.
- **A forge whose terms you sit outside of is not sovereignty.**
  It is borrowed tolerance, which is the same dependency #029 set out to escape, wearing better politics.

So the freedom argument is not withdrawn — it is **relocated**.
Sovereignty over the record comes from *self-hosting* a Forgejo instance, not from moving onto someone else's non-profit forge.
That instance does not exist yet.

Until it does, the visibility force stands unopposed: GitHub is where contributors, tooling and search already are, and it is the lowest-risk place for the project to be found.

## Decision

1. **The canonical repository is GitHub** (`git@github.com:Skl8em/documentality.git`), for now.
   It holds the authoritative history; contributions land there.
2. **There is no mirror**, and so no split contribution surface — the honest limit #029 accepted is simply not incurred.
3. **The sovereignty aim is deferred to a self-hosted Forgejo instance.**
   When it exists it becomes canonical, and this decision is superseded in turn.

## Entail — what follows

- The trunk on GitHub is the singular governance line: merge to the trunk is the enacting `decide`.
- CI runs on GitHub Actions, which [`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml) already does — nothing to port.
- **Host-independence becomes a standing obligation, not a happy accident.**
  `scripts/check.py` is the gate, and it must stay runnable on any forge: no GitHub-only automation may be moved *into* it.
  That constraint is what keeps the eventual migration a remote change plus a CI port, and nothing more.
- The exit cost stays deliberately low: the history is portable, and the gate is stdlib Python plus a Nix devShell.

## Honest limit

GitHub is vendor-owned, and the FSF/GNU hosting evaluation rates it poorly.
This decision accepts that cost knowingly rather than arguing it away; choosing GitHub is a reach-and-risk judgement, not an endorsement of the platform.

The phrase "for now" is doing real work here, and decisions resting on "for now" tend to calcify into permanence by default.
The mitigation is the host-independence obligation above — a testable property — rather than an intention to migrate later.
