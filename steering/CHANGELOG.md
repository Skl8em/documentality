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

## [v4.0-alpha.14] — Phase 11 T4: referential integrity

- **Added:** `scripts/ulid_check.py` now validates `supersedes`/`superseded-by` corpus-wide, not just `id`.
  Three checks: every non-null reference resolves to some record's `id` or filename stem (the pre-ULID reference form, e.g. `supersedes: ADR-001-inscribed-act`); supersession is symmetric, matching what `schema/frontmatter-rules.yaml` already documented (`superseded-by` as "the inverse of `supersedes`, kept symmetric") but never enforced; and every row of the central register ([`steering/ADR.md`](ADR.md)) agrees with the `superseded-by` of the record its link points at.
  A `<...>` placeholder (a force template's SPECIMEN frontmatter) is not a reference and is skipped, the same test `hash_seal.is_frozen` already used for a specimen `provenance.id`.
- **Fixed:** three real asymmetric references, found by the new check, not suspected: ADR-001, ADR-002 and ADR-006 (`phases/naive-sketch/`) each carried `superseded-by: null` although the register and their superseding record (ADR-014, ADR-015, ADR-017) had already recorded the other direction.
  Retrofitted `superseded-by` on the three, the same way [`hosting-codeberg-github-mirror.md`](../phases/refoundation/phase-10-schema/hosting-codeberg-github-mirror.md) already had it added when [`hosting-github-canonical.md`](../phases/refoundation/phase-10-schema/hosting-github-canonical.md) superseded it — the pointer is kept live, only the decision's own reasoning is dated-fixed.
- **Added:** [`scripts/test_ulid_check.py`](../scripts/test_ulid_check.py), fixtures on the same model as `test_frontmatter_lint.py` — a dangling reference, a broken symmetry, a register disagreement, a `<...>` placeholder, a list-valued reference — run by the gate (`ulid-test`) before the corpus check it gates.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.13] — Phase 11 T3: YAML source, generated JSON

- **Changed:** the schema's source of truth is now [`schema/frontmatter-rules.yaml`](../schema/frontmatter-rules.yaml) — hand-edited, `#` comments allowed, replacing the `"//"` key JSON used as a comment substitute.
  [`scripts/generate_schema.py`](../scripts/generate_schema.py) compiles it to `schema/frontmatter-rules.json`, the artifact `frontmatter_lint.py` and any other dependency-free reader actually loads; the two files carry identical data.
  This retires `schema/frontmatter.schema.json`, whose name claimed a JSON Schema dialect the hand-written validator never implemented.
- **Added:** a drift check — `scripts/generate_schema.py --check` regenerates the JSON in memory and diffs it against the committed file, failing loud on any mismatch.
  Wired into `check.py` as `schema-drift`, run before anything that loads the generated file, so a schema edit can never go unenforced because the generated artifact was left stale.
- **Fixed:** compiling the YAML source with a plain `yaml.safe_load` turned `error_enums.constitutive: [yes, no]` into `[true, false]` — YAML 1.1's implicit bool resolution, the exact failure mode Phase 11 T2 fixed for frontmatter *documents*, reappearing in the schema's own source.
  `scripts/generate_schema.py` now loads through `yaml_frontmatter.StrictLoader` (renamed from the module-private `_Loader`, now an explicit shared export) — the same string-only, duplicate-key-errors loader `yaml_frontmatter.py` already used, so this class of bug is fixed once, not twice.
- **Changed:** the two `still_open` cross-references in [`steering/open-questions.md`](open-questions.md) now point at `schema/frontmatter-rules.yaml`.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.12] — Phase 11 T2: parse YAML with YAML

- **Changed:** frontmatter is parsed as **real YAML**, through one shared reader, [`scripts/yaml_frontmatter.py`](../scripts/yaml_frontmatter.py), on `pyyaml` pinned in the devShell (`python3.withPackages`, no new flake input).
  It replaces three hand-rolled comma-and-colon splitters: the one in `frontmatter_lint.py`, and the one duplicated in `slug_check.py` and `ulid_check.py` (which `slugify_names.py` imported).
  `hash_seal.is_frozen` reads its three fields through it too; the seal's line-based canonical form is untouched, and every seal still verifies.
- **Ruled:** two departures from `yaml.safe_load`, each for a failure it would otherwise introduce.
  Scalars stay strings and only `null` resolves, because YAML 1.1 reads `constitutive: no` as a boolean, an all-digit ULID as an integer and a date as a date — against a schema whose vocabulary is strings.
  Duplicate keys are errors at any depth, because pyyaml silently keeps the last one.
- **Added:** [`scripts/test_frontmatter_lint.py`](../scripts/test_frontmatter_lint.py), fixtures on the MD100 harness model, run by the gate before the corpus checks.
  Nine of its ten lint cases fail against the old parser: five documents it wrongly passed (a field hidden by indentation, a plain scalar folded onto the next line, a duplicate key at the top level and inside an inline map, an unterminated quote), one it failed for the wrong reason, and three valid documents it rejected.
  The tenth pins the string-typing policy.
  In the corpus, the only value the old parser misread was the root README's `axis`, which carried its trailing `# comment` inside the value; nothing checked it, so nothing failed.
- **Changed:** `check.py` re-runs itself under `nix develop` when its interpreter lacks `pyyaml`, and fails loud without nix.
  The validators that import the parser no longer claim "stdlib only".
  `ulid.py`, `rename_doc.py` and the MD100 harness still make that claim, and still truthfully, so their comments are kept; the plan's T2 row listed them by mistake and is corrected.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.11] — Phase 11 T1: close the frontmatter vocabulary

