# Following the structuring tutorial on `weft` — a first-time run

I read the tutorial exactly once, start to finish, before touching the spec's structure.
Below is the honest record of the five steps applied to `weft`, including every place I had to invent a rule the tutorial didn't give me.
Invented moves are marked **[INVENTED]** inline; hesitations are marked **[HESITATED]**.

## Before Step 1 — greenfield or existing?

The tutorial asks me to classify the project first: greenfield (run forward) or existing (run backward, as an audit).
`weft` doesn't fit cleanly.
The **code** is greenfield — frontmatter says `status: draft`, `written-at: design-phase`, and section 1 talks about a library that doesn't exist yet.
But the **spec document itself** is not a blank page — it's a single ~280-line file already organized into ten numbered sections that read like chapter divisions (Purpose, Core concepts, Two surfaces, File deps, Preconditions, Workspace resolution, Registry/CLI, Runner, Open decisions, Type inventory).

**[INVENTED]** I decided to treat this as two different objects in two different states: the *project* (weft-the-library) is greenfield, so I ran Steps 1-3 forward, as a generator, imagining the activities of a tool that doesn't run yet.
But the *spec.md artifact* is already a "pile," so when I got to Step 4 I also ran the seam tests backward over the existing document, as an audit, the way the tutorial says to do for an inherited split.
The tutorial presents greenfield/existing as a single up-front choice about "your project."
It does not anticipate a project with zero code and one large pre-structured design document, and I had no textual license for treating the same project as both at once — I did it because it was the only way to make Step 4 meaningful.

## Step 1 — Naming the activities

Following the coarse meta-activity list (use / provide / build / govern / learn-or-teach / imagine), here is weft's honest list, by analogy with the tutorial's own `prep` example:

