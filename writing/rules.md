---
title: "Writing rules (binding)"
force: mandate
verb: require
intention: state
view: synchronic
provenance: { type: function, id: writing }
constitutive: yes
audience: [user]
reader: H+M
status: stable
---

These rules are **binding** for documents written in this system.
Unlike [`patterns.md`](patterns.md), which you may relax with reason, breaking these breaks the system's guarantees (catalogue validity, chunk retrievability, honest records).
They apply to every file except ephemeral working notes.

## The rules

- You **must** give every document **one dominant force**, declared in the frontmatter.
  If two forces fit, the document is split, or one is dominant and the other subordinate inside it.
  Scope: all non-ephemeral files.
  Consequence: a file with a mixed or missing force does not enter the catalogue.

- You **must not** mix incompatible types on one page — a reference that explains, a tutorial that mandates.
  Each drift degrades both.
  Consequence: reviewers reject the file back to a split.

- You **must** keep **terminology strict**: one term per concept, and document the domain's synonyms once.
  (This is the single readability pattern promoted from recommendation to rule, because a machine reader — unlike an expert human — does not absorb silent variation.)
  Consequence: inconsistent terminology is a blocking review comment.

- You **must** make every section **self-sufficient** enough to be read as an isolated chunk: no `reader: M` or `H+M` document may rely on cross-section anaphora ("as above", "this value") to be understood.
  Consequence: RAG returns a broken chunk; treated as a defect.

- You **must** write **diachronic** documents (`view: diachronic` — decisions, changelog entries, proofs, decided proposals) as **frozen and dated**; never edit them to reflect a later state.
  A superseding document is a *new* record linking the old via `supersedes`.
  Consequence: a rewritten record is a loss of organizational memory and is reverted.

- You **must** set `audience` (roles) and, for anything a machine will read, `reader`.
  Consequence: without them the writing AI and RAG cannot route the document.

## Why these and not the patterns

A rule earns its place here only if breaking it silently corrupts something a reader or the machine relies on — the catalogue, a retrieved chunk, a frozen record, the meaning of a term.
Everything else that merely *helps* is a recommendation ([`patterns.md`](patterns.md)), overridable with judgment.
Keeping this list short is deliberate: a `mandate` that swells into advice stops being obeyed.
