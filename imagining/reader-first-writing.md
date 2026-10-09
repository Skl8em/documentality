---
title: "Reader-first writing — tools against prose that narrates its own history"
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

A proposal for a class of defect and the tools to detect and prevent it, to be built up over time.
The casebook at the end grows with each example found.

## The defect

A document declared `view: synchronic` states what *is*: the current state, for the reader its frontmatter names.
A recurring failure fills such a document with what *happened*: the changes that produced the state, the rulings taken on the way, the corrections made.
The result reads as an `account` under an `orient` or `describe` label — a force drift the gate cannot see, because the gate reads the frontmatter and not the prose.

A newcomer cannot use that history: they never saw the previous state, so a sentence defined against it makes no sense to them.

The writing literature names the general pattern *writer-based prose*: text organised around the writer's own path to the content rather than the reader's need (Linda Flower, *College English*, 1979 [title and details: to verify]).

## Why it happens, especially with an agent writer

- **The writer starts from the diff.**
  An agent editing a document has the change in front of it, not the state; the change is what it describes.
- **The imagined reader is the person in the conversation.**
  The user watched the change happen, so history reads as context to them — but they are not the reader the document declares.
- **Accounting is a real obligation with no channel.**
  Reporting what changed is right in a reply or a commit message; with nowhere else to go, it lands in the document.
- **The corpus is the style guide.**
  An agent imitates the documents around it.
  A corpus whose synchronic documents narrate history teaches every new session to do the same, and a written rule loses to twenty examples.

## Tools, from the cheapest to the strongest

1. **A rule and a revision test**, in [`writing/rules.md`](../writing/rules.md).
   The test, per sentence: *would it still be true and useful if the document had always been written this way?*
   If understanding it requires the previous version, it belongs in the account.
   A reason is synchronic ("X, because Y"); an event is not ("X was changed after Z").
   The exception is a migration note, whose declared reader does hold the former state.
2. **Two outputs per edit.**
   Every edit to a synchronic document produces the *state*, which goes into the document, and the *account*, which goes into the commit message, the changelog or the reply to the user.
   The skill teaches this as one procedure, so the urge to account has its channel.
3. **The frontmatter as the brief.**
   Before writing, the agent reads the declared `force`, `audience` and `distance` as the statement of who arrives and what they came for; after writing, it reviews against the same fields.
4. **A cold-reader pass.**
   A subagent with no conversation history receives only the document and its declared audience, and reports every sentence it cannot make sense of, or that refers to something it cannot see.
   This is the cheapest available stand-in for a human cold reader, and it tests the document rather than its metadata.
5. **A force-conformance review.**
   The same kind of agent answers one question: does the prose perform the force the frontmatter declares?
   It catches this defect and its cousins — a `describe` page labelled `explain`, an `explain` that has drifted into instructions.
6. **A smell detector for temporal markers.**
   A warning, never an error, in synchronic documents: "now", "no longer", "used to", "previously", "since Phase", "was renamed", "ruled", a task identifier such as "T6(b)".
   It measures vocabulary, not stance, so it points a reviewer at a sentence and never counts as a verdict.
7. **Clean anchors and paired examples.**
   The synchronic documents an agent reads are rewritten to the rule, and the skill carries before/after pairs from the casebook below.
   Without this, the other tools erode.

## How we would know it works

A cold-reader pass on a cleaned page reports nothing it cannot place, and the project owner stops finding new cases in documents an agent has just written.
Neither is a measurement; both are observable.

## Casebook

Each case: where it was found, the sentence, and its rewrite as state.

### 1 — `imagining/README.md`, an `orient`

Found by the project owner, 2026-10-09.

> Phase II, which it used to park as a whole, left it when Phase I closed by ruling: the rush to MVP builds it ([ADR-042](…), [`../steering/roadmap.md`](…)).

Every clause is defined against a former state the reader never saw: what the shelf *used to* hold, what *left*, what *closed*.
As state:

> This shelf holds proposals: work the project intends but has not ruled on, one file each.
> Nothing here is enacted; a proposal leaves for the function that enacts it once it is ruled on.
