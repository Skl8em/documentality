# Applying "Structure your project's documentation" to weft

This is a real, honest run of the tutorial against the weft spec, done as a first-time reader.
I am treating myself as weft's maintainer, working only from the spec text I was given.
No code was read; nothing outside the spec was consulted.

## Step 1 — Name the activities weft takes part in

I went past the first three that came to mind (use it, install it, extend it) and kept pushing, per the instruction.
Here is the list, each with the body of knowledge it draws on.

1. **Run project tasks day to day** (`weft run` / `weft chain`) — draws on: the specific project's own task graph; general CLI conventions.
2. **Browse the registry** ("what can this project do") — draws on: weft's CLI conventions (`weft list`), this project's own naming choices in its `weftfile.py`.
3. **Author tasks** — write a lightweight `>>`/`&` chain, or a fully-decorated Python task — draws on: Python; the DSL operators; the `Task`/`Context` API.
4. **Declare preconditions, resolvers, and provider alternatives** for a task — draws on: the domain of the specific precondition (e.g. "is the DB migrated"); weft's own `Precondition`/`Resolver`/`Provider`/`Requirement` (`all_of`/`any_of`/`one_of`) vocabulary.
5. **Embed weft as a runtime library** inside another host program — draws on: Python packaging/import mechanics; weft's `Runner`/`Context` contract; the host program's own architecture.
6. **Install and pin weft as a dependency** from the corporate Nexus — draws on: pip/Nexus mechanics, ordinary dependency-management practice.
7. **Diagnose a run** that came back FAILED / BLOCKED / AWAITING — draws on: `State` semantics; the `RunReport` format; the logic of the specific task that didn't succeed.
8. **Consume the generated task graph** (`weft graph` → Mermaid → a docs pipeline) — draws on: Mermaid; the conventions of whatever downstream docs pipeline receives it.
9. **Extend or fix weft's own core** — draws on: weft's internals, its design rationale, the self-imposed ~600–900 line budget.
10. **Steer/decide weft's direction** — resolve the four open design decisions the spec flags, and evaluate the invoke-fallback gate — draws on: the tradeoffs named in the spec; the project's own history of why choices were made.
11. **Evaluate/adopt weft** for a new project, against make/just/doit/invoke — draws on: comparative knowledge of those alternatives; the adopting project's own needs; the one-maintainer risk.
12. **Rename weft** before adoption (the spec explicitly says the name is a placeholder) — draws on: whatever process governs a rename — the spec does not say.

Twelve is more than I expected going in.
Several of these (4, 5, 8, 11, 12) are easy to miss on a first pass — which the tutorial predicted would happen, and it did.

## Step 2 — Who performs each, and their distance

| # | Activity | Person (role) | Distance |
|---|---|---|---|
| 1 | Run tasks | Developer working in a project that uses weft | Initiated in the project's own task graph; possibly novice in weft's CLI on first contact |
| 2 | Browse registry | Newcomer to the repo, or the same developer | Novice in weft's CLI conventions; initiated in the project domain |
| 3 | Author tasks | Task author (often the same maintainer wearing a different hat) | Initiated in Python; novice in weft's own DSL/Task API until they've written a few |
| 4 | Declare preconditions | Task author, doing the harder sub-case | Likely novice in weft's `Requirement` combinator vocabulary even when fully initiated in Python generally — this vocabulary is bespoke, nobody arrives already knowing it |
| 5 | Embed as library | Integrator — developer of a separate host tool/library | Initiated in Python packaging; novice in weft's `Runner`/`Context` contract, since the spec never claims it is a stable, documented API |
| 6 | Install/pin dependency | Whoever manages the project's dependencies | Initiated in pip/Nexus; needs zero knowledge of weft internals |
| 7 | Diagnose a run | On-call developer, or the original task author | Initiated in `State` semantics if they wrote the task; novice if they're a bystander hitting someone else's failing task |
| 8 | Consume graph export | Docs-pipeline maintainer (possibly the same maintainer, possibly a separate docs-tooling owner) | Novice in weft's graph output format on first contact |
| 9 | Extend core | The maintainer (declared audience) | Fully initiated — it's their own code — but designing for a "readable in an afternoon" budget, i.e. designing for their own future novice self |
| 10 | Steer/decide | The maintainer / "future self" (declared audience) | Initiated in the tradeoffs, by definition, since they wrote the risk note |
| 11 | Evaluate/adopt | A prospective adopter — a team lead or engineer sizing weft up against alternatives | Novice in weft entirely; this is a first contact |
| 12 | Rename | The maintainer, but decision ownership is unstated | Initiated in the reasons a rename is needed; the process itself is undefined |

Finding worth flagging here: activities 5, 8, and 11 imply real audiences beyond the spec's declared `[maintainer, future-self]`.
Step 2 forced this to the surface — I did not go looking for it, it fell out of "read the people off the activities."

## Step 3 — What each person needs, and in what order

