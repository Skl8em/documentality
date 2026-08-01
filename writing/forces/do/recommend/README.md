---
title: "Recommend — the stance"
force: explain
verb: illuminate
intention: model
view: synchronic
provenance: { type: function, id: writing }
audience: [user]
reader: H+M
status: stable
---

`recommend` gives honest, actionable advice that stays **non-binding**.
It sits **at the floor** (`intention: state`): it serves the reader with a *should*, not a *must*, and must say when it does not apply.
It is the middle notch of the do-door deontic gradient — *here is how* (`instruct`) → *you should* (`recommend`) → *you must* (`mandate`) — and one of the forces this system *adds* to the base repertoire (ADR-003).
Use [`template.md`](template.md) to write one.

- **Generative verb:** *advise.*
- **Stake:** honest, actionable advice that stays non-binding.
  The reader must be able to tell this is a *should*, not a *must*, and must know when it does not apply.
- **Move structure:** state the recommendation plainly → fix when it applies and when it does not → give the tradeoff that makes it the better default, briefly → mark it explicitly overridable and say how to deviate.
- **Failure mode:** symmetric drift — hardening into a `mandate` (the modals creep to *must*, a false obligation) or dissolving into `explain` (advice with no actionable form).
- **Genres:** best-practices guide, guidelines, style guide (its non-binding parts), recommendations.

Recipient note: keep the modality visible — a reader must never mistake a `should` for a `must`.
If the advice becomes binding, it is a `mandate`, not a `recommend`.
See [`../../../patterns.md`](../../../patterns.md).
