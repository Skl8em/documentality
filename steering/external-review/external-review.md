---
title: "External review — the project read through The Life of Projects (2026-10-07)"
force: propose
verb: argue
intention: suasive
view: diachronic
provenance: { type: function, id: steering }
constitutive: no
concerns: [theorising, operationalizing, writing, structuring, codifying, steering]
audience: [contributor, decider]
reader: H+M
status: stable
---

This is an adversarial review of the whole project, taken on 2026-10-07 at commit `236cce1`, read through the integrative review `theorising/the_life_of_projects.md` added in that commit.
It was written by an AI session (Claude Opus 5.5) at the maintainer's request, with the repository and the paper as its only inputs, so it is external to the project's history but not to its means of production.
It decides nothing: each recommendation awaits a ruling by the maintainer, and the three flagged as rulings are listed in the closing section, *Candidate rulings*.
Line numbers in the links refer to commit `236cce1` and will drift; the commit is the reference.

The brief was to be forgiving towards missing work that is already planned, sharp about what exists — the code and its documentation especially — and sharp about what is missing and not even planned, and to question whether the approach can deliver what the project aims at.

## Verdict

In 94 commits and twelve phases the project has built a careful apparatus for keeping its own representations of itself consistent, and almost nothing that confronts the product with a reader other than its author.
In the paper's terms, the ostensive — roadmap, phase ledger, ADR register, gate — keeps being refined, while the product has had no performance outside the project: no adopter, no human cold reader, and none of the maintainer's sibling projects uses it (the `weft` blind-test subject holds a single spec file).

