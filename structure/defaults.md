---
title: "Recommended structural defaults"
force: recommend
verb: advise
perlocution: none
view: synchronic
provenance: { type: function, id: doc-system }
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

Defaults, not rules — override with reason (the binding minimum is in [`rules.md`](rules.md)). They save you from re-deciding the same things per project.

## Tree axis

- **Cross-project docs repo** → organize by **business function**. The dominant readers cross projects and think in the business's language, not the implementation's.
- **In-repo docs of a code project** → organize by **component / builder's path**. The dominant readers are builders.
- **Mixed teams** → pick the *dominant* community and serve it well rather than serving everyone weakly; note the choice at the tree root.

## Retention by force

| Type (force) | View | Recommended retention |
|---|---|---|
| Decision (`decide`) | diachronic | permanent, never rewritten |
| Changelog / report (`account`) | diachronic | permanent, append-only |
| Proof / dossier (`prove`) | diachronic | per legal/contractual obligation (`legal:<duration>`) |
| Reference, architecture (`describe`, `explain`) | synchronic | maintained while the function lives; archived version per release |
| Guidelines (`recommend`), conventions (`mandate`) | synchronic | maintained while the function lives; supersede rather than silently edit |
| Proposal (`propose`) | diachronic | frozen once decided; the ADR references it |
| Working note, draft | — | ephemeral; delete or promote, never let it sediment |

## Wiki-in-decay: what to check

A corpus that sediments lacks three *independent* things — repair them independently:

- a **provenance** (which activity is each doc a trace of?),
- a **retention rule** (when does it die?),
- a **tree chosen for a real community**.

"The wiki is a mess" is not a diagnosis; those three lacks are.

## Cost discipline

Do not pay archival cost everywhere. A document whose life is a sprint deserves neither the armor of a proof nor the scaffolding of a cross-project reference. Match the cost to the horizon and the recipient (`../write/patterns.md`, recipient section).
