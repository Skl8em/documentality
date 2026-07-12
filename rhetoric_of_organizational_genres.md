# A Rhetoric of Organizational Genres
## From the inscribed act to the act of writing

*A companion to* The Inscribed Act: A Coordinate Theory of the Organizational Document

---

## Preface: the generative turn

The coordinate theory of the organizational document classifies: it tells you *where* a document sits — what it does (its illocutionary force), toward whom (distance and power), and whether it aims to change the reader (its formative character). Classification is useful for an archivist. It is not, by itself, useful for a writer.

This companion takes the step from classification to composition. Its premise is a claim made in passing by the parent theory and elevated here to a working principle:

> A document's coordinate is not a label applied after writing. It is an instruction issued before it. To know a document's force is to know what matters in it, what its centre of gravity is, and therefore how to write it.

The evidence for this is mundane and convincing. Asked to write the front page of a software project, a competent author who believes the task is to **describe** the project will produce a flat inventory of features. The same author, told the task is to **orient** the reader — to answer *where am I, what is this, why should I care, where do I go next* — will produce something that actually works. Nothing changed but the verb. The verb did the work, because it pointed at the centre of gravity, and everything else arranged itself around that point.

What follows is a rhetoric in the classical sense: not a set of templates, but an account of the *stance* each kind of act requires, the *move structure* that realizes it, the thing that must be gotten right, and the characteristic way it fails. Templates can be derived from this; they are not a substitute for it. The treatment is grounded in genre linguistics — the notion of the **move**, a stretch of text performing one coherent communicative function — but it is meant to be read by anyone who has to write under a deadline and wants to know where to put their effort.

A caution carried over from the parent theory: this is an *open* repertoire. The forces below are the families that recur until new material stops adding them, not a closed catalogue. New stances will appear; existing ones will split. The value is not in the completeness of the list but in the habit of asking, before writing anything, *what is this document trying to do, and to whom* — and letting the answer set the form.

---

## How to read each entry

Each force is presented as a writer's stance, with five elements:

- **The generative verb** — the word that, held in mind while writing, points at the centre of gravity. Often not the classificatory name. A decision record is classified under *decide*; it is *written* under **justify**, because justification is what matters in it.
- **What is at stake** — the one thing that, if gotten wrong, makes the document fail regardless of how polished it is.
- **The move structure** — the ordered functional units that realize the act. Moves are not headings; a single paragraph may carry several, and good documents often fuse them. They are a checklist of *functions that must be present*, not a mandatory outline.
- **The failure mode** — the characteristic way the document collapses, usually by drifting into a neighbouring force.
- **Genres** — the recognizable document types that instantiate the stance.

After the eleven entries, two cross-cutting sections show how the **recipient relation** (distance and power) rewrites these structures, and how the **formative** stances differ in kind from the rest.

---

## I. The assertive stances (word-to-world)

These make words answer to the world. Their shared virtue is fidelity; their shared temptation is to slide into one another, because they all traffic in true statements and differ only in what the truth is *for*.

### Describe

- **Generative verb:** *specify.*
- **At stake:** completeness and neutrality. The reader must be able to find any fact and trust that what is stated is exhaustive within its scope.
- **Move structure:** delimit the scope → state the facts in a stable, predictable order → exemplify where a fact is ambiguous → mark the boundaries of what is *not* covered.
- **Failure mode:** narrativizing. The moment a reference starts explaining *why*, it has drifted into *explain* and stopped being reliable as a lookup surface. Description does not argue and does not teach; it states.
- **Genres:** reference manual, API documentation, data dictionary, glossary, specification.

### Orient *(formative)*

- **Generative verb:** *situate.*
- **At stake:** the reader never losing the thread. Every element must answer one of four questions — *what is this, where am I, why does it concern me, where do I go next* — and anything that answers none of them is noise.
- **Move structure:** name the whole in one line → locate the reader within it → state the relevance to the reader's likely purpose → route onward to the appropriate next document.
- **Failure mode:** turning into a manual (drifting to *describe*) or a tutorial (drifting to *teach*). An orientation that tries to be complete has failed; its job is to hand off, not to hold.
- **Genres:** README, project overview, landing page, table of contents with annotations, "start here" page.

### Explain *(formative)*

