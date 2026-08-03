---
title: "Phase 10 — Reconcile governance & the frontmatter schema — detailed plan"
force: propose
verb: argue
register: govern
intention: suasive
view: synchronic
provenance: { type: project, id: phase-10-schema }
concerns: [steering, writing, structuring, theorising, imagining]
audience: [contributor, decider]
reader: H+M
status: draft
---

Phase 10 executes the decisions ratified on 2026-08-02 (see [`../../../steering/open-questions.md`](../../../steering/open-questions.md)) against the Phase-09 lint harness.
It is honestly a **rewrite pass** — many frontmatters change — plus a **governance cleanup**.
The schema decisions become one-line edits to `schema/frontmatter.schema.json`; the linter turns the settled fields from warnings into errors; the corpus is swept to match.

**Explicitly out of scope** (so the phase stays finite):

- `operationalizing` (the sixth function) — still open, not ruled on; if adopted it is its own small change, not this phase.
- deriving `constitutive` from `force × power` — deferred by decision; `constitutive` is a conscious stored `yes|no` for now.
- the **ways-of-working** convention (VCS topology, the Claude-Code/Cowork division) — a working convention between us, *not* a project record; it lives in `steering/ways-of-working.md`, outside this phase.
- Phase II design — that is Phase 11.

## Ratified inputs

- **⚑ Decision 1 — `intention` coarse** `{state, formative, suasive, affective}`.
- **⚑ Decision 2 — `register` derived**, not stored.
- **Register re-founding:** `register` is derived as `constitutive ? govern : direction-of-fit(force)` → `{know, do, govern}`; a new **stored** `constitutive: yes|no` (conscious).
- **Content-hash fixity:** an optional `hash:` sealing each frozen record.
- **ADR tiering:** an ADR only for a *standing obligation*; punctual actions are changelog lines; review the register by receivability.

## The ADR receivability review

Criterion (ratified): a record is a **receivable ADR** iff it installs a *standing obligation to verify and apply*; a punctual action is a changelog line.
Applying it to the register, keeping every record we merely *changed our mind on* (receivability is the only filter):

| Record | Verdict | Note |
|---|---|---|
| ADR-001…006, 008–018, 021, 022, 025–028 | **keep** | each installs a durable model, schema rule, vocabulary, naming, shelf, governance, or identity norm — standing obligations |
| ADR-007 (fractal reorg, forces by door) | **keep** | the *forces-by-door* convention is standing; the reorg half was execution |
| ADR-019 (restart strategy: front-end first, reorg in Phase 08) | **demote** | a one-time *sequencing/plan* decision — no standing obligation once executed; belongs in the roadmap/changelog, not the register |
| ADR-020 (scope Phase I; defer Phase II) | keep *(borderline)* | reads as a plan, but it is a standing guardrail we keep applying ("stay in Phase I") |
| ADR-023 (tutorial rewrite) | keep *(borderline)* | event-flavoured, but it carries durable design commitments (relevance-not-recurrence, organize-for-author, `imagine`) |
| ADR-024 (producer shelf: dissolve `docs/`) | keep | the *axis = provenance* half is a standing norm; the "dissolve `docs/`" half was punctual (a changelog matter) |

Net: **one demotion (ADR-019)**; three borderlines kept.
Demotion mechanics: move ADR-019's content to a roadmap "plan changes" note (or a changelog line), remove its register row, and record the demotion — the generated ordinal (ADR-028) absorbs the gap without renumbering.

## Workstreams

| # | Workstream | Output |
|---|---|---|
| **T1** | **Schema encoding.** In `schema/frontmatter.schema.json`: `intention` → coarse enum; add `constitutive: {yes, no}` (required, no implicit default — the conscious choice); encode the `force → {know, do}` direction-of-fit table; declare `register` **derived, not stored**; add optional `hash`. | updated schema |
| **T2** | **Corpus sweep.** `intention` fine → coarse everywhere; **remove stored `register`**; add `constitutive` to every catalogued doc (a real per-document judgement — `yes` for the constitutive-force records, `no` for the rest). A script drives it; gated by `frontmatter_lint` + `linkcheck`. | rewritten frontmatters |
| **T3** | **Register/constitutive re-founding ADR.** Write it: register derived (`constitutive ? govern : direction`), `constitutive` a conscious stored `yes|no`, force × power deferred, three doors kept & re-founded. Supersedes the register part of ADR-016; refines/supersedes that of ADR-025. | new ADR |
| **T4** | **Content-hash fixity.** `scripts/hash_seal.py` (sha256 over canonical frontmatter-minus-`hash` + body, written on freeze), `scripts/hash_check.py` (verify), schema `hash` field, wired into `scripts/check.py`. | hash tooling + ADR |
| **T5** | **ADR tiering & register cleanup.** Relax `CONTRIBUTING`'s trigger to "any decision that creates a standing obligation → ADR"; write the tiering ADR; demote ADR-019 per the review. | CONTRIBUTING, ADR, roadmap |
| **T6** | **Promote the linter & close.** Turn the now-settled fields (`intention` coarse, no stored `register`, `constitutive` present) from warnings into errors in `frontmatter_lint.py`; close ⚑ 1 & 2 in `open-questions.md` (decant to the ADRs); realign `steering/` + `phases/` frontmatters; regenerate the register ordinal; fix the stale roadmap `phase:` field; dedupe the round-2 blind-test; note the zombie `git clean` for the working tree. | green gate, closed questions |

## Verification / definition of done

- `frontmatter_lint.py` **errors** on the settled fields (coarse `intention`, no stored `register`, `constitutive` present) and still warns on anything genuinely undecided.
- `scripts/check.py` is green (markdownlint, frontmatter, ULID, hash, links); ideally extended with a `git status --porcelain` assertion so untracked cruft can no longer pass silently.
- ⚑ Decision 1 and 2 are **closed** in `open-questions.md`, decanted into their ADRs.
- The register carries no non-receivable record (ADR-019 demoted); the tiering rule is in `CONTRIBUTING`.
- Every frozen record can be sealed and re-verified by `hash_check.py`.

## Who does what

The **decisions** in T3/T5 (the re-founding ADR, the tiering, the demotion) are methodological — authored here.
The **sweeps and tooling** in T1/T2/T4/T6 are mechanical and iterative against the gate — Claude Code's home, with this plan and the ADRs as the spec.
