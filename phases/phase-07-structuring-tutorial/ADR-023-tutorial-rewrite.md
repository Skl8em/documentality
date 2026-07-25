---
title: "ADR-023 — Tutorial rewrite: relevance not recurrence, imagine, organize-for-author, fractal explicit, conventional docs as examples"
force: decide
register: govern
intention: suasive
view: diachronic
provenance: { type: project, id: phase-07-structuring-tutorial }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
---

## Status

accepted — 2026-07-24

## Context and forces in play *(justify)*

We ran a blind test: a fresh agent, given only a neutral spec and the functions-first tutorial, followed it on two subjects (this project and `weft`, an external design-phase library) and wrote both a response and an adversarial review.
The two reviews converged, and the external subject gave the cleaner signal.
The critique, our independent review of it, and the maintainer's own notes are recorded in [`tutorial-revision-plan.md`](tutorial-revision-plan.md).
Consolidated, the findings were not thirteen local defects but a few deep ones, and the maintainer's notes sharpened several past our first reading — most importantly that the tutorial was chasing a determinism the system does not have and should not fake.

## Options considered

- Patch each surfaced defect locally (add a grain rule, a threshold, a name here and there) — consequence: a longer tutorial still pretending to a determinism it cannot deliver, and still greenfield- and solo-biased.
- Rewrite around a small number of deeper moves that dissolve the defects at their root — consequence: a shorter conceptual load, a tutorial honest about being non-deterministic and partial, first-class about existing (not just greenfield) projects.

## Decision

Rewrite `structure/tutorial.md` around five deep moves plus a few small ones.

1. **A function is an activity *of relevance*, not a recurring one.** What qualifies an activity is that it is important enough to warrant thinking and talking about; recurrence is only one sign. This admits one-off-but-central activities (a paper's single analysis), once-per-person activities (adoption), and defensive activities (disaster recovery).
2. **Make the fractal method explicit, and drop the pretence of determinism.** Two runs may differ and neither is wrong; we give a light, not a map, and an explicit licence to take forks the text does not draw. Start coarse, keep any list to ~3–7, group up past ~7, refine only when a gap becomes intolerable, and *see* your holes rather than fill them all. Present the moving parts as hierarchies, not flat lists.
3. **Organize for the author** — the person writing and maintaining the docs, their first reader — not for "the user". Outside readers get a *generated* view in their own order; that generation and its frontmatter are deferred to their own (planned) tutorial.
4. **Add `imagine` as a first-class activity** — design, plan, dream what is not built — which homes intended/future work (including Phase-II-shaped material) instead of leaving it un-placed.
5. **Ground everything in the conventional repo documents** (README, INSTALL, CONTRIBUTING, LICENSE, ARCHITECTURE, CHANGELOG, ADR): name each, classify it by force, and place it — ending with two or three genuinely different valid trees and a fractal folder rule, rather than one anchoring example.

Small moves folded in: know/do/**govern** as the need triad, with "you are drawing boxes here, not yet filing into them"; the permanent/bounded (current/frozen) distinction introduced early but held lightly, as a working device we push until it breaks; **intended audience** (with the returning-self reminder) rather than observed; generated/ephemeral artifacts scoped out with a pointer; two entry-states (greenfield forward / existing audit-backward); and seam thresholds handled via the 3–7 heuristic and the surface-craft patterns rather than invented line counts.

Two further corrections from the maintainer's review of the rewrite.
**Distance is habitus, not knowledge alone** — it is the gap between the *authors'* habitus and the *intended reader's* habitus, spanning social codes, register, and domain style (future self vs. ten-year colleague vs. an unknown PyPI user), not merely how much each knows. This sharpens ADR-017/ADR-022's per-community distance.
**Folder nesting is provenance-first**: when a function's documents accumulate across registers, the *function* claims its own subtree and the register splits *inside* it (`docs/build/know/`, `docs/build/do/`), never the reverse (`docs/know/build/`), so a function's documents are never torn apart; `docs/know|do|govern/` hold only transversal or not-yet-migrated files. The diachronic (phase/change-stream) provenance is named briefly and deferred to a planned lifecycle tutorial.

## Entail — what follows

`structure/tutorial.md` is rewritten accordingly, threading one neutral worked example (`prep`) throughout.
The neutral blind-test spec ([`blind-test/self-spec.md`](blind-test/self-spec.md)) is revised to close the state-of-the-project gaps the reviews surfaced (no second contributor yet, schema in flux, no formal release, phase-close and freeze semantics, Phase II un-homed, the near-solo-vs-public-product tension) while staying neutral on structure.
Open threads recorded, not closed here: whether the current/frozen distinction is well-founded in the theory (pushed until it breaks); a dedicated **frontmatter tutorial** for the generated reader surface; power and the observed-vs-intended audience flag, both left for later.
The blind-test artifacts (spec, two responses, two reviews) are kept as records of this phase.

A **second blind test** (round 2, `weft`, output kept in `blind-test/weft-*-round2.md`) validated the rewrite: four of round 1's five "cold-stop" defects were cleanly resolved, and the mechanical parts (3–7 seam heuristic, provenance-first folder rule, ADR naming, generated-artifacts exclusion, habitus distance, see-your-holes) applied with little or no hesitation.
It surfaced three refinements, now folded into the tutorial:
(1) the greenfield/existing entry-state is keyed to what is **written**, not to code maturity, and the hybrid (no code, one large design doc) is named explicitly;
(2) a document two activities seem to co-own is assigned by **who authors and maintains it, not who reads it** — the consuming reader gets a pointer, honoring the Step 3 → Step 5 promise;
(3) an **open question / deliberation** is a *current* `govern` document that **decants into frozen records** as each question closes — which refines the current/frozen device rather than breaking it (the seam the maintainer flagged did not, in the end, force a third primitive).

This extends ADR-022 (functions-first); it does not supersede it.
