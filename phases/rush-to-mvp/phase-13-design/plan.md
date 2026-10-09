---
title: "Phase 13 design — the plan"
force: propose
verb: argue
intention: suasive
view: synchronic
provenance: { type: project, id: phase-13-design }
constitutive: no
concerns: [steering, codifying, writing]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

The rush to MVP has two delivery phases, adoption and the agent kit ([ADR-042](rush-to-mvp.md)).
This phase plans and designs them, so that each starts with its rulings taken and its blocking questions answered.
It builds nothing.

## Workstreams

| # | Workstream | Output | State |
|---|---|---|---|
| **D1** | **Open the era**: the decision that closes Phase I and bounds the rush by an observable condition. | [ADR-042](rush-to-mvp.md) | done |
| **D2** | **Plan the adoption phase**: what an adopter installs, how the engine leaves this repository, how strictness lets legacy documents in. | [adoption plan](adoption-plan.md), with its rulings: a Python package in its own repository, adopter defaults, the shrinking baseline | drafted |
| **D3** | **The proposals the delivery phases rest on**: what a project's documentation must carry about its code; reader-first writing; one package per ecosystem bound to one API. | [`theory-of-the-code.md`](../../../imagining/theory-of-the-code.md), [`reader-first-writing.md`](../../../imagining/reader-first-writing.md), [`multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md) | drafted; the theory of the code awaits rulings on its three open questions |
| **D4** | **Plan the agent kit**: what an agent installs (skills, agents, instructions), how it is generated from `writing/` rather than copied, how it runs the gate and the cold-reader pass, and how the `weft` pilot tests ADR-042's condition. | an agent-kit plan in this folder | to do |
| **D5** | **Close the phase**: a README, the ledger, the roadmap and the index. | phase README | to do |

## Open points

| # | Open point | Settled by | Blocking? |
| --- | --- | --- | --- |
| 1 | **The engine's repository**: its name, where it is hosted, and its visibility. | The project owner | Blocks the adoption phase's T2 |
| 2 | **The theory of the code**: one document or two, whether the lexicon is constitutive, whether it is a default or required ([its open questions](../../../imagining/theory-of-the-code.md#open-questions-for-a-ruling)). | The project owner | Blocks D4 |

## Definition of done

- The adoption plan has no blocking open point left except those its own tasks settle.
- The agent-kit plan exists, states how ADR-042's condition is tested, and has no blocking open point left except those its own tasks settle.
- The proposals the plans depend on are ruled on, or the plans say what they assume.
- The gate is green.
