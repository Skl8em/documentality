---
title: "Frontmatter schema — the machine-readable catalogue"
force: describe
verb: specify
formative: false
diataxis: reference
view: synchronic
audience: [developer, AI, tooling]
status: stable
written-at: v1
valid-for: v1
---

This reference specifies the **YAML frontmatter** every document in the system carries. The frontmatter is the *catalogue*: it gives the machine (index generators, validators, RAG, future AI) a document's coordinates without a human having to read them. Scope: all fields, their allowed values, whether they are required or optional, plus a minimal and a full example. Not covered: metadata specific to a particular site generator (declared in addition, without conflict).

## Fields

Recommended stable order. `R` = required, `O` = optional.

| Field | R/O | Values | Role |
|---|---|---|---|
| `title` | R | free text | Human title of the document. |
| `force` | R | `orient` `explain` `describe` `prove` `account` `instruct` `teach` `mandate` `commit` `propose` `decide` | The dominant illocutionary force. See `writing.md` §I. One only; if two, put the dominant one and list the other after `+` (`explain+mandate`). |
| `verb` | O | associated generative verb | The verb that guides writing (e.g. `decide`→`justify`). Redundant with `force` but useful to the writer and the AI. |
| `formative` | R | `true` `false` | Does the act aim to change the reader's internal state? True for `orient`, `explain`, `teach` only. |
| `diataxis` | O | `tutorial` `how-to` `reference` `explanation` | Diátaxis type where applicable (mainly user-facing forces). Signals the expected reading mode. |
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

## Validation rules

**RULE.** `force`, `view`, `provenance`, `status` are required on every non-ephemeral document. A file lacking them does not enter the catalogue.

**RULE.** `formative: true` is allowed only if `force` ∈ {`orient`, `explain`, `teach`}. Any other combination is an error.

**RULE.** `provenance.type: project` implies the document is not rewritten after the project closes; if it must change, the new content is a *new* document linking the old via `supersedes`. Consistent with `view: diachronic`.

**RULE.** `view: synchronic` with `provenance.type: project` is a suspect pair (a maintained state normally belongs to a function): allow it only knowingly.

**RULE.** `status: deprecated` requires a non-null `superseded-by` (or an explicit justification for abandonment without a replacement).

## Minimal example

For a note or a simple document:

```yaml
---
title: "Branch naming policy"
force: mandate
view: synchronic
provenance: { type: function, id: dev-conventions }
formative: false
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
formative: false
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

The reader never reads these tags: they browse the tree (`structure.md` §4). The machine reads them to **generate** index surfaces in `catalog/` — by force, by function, by status, by audience. It also reads them to validate (the RULES above), to route RAG (filter by `audience`, `status`, `view`), and — a later step — to drive a writing AI: `force` + `verb` select the move structure, `distance` + `power` set the register, `view` + `provenance` decide whether the AI may edit in place or must create a new record.

## In short

Four fields required everywhere — `force`, `view`, `provenance`, `status` — plus `title`. They suffice to catalogue, validate, and route. The rest refines: `verb` and `formative` guide the writing, `distance`/`power` the register, `written-at`/`valid-for`/`retention`/`supersedes` the life cycle, `pin` the cross-project archival anchor.
