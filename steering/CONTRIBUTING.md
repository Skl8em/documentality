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

- You **must** work in nested branches and merge each into the one it came from with `--no-ff`: the phase branch holds one branch per workstream (`t2-port-other-checks-one-at-a-time`), which holds one branch per item (`t2-port-slug-check`), named `<workstream id>-<item>` in hyphen-case.
  An item branch is cut from its workstream branch, and merged back into it when the project owner has accepted the item; a workstream branch is merged into the phase branch the same way when its workstream closes.
  Consequence: the larger branch reads as one merge commit per item, and the steps of each item stay in the history under it.

- You **must** commit an item in steps, each made only when it is meaningful: *specify* (the rules, as data or prose), *red* (the tests that fail for the right reason, run and seen failing), *implement* (the change that turns them green), *document* (the account of what was done, for the reader who inherits it), *integrate* (the change wired into what uses it), *review global docs* (the pages elsewhere that state the present, brought up to date).
  Code that is moved, not written, is moved with its tests in a first commit that changes nothing else, and is not given a red step; *integrate* and *document* follow as they are worth it.
  A commit's subject names the item and says what the step leaves true (`T2 slug: the check reports the rules conformance/slugs.yaml states`); its body says why, when the diff does not.
  A commit holds one step, and only the files of that step.

- You **must** present a finished item before merging it: what each step committed, what was run and what it showed, the assumptions taken, and what the project owner should check.
  Consequence: a merge without that acceptance is reverted.

- You **must** use the same branch names in the engine's repository (the `docsys/` submodule) and in this one when an item changes both.
  The engine's branch is merged first; the commit in this repository that moves the submodule pointer to the engine's merge commit goes on the branch it is merged into.
  Nothing is pushed without the project owner's word.

- You **must** register a new check in the `checks:` list of [`docsys.yaml`](../docsys.yaml), never in `scripts/check.py`, which only runs what the list names.
  A check brings its fixtures, written red first and listed *ahead of* it, and every failure message names the file, the rule and a `fix:` clause.
  Consequence: a check without fixtures can stop detecting and still read green.
  ([`codifying/gate.md`](../codifying/gate.md) says why the order matters.)

- You **may** propose larger changes as an RFC (`propose`) before writing the ADR; for small, obvious fixes an ADR alone suffices.
