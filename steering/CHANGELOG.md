---
title: "Changelog of the system"
force: account
verb: report-against
intention: state
view: diachronic
provenance: { type: function, id: steering }
constitutive: yes
audience: [contributor, decider]
reader: H+M
status: stable
retention: permanent
---

History of the documentation system itself.
Append-only; each entry is dated-fixed.
Design rationale for each line lives in the matching ADR — listed in the register [`ADR.md`](ADR.md), written in full in its [`phases/`](../phases/README.md) folder.

## [v4.0-alpha.8] — Phase 10 schema & governance reconciliation

- **Decided:** **`register` is derived, never stored** — `constitutive ? govern : direction-of-fit(force)` — and a new required, stored **`constitutive: yes|no`** carries the markedness the old know/do/govern triad hid (`govern` was never a third direction of fit).
  Settles ⚑ Decision 2; supersedes the register part of ADR-016, refines that of ADR-025; the three `writing/forces/` doors are unchanged.
  Deriving `constitutive` from `force × power` stays deferred.
  (ADR-030)
- **Changed:** `intention` is stored as the **coarse** family `state` · `formative` · `suasive` · `affective`; the fine aims (locate/model/enable/convince) remain in the guidance as *readings* of a stored value, not as values.
  Settles ⚑ Decision 1.
- **Changed:** the corpus swept to match — 89 of 93 catalogued documents rewritten (fine `intention` → coarse, stored `register` removed, `constitutive` judged per document: 21 `yes`, 72 `no`).
- **Changed:** `schema/frontmatter.schema.json` reconciled and `scripts/frontmatter_lint.py` **promoted** — coarse `intention`, absent `register`, and present `constitutive` are now **errors**, not warnings; the schema also encodes the direction-of-fit table (the linter refuses to load a table that does not partition the twelve forces exactly) and `frontmatter_lint.py --registers` computes the derived value.
- **Decided:** **content-hash fixity** — an optional `hash: sha256:…` seals each frozen record, with the canonical form defined exactly; `scripts/hash_seal.py` mints (`--frozen`, `--reseal`, `--print`) and `scripts/hash_check.py` verifies.
  Where `pin` fixes what a document *points at*, `hash` fixes what it *is*.
  (ADR-031)
- **Decided:** **ADR tiering** — a decision earns an ADR only by installing a **standing obligation to verify and apply**; a punctual action is a changelog line.
  `CONTRIBUTING`'s trigger relaxed from a four-subject list to that test; the register reviewed by receivability (27 of 28 kept, three borderlines named).
  (ADR-032)
- **Removed:** ADR-019 (restart strategy) from the register — a punctual sequencing decision.
  Its frozen record stays unedited; the plan content moves to a roadmap "plan changes" note; the generated ordinal absorbs the gap without renumbering.
- **Decided:** **`operationalizing` is the sixth function**, between theory and product — recording a decision ratified and enacted in alpha.7 but never written to the register; the function set is reconciled in `foundation.md`, `CONTRIBUTING`, and the root `README`.
  (ADR-033)
- **Changed:** the product guidance realigned with the schema — `writing/frontmatter.md` (the `constitutive` and `hash` fields, `register` as a derived view, the required set now eight), `writing/concepts.md` (the register re-founding, coarse-vs-fine made explicit), `writing/choosing.md` (a new step 4: judge whether the act constitutes).
- **Added:** two checks to the gate — fixity, and a `git status --porcelain` assertion, so untracked on-disk cruft can no longer pass a gate that reads only `git ls-files`.
- **Closed:** two technical debts — the untracked reorg zombies (gone, and the gate now notices) and the duplicated round-2 blind-test transcripts (byte-identical; the `weft-blindtest-round2/` copy deleted).
- **Closed:** Phase 10 — `steering/open-questions.md` now holds nothing open; the ratified deliberations are decanted into ADR-030–033, and what remains undecided is listed as `still_open` in the schema rather than as a live question.

## [v4.0-alpha.7] — hosting: Codeberg canonical + GitHub mirror

