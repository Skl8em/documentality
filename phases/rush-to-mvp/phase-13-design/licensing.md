---
title: "Decision — licensing by kind of artefact: GPL for the engine, AGPL for services, CC0 for what adopters copy, CC BY-SA for the prose"
id: 01M4J3FMY0Q5RW8Y5DNVFZAMQK
slug: licensing
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-13-design }
constitutive: yes
concerns: [steering, codifying, writing]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:f245cbeb235335245de76aa236e6ad25d916c88e71b80b290223b65cd567898a
---

## Status

accepted — 2026-10-10, by the project owner.
It clears the [ADR-032](../../refoundation/phase-10-schema/adr-tiering.md) test: every new file a contributor adds falls under one of these licences, and `REUSE.toml` must say which.

## Context and forces in play *(justify)*

The repository carried the GPL-3.0 text alone, with no statement of "only" or "or later", and the project is about to put three different kinds of artefact in other people's hands.

**The engine is run, not linked.**
An adopter installs `docsys` as a development tool and runs it.
Running a program places no condition on the adopter's own code, so the GPL's copyleft binds only whoever distributes a modified engine; the LGPL's one concession, linking from proprietary programs, answers a use the engine does not have.

**A service escapes the GPL.**
The agent machinery points toward components that run as services — an MCP server, a hosted documentation agent.
Under the GPL, a modified version offered over a network owes its users nothing; the AGPL closes that.
Its cost is real: many organisations forbid AGPL software outright, even as an internal tool, which would slow adoption of the engine where the rush to MVP most needs it.

**What adopters copy becomes theirs.**
The templates, the agent kit's files and the configuration a new instance starts from are copied into an adopter's repository and edited there.
Under the GPL, a README written from the orient template could be argued to be a derivative work, carrying the licence into the adopter's documentation; the argument is legally uncertain, and the uncertainty alone deters.
GNU Bison met the same problem with the parser skeleton it copies into its output, and answered it with an exception.

**The format must stay free to implement.**
The schema and the conformance suite are the API every package honours ([`imagining/multi-ecosystem-distribution.md`](../../../imagining/multi-ecosystem-distribution.md)).
If anyone may implement it, an adopter's frontmatter never depends on this project's implementation.

**Prose is not code.**
The GPL fits text badly; CC BY-SA 4.0 is the copyleft written for it, and Creative Commons lists it as one-way compatible with GPLv3 [to verify].

## Options considered

- **GPL-3.0 for everything** — consequence: one licence, and copyleft that may reach adopters' own documents through the templates.
- **AGPL-3.0 for everything** — consequence: services covered, and the engine refused by organisations that ban the AGPL.
- **LGPL-3.0 for the engine** — consequence: weaker protection for a use (linking) the engine does not have.
- **A licence per kind of artefact** — consequence: the strongest fitting licence for each, at the cost of a per-file map that must be kept.

## Decision

1. **The engine's code** — the validators, the gate, the custom lint rule, the build and CI wiring, and the `docsys` package — is **GPL-3.0-or-later**.
2. **A component that runs as a service** — an MCP server, a hosted runner — is **AGPL-3.0-or-later**, decided when such a component is created.
3. **What an adopter copies into its own repository** — the force templates, the schema, the configuration files an instance starts from, the agent kit's files, the conformance suite — is **CC0-1.0**.
4. **The prose** — the theory, the guidance, the project's records — is **CC BY-SA 4.0**.
5. **The map is `REUSE.toml`**, following the [REUSE specification](https://reuse.software): a default for prose, then the exceptions; the licence texts are in `LICENSES/`, and `reuse lint` verifies that every file has one.
   The root `LICENSE` keeps the GPL text, which forges read to label the repository; the README states the whole scheme.

## Entail — what follows

- A contributor adding a file checks which annotation of `REUSE.toml` covers it, and adds or narrows one when a new kind of file appears; `steering/CONTRIBUTING.md` says so.
- The `docsys` repository starts with the same scheme: its code GPL, its schema, templates and conformance suite CC0, its prose CC BY-SA.
- `reuse lint` is not in the gate; whether it joins, in this repository or in what `docsys init` sets up for adopters, is decided with the adoption phase.

## Honest limit

**This is not legal advice.**
Whether a document written from a template is a derivative work is the least settled point, and CC0 is chosen to make the question moot rather than to answer it.

**Copyright in machine-written code is unsettled.**
Much of this repository was written with an AI agent; whether those parts are protected by copyright at all depends on the jurisdiction [to verify].
The licences apply to whatever copyright exists.

**Relicensing gets harder with each contributor.**
While the project owner is the only author, any of these choices can be changed; once others contribute, a change needs their consent.
