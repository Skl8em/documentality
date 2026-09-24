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

- You **must** keep `provenance` meaningful: use the maintaining function (`theorising`/`operationalizing`/`writing`/`structuring`/`codifying`/`steering`/`imagining`) or the owning project (`phase-NN`), never a blanket id.

- You **must** pair a change to the tooling with its account: a commit that touches `scripts/` or `schema/` also edits a file that explains it — under `writing/`, `structuring/`, `operationalizing/` or `codifying/`, or `steering/ARCHITECTURE.md` — in the same commit.
  In practice that is the [`codifying/`](../codifying/README.md) fiche for what you touched, or a new one.
  The gate checks it ([ADR-039](../phases/refoundation/phase-12-codifying/paired-change-rule.md)); it checks that an edit exists, not that it is right, so write the account you would want to have read.
  Consequence: an unpaired commit fails the gate, and it cannot be repaired by a docs commit afterwards — amend it, or move `paired_change.since` in [`docsys.yaml`](../docsys.yaml) past it, which is a deliberate acceptance that shows in review.

- You **must** run the gate before committing: `python3 scripts/check.py`, which enters the devShell itself when Nix is available.
  Opt in to the pre-commit hook once with `git config core.hooksPath .githooks`.
  Consequence: without the hook, a violation is found only by CI, after the commit exists.

- You **must** register a new check in the `checks:` list of [`docsys.yaml`](../docsys.yaml), never in `scripts/check.py`, which only runs what the list names.
  A check brings its fixtures, written red first and listed *ahead of* it, and every failure message names the file, the rule and a `fix:` clause.
  Consequence: a check without fixtures can stop detecting and still read green.
  ([`codifying/gate.md`](../codifying/gate.md) says why the order matters.)

- You **may** propose larger changes as an RFC (`propose`) before writing the ADR; for small, obvious fixes an ADR alone suffices.
