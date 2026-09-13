---
title: "Frontmatter schema — the machine-readable catalogue"
force: describe
verb: specify
intention: state
view: synchronic
provenance: { type: function, id: writing }
constitutive: no
audience: [user]
reader: H+M
status: stable
---

This reference specifies the **YAML frontmatter** every document carries.
It lives in `writing/` because you fill it *while writing*, even though several of its fields (`provenance`, `view`, `pin`) source their meaning from the organization (`../structuring/`).
The frontmatter is the *catalogue*: it gives the machine a document's coordinates without a human reading them.

Design note: the schema carries only **hard coordinates not derivable from one another**.
It omits `diataxis` (re-derived by `force` × `intention`, see [`concepts.md`](concepts.md)), any direction-of-fit field (fixed by `force`), and `register` (derived from `constitutive` and `force`).
Storing any of them would encode the same fact twice.

## Fields

`R` = required, `O` = optional.

| Field | R/O | Values | Role |
|---|---|---|---|
| `title` | R | free text | Human title. |
| `force` | R | `orient` `explain` `describe` · `instruct` `teach` `recommend` · `mandate` `commit` `propose` `decide` `prove` `account` | The dominant illocutionary force (grouped by door: know · do · govern-and-record). One only; if two, dominant `+` other. See [`concepts.md`](concepts.md). |
| `verb` | O | generative verb | Soft summary of the whole tuple; picks the move structure. Store only when it diverges for a perlocutionary (a) or illocutionary-internal (b) reason — not for a recipient shift (c). |
| `intention` | R | `state` `formative` `suasive` `affective` | Which change the act works in the reader, parallel to `force`. `state` = the constitutive floor (served, not moved); an aim may rise above it — `formative` (forming a map, model, or competence), `suasive` (moving assent), `affective` (moving feeling). The coarse family is what you store; the finer readings (`locate`/`model`/`enable`/`convince`) are ways of reading it, not values (ADR-015/026; coarse settled by ⚑ Decision 1). |
| `constitutive` | R | `yes` `no` | Does the act **posit or fix a social object** — a norm, an obligation, a decision, an evidentiary record — or merely serve a reader? A conscious judgement per document, not derived from `force`: an authoritative `recommend` constitutes, a friendly one does not. Founds the derived `register`. See [`../operationalizing/constitutive.md`](../operationalizing/constitutive.md). |
| `view` | R | `synchronic` `diachronic` | State kept current vs. frozen change. Seam in `../structuring/concepts.md`. |
| `provenance` | R | `{type, id}` | `type: function` (maintained) or `type: project` (freezes). See `../structuring/concepts.md`. |
| `audience` | R | roles, e.g. `[contributor, decider]` | Generic roles `user` / `contributor` / `decider`, refinable per project. See [`../structuring/audience.md`](../structuring/audience.md). |
| `reader` | R | `H` `M` `H+M` | Human / machine / both. Sub-kinds like `M[rag]` only if a project needs them. See [`../structuring/audience.md`](../structuring/audience.md). |
| `distance` | O | `peer` `near` `far` | Shared code → scaffolding. `patterns.md` recipient section. |
| `power` | O | `none` `holds` | Sanction → armor. |
| `status` | R | `draft` `stable` `deprecated` | Life cycle; make staleness explicit. |
| `written-at` | O | phase, e.g. `mvp` `v3` | Production phase. |
| `valid-for` | O | phase | Phase the content is valid for; the gap is computable. |
| `supersedes` / `superseded-by` | O | path/id | Chain frozen records (ADRs). |
| `retention` | O | `permanent` `until-release` `ephemeral` `legal:<duration>` | Defaults by force in `../structuring/defaults.md`. |
| `pin` | O | submodule ref / SHA | Fixity anchor for a cross-project reference. `../structuring/concepts.md`. |
| `hash` | O | `sha256:<64 hex>` | Fixity seal of a *frozen* record — written at close, verified thereafter. Where `pin` fixes what a document points at, `hash` fixes what the document is. |
| `axis` | R* | shelf axis, e.g. `scope` `function` `component` | *Required only on the root orient of a tree* (omitted elsewhere). The order the shelf is browsed by. `../structuring/rules.md`. |
| `dominant-community` | R* | a role, e.g. `contributor` | *Required only on the root orient of a tree.* The community the shelf's axis is chosen to serve (see [`../structuring/audience.md`](../structuring/audience.md)). |

## Derivable views (generate, do not store)

Computed, read by tooling and newcomers, and **never written into the frontmatter**:

- **`register`** (know / do / govern) — `constitutive: yes` ⇒ `govern`; otherwise the force's direction of fit ⇒ `know` (word-to-world: `orient` `explain` `describe` `prove` `account`) or `do` (world-to-word: `instruct` `teach` `recommend` `mandate` `commit` `propose` `decide`).
  The third bin is not a third direction of fit — it is the constitutive one.
  Storing `register` is an error.
- **Direction of fit** — fixed by `force`, per the same table.
- **`diataxis`** — `force` × `intention`, where the register is know or do.

## Validation rules

- `force`, `intention`, `constitutive`, `view`, `provenance`, `audience`, `reader`, `status` are **required** on every non-ephemeral document.
  A file lacking them does not enter the catalogue.
- `constitutive` has **no default**: it is required precisely so that the judgement is made consciously rather than inherited.
- `intention` is **not** constrained by `force` — it is an independent coordinate, and any pairing is permitted.
  Each force has a *typical* intention (`orient`/`explain`/`teach`→`formative`, `prove`/`decide`→`suasive`, others→`state`), but a divergent pairing is legal and often meaningful — an `account` that explains a failure carries `intention: formative`; a `describe` that means to convince carries `suasive`.
  A validator may *surface* an unusual pairing for review; it never rejects one.
  (We do not commit to a table of which pairings are possible — that would be a definitiveness the theory's "saturated, not closed" stance forbids.)
- `provenance.type: project` ⇒ not rewritten after closure; a change is a *new* document via `supersedes`.
  Consistent with `view: diachronic`.
- `view: synchronic` with `provenance.type: project` is a suspect pair; allow only knowingly.
- `status: deprecated` requires a non-null `superseded-by` (or an explicit no-replacement note).
- `hash`, once written, must keep matching its record; a broken seal means a frozen record changed, and is either reverted or consciously re-sealed.
- `reader` including `M` ⇒ the document must satisfy the machine rules in [`rules.md`](rules.md) (self-sufficient chunks, no cross-section anaphora).
- The **root orient document of a tree** (the top `README.md`) must carry `axis` and `dominant-community`; no other document carries them.
  A validator flags a tree root missing either, or a non-root file that declares them.

## Full example

```yaml
---
title: "ADR-014 — Move from REST to gRPC for the ingestion service"
force: decide
verb: justify
intention: suasive
view: diachronic
provenance: { type: project, id: migration-2026 }
constitutive: yes
audience: [decider, contributor]
reader: H+M
distance: near
power: none
status: stable
supersedes: decisions/ADR-009.md
retention: permanent
pin: projects/ingestion@a1b2c3d
hash: sha256:3b1f…
---
```

Its `register` is not written down: `constitutive: yes` derives `govern`.

## In short

Eight fields required everywhere — `force`, `intention`, `constitutive`, `view`, `provenance`, `audience`, `reader`, `status` — plus `title`.
They catalogue, validate, and route.
`verb` guides writing when it diverges; `distance`/`power` tune the address; the life-cycle fields track trajectory, and `pin`/`hash` fix what a record points at and what it is.
Anything derivable — `register`, direction of fit, `diataxis` — is generated, never stored.
