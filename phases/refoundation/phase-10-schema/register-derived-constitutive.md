---
title: "Decision — `register` is derived from `constitutive` and direction of fit; `constitutive` is stored"
id: 01KZ2EQ4002M9D4G3R50WT9TAE
slug: register-derived-constitutive
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-10-schema }
constitutive: yes
concerns: [steering, writing, structuring, theorising, operationalizing]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:82c78ae75eb17ccb87a7e3c3d8a2835faba08a64e3f7ae410aaa8fd79b6f48d1
---

## Status

accepted — 2026-08-03.
Settles ⚑ Decision 2 (store `register`, or derive it), open since Phase 07.
Supersedes the *register* part of ADR-016 (know/do/govern as a gloss over `force`) and refines the register part of ADR-025; the rest of both records stands.

## Context and forces in play *(justify)*

`know / do / govern` has been in the system since v3, first as three folder doors and then, after ADR-016, as a "register gloss over `force`".
Calling it a gloss removed the claim that it was a shelf axis, but it never said what the three bins *are*.
Under inspection the triad was ill-founded in a specific way: **`know` and `do` are directions of fit, and `govern` is not**.
Word-to-world and world-to-word exhaust the directions; there is no third one.
So the triad was two coordinates wearing one name — a direction, plus something else.

That something else is **markedness**: whether the act *posits or fixes a social object* — a norm, an obligation, a decision, an evidentiary record — or merely *serves a reader*.
This is the Ferraris/Searle distinction the refoundation already rests on, and it is orthogonal to direction of fit: a `mandate` and an `explain` differ in direction, but a Quai d'Orsay `recommend` and a friend's `recommend` differ in *this*.

Meanwhile the corpus disagreed with itself about whether `register` was stored at all.
The `steering/` records carried `register: govern` in frontmatter; the product files carried nothing.
Storing it duplicates what `force` already fixes — the exact fault the schema names in its own design note ("anything derivable from `force` is generated, never stored") — and duplicated data drifts.

Three options were weighed.
Keep `govern` as a third direction of fit: rejected, it is the original error.
Drop `govern` and let the register be binary `know | do`: rejected — the three-way handle is the one the maintainer, the readers, and the `writing/forces/` doors actually use.
**Re-found it**: keep the three bins, and derive them honestly from two things we can defend.

## Decision

1. **`register` is derived, never stored**.
   Storing it is a lint **error**.
   The derivation is:

   ```text
   register = constitutive == yes  ?  govern
                                   :  direction-of-fit(force)   # know | do
   ```

   The third bin is not a third direction of fit — it is the *constitutive* one.

2. **`constitutive: yes | no` is a new required, stored field**, and it is a **conscious per-document judgement**, not a derivation.
   `yes` means the act posits or fixes a social object; `no` is the unmarked default, an act that informs or guides.

3. **The direction-of-fit table is encoded in the schema**, partitioning the twelve forces exactly:

   | direction | register | forces |
   |---|---|---|
   | word-to-world (the words answer to the world) | `know` | `orient` `explain` `describe` `prove` `account` |
   | world-to-word (the world is to answer to the words) | `do` | `instruct` `teach` `recommend` `mandate` `commit` `propose` `decide` |

   The linter refuses to load a schema whose table does not cover the forces exactly, so the derivation can never be partial.

4. **Deriving `constitutive` from `force` × `power` is deferred, not rejected**.
   Authority is what makes the Quai d'Orsay's `recommend` bind and a friend's not, which is `power`.
   We store the judgement first and watch how it is actually used, rather than automate a rule we have not yet observed.

5. **The three `writing/forces/` doors are kept**.
   Only their foundation changes; no folder moves, no force is reclassified.

6. **The non-constitutive pole gets no name**.
   It is the unmarked default, and naming it would suggest a symmetry that is not there.

## Entail — what follows

- `constitutive` joins the required set in `schema/frontmatter.schema.json`; `register` in frontmatter is an error; both are enforced by `scripts/frontmatter_lint.py`.
- The whole catalogue was swept: stored `register` removed everywhere, `constitutive` judged and written on all 93 catalogued documents (21 `yes`, 72 `no`).
- `scripts/frontmatter_lint.py --registers` computes the derived register, so the value is available to tooling without being stored.
- `writing/frontmatter.md` documents `constitutive` as a field and `register` as a derived view.
- The apports themselves are described in [`../../../operationalizing/constitutive.md`](../../../operationalizing/constitutive.md) and [`../../../operationalizing/register.md`](../../../operationalizing/register.md) — this record decides, those fiches explain.
- `decide` sits under `do` in the table, which is a compromise worth naming: a declaration has, strictly, a double direction of fit.
  It only matters for a *non-constitutive* `decide`, which is close to a contradiction in terms — a `decide` that constitutes nothing.
  In practice every `decide` in the corpus is `constitutive: yes` and derives `govern` before the table is ever consulted.

## Honest limit

`constitutive` is a judgement, and judgements are inconsistent across authors and across time.
Two contributors will classify the same borderline document differently — is a roadmap that records plan changes constitutive, or does it merely propose? — and nothing in the tooling can catch that, because there is no ground truth to check against.
We chose this deliberately: the alternative (deriving from `force × power` now) would give consistency at the price of encoding a rule we have not yet earned.
The cost is that the field's meaning is only as good as the care taken per document, and that early judgements may need revisiting once the pattern is visible.

A second, smaller limit: `yes | no` are YAML 1.1 booleans.
A strict YAML 1.2 parser reads them as the strings `"yes"`/`"no"`, a YAML 1.1 parser as `true`/`false`.
Our linter reads them as strings and requires exactly `yes` or `no`, so the corpus is unambiguous, but any downstream tool must know which it is reading.
