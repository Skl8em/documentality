---
title: "T1(a) — the tooling's communities, mapped"
force: explain
verb: illuminate
intention: formative
view: synchronic
provenance: { type: project, id: phase-12-codifying }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

`plan.md` T1(a): run the structuring front-end (`../../../structuring/tutorial.md` Steps 2–3) on the tooling itself — `scripts/`, `schema/`, the gate — before writing a single fiche.
Step 1 (activities) is not re-derived from scratch: the plan already named four candidates to confirm or cut.
This document reads communities off them, judges distance, states what each needs, rules on the two questions the plan left open, and hands the split to T1(c).

## Step 1 recap — the candidate activities, confirmed or cut

| Activity | Verdict |
| --- | --- |
| Run the gate; decode a failure and fix it | **confirmed** — the highest-frequency activity in the whole repo |
| Extend the tooling — add or change a check, touch `scripts/*.py` or `schema/frontmatter-rules.yaml` | **confirmed** — rare, but it is exactly what Phase 11 did without explaining itself |
| Install and configure the pipeline in a second project | **cut this pass** — see §Cut |
| Run the gate unattended (CI, pre-commit, a coding agent) and read only its output | **confirmed** — `reader: M`, distinct from the human doing the same activity by hand |

## Step 2 — communities and distance

Distance is per activity and per **field** (`../../../structuring/tutorial.md` Step 2): the same physical person can be close to us in one body of knowledge and far in another.
Until now this repo mobilized essentially one field, the theory (`foundation.md` §2–3), which is why `user ≈ contributor` could collapse into one discourse community.
`codifying` is the first time a second field — the tooling's own engineering (Python, the YAML/JSON split, the ADR register format `ulid_check.py` assumes) — is named as something a reader must be at home in.
That is a real, new axis, not a rhetorical one: two of the four "why this phase exists" gaps in `plan.md` are exactly a maintainer-shaped document that was never written.

| Community | Base role | Field | Distance | Why |
| --- | --- | --- | --- | --- |
| gate-runner | `contributor` (unrefined) | tooling engineering | **novice** | fixing a bad frontmatter field must need zero Python or schema-mechanics knowledge — the message does the teaching, not a fiche |
| gate-runner | `contributor` (unrefined) | the theory (force/intention/audience/…) | **initiated** | unchanged by this phase; already the corpus-wide default (`foundation.md` §3) |
| maintainer | `contributor`, refined | tooling engineering | **initiated** | must hold `check.py`'s sequencing, the YAML-source/JSON-generated split, and `ulid_check.py`'s register-format assumption *before* touching any of it, or a change corrupts the corpus silently |
| maintainer | `contributor`, refined | the theory | **initiated** | same person, same corpus, unchanged |
| the machine | occupies `contributor`/`user` (`../../../structuring/audience.md` §Axis 2) | — | **far, always** | `reader: M` is the recipient relation pushed to its limit; not a knowledge gap, an explicitness requirement |

The gate-runner and the maintainer are **not two base roles** — they are one `contributor` wearing two hats, distinguished only by which field's distance is at issue for a given activity, exactly the case `../../../structuring/tutorial.md` Step 2 names ("close to you in your Python and far in your statistics").
The adopter is not in this table; see §Cut.

## Step 3 — what each needs, and in what order

