---
title: "Audience — who a document is written toward"
force: describe
verb: specify
intention: state
view: synchronic
provenance: { type: function, id: structuring }
audience: [user]
reader: H+M
status: stable
---

Audience is **project-specific in its details but generic in its shape**. Every project, whatever its domain, has the same three functional roles; a project refines them but does not invent a fourth family. This reference fixes the model and the frontmatter fields, then gives two concrete instantiations: this project, and a generic IT project.

Audience has **two orthogonal axes**. The role says *who, functionally*; the reader kind says *human or machine*. They vary independently — an audit dossier and a RAG-indexed reference can both target a `decider`, yet one is `H` and the other `H+M`.

## Axis 1 — role (generic, project-refinable)

The three roles align with the three doors (`../writing/forces/*`), which is why they are a good default lens: each role lives mostly behind one door.

| Role | Lives behind | Reads mostly | What they do here |
| --- | --- | --- | --- |
| **user** | know (+ do) | orient, explain, describe, instruct, teach | consumes the product/output; wants to understand and operate it |
| **contributor** | do (+ govern) | instruct, recommend, teach, mandate; writes account, propose | builds and maintains; follows the rules, records changes |
| **decider** | govern & record | decide, propose, commit; reads prove, account | steers, approves, is accountable |

They may be the **same people** (a solo maintainer is all three) or **refined** into sub-roles, but the three families are generic enough to apply everywhere. A document names one or more roles in `audience`; naming none means it is not addressed to a reader and probably should not exist.

## Axis 2 — reader kind (the `reader` flag)

Orthogonal to role: is the document optimized for a human reader, a machine reader (LLM / agent), or both?

| `reader` | Meaning | Consequence |
| --- | --- | --- |
| `H` | human only | optimize for scanning, F-pattern, brevity; LLM patterns optional |
| `M` | machine only | optimize for chunk self-sufficiency, no cross-section anaphora, explicit recaps |
| `H+M` | both (the common case) | apply both sets of `../writing/patterns.md`; when they conflict, the `M>H` items win because a human tolerates redundancy a machine needs |

Different agents (a RAG retriever vs. a coding agent vs. a writing agent) are a **sub-categorization of `M`**, introduced only by a project that needs it — e.g. `reader: M[rag]`. Default projects use just `H | M | H+M`.

In the theory, *being a machine* is neither a role nor really a separate kind: it is the **recipient relation pushed to its limit** — maximum `distance` (it shares almost none of our tacit code, so everything must be made explicit) and a quiet, latent `power` (it acts on what we write). That is why the reader kind stays **orthogonal to role**, and why `reader: M` *tightens* the same `distance`/`power` costs the recipient section already governs rather than opening a new register. A machine can occupy the `user` or `contributor` function — it reads and it writes — but never `decider`: it does not set conventions (ADR-017/022).

## Frontmatter

`audience` holds the **roles** (a list); `reader` holds the **kind** (one flag). Both refine but never contradict `distance`/`power`, which stay the register controls (`../writing/patterns.md`, recipient section).

```yaml
audience: [contributor, decider]
reader: H+M
```

## Example — this project (apply this to our own docs)

The doc-system's own documents are written for the people *using the system to write docs* and the people *owning the conventions* — and they must also feed the future writing AI. So, as a default for files in this repo:

```yaml
audience: [contributor, decider]
reader: H+M
```

A `user` (someone who only ever *reads* a documented project, never authors) is not a primary audience of the meta-system itself — they meet the system only through the projects that adopt it.

## Example — a generic IT project

Here the three roles refine into familiar sub-roles, and the `reader` flag varies per document:

| Document (force) | `audience` | `reader` | Why |
|---|---|---|---|
| README (orient) | [user, contributor] | H+M | front door for everyone; also parsed by tools |
| API reference (describe) | [user, contributor] | H+M | consumed by integrators and by RAG |
| Getting-started (teach) | [user] | H | a human learner's experience |
| Runbook (instruct) | [contributor] | H | an on-call operator under pressure |
| Best-practices (recommend) | [contributor] | H+M | advises humans, guides coding agents |
| CONTRIBUTING (mandate) | [contributor] | H+M | rules humans follow, agents enforce |
| ADR (decide) | [decider, contributor] | H+M | future readers, including the writing AI |
| Audit dossier (prove) | [decider] | H | an examiner reads it, hostile and human |

Role sub-refinement for that project: `user` → end-user, API integrator; `contributor` → developer, reviewer, ops/SRE; `decider` → tech lead, product owner, auditor/compliance. The sub-roles are a project's own vocabulary; the three families above are the stable spine tooling can rely on.

## In short

Two axes: `audience` (roles — user, contributor, decider — aligned with the three doors, refinable per project) and `reader` (H | M | H+M, with agent sub-kinds only when needed). For this repo, default to `[contributor, decider]` / `H+M`. For a product project, vary both per document. Neither axis replaces `distance`/`power`; they answer *who*, those answer *how much to scaffold and armor*.
