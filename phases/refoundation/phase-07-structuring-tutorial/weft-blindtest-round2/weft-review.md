# Adversarial review — the tutorial and the weft spec, both under attack

## Part A — attacking the tutorial

### The greenfield/existing binary breaks on contact with weft
The tutorial's very first classifying move is: "Greenfield — you are starting, or still designing, and there is little or nothing written... Existing — you already have a pile of documents."
It presents this as an exhaustive either/or, chosen once, before Step 1 even begins.
weft is neither.
There is zero code and zero shipped functionality — genuinely greenfield by the letter of the definition — but there is also one dense, ten-section, near-3000-word design document that already reads like a pre-split corpus with chapter breaks.
The tutorial has no third box for "the code doesn't exist but the design doc does, and the design doc itself needs the audit treatment."
I had to invent a resolution (treat the code as greenfield, the spec-as-artifact as existing) with zero textual support, and a less improvisational reader would either force weft into "greenfield" and never split the spec at all, or force it into "existing" and be confused when Step 1 asks them to generate activities forward for a tool that doesn't run yet.
Given the tutorial's own admission that "most real projects that come looking for a structuring tutorial are" in the existing state, it is a real gap that the one hybrid case — a substantial spec, no code — goes unaddressed, because that hybrid case is exactly what a serious project looks like in its design phase, which is to say: exactly the phase weft's own frontmatter says it's in (`written-at: design-phase`).

### Step 1 is genuinely strong, and the `prep` example earns its keep
No real complaint here.
The instruction to write down "the activities that matter, whatever their cadence" and the four-bullet list (recurring / once-per-person / once-ever / hoped-never) is concrete enough to actually apply, and translating weft's "honest risk note" fallback clause into the "hoped-never" bucket was a clean, load-bearing move.
The instruction to explicitly write "X — not covered yet" rather than silently omitting an activity is good discipline and I used it twice (adopt, license/compliance).
This step earned the confidence I later lost in Step 5.

### Step 2's "you read them off the list, you do not invent them" is not honored by the tutorial's own procedure
Quoting directly: "Now, and only now, the people — and you read them off the list, you do not invent them."
This promises something Step 2 cannot actually deliver whenever the source document's *own* declared audience contradicts what its content implies — which is exactly weft's situation (frontmatter says `[maintainer, future-self]`, §3.1 and §6 are written in a voice instructing a task author).
The tutorial gives no procedure for this collision.
"Read off, don't invent" is a comforting frame, but I did invent a persona (task author) that the source's own metadata explicitly excludes, and the tutorial's confident phrasing papered over how much interpretive judgment that took.

### Step 3 makes a promise it doesn't keep
Quoting: "so if a need seems to sit between two boxes, do not force it; the tension resolves at placement, in Step 5."
It does not resolve at Step 5.
When I reached the identical structural problem in Step 5 — a document (workspace resolution, §6) with equal claims from two functions — Step 5 offers only "provenance is the primary cut" and "a function's documents stay together," neither of which tells you what to do when two functions co-produce one document.
I had to invent a tiebreaker (assign by who maintains it, not who reads it) that the text nowhere suggests.
The tutorial told me the tension would resolve later and then didn't resolve it; that's a specific, falsifiable failure of the text's own promise, not a vague complaint.

### Step 4's seam tests are the best-designed part of the tutorial
The three-item seam test (too big / divergent lives / distinct community) plus the roughly-3-to-7-sections heuristic is mechanical enough to apply without judgment calls, and it produced a decisive, unambiguous verdict on weft's spec (ten sections, clearly over threshold).
No complaints; this is the tutorial working as advertised.

### Step 5's current/frozen model is announced as fragile, and then treated as load-bearing anyway
Quoting: "Hold this current/frozen split lightly: it is a working device we are pushing on until it either proves itself or breaks — treat it as useful scaffolding, not settled law."
That's an honest hedge in the abstract.
But nothing downstream of it hedges: every worked example (README/INSTALL/CONTRIBUTING/LICENSE/ARCHITECTURE/CHANGELOG/ADR) is confidently sorted into current or frozen with no third option offered anywhere in the text.
When I hit weft's §9 — a section that is neither current reference nor a frozen decision, but an open, blocking, undecided question — the tutorial's hedge told me the model *might* break, but gave me no indication of what to do when it actually did, in front of me, on this exact project.
A hedge that isn't paired with a fallback instruction is not much better than no hedge at all.

### The three worked trees at the end don't cover weft's shape
Solo tool, used library, and data-analysis-for-a-paper are all *artifacts that already do something* — a tool that runs, a library with users, a paper that got submitted.
weft is a fourth shape none of the three examples anticipate: a pure design specification for something that does not exist yet, written by one person for an audience of one plus their future self, that is *already* large enough to need internal structure before a single line of the thing it describes has been written.
The tutorial's examples are all reassuring ("here is proof the fit is what matters") but they're reassuring about a kind of project I don't have.
I had no anchor for `docs/govern/open-questions.md`; I built it from the seam tests alone, with no worked precedent to check it against.

### Where the tutorial's caution was well-placed
To be fair in both directions: the tutorial's insistence that "this is not deterministic, and that is fine" and its explicit statement that a different reader could reach a different valid structure turned out to be true in practice, not just a disclaimer — I flagged at least three points (imagine vs. govern for §9, README vs. ADR for non-goals, know vs. do for workspace resolution) where I can see the other choice being equally defensible. The tutorial's honesty about its own indeterminacy is not padding; it correctly predicted where I would get stuck.

