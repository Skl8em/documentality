---
name: branch-and-commit
description: Branch, commit, rebase and merge a unit of work in this repository by the contributing rules — a branch per track and per task, a task committed in meaningful steps, rebased on its destination, presented before it is merged with --no-ff. Use whenever you start or resume a task of a plan, commit, rebase, merge, or are asked to "proceed with the next task" or "commit this".
---

The binding rules are in `steering/CONTRIBUTING.md` (the rules on how a plan is divided and branched, steps, presentation, the engine's mirror and `main`); read them first.
This skill is the procedure.

A plan divides a phase (`ph`) into workstreams (`ws`, no branch), a workstream into tracks (`tr`, a branch cut from the phase branch), a track into tasks (`ts`, a branch cut from the track's, sized for one session), a task into steps (`sp`, one commit each).
A plan names work it has not started and never numbers it: a track or a task takes the next free number at its level when you cut its branch.
If the task in front of you cannot be finished in this session, say so and propose how to split it before starting.

## Starting a task

1. Check which branch you are on and that the tree is clean: `git status`.
   Uncommitted work that belongs to an earlier task is committed there first, never carried into the new branch.
2. If the track has no branch yet, cut it from the phase branch, numbered after the workstream's last track (`git branch --list 'ph14-ws2-tr*'`): `git switch -c ph14-ws2-tr<N>-<track> ph14-adoption`.
3. Cut the task branch from its track branch, numbered after the track's last task: `git switch -c <track branch>-ts<N>-<task>` (`ph14-ws2-tr1-ts1-ci-engine-shell` from `ph14-ws2-tr1-ci`).
   A track with no tasks listed is one task of the same slug, `-ts1-<track>`.
4. If the task touches `docsys/` (the engine), cut the same branch name there, from the counterpart of the branch you cut from here: `git -C docsys switch -c <same name> <track branch>`.
   If the engine has no track or phase branch of that name yet, cut it first, the same way one level up; the engine's phase branch is cut from its `main`.
   Then `git -C docsys branch --list` and `git branch --list` should name the same branches for this work.

Resuming a task or a track in a later session, rebase it first (*Rebasing*).

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
- Subject: `<branch less ph<NN>->: <what the step leaves true>`, e.g. `ws2-tr1-ts1-ci-engine-shell: the engine pins its development tools in a flake`; `ph14: …` on the phase branch. The step is visible in the diff; the subject is not a step label.
- Stage by path, never `git add -A`. The pre-commit hook runs the gate on this repository; do not bypass it.
- A test is red only if you ran it: record what it showed.
- Co-author trailer as the session's attribution reminder says.

## Rebasing

Rebase a branch on the branch it will be merged into (a task on its track, a track on the phase branch) when you start a session on it, whenever that branch has moved, and last before presenting it.
Never rebase a branch that has been pushed: the phase branch and `main` never are.

1. In the engine first, when the branch exists there: `git -C docsys rebase <destination>` for a task, `git -C docsys rebase --rebase-merges <destination>` for a track.
2. Then here, the same way. A plain rebase of a track flattens the merges of its tasks; `--rebase-merges` keeps them.
3. Resolve a conflict in the commit that made it, `git add` the files, `git rebase --continue`.
   A conflict on `docsys` is a pointer: check `docsys` out at the engine's rebased commit for that step, and `git add docsys`.
4. When the engine was rebased, move every pointer commit to the engine's rebased commit.
   On a task, the pointer commit is the last: with `docsys` at the engine's rebased task tip, `git add docsys && git commit --amend --no-edit`.
   On a track, a pointer commit follows each task merge: `git rebase -i --rebase-merges <destination>`, mark each pointer commit `edit` (without an editor, through `GIT_SEQUENCE_EDITOR`), and at each stop `git -C docsys checkout <the engine's rebased merge of that task>`, `git add docsys`, `git commit --amend --no-edit`, `git rebase --continue`; switch `docsys` back to its branch after.
5. Check that no pointer names a commit the rebase replaced; each line must say `ok`:
   `git log --format=%H <destination>..HEAD -- docsys | while read c; do git -C docsys merge-base --is-ancestor "$(git rev-parse "$c:docsys")" <engine branch> && echo "ok $c" || echo "STALE $c"; done`
6. Run the suite of each repository touched and the gate here on the tip: no hook runs during a rebase.
   `git merge-base --is-ancestor <destination> HEAD` now holds, so the merge will be a fast-forward that `--no-ff` records as a merge commit.

## Finishing a task

1. Rebase the task on its track (*Rebasing*), then run the full suite of each repository touched, and the gate in this one.
2. **Present the task** to the project owner: the commits by step, what was run and what it showed, the assumptions taken, what to check. Then stop: do not merge.
3. On acceptance only (given in advance when the project owner asked for the whole track; the presentation is then the track's): in the engine first (`git -C docsys switch <track> && git -C docsys merge --no-ff <task>`), then in this repository merge the task branch with `--no-ff`, and commit the submodule pointer at the engine's merge commit on the track branch.
   A merge that meets a conflict was not rebased: `git merge --abort`, rebase, check, and merge again.
4. Keep the task branch until told otherwise; push nothing without the project owner's word.
5. Start the next task (back to *Starting a task*).

Closing a track is the same, one level up: rebase it on the phase branch with `--rebase-merges`, check it, present it, then merge the track branch into the phase branch with `--no-ff`, in the engine first when the track changed it, and commit the submodule pointer at the engine's merge on the phase branch here.
A workstream has no branch: it closes when its last track is merged.

`main` is left alone in both repositories until the phase closes; the phase branch is then merged into it with `--no-ff`, the same way.
