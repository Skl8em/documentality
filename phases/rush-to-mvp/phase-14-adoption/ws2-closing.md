---
title: "Closing ws2 — from continuous integration to the switch"
force: instruct
intention: state
view: synchronic
provenance: { type: project, id: phase-14-adoption }
constitutive: no
distance: initiated
audience: [contributor]
reader: H+M
status: draft
---

This walks ws2, a workstream of Phase 14, to its close: both phase branches pushed and green, and the plan saying ws2 is done.
Everything else ws2 set out to do is done, and [Where ws2 stands](workstreams.md#where-ws2-stands) states it: continuous integration of both repositories, every Markdown file a document, the link check's allowance, the author tools, and the switch, which made this repository's gate `docsys check` and retired `scripts/` and `schema/`.
The switch is the track `ph14-ws2-tr5-switch`, in both repositories; *Close ws2* merges it into `ph14-adoption`.
The engine's check of itself by `docsys` is ws4's, by the project owner's ruling.
The rulings it carries out are in [Rulings](rulings.md); ws1's remaining defects come after it.

## Before you start

- Run every command inside the devShell (`nix develop`, or the shell direnv enters); `uv` locks only there.
- Branch, commit, rebase and merge by [`CONTRIBUTING.md`](../../../steering/CONTRIBUTING.md) and the skill `branch-and-commit`: each track below is a branch cut from `ph14-adoption`, each task a branch cut from its track, carried out in one session and committed in steps, mirrored in `docsys/` when the task changes the engine.
  A track or a task is numbered when its branch is cut, with the next number at its level (the next track is `ph14-ws2-tr6-…`); until then this page names it by its slug (`close`).
  A track with no tasks listed is carried out as a single task of the same slug, on a task branch of its own like any other.
- Present each task to the project owner before merging it.
- Push only with the project owner's word, which *Close ws2* asks for.
- Before changing a check, read its fiche in the engine's `docs/`.

## The order

| Track | Repositories | Done when |
| --- | --- | --- |
| close | both | the plan says ws2 is done, and both phase branches are pushed and green |

## Close ws2

1. Bring ws2 to *done* in the plan and in [Workstreams](workstreams.md), and add the changelog entry.
2. Merge any track still open into `ph14-adoption`, the engine first.
3. Push both phase branches with the project owner's word, the engine first and this repository after: CI here checks the submodule out at the commit the pointer names, which must already be on the engine's remote.
4. Check: `gh run list -R Skl8em/docsys` and `gh run list` show a green run on each pushed commit.
   On a red run, read `gh run view <id> --log-failed`, fix it in a new task, and push again.

The links from this repository to the engine's fiches and to its `main` point at a branch that receives the phase only when the phase closes: they stay dead on GitHub until then, and the link check does not read web links.

## When something fails

- **CI is red but the gate passes locally:** a fixture depends on the machine (a default branch, a tool on the `PATH`, a file the Finder leaves); reproduce it with `GIT_CONFIG_GLOBAL` or a shell without your profile.
- **`uv.lock` changes revision:** it was locked outside the devShell; lock again inside it.
- **A commit fails the paired-change rule only on `main`:** it changed the mechanism without its account; amend it with its account before the merge, or move `paired_change.since` past it with a reason.
- **The paired-change rule reports its anchor missing:** `paired_change.since` names a commit that a rebase replaced; point it at the rebased commit, the last one before the gate became `docsys check`.