- **Changed:** `frontmatter_lint.py` now **rejects any field outside `required` ∪ `optional_fields` ∪ `root_only_fields`**, and `load_schema()` refuses to start if an `optional_fields` entry has no rationale string — "declared" and "justified" are now the same act.
  `schema/frontmatter.schema.json`'s `optional_fields` is rewritten one key per field (it previously bundled several field names into a single description, e.g. `supersedes` silently covering `superseded-by`, `retention`, `pin`, `order`, and `phase`), each now carrying its own rationale.
- **Ruled:** the four vocabulary cases the gate could not see, checked against the two documents that actually define the intended vocabulary (`writing/frontmatter.md`'s field table and `operationalizing/README.md`'s coordinate inventory), not against corpus habit alone.
  `pin` is **declared and justified** — `writing/frontmatter.md` already names it as a real coordinate ("fixity anchor for a cross-project reference"); it is unused only because this repo is a single-project (topology A) instance and never instantiates the `projects/`-submodule topology it fixes a reference into.
  `phase` (2 documents, `steering/roadmap.md` and `steering/foundation.md`) is **declared and justified** and **added to `writing/frontmatter.md`'s field table**, which had drifted: `git log -p` shows the field is bumped forward as a steering document is reconciled to a later phase, not fixed at creation — a real, machine-checkable coordinate the reference document had simply never recorded.
  `note` (4 documents) is **dropped**, and reconsidered on stronger grounds than "undeclared": `writing/frontmatter.md` states the frontmatter carries only "hard coordinates not derivable from one another" and exists so "the machine" gets a document's coordinates "without a human reading them" — `note` is free prose nothing reads, present in neither canonical field list.
  Each of the 4 documents' `note:` value is moved into its own opening prose instead of dropped outright.
  `review` (1 use, `steering/roadmap.md`) is **dropped**: `git log -S"review:"` traces it to a single silent addition in the Phase-10 sweep commit, with no explanation anywhere and no field-table entry.
  `order` (0 uses) is dropped for the same absence of any documented rationale.
  The single `review: 10-schema` line is removed from `steering/roadmap.md`.
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))

## [v4.0-alpha.10] — Phase 11 inserted: tooling hardening

- **Planned:** **Phase 11 — tooling hardening**, inserted before the Phase-II design.
  Phase 10 reconciled the schema and enforced it, but enforcement stops at the nine required fields and six enums: the vocabulary is open (`note` and `review` sit in the corpus declared nowhere, while `order` and `pin` are declared and unused), the YAML parser is hand-rolled and mis-parses silently instead of failing, and no identifier is checked to point at anything.
  Hardening is placed first because Phase II generates *from* the frontmatter, and generation inherits every weakness the catalogue carries.
  A sequencing decision, so it is held here and in the roadmap rather than in the ADR register (ADR-032).
  ([plan](../phases/refoundation/phase-11-tooling-hardening/plan.md))
- **Changed:** **unstarted phases are no longer numbered.**
  Inserting this phase moved a forward reference for the second time (the Phase-09 insertion did it first), so the roadmap now names and orders work it has not begun rather than giving it an ordinal it cannot keep.
  A phase takes its number when we tackle it — the same move the ADR register already makes, where the ordinal is a generated display label and the identity lives elsewhere (ADR-028).
  Referring to unstarted work by number is what made both insertions a renumbering sweep; the sweeps were the symptom, the numbering was the cause.
- **Recorded:** folding the frontmatter validator into markdownlint was considered and **rejected on evidence** — a custom rule receives frontmatter as raw text, no YAML parser is reachable from it, and the VSCode extension loads custom rules in its own Node context, so any external dependency would pass in CI and fail in the editor.
  Referential integrity is also corpus-level, which markdownlint's per-file model cannot express.
- **Changed:** stale phase claims corrected, since a misleading comment is worse than none — the root `README` and `phases/README.md` both still announced Phase 10 as *next* and Phase 11 as the Phase-II design, and the roadmap's own `phase:` field still read `08-refactor`.

## [v4.0-alpha.9] — hosting reversed: GitHub canonical

- **Decided:** the canonical repository is **GitHub**, and there is **no mirror** — superseding the Codeberg decision of alpha.7, which was recorded but never enacted (no Codeberg repository was ever created).
  Ground: Codeberg restricts predominantly AI-generated repositories and this one is substantially AI-assisted, so the sovereignty #029 sought there would have been borrowed tolerance, not sovereignty.
  The freedom argument is relocated, not withdrawn — it is deferred to a **self-hosted Forgejo instance**, which becomes canonical when it exists.
  ([decision](../phases/refoundation/phase-10-schema/hosting-github-canonical.md); register #034, supersedes #029)
- **Added:** host-independence as a **standing obligation** — no GitHub-only automation may move into `scripts/check.py`, so the eventual migration stays a remote change plus a CI port.
- **Fixed:** the `sentence-per-line` fixture harness matched nothing.
  Its violation regex expected a severity token between the column and the rule name that markdownlint-cli2 does not emit, so every positive fixture parsed as "no violations" and every negative one passed vacuously — the MD100 rule itself was correct all along (18/18 once the regex was fixed).
- **Removed:** `.github/instructions/mermaid.instructions.md` — vendor boilerplate that carried no catalogue frontmatter and failed the gate.

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