- **Generative verb:** *illuminate.*
- **At stake:** the reader's mental model. Success is not that the reader can recite facts but that they now understand *why* the thing is as it is and could reason about cases not covered.
- **Move structure:** pose the question or tension the reader is likely to hold → build the model that resolves it, in conceptual not procedural order → connect the model to its consequences and limits → leave the reader able to extrapolate.
- **Failure mode:** degenerating into a reference list (losing the *why*) or into instructions (answering *how* instead of *why*). Explanation is the only assertive stance organized around understanding rather than retrieval.
- **Genres:** explanation / discussion document, design rationale, `ARCHITECTURE.md`, conceptual overview, the "why" sections of good documentation.

### Prove

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

## II. The directive and commissive stances (world-to-world)

These ask the world to be made to match the words. Their shared property is that they create obligation — on the reader, on the writer, or on both — and their shared temptation is vagueness, because precise obligation is uncomfortable to write.

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
- **Failure mode:** softening into advice. The rationale grows, the modal verbs weaken from *must* to *should* to *might consider*, and the reader can no longer tell what is required. Mandate that is too gentle becomes *explain* with a moral.
- **Genres:** policy, naming or coding convention, standard, `CONTRIBUTING.md`, directive.

### Commit

- **Generative verb:** *promise precisely.*
- **At stake:** the precision of what is promised and, equally, what is *not*. An unbounded promise is a liability; the value of a commitment is as much in its limits as in its undertaking.
- **Move structure:** define the scope of the undertaking → state the promise in measurable terms → state the conditions, exclusions, and limits → specify the remedy or escalation when the promise is not met.
- **Failure mode:** ambiguity that creates unbounded exposure — the promise whose terms are warm but unmeasurable, so that no one can say whether it was kept. A commitment that cannot be falsified is not a commitment.
- **Genres:** service-level agreement, charter, contract, objective with key results, public roadmap (as promise).

### Propose

- **Generative verb:** *argue.*
- **At stake:** the case, and the alternatives considered. A proposal that states a preference without arguing for it against the alternatives is a request, not a proposal, and invites a yes/no rather than a decision.
- **Move structure:** establish the territory (the shared situation) → identify the problem or gap → build the case for the proposed course, treating the alternatives fairly → make the explicit ask of the reader.
- **Failure mode:** asserting a preference as though it were obvious, skipping the alternatives — which leaves the reader unable to *decide*, only to *agree or refuse*. The move that distinguishes a proposal from a demand is the honest treatment of what was rejected.
- **Genres:** RFC, requirements document, design proposal, product requirements document, pitch.

---

## III. The declarative stance (both directions)

### Decide

- **Generative verb:** *justify.*
- **At stake:** the reasoning, not the verdict. The decision itself is a single line; the entire value of the document is the record of *why*, because that is what a future reader — including the author — will need when the context has been forgotten and the decision is questioned.
- **Move structure:** state the context and the forces in play → lay out the options that were genuinely considered → record the decision → record the consequences accepted, including the ones that are unwelcome. The reasoning is written to be read by someone who does not yet agree.
- **Failure mode:** recording the verdict and discarding the reasoning — the decision log that says *what* was chosen and is therefore useless the moment anyone asks *why*. A decision record without its rejected options is an assertion, not a justification.
- **Special property:** a decision is *dated-fixed* by nature. It is the record of a moment of choice and must not be edited to reflect a later one; a superseding decision is a new record. To rewrite it is to erase the organization's memory of how it once reasoned.
- **Genres:** architecture decision record, committee minutes, sign-off, formal approval, resolution.

---

## IV. How the recipient rewrites the stance

The eleven stances above describe *what* each act does. But the same act, performed toward a different recipient, is *written differently* — and the two coordinates of the recipient relation rewrite it along two distinct dimensions.

**Distance rewrites the scaffolding.** Distance is how much of the writer's discourse community the reader shares — how much code is common. The smaller the shared code, the more the document must carry its own context: define its terms, state what peers would assume, explain the conventions it relies on. A proof among specialists may exhibit only its results, because the method is common ground; the same proof for a reader outside the field must make the method visible step by step. Every stance has a "native" amount of scaffolding for its home community and must add more as it travels outward. The writer's question is: *how much of what I take for granted does this reader not share?*

