---
title: "The tutorial applied to ourselves — our functions, our front-matter values, our tree"
force: explain
verb: illuminate
intention: formative
view: synchronic
provenance: { type: project, id: phase-07-structuring-tutorial }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
retention: permanent
note: "The closing act of Phase 07: the rewritten structuring tutorial run on this project itself, non-blind, to derive our own controlled front-matter vocabulary and our target source tree. Supersedes the stale v3 self-reading in structure/applied.md."
---

This is the structuring tutorial run on the project that produced it — the worked example of its own theory, made actual rather than asserted.
`foundation.md` already stated our front-end in prose; this document *executes* the five steps and reads two concrete deliverables off the result: the **controlled vocabulary our frontmatter fields may take**, and the **source tree** the exercise yields for us.
It is not blind — we know this project — so its value is not an independent test but a derivation we can commit against.
Where a value is a committed choice it is marked **[decided]**; where the exercise proposes a change to current practice it is marked **[proposed → Phase 08/09]**; where it opens a question it goes to §Pending.

## Entry state

We are *existing in prose, part-greenfield in code*.
A great deal is written (three theory essays, the writing and structuring guidance, the governance records) and almost nothing is generated or tooled yet (the schema is not derived, no surface is generated).
So we run Steps 1–3 partly **backward**, auditing what is already written, and partly **forward** for the `imagine` band (Phase II), exactly the hybrid the tutorial now names.

## Step 1 — Our functions (activities of relevance)

Two faces, as `foundation.md` §2 insists: the **functions served** to whoever meets the project (which order a *generated reader surface*), and the **producer's ways of working** (which order the *source shelf*).
The tree is the source, so its provenance draws on the **producer** functions; the served functions are a reading order, generated later.

Producer functions — the synchronic provenances, each a standing activity that does not end:

| Function (`provenance.id`) | The activity | Knowledge it mobilizes |
|---|---|---|
| **theory** | maintain the three essays and the readability patterns — the intellectual basis the product depends on | philosophy of language, speech-act theory, Ferraris's documentality, archival science |
| **writing** | author the guidance for writing *one* document — the forces, their moves, templates | the theory, technical-writing craft, Markdown/YAML |
| **structuring** | author the guidance for keeping the *whole* corpus — provenance, life cycle, scale, this tutorial | the theory, topology / near-decomposability, information architecture |
| **steering** | govern the project itself — foundation, roadmap, the decision register, the changelog, architecture, contribution rules | the project's own history and conventions |
| **imagine** | design and dream Phase II — the machine-operational layer, not yet built | LLM / agent tooling *(a new body of knowledge → a new community; deferred and re-founded)* |

Bounded producers — the diachronic provenances, which close and freeze:

| Provenance | The activity | Life |
|---|---|---|
| **project: phase-NN** | a single construction phase (01…10) | freezes its records when it closes; grouped into three **eras** (naive sketch 01–05, refoundation 06–09, phase II later) |
| a function's **change-stream** | the frozen trail a standing function leaves | e.g. the `CHANGELOG` is `diachronic` yet `provenance: steering` — a function's own stream, not a project |

Two findings this step forces, both refinements of current practice:

- **`onboarding` is not a producer function; it is a *served* order.**
  [proposed → Phase 08] The front doors (`README`, the two teach on-ramps) are *authored and maintained* by `steering`, `writing`, and `structuring` respectively; "onboarding" is the *reading order* in which a newcomer meets them, which belongs to a generated surface, not to the shelf.
  This retires the old `onboarding` provenance id.
- **`maintenance` stays folded into the owning function.**
  [decided, per ADR-012] There is no separate "maintenance" provenance; keeping a function's docs current *is* that function.

`imagine` band, named and parked (not-yet-enacted): the Phase II material — AI operating instructions, git hooks, validation/generation from the frontmatter.
It has no document of its own yet, by design; it lives as a line in the roadmap under `imagine`, to be pulled out when Phase I closes.

Holes named on purpose (not covered this pass):

- **use** as a *produced* thing — we serve users, but we do not yet generate the user surface; the reader view is deferred (`foundation.md` §6), so no `use`-owned source exists.
- **adopt / external contributor** — no onboarding path for a second contributor yet; deferred until the writing/structuring/frontmatter guidance it will be built on is complete.
- **license / compliance** — no `LICENSE`, no compliance posture; a real, named gap.

## Step 2 — Communities and distance

