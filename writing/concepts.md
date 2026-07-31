---
title: "The coordinate system"
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

This document builds the model behind the whole system, so that the rules and templates elsewhere read as consequences rather than arbitrary conventions. The question it answers: *why does naming a document's force tell you how to write it?*

## Two strata: hard coordinates, one soft verb

A document has **hard coordinates** a machine can read: its `force` (which illocutionary act it performs), its direction of fit (does it convey *knowing* or aim at *doing*), its `intention` (whether, and how, it aims to move the reader above the constitutive floor), and its recipient relation (`distance`, `power`). These span a space — and the forces are the **recognized cells** of that space: the conventionalized acts a community has named, not a closed set of primitives (ADR-015/016). Not every cell is occupied, and new ones can be recognized — `recommend` was added to the do-gradient, and `entail` is a second face of `decide`.

Over that space sits one **soft handle for the human**: the **verb**. The verb is a compressed summary of the occupied cell — one word naming where the centre of gravity lies, and thereby selecting the move structure. This is why the verb is not redundant with the force: the force is one coordinate, the verb is the label of the whole tuple. A decision is classified `decide` but written toward *justify*, because *justify* summarizes "declarative act + aimed at the reader's assent + toward a reader who does not yet agree" in one actionable word.

## Why the verb sometimes differs from the force

When the verb diverges from the force's name, it is for one of three reasons — two earn a stored `verb`, one does not:

- **(a) Perlocutionary** — the force reshapes the reader and the verb names *which* faculty (orient→*situate*, explain→*illuminate*, teach→*bring-along*, and the convince forces).
- **(b) Illocutionary-internal** — the force is coarse and the verb picks a finer point on its own axis (decide→*justify* vs *ratify*; mandate→*require* vs *forbid*; describe→*specify* vs *define*).
- **(c) Recipient** — distance/power shift the centre of gravity. This does **not** earn a new verb; it is already captured by `distance`/`power` (prove→*attest* is prove × `power: holds`).

Store `verb` only for (a) and (b). For (c), set `distance`/`power` instead.

## Intention: a floor, and an aim above it

`intention` names the change the act works in the reader — the *perlocutionary* aspect in Austin's sense, parallel to and independent of the illocutionary `force`. It has **no zero** (ADR-015). Every inscription carries a constitutive **floor**: even at its minimum the act *establishes a state* in the reader — an uptake they now hold that they did not before — and, by selecting what it says, *casts a shadow on the unsaid*. We name that floor `state` (ADR-026): the act serves, and no aim rises above it. Above the floor an **intention** may rise — the act sets out to *move* the reader, and the value names how. Like the force repertoire it is an open, saturated list.

| `intention` | What is reshaped | Verb | Host forces |
|---|---|---|---|
| `state` | the floor: an uptake is set and the unsaid shadowed; nothing rises above it | — | describe, account, instruct, recommend, mandate, commit, propose |
| `locate` | the reader's cognitive map (where am I) | situate | orient |
| `model` | the reader's conceptual model (why) | illuminate | explain |
| `enable` | the reader's competence (able to act) | bring-along | teach |
| `convince` | the reader's assent / belief | justify, demonstrate | decide, prove |

The four aims above the floor gather into three coarse families — **formative** (`locate`/`model`/`enable`, forming the reader's map, model, or competence), **suasive** (`convince`, moving assent), and **affective** (moving feeling) — the refounded set `state` · `formative` · `suasive` · `affective` (ADR-015/026). Whether the schema stores the coarse family or the fine value is settled in Phase 09; the fine values are used here as current practice.

The `convince` row folds `prove` and `decide` into the perlocutionary family: a dossier convinces an examiner a claim holds; a decision record convinces a future reader the choice was reasoned. For those two the aim is *instrumental* (the primary point stays evidential/declarative); for orient/explain/teach it is *primary*. Both are real, so both are named.

The **Host forces** column names each intention's *typical* home, not a whitelist. Intention is an independent coordinate, so **any force may carry any intention** — an `account` that means to explain a failure takes `model`, a `describe` written to persuade takes `convince`. Some pairings are natural, others awkward, but we do not commit to a table of which are "possible": that would be a definitiveness the theory's *saturated, not closed* stance forbids. The force implies a *default* intention; a divergence is legal and usually says something (see `phases/naive-sketch/phase-05-records-governance/ADR-013-open-pairings.md`).

## The three doors, and why there is no `diataxis` field

Direction of fit splits the repertoire into **know** (savoir, word-to-world: you end up *knowing*) and **do** (savoir-faire, world-to-word: you end up *doing*). Crossing that with intention (reader *moved above the floor* or merely *served at it*) re-derives Diátaxis exactly — which is why the schema carries no `diataxis` field; it would encode twice what `force` already fixes:

| | Know (savoir) | Do (savoir-faire) |
|---|---|---|
| **Moved** (intention ≠ state) | explain / orient | teach |
| **Floor only** (intention = state) | describe | instruct |

Diátaxis sees only this 2×2. The forces this theory *adds* — prove, account, mandate, commit, propose, decide, recommend — fall outside it because they do not address a *user of a system*; they regulate relationships or fix a record. Hence three doors, not two:

- **know** — `orient`, `explain`, `describe`.
- **do** — `instruct`, `teach`, `recommend` (a deontic gradient: *here is how* → *you should* → *you must*, that last being `mandate`).
- **govern & record** — `mandate`, `commit`, `propose`, `decide`, plus the evidence/memory forces `prove`, `account`.

These three doors — **know / do / govern** — are a **register** gloss over the forces: a reading convenience *derived* from `force`, not the shelf axis (ADR-016). The source is shelved by **provenance** (the maintaining function), never by door; the doors order a *generated* reader surface. `writing/forces/` is split along them only because it is itself such a surface. Each door's `README.md` explains its family; each force's `README.md` is its stance.

## In short

Hard coordinates (force, direction of fit, intention, distance, power) span a space whose **recognized cells are the forces**; the soft `verb` names the occupied cell and picks the move structure. Intention is a floor (`state`) with an optional aim above it, not a boolean. The three doors are a register gloss and the newcomer's map. Everything derivable from `force` — door, direction of fit, diataxis — is generated, never stored.
