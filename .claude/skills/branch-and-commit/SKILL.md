---
name: branch-and-commit
description: Branch, commit and merge a unit of work in this repository by the contributing rules — a branch per track and per task, a task committed in meaningful steps, presented before it is merged with --no-ff. Use whenever you start a task of a plan, commit, merge, or are asked to "proceed with the next task" or "commit this".
---

The binding rules are in `steering/CONTRIBUTING.md` (the rules on how a plan is divided and branched, steps, presentation, the engine's mirror and `main`); read them first.
This skill is the procedure.

A plan divides a phase into workstreams (no branch), a workstream into tracks (a branch cut from the phase branch), a track into tasks (a branch cut from the track's, sized for one session), a task into steps (one commit each).
A plan names work it has not started and never numbers it: a track or a task takes the next free number at its level when you cut its branch.
If the task in front of you cannot be finished in this session, say so and propose how to split it before starting.

## Starting a task

1. Check which branch you are on and that the tree is clean: `git status`.
   Uncommitted work that belongs to an earlier task is committed there first, never carried into the new branch.
2. If the track has no branch yet, cut it from the phase branch, numbered after the workstream's last track (`git branch --list 'feature/ph14-t2-ws*'`): `git switch -c feature/ph14-t2-ws<N>-<track> feature/phase-14-adoption`.
3. Cut the task branch from its track branch, numbered after the track's last task: `git switch -c <track branch>-tsk<N>-<task>` (in Phase 14, `feature/ph14-t2-ws1-tsk1-ci-engine-shell` from `feature/ph14-t2-ws1-ci`, where `t2` is the workstream and `ws1` the track).
   A track with no tasks listed is one task of the same slug, `-tsk1-<track>`.
4. If the task touches `docsys/` (the engine), cut the same branch name there, from the counterpart of the branch you cut from here: `git -C docsys switch -c <same name> <track branch>`.
   If the engine has no track or phase branch of that name yet, cut it first, the same way one level up; the engine's phase branch is cut from its `main`.
   Then `git -C docsys branch --list` and `git branch --list` should name the same branches for this work.

## Committing in steps

Make only the steps that are meaningful, in this order, one commit each, only the files of that step:

| Step | The commit holds | Check before committing |
| --- | --- | --- |
| specify | the rules and cases, as data or prose | they read as a statement of the rule |
| red | the tests (and a stub, if the tests cannot import without one) | **run them and see them fail for the right reason** |
| implement | the change that turns them green | the task's tests pass; types and lint pass |
| document | the account of what was done and why, for the next reader | a reader with no context could act on it |
| integrate | the change wired into what uses it | the whole suite and the gate pass |
| review global docs | the pages elsewhere that state the present (plan progress, READMEs, changelog) | each states the present, not the change |

- Moving code is a naive move first: code and tests together, nothing else changed, no red step. Integrate and document afterwards, as they earn it.
- Subject: `<track> <task>: <what the step leaves true>`, e.g. `ws1 ci-engine-shell: the engine pins its development tools in a flake`. The step is visible in the diff; the subject is not a step label.
- Stage by path, never `git add -A`. The pre-commit hook runs the gate on this repository; do not bypass it.
- A test is red only if you ran it: record what it showed.
- Co-author trailer as the session's attribution reminder says.

## Finishing a task

1. Run the full suite of each repository touched, and the gate in this one.
2. **Present the task** to the project owner: the commits by step, what was run and what it showed, the assumptions taken, what to check. Then stop: do not merge.
3. On acceptance only (given in advance when the project owner asked for the whole track; the presentation is then the track's): in the engine first (`git -C docsys switch <track> && git -C docsys merge --no-ff <task>`), then in this repository merge the task branch with `--no-ff`, and commit the submodule pointer at the engine's merge commit on the track branch.
4. Keep the task branch until told otherwise; push nothing without the project owner's word.
5. Start the next task (back to *Starting a task*).

Closing a track is the same, one level up: present it, then merge the track branch into the phase branch with `--no-ff`, in the engine first when the track changed it, and commit the submodule pointer at the engine's merge on the phase branch here.
A workstream has no branch: it closes when its last track is merged.

`main` is left alone in both repositories until the phase closes; the phase branch is then merged into it with `--no-ff`, the same way.
