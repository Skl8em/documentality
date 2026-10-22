---
title: "Decision — the engine's YAML is the one vocabulary, read directly; the generated JSON retires"
id: 01M5G47VH8GVQ5KAQPX5WWTQ6D
slug: one-vocabulary-read-directly
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-14-adoption }
constitutive: yes
concerns: [codifying]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: 01M39G4VTECMXE57PBSCKYKW66
superseded-by: null
pin: docsys@fc58fd6663539ce8ea387f476f84fafd9c769511
hash: sha256:b963babe47fb4c6cb1722a00216c09bf59e7466f30dcae7824c6744625d40f72
---

## Status

accepted — 2026-10-21, recording a ruling the project owner took on 2026-10-20 ([Phase 14 rulings](rulings.md), *What precedes the switch, and what it retires*).
It supersedes [ADR-037](../../refoundation/phase-11-tooling-hardening/yaml-source-generated-json.md), which stays frozen and unedited apart from the link back to this record.
It clears the [ADR-032](../../refoundation/phase-10-schema/adr-tiering.md) test: it obliges anyone who edits the frontmatter vocabulary, or writes a program that reads it, from now on.

## Context and forces in play *(justify)*

ADR-037 kept two files: `schema/frontmatter-rules.yaml`, edited by hand, and `schema/frontmatter-rules.json`, generated from it for a program that would read the vocabulary without a YAML parser.
It kept the JSON as a hedge and said so in its honest limit: no such reader existed, the one reader of the JSON already needed a YAML parser, and the drift check that guarded the pair guarded a failure that only the pair made possible.

Three things have changed since.

**The vocabulary has moved to the engine.**
The `docsys` package ships `src/docsys/schema/frontmatter-rules.yaml` and reads it directly, through its strict loader, with no generated file.
This repository's gate switches to `docsys check`, so `scripts/` and the one reader of the JSON retire, and `schema/` would keep a second copy of a vocabulary that nothing here reads.

**The reader kept in reserve has not appeared.**
No program in either repository reads the JSON but the script that retires; the markdownlint custom rule is pure regex and reads no schema.
ADR-037's answer was to lapse if the design of the agent machinery closed with no non-Python reader; that design is not closed, but the proposal for other ecosystems ([`imagining/multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md)) has every package load the YAML unchanged, so the reader the JSON was kept for is not the one that design expects.

**Keeping two copies costs a check.**
While the gate still ran `scripts/`, the engine's test suite compared its vocabulary with this repository's on every verdict-bearing key; once the gate is `docsys check`, that comparison has nothing to compare, and keeping `schema/` would need a check of its own to stay true.

## Options considered

- **Keep `schema/` and its JSON beside the engine** — consequence: two copies of the vocabulary and a generated third, kept in step by checks, for a reader that does not exist.
- **Keep `schema/` as YAML only, the engine's copy generated from it** — consequence: the vocabulary is authored outside the package that ships it, and every release of the engine depends on this repository.
- **The engine's YAML is the one vocabulary, read directly** — consequence: one file, one loader, no drift check; a non-Python reader, if one appears, parses YAML or generates its own artefact.

## Decision

1. **The vocabulary is `src/docsys/schema/frontmatter-rules.yaml` in the engine**, edited by hand, comments allowed, shipped inside the package.
   It is the one copy; this repository and every adopter read it through the installed `docsys`.
2. **It is read directly**, through the engine's strict loader, by the engine's one reader of the vocabulary; no file is generated from it.
3. **`schema/` retires with `scripts/`**, both files with it, and the `schema-drift` check with them.
4. **A program in another language that needs the vocabulary** reads the YAML, or generates from it what it needs, in its own repository and at its own cost; the engine generates nothing for it in advance.

## Entail — what follows

- A change to the vocabulary is a change to the engine, made in its repository and paired there with its account, the engine's [vocabulary fiche](https://github.com/Skl8em/docsys/blob/fc58fd6663539ce8ea387f476f84fafd9c769511/docs/vocabulary.md); this repository's [`writing/frontmatter.md`](../../../writing/frontmatter.md) explains the fields to the people who fill them, and follows the engine's version.
- Every load of the vocabulary goes through the engine's strict loader, never a bare `safe_load`, which keeps ADR-037's one obligation that outlives its JSON: YAML 1.1 reads a bare `yes` as a boolean, and the vocabulary's own enumerations would break silently.
- The engine's test that compared its vocabulary with this repository's copy retires with the copy.
- A link from a frozen record to `schema/` is allowed by the link check with its reason, as the other links into `scripts/` are.

## Honest limit

**This settles the question before the design ADR-037 waited for.**
Its own lapse condition, the agent machinery designed with no non-Python reader, has not been met; this record retires the JSON on the observation that its reader has not appeared and that the proposal for other ecosystems reads YAML, which is a reading of a proposal, not of a design.

**ADR-037's argument runs both ways.**
It kept the JSON because collapsing later would cost what collapsing then did; by the same reasoning, generating a JSON later, when a reader that needs it exists, costs what keeping it costs now, and the reader can then say what it needs.

**The vocabulary is still not all of the rules.**
What the frontmatter check enforces is partly in the engine's code, as ADR-037 said of `scripts/`; one file makes the data single, not the rules.
