---
title: "Writing a document: the twelve forces and the readability patterns"
force: explain+mandate
verb: illuminate
perlocution: model
view: synchronic
audience: [developer, AI, writer]
status: stable
written-at: v2
valid-for: v2
---

This document says **how to write a given document**: first find what it *does* (its force), then follow the structure that force imposes, finally apply the writing patterns that lower cognitive load for a hurried human *and* an LLM. §0 gives the coordinate system a newcomer needs. Part I is the core: twelve stances, one per force. Part II tunes each stance to the recipient. Part III lists the cross-cutting writing patterns.

Governing principle: **the coordinate is an instruction, not a label**. Knowing a document *decides* — and telling yourself you write it to *justify* — already says where to put the effort. Misname the act and no polish recovers the wrong centre of gravity.

---

## §0. The coordinate system (read this first)

### Two strata: hard coordinates, one soft verb

A document has a set of **hard coordinates** — the formal categories a machine can read: its `force` (what illocutionary act it performs), its direction of fit (does it convey *knowing* or aim at *doing*), its `perlocution` (which change, if any, it works in the reader), and its recipient relation (`distance`, `power`). These coordinates span a space, and *not every cell is occupied*.

Over that space sits one **soft handle for the human**: the **verb**. The verb is a compressed summary of the occupied cell — one word that names where the centre of gravity lies and thereby selects the move structure. This is why the verb is not redundant with the force: the force is one coordinate, the verb is the label of the whole tuple. A decision is classified `decide` but written toward *justify*, because *justify* summarizes "declarative act + aimed at the reader's assent + toward a reader who does not yet agree" in a single actionable word.

### The verb diverges from the force for three reasons

When the verb differs from the force's name, it is for one of three reasons — worth knowing, because two of them earn a `verb` and one does not:

- **(a) Perlocutionary** — the force reshapes the reader, and the verb names *which* faculty. This is the strongest case (orient→*situate*, explain→*illuminate*, teach→*bring-along*, and the convince forces below).
- **(b) Illocutionary-internal** — the force is coarse and the verb picks a finer point on its own axis (decide→*justify* vs *ratify*; mandate→*require* vs *forbid*; describe→*specify* vs *define*).
- **(c) Recipient** — distance/power shift the centre of gravity. This does **not** earn a new verb, because it is already captured by `distance`/`power` (prove→*attest* is just prove × `power: holds`; commit→*charter* is a change of audience).

Rule of thumb: fill `verb` only for (a) and (b). For (c), set `distance`/`power` instead.

### Perlocution: a typology, not a boolean

The `perlocution` coordinate names the change the act works in the reader — the *perlocutionary* aspect in Austin's sense, parallel to and independent of the illocutionary `force`. Like the force repertoire, it is an open, saturated list, not a closed one. `none` means the reader is *served*, not changed.

| `perlocution` | What is reshaped | Verb | Host forces |
| --- | --- | --- | --- |
| `locate` | the reader's cognitive map (where am I) | situate | orient |
| `model` | the reader's conceptual model (why) | illuminate | explain |
| `enable` | the reader's competence (able to act) | bring-along | teach |
| `convince` | the reader's assent / belief | justify, demonstrate | decide, prove |
| `none` | — reader served, not changed | — | describe, account, instruct, recommend, mandate, commit, propose |

