# A Rhetoric of Organizational Genres
## From the inscribed act to the act of writing

*A companion to* The Inscribed Act: A Coordinate Theory of the Organizational Document

---

## Preface: the generative turn

The coordinate theory of the organizational document tells you *where* a document sits — what it does (its **illocutionary force**), what it seeks in the reader (its **perlocutionary intention**: to form, to persuade, or, at the floor no document escapes, simply to posit a world and silence the rest), and toward whom (the recipient relation of **distance** and a graded **power**). Knowing where a document sits is useful for placing it. It is not, by itself, useful for a writer.

This companion takes the step from placing to composing. Its premise is a claim made in passing by the parent theory and elevated here to a working principle:

> A document's coordinate is not a label applied after writing. It is an instruction issued before it. To know what a document is doing is to know what matters in it, what its centre of gravity is, and therefore how to write it.

The evidence is mundane and convincing. Asked to write the front page of a software project, a competent author who believes the task is to **describe** the project will produce a flat inventory of features. Told instead that the task is to **orient** the reader — *where am I, what is this, why should I care, where do I go next* — the same author produces something that works. Nothing changed but the verb. The verb did the work, because it pointed at the centre of gravity, and everything else arranged itself around that point.

**Three registers, not eleven names.** The parent's stances are many, and a list of eleven is a list no one holds in mind: the research on working memory is consistent that we manage three or four groups, not a dozen items. So this companion is organized first by the three registers of what an act does — **know** (make words answer to the world), **do** (ask the world to be made to answer to the words), and **govern** (institute a fact by the authority of the record). The finer stances live inside those three, to be consulted, not memorized. The registers are the mental model; the stances are the reference behind it.

**A stance is not a primitive.** Several of the finer stances — explain, orient, prove, justify — are recognized *conjunctions* of a register with a perlocutionary intention, reified into a genre because their situation recurs. This companion treats them as writer's stances all the same, because a writer composes toward a recognized whole and not toward an axis; but nothing here claims they are atoms, and new ones will appear as old ones split.

**Two boundaries.** This is an *open* repertoire, saturated not closed; its value is not the completeness of the list but the habit of asking, before writing anything, *what is this document trying to do, in which register, and toward whom* — and letting the answer set the form. And this companion governs the **macro-structure** of a document: which functional moves it needs and in what order. The surface craft that makes any move legible — plain language, sections that stand alone, worked examples, one term per concept, resilience to being read out of context by a hurried human or a retrieving machine — has its own empirical literature and its own reference (§VII), to which this defers rather than repeating it.

---

## How to read each entry

Each stance is presented as a writer's stance, with five elements:

- **The generative verb** — the word that, held in mind while writing, points at the centre of gravity. Often not the classificatory name. A decision record is placed under *decide*; it is *written* under **justify**, because justification is what matters in it.
- **What is at stake** — the one thing that, if gotten wrong, makes the document fail regardless of how polished it is.
- **The move structure** — the ordered functional units that realize the act. Moves are not headings; a single paragraph may carry several, and good documents often fuse them. They are a checklist of *functions that must be present*, not a mandatory outline.
- **The failure mode** — the characteristic way the document collapses, usually by drifting into a neighbouring stance.
- **Genres** — the recognizable document types that instantiate the stance.

Where a stance is marked *(formative)* or *(suasive)*, it intends a change in the reader beyond mere correctness; the two cross-cutting sections after the stances — §IV on the recipient, §V on those intended changes — treat what that demands.

---

## I. Knowing — the assertive register (word-to-world)

To **know** is to make words answer to the world. These stances represent what is the case; their shared virtue is fidelity, and their shared temptation is to slide into one another, because they all traffic in true statements and differ only in what the truth is *for*. None of them is neutral: a reference poses the world it describes as *the* world and makes the undescribed invisible — a power the writer holds and answers for, taken up in §V.

### Describe

- **Generative verb:** *specify.*
- **At stake:** completeness within scope — and the honesty of that scope, since what a reference leaves out ceases to exist for its reader. The reader must be able to find any fact and trust that what is stated is exhaustive within its declared bounds.
- **Move structure:** delimit the scope → state the facts in a stable, predictable order → exemplify where a fact is ambiguous → mark the boundaries of what is *not* covered.
- **Failure mode:** narrativizing. The moment a reference starts explaining *why*, it has drifted into *explain* and stopped being reliable as a lookup surface. Description does not argue and does not teach; it states.
- **Genres:** reference manual, API documentation, data dictionary, glossary, specification.