1. **Task runner** — needs **do** first (how to invoke a task, read `weft list`/`weft run` output), then **know** (what a non-SUCCESS state means) only once something isn't plain success.
2. **Newcomer/browsing** — needs **know** first, and it's almost the whole need: "what can this project do" *is* the registry's job. A short how-to for `weft list`/`check` syntax is secondary.
3. **Task author** — needs **do** first (write a simple `>>` chain), then **know** (why both DSL and decorated-Python compile to the same `Task` object, and when to graduate).
4. **Precondition author** — needs **know** *first*, unusually — the `Precondition`/`Resolver`/`Provider`/combinator vocabulary is not guessable, so a how-to attempted before the concepts are named will fail.
5. **Integrator (embed as library)** — needs **know** (the `Runner`/`Context` contract, when workspace resolution happens) before **do** (constructing a `Runner`) — a wrong workspace `Path` silently breaks `FileDeps`, so here, unlike the tutorial's plain "installer wants how-to first" case, know has to come first or the how-to is dangerous.
6. **Packager** — needs **do** only: install command, version pin, Nexus coordinates. No **know** at all.
7. **Diagnoser** — needs **orient** first (what ran, what state, where the report lives under `workspace/.weft/runs/`) — this is the tutorial's "returning after three months" case, except it can hit the same day; then **know** (state semantics), then **do** (re-run/resume — unresolved for AWAITING per the spec's own open question).
8. **Docs-pipeline consumer** — needs **do** (how to invoke `weft graph` and where the Mermaid output goes) with minimal **know**.
9. **Maintainer extending core** — needs **why** (design rationale, the line-count constraint, the risk note) before **do** — the tutorial's textbook "why before how-to" case for internal work.
10. **Steering/deciding** — needs to **see a decision**, literally: this activity's whole need is the decision record itself, for each of the four open items and the invoke-fallback gate.
11. **Evaluator/adopter** — needs **know** first (what weft is, is not, and the honest risk paragraph) before anything else; if the "why" doesn't land, they never reach "do."
12. **Renamer** — needs to **see a decision**: has it been renamed, to what, when — a one-line status, not a document.

## Step 4 — Start together, then split along the seams

Starting point: one README holding the elevator pitch (what weft is / is not, the non-goals), a quickstart (`weft list`/`run`), and a pointer to "why" for anyone who wants more.
Seams that actually appeared while drafting it:

- **Grown too big**: the `Precondition`/`Resolver`/`Provider`/`Requirement` vocabulary needed more than a paragraph to make sense at all — first seam, split into its own how-to.
- **Divergent lives**: the four open design decisions (manifest granularity, concurrency model, AWAITING resumption, operator-overloading limit) plus the invoke-fallback gate are decisions that should *freeze* once made, while the rest of the README keeps *changing* as the tool changes — the clearest, most textbook seam in this whole exercise.
- **Distinct community**: the embedding/library API (`Runner`/`Context`) serves integrators who will never touch the CLI or the DSL — split out on its own.
- **Arguable seam, deliberately not cut**: diagnosing a run touches generated, per-run data (`RunReport`s under `workspace/.weft/runs/`), which is neither "current" documentation nor a "frozen" decision — the tutorial has no vocabulary for this third kind of artifact (see review). I kept only a how-to for *reading* reports, and treated the reports themselves as data, not documentation.

## Step 5 — Where things go, by provenance

| Document | Provenance (Step 1 activity) | Current or frozen | Location |
|---|---|---|---|
| `README.md` | Use / browse (permanent) | Current | root — it's the surface where users meet the project |
| `docs/howto-write-tasks.md` | Author tasks (permanent) | Current | docs/ |
| `docs/howto-preconditions.md` | Declare preconditions (permanent) | Current | docs/ — split out once it outgrew a paragraph |
| `docs/embedding.md` | Integrate/embed (permanent, distinct community) | Current | docs/ |
| `docs/design.md` | Extend/steer the core (permanent) | Current | docs/ — holds the "why," the line-count constraint, the risk note, the non-goals |
| `docs/decisions/NNNN-*.md` | Steer/decide (each decision is a bounded effort) | Frozen per entry, once decided; the log itself keeps growing | docs/decisions/ |
| `docs/diagnosing-runs.md` | Diagnose a run (permanent) | Current | docs/ — a how-to for reading `workspace/.weft/runs/*`, not the reports themselves |
| *(none yet)* | Evaluate/adopt | — | Not written: the spec's declared audience excludes prospective adopters, so per the tutorial's own rule this activity isn't real yet |
| *(none yet)* | Consume graph export | — | Not written: the downstream docs pipeline is undefined in the spec |

## Resulting structure

```
README.md                          # use/browse — current, root
docs/
  howto-write-tasks.md             # author tasks — current
  howto-preconditions.md           # declare preconditions — current
  embedding.md                     # embed as library — current
  design.md                        # extend/steer the core — current (why, constraints, risk, non-goals)
  diagnosing-runs.md               # diagnose a run — current
  decisions/
    0001-manifest-granularity.md   # frozen once decided
    0002-concurrency-model.md      # frozen once decided
    0003-awaiting-resumption.md    # frozen once decided
    0004-operator-overload-limit.md# frozen once decided
    0005-rename.md                 # frozen once decided
    0006-invoke-fallback-gate.md   # frozen once decided (or re-opened if revisited)
```

Two activities (evaluate/adopt, consume-graph-export) were deliberately left undocumented, because Step 2 showed their audiences aren't real yet per the spec's own declared scope — this is flagged as an open question, not silently dropped.
