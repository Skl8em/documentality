# Adversarial review

Two parts.
First, a hard critique of the tutorial, step by step, written from inside the confusion of actually trying to follow it.
Second, a skeptical review of the project spec, using the friction the tutorial surfaced as evidence.

## Part A — Critique of the tutorial

### Step 1

The core definition ("a recurring activity, a verb with a purpose and a doer") is the strongest sentence in the tutorial, and it did real work.
But the step gives no rule for **grain**.
Is "use it" one activity, or is "query it," "read its output," and "get an answer from it" three separate ones?
The tutorial's own wide-net list mixes grains freely — "audit, review, verify" bundles at least three activities (correctness, security, licence) that plausibly have different audiences, while "use" stays a single generic bucket — and never flags that its own example is doing this.
Since everything downstream is derived from this list, getting the grain wrong here is expensive, and the tutorial offers no way to check your grain before Step 2 already shows you the cost.

The step also never distinguishes a **recurring** activity from an anticipated one that hasn't started yet.
"Someone wants to verb it, repeatedly" is explicitly a repetition test, but my project spec names a function (an AI eventually operating the system) that is asserted in the text without a single occurrence so far — it fails the repetition test outright, and the tutorial gives no instruction for whether to include, bracket, or drop such things.
I included it and flagged the discomfort myself; a less careful first-timer might silently drop it, or silently include it and let it distort Step 5 later without noticing why.

Separately: the bounded-vs-permanent distinction that Step 5 depends on entirely is never introduced here, where it's first needed to classify activities correctly.
I had to reread Step 1 once I reached Step 5 and realized I'd need it earlier.
A first-time user without that hindsight will do Step 1 once, correctly by the letter of the instructions, and then discover in Step 5 that the classification they need was never asked for.

### Step 2

"You read them off the list, you do not invent them" is a good discipline in principle, but it collides immediately with the single-maintainer case, which the tutorial's own scratch-file framing (a lone person's personal project) practically invites.
If one person performs five different activities, do they get five audience write-ups, or one?
The tutorial never says.
I invented a "different hat" heuristic to keep the activities distinguishable, but nothing in the text licenses or forbids that move — it's exactly the kind of ambiguity that produces a stuck, re-reading-the-same-paragraph first-time experience.

Distance is defined along exactly one axis (initiated/novice, per field).
That's workable, but thin: the spec I was working from also talks about *power*, and real audiences differ in authority, urgency, and stake, not just familiarity with vocabulary.
The tutorial promises this step will tell you "who" and "what they bring," and delivers only the vocabulary axis, without warning that it is deliberately narrowing the question.

### Step 3

The "know / do / decide" triad is presented as though every need will sort into one of the three cleanly.
Mine didn't: an activity I derived (checking the corpus against its own theory) is a comparison need, not a lookup, a task, or a decision-view, and forcing it into the triad felt like a category error rather than a fit.
The tutorial doesn't warn that the triad might not cover everything, so a first-timer is likely to force a bad fit rather than notice the triad's edge.

The "returning after three months" illustration is vivid, but it is the *only* worked illustration in the whole step, and it happens to be the easiest case (you, alone, meeting your own project).
Every other persona — an installer, a contributor, an evaluator — gets one sentence of contrast ("wants the opposite order") and no equivalent worked-through example.
A step that leans this heavily on a single anecdote to teach a method risks readers copying the anecdote's conclusion ("orient then why") onto personas where it may not actually hold, rather than genuinely re-deriving it for each one — which is precisely the derivation the step claims to be teaching.

### Step 4

