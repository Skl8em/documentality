---
title: "The system lived — this repo, and a generic IT project"
force: explain
verb: illuminate
perlocution: model
view: synchronic
provenance: { type: function, id: doc-system }
audience: [contributor, decider]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

The best proof of the model is that this repository *is* an instance of it. This document reads our own tree as an example, then shows how a generic IT project would instantiate the same shape — so you can see the theory lived, not just described.

## This repository, read as an instance

The two top-level folders are the two activities; each is a **function** (permanent, synchronic), so nothing here is a frozen project record — the whole meta-system is maintained state. Within each activity, the forces do their own jobs:

```text
README.md              orient    — the front door (perlocution: locate)
tutorial.md            teach     — guided first-document on-ramp
write/
  README.md            orient
  concepts.md          explain   — the coordinate system (the why)
  choosing.md          instruct  — the five-question procedure
  patterns.md          recommend — readability defaults
  rules.md             mandate   — the binding writing rules
  frontmatter.md       describe  — the catalogue schema
  forces/<door>/<force>/
    README.md          explain   — the stance
    template.md        instruct  — a skeleton to fill
structure/
  concepts.md          explain   · setup.md   instruct
  defaults.md          recommend · rules.md   mandate
  audience.md          describe  — the audience model
  applied.md           explain   — this file
```

Notice what this demonstrates:

- **Self-similarity.** Each activity is documented by the same forces the system teaches — an `explain` for the why, an `instruct` for the how, a `recommend` for defaults, a `mandate` for rules. The old flat version failed here: it crammed all four into one `writing.md` (now in `_legacy/`), violating the "one force per file" rule it preached.
- **The three doors are the folder layout**, so `forces/` navigates by *what you are trying to do*, not an alphabetical twelve.
- **Frontmatter lives in `write/`**, because you fill it while writing — even though `provenance`/`view` source their meaning from `structure/`.
- **Default audience for our files:** `audience: [contributor, decider]`, `reader: H+M` — we serve the doc author, the convention owner, and the future writing AI (see [`audience.md`](audience.md)).

What we do *not* have here (because the meta-system is one maintained function): no `projects/` submodules, no frozen `decide`/`prove` records. Those appear the moment the system is applied to real, bounded work — as below.

## A generic IT project, read as an instance

Take a service with a public API, maintained by a small team, audited yearly. In-repo docs (the project's own provenance and local surface):

```text
README.md              orient    [user, contributor] / H+M
docs/
  architecture.md      explain   [contributor] / H+M       — references ADRs
  reference/api.md     describe  [user, contributor] / H+M — RAG-indexed
  guides/deploy.md     instruct  [contributor] / H         — on-call under pressure
  guidelines/style.md  recommend [contributor] / H+M       — guides coding agents too
  tutorials/quickstart teach     [user] / H
  decisions/ADR-*.md   decide    [decider, contributor] / H+M — frozen, per project
  CHANGELOG.md         account   [user, contributor] / H+M    — append-only
CONTRIBUTING.md        mandate   [contributor] / H+M
```

Then, if this service joins a **cross-project docs repo**, it is added under `projects/` as a **pinned submodule**, and a `functions/reporting/` page (synchronic, business-function axis) references its exact state via the pin. The yearly **audit dossier** (`prove`, `[decider]/H`, `retention: legal:7y`) lives in `archive/`, frozen. The audience roles refine into the project's vocabulary — `user` → end-user / API integrator, `contributor` → developer / reviewer / SRE, `decider` → tech lead / product owner / auditor — but the three families stay the spine tooling relies on.

## What the two instances share

Same twelve forces, same three doors, same seam between maintained state and frozen record, same two-axis audience. What differs is only which cells are occupied: the meta-system is a single function with no frozen records; the product project has projects, decisions, and evidence with real retention. That is the model working: *not every cell is populated, and the empty ones are as informative as the full ones.*
