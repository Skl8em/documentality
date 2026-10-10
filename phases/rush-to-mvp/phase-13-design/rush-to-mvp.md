---
title: "Decision — Phase I closes by ruling, and the next era is a rush to a minimal viable product"
id: 01M4FM6C3CASQQB5BRBN7C3BGE
slug: rush-to-mvp
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-13-design }
constitutive: yes
concerns: [steering]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: ADR-020-scope-phase-i
superseded-by: null
hash: sha256:b55e08ec70dc6e29a70c731663e08e850844ef7daffb145bedf983d9a3df0cc6
---

## Status

accepted — 2026-10-09, by the project owner, at the close of Phase 12.
It supersedes [ADR-020](../../refoundation/phase-06-refoundation/ADR-020-scope-phase-i.md), which stays frozen and unedited apart from the link back to this record.
It clears the [ADR-032](../../refoundation/phase-10-schema/adr-tiering.md) test: it changes what the project works on and installs one standing restriction, on new gate checks, that every contributor must apply.

## Context and forces in play *(justify)*

ADR-020 restricted work to Phase I and deferred Phase II until Phase I was complete, when the structuring front-end would be re-run for the AI discourse community.
Three things have changed since.

**Phase I has no stopping rule, and twelve phases show it does not stop.**
Nothing in the repository defined "Phase I complete".
The roadmap absorbed four insertions, and each tooling phase paid the last one's debt while opening the next ([external review](../../../steering/external-review/external-review.md), findings 1f and 3).
The neutral specification the project wrote for its own Phase 07 blind test did name an exit — "Phase I is left when it reaches a minimal-viable-product state … there is no mechanical rule beyond that judgment" ([self-spec](../../refoundation/phase-07-structuring-tutorial/blind-test/self-spec.md)) — and nobody ever made that judgment.

**Phase II has already started without being admitted.**
An AI agent has co-produced most of the repository, and the gate is built for a machine reader: every failure line carries its `fix:`, and the reader is assumed to have no memory (review, finding 1b).
Deferring the "new discourse community" while working with it every day means the community shapes the product without the product ever being designed for it.

**The product has never left its author.**
No adopter, no human cold reader, and no other project of the maintainer's has used it; the `weft` blind-test subject holds a single spec file.
The gate measures consistency, so the project kept improving what its method could see (review, finding 4).

The project owner's statement of purpose settles what the next step is for: the project is about understanding what one wants from project documentation and how to teach it to agents, and the next two things are deploying it into other projects and the agent machinery that goes with it.

## Options considered

- **Keep ADR-020: finish Phase I, then design Phase II** — consequence: the life-cycle phase, then deployment, then a design phase, before any agent uses the product; on the project's own record, each opens another.
- **Close Phase I by ruling and design Phase II first, by re-running the front-end** — consequence: one more phase of design, a priori, for a community the project already works with daily.
- **Close Phase I by ruling, and let the next era be bounded by an observable result** — consequence: what the agent community needs is found by watching an agent use the product on a real project, not designed in advance; the cost is accepting known inconsistencies the project would earlier have stopped for.

## Decision

1. **Phase I closes by ruling, with Phase 12.**
   The judgment the Phase 07 self-specification called for is made by the project owner: the product is usable enough to be tried on someone other than its author.
   ADR-020's deferral of Phase II is superseded.

2. **The next era is the *rush to MVP*, and it has two deliverables.**
   - **Adoption** — an external project can install the machinery (the gate, the linter, identifiers, the schema) and is guided through populating what the framework needs to run, frontmatter included.
   - **The agent kit** — an external project can install what an agent needs (skills, agents, instructions) to amend and expand that project's documentation according to this product.

3. **The era ends on an observable condition, not on completeness.**
   On `weft`, one command installs the system and its gate is green on the scaffold.
   A fresh agent session given only the installed kit writes `weft`'s orient, the documents carrying the theory of its code, and one decision record; all pass the gate, and the project owner judges them right.
   A modification request that `weft`'s design refuses is questioned by the agent, not carried out.

4. **The front-end is not re-run in advance.**
   ADR-020's re-founding for the AI discourse community is replaced by the pilot: what the agent needs is observed on `weft`, and the front-end is re-run afterwards if the evidence calls for it.

5. **No new gate check whose object is the project's own state, for the duration of the era.**
   A check about this repository's phases, register or roadmap is out; a check that an adopter's gate runs is in.
   This adopts the review's proposed moratorium in a narrower form.
   The review would have frozen every new check until a non-author had used the product, which would also block the adoption work itself.

## Entail — what follows

- The roadmap gains the era and its phases, and the phase ledger opens it; the planned phases that the era makes obsolete are parked, which is a sequencing change recorded in the [roadmap](../../../steering/roadmap.md), not here: the life-cycle phase, the deployment phase (absorbed by the era), and the design of Phase II (superseded by point 4).
- `steering/foundation.md` §1 stops describing Phase II as deferred.
- A known inconsistency that does not block an adopter or an agent is recorded and left, not fixed.
  Fixing it is not a reason to delay the MVP.
- The defects in what an agent will *read* are the exception.
  An agent applies a page literally, so a wrong product page becomes wrong documentation in every project that installs the kit; those are fixed first.

## Honest limit

**The MVP condition is judged by the author, on the author's own project.**
`weft` is a second consumer of the engine but not a stranger to the theory: it tests the agent as a cold reader, not a human one.
The review's argument from distance — that the product's target reader is `distance: far` and nobody far has read it — is narrowed by this era, not answered.

**Speed is bought with consistency.**
The era will leave stale passages that earlier phases would have stopped to fix, and its records will be lighter than Phase 12's.
That trade is the decision, not a side effect of it.

**The moratorium is a rule without a check.**
Nothing mechanical stops a new self-referential check from landing; this record is what a reviewer cites.