This is where I got most stuck.
"Open one README... do not scatter before there is anything to scatter" is written for a project starting from zero.
It gives no instructions at all for a project that is already split — which describes not just my test case but arguably most real projects that go looking for a documentation-structuring tutorial in the first place (you don't usually seek this out on day one).
I had to invent my own move: run the three seam-tests backward, as an audit of existing splits, rather than forward as a generator of new ones.
That inversion is not hard, but the tutorial doesn't perform it, doesn't name it as a variant, and doesn't warn that the "start with one file" framing will feel inapplicable the moment you try to use it on anything past inception.

The three seam-tests themselves are given without weighting.
One of my own splits (writing guidance vs. structuring guidance) didn't cleanly satisfy any of the three tests as written — I ended up leaning on a soft "these are each big enough alone" argument that stretches the "grown too big" test past what it plainly says.
The tutorial gives no guidance for what to do when a real, pre-existing split fails its own seam test: re-merge it despite the cost, or let precedent override the test?
I don't know, and the tutorial doesn't say.

### Step 5

The provenance rule — a document lives by the activity that produces and maintains it — is genuinely the best line in the tutorial: clear, checkable, and it did real work above.
But it silently assumes every document has a *currently live* activity behind it.
My project names a future capability (the AI operating the system from metadata) with no current activity producing anything for it yet.
The rule has no answer for a document that doesn't exist yet because its producing activity hasn't started — which is a completely ordinary situation for any project with a stated roadmap, and the tutorial doesn't anticipate it at all.

"Current vs. frozen" arrives here as though newly introduced, but it is the same permanent/bounded distinction Step 1 quietly needed and never named.
This is a sequencing defect: the reader is handed vocabulary one step later than the point where it was actually required, and has to backtrack to re-use it correctly.

The closing claim — root-vs-docs/ is "a consequence," because the surface is "where its users meet it" — treats "the users" as a settled singular, right after Steps 1–3 spent three steps establishing that a project meets *different* people through *different* activities.
If a project has a Documenter, a Newcomer, and an Evaluator, each meeting it differently, "where its users meet it" doesn't pick a unique root by itself — I had to decide, unassisted, which of my personas counts as *the* meeting-point audience for root placement, and the tutorial gives no method for that choice, only the assertion that a choice this important is "a consequence."

### Whole-tutorial issues

No worked example appears anywhere in the tutorial's own body — every instruction is given in the abstract, and the only concrete case offered is the reader's own unseen scratch file.
This makes it very easy to nod along to "activity, not topic" while still drifting into topic language in practice; I caught myself doing exactly this ("theory," "governance") and had to consciously translate back into verbs partway through Step 1.
A single fully worked example, even a toy one, would have caught this far earlier than my own self-monitoring did.

The "know/do/decide" triad in Step 3 also reads as a simplified public face of a richer private taxonomy — the project spec I was given separately mentions a much longer list of illocutionary forces (orient, explain, describe, prove, account, instruct, teach, recommend, mandate, commit, propose, decide).
The tutorial never discloses this relationship, or whether the triad is a deliberate simplification of that longer list or an independently-motivated idea.
Not knowing which makes it hard to know how much to trust the triad's boundaries, exactly the question that came up concretely with my "comparison need" case above.

### What a first-time user gets stuck on, concretely

Rank order of where I actually lost time or had to invent unlicensed moves: Step 4's greenfield assumption on an existing project (worst), Step 2's silence on one-person-many-hats, Step 5's silent assumption that every document has a currently-live producing activity, and Step 1's missing grain rule.
None of these are fatal, but all four required me to invent a move the text doesn't give, sanction, or even acknowledge as a fork in the road.

## Part B — Adversarial review of the project spec

The spec collapses **first encounter and ongoing reference use** into one sentence — "someone documenting their own project reads the product" — but the tutorial's own Step 3 method forced me to split this into a Newcomer (orient, then a how-to, evaluating fit) and a Documenter (task-shaped, wants a template immediately, no evaluation left to do).
The spec never names this split, even though it's a direct, unavoidable consequence of taking its own tutorial seriously.
That is either a gap in the spec's self-description, or evidence that the spec was written before this distinction was noticed — either way, applying the tutorial surfaced it, the spec didn't.

The spec states "essentially one maintainer" and a "tight readership," then separately implies (through its own function-shaped language: writing guidance, structuring guidance, governance, an eventual AI operator) at least five internally-facing activities.
All five currently collapse onto that one person.
The spec never says what happens when that stops being true — there is no stated activity for an **external contributor** joining the project, even though the tutorial's own function checklist flags "extend or contribute" as one of the most commonly-missed functions.
For a project built on a general theory of documents and explicitly meant to be reusable by others, the total silence on how a second contributor would be onboarded, and what they would read first, is a real and somewhat surprising gap.

The spec rules out a hosted site and a tie to any particular generator, but never says whether the project is **distributed or versioned** at all — is it read by cloning the repo, is there a tagged release, is there any "here is the current stable state" marker distinct from the live-editing HEAD?
Given the theory's own vocabulary includes speech acts like "commit" and "mandate," it's a notable omission that the spec never states whether the product itself is ever formally "published" or "released" as opposed to simply sitting in a single continuously-edited repository. This directly affects the README: does it introduce a *product* to outside adopters, or a personal working notebook to nobody in particular?

**Phase II is named but has no textual home.**
The spec asserts a future capability (AI instructions, git hooks, validation/generation from metadata) in enough detail to sound planned, but never says whether any placeholder document exists for it now — a design note, a frozen "future work" decision record, anything.
Step 5's provenance rule needs a currently-live activity to place a document; Phase II supplies a named future activity with no current instance of it happening, so the rule simply cannot resolve where its documentation should go today.
The spec should have said either "there is nothing written yet, and that's deliberate" or pointed to an existing placeholder — it does neither, and the ambiguity is not cosmetic, since it's the one case my structure genuinely could not place.

**The metadata schema's own status is unclear.**
The spec says the project is "mid-refactor," with "some parts still carry[ing] older vocabulary," but never states whether the schema is one of the stale parts or the settled reference everything else must catch up to.
That single fact changes where I'd file it — a stabilizing reference belongs in a different place, with a different current/frozen judgment, than an actively churning draft — and the spec leaves it unresolved.

**"Worked example of its own theory" is asserted as a property, not tied to any owner or checkpoint.**
I invented an "Auditor" activity in Step 1 to make this claim actionable under the tutorial's method, but there is no textual warrant for it — the spec never says anyone actually checks this, on any cadence, by any process.
A stricter reading would drop this from my activity list entirely and treat "being a worked example" as an aspiration the project asserts about itself rather than something anyone does — in which case my Step 1 list over-generated relative to what the spec actually supports, and I should say so plainly rather than let a plausible-sounding role stand unchallenged.

**Phases are named but not bounded.**
The spec says decisions are "grouped into phases," which the tutorial's freeze/current distinction needs in order to know when a record actually freezes.
But the spec never says what ends a phase, or what happens when a "frozen" decision is later reversed — does the old record stay frozen and a new one gets appended, or can frozen records be reopened?
Applying Step 5's freeze rule requires an answer the spec doesn't give.

**A tension between "generated reading surface" and the spec's own hand-drawn folder plan.**
The spec insists the source is tool-agnostic and that "any published reading surface is to be generated, not hand-maintained," while also describing the project as already "made of" a specific-sounding set of parts (theory / writing guidance / structuring guidance / metadata schema / governance-and-records) that reads very much like a hand-maintained folder plan.
It's not clear from the spec which of these named parts are committed source-of-truth folders I should be placing files into (per my Step 5 output), and which are conceptual groupings that a future generator is meant to derive and present, with the actual source organized some other, unstated way.
I produced a folder tree anyway, because the tutorial requires one, but the spec leaves genuinely open how literally that tree should be taken as the real source layout versus a reader-facing view that doesn't need to exist as folders at all.

**Scale claim vs. audience claims sit oddly together.**
The spec calls the project "small," with "one maintainer" and a "tight readership," which sounds like a near-solo tool — yet the same spec talks about theory essays grounded in an academic-register framework (Ferraris, illocution/perlocution) meant to be "a worked example of its own theory," which reads like a public, citable intellectual project with outside readers in mind.
These two self-descriptions pull toward different Step 4 outcomes: a solo tool needs very few seams (maybe just a README and a decisions log), while a public theoretical product with distinct communities needs the fuller split I ended up producing.
The spec doesn't resolve which self-image should win, and my structure quietly picked the more elaborate one without the spec ever having sanctioned that choice outright.
