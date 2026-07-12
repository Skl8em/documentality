---
title: "Decide — the stance"
force: explain
verb: illuminate
perlocution: model
view: synchronic
provenance: { type: function, id: writing }
audience: [user]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

`decide` institutes a choice by record. It is a `convince` force, and — unusually — it has **three faces**, because a decision looks in three directions at once. Use [`template.md`](template.md) to write one.

## The three faces

- **`enact` — the act.** Take the choice on record where it must be noted: "this is decided, on this date." Pure declarative. In a large corpus this face can live in a central **register** (a one-line-per-decision index) separate from the reasoning.
- **`justify` — backward.** Motivate the choice from its settled context: the forces in play, the options genuinely considered, why this one. It *integrates the past*. Written for a reader who does not yet agree. Failure: recording the verdict and discarding the reasoning.
- **`entail` — forward.** Unfold what the decision *changes, commits, and requires* going forward — the operative consequences (the *dispositif*, to justify's *recitals*). It *differentiates into the future*, and because the future does not accumulate it is a projection, not a proof: write it as defeasible. Failure: leaving the implications implicit, so no one knows what the decision requires of them.

## Move structure

State the context and forces → lay out the options genuinely considered → record the decision (`enact`) → give the reasoning (`justify`) → unfold the implications (`entail`): what must now change, what it commits us to, which `mandate`/`commit`/`instruct` follow, or which `propose` it reopens.

- **Special property:** *dated-fixed*. Never edit a decision to reflect a later choice; a superseding decision is a **new** record that sets `supersedes`. `view: diachronic`, `retention: permanent`.
- **Genres:** architecture decision record, committee minutes, sign-off, resolution. (A sign-off, where authorization outweighs reasoning, is written under the variant verb *ratify*.)

Because it freezes, a decision belongs to the **project/phase** that produced it (`provenance.type: project`), not to a maintained state. The state document it changes (an `explain` page) is updated separately and *references* the record — see `../../../../structure/concepts.md` on the state/change seam, and `docs/` in this repo for a worked example (a register plus per-phase records).
