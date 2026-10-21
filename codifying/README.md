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

This shelf holds the **account of the tooling**: the engine this repository runs, its configuration here and the gate that make the theory's coordinates checkable, and the reasons each is built the way it is.
It is the last link of the chain [ADR-033](../phases/refoundation/phase-10-schema/operationalizing-function.md) drew, named and shelved by [ADR-035](../phases/refoundation/phase-12-codifying/codifying-function.md):

`theorising → operationalizing → structuring / writing → designing → codifying`

`operationalizing` says *what a coordinate is and why we reified it*.
`codifying` says *how a rule about it is enforced, and why the enforcement is built so*.
The test for filing a document is its subject: a coordinate or convention of the corpus goes to `operationalizing`; a mechanism that checks, generates or runs goes here.
It holds the account, not the code — `docsys.yaml` and `tools/` stay where they are and belong to this function, and the engine's code is in its own repository, mounted here at `docsys/`.

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
| **engine** — [`docsys`](https://github.com/Skl8em/docsys), mounted at `docsys/` | the checks, the commands and the markdownlint rule: behaviour any project using this system runs unchanged | the engine's fiches below |
| **methodology** — the engine's `src/docsys/schema/frontmatter-rules.yaml` | the frontmatter vocabulary, its enums, each optional field's reason | [the vocabulary fiche](https://github.com/Skl8em/docsys/blob/main/docs/vocabulary.md) |
| **instance** — `docsys.yaml`, and `tools/` | what is out of scope, its register's shape, where its phase ledger is, where the paired-change rule bites, which tools run after the checks; this repository's own checks | [the gate](gate.md) |

## The fiches

- [`gate`](gate.md) — why every check is one property, what this repository configures and runs, and what a green gate does not say.

For a project that uses the engine, [`docsys`](https://github.com/Skl8em/docsys):

- [`docsys-configuration`](docsys-configuration.md) — every key of `docsys.yaml`, what it means, and when a value is refused.
- [`docsys-commands`](docsys-commands.md) — every command of `docsys`: `check`, `report`, and the four that write for the author (`id`, `seal`, `rename`, `slugify`), with their options and exit codes.

How the engine works inside is explained with it, in its `docs/` folder, for the engine's maintainer:

- [`runner`](https://github.com/Skl8em/docsys/blob/main/docs/runner.md) — why every check runs, what makes a run fail, how the tools run, and how a rule's severity is set.
- [`links`](https://github.com/Skl8em/docsys/blob/main/docs/links.md) — what the link check resolves, and why a dead link is allowed only with its reason.

- [`referential-integrity`](https://github.com/Skl8em/docsys/blob/main/docs/referential-integrity.md) — why a dangling `supersedes` is an error, why supersession must be symmetric, and what the ULID check does not establish.
- [`paired-change`](https://github.com/Skl8em/docsys/blob/main/docs/paired-change.md) — why the unit is the commit, what needs no account, where the rule fails rather than warns, and what it does not establish.
- [`phase-state`](https://github.com/Skl8em/docsys/blob/main/docs/phase-state.md) — why the current phase is declared once in a ledger, what the ledger and phase-state checks verify against it, and what they do not establish.
- [`vocabulary`](https://github.com/Skl8em/docsys/blob/main/docs/vocabulary.md) — why the vocabulary is YAML with a reason per field, why it is never loaded through a bare `safe_load`, what the frontmatter check knows beyond it, and which statuses close a record.
- [`author-tools`](https://github.com/Skl8em/docsys/blob/main/docs/author-tools.md) — why the author's commands write what the checks verify, and where each refuses.

Still to write, in `docsys`'s `docs/`: the fixity check, and the sentence-per-line markdownlint rule.
The environment the gate runs in is an `instruct` document, [`steering/environment.md`](../steering/environment.md), not a fiche.