### Orient *(formative)*

- **Generative verb:** *situate.*
- **At stake:** the reader never losing the thread. Every element must answer one of four questions — *what is this, where am I, why does it concern me, where do I go next* — and anything that answers none of them is noise.
- **Move structure:** name the whole in one line → locate the reader within it → state the relevance to the reader's likely purpose → route onward to the appropriate next document.
- **Failure mode:** turning into a manual (drifting to *describe*) or a tutorial (drifting to *teach*). An orientation that tries to be complete has failed; its job is to hand off, not to hold.
- **Genres:** README, project overview, landing page, annotated table of contents, "start here" page.

### Explain *(formative)*

- **Generative verb:** *illuminate.*
- **At stake:** the reader's mental model. Success is not that the reader can recite facts but that they now understand *why* the thing is as it is and could reason about cases not covered.
- **Move structure:** pose the question or tension the reader is likely to hold → build the model that resolves it, in conceptual not procedural order → connect the model to its consequences and limits → leave the reader able to extrapolate.
- **Failure mode:** degenerating into a reference list (losing the *why*) or into instructions (answering *how* instead of *why*). Explanation is the only assertive stance organized around understanding rather than retrieval.
- **Genres:** explanation / discussion document, design rationale, `ARCHITECTURE.md`, conceptual overview, the "why" sections of good documentation.

### Prove *(suasive)*

- **Generative verb:** *demonstrate.*
- **At stake:** that the evidence actually covers the claim, and that the demonstration can be reproduced. A proof that shows results without exposing how they were obtained proves nothing to a reader who does not already trust the author.
- **Move structure:** state the claim precisely → declare the method → exhibit the evidence → establish coverage (show the evidence is sufficient for the claim, not merely consistent with it) → state the limits of what was shown.
- **Failure mode:** showing results without method, or exhibiting evidence whose coverage of the claim is assumed rather than demonstrated. The gap between "consistent with" and "sufficient for" is where most proofs quietly fail.
- **Genres:** audit report, test report, validation dossier, compliance evidence, verification record.

### Account

- **Generative verb:** *report against.*
- **At stake:** honest variance. An account is only worth reading if it compares what happened to what was expected; a list of activities with no baseline is not an account, it is noise dressed as a report.
- **Move structure:** restate the baseline or expectation → state what actually occurred → name the variance and its causes → state the consequence or next step.
- **Failure mode:** narrating activity instead of reporting against an expectation — the perennial "status-green" report that lists effort and hides the gap between plan and reality.
- **Genres:** status report, postmortem / incident review, changelog entry, retrospective, progress update.

---

## II. Doing — the directive and commissive register (world-to-word)

To **do** is to ask the world to be made to match the words. These stances create obligation — on the reader, on the writer, or on both — and their shared temptation is vagueness, because precise obligation is uncomfortable to write. Between the stance that only shows the way (*instruct*) and the one that binds (*mandate*) lies a third, advisory one — **recommend**: it urges a preferred way *without* obligation, *should* rather than *must*, as a style guide or a coding guideline does. The parent treats it as a worked example of how the repertoire extends; it is named here so the register reads whole.

### Instruct

- **Generative verb:** *walk through.*
- **At stake:** the reader's success at the task, assuming nothing. Every precondition that is not stated is a trap; every step that is skipped is a place the reader will fail silently.
- **Move structure:** state the goal and the preconditions → give the steps in strict executable order → provide the means to verify success at the end (and ideally at checkpoints) → handle the common failure.
- **Failure mode:** explaining instead of telling. An instruction that pauses to justify each step has drifted toward *explain* and has lost the reader who only wants to get the thing done.
- **Genres:** how-to guide, runbook, procedure, `INSTALL.md`, operating instruction.

### Teach *(formative)*

