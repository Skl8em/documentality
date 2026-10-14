---
name: branch-and-commit
description: Branch, commit and merge a unit of work in this repository by the contributing rules — a branch per workstream and per item, an item committed in meaningful steps, presented before it is merged with --no-ff. Use whenever you start an item of a plan, commit, merge, or are asked to "proceed with the next item" or "commit this".
---

The binding rules are in `steering/CONTRIBUTING.md` (the three rules on nested branches, steps and presentation); read them first.
This skill is the procedure.

## Starting an item

1. Check which branch you are on and that the tree is clean: `git status`.
   Uncommitted work that belongs to an earlier item is committed there first, never carried into the new branch.
2. Cut the item branch from its workstream branch: `git switch -c <workstream id>-<item>` (e.g. `t2-port-slug-check` from `t2-port-other-checks-one-at-a-time`).
3. If the item touches `docsys/` (the engine), cut the same branch name there: `git -C docsys switch -c <same name>`.

## Committing in steps

Make only the steps that are meaningful, in this order, one commit each, only the files of that step:

| Step | The commit holds | Check before committing |
| --- | --- | --- |
| specify | the rules and cases, as data or prose | they read as a statement of the rule |
| red | the tests (and a stub, if the tests cannot import without one) | **run them and see them fail for the right reason** |
| implement | the change that turns them green | the item's tests pass; types and lint pass |
| document | the account of what was done and why, for the next reader | a reader with no context could act on it |
| integrate | the change wired into what uses it | the whole suite and the gate pass |
| review global docs | the pages elsewhere that state the present (plan progress, READMEs, changelog) | each states the present, not the change |

- Moving code is a naive move first: code and tests together, nothing else changed, no red step. Integrate and document afterwards, as they earn it.
- Subject: `<phase> <workstream> <item>: <what the step leaves true>`, e.g. `T2 slug: the check reports the rules conformance/slugs.yaml states`. The step is visible in the diff; the subject is not a step label.
- Stage by path, never `git add -A`. The pre-commit hook runs the gate on this repository; do not bypass it.
- A test is red only if you ran it: record what it showed.
- Co-author trailer as the session's attribution reminder says.

## Finishing an item

1. Run the full suite of each repository touched, and the gate in this one.
2. **Present the item** to the project owner: the commits by step, what was run and what it showed, the assumptions taken, what to check. Then stop: do not merge.
3. On acceptance only: in the engine first (`git -C docsys switch <workstream> && git -C docsys merge --no-ff <item>`), then in this repository merge the item branch with `--no-ff`, and commit the submodule pointer at the engine's merge commit on the workstream branch.
4. Keep the item branch until told otherwise; push nothing without the project owner's word.
5. Start the next item (back to *Starting an item*).

Closing a workstream is the same, one level up: present it, then merge the workstream branch into the phase branch with `--no-ff`.
