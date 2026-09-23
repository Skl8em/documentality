---
title: "codifying — the tooling that enforces the theory, and why it is built this way"
force: orient
intention: formative
view: synchronic
provenance: { type: function, id: codifying }
constitutive: no
distance: initiated
audience: [contributor]
reader: H+M
status: draft
---

This shelf holds the **account of the tooling**: the scripts, the schema pipeline and the gate that make the theory's coordinates checkable, and the reasons each is built the way it is.
It is the last link of the chain [ADR-033](../phases/refoundation/phase-10-schema/operationalizing-function.md) drew, named and shelved by [ADR-035](../phases/refoundation/phase-12-codifying/codifying-function.md):

`theorising → operationalizing → structuring / writing → designing → codifying`

`operationalizing` says *what a coordinate is and why we reified it*.
`codifying` says *how a rule about it is enforced, and why the enforcement is built so*.
The test for filing a document is its subject: a coordinate or convention of the corpus goes to `operationalizing`; a mechanism that checks, generates or runs goes here.
It holds the account, not the code — `scripts/`, `schema/` and `docsys.yaml` stay where they are and belong to this function.

## Who this is for, and who it is not

The distance here is judged in **tooling engineering**, a field the theory shelves do not ask a reader to know.
That is why the shelf splits its readers in two ([`community-map.md`](../phases/refoundation/phase-12-codifying/community-map.md) derives it).

- **You ran the gate and it failed.**
  Do not read the fiches; read the failing line.
  Every line the gate prints names the file, the rule and, after `fix:`, the edit that clears it — that is the whole interaction, by design ([the audit](../phases/refoundation/phase-12-codifying/error-message-audit.md)).
  If a line is not enough, that is a defect in the message, worth reporting, not a reason to learn the engine.
- **You are about to change the tooling** — add a check, touch a validator, edit the schema.
  Read the fiche for what you are touching *first*.
  You are the `maintainer`: a `contributor` whose distance is judged in this field, initiated in it before acting, because a change here can corrupt the corpus silently rather than merely fail a lint.
  The fiches are written for you.
- **A machine running the gate** reads only its output, with no memory of any prior turn.
  It is served by the message contract above, not by prose.

## The apparatus, by where it is configured

The tooling separates by rate of change ([`engine-config-seam.md`](../phases/refoundation/phase-12-codifying/engine-config-seam.md) draws the line and lists what stayed on the wrong side of it).

| Home | What lives there | Read |
| --- | --- | --- |
| **engine** — `scripts/`, `tools/markdownlint/` | behaviour any project using this system would run unchanged | the fiches below |
| **methodology** — `schema/frontmatter-rules.yaml` | the frontmatter vocabulary, its enums, each optional field's reason | [the schema pipeline](schema-pipeline.md) |
| **instance** — `docsys.yaml` | where this repo keeps its schema, what is out of scope, its register's shape, which checks make its gate and in what order | [the gate](gate.md) |

## The fiches

- [`gate`](gate.md) — why every check is one property, what the order of the checks means, and what a green gate does not say.
- [`schema-pipeline`](schema-pipeline.md) — why the schema is authored in YAML and compiled to JSON, and how the two are kept from drifting.
- [`referential-integrity`](referential-integrity.md) — why a dangling `supersedes` is a hard error, why supersession must be symmetric, and the holes the check still has.

Still to write: the frontmatter linter's derivation of `register` and its closed vocabulary; the YAML reader and its two departures from `safe_load`; the content-hash fixity mechanism (`hash_seal.py`, `hash_check.py`); the identifier tools and the safe-rename core; the sentence-per-line markdownlint rule; and the `linkcheck` scope.
The environment the gate runs in is an `instruct` document, [`steering/environment.md`](../steering/environment.md), not a fiche.
