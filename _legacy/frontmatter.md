---
title: "Frontmatter schema — the machine-readable catalogue"
force: describe
verb: specify
perlocution: none
view: synchronic
audience: [developer, AI, tooling]
status: stable
written-at: v2
valid-for: v2
---

This reference specifies the **YAML frontmatter** every document in the system carries. The frontmatter is the *catalogue*: it gives the machine (index generators, validators, RAG, future AI) a document's coordinates without a human having to read them. Scope: all fields, their allowed values, whether they are required or optional, plus a minimal and a full example. Not covered: metadata specific to a particular site generator (declared in addition, without conflict).

Design note: the schema carries only **hard coordinates that are not derivable from one another**. It deliberately omits a `diataxis` field (fully re-derived by `force` × `perlocution`, see `writing.md` §0) and a direction-of-fit field (fixed by `force`). Storing either would encode the same fact twice.

## Fields

Recommended stable order. `R` = required, `O` = optional.

| Field | R/O | Values | Role |
| --- | --- | --- | --- |
| `title` | R | free text | Human title of the document. |
| `force` | R | `orient` `explain` `describe` `prove` `account` `instruct` `teach` `recommend` `mandate` `commit` `propose` `decide` | The dominant illocutionary force. See `writing.md` §I. One only; if two, put the dominant one and list the other after `+` (`explain+mandate`). |
| `verb` | O | generative verb | The soft summary of the whole coordinate tuple; it picks the move structure. Fill it only when it **diverges** from the force name for a perlocutionary reason (a) or an illocutionary-internal reason (b) — e.g. `decide`→`justify`, `account`→`diagnose`. Do **not** invent a verb for a mere recipient shift (reason c); set `distance`/`power` instead. See `writing.md` §0. |
| `perlocution` | R | `none` `locate` `model` `enable` `convince` | Which change the act works in the reader (Austin's perlocutionary aspect), parallel to `force`. `none` = reader served, not changed. Open, saturated list. See `writing.md` §0. |
| `view` | R | `synchronic` `diachronic` | State kept current (`synchronic`) vs. frozen change (`diachronic`). The seam of `structure.md` §6. |
| `provenance` | R | object `{type, id}` | `type: function` (permanent, maintained) or `type: project` (bounded, freezes). `id`: stable identifier of the function or project. |
| `distance` | O | `peer` `near` `far` | How much code the reader shares. Sets the scaffolding. `writing.md` §II. |
| `power` | O | `none` `holds` | Whether the reader can sanction the author. Sets the armor. |
| `audience` | O | list, e.g. `[developer, AI]` | Intended readers. Including `AI` signals that LLM-specific patterns take priority on this document. |
| `status` | R | `draft` `stable` `deprecated` | Life cycle. An LLM does not detect implicit staleness: make it explicit. |
| `written-at` | O | phase, e.g. `poc` `mvp` `v2` | Production phase. Encodes context an ISO date does not carry. |
| `valid-for` | O | phase | Phase for which the content is deemed valid. The `written-at`/`valid-for` gap is computable. |
| `superseded-by` | O | path/id, or `null` | If `status: deprecated`, points to the replacing document. |
| `supersedes` | O | path/id | Reciprocal: this document replaces that one. For `decide`, chains the ADRs. |
| `retention` | O | `permanent` `until-release` `ephemeral` `legal:<duration>` | Retention rule. Defaults by force in `structure.md` §7. |
| `pin` | O | submodule ref / SHA | For a cross-project docs-repo document that references an exact project state. This is the fixity bond (`structure.md` §2). |

## Derivable views (do not store, generate)

These are computed from `force` and read by tooling / newcomers; they are not fields:

- **door** — `know` (savoir), `do` (savoir-faire), `govern & record`. The newcomer routing of `writing.md` §0.
- **direction of fit** — word-to-world vs world-to-world, fixed by the force.
- **diataxis** — the four user-facing cells, = `force` × `perlocution` where the door is know/do.

## Validation rules

**RULE.** `force`, `perlocution`, `view`, `provenance`, `status` are required on every non-ephemeral document. A file lacking them does not enter the catalogue.

**RULE.** `perlocution` is constrained by `force`: `orient`→`locate`, `explain`→`model`, `teach`→`enable`, `prove`/`decide`→`convince`, all others→`none`. Any other pairing is an error. (A postmortem written under the verb `diagnose` is the one sanctioned drift: `force: account` may then carry `perlocution: model`.)

**RULE.** `provenance.type: project` implies the document is not rewritten after the project closes; if it must change, the new content is a *new* document linking the old via `supersedes`. Consistent with `view: diachronic`.

**RULE.** `view: synchronic` with `provenance.type: project` is a suspect pair (a maintained state normally belongs to a function): allow it only knowingly.

**RULE.** `status: deprecated` requires a non-null `superseded-by` (or an explicit justification for abandonment without a replacement).

## Minimal example

For a note or a simple document:

```yaml
---
title: "Branch naming policy"
force: mandate
perlocution: none
view: synchronic
provenance: { type: function, id: dev-conventions }
status: stable
---
```

## Full example

For an ADR referenced in a cross-project docs repo:

```yaml
---
title: "ADR-014 — Move from REST to gRPC for the ingestion service"
force: decide
verb: justify
perlocution: convince
view: diachronic
provenance: { type: project, id: migration-2026 }
distance: near
power: none
audience: [developer, AI, architect]
status: stable
written-at: v2
valid-for: v2
supersedes: decisions/ADR-009.md
retention: permanent
pin: projects/ingestion@a1b2c3d
---
```

## How the catalogue is used

The reader never reads these tags: they browse the tree (`structure.md` §4). The machine reads them to **generate** index surfaces in `catalog/` — by force, by door, by function, by status, by audience. It also reads them to validate (the RULES above), to route RAG (filter by `audience`, `status`, `view`), and — a later step — to drive a writing AI: `force` + `verb` select the move structure, `perlocution` decides whether to organize by the reader, `distance` + `power` set the register, `view` + `provenance` decide whether the AI may edit in place or must create a new record.

## In short

Five fields required everywhere — `force`, `perlocution`, `view`, `provenance`, `status` — plus `title`. They suffice to catalogue, validate, and route. The rest refines: `verb` is the soft summary that guides writing when it diverges, `distance`/`power` set the register, `written-at`/`valid-for`/`retention`/`supersedes` the life cycle, `pin` the cross-project archival anchor. Anything derivable from `force` (door, direction of fit, diataxis) is generated, never stored.