| Community | Needs | Order |
| --- | --- | --- |
| gate-runner | **do**, and only `do` — the failing message *is* the interaction; they did not come to learn the engine, they came to unblock a commit | fix, inline, now |
| maintainer | **know** first (why the gate sequences every check into one property; why the split holds; why referential integrity must be symmetric), **do** second (where `docsys.yaml` holds the out-of-scope list, the register's shape and the check list T1(b) moved out of the scripts, and the residue in [`engine-config-seam.md`](engine-config-seam.md) that still lives in code) | know before do — acting blind here can break the corpus, not just fail a lint |
| the machine | **do** only, in the strictest sense: no session memory is assumed, so every message must carry the file, the rule, and the fix with nothing left to a prior turn | no order — each message is the whole interaction, self-sufficient or not at all |

## Ruling 1 — is `maintainer` declared in the schema, or left as the linter's warning?

**Left as the warning, named in prose instead of promoted to an enum.**

`schema/frontmatter-rules.yaml`'s `audience_base_roles` are error-checked on purpose; anything else is a **warning**, by design (`scripts/frontmatter_lint.py:139-147`), precisely so a project can name its own sub-roles without touching the schema every time — `../../../structuring/audience.md` already demonstrates this for a generic IT project (`developer`, `reviewer`, `ops/SRE`, …) without any of them entering `error_enums`.
One project-local sub-role, used across the three fiches T1(c) is about to write, does not clear the bar that would justify enum-promotion: the fractal rule (`../../../structuring/tutorial.md`) says refine only when the coarse version starts to hurt, and it has not.

What was actually missing was not schema coverage — the warning already fires correctly on `maintainer` today — it was that nobody had ever *written down* that `maintainer` is this project's deliberate refinement of `contributor`, so the warning read as noise instead of as an intended, examined value.
That gap closes here: `maintainer` = `contributor`, refined, for anything whose distance is judged in the tooling-engineering field rather than the theory field.
T1(c)'s three fiches carry `audience: [contributor]` with this document as the pointer that explains what `maintainer` means when it is used; a paragraph goes into `../../../structuring/audience.md`'s this-project example, beside the generic-IT-project sub-role list that reference already carries, so the next reader of it finds the ruling instead of re-deriving it.

## Ruling 2 — the `contributor ≈ user` premise, revisited for codifying

**Holds, narrowly, and codifying is the reason to say so out loud rather than let it erode by assumption.**

`foundation.md` §3 collapses `user ≈ contributor` because "our functions sit in essentially one domain" (§2: "that near-single domain is *why* our communities collapse below — a derived fact, not an assumption").
That derivation was always scoped to the theory.
Naming tooling-engineering as a second mobilized field (this document, Step 2) does not reopen the collapse — nobody reads the product as a `user` who is not also a `contributor` here, and that has not changed — but it does mean the collapse can no longer be read as covering *everything* the repo now mobilizes.
`foundation.md` §2 already hedged this with "light tooling (Markdown, git)"; `codifying` is exactly that hedge growing past "light."

So the premise is reaffirmed for the **role** axis (still three families, still one discourse community for `user`/`contributor`) and qualified for the **distance** axis (now two fields, not one, and a document must say which field its `distance` value is measured in when it is not the theory).
T1(c) states this explicitly wherever the function set is enumerated, so `foundation.md` §3 stops reading as though the derivation still covers the whole repo.

## What this hands to T1(c)

| Planned artifact | Audience | Distance (field) |
| --- | --- | --- |
| `codifying/README.md` (orient) | `contributor` (both hats) | brief for the gate-runner, a pointer into the fiches for the maintainer |
| gate-architecture fiche (why `check.py` sequences every check into one property) | `contributor`/maintainer | initiated, tooling engineering |
| YAML-source / JSON-generated split fiche | `contributor`/maintainer | initiated, tooling engineering |
| referential-integrity fiche (symmetric supersession, dangling pointer as hard error) | `contributor`/maintainer | initiated, tooling engineering |
| the gate's own error messages (not a fiche — the running tool's text) | the machine, and the gate-runner incidentally | far, always (`reader: M`) — checked against self-sufficiency per `plan.md`'s verification list |
| `codifying`'s own ADR (adopting the seventh function) | `contributor`, `decider` | initiated, theory — it is a decision record, not a fiche |

## Cut — the adopter

Named, not documented: installing and configuring `scripts/`/`schema/` in a second project has no one to write for yet — `plan.md`'s own "Explicitly out of scope" section defers extraction "until a second project wants the pipeline," and T1(b)'s engine/config seam is what would make that adoption cheap when it happens, not this step.
Writing a fiche for a community that does not exist would fix the split by assumption, exactly what T1(a) exists to avoid.
The hole is deliberate and stays visible here rather than silently absent from the map; revisit the day a second consumer is real, or park a line under `imagining/` if the intent needs a home before then.