Because every producer function sits in essentially **one domain — the inscribed-act theory** — the audiences nearly collapse: `user` (documents their own project) and `contributor` (writes in this repo) are one discourse community sharing one code, and `decider` is us.
[decided, ADR-017/022]

Distance, in the habitus sense the tutorial now uses, is the gap between *our* habitus as authors and the intended reader's.
Here it reduces to **how much of the theory the reader already holds**, in a register that is frankly **academic** (Ferraris, illocution/perlocution) — a deliberate habitus that a beginner-facing document must open up and an initiated-facing one may presume.

- **novice** in the theory — the tutorials, the orients: concepts spelled out.
- **initiated** in the theory — the rules, the schema, the ADRs: concepts presumed.

`reader` is orthogonal: we write `H+M` almost everywhere, because keeping the catalogue machine-legible is Phase I's one commitment toward Phase II.
The machine can occupy `user`/`contributor` but never `decider`.
[decided]

## Step 3 — What each needs: know / do / govern

The exercise fills all three registers, which is why the product has three doors:

| Register | Our documents | Ordered for a returning contributor |
|---|---|---|
| **know** | the theory essays, `foundation.md`, the `concepts` files, `ARCHITECTURE.md` | first: **orient** (`README`, `foundation`), then **why** (theory, ADR rationale) |
| **do** | the two tutorials, the force templates, `setup.md`, `CONTRIBUTING.md` | last: the how-to, for the step we re-forget |
| **govern** | `ADR.md` register, the frozen phase records, `roadmap.md`, the `rules`/`mandate` docs | the decision log and the plan, consulted before adding to either |

The one in-between our own case throws up is the **structuring tutorial itself**: it is `do`-shaped guidance (a how-to) that also *orients* a newcomer.
Per Step 3 we do not force it; per Step 5 its provenance decides (below).

## Step 4 — Seams

Audited backward against what is already split, every seam holds:

- **theory vs guidance** — divergent lives (a stabilizing foundation vs living guidance) and a distance seam (initiated theory vs novice-facing product).
  Real.
- **writing vs structuring** — one document vs the whole corpus; each is large (≥3 docs), so a size seam.
  Real.
- **product vs the project's own governance** — the sharpest seam: `steering/` (current governance) and `phases/` (frozen ADRs) record *this repo's* own construction, which a user of the product never reads.
  Real, and the paradigm frozen/current case.
- **the schema** — a shared reference that `writing`, `structuring`, and (future) `imagine` all depend on; earns its own place.
- **generated / ephemeral** — we have essentially none (we are prose); the future generated surface and any validation output are *not* authored documentation and stay out of the shelf.

Named artifacts: our decision record is the **ADR** (`steering/ADR.md` register + one frozen file per decision under `phases/`); our **open questions** are not yet a record — see §Pending.

## Step 5 — Placement: provenance, life, and the tree

Source is shelved by **provenance**, organized for the **author** (the producer), with the register split *inside* a function once it earns it.
Life: standing functions stay **current**; phase projects **freeze**; deliberations are **current and decant into frozen** as they close.

The co-owned document, resolved by the round-2 rule: the **structuring tutorial** is *authored and maintained by* `structuring`, and merely *serves* the onboarding order — so its provenance is `structuring`, and the newcomer's orientation to it is a pointer on the generated surface, not a second home.
[decided] The same rule places `README` with `steering` (it orients about the whole project), served to onboarding.

### Derived front-matter vocabulary — the valid values for us

Read off the exercise; this is the controlled vocabulary our fields may take (encoding of `intention` and `register` remains the two open ⚑, §Pending).

| Field | Valid values (for this project) |
|---|---|
| `force` | `orient` `explain` `describe` `prove` `account` `instruct` `teach` `recommend` `mandate` `commit` `propose` `decide` (composite with `+`) |
| `register` *(derived from `force`)* | `know` `do` `govern` |
| `intention` | `state` `formative` `suasive` `affective` *(`state` = the floor only, ADR-026)* |
| `verb` *(optional, only when it diverges)* | e.g. `justify` `entail` (for `decide`), `diagnose` (for `account`), `illuminate` (for `explain`) |
| `view` | `synchronic` `diachronic` |
| `provenance.type` | `function` `project` |
| `provenance.id` — **function** | `theory` `writing` `structuring` `steering` `imagine` |
| `provenance.id` — **project** | `phase-01-foundation` … `phase-10-…` (grouped in eras: naive-sketch / refoundation / phase-II) |
| `audience` | `user` `contributor` `decider` *(here user≈contributor, one community; roles kept generic and project-refinable)* |
| `reader` | `H` `M` `H+M` |
| `distance` | `initiated` `novice` *(per community; our one community is the theory)* |
| `power` *(optional)* | `none` `low` `holds` |
| `status` | `draft` `stable` `deprecated` `accepted` |
| `retention` *(optional)* | `permanent` `until-release` `ephemeral` `legal:<dur>` |
| `axis` *(tree-root orient only)* | `provenance` *(the source shelf axis — replaces the old `scope`, ADR-018)* |
| `dominant-community` *(tree-root orient only)* | `contributor` *(the producer shelf serves the contributor; the user surface is generated)* |

