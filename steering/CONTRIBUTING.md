---
title: "Contributing to the system"
force: mandate
verb: require
intention: state
view: synchronic
provenance: { type: function, id: steering }
constitutive: yes
audience: [contributor]
reader: H+M
status: stable
---

Binding rules for changing this repository (the system itself), not for using it.
Rules for documents you write *with* the system are in the product ([`../write/rules.md`](../writing/rules.md), [`../structure/rules.md`](../structuring/rules.md)); this file governs contributions *to* the system.

## Rules

- You **must** give every new file a valid frontmatter and a single dominant `force` — the system must obey its own [`../write/rules.md`](../writing/rules.md).
  A contribution that violates the product's own rules is rejected.

- You **must** record any decision that **creates a standing obligation to verify and apply** by appending a row to the register [`ADR.md`](ADR.md) *and* writing the full record (context + `justify` + `entail`) in the **current phase** under [`phases/`](../phases/README.md); add a line to [`CHANGELOG.md`](CHANGELOG.md).
  A **punctual** action — one that is complete once done, and obliges nobody afterwards — is a changelog line only, with no ADR.
  Consequence: an undocumented standing obligation is reverted — the ADR *is* the decision.
  (The test, and the review of the register against it, are in [`../phases/refoundation/phase-10-schema/adr-tiering.md`](../phases/refoundation/phase-10-schema/adr-tiering.md).)

- You **must not** edit an existing ADR to reflect a later choice.
  A superseding decision is a **new** ADR that sets `superseded-by`/`supersedes`.
  ADRs are `view: diachronic`, frozen.
  Consequence: a rewritten ADR erases the design memory and is reverted.

- You **must** shelve content by its **provenance** — the function that maintains it: `theorising/`, the operational apports in `operationalizing/`, `writing/`, `structuring/`, the account of the tooling in `codifying/`, the project's governance in `steering/`, intended work in `imagining/`, and frozen records under `phases/`.
  Do not mix a function's content into another's shelf; the user's reading order across `writing/` and `structuring/` is a *generated* surface, not a folder to hand-carve.
  The rule shelves documentation: tooling and configuration folders — `scripts/`, `tools/`, `schema/`, `LICENSES/`, the engine's submodule, the dot-folders — are not shelves and carry no function.

- You **must** keep `provenance` meaningful: use the maintaining function (`theorising`/`operationalizing`/`writing`/`structuring`/`codifying`/`steering`/`imagining`) or the owning project (`phase-NN`), never a blanket id.

- You **must** contribute under the licence [`REUSE.toml`](../REUSE.toml) assigns to the file you add or change: GPL-3.0-or-later for code, CC0-1.0 for what an adopter copies (templates, schema, starting configuration), CC BY-SA 4.0 for prose ([ADR-043](../phases/rush-to-mvp/phase-13-design/licensing.md)).
  A new kind of file that no annotation fits gets one in the same commit; `reuse lint` confirms every file is covered.

- You **must** pair a change to the tooling with its account: a commit that touches `scripts/`, `schema/` or `docsys.yaml` also edits a file that explains it — under `writing/`, `structuring/`, `operationalizing/` or `codifying/`, or `steering/ARCHITECTURE.md` — in the same commit.
  In practice that is the [`codifying/`](../codifying/README.md) fiche for what you touched, or a new one.
  The gate checks it ([ADR-039](../phases/refoundation/phase-12-codifying/paired-change-rule.md), [ADR-040](../phases/refoundation/phase-12-codifying/paired-change-where-it-fails.md)); it checks that an edit exists, not that it is right, so write the account you would want to have read.
  A change to a test file, or to a Python file that alters only comments, docstrings or formatting, has nothing to explain and needs none.
  Consequence: on `main`, on `develop` and in a pull request an unpaired commit fails the gate; on any other branch it is a warning, so work in progress is not blocked, but it will fail when it lands.
  It cannot be repaired by a docs commit afterwards — amend or squash it with its account, or move `paired_change.since` in [`docsys.yaml`](../docsys.yaml) past it, which is a deliberate acceptance that shows in review.

- You **must** run the gate before committing: `python3 scripts/check.py`, which enters the devShell itself when Nix is available.
  Opt in to the pre-commit hook once with `git config core.hooksPath .githooks`.
  Consequence: without the hook, a violation is found only by CI, after the commit exists.