- **Decided:** the canonical repository is **Codeberg** (non-profit, EU, Forgejo), **mirrored to GitHub** for visibility; contributions land on the canonical, CI on the canonical or the mirror.
  Rationale: visibility (GitHub) + freedom/sovereignty (FSF/GNU rate GitHub `F`; SFC's *Give Up GitHub* recommends Codeberg/Forgejo; GNU Guix moved to Codeberg).
  ([decision](../phases/refoundation/phase-10-schema/hosting-codeberg-github-mirror.md); register #029)
- **Added:** a root `.gitignore` (`.DS_Store`, `__pycache__`, Nix outputs) — closes the untracked "zombie directory" gap; `git clean -fd` retires them.
- **Note:** the technical setup (Codeberg repo, remotes, push-mirror, CI port) is executed with Claude Code, per the ways-of-working division.

## [v4.0-alpha.6] — Phase 09 tooling (enforce the conventions, ready the catalogue)

- **Added:** a reproducible **Nix `devShell`** (`flake.nix`/`flake.lock`) pinning `markdownlint-cli2`, node, python, and git per project — so local and CI run the same bit-for-bit tools; install/usage in `steering/environment.md`.
- **Added:** a **unified markdownlint** ruleset shared by the CLI and the VSCode extension — title in frontmatter (no body `# H1`), a custom `sentence-per-line` rule enforcing ADR-021, defaults taken over explicitly; the corpus was reflowed to one sentence per line (286 splits + 48 joins, rendering-neutral) to zero violations.
- **Added:** a **frontmatter-lint** safe starter (`scripts/frontmatter_lint.py` + `schema/frontmatter.schema.json`) — errors on the settled invariants, warns on the contested ones (handed to Phase 10).
- **Decided:** **ULID + slug identifiers** (ADR-028) — canonical `id: <ULID>` in frontmatter, filenames stay `<slug>.md` (ULID *not* in the name), two minting modes (ADRs chronological, phases ordinal via an `order` key), generated display ordinal; `scripts/ulid.py` mints, `scripts/ulid_check.py` verifies ids, `scripts/slug_check.py` lints filename == slug.
The naming convention is kept **open**, with tools both ways — `scripts/slugify_names.py` (→ `<slug>.md`) and `scripts/migrate_ids.py` (→ `<slug>-<ulid>.md`), both on the safe-rename core `scripts/rename_doc.py`; legacy count-named records are left as-is for now.
- **Added:** one **gate** — `scripts/check.py` (markdownlint + frontmatter + ULID + links), always using the *pinned* markdownlint; wired into an opt-in pre-commit hook and a CI workflow.
- **Added:** `steering/technical-debt` (the deferred-work register) and `steering/environment.md`.

## [v4.0-alpha.5] — roadmap: insert Phase 09 (tooling), renumber

- **Changed:** the roadmap gains **Phase 09 — Tooling** (unified markdownlint sharing one ruleset between CLI and the VSCode extension; a *safe-starter* frontmatter-lint harness; ULID + slug identifiers replacing the sequential counts, with minting and verification).
  The former schema-reconciliation phase becomes **Phase 10**, and design-of-Phase-II becomes **Phase 11**; the *refoundation* era now spans phases 06–10. Tooling is placed *before* the schema so the lint harness makes Phase 10 efficient. A detailed plan lives in [`phases/refoundation/phase-09-tooling/plan.md`](../phases/refoundation/phase-09-tooling/plan.md). Frozen records from earlier phases keep their-time phase numbers; the live plan and governance docs are renumbered.

## [v4.0-alpha.4] — refounded vocabulary, the twelve forces, and the gerund shelf (Phase 08 complete)

- **Changed:** `perlocution` → `intention` across the product and catalogue — a constitutive floor (`state`) with an optional aim above it (`locate`/`model`/`enable`/`convince`, grouping into `formative`/`suasive`/`affective`); the field, the guidance prose (`writing/concepts.md`, `frontmatter.md`, `choosing.md`, the force stances), and the twelve v3 `perlocution: none` frontmatters all convert (`none` → `state`).
  (ADR-026; refines ADR-015)
- **Clarified:** know/do/govern named as a **register gloss** over `force` (a generated view, not the shelf axis); `recommend` and `entail` as extension examples; the **machine** as the recipient relation at its limit (maximum distance, quiet power) — a flag, never a role.
  (ADR-016; ADR-017/022)
- **Added:** the nine not-yet-built forces — `explain`, `describe`, `teach`, `recommend`, `mandate`, `commit`, `propose`, `prove`, `account` — authored under `writing/forces/` (stance `README.md` + `template.md`); all twelve forces are now built.
- **Removed:** `_legacy/` (the migration source) and `structuring/applied.md` (the stale v3 self-reading, superseded by `self-application.md`).
- **Renamed:** function folders and `provenance.id` to the **gerund** form — `theory→theorising`, `write→writing`, `structure→structuring`, `imagine→imagining` (`steering` already conformed); the `theory` nested git repo absorbed via a history-preserving subtree merge.
  (ADR-027)
- **Changed:** `phases/` grouped into **physical era folders** (`naive-sketch/`, `refoundation/`); stale `written-at`/`valid-for` v3 markers dropped from the live docs.
- **Added:** `steering/open-questions.md` — the live deliberation register (⚑ intention coarse-vs-fine, ⚑ register stored-vs-derived → Phase 10) — and `scripts/linkcheck.py`, the phase-close link gate (reports zero broken links).

## [v4.0-alpha.3] — provenance shelf & the govern model (Phase 08)

- **Changed:** the source is now shelved **provenance-first** — the generic `docs/` bucket is dissolved into `steering/` (governance) and root `phases/` (frozen records), and `imagine/` is added at root (Phase II, parked).
  One folder per function: `theory/` `write/` `structure/` `steering/` `imagine/`, plus `phases/`.
  (ADR-024)
- **Changed:** the root axis declaration moves from `scope` (dominant `user`) to `provenance` (dominant `contributor`); the root `README` provenance is `steering` — `onboarding` is a *served* reading order, not a producer function.
  (ADR-024)
- **Clarified:** a `govern` document is classed by the **domain it governs**, not by register; `steering` is the activity whose domain is the project itself (so it carries its own know/do/govern); a *decision* (frozen) and the *rule* it installs (current) are two documents joined at the state/change seam.
  (ADR-025)
- **Added:** the **transversal/vertical** governance tension named as irreducible, with a root **governance-axis** declaration (central vs local), a subsidiarity/VSM procedure, and a `concerns` coordinate (the activities a document governs, distinct from its `provenance`); per-activity views are **generated, not moved**.
  (ADR-025)
- **Renamed:** the perlocution/intention **floor value `none` → `state`** — the floor is not absence; the act establishes a state in the reader and shadows the unsaid.
  The coarse set is now `{state, formative, suasive, affective}`.
  Canonical vocabulary updated; the twelve v3 `perlocution: none` frontmatters convert with the vocabulary pass.
  (ADR-026; refines ADR-015)
- **Note:** references updated across the live docs (root `README`, `steering/ARCHITECTURE`, `steering/README`, `CONTRIBUTING`, `write/**` pointers, `foundation`, `roadmap`); frozen ADR records and historical changelog entries are left as-is.
  The refounded vocabulary in the v3 files and the `_legacy/` migration remain the rest of Phase 08.

## [v4.0-alpha.2] — tutorial rewrite from the blind test (Phase 07)

- **Added:** a blind test — a fresh agent followed the tutorial on this project and on `weft` (external), each with an adversarial review; artifacts kept under `phases/phase-07-structuring-tutorial/blind-test/`.
  (ADR-023)
- **Changed:** a **function** is now an activity *of relevance* (importance), not a *recurring* one — admitting one-off-but-central, once-per-person, and defensive activities.
  (ADR-023)
- **Added:** the **fractal method** made explicit — coarse-first, ~3–7 per level, group past 7, refine on intolerable gaps, see-your-holes — with an explicit licence to leave the path; the tutorial no longer pretends to be deterministic.
  (ADR-023)
- **Changed:** the source tree is organized **for the author** (first reader), not "the user"; the generated reader surface is deferred to a planned frontmatter tutorial.
  (ADR-023)
- **Added:** **`imagine`** as a first-class activity, homing intended/future (Phase-II-shaped) work.
  (ADR-023)
- **Added:** worked examples via the **conventional repo documents** (README, INSTALL, CONTRIBUTING, LICENSE, ARCHITECTURE, CHANGELOG, ADR) — named, classified, placed — plus two/three valid trees and a fractal folder rule; two entry-states (greenfield / existing-audit).
  (ADR-023)
- **Changed:** the neutral blind-test spec (`self-spec.md`) revised to close the state gaps the reviews surfaced, kept neutral on structure.
  (ADR-023)
- **Verified:** a second blind test (round 2, `weft`) validated the rewrite — four of five round-1 cold-stops resolved — and drove three folded refinements: entry-state keyed to what is *written* not code; a co-owned document assigned by who authors/maintains it (honoring the Step 3 → 5 promise); and the open-question/deliberation life (a *current* `govern` doc that decants into frozen records, refining current/frozen rather than breaking it).
  Artifacts under `blind-test/weft-*-round2.md`.
  (ADR-023)
- **Added:** `self-application.md` — the rewritten tutorial run on this project itself (dogfood), deriving our functions (`theory`/`writing`/`structuring`/`steering`/`imagine`), the controlled front-matter vocabulary, and our target source tree; supersedes the stale v3 `structure/applied.md`.
- **Proposed → Phase 08** *(enacted in alpha.3)*: root axis moves from `scope` (dominant `user`) to `provenance` (dominant `contributor`); `onboarding` provenance retired (a served order, not a producer function); add `steering/open-questions.md` (the pending deliberation: schema Decisions 1 & 2).
- **Closed:** Phase 07 — tutorial delivered and hardened, foundation reconciled, rewrite validated, system dogfooded on itself; records frozen.

## [v4.0-alpha.1] — front-end correction (Phase 07)

- **Changed:** the front-end is derived **functions-first** — a project's functions are laid flat, and its communities and their `distance` are derived from them, not assumed.
  (ADR-022; refines ADR-017)
- **Changed:** `distance` is **per discourse community** (per domain), not a single beginner/initiated axis.
- **Clarified:** a function *is* a provenance type — no function-vs-provenance tension; `synchronic ⇒ function`, `diachronic ⇒ its producer` (a project or a function's change-stream).
- **Added:** groupings are mutable; the phase log is grouped into three **eras** (naive sketch 01–05, refoundation 06–09, phase II later).
- **Changed:** the structuring tutorial (`structure/tutorial.md`) rewritten functions-first, now reaching placement; `foundation.md` reconciled.

## [v4.0-alpha] — refoundation & front-end (Phase 06)

- **Changed:** the theory is refounded on Ferraris's documentality; the three revised essays are the new basis (supersedes the v1–v3 basis).
  (ADR-014)
- **Changed:** perlocution has no zero — a constitutive floor plus an intention (formative/suasive/affective); forces are recognized cells, not primitives.
  (ADR-015; supersedes ADR-002)
- **Changed:** know/do/govern reframed as a register gloss; recommend & entail as extension-method examples.
  (ADR-016)
- **Changed:** audience for this project — roles collapse, `distance` (beginner/initiated) is the live axis, human/machine orthogonal.
  (ADR-017; supersedes ADR-006 for this project)
- **Decided:** source folder = producer's shelf; the reader surface is generated from the catalogue; the catalogue is the single pivot.
  (ADR-018; refines ADR-010)
- **Added:** the front-end laid flat — `foundation.md` and `roadmap.md` — and the restart strategy, Phase-I scope, and semantic line breaks.
  (ADR-019, ADR-020, ADR-021)
- **Note:** this is a refoundation in progress; the product refactors to the new vocabulary in Phase 08, the schema in Phase 09.

## [v3.2] — records & governance

- **Changed:** decision records regrouped **by phase** (`docs/phases/`) instead of a flat `decisions/` pile — provenance filing, not force filing.
  (ADR-012)
- **Added:** the central register `docs/ADR.md` (the `enact` act) and a permanent `steering` function owning the governance docs; frozen records now belong to their `phase-NN` project.
  (ADR-012)
- **Changed:** `provenance` on `docs/` split into `steering` (maintained) and `phase-NN` (frozen), replacing `maintenance`/`v3-redesign`.
  (ADR-012)
- **Added:** `decide` now has a forward **`entail`** face (act / justify / entail); the stance and template carry an explicit Entail section.
  (ADR-011)
- **Deprecated:** `docs/decisions/` — redirected, not erased.

## [v3.1] — content / docs disentangled

- **Changed:** split the *product* (content for users) from `docs/` (the repo's own internals for contributors).
  Root `dominant-community` corrected from `contributor` to `user`.
  (ADR-010)
- **Changed:** the product's axis renamed from `activity` to **scope** (one document vs the whole corpus).
  (ADR-010)
- **Changed:** `provenance` now names the maintaining function (`onboarding`/`writing`/`structuring`/`maintenance`) instead of a blanket `doc-system`.
  (ADR-010)
- **Added:** `docs/` with `ARCHITECTURE`, `CONTRIBUTING`, `CHANGELOG`, and this decision log.

## [v3] — self-similar reorganization

- **Changed:** flat `writing.md` / `structure.md` replaced by `write/` and `structure/`, each split by force (explain / instruct / recommend / mandate / describe).
  (ADR-007)
- **Added:** forces grouped under three doors in `write/forces/{know,do,govern-and-record}/`.
  (ADR-007)
- **Added:** `tutorial.md` — a `teach` on-ramp; obligations enforced by validation, not reading order.
  (ADR-009)
- **Added:** `axis` / `dominant-community` declared at each tree root.
  (ADR-008)
- **Moved:** the audience model into `structure/` (premise of the communication system).
  (ADR-006)

## [v2] — theory sharpening

- **Changed:** `formative: true|false` replaced by the `perlocution` typology (`locate`/`model`/`enable`/`convince`/`none`); `prove` and `decide` reclassified as `convince`.
  (ADR-002)
- **Added:** `recommend` as the twelfth force, on the deontic gradient instruct → recommend → mandate.
  (ADR-003)
- **Removed:** the `diataxis` frontmatter field — re-derived from `force` × `perlocution`.
  (ADR-004)
- **Clarified:** `verb` is a soft summary of the coordinate tuple; stored only when it diverges.
  (ADR-005)

## [v1] — foundation

- **Added:** the inscribed-act reframe — a document is an act with a `force`, and the force generates the writing.
  Eleven forces, move structures, readability patterns, frontmatter catalogue.
  (ADR-001)