**Power rewrites the armor.** Power is whether the reader can impose consequences on the writer. The greater that power, the more the document must be defensible: self-contained, precise, free of the loose phrasing that is harmless among peers and dangerous before an authority. This is independent of distance. A note to one's own manager travels almost no distance — the code is fully shared — yet carries high armor, because the manager holds power. A specification for an engineer at another firm travels far in distance yet needs little armor, because that engineer holds none. The writer's question is: *can this reader use my words against me, and is the document built to withstand that?*

The sharpest case is the proof addressed to an authority — *prove* at maximum distance and maximum power simultaneously. It must expose its entire method (distance) *and* be airtight against hostile reading (power), which is why evidential documents for auditors or courts are the most laborious writing an organization produces. The labor is not optional diligence; it is the move structure of *prove* rewritten by the two coordinates at their extreme.

A corollary, carried from the parent theory: do not pay this cost everywhere. Writing every document as though its reader held power and shared no code — the "write every email as if for court" reflex — over-armors and over-scaffolds routine communication into illegibility. The recipient relation tells you where the cost is owed and, just as importantly, where it is not.

---

## V. What the formative stances ask that the others do not

Three of the eleven stances — orient, explain, teach — are **formative**: they aim to change the reader's internal state, not merely to relate words and world. They share a property that sets them apart from the other eight and changes how they must be written.

The non-formative stances succeed when the document is *correct*: the reference is complete, the instruction works, the commitment is precise. The formative stances succeed only when the *reader* is changed — and the reader's change is not visible in the document. This is why they are the hardest to write and the easiest to misjudge. A tutorial can be factually flawless and pedagogically useless; an explanation can be complete and illuminate nothing; an orientation can list everything and situate no one.

The practical consequence is that formative documents must be written from the reader's present state, not the subject's logical structure. The describer organizes by the shape of the subject; the explainer must organize by the shape of the reader's likely confusion. The instructor lists the steps of the task; the teacher must stage the steps of the *learner's* growing competence, which is a different order. The orienter must model where the reader actually stands, not where the map says they are. Each formative stance, in other words, requires a theory of the reader — and that theory, not the subject matter, is its organizing principle.

This is also why the three formative stances are the ones most often misfiled as their non-formative neighbours, and most damaged by the misfiling. An explanation written as a reference, a tutorial written as a how-to, an orientation written as a description: each is the formative act flattened into its informational shadow, correct in content and inert in effect.

---

## VI. Using the rhetoric

In practice the rhetoric is a short interrogation to run before writing anything:

1. **What is this document doing?** Find the force. If more than one, find the *dominant* one — the centre of gravity — and treat the others as subordinate. A README that orients but also instructs is an orientation with an instruction inside it, not a hybrid with no centre.
2. **What is the generative verb?** Hold it in mind. Let it set the centre of gravity and subordinate everything else to it.
3. **Is it formative?** If so, organize by the reader's state, not the subject's structure, and judge success by the reader's change, not the document's correctness.
4. **Who is the recipient — in distance and in power?** Set the scaffolding from the distance, the armor from the power. Pay each cost where it is owed and nowhere else.
5. **What is the failure mode for this force?** Name it before starting, and watch for the drift toward the neighbouring stance.

This is not a template. It is the set of questions a template would have to answer, and a writer who carries the questions can compose without one — which is the point. Templates standardize the output; the rhetoric trains the judgment that produces the output, and judgment travels to the cases no template anticipated.

---

## Coda

The parent theory locates a document; this companion writes it. Between them they make a single claim with two faces: that what a document *is* and how it should be *written* are the same question asked at two moments — once to place the act, once to perform it. The coordinate is the instruction. Name the act correctly and the form follows; misname it and no amount of polish recovers what the wrong centre of gravity has cost. The humblest practical yield of a long theoretical detour is therefore also the most useful: before writing, say in one word what the document is for — and mean the right word.

---

## Sources

The move-structure analysis draws on J. Swales, *Genre Analysis* (1990), particularly the notion of the rhetorical move and the CARS model, here generalized from the research-article introduction to organizational genres at large. The stances and their failure modes synthesize the documentation-framework literature (D. Procida's Diátaxis for the formative/non-formative and action/cognition distinctions; M. Nygard on decision records) with the speech-act foundations set out in the parent essay (Austin; Searle; Anscombe). The recipient analysis rests on Swales's *discourse community* (distance) and Weber's *legal-rational authority* (power), as developed in *The Inscribed Act*.
