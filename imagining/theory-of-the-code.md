---
title: "The theory of the code — what documentation must carry for a project, after Naur"
force: propose
intention: suasive
view: diachronic
provenance: { type: function, id: imagining }
constitutive: no
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

A proposal, ruled on (see *Rulings*).
It answers finding 1a of the [external review](../steering/external-review/external-review.md) — the project has no written position on Naur — and refines what the product asks a project's documentation to carry.

## The gap

Everything the product teaches today is about *documents as acts*: which force a document performs, toward whom, for how long.
It says nothing about *what a project's documentation must be about*.
A project can satisfy every rule here — each file a well-formed `explain`, `describe` or `decide` — and still leave a newcomer, or an agent, without the one thing they need before changing the code: the theory the code embodies.

The project has built that theory for its own domain without naming it as such.
`schema/frontmatter-rules.yaml` is a closed lexicon — each term declared once, each carrying its reason — and a checker holds documents to it.
That is the pattern this proposal asks the product to teach for an adopter's *code*.

## A position on Naur

Naur's thesis (*Programming as Theory Building*, 1985) is that a program is a theory held by the people who built it, and that documentation cannot re-establish it [quotation wording: to verify against the original].
The thesis names three things the holder of a theory can do — the test of whether someone holds it [paraphrase; to verify]:

1. explain how the program maps onto the affairs of the world it serves;
2. justify why each part of the program is as it is;
3. respond constructively to a demand for modification.

**The position taken here: documentation does not carry the theory; it carries the theory's articulation, from which each reader rebuilds a theory of their own.**
Naur is right that the two differ and that the rebuilt theory can be wrong.
He is not an objection to documenting; he is the specification of what to document, and of how to tell when it failed.

An agent makes this sharper, not weaker.
Every agent session is a programmer who never held the theory and will not keep it: Naur's "revival from documentation" happens at the start of every session.
For an agent the articulation is the *only* channel — so its gaps show up directly, as modifications that break the theory.
That turns Naur from a threat to the founding wager into its test: if an agent given the articulation makes no fewer theory-breaking changes than one without it, the wager fails for that project.

## What the articulation contains

Each part answers one of Naur's three abilities, and each must be traceable to the code.

| Part | What it states | Grammar | Naur's ability | Maps to in code |
|---|---|---|---|---|
| **Concepts** | the entities the code cares about: one term each, a definition, and what the term is *not* | nouns | 1 — the world mapping | a type, a module, a table |
| **Relations** | how the entities act on and depend on each other | verbs | 1, 2 | a function, a method, an operator |
| **States and qualities** | the states an entity passes through and what each licenses | adjectives | 2 | an enum, a predicate, a flag |
| **Invariants** | what always holds, whatever changes | "always", "never" | 2 | a test, an assertion, a type constraint |
| **Grain** | why each part is as it is, and the changes the theory *refuses*, with their reason | "because", "not … because" | 3 — responding to modification | (refusals have no symbol; that is why they must be written) |
| **Limits** | where the theory stops holding, and what would make it wrong | "if … then abandon" | 3 | — |

The **grain** matters most for an agent, because an agent's default response to any request is to *add*.
A theory that only describes what exists cannot tell it which additions betray the design.

The maintainer's own `weft` spec already does all of this by hand, which is the evidence that this is what is wanted, not a theory imposed from outside:

- **concepts with contrast** — `SKIPPED` and `SUCCESS` both let downstream tasks proceed, "the distinction is reporting and idempotence";
- **a world mapping** — `AWAITING` is the human-validation step of the migration;
- **an invariant** — a task never hard-codes a path, it asks the `Context`;
- **grain** — "Resisting `|` for fallback, because fallback is a state-handler concern";
- **a limit** — past the 600–900-line core, fall back to `invoke`.

What the spec lacks is what this proposal adds: once there is code, the theory must leave the spec (a `propose`, frozen once decided) for a document that is maintained, and the code must be held to its terms.

## Code and theory, held together

The correspondence runs both ways, and a change to either is a change to both.

- **Code reflects the theory.**
  A public symbol uses the lexicon's term for its concept, and only that term (the writing rules' *one term per concept*, applied to identifiers).
  A public symbol that names no concept, or a concept with no symbol, is a finding — not always an error, since some concepts are deliberately symbol-less, but always a question.
- **The theory reflects the code.**
  A change that introduces, renames or removes a concept changes the lexicon in the same commit.
  This is the paired-change rule (ADR-039) pointed at an adopter's code: `mechanism` is the source tree, `understanding` is the theory documents.
  The engine already exists; only the configuration is new.
- **Naming is a decision.**
  Introducing a term into a project's language institutes it — a declaration in the speech-act sense, the act this product's theory calls constitutive.
  So an agent may *draft* a term, from the code or from a request, but the term binds only once a human rules on it, exactly as the agent drafts and the maintainer rules on ADRs here.

## Where it sits in the existing vocabulary

No new force is needed; this is the claim to test first, because adding one would be the costlier move.

- **The lexicon** — concepts, relations, states and invariants — is a `describe` (its genres already include *glossary* and *data dictionary*) marked `constitutive: yes`, which derives `register: govern`: the terms bind the code.
  It must be machine-readable, so a check can compare it with the code's symbols.
- **The grain and the limits** are an `explain` — the genre the product already calls *design rationale* or `ARCHITECTURE.md`.
- Both are `view: synchronic` under the function that builds the code, and kept current.
  A spec like `weft`'s is their diachronic ancestor, and stays frozen once its decisions are taken.

They are two documents (*Rulings*, 1).

## How we would know it works

The test belongs to the MVP's pilot on `weft`, at small scale and with no pretence of statistics.

- Give a fresh agent session, with no prior context, a short series of modification requests against `weft`, some of which the grain refuses (a fallback operator, a hard-coded path, a persisted execution state).
- Run each request once with the theory documents installed and once without.
- Record which changes break an invariant or the grain, and which ones the agent questions before making.

A handful of requests cannot prove the wager.
It can show where the articulation is too thin to carry, which is the finding we need.

## What this does not settle

- **The tacit residue.**
  Naur's point stands for what no one thought to write — the theory's unexamined assumptions.
  This proposal narrows that gap; it does not close it, and nothing documentary can.
- **Decay.**
  A maintained theory goes stale like any `synchronic` document; the paired-change rule catches a renamed concept, not a changed reason.
- **The symbol check's precision.**
  Matching identifiers to terms is language-specific and noisy (casing, plurals, compound names); how strict it can be without drowning the signal is an empirical question, settled on `weft` before it is generalised.

## Rulings

Ruled by the project owner on 2026-10-10.
The agent kit enacts them, writing the two genres into `writing/` and the kit's skill.

1. **Two documents**: a lexicon, read by agents looking terms up and by the check that compares it with the code's symbols, and an `explain` carrying the grain and the limits, read by whoever must build the model.
2. **The lexicon is `constitutive: yes`**: its terms bind the code.
3. **A recommendation, never a requirement**: the scaffold proposes both documents to a project with code; the gate does not require them, since a documentation-only project has no code to theorise.