- **Generative verb:** *bring along.*
- **At stake:** the learner's experience, not the curriculum's coverage. A tutorial is judged by whether the learner ends able and confident, not by whether it mentioned everything. The learner's success at each step is the writer's only responsibility.
- **Move structure:** establish a safe, bounded context where success is guaranteed → have the learner *do* something real and immediately rewarding → graduate the difficulty in small reliable increments → consolidate, naming what was learned and pointing beyond.
- **Failure mode:** collapsing into a how-to (treating the learner as someone who already wants only the steps) or into a lecture (explaining at a learner who wanted to act). Teaching is the directive stance that is also formative: it changes the reader's competence, which is why coverage is the wrong measure.
- **Genres:** tutorial, onboarding path, guided workshop, getting-started experience.

### Mandate

- **Generative verb:** *require.*
- **At stake:** the unambiguous boundary between what is obligatory and what is merely recommended. A convention that leaves the reader unsure whether a rule is binding has failed at the one thing it exists to do.
- **Move structure:** state the rule plainly → fix its scope and applicability (who, when, where it binds) → give the rationale, but briefly, lest it read as optional → state the consequence of non-compliance.
- **Failure mode:** softening into advice. The rationale grows, the modal verbs weaken from *must* to *should* to *might consider*, and the reader can no longer tell what is required. Mandate that is too gentle becomes *explain* with a moral. (This is the stance that leans toward *govern*: to institute a norm is nearly to declare one.)
- **Genres:** policy, naming or coding convention, standard, `CONTRIBUTING.md`, directive.

### Commit

- **Generative verb:** *promise precisely.*
- **At stake:** the precision of what is promised and, equally, what is *not*. An unbounded promise is a liability; the value of a commitment is as much in its limits as in its undertaking.
- **Move structure:** define the scope of the undertaking → state the promise in measurable terms → state the conditions, exclusions, and limits → specify the remedy or escalation when the promise is not met.
- **Failure mode:** ambiguity that creates unbounded exposure — the promise whose terms are warm but unmeasurable, so that no one can say whether it was kept. A commitment that cannot be falsified is not a commitment.
- **Genres:** service-level agreement, charter, contract, objective with key results, public roadmap (as promise).

### Propose *(suasive)*

- **Generative verb:** *argue.*
- **At stake:** the case, and the alternatives considered. A proposal that states a preference without arguing for it against the alternatives is a request, not a proposal, and invites a yes/no rather than a decision.
- **Move structure:** establish the territory (the shared situation) → identify the problem or gap → build the case for the proposed course, treating the alternatives fairly → make the explicit ask of the reader.
- **Failure mode:** asserting a preference as though it were obvious, skipping the alternatives — which leaves the reader unable to *decide*, only to *agree or refuse*. The move that distinguishes a proposal from a demand is the honest treatment of what was rejected.
- **Genres:** RFC, requirements document, design proposal, product requirements document, pitch.

---

## III. Governing — the declarative register (both directions)

To **govern** is to institute a fact by the authority of the record: the act changes reality by being issued. In the organizational world these are the decisions, sign-offs, and resolutions — the acts that the archival system must later keep, and the same *govern* that names the archive's half of *The Documentary System*: what is governed here is what is kept there. It is a marked register, self-guaranteeing, and — for now — thinly populated.

### Decide *(suasive: justify + entail)*

- **Generative verbs:** *justify* and *entail.* A decision has two faces. **Justify** records why it was right against the alternatives — its backward face, written to be read by someone who does not yet agree. **Entail** unrolls what it now commits — the consequences, constraints, and downstream obligations it sets in motion — its forward face, which reaches into the genre system and engenders the mandates and tasks that follow. A record that justifies but does not entail leaves the reader knowing *why* but not *what now*.
- **At stake:** the reasoning and what follows from it, not the verdict. The decision itself is a single line; the value of the document is the record of *why* (so a future reader — including the author — can reopen it once the context is forgotten) and of *what it now commits* (so they can trace what depends on it).
- **Move structure:** state the context and the forces in play → lay out the options that were genuinely considered → record the decision → **entail** its consequences: unroll what it now requires and forecloses, including the unwelcome, and the downstream acts it engenders.
- **Failure mode:** recording the verdict and discarding the reasoning — the decision log that says *what* was chosen and is therefore useless the moment anyone asks *why*. A decision record without its rejected options is an assertion, not a justification.
- **Special property:** a decision is *dated-fixed* by nature. It is the record of a moment of choice and must not be edited to reflect a later one; a superseding decision is a new record. To rewrite it is to erase the organization's memory of how it once reasoned. (This is the diachronic pole of the state–change seam that *The Documentary System* develops.)
- **Genres:** architecture decision record, committee minutes, sign-off, formal approval, resolution.