The irony is that the project's own theory already knows better.
[`the_documentary_system.md`](../../theorising/the_documentary_system.md#L105) makes the records continuum the "governing frame" of the archival system, and [its section 2](../../theorising/the_documentary_system.md#L32) cites Scott's case for abandoning the record-group model.
The implementation follows the lifecycle and record-group models that essay sets aside, and the next planned phase is named *Life cycle*.

**The lens has limits of its own.**
The paper's citations were not verified for this review, and several of its quotations need checking against the originals.
More importantly, the paper's own caveat — solo practice is "theorized mostly by extrapolation" — applies to everything here, and it cuts against the project's theory as much as against this review (finding 1e).

## 1. The premises

### 1a. Naur against the project's founding wager — not addressed, not planned

The whole project wagers that a document with the right coordinates carries enough of the project's theory for a stranger, and later a machine, to act on it.
Naur's thesis (1985) is that a program's theory lives in the people who built it and cannot be re-established from documentation; the thesis is contested but serious.
Naur appears nowhere in the repository outside the new paper.
Yet the Phase II design assumes generation from the frontmatter, and the maintainer's broader goal is that an agent could execute a process from its documentation alone; both need an explicit position on what documentation can and cannot carry.
Meanwhile the theory of this project sits in one person and in stateless AI sessions: 65 of the 94 commits are co-authored by Claude.
That is a bus factor of one, which is exactly the threshold at which the paper's fourth recommendation says to act.

### 1b. Phase II has already happened, unacknowledged

[`foundation.md`](../foundation.md#L27-L33) defers the AI to a future "new discourse community" whose front-end is to be re-run once Phase I is complete.
The AI is already the main co-producer.
The gate's design is its imprint: every failure line carries a `fix:` clause, its reader is assumed to have "no memory of any prior turn", and every fact is declared once and cross-checked.
That is Conway's law with one human and one amnesiac agent as the communication structure, and it may be the most genuinely original thing in the repository — but the foundation's account of the project's communities misdescribes the present.
[`audience.md`](../../structuring/audience.md#L50) states the machine is "never `decider`"; the machine drafts the decision records the maintainer rules on, and that sentence needs at least a qualification.

### 1c. Lifecycle where the theory says continuum — planned work, but its frame is being fixed now

The inventory the life-cycle phase was created to answer is not a set of missing rulings; it is the continuum leaking through a lifecycle model.

- The fixity seal cannot tell an annotation from an edit.
- `status` carries three different state machines.
- Ten working documents are `view: synchronic` under a project's provenance.
- ADR-036 to ADR-038 were written after the decisions they record.

A record keeps being drawn into new contexts, which is what the continuum calls pluralisation.
A phase that starts from "which states does a document pass through" will refine the lifecycle model the project's own essay demotes.
The recommendation is to reframe the phase before it starts, around the essay's own position: which dimensions of a record's continuing life the catalogue records.

### 1d. The record-group model the project's own essay rejects — not planned

Provenance is a single `{type, id}` fused into each file and mirrored by its folder.
The project has refiled itself repeatedly: `docs/` dissolved, `write` renamed `writing` along with every other gerund rename (ADR-027), and the function set grown from five to six to seven.
That is precisely the cost Scott says the record-group model imposes at every reorganisation.
The series system's move — describe the context separately from the records, and relate them by many dated links — has no counterpart in the schema.

### 1e. Institutional theory applied to a one-person project

Several parts of the theory come from institutions and are applied here without adjustment:

- an archive kept for a "future examiner", who is never named for this project;
- three roles that "every project, whatever its domain" has ([`audience.md`](../../structuring/audience.md#L15));
- a binding rule to reference project states by pinned submodule ([`structuring/rules.md`](../../structuring/rules.md#L28)), when the schema's own rationale for `pin` calls it "structurally unreachable here".

[`foundation.md`](../foundation.md#L91) says the project is "small, and honest about it", yet it runs seven functions, a forty-row decision register, ULIDs, fixity seals and a phase ledger.
The structuring tutorial tells a solo author they "certainly do not need this tutorial's full ceremony" ([`tutorial.md`](../../structuring/tutorial.md#L123)); the project does not apply its own cost rule to itself.

### 1f. Plans as control, and the metric becoming the goal

**Reference class.**
The roadmap has absorbed four insertions — Phases 09, 11 and 12, then the life-cycle phase — plus the deployment phase.
Each tooling phase paid the previous phase's debt and opened the next one.
On the project's own record, the life-cycle phase is likely to open another.

**More instruments, not looser plans.**
The response to emergence has been further apparatus: ADR-038 (unstarted work unnumbered), the phase ledger, the `phase-state` check.
Phase 12 alone added roughly 1,400 lines of Python and fixtures to keep the repository's mentions of its own phase consistent.

**The concrete Goodhart case.**
The "New here?" block of the root README ([`README.md`](../../README.md#L20-L26)) has been broken since 2026-07-25: it reads "Go to `structuring/*to be defined*`", ends on "Go to ...", and carries a stray backtick inside a link label.
It stayed broken for 74 days, through 17 commits to that file, on a document marked `status: stable`, while the gate grew to 24 entries and stayed green throughout.

### 1g. A closed vocabulary against the behaviour of genres

Genres hybridise and drift (Yates and Orlikowski), and a boundary object needs local plasticity to work (Star and Griesemer).
A newcomer's first document needs nine fields, two of which — `constitutive` and `intention` — cannot be filled without the theory.
Nothing observes how the forces and fields drift in use, because there is no use to observe.

## 2. What exists: defects in the code and its documentation

### The product contradicts itself on where documents go

- [`structuring/setup.md`](../../structuring/setup.md#L23-L34) lays out `docs/` by force: `reference/`, `guides/`, `guidelines/`, `tutorials/`, `decisions/`.
- [`structuring/defaults.md`](../../structuring/defaults.md#L17) says to organise in-repo docs by component.
- [`structuring/tutorial.md`](../../structuring/tutorial.md#L233) says provenance comes first and "never `docs/know/build/`".
- The tutorial files CHANGELOG as "`govern`, current and append-only" ([line 224](../../structuring/tutorial.md#L224)); `setup.md` files it as "`account` — frozen, append-only (diachronic)" ([line 32](../../structuring/setup.md#L32)).

A user who follows `setup.md` breaks the tutorial.

### The first document a newcomer writes carries the "suspect pair"

The [orient template](../../writing/forces/know/orient/template.md) and step 3 of the [writing tutorial](../../writing/tutorial.md#L40) set `view: synchronic` with `provenance.type: project`.
[`writing/frontmatter.md`](../../writing/frontmatter.md#L82) calls that combination "a suspect pair; allow only knowingly".
The tutorial's claim to take "about ten minutes" ([line 17](../../writing/tutorial.md#L17)) has never been tested on anyone.

### Validation rules stated on the page and enforced by nothing

The *Validation rules* section of [`writing/frontmatter.md`](../../writing/frontmatter.md#L82) lists checks that `scripts/frontmatter_lint.py` does not perform:

- `status: deprecated` requires `superseded-by`;
- `view: synchronic` with `provenance.type: project` is flagged;
- a document read by a machine satisfies the self-sufficient-chunk rules;
- a project record is not rewritten after closure (only sealed records are protected).

Nothing on the page separates the enforced rules from the aspirational ones.
Commit `5f9eed9` corrected exactly this defect in `operationalizing/view.md`, in that file only; the class of defect remains.

### An accepted decision contradicts the linter

[ADR-008](../../phases/naive-sketch/phase-03-reorganization/ADR-008-tree-axis-declaration.md) declares `axis` and `dominant-community` "at each tree root".
[`frontmatter_lint.py`](../../scripts/frontmatter_lint.py#L154) hard-codes `is_root = path == "README.md"` and fails `axis` anywhere else.
The sub-axis "by door" that the root README declares for `writing/forces/` therefore cannot be declared where the rule says it should be.
The literal is also an instance value inside the engine, exempted from the engine/config seam check by statement in [`codifying/gate.md`](../../codifying/gate.md) rather than by design.

### Binding rules the corpus itself breaks

- [`writing/rules.md`](../../writing/rules.md) forbids cross-section anaphora in any `H+M` document; [`writing/frontmatter.md`](../../writing/frontmatter.md#L24), an `H+M` document, says "the table below" on line 24 and "the vocabulary above" on line 84.
- The same rules require one term per concept; `writing/concepts.md` equates the doors with the register, and the structuring tutorial uses *activity* and *function* interchangeably.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) says a contribution that violates the product's rules "is rejected"; nothing checks either rule, and nothing was rejected.

### The project does not apply its own mandate to itself

[`CONTRIBUTING.md`](../CONTRIBUTING.md#L24) states that "an undocumented standing obligation is reverted — the ADR *is* the decision".
ADR-036 to ADR-038 ran undocumented for up to eleven days and were then written up retroactively ([`ADR.md`](../ADR.md#L65)), not reverted.
Either the rule is false as written, or those three records are accounts of decisions presented as the decisions themselves — retrospective sensemaking in Weick's sense, filed under `decide`.

### `linkcheck.py` cannot link the new paper

- A link to `theorising/the_life_of_projects.md` is reported broken both raw and percent-encoded (both tested).
- The CommonMark form for such a path, `<…>`, is skipped as a "placeholder" ([`linkcheck.py`](../../scripts/linkcheck.py#L33)), so a correct link would go unchecked.
- Anchors and reference-style links are never checked.

That is why this review names the paper in code text rather than linking it.

### The theory shelf is outside every check

`theorising/` is excluded wholesale from the frontmatter linter and from markdownlint, so the shelf the whole project rests on has no metadata, no index, and now a filename that breaks the slug convention.
How a new theoretical input enters the project — a reading note, an ADR, its consequences traced into the documents it affects — is undefined, and not planned.
The only precedent is ADR-014, which took a whole refoundation phase.

### Smaller stale artefacts

- [`README.md`](../../README.md#L40) still describes `theorising/` as "the three essays + readability patterns".
- [`environment.md`](../environment.md) describes the gate as four checks; it runs 24 entries.
- `CONTRIBUTING.md` still uses the pre-gerund `../../write/` and `../../structure/` names as link text.
- [`imagining/README.md`](../../imagining/README.md#L17) still places the Phase II design at Phase 10; `phase-state` only flags numbers ahead of the ledger, so a stale backward reference passes.
- CI installs Nix with `DeterminateSystems/nix-installer-action@main` ([`checks.yml`](../../.github/workflows/checks.yml#L17)), which contradicts the "bit-for-bit" toolchain claim and is not in the technical-debt register.

### What is done well

The [technical-debt register](../technical-debt.md), the fixtures-first discipline, the *Plan changes* log in the roadmap, and the *What the gate does not establish* section of [`codifying/gate.md`](../../codifying/gate.md) are rigorous and honest, and the Phase 07 blind tests were the right instinct.
The problem this review raises is what that rigour is pointed at, not its quality.

## 3. What is missing and not planned

- **A definition of "Phase I complete".**
  None exists anywhere in the repository, yet the Phase II design is gated on it.
  With no stopping rule (Rittel and Webber) and four insertions so far, deferral is unbounded.
- **Any test of the product's empirical claims**: "about ten minutes", conflation of the two systems as "the root failure of most wikis", "a short mandate is an obeyed mandate".
- **Any preservation of the project's theory beyond text** (Naur), and any succession plan.
- **A migration path for an adopter's frontmatter** when the vocabulary changes, which on this project's record is the normal case.
- **The cheapest second consumer.**
  The technical-debt register says the engine/config seam "cannot be tested without a second consumer"; the maintainer's own projects are the cheapest one available, and adopting the system on `weft` now is the affordable-loss move.

## 4. Can the approach deliver what the project aims at?

The aim is to let *someone* structure and write a project's documentation.
Dogfooding at zero distance — the author as the only user, fully initiated — can test consistency but not usefulness, because the product's target reader is `distance: far`.
The gate measures consistency, so the project keeps optimising what its method can observe.
Without a performance outside itself, further phases will make the product more coherent without making it more likely to be useful.

Recommended, in order:

1. Repair the root README's front door and reconcile `structuring/setup.md`, `structuring/defaults.md` and the structuring tutorial; both mislead a reader today.
2. Before the life-cycle phase, run one human cold reader on the writing tutorial.
   It does not need the deployment phase.
   The ordering of those two phases was ruled on 2026-10-07; the reference-class and Naur arguments in findings 1a and 1f were not part of what that ruling weighed.
3. Reframe the life-cycle phase around the records continuum, as the project's own third essay already argues, before it starts.
4. Add no new gate check until someone other than the author has used the product.
5. Rewrite the communities section of `foundation.md` to admit the AI as a current co-producer, and take a written position on Naur.
6. Define "Phase I complete" as an observable condition.

## Candidate rulings

Three of the recommendations are standing decisions rather than tasks, and are flagged for the maintainer's ruling; none is decided here.

- A moratorium on new gate checks until the product has a non-author user.
- A definition of "Phase I complete".
- Reframing the life-cycle phase around the records continuum.
