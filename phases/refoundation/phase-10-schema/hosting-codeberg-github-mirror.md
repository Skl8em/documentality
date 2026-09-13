---
title: "Decision — hosting: Codeberg canonical, GitHub mirror"
id: 01KZ2EQ400KNDBJ8A7BWDV7ZKQ
slug: hosting-codeberg-github-mirror
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
supersedes: null
superseded-by: 01M29EKW00YBM4S6AGM1RVPJX7
hash: sha256:3688d7a331084233c2963e47c903e51694439e3190d9193cc692bc990af704a7
---

## Status

accepted — 2026-08-03.
**Superseded on 2026-09-12** by [the GitHub-canonical decision](hosting-github-canonical.md) (register #034), on a ground this record never weighed: Codeberg restricts predominantly AI-generated repositories, and this one is substantially AI-assisted.
The decision below was **never enacted** — no Codeberg repository was created, and the remote stayed on GitHub throughout.

## Context and forces in play *(justify)*

The repository needed a home, and the choice is not neutral for a project whose subject is *documentality* — where a record is preserved and by whom is part of what the record is.

Two forces pull against each other:

- **Visibility.**
  GitHub is where contributors, tooling, and search already are; a project nobody finds is a project nobody receives.
- **Freedom and sovereignty.**
  The FSF/GNU hosting-evaluation rates GitHub `F`; the Software Freedom Conservancy's *Give Up GitHub* campaign recommends Forgejo instances such as Codeberg; GNU Guix moved to Codeberg.
  Codeberg is a non-profit, EU-based, Forgejo-run forge — its governance matches this project's own stance on preservation better than a vendor-owned platform does.

The forces are not reconcilable by choosing one host, but they are reconcilable by ranking them: one host is *canonical* (where the fact lives) and the other is a *derived surface* (where it is seen).
That is the same state/change and source/generated distinction the system already makes everywhere else.

## Decision

1. **The canonical repository is Codeberg**.
   It holds the authoritative history; contributions land there.
2. **GitHub is a push mirror**, for visibility only.
   It is a generated surface, not a second source of truth.
3. **CI runs on the canonical, or on the mirror** — whichever is cheaper to operate — since the gate (`scripts/check.py`) is host-independent by construction.

## Entail — what follows

- The trunk on Codeberg is the singular governance line (per the ways-of-working convention: merge to the trunk is the enacting `decide`).
- A pull request opened on the GitHub mirror is *not* on the canonical line; it must be brought to Codeberg to be enacted.
- The mirror can be re-created from the canonical at any time, so mirror-side history is disposable by design.
- The technical setup — Codeberg repository, remotes, push-mirror, CI port — is execution, not decision.

## Honest limit

A mirror splits the contribution surface: someone who finds the project on GitHub and opens a pull request there has done real work in the wrong place, and no amount of README text fully prevents that.
We accept the friction rather than resolve it, and it is worth revisiting if it ever produces lost contributions.