---

## IV. How the recipient rewrites the stance

The stances above describe *what* each act does. But the same act, performed toward a different recipient, is *written differently* — and the recipient relation rewrites it along two dimensions, with a third reader now joining the human ones.

**Distance rewrites the scaffolding.** Distance is how much of the writer's discourse community the reader shares — how much code is common. The smaller the shared code, the more the document must carry its own context: define its terms, state what peers would assume, explain the conventions it relies on. A proof among specialists may exhibit only its results, because the method is common ground; the same proof for a reader outside the field must make the method visible step by step. Every stance has a "native" amount of scaffolding for its home community and must add more as it travels outward. The writer's question is: *how much of what I take for granted does this reader not share?*

**Power rewrites the armor.** Power is whether, and how far, the reader can impose consequences on the writer — a graded, many-formed relation, not a switch. The greater that power, the more the document must be defensible: self-contained, precise, free of the loose phrasing that is harmless among peers and dangerous before an authority. This is independent of distance. A note to one's own manager travels almost no distance — the code is fully shared — yet carries high armor, because the manager holds power. A specification for an engineer at another firm travels far in distance yet needs little armor, because that engineer holds none. Between a peer, a manager, an outside authority, there are as many settings as there are shapes of power. The writer's question is: *what can this reader do with my words, and is the document built to withstand it?*

**A third reader: the machine.** Increasingly a document's reader is not a person but a model — an LLM retrieving a fragment, a generator completing from a docstring. Its distance is peculiar and extreme: it shares none of the writer's tacit code, cannot ask, and often sees a section shorn of the document around it. It therefore demands the scaffolding of maximum distance made literal — no reference that reaches across sections ("as seen above"), one term per concept, each section legible alone, the critical fact never buried in the middle of a long context. And it holds a quiet power, because what it misreads it reproduces at scale. This is not a new axis; it is the recipient relation pushed to its limit — a reader who never shared the code and never will. The concrete patterns it calls for are worked out in the surface-craft reference (§VII).

**The sharpest case** remains the proof addressed to an authority — *prove* at maximum distance and maximum power at once. It must expose its entire method (distance) *and* be airtight against hostile reading (power), which is why evidential documents for auditors or courts are the most laborious writing an organization produces. The labor is not optional diligence; it is the move structure of *prove* rewritten by the two coordinates at their extreme.

A corollary, carried from the parent theory: do not pay this cost everywhere. Writing every document as though its reader held power and shared no code — the "write every email as if for court" reflex — over-armors and over-scaffolds routine communication into illegibility. The recipient relation tells you where the cost is owed and, just as importantly, where it is not.

---

## V. What the formative and suasive stances ask that mere serving does not

Above the floor that every inscription carries — the bare positing of a world, and the silencing of what it omits (§I) — a stance may *intend* a further change in the reader, and two such intentions matter enough to reshape how the document is written.

The **formative** stances — orient, explain, teach — aim to change what the reader *knows or can do*: a map, a model, a competence. The **suasive** stances — prove, propose, and decide written as *justify* — aim to change what the reader *believes or will assent to*. What unites them, and separates them from the merely serving stances (describe, instruct, account, commit, mandate), is that their success is not visible in the document. A reference succeeds when it is *correct*; but an explanation can be correct and illuminate nothing, a proof complete and convince no one, a proposal accurate and move no one to decide. The formative and suasive stances succeed only when the *reader* is changed, and the reader's change is not on the page.

The practical consequence is that both must be written from the reader's present state, not the subject's logical structure. The describer organizes by the shape of the subject; the explainer must organize by the shape of the reader's likely confusion, the prover by the shape of the reader's likely doubt, the proposer by the shape of the alternatives the reader would weigh. Each requires a theory of the reader — of what they do not yet understand, or do not yet accept — and that theory, not the subject matter, is the organizing principle. It is why these are the stances most often flattened into their serving neighbours: an explanation written as a reference, a proof as a data dump, a proposal as a bare preference — each the intended act reduced to its informational shadow, correct in content and inert in effect.

