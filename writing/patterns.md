---
title: "Readability patterns (human + LLM)"
force: recommend
verb: advise
perlocution: none
view: synchronic
provenance: { type: function, id: writing }
audience: [user]
reader: H+M
status: stable
written-at: v3
valid-for: v3
---

These are **recommendations, not rules** (the binding ones are in [`rules.md`](rules.md)). They lower cognitive load whatever the force. They apply most strongly when `reader: H+M`; a pure-`H` document may relax the `M>H` items, a pure-`M` document may relax the human-scan ones. Override any of them knowingly when a document has a good reason.

Benefit legend: `H` human · `M` LLM · `H+M` both · `M>H` useful to both, decisive for the model.

## Organization and navigation
- **Semantic, intent-bearing titles** `H+M` — the title informs out of context. ✗ `Advanced configuration` ✓ `Configure the SQL connection timeout`.
- **Self-sufficient modularity** `H+M` *(decisive for RAG)* — each section understandable without the whole document. ✗ "as seen above…" ✓ "the pipeline (described in `pipeline.md`) receives…".
- **Progressive disclosure** `H+M` — show the minimum to move forward, make detail reachable without imposing it.
- **Information scent** `H+M` — every link/title/first sentence signals what following it yields. ✗ "More info" ✓ "See the detailed format of the `Result` parameters".

## Cognitive load and density
- **Working-memory limit (~4 chunks)** `H` — beyond 4–5 simultaneous items, group them.
- **Eliminate extraneous load** `H+M` — jargon defined at first use, predictable structure; drop anything that doesn't serve comprehension.
- **Split-attention** `H+M` — annotate on the diagram, put text beside the element; don't force integrating two separate sources.
- **Coherence** `H+M` — no anecdote in a reference; conceptual material goes in a separate `explain`.
- **Signaling** `H+M` — highlight structure (headings, terminological keywords bolded sparingly).

## Style and clarity
- **Plain language** `H+M` — active voice, common words, few nominalizations.
- **Linear sentences** `H+M` — minimize distance between dependent elements. ✗ "The returned value, if the flag is active and the connection was not closed by the timeout, is a Result." ✓ "If the flag is active and the connection open, the function returns a `Result`."
- **Fight the curse of knowledge** `H+M` — expand acronyms at first use, make presuppositions explicit at the head of a section.

## Examples and concreteness
- **Worked examples** `H+M` *(marked for M)* — a step-by-step example beats an abstract definition.
- **Explicit counter-examples** `H+M` — positive + negative creates the boundary. ✓ "Do not: `result.value` before checking `result.ok` — raises `UnboundError`."
- **Plural, heterogeneous examples** `M>H` — a single example fixes all its dimensions as constraints; give 3 varying on the free ones.
- **Name the free dimensions** `M>H` — "format, register, and length are free; only the return structure is constrained."

## Referential clarity (LLM-specific)
- **No cross-section anaphora** `M>H` — "this value", "the module above" break when a chunk is extracted alone. Name the referent.
- **Recap at start and end of section** `M>H` *(lost-in-the-middle)*.
- **Critical info at start/end, never mid-context** `M>H`.

## Code-specific
- **Self-sufficient first docstring paragraph** `H+M` — first sentence = input → output.
- **Document invariants and failure cases (Design by Contract)** `M>H` — state `Raises` / when `result.ok is False`.

*(The one pattern promoted to a binding rule — strict terminological consistency — lives in [`rules.md`](rules.md). Full academic references in `../theorising/patterns-ecriture-documentation.md`, web-verified set: Sweller 1988, Cowan 2001, Liu et al. 2024 "Lost in the Middle", Nielsen F-pattern, OASIS DITA 1.3, Procida Diátaxis, PEP 257, Anthropic multishot.)*

## Overriding

These are defaults. A `reader: H` runbook may drop the recaps; a poster-sized `orient` may ignore working-memory grouping. Deviate when the document's force and audience justify it — and, if the deviation is systematic, record it in a project `recommend` doc so it is a shared default rather than a one-off.
