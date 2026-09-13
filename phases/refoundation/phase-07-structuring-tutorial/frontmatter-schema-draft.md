---
title: "Refounded frontmatter schema — draft for confirmation"
force: describe
intention: state
view: synchronic
provenance: { type: project, id: phase-07-structuring-tutorial }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

This is the refounded frontmatter, brought forward from Phase 09 so it can be the single target of the Phase-08 refactor.
It is a **draft**: two decisions, marked **⚑**, are yours to confirm before it becomes the real `write/frontmatter.md`.
The guiding rule is unchanged: store only **hard coordinates that are not derivable from one another**; everything a force already fixes is *generated, never stored*.

## Stored fields

`R` = required on every non-ephemeral document, `O` = optional, `R*` = required only on a tree-root orient.

| Field | R/O | Values | Role |
|---|---|---|---|
| `title` | R | free text | Human title. |
| `force` | R | the recognized cell — `orient` `explain` `describe` `prove` `account` `instruct` `teach` `recommend` `mandate` `commit` `propose` `decide` (composite with `+`) | The illocutionary act, as a reified cell of direction-of-fit × intention. Open, saturated. |
| `intention` | R | `state` `formative` `suasive` `affective` | The perlocutionary aim **above the floor**. `state` = the floor is established, no aim above it (served, never "reader untouched"). ⚑ **Decision 1.** (ADR-026) |
| `verb` | O | generative verb | Soft summary of the tuple; stored only when it diverges (e.g. `decide`→`justify`/`entail`, `account`→`diagnose`). |
| `view` | R | `synchronic` `diachronic` | Maintained state vs frozen change. |
| `provenance` | R | `{type: function\|project, id}` | The producing/maintaining activity. `synchronic ⇒ function`; `diachronic ⇒ its producer` (a project, or a function's change-stream). |
| `concerns` | O | one or more activity ids (or `all`) | The activity/activities a document *governs or bears on* — a **relation**, distinct from `provenance` (who produced it). One ⇒ vertical (locally ownable); several ⇒ transversal. Lets the per-activity view be *generated*, not moved (ADR-025). |
| `audience` | R | roles, e.g. `[contributor, decider]` | Generic roles `user`/`contributor`/`decider`, derived from the functions (ADR-022), project-refinable. |
| `reader` | R | `H` `M` `H+M` | Human / machine / both — orthogonal to role. |
| `distance` | O | `initiated` `novice` (per the doc's community) | How much of *that community's* code the reader shares; per-domain, not global (ADR-022). |
| `power` | O | `none` `low` `holds` | The recipient's sanction over the writer — graded, not binary. |
| `status` | R | `draft` `stable` `deprecated` (`accepted` for decisions) | Life cycle. |
| `written-at` / `valid-for` | O | phase | Production vs validity phase. |
| `supersedes` / `superseded-by` | O | path/id | Chain frozen records. |
| `retention` | O | `permanent` `until-release` `ephemeral` `legal:<dur>` | Retention rule. |
| `pin` | O | submodule ref / SHA | Fixity anchor for a cross-project reference. |
| `axis` | R* | e.g. `provenance` `function` `scope` | The tree-root shelf axis. |
| `dominant-community` | R* | a role | Whom the shelf serves. |
| `governance-axis` | R* | `central` `local` | Whether decisions are governed by one central register + phase records, or owned locally by each activity (transversals escalate). Default `central` (ADR-025). |

## Generated, never stored

Computed from `force` (and `intention`), read by tooling and newcomers:

- **register** — `know` / `do` / `govern`, from the force's direction of fit. ⚑ **Decision 2.**
- **direction of fit** — word-to-world / world-to-word / both, fixed by the force.
- **diataxis** — the four user-facing cells, = `force` × `intention` where the register is know/do.
- **era** — the coarse grouping of a phase (`provenance`), for the record's orient.
- **the constitutive floor** — universal; every inscription carries it, so it is never a field.

## The two decisions ⚑

**Decision 1 — how to encode intention + floor.**
The floor is universal, so it is *not* stored; what varies is the aim above it.
*Proposed:* store `intention ∈ {state, formative, suasive, affective}` (`state` = the floor only, per ADR-026) — coarse enough to route, and honest that the finer flavour (formative→map/model/competence, suasive→convince) is usually derivable from the force and stored only when it diverges.
*Alternative:* store the fine flavour always (`locate|model|enable|convince|…`), more precise but more to maintain and closer to the old per-force typology we moved away from.

**Decision 2 — is `register` stored or derived?**
*Proposed:* **derived** from `force` (each force has a fixed direction of fit → register), like `diataxis` — storing it would double-encode what the force already fixes.
*Alternative:* store it as a convenience for navigation/filtering, accepting the redundancy.

## Validation rules (unchanged in spirit)

- `force`, `intention`, `view`, `provenance`, `audience`, `reader`, `status` required on every non-ephemeral doc.
- `intention` is **not** constrained by `force` (pairings are open, ADR-015); the force's *typical* intention is a default a validator may surface, never enforce.
- `synchronic ⇒ provenance.type: function`; `provenance.type: project ⇒ frozen after closure` (a change is a new doc via `supersedes`).
- tree-root orient carries `axis` + `dominant-community`; no other file does.
- `reader` including `M` ⇒ the doc must satisfy the machine rules (self-sufficient chunks, no cross-section anaphora).

Confirm the two ⚑ and I write this as `write/frontmatter.md`, then Phase 08 refactors every file to it in one pass.