A word on the floor, because "serving" is not innocence. Even the stances that intend no uptake beyond correctness still pose a world and silence what they leave out; the reference's choice of scope, the runbook's tacit *this is simply how it is done*, carry the writer's power whether or not the writer notices it. The serving stances are not exempt from responsibility — only from needing a theory of the reader's *change*. Choosing what a reference contains is choosing what, for its reader, exists.

---

## VI. Using the rhetoric

In practice the rhetoric is a short interrogation to run before writing anything.

1. **Which register — know, do, or govern?** Place the act in one of the three first. This is the coarse, reliable cut, and it alone prevents the common disasters: a decision written as a description, a mandate written as an explanation, a proof written as an account.
2. **Which stance, and what is its generative verb?** Within the register, find the stance and the verb that names its centre of gravity — *specify, situate, illuminate, demonstrate, argue, justify* — and hold it in mind. Let it subordinate everything else.
3. **One act, or several?** If the document carries more than one, choose between *subordinating* and *splitting*. While it is small, keep the dominant act and subordinate the rest — a README that orients and also instructs is an orientation with an instruction inside it, not a centre­less hybrid. As it grows and the tension becomes unmanageable, split: first by register and force, then, within a force, by intention (the reference pulled apart from the rationale). Cut only along principled seams.
4. **Is it formative or suasive?** If so, organize by the reader's state — their confusion or their doubt — and judge success by the reader's change, not the document's correctness. If it merely serves, judge by correctness — but remember the floor: what you leave out will not exist for the reader.
5. **Who is the recipient — in distance and in power, human or machine?** Set the scaffolding from the distance, the armor from the power, and pay each cost where it is owed and nowhere else.
6. **What is the failure mode?** Name the neighbouring stance this one drifts toward, and watch for the drift.

This is not a template. It is the set of questions a template would have to answer, and a writer who carries the questions can compose without one — which is the point. Templates standardize the output; the rhetoric trains the judgment that produces the output, and judgment travels to the cases no template anticipated.

---

## VII. Beneath the stance: the surface craft

Everything above concerns the *macro-structure* of a document — which functional moves it needs, in what order, toward whom. Beneath it lies a second layer, largely independent of the stance: the sentence-level and page-level craft that makes any move land — plain language and linear syntax, sections that stand alone, worked examples and explicit counter-examples, one term per concept, information placed where a scanning eye or a retrieving model will actually find it. That craft has its own empirical base — cognitive load and working-memory limits, multimedia-learning principles, information foraging, and the observed behaviour of language models on long contexts — and its own reference, the surface-craft companion for code repositories. This *Rhetoric* sets the shape of the act; that reference sets the texture of the prose. A document needs both, and neither substitutes for the other: a flawless move structure written in dense, anaphoric, jargon-locked prose fails, and so does limpid prose with no centre of gravity.

---

## Coda

The parent theory locates a document; this companion writes it. Between them they make a single claim with two faces: that what a document *is* and how it should be *written* are the same question asked at two moments — once to place the act, once to perform it. The coordinate is the instruction. Name the register and the act correctly and the form follows; misname it and no amount of polish recovers what the wrong centre of gravity has cost. The humblest practical yield of a long theoretical detour is therefore also the most useful: before writing, say in which register — know, do, or govern — and in one word what the document is for, and mean the right word.

---

## Sources

The three registers — *know / do / govern* — are the direction-of-fit families of the parent theory (Austin; Searle; Anscombe), glossed for the writer; the finer stances are the recognized cells of its force axis, and *typified communicative action* is C. Miller's ("Genre as Social Action," 1984), carried into organizations by Yates & Orlikowski. The move-structure analysis draws on J. Swales, *Genre Analysis* (1990), particularly the rhetorical move and the CARS model, generalized from the research-article introduction to organizational genres at large. The stances and their failure modes are read charitably against the documentation-framework literature — D. Procida's *Diátaxis*, whose acquisition/action distinctions this companion recovers rather than displaces, and M. Nygard on decision records — and against the speech-act and social-ontology foundations set out in *The Inscribed Act* (Austin; Searle; Ferraris). The recipient analysis rests on Swales's *discourse community* (distance) and Weber's *legal-rational authority* (power). The surface-craft layer (§VII) has its own sources — cognitive load (Sweller), multimedia learning (Mayer), information foraging (Pirolli & Card), and the long-context behaviour of language models (Liu et al., "Lost in the Middle," 2024) — gathered in the surface-craft reference, to which this companion defers for everything below the move.