The `convince` row is the deliberate move that folds `prove` and `decide` into the perlocutionary family: a dossier convinces an examiner a claim holds; a decision record convinces a future reader the choice was reasoned. For these two, the perlocutionary aim is *instrumental* (the act's primary point is still evidential/declarative), whereas for orient/explain/teach it is *primary* — but both are real, so both are named.

### Know vs do vs govern: the newcomer's three doors

The direction of fit splits the whole repertoire into **savoir** (word-to-world: the document tells you how things *are*, and you end up *knowing*) and **savoir-faire** (world-to-word: the document aims at the world, and you end up *doing* or *able to do*). Crossing that with perlocution (is the reader *changed* or merely *served*) re-derives Diátaxis exactly — which is why this system carries **no separate `diataxis` field**; it would encode twice what `force` already fixes:

| | Savoir (knowing) | Savoir-faire (doing) |
| --- | --- | --- |
| **Changed** (perlocution ≠ none) | explain / orient | teach |
| **Served** (perlocution = none) | describe | instruct |

Diátaxis sees only this 2×2. The forces this theory *adds* — prove, account, mandate, commit, propose, decide, recommend — fall outside it because they do not address a *user of a system*; they regulate relationships or fix a record. So a reader arriving on a project meets **three doors**, not two:

- **Know (savoir)** — `orient` (where I am), `explain` (why), `describe` (the facts), and `account` / `prove` (what happened / what is established).
- **Do (savoir-faire)** — `teach` (learn by doing), `instruct` (execute a task), `recommend` (what you'd do well to do).
- **Govern & record** — `mandate` (rules), `decide` (decisions), `commit` (promises), `propose` (what is under deliberation); `prove` and `account` lean here too, as evidence and memory.

Within **do**, the transparency you want as a newcomer is a deontic gradient: `instruct` ("here is *how*") → `recommend` ("you *should*", non-binding) → `mandate` ("you *must*", binding). Reading a page, you can tell at once whether you are being shown a procedure, advised, or commanded.

### Finding the force: five questions before writing

1. **Know or do?** Which door — savoir (convey how things are) or savoir-faire (aim at action)? Then, within it, which force?
2. **What is the generative verb?** Hold it in mind; let it order the rest.
3. **What is the perlocution?** If `none`, judge success by correctness. If `locate`/`model`/`enable`/`convince`, organize by the reader's state and judge success by the reader's change.
4. **Who is the recipient — in distance and in power?** Distance sets the scaffolding, power sets the armor. Pay each cost where owed, nowhere else (Part II).
5. **What is the failure mode of this force?** Name it before starting, watch for drift toward the neighbouring stance.

---

## I. The twelve forces

Each entry gives the **generative verb**, the **stake**, the **move structure** (functions that must be present, not an imposed outline), the **failure mode**, the **perlocution**, and the **genres**.

### Assertive stances (word-to-world / savoir) — virtue: fidelity; temptation: sliding into one another

#### Describe — `describe` · perlocution `none`

- **Verb:** *specify.*
- **Stake:** completeness and neutrality. The reader must find any fact and trust the statement is exhaustive within its scope.
- **Moves:** delimit the scope → state the facts in a stable, predictable order → exemplify where a fact is ambiguous → mark the bounds of what is *not* covered.
- **Failure:** narrativizing. The moment a reference explains *why*, it has drifted to `explain`.
- **Genres:** reference manual, API docs, data dictionary, glossary, specification.

#### Orient — `orient` · perlocution `locate`

- **Verb:** *situate.*
- **Stake:** the reader never losing the thread. Every element answers one of four questions — *what is this, where am I, why does it concern me, where do I go next* — the rest is noise.
- **Moves:** name the whole in one line → locate the reader within it → state relevance to their likely purpose → route onward to the right next document.
- **Failure:** turning into a manual (`describe`) or a tutorial (`teach`). An orientation that seeks completeness has failed: its job is to hand off, not to hold.
- **Genres:** README, overview, landing page, annotated table of contents, "start here" page.

#### Explain — `explain` · perlocution `model`

- **Verb:** *illuminate.*
- **Stake:** the reader's mental model. Success = they understand *why* the thing is as it is and can reason about cases not covered.
- **Moves:** pose the question/tension they likely hold → build the model that resolves it, in conceptual not procedural order → connect the model to its consequences and limits → leave them able to extrapolate.
- **Failure:** degenerating into a reference list (losing the *why*) or into instructions (answering *how*).
- **Genres:** explanation document, design rationale, `ARCHITECTURE.md`, conceptual overview.

#### Prove — `prove` · perlocution `convince`

- **Verb:** *demonstrate.*
- **Stake:** that the evidence *covers* the claim and the demonstration is reproducible. Showing results without the method proves nothing to a reader who does not already trust you.
- **Moves:** state the claim precisely → declare the method → exhibit the evidence → establish coverage (sufficient for the claim, not merely consistent with it) → state the limits of what was shown.
- **Failure:** the gap between "consistent with" and "sufficient for" — where most proofs quietly fail.
- **Genres:** audit report, test report, validation dossier, compliance evidence.

#### Account — `account` · perlocution `none`

- **Verb:** *report against.*
- **Stake:** honest variance. An account is only worth reading if it compares what happened to what was expected; a list of activities with no baseline is not an account.
- **Moves:** restate the baseline/expectation → state what actually occurred → name the variance and its causes → state the consequence or next step.
- **Failure:** narrating activity instead of reporting against an expectation — the perennial "status-green" report. (Note: a *postmortem* drifts toward `explain`; when its centre of gravity is the *why* of a failure, write it under the verb *diagnose*.)
- **Genres:** status report, postmortem, changelog entry, retrospective.

### Directive and commissive stances (world-to-world / savoir-faire and govern) — they create obligation; temptation: vagueness

#### Instruct — `instruct` · perlocution `none`

- **Verb:** *walk through.*
- **Stake:** the reader's success at the task, assuming nothing. Every unstated precondition is a trap; every skipped step is a silent failure point.
- **Moves:** state the goal and preconditions → give the steps in strict executable order → provide the means to verify success (at the end, ideally at checkpoints) → handle the common failure.
- **Failure:** explaining instead of telling. An instruction that justifies each step has drifted to `explain`.
- **Genres:** how-to, runbook, procedure, `INSTALL.md`.

#### Teach — `teach` · perlocution `enable`

- **Verb:** *bring along.*
- **Stake:** the learner's experience, not the curriculum's coverage. A tutorial is judged by whether the learner ends able and confident.
- **Moves:** establish a bounded, safe context where success is guaranteed → have them *do* something real and immediately rewarding → graduate difficulty in small reliable increments → consolidate, naming what was learned, pointing beyond.
- **Failure:** collapsing into a how-to (treating the learner as someone who just wants steps) or a lecture (explaining at someone who wanted to act).
- **Genres:** tutorial, onboarding path, guided workshop, getting-started.

#### Recommend — `recommend` · perlocution `none`

- **Verb:** *advise.*
- **Stake:** honest, actionable advice that stays **non-binding**. The reader must be able to tell this is a *should*, not a *must*, and must know when it does not apply. It sits on the deontic gradient between `instruct` (neutral steps) and `mandate` (binding rule): *here is how* → *you should* → *you must*.
- **Moves:** state the recommendation plainly → fix when it applies and when it does not → give the tradeoff that makes it the better default, briefly → mark it explicitly overridable and say how to deviate.
- **Failure:** symmetric drift — hardening into a `mandate` (false obligation, modals creep to *must*) or dissolving into `explain` (advice with no actionable form).
- **Genres:** best-practices guide, guidelines, style guide (its non-binding parts), recommendations.

#### Mandate — `mandate` · perlocution `none`

- **Verb:** *require.*
- **Stake:** the unambiguous boundary between obligatory and recommended. A convention that leaves the reader unsure whether a rule is binding has failed at its one job.
- **Moves:** state the rule plainly → fix its scope (who, when, where it binds) → give the rationale, but briefly, lest it read as optional → state the consequence of non-compliance.
- **Failure:** softening into advice — into `recommend` or `explain`. The modals weaken from *must* to *should*, and the reader can no longer tell what is required.
- **Genres:** policy, naming/coding convention, standard, `CONTRIBUTING.md`.

#### Commit — `commit` · perlocution `none`

- **Verb:** *promise precisely.*
- **Stake:** the precision of what is promised and, equally, what is *not*. An unbounded promise is a liability; a commitment's value is as much in its limits as in its undertaking.
- **Moves:** define the scope of the undertaking → state the promise in measurable terms → state conditions, exclusions, limits → specify the remedy/escalation when unmet.
- **Failure:** ambiguity that creates unbounded exposure — the warm but unmeasurable promise nobody can say was kept.
- **Genres:** SLA, charter, contract, OKR, roadmap (as promise).

#### Propose — `propose` · perlocution `none`

- **Verb:** *argue.*
- **Stake:** the case, and the alternatives considered. A proposal that states a preference without arguing it against the alternatives is a request, not a proposal: it invites a yes/no, not a decision.
- **Moves:** establish the territory (the shared situation) → identify the problem/gap → build the case for the proposed course, treating alternatives fairly → make the explicit ask.
- **Failure:** asserting a preference as if obvious, skipping the alternatives — leaving the reader unable to *decide*, only to agree or refuse.
- **Genres:** RFC, requirements document, design proposal, PRD, pitch.

### Declarative stance (both directions)

#### Decide — `decide` · perlocution `convince`

- **Verb:** *justify.*
- **Stake:** the reasoning, not the verdict. The decision is one line; the whole value is the record of *why*, which a future reader — including you — will need when the context is forgotten. This is why it is a `convince` force: it is written to bring a reader who does not yet agree to accept the choice as reasoned.
- **Moves:** state the context and forces in play → lay out the options genuinely considered → record the decision → record the consequences accepted, including the unwelcome ones.
- **Failure:** recording the verdict and discarding the reasoning — the log that says *what* and is useless the moment anyone asks *why*.
- **Special property:** a decision is *dated-fixed*. It is not edited to reflect a later choice; a superseding decision is a *new* record. (When the centre of gravity is authorization rather than reasoning — a sign-off — write it under the verb *ratify*.)
- **Genres:** ADR, committee minutes, sign-off, resolution.

---

## II. How the recipient rewrites the stance

The twelve stances say *what* each act does. The same act, toward a different recipient, is **written differently** — along two independent dimensions.

**Distance rewrites the scaffolding.** Distance = how much code the reader shares with you. The less they share, the more the document must carry its own context: define its terms, state what peers would assume, explain its conventions. A proof among specialists exhibits only results; the same proof for a reader outside the field must make the method visible step by step. Ask: *how much of what I take for granted does this reader not share?*

**Power rewrites the armor.** Power = whether the reader can impose consequences on you. The more they have, the more the document must be defensible: self-contained, precise, free of loose phrasing. This is independent of distance. A note to your own manager travels no distance (shared code) yet carries high armor (they hold power). A spec for an engineer at another firm travels far yet needs little armor (they hold no power). Ask: *can this reader use my words against me, and is the document built to withstand that?*

The sharpest case is `prove` toward an authority (distance *and* power at maximum): expose the whole method *and* be airtight against hostile reading — hence the cost of audit dossiers. That cost is not optional diligence; it is the structure of `prove` rewritten by the two coordinates at their extreme.

**RULE.** Do not pay this cost everywhere. The "write every email as if for court" reflex over-arms and over-scaffolds routine communication into illegibility. Set scaffolding from `distance`, armor from `power`, keep short-lived documents light. (This is also why recipient variants — prove→*attest* — do not spawn new verbs: they are `distance`/`power`, already recorded.)

**The perlocutionary stances organize by the reader.** Where `perlocution ≠ none` (orient, explain, teach, and instrumentally prove/decide), success is invisible in the document — it lives in the changed reader. Write these from the reader's present state, not the subject's logical structure: the describer organizes by the shape of the subject, the explainer by the shape of the reader's likely confusion. Each needs a theory of the reader — that, not the subject matter, is its organizing principle.

---

## III. Writing patterns (human + LLM), cross-cutting every force

These patterns lower cognitive load whatever the document. Benefit legend: `H` human · `M` LLM · `H+M` both · `M>H` useful to both, decisive for the model.

### Organization and navigation

- **Semantic, intent-bearing titles** `H+M` — the title informs out of context. ✗ `Advanced configuration` ✓ `Configure the SQL connection timeout`.
- **Self-sufficient modularity** `H+M` *(decisive for RAG)* — each section is understandable without the whole document. ✗ "as seen in the previous section…" ✓ "the pipeline (described in `pipeline.md`) receives…".
- **Separation by type** `H+M` — the four know/do stances (explain, describe, teach, instruct) have incompatible structures; mixing them degrades all four. One force per file, declared in the frontmatter.
- **Progressive disclosure** `H+M` — show the minimum to move forward, make detail accessible without imposing it.
- **Information scent** `H+M` — every link/title/first sentence gives a reliable signal of what's found by following. ✗ a "More info" link ✓ "See the detailed format of the `Result` parameters".

### Cognitive load and density

- **Working-memory limit (~4 chunks)** `H` — beyond 4–5 simultaneous items, group them. ✗ 12 parameters at one level ✓ 3–4 groups of 3–4.
- **Eliminate extraneous load** `H+M` *(M sensitive to noise in context)* — any effort that doesn't serve comprehension goes. Jargon defined at first use, predictable structure.
- **Split-attention** `H+M` — don't force integrating two separate sources; annotate on the diagram, put text next to the element.
- **Coherence (exclude the irrelevant)** `H+M` — no anecdote in a technical reference; conceptual material goes in a separate `explain` document.
- **Signaling** `H+M` — highlight structure (headings, terminological keywords bolded sparingly); aids human memory and LLM segmentation.

### Style and clarity

- **Plain language** `H+M` — active voice, common words, few nominalizations. ✗ "the implementation of the verification of data conformity" ✓ "to check that the data conforms".
- **Linearly structured sentences** `H+M` *(M sensitive to syntactic ambiguity)* — minimize distance between dependent elements. ✗ "The returned value, if the flag is active and the connection was not closed by the timeout, is a Result object." ✓ "If the flag is active and the connection open, the function returns a `Result` object."
- **Strict terminological consistency** `M>H` — one term per concept, stick to it, document the domain's synonyms. ✗ `process`/`task`/`job` used interchangeably ✓ "a *process* (also called a *job* in the source docs) is…".
- **Fight the curse of knowledge** `H+M` — expand acronyms at first use, make presuppositions explicit at the head of a section.

### Examples and concreteness

- **Worked examples** `H+M` *(marked effect for M)* — a step-by-step worked example activates more robust schemas than an abstract definition.
- **Explicit counter-examples** `H+M` — a lone positive example creates an attractor; positive + negative creates the boundary. ✓ "Do not: `result.value` before checking `result.ok` — raises `UnboundError`."
- **Plurality and heterogeneity of examples** `M>H` — a single example implicitly fixes all its dimensions as constraints. Give 3 examples varying on the irrelevant dimensions.
- **Principle → example → principle framing** `M>H` — repeat the principle after the example to bring attention back to the abstraction.
- **Name the free dimensions** `M>H` — rather than "there are others", enumerate what may vary. ✓ "Format, register, and length are free; only the return structure is constrained."

### Referential clarity (LLM-specific)

- **Eliminate cross-section anaphora** `M>H` — "this value", "the module above" fall apart when a chunk is extracted alone. ✗ "this value must match the one defined above" ✓ "the value `timeout_ms` must match `DB_TIMEOUT` in `config.py`".
- **Explicit recap at start and end of section** `M>H` *(lost-in-the-middle)* — "This section explains X. Key points: A, B, C." … "In summary, X works via A and B."
- **Position of critical information** `M>H` — never in the middle of a long context; at the start/end, or in a short dedicated file.

### Code-specific

- **Self-sufficient first docstring paragraph** `H+M` — tools/LLMs often retrieve only it; first sentence = what the function does (input → output).
- **Document invariants and failure cases (Design by Contract)** `M>H` — ✗ `Returns: Result object` ✓ `Returns: Result. result.ok is False if [conditions]. Raises ValueError if [condition].`

*(Full academic references in the research source file `patterns-ecriture-documentation.md`. Web-verified ✓: Sweller 1988, Cowan 2001, Liu et al. 2024 "Lost in the Middle", Nielsen F-pattern, OASIS DITA 1.3, Procida Diátaxis, PEP 257, Anthropic multishot.)*

## In short

The hard coordinates (force, direction of fit, perlocution, distance, power) span a space; the soft `verb` names the occupied cell and picks the move structure. A newcomer routes by three doors — know, do, govern & record — and, within *do*, by the deontic gradient instruct → recommend → mandate. Before writing: find the force, hold its verb, read its perlocution (organize by the reader if not `none`), set scaffolding and armor from the recipient, name the failure mode. Then apply the cross-cutting patterns.