## Part B — attacking the spec, using the tutorial's friction as evidence

### The spec asserts a governance obligation it never meets for itself
Step 1's own bolded activity list — which I was applying to weft, not writing myself — names "audit, review, verify correctness, security, licence, compliance" as the content of `govern`.
weft's spec contains not one sentence about license, security posture, or compliance review, despite being explicitly designed to be "installable from a corporate Nexus" — i.e., inside an organization that, by definition, has a compliance process a Nexus-distributed dependency must pass through.
This isn't a neutral omission; it's the spec naming its own missing governance activity by implication (§1's Purpose section lists `govern` as a first-class need for the *library's users* — "audit, review, verify correctness, security, licence, compliance") while supplying zero material for `govern`-as-applied-to-weft-itself.

### The declared audience contradicts the actual content
Frontmatter: `audience: [maintainer, future-self]`.
Content: §3.1 explains that "Function parameters become CLI flags automatically" and §6 states "This is the single discipline the design enforces on task authors" — both sentences instructing a reader who writes tasks against weft, not a reader designing weft.
Step 2 of the tutorial ("read the audience off the activities") only surfaced this because it forced a side-by-side check between declared and implied audience that the spec itself never performs.
A spec that doesn't know who it's talking to at every paragraph is a spec that will eventually be read wrong by someone — most plausibly the exact task author it forgets to address as a persona while addressing as a reader.

### "Task authors" is a load-bearing term the spec never defines
It appears exactly once, in §6, doing real interpretive work ("the discipline of the design enforces on task authors"), and nowhere else — not in Purpose, not in a glossary, not anywhere a first-time reader would find it introduced.
This is precisely the tacit-knowledge failure Step 1 warns every project commits by default ("what a project is for... usually stays tacit, assumed, never written") — and the spec commits it about its own vocabulary, not just its own activities.

### The line-budget threshold is a policy with no enforcement mechanism
"Target: ~600-900 lines for the core, excluding the CLI. If the design drifts past that, the right move is invoke + a thin local is_done() convention, accepting the loss."
This reads as a governance commitment, but it names no owner, no check, no cadence, no CI gate, no review trigger.
Under the tutorial's own current/frozen framing, a *standing* policy like this should be `current` — i.e., alive, actively checked — but the spec gives it no mechanism to stay alive.
As written it is a hope stated once at design time, not a governed, ongoing activity, despite living in a section titled with governance language ("Honest risk note").

### §9 bundles four unrelated decisions with no owner, priority, or deadline
Manifest granularity, concurrency model, AWAITING resumption, and operator-overloading limits have nothing to do with each other beyond "not yet decided."
The tutorial's ADR pattern — "one dated, append-only entry per decision, each frozen the moment it is made" — implies decisions get closed one at a time, with some forcing function.
The spec gives none of the four forks a decision date, an owner, or a trigger for when it must be closed (before v0.1? before the first task author onboards? never, if it turns out not to matter?).
The friction I hit trying to place §9 in a tree (govern vs. imagine, current vs. frozen vs. pending) is not a documentation-structure problem — it's evidence that the spec has genuinely deferred these decisions without deferring them *on purpose*, with no visible plan for un-deferring them.

### "Provide" is nearly empty of actual content
Step 1 asks for what people *do* under each meta-activity.
Under `provide`, weft's spec supplies only negative and structural claims — "no external binary, no daemon," "installable... as an ordinary Python dependency" — and nothing about versioning, release cadence, who cuts a release, or what "publish to the internal Nexus" actually involves operationally.
Compare this to the density of §2-§8 (six sections of `build`/`use` detail) against one clause of `provide` detail: the spec has clearly been written from inside the `build` activity outward, and the `provide` activity — the one that determines whether anyone outside the author ever actually gets this library — is the thinnest part of the document by a wide margin.

### Non-goals are argued like decisions but declared like facts
"Not a build system competing with make on compilation graphs of thousands of artifacts" is a justified, reasoned scope boundary — it has the shape of something that was decided, possibly after considering the alternative.
But it sits in a plain prose list with no framing about whether it's revisitable, and the tutorial's decision-record pattern (Step 5) has no way to apply itself to a claim that looks like a decision but isn't marked as one.
This is a spec-level ambiguity, not just a placement problem: readers six months from now won't know whether non-goals are settled architecture or just today's opinion, because the spec never says.

### The most concrete, most "do"-shaped material in the spec is explicitly marked provisional
§7's CLI usage block is introduced as "CLI (illustrative)."
That's the exact material a task author would learn the tool from — the only worked, concrete surface in the entire document — and it's flagged, in the spec's own words, as not necessarily final.
A structuring exercise has to place this material somewhere (I put it in `docs/do/cli-reference.md`), but doing so means writing a "current, do" document out of content the spec itself calls illustrative rather than decided.
That's a real contradiction for anyone trying to structure this project today: the spec wants a reference document written about something it says isn't a reference yet.

### The risk note argues for taking on risk, then under-specifies the escape hatch
The spec's central justification for building a custom orchestrator at all rests on a bet: state-branching and alternative-preconditions are "genuine and recurring" needs, and the core stays small.
The escape hatch — fall back to `invoke` + manual `is_done()` — is the single most important sentence in the risk calculus, since it's what makes the bet survivable if it's wrong.
It gets one clause, no migration plan, no data on what existing weft users would lose.
For a document that spends real effort justifying a one-person-maintained dependency (team-rotation risk, named explicitly), the least-developed part of the whole spec is exactly the part that determines how bad it is if the bet fails.