- You **must** divide a phase (`ph`), in its plan, into workstreams (`ws`), tracks (`tr`), tasks (`ts`) and steps (`sp`), and branch by them, merging each branch into the one it came from with `--no-ff`:
  - a **workstream** is a part of the phase that may run beside the others; it has no branch, since the tracks of different workstreams land on the phase branch in any order;
  - a **track** is a part of a workstream, with a branch cut from the phase branch and merged back into it when the track closes;
  - a **task** is a part of a track sized to be carried out in one agent session without running out of context, with a branch cut from its track's and merged back into it when the project owner has accepted the task;
  - a **step** is one commit (below).

  The project owner may accept in advance, by asking for a whole track to be carried out: each task is then merged as soon as its checks pass, and the presentation (below) is made once, for the track.
  Work is numbered when it starts, never before, as [ADR-038](../phases/refoundation/phase-11-tooling-hardening/unstarted-work-unnumbered.md) says of phases: a plan names and orders the workstreams, tracks and tasks it has not begun, and each takes the next free number at its level when it starts; a step is a commit, identified by its hash, and takes no number.
  Phase 14 applies these levels as far as its plan allows, its workstreams keeping the numbers its plan gave them; every plan after Phase 14 is divided by them.
  Branches are named in hyphen-case from those abbreviations: the phase branch `ph<NN>-<phase>` (`ph14-adoption`), a track's `ph<NN>-ws<N>-tr<N>-<track>` (`ph14-ws2-tr1-ci`), a task's `ph<NN>-ws<N>-tr<N>-ts<N>-<task>` (`ph14-ws2-tr1-ts1-ci-engine-shell`); older branches keep the names they were merged under (`t2-port-slug-check`, `phase-13-design-rush-to-mvp`).
  Consequence: the phase branch reads as one merge commit per track, each track as one merge commit per task, and the steps of each task stay in the history under it.

- You **must** keep a branch rebased on the branch it will be merged into, and merge it only from there: rebase it when you start a session on it, whenever its destination moves, and last before you present it; then run the suite and the gate on its tip, since no hook runs during a rebase.
  The merge is then a fast-forward that `--no-ff` records as a merge commit: it meets no conflict and brings nothing the checks have not seen.
  `--no-ff` does not squash: every step stays in the history, and the merge commit groups them, so that `git log --first-parent` on the destination reads one commit per task or track.
  A track is rebased with `--rebase-merges`, which keeps the merge commits of its tasks; a plain rebase flattens them.
  Only a branch that has never been pushed is rebased: task and track branches stay local, and the phase branch and `main`, which are pushed, never are.
  Consequence: conflicts are met early and in small pieces, on the branch that made them, never in a merge.

- You **must** carry out a task in steps, each one commit, made only when it is meaningful: *specify* (the rules, as data or prose), *red* (the tests that fail for the right reason, run and seen failing), *implement* (the change that turns them green), *document* (the account of what was done, for the reader who inherits it), *integrate* (the change wired into what uses it), *review global docs* (the pages elsewhere that state the present, brought up to date).
  Code that is moved, not written, is moved with its tests in a first commit that changes nothing else, and is not given a red step; *integrate* and *document* follow as they are worth it.
  A commit's subject starts with the name of the branch it is made on, less `ph<NN>-`, and says what the step leaves true (`ws2-tr1-ts1-ci-engine-shell: the engine pins its development tools in a flake`); on the phase branch it starts with `ph<NN>:`; its body says why, when the diff does not.
  A commit holds one step, and only the files of that step.

- You **must** present a finished task before merging it: what each step committed, what was run and what it showed, the assumptions taken, and what the project owner should check.
  For a track carried out on the project owner's standing request, the presentation is the track's: every task with its commits, what was run, what remains open.
  Consequence: a merge without that acceptance is reverted.

- You **must** mirror in the engine's repository (the `docsys/` submodule) the branches of work that changes both repositories: the same phase, track and task branches, under the same names, each cut from its counterpart there and merged with `--no-ff` at the same level and at the same time as here.
  The engine's branch is merged first; the commit in this repository that moves the submodule pointer to the engine's merge commit goes on the branch it is merged into, so each merge here is followed by a pointer at the merge of the same name there.
  A task that changes only the engine still gets its pointer commit here, on the task branch, at the engine's task tip, so that merging the task here is a real merge; the pointer at the engine's merge follows on the track branch.
  A rebase, too, is made in the engine first; every pointer commit here is then moved to the engine's rebased commit, since a pointer at a commit the rebase replaced names a commit no branch holds, which CI cannot fetch once it is pushed.
  Work that changes the engine alone and belongs to no task here needs no mirror, and the engine may carry branches of its own beside it.
  Consequence: the two branch graphs read alike, so whether the repositories are in step can be seen by comparing them.

- You **must** leave `main` alone until a phase closes: the phase branch is then merged into `main` with `--no-ff`, as one commit, in each repository the phase changed.
  Nothing is pushed without the project owner's word.

- You **must** register a new check in the `checks:` list of [`docsys.yaml`](../docsys.yaml), never in `scripts/check.py`, which only runs what the list names.
  A check brings its fixtures, written red first and listed *ahead of* it, and every failure message names the file, the rule and a `fix:` clause.
  Consequence: a check without fixtures can stop detecting and still read green.
  ([`codifying/gate.md`](../codifying/gate.md) says why the order matters.)

- You **may** propose larger changes as an RFC (`propose`) before writing the ADR; for small, obvious fixes an ADR alone suffices.
