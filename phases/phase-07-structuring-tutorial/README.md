---
title: "Phase 07 — Structuring tutorial & front-end correction"
force: orient
register: know
intention: locate
view: diachronic
provenance: { type: project, id: phase-07-structuring-tutorial }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: done
---

Authoring the structuring tutorial exposed that the front-end model was wrong at the root.
The first draft imposed *our* decomposition, ordered communities before functions, presupposed that a user reads, misjudged what a returning maintainer needs first, and named a few genres without ever saying where they go.

Correcting it settled a real point of the model — functions come first and communities are derived from them, distance is per discourse community, and the groupings themselves are mutable and best kept coarse.
So this phase both delivers the tutorial and repairs the foundation.

A blind test then stress-tested the functions-first tutorial: a fresh agent followed it on this project and on an external library, and wrote an adversarial review of each.
The convergent findings — and the maintainer's own notes on them — drove a rewrite around a few deep moves (relevance not recurrence, an explicit fractal method, organizing for the author, an `imagine` activity, and the conventional repo documents as worked examples).
The critique, our review, and the plan are in [`tutorial-revision-plan.md`](tutorial-revision-plan.md); the test artifacts are kept under [`blind-test/`](blind-test/).

A **second blind test** (round 2, on `weft`) validated the rewrite: four of round 1's five cold-stops were resolved, and it surfaced three refinements now folded in — the entry-state keyed to what is *written* (not code), the co-owned-document tiebreaker (author-and-maintainer, honoring the Step 3 → 5 promise), and the open-question/deliberation life (a *current* `govern` doc that decants into frozen records).
That third one is where the maintainer expected the current/frozen device to break; it refined instead of breaking.

Finally the tutorial was turned on its own author: [`self-application.md`](self-application.md) runs the five steps on this project itself, deriving our functions (`theory`, `writing`, `structuring`, `steering`, `imagine`), the controlled front-matter vocabulary our fields may take, and our target source tree — the worked example of the theory made actual rather than asserted, and it supersedes the stale v3 self-reading in `structure/applied.md`.
With the tutorial delivered and hardened, the foundation reconciled, the rewrite validated, and the system dogfooded on itself, **Phase 07 is closed**; its records freeze here.

- [ADR-022 — front-end correction: functions first, distance per community, mutable groupings & eras](ADR-022-functions-first.md)
- [ADR-023 — tutorial rewrite: relevance not recurrence, `imagine`, organize-for-author, fractal explicit, conventional docs as examples](ADR-023-tutorial-rewrite.md)
- [self-application.md — the tutorial applied to ourselves: our functions, front-matter values, and tree](self-application.md)