The single most consequential change the exercise commits: the root axis moves from **`scope` (dominant `user`)** to **`provenance` (dominant `contributor`)**, because the source is the producer's shelf and the user order is a generated view.
[enacted — `docs/` dissolved into `steering/` + `imagine/` + root `phases/`, per ADR-018]

### The tree for us

The source tree the exercise yields — provenance-first, author-organized — now **enacted**: the generic `docs/` bucket is dissolved, `steering/` and `imagine/` sit at root, and `phases/` is a root provenance.

```text
README.md                         # orient · steering · current · root (served: onboarding)
LICENSE                           # NOT WRITTEN — named gap (govern/commit)

theory/                           # function: theory
  inscribed_act_organizational_document.md   # explain · know
  rhetoric_of_organizational_genres.md
  the_documentary_system.md
  patterns-ecriture-documentation.md

write/                            # function: writing (author ONE document)
  README.md · concepts.md · choosing.md · patterns.md · rules.md
  frontmatter.md                  # describe · the catalogue schema
  tutorial.md                     # teach on-ramp (served: onboarding)
  forces/<know|do|govern-and-record>/<force>/  README.md (stance) + template.md

structure/                        # function: structuring (keep the WHOLE corpus)
  README.md · concepts.md · setup.md · defaults.md · rules.md · audience.md
  tutorial.md                     # THIS tutorial — provenance structuring (served: onboarding)
  applied.md                      # deprecated (v3) → retire in Phase 08

steering/                         # function: steering — the project governing itself
  README.md · foundation.md · roadmap.md · ARCHITECTURE.md · CONTRIBUTING.md
  ADR.md                          # decide · govern · the register (current)
  CHANGELOG.md                    # account · govern · diachronic
  open-questions.md               # NEW — current deliberation, decants to phases/ [to add]

imagine/                          # function: imagine — Phase II, parked
  README.md

phases/                           # project provenance — frozen records (group by era [Phase 08])
  phase-01-foundation/ … phase-07-structuring-tutorial/

_legacy/                          # RETIRE once the nine forces migrate [Phase 08]
```

What the move did, and what remains:

- **done now:** dissolved the generic `docs/` bucket → `steering/` (governance) + root `phases/` (frozen records); added `imagine/` at root; re-declared the root `axis: provenance`, `dominant-community: contributor`; folded the `onboarding` provenance into each front door's author-function (`steering`/`writing`/`structuring`); updated references across the live docs.
- **remains (Phase 08):** retire `structure/applied.md` (superseded here) and `_legacy/`; add `steering/open-questions.md`; group `phases/` under its three eras; refound the v3 vocabulary (perlocution → intention, etc.).

## Pending — our own deliberation, dogfooded

The round-2 finding says a deliberation is a **current `govern` document that decants into frozen records**.
We have exactly one, and it should become `steering/open-questions.md`:

- **⚑ Decision 1 — encode `intention` coarse (`state|formative|suasive|affective`, ADR-026) or fine (`locate|model|enable|convince|…`).**
  Proposed: coarse.
  Open.
- **⚑ Decision 2 — `register` stored or derived from `force`.**
  Proposed: derived.
  Open.
- the retire-`_legacy` / migrate-nine-forces debt (roadmap), open until Phase 08 closes it.

Each closes into a frozen ADR when decided — the open-questions document sitting on the *current* side until then, which is the current/frozen device surviving contact with our own unsettled work.

## What this closes

Phase 07 set out to write the structuring tutorial and correct the front-end it exposed.
It ends by turning the tutorial on its author: the five steps run, our functions named (`theory`, `writing`, `structuring`, `steering`, `imagine`), our front-matter vocabulary derived, our tree confirmed, and our one live deliberation given a home.
The formal schema encoding (the two ⚑) and the physical file moves are Phase 09 and Phase 08 respectively — routed, not owed here.
