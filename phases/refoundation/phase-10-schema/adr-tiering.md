---
title: "Decision — ADR tiering: a record earns an ADR by installing a standing obligation"
id: 01KZ2EQ400A2KMKSQWPECHM3ED
slug: adr-tiering
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-10-schema }
constitutive: yes
concerns: [steering]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:6584f691bd970c6ff3fe0007711c99942ca00fabceba5de9bd121252f6108634
---

## Status

accepted — 2026-08-03.
Refines the ADR trigger installed by ADR-012 (decision records grouped by phase, the central register) and stated in `CONTRIBUTING`.

## Context and forces in play *(justify)*

`CONTRIBUTING` triggered an ADR on "any design decision that changes the theory, the schema, the force repertoire, or the tree shape".
That is a *subject-matter* test, and subject matter is the wrong axis.
It let in decisions that were purely punctual — do this thing, once, now — and it gave no guidance on the many decisions that are consequential without touching those four subjects.

The cost of the wrong test is not tidiness.
A register that mixes standing norms with executed actions cannot be *read as a set of obligations*: a contributor consulting it to learn what still binds them has to re-judge every row.
The register stops being receivable.

The right axis is what the decision *does to the future*.
A decision that installs a **standing obligation to verify and apply** keeps acting after it is executed — it constitutes a norm.
A **punctual** action (move a folder, rename a file, sequence the next two phases) is complete when done; recording it is history, and history is what the changelog is for.
This is the same `constitutive` distinction the register re-founding turns on, applied to the register itself.

## Decision

1. **The ADR trigger is receivability, not subject matter**.
   A decision earns an ADR **iff it installs a standing obligation to verify and apply**.
   A punctual action is a changelog line, with no ADR.

2. **`CONTRIBUTING` is relaxed accordingly** — from the four-subject list to the standing-obligation test.

3. **The existing register was reviewed by that criterion**, keeping every record we merely later *changed our mind on*: receivability is the only filter, and a superseded norm was still a norm.
   Twenty-seven of twenty-eight records pass.

4. **ADR-019 (restart strategy: front-end first, principles now, reorg in Phase 08) is demoted**.
   It sequenced a plan; once executed it obliges nobody.
   Its row leaves the register; the plan content it carried is held by the roadmap.

5. **Three records are kept as acknowledged borderlines**, named here so the judgement is auditable rather than invisible:
   - **ADR-007** (fractal reorg) — the reorg half was execution, but the *forces-by-door* convention still binds.
   - **ADR-020** (scope Phase I, defer Phase II) — reads as a plan, but "stay in Phase I" is a guardrail we keep applying.
   - **ADR-023** (tutorial rewrite) — event-flavoured, but it carries durable design commitments (relevance-not-recurrence, organize-for-author, `imagine`).
   - **ADR-024** (producer shelf) — the "dissolve `docs/`" half was punctual; the *axis = provenance* half is standing, and that half decides it.

6. **Demotion does not erase a record**.
   The frozen file stays where it is, unedited — a demoted decision was still taken, and rewriting it would be the erasure `CONTRIBUTING` forbids.
   What changes is its membership in the register.

7. **The display ordinal absorbs the gap**.
   Ordinals are generated (ADR-028), not identities, so nothing is renumbered and every existing reference to "ADR-020" still resolves.

## Entail — what follows

- `CONTRIBUTING`'s ADR rule now reads "any decision that creates a standing obligation".
- `steering/ADR.md` loses its ADR-019 row and gains a note recording the demotion and pointing here.
- `steering/roadmap.md` gains a "plan changes" note carrying the restart strategy, alongside the Phase-09 insertion already recorded there.
- The register is now readable as a set of live obligations, which is what makes it worth consulting.
- Future contributors have one question to answer, not four: *does this oblige anyone tomorrow?*

## Honest limit

"Standing obligation" is sharper than "changes the schema" but it is still a judgement, and the borderlines above show it bending under pressure.
Three of the four kept-borderlines are kept because a *part* of the record is standing while another part is punctual — which is really evidence that those records bundled two decisions each.
The honest fix would be to write smaller records, one obligation per record; the test cannot repair records that were already written mixed.

We also reviewed the register once, at one moment, against a criterion invented at that moment.
A criterion applied retroactively by its own authors to their own records is not an independent audit, and a second reviewer would very likely demote differently.
