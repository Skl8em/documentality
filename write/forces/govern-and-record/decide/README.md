---
title: "Decide — the stance"
force: explain
verb: illuminate
perlocution: model
view: synchronic
provenance: { type: function, id: doc-system }
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

`decide` institutes a choice by record. It is a `convince` force: the whole value is bringing a future reader — including you, once the context is forgotten — to accept the choice as reasoned. Use [`template.md`](template.md) to write one.

- **Generative verb:** *justify.*
- **Stake:** the reasoning, not the verdict. The decision is a single line; the value is the record of *why*, written to be read by someone who does not yet agree.
- **Move structure:** state the context and the forces in play → lay out the options genuinely considered → record the decision → record the consequences accepted, including the unwelcome ones.
- **Failure mode:** recording the verdict and discarding the reasoning — the log that says *what* and is useless the moment anyone asks *why*. A decision record without its rejected options is an assertion, not a justification.
- **Special property:** *dated-fixed*. Never edit it to reflect a later choice; a superseding decision is a **new** record linking the old via `supersedes`. `view: diachronic`, `retention: permanent`.
- **Variant verb:** when the centre of gravity is authorization rather than reasoning (a sign-off), write it under *ratify*.
- **Genres:** architecture decision record, committee minutes, sign-off, resolution.

Because it freezes, a decision belongs to the **project** that produced it (`provenance.type: project`), not to a maintained state. The state document it changes (an `explain` architecture page) is updated separately and *references* the ADR — see `../../../../structure/concepts.md` on the state/change seam.