- **use** — write task modules with the decorator or the DSL; run tasks via the CLI (`weft run`, `weft check`) or import the `Runner`/`Registry` as an API in a host process; browse the registry (`weft list`); read a `RunReport`.
- **provide** — package and publish weft to the internal Nexus so it installs as an ordinary dependency. (This activity is almost content-free in the spec — see the review file.)
- **build** — implement and extend the core types (`State`, `TaskResult`, `Context`, `Task`, `Runner`, ...); keep the core inside the declared ~600-900 line budget; add new precondition/provider primitives.
- **govern** — decide the still-open design forks listed in §9; decide (and re-check) the line-budget / fallback-to-`invoke` threshold from the "honest risk note"; set conventions for the DSL vs decorator boundary.
- **learn or teach** — explain to a task author, who is not the maintainer, the one discipline the whole design leans on: never hardcode a path, always resolve through `ctx.path(...)` (§6). Explain when to reach for the DSL surface vs the decorator surface (§3.2's "covers what reads cleanly as one line" rule).
- **imagine** — the still-undecided items in §9 read, on one plausible reading, as roadmap material: manifest granularity, the concurrency model, whether AWAITING ever gets real suspend/resume, whether `|` gets added as a fallback operator.

That's six, inside the tutorial's 3-7 ceiling, so I stopped there.

**[HESITATED]** §9's four items could just as easily live under **govern** (things to be decided and frozen) as under **imagine** (things not yet built, dreamed about).
The tutorial's own examples of `imagine` are all forward-looking capabilities never attempted before (a plugin API, a roadmap phase).
§9's items are not that — they are blocking, unresolved questions about the *current* design, not extensions to a working system.
I ended up filing them under **govern** in the final tree (see Step 5), not `imagine`, precisely because they read as "must be closed before build can be called finished," not "nice to dream about later" — but the tutorial gave me no rule to distinguish these two cases, and a different reader could reasonably go the other way.

Also flagged as **not covered this pass**, per the tutorial's explicit instruction to name the holes you're choosing not to fill:
- **adopt** — a new team picking weft up for their own project. The spec's own frontmatter audience is `[maintainer, future-self]` only, so onboarding an outside adopter is out of scope for this document, even though the Purpose section clearly anticipates outside adopters existing ("embeddable inside another library," "usable... in an arbitrary host context").
- **license/compliance clearance** — the spec's own Step-1-style activity list (bolded in the tutorial) names "audit, review, verify correctness, security, licence, compliance" under `govern`; weft's spec has none of this, and I am not inventing it here, only marking the hole.

Body of knowledge, briefly, per activity (tutorial insists this is not "Python" but the *mobilized* skill): `use` mobilizes ordinary Python plus weft's own vocabulary (State, Context, Handler); `build` mobilizes `graphlib.TopologicalSorter`, `concurrent.futures`, and the discipline of keeping a core small enough to read in an afternoon; `govern` mobilizes architectural judgment about the four open forks; `provide` mobilizes Nexus/packaging conventions the spec never states.

## Step 2 — Who performs each activity, and distance

The tutorial says to read people *off* the activity list, not invent them.
Doing that honestly:

- **The maintainer** (you, single person) — performs `build`, `govern`, `provide`, and dogfoods `use`. The "honest risk note" names team-rotation risk explicitly, so there is already a second, later persona baked into the spec: **a successor maintainer**, someone who inherits this after rotation and was not present for any of the reasoning in §9.
- **The task author** — someone on a *different* team who imports weft and writes `@task`-decorated functions or DSL chains for their own project. This role is never named as a persona anywhere in the spec's Purpose section, but §6 uses the exact phrase "task authors" as if the reader already knows who that is.
- **Future self**, three months on, returning to the design doc mid-decision on one of the §9 forks.

**[HESITATED]** The spec's frontmatter declares `audience: [maintainer, future-self]` only.
But §3.1 ("Function parameters become CLI flags automatically") and §6 ("This is the single discipline the design enforces on task authors") are written in a voice that is clearly instructing a task author, not explaining design history to a maintainer.
Step 2 tells me to read the audience off the activities, "you do not invent them" — but the document's own declared audience and its own implied audience disagree, and the tutorial gives no instruction for what to do when a document's frontmatter contradicts what Step 2's inference produces. I resolved it by treating "task author" as real and adding it as a persona the frontmatter under-declares, but I want to flag that this is a genuine contradiction in the source, not a clean read-off.

Distance, per the tutorial's habitus framing:
- Maintainer ↔ future-self: close today, but the whole "honest risk note" is *about* the fact that this distance grows — the line-budget target is explicitly a distance-management device (a core "read in an afternoon" is a distance-closing move for a future/successor maintainer), which is a genuinely nice fit between the tutorial's Step 2 concept and something the spec already does on purpose.
- Maintainer ↔ task author: shares fluent Python, does not share weft's own vocabulary (`State`, `Provider`, `Handler`, `uptodate`) — needs those terms built from zero, in an internal-tooling register, not an academic one.
- Maintainer ↔ successor maintainer (team rotation): the spec names this distance as a *risk*, but never writes anything for this reader specifically — no document currently targets "you inherited this and don't know why the four forks in §9 aren't settled."

Unlike the tutorial's `prep` example ("a user who must install it himself... an IT specialist tasked to install it for a customer"), weft has no separate install-for-someone-else role — `pip install` from Nexus collapses that distinction. I record this as a place the tutorial's own worked example didn't transfer, not as a gap in weft.

## Step 3 — Know / do / govern

- **Task author × use**: `do` first — how to declare a task, how to chain with `>>`/`&`, how to run `weft run` — then `know`, and only when they hit trouble: why `Context` resolves at invocation and not at definition (§6), because that's the one rule violating it breaks silently. This matches the tutorial's "someone arriving only to install it wants the how-to first" case reasonably well.
- **Maintainer × build, returning after rotation or after three months**: `orient` first (which of the four §9 forks are still open, which got closed) — then `know` (rationale in §2-§3) — `do` last (how to add a new precondition primitive). This is a near-exact match to the tutorial's own "returning to a personal project after three months" example, and it was the point in the tutorial where I felt most confident I was doing the exercise "right."
- **Maintainer × govern, deciding one of the §9 forks**: this is the tutorial's own "diagnosing a failed run" in-between case, recurring almost verbatim. Weighing ThreadPoolExecutor vs. an alternative concurrency model is `know` work (comparing evidence); freezing the choice is `govern`. The tutorial explicitly tells me not to force this at Step 3 ("the tension resolves at placement, in Step 5") — but at Step 5 it did not fully resolve (see below), so the promise wasn't completely kept.
- **A hypothetical security/compliance reviewer × govern**: would need `know` first (what does this do, what's its attack surface: no daemon, no external binary, runs on demand) then their own `govern` sign-off — but the spec supplies zero material for this reader. Named as a hole, not filled.

## Step 4 — Start together, split at real seams

Because I decided the spec-as-artifact is functionally an "existing pile," I ran the seam tests backward against it rather than starting from one blank README.

Test 1, "too big" (roughly 3-7 sections before a document stops being holdable): weft's spec has **ten** numbered top-level sections in one file. That is a clean, mechanical, unambiguous seam signal — the single most decisive moment in the whole exercise.

Test 2, "divergent lives": the spec visibly mixes at least three different life-states in one file —
(a) settled reference material that stays current (§2 core concepts, §10 type inventory),
(b) a standing policy that's re-checked continually, not frozen once (§1's line-budget / fallback threshold),
(c) explicitly unsettled forks with no frozen answer yet (§9).
**[HESITATED]** The tutorial's model in Step 5 only names two life-states, current and frozen, and even hedges that this split is "scaffolding, not settled law." §9 is neither current reference nor a frozen decision — it's *pending*. I needed a third bucket the tutorial never names, and I had to invent one.

Test 3, "distinct community": §7 (Registry/CLI) is read by task authors as a `do` document; §2-3, §8 (core concepts, runner mechanics) are read by the maintainer as `know`; §9 is read by the maintainer alone, as `govern`. Different audiences, real seam.

All three tests fire, so I split.

The tutorial also names two artifacts I should use rather than reinvent: a decision record (ADR-style, one frozen entry per decision) for things that freeze, and the observation that generated/ephemeral artifacts (weft's own `RunReport` JSON, `manifest.json`) are not authored documentation at all — I document *how to read* them, not file them into the tree. Both of those were easy, unambiguous applications once I got to them.

**[HESITATED]** The ADR pattern is for decisions *already made*. Nothing in weft is decided yet — §9 is a list of open questions, not a decision log. The tutorial gives me a home for frozen decisions (`docs/decisions/` or `docs/govern/`) but no home for *undecided, blocking* questions. I invented `docs/govern/open-questions.md` as a holding pen, explicitly not an ADR, to be emptied into `docs/govern/decisions/` one entry at a time as each fork closes.

## Step 5 — Placement

Applying the fractal folder rule, and starting from the coarse cut (the tutorial says a small folder doesn't yet need per-function subfolders — "the moment one function has three-or-so documents *scattered across those registers*, pull the whole function out"). I checked: no single function currently has documents scattered across `know`/`do`/`govern` for weft — each function's material sits mostly in one register. So I stayed at the coarse cut, not the per-function split, which is a size-appropriate move for a project this small (I drafted a `docs/build/`, `docs/govern/`, `docs/use/` version first and pulled back once I reread the trigger condition — recorded here as a real false start).

**[HESITATED]** §6 (workspace resolution) is genuinely needed by two audiences equally: the maintainer needs to know how it works to keep it correct; the task author needs to follow it as a rule ("never hardcode a path"). The tutorial's core principle — "a function's documents stay together," provenance is the primary cut — doesn't tell me what to do when two functions have an equal claim to producing/consuming one document. **[INVENTED]** I assigned provenance by *who writes and maintains the document*, not who reads it — the maintainer authors and maintains the workspace-resolution explanation, so it lives under `know/` (build's register), and a much shorter rule (`always use ctx.path(...)`) gets pulled out and restated for task authors inside the do-facing CLI reference, as a pointer back, not a duplicate.

**[HESITATED]** "Non-goals" (§1) reads as argued, justified scope decisions ("Not a build system competing with make..."), which could be a frozen governance record. I placed it in the README as orientation instead, because it answers "what is this" for an arriving reader before anything else — but I want to flag that a stricter reading of Step 5 would put it in `docs/govern/decisions/` as a scope-boundary ADR, and the tutorial does not adjudicate between these two readings.

### The tree

```
README.md                       # orient: what weft is, non-goals, who it's for — root, providing/teaching, current
LICENSE                         # NOT WRITTEN — named gap, spec has no license/compliance content at all
docs/
  know/
    architecture.md             # §2 core concepts, §3 two surfaces + state branching,
                                 # §4 file deps, §5 preconditions, §6 workspace resolution,
                                 # §8 the runner end-to-end, §10 type inventory — build-provenance, current
  do/
    cli-reference.md            # §7 registry/CLI, marked internally as "(illustrative)" in the spec itself —
                                 # so this document is documenting something the spec calls provisional
    writing-a-task.md           # NOT WRITTEN — named gap: no worked how-to exists yet for a task author,
                                 # despite §3.1/§6 clearly assuming that reader
  govern/
    risk-policy.md              # §1 honest risk note + the ~600-900 line budget — a STANDING policy,
                                 # re-checked continually, therefore current, not frozen
    open-questions.md           # §9 open design decisions — INVENTED third life-state: pending, not current,
                                 # not frozen; no home for this in the tutorial's own current/frozen model
    decisions/                  # empty for now — future home for each §9 fork once actually settled
```

No `docs/imagine/` materialized — I folded §9 into govern rather than imagine, for the reasons flagged above, but a different first-time user following the same tutorial could reasonably produce `docs/imagine/open-forks.md` instead, and nothing in the text would tell either of us we were wrong.

## What actively helped

The "roughly three to seven sections" heuristic in Step 4 was the single cleanest, most mechanically applicable rule in the whole tutorial — counting weft's ten sections and getting an unambiguous "yes, split" was the only moment I felt zero hesitation.
The fractal folder rule's worked prohibition — never `docs/know/build/` and `docs/do/build/`, keep a function's documents together — was equally clean once I reached it.
The "generated, ephemeral artifacts are a third category, don't file them" rule mapped directly onto weft's `RunReport`/`manifest.json` with no friction at all.
The returning-after-three-months ordering example (orient, then know, then do) mapped almost exactly onto the successor-maintainer persona the spec itself half-names via its team-rotation risk language.
