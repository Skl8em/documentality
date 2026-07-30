---
title: "Frontmatter schema — the machine-readable catalogue"
force: describe
verb: specify
perlocution: none
view: synchronic
provenance: { type: function, id: writing }
audience: [user]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

This reference specifies the **YAML frontmatter** every document carries. It lives in `write/` because you fill it *while writing*, even though several of its fields (`provenance`, `view`, `pin`) source their meaning from the organization (`../structure/`). The frontmatter is the *catalogue*: it gives the machine a document's coordinates without a human reading them.

Design note: the schema carries only **hard coordinates not derivable from one another**. It omits `diataxis` (re-derived by `force` × `perlocution`, see [`concepts.md`](concepts.md)) and any direction-of-fit field (fixed by `force`). Storing either would encode the same fact twice.

## Fields

`R` = required, `O` = optional.

| Field | R/O | Values | Role |
|---|---|---|---|
| `title` | R | free text | Human title. |
| `force` | R | `orient` `explain` `describe` · `instruct` `teach` `recommend` · `mandate` `commit` `propose` `decide` `prove` `account` | The dominant illocutionary force (grouped by door: know · do · govern-and-record). One only; if two, dominant `+` other. See [`concepts.md`](concepts.md). |
| `verb` | O | generative verb | Soft summary of the whole tuple; picks the move structure. Store only when it diverges for a perlocutionary (a) or illocutionary-internal (b) reason — not for a recipient shift (c). |
| `perlocution` | R | `none` `locate` `model` `enable` `convince` | Which change the act works in the reader, parallel to `force`. `none` = served, not changed. Open, saturated list. |
| `view` | R | `synchronic` `diachronic` | State kept current vs. frozen change. Seam in `../structure/concepts.md`. |
| `provenance` | R | `{type, id}` | `type: function` (maintained) or `type: project` (freezes). See `../structure/concepts.md`. |
| `audience` | R | roles, e.g. `[contributor, decider]` | Generic roles `user` / `contributor` / `decider`, refinable per project. See [`../structure/audience.md`](../structuring/audience.md). |
| `reader` | R | `H` `M` `H+M` | Human / machine / both. Sub-kinds like `M[rag]` only if a project needs them. See [`../structure/audience.md`](../structuring/audience.md). |
| `distance` | O | `peer` `near` `far` | Shared code → scaffolding. `patterns.md` recipient section. |
| `power` | O | `none` `holds` | Sanction → armor. |
| `status` | R | `draft` `stable` `deprecated` | Life cycle; make staleness explicit. |
| `written-at` | O | phase, e.g. `mvp` `v3` | Production phase. |
| `valid-for` | O | phase | Phase the content is valid for; the gap is computable. |
| `supersedes` / `superseded-by` | O | path/id | Chain frozen records (ADRs). |
| `retention` | O | `permanent` `until-release` `ephemeral` `legal:<duration>` | Defaults by force in `../structure/defaults.md`. |
| `pin` | O | submodule ref / SHA | Fixity anchor for a cross-project reference. `../structure/concepts.md`. |
| `axis` | R* | shelf axis, e.g. `scope` `function` `component` | *Required only on the root orient of a tree* (omitted elsewhere). The order the shelf is browsed by. `../structure/rules.md`. |
| `dominant-community` | R* | a role, e.g. `contributor` | *Required only on the root orient of a tree.* The community the shelf's axis is chosen to serve (see [`../structure/audience.md`](../structuring/audience.md)). |

## Derivable views (generate, do not store)

Computed from `force`, read by tooling / newcomers: **door** (know / do / govern-and-record), **direction of fit** (word-to-world vs world-to-world), **diataxis** (`force` × `perlocution` where the door is know/do).

## Validation rules

- `force`, `perlocution`, `view`, `provenance`, `audience`, `reader`, `status` are **required** on every non-ephemeral document. A file lacking them does not enter the catalogue.
- `perlocution` is **not** constrained by `force` — it is an independent coordinate, and any pairing is permitted. Each force has a *typical* perlocution (`orient`→`locate`, `explain`→`model`, `teach`→`enable`, `prove`/`decide`→`convince`, others→`none`), but a divergent pairing is legal and often meaningful — an `account` that explains a failure carries `perlocution: model`; a `describe` that means to convince carries `convince`. A validator may *surface* an unusual pairing for review; it never rejects one. (We do not commit to a table of which pairings are possible — that would be a definitiveness the theory's "saturated, not closed" stance forbids.)
- `provenance.type: project` ⇒ not rewritten after closure; a change is a *new* document via `supersedes`. Consistent with `view: diachronic`.
- `view: synchronic` with `provenance.type: project` is a suspect pair; allow only knowingly.
- `status: deprecated` requires a non-null `superseded-by` (or an explicit no-replacement note).
- `reader` including `M` ⇒ the document must satisfy the machine rules in [`rules.md`](rules.md) (self-sufficient chunks, no cross-section anaphora).
- The **root orient document of a tree** (the top `README.md`) must carry `axis` and `dominant-community`; no other document carries them. A validator flags a tree root missing either, or a non-root file that declares them.

## Full example

```yaml
---
title: "ADR-014 — Move from REST to gRPC for the ingestion service"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: migration-2026 }
audience: [decider, contributor]
reader: H+M
distance: near
power: none
status: stable
written-at: v2
valid-for: v2
supersedes: decisions/ADR-009.md
retention: permanent
pin: projects/ingestion@a1b2c3d
---
```

## In short

Seven fields required everywhere — `force`, `perlocution`, `view`, `provenance`, `audience`, `reader`, `status` — plus `title`. They catalogue, validate, and route. `verb` guides writing when it diverges; `distance`/`power` set the register; the life-cycle and `pin` fields track trajectory and fixity. Anything derivable from `force` is generated, never stored.
