---
title: "Architecture of <project>"
force: explain
verb: illuminate
perlocution: model
view: synchronic
provenance: { type: function, id: <function-id> }
distance: near
power: none
audience: [developer, architect, AI]
status: draft
---

<!--
TEMPLATE — force `explain` (verb: illuminate). See writing.md §I > Explain.
Stake: the reader's mental model — that they understand WHY it is so and can
reason about cases not covered.
Organize by the shape of the reader's likely confusion, NOT by the code's structure.
Failure: degenerating into a reference list (losing the why) or into instructions (the how).
When a structural choice is made, it becomes an ADR (decide, frozen); this state file
(synchronic) REFERENCES it and is updated afterward — never the reverse.
-->

## The question you're probably asking

<The tension/why the reader carries on arrival. State it explicitly.>

## The model

<Build the model that resolves the tension, in conceptual order. A diagram beats a paragraph;
annotate it in place (no separate legend at the bottom — split-attention).>

## Consequences and limits

<What this model implies, what it makes easy/hard, its bounds.>

## Decisions that shaped this architecture

<Links to the relevant ADRs. Don't rewrite their reasoning here: point.>

- [ADR-00X — …](decisions/ADR-00X.md)

## In short

<The model in 2–3 sentences, to anchor (end recap, useful to the LLM).>
