---
title: "Structuring tutorial — review of the blind test, and a rewrite plan"
force: propose
register: govern
intention: suasive
view: synchronic
provenance: { type: project, id: phase-07-structuring-tutorial }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

A structured reading of the blind test, and a plan (not diffs) for the next tutorial rewrite.
Parts A and B are written before reading Benjamin's own notes; Part C reacts to them.
For each critique the verdict is **accept** (with a plan-level change), **partial**, or **reject** (with a reason).

## Overall take

The test was worth far more than the tutorial cost.
Two things stand out before any detail.

First, the two reviews **converge** — grain, greenfield-vs-existing, the missing worked example, the strained know/do/decide triad, and the homeless future/generated artifacts appear in both, independently.
Convergence across a theory-native project (ours) and a plain Python library (weft) is the strongest evidence these are real gaps, not artifacts of one reader.

Second, weft is the **more trustworthy** signal.
Our own project was written under the same theory the tutorial encodes, so the self-run risks circularity — the agent even caught itself possibly fitting our project to the tutorial's example rather than deriving it.
weft is the clean blind subject; where weft and self agree, trust it.

The tutorial's core is validated, not in doubt: the **verb test** ("someone wants to ⟨verb⟩ it, repeatedly") and the **provenance rule** ("a doc lives with the activity that produces and maintains it") are named the best lines by both readers and did real work.
The fixes below are a handful of **structural moves**, not a hundred nits.

## Part A — The critique of the tutorial

### A1. Step 1 has no grain / stopping rule — **accept (top priority)**

Both readers hit this first and hardest: "use it" as one activity vs three; weft produced 12 activities where another reader would produce 6 or 20, with no way to know which is right or that you are done.
Everything downstream inherits the grain, so getting it wrong is expensive and invisible until later.

Plan: tie grain to its *purpose*. Split an activity only when the split would change **who does it, what they already know, or what they need** — i.e. when it yields a different audience, distance, or need downstream; merge otherwise.
Add that as the explicit stopping test ("if two candidate activities would produce the same person, distance, and need, they are one"), and show one worked merge and one worked split.

### A2. Step 1 conflates actual and intended activities — **accept**

The "recurring" test excludes anything not yet happening, yet weft is a design-phase spec (nothing has recurred) and our project names a future Phase-II activity.
Both readers had to guess whether to include, bracket, or drop these.

Plan: introduce a tense/stage distinction. An activity is **actual** (already happening) or **intended** (planned, on the roadmap).
Ask up front what stage the project is at; include intended activities but mark them, because their audiences are *predicted* not observed (revisit later) and their documents get a roadmap home, not "nowhere" (see A7).

### A3. Step 1 needs permanent-vs-bounded, introduced here not in Step 5 — **accept (sequencing)**

The permanent/bounded distinction that Step 5's current/frozen depends on is only introduced in Step 5, so a by-the-letter first-timer classifies activities in Step 1 without it and must backtrack.

Plan: when listing each activity in Step 1, mark it **permanent** (never ends → its docs stay current) or **bounded** (ends → its records freeze). Step 5 then falls straight out.

### A4. Step 2 has no rule for one person, many hats — **accept**

The modal case for the scratch-file framing — one maintainer performing every activity — is unaddressed; both readers invented a "hat" heuristic to keep activities distinct.

Plan: name the move. The audience of an activity is its **stance** (the knowledge in play and the need at that moment), not a headcount; so a solo maintainer still gets one audience-role *per activity*, and they may collapse to one document later only if their needs coincide.
Use the solo case as the worked example, since it is the common one.

### A5. Step 2's distance axis is thin, and its status (observed vs designed) is unstated — **partial**

Reject adding `power`: narrowing to distance is right for a first run, and a small/solo project rarely needs armor.
Accept the two disclosure gaps: (a) say plainly that we use distance and set power aside on purpose; (b) say that on a project with no real readers yet, every distance is a **prediction/design target** to revisit, not an observation.

### A6. Step 3's know/do/decide triad is wrong, not just incomplete — **accept**

A comparison/audit need (ours) and a diagnose-a-failed-run need (weft) fit none of the three; and the triad's relation to the fuller force list is never disclosed.

Plan: replace **know / do / decide** with the theory's own three registers **know / do / govern**, and widen `know` to *understand, compare, and show evidence* (explain, account, prove), not just look up.
Diagnosing and auditing are then `know` needs, cleanly.
Disclose in one line that the triad is a coarse gloss over the full force list (link the forces), so a reader knows how much to trust its edges.

### A7. Step 5 (and Step 1) cannot place a document whose activity has not started — **accept**

Both readers hit the roadmap case: a future capability names an activity with no live instance, and the provenance rule "simply cannot resolve" where its doc goes.

Plan: an **intended** activity (A2) has a provenance too — a *planned/roadmap* one.
Its material (a design note, a "future work" `propose` record) lives with the steering/roadmap activity until the activity starts, then migrates.
Intended activities get a home, not "nowhere." (A2 → A7 are one thread.)

### A8. Step 4 assumes greenfield; most real projects arrive already split — **accept (top priority)**

Self ranks this the worst: "start with one README" is inapplicable the moment a project is past day one, which is exactly when people seek a structuring tutorial.
Both readers inverted the seam-tests into a backward *audit* of existing splits.

Plan: give the tutorial **two entry states**.
Greenfield: start with one README, split forward as seams bite.
Existing: run the seam-tests *backward* as an audit — keep each split that passes a seam, question each that does not.
Name the audit variant; this also legitimizes "the structure mostly validated what existed" as the *correct* outcome for an existing project.

### A9. Step 4's seams are ad hoc and miss the activity/provenance seam — **accept**

The three tests (too big, divergent lives, distinct community) are judgment calls with no thresholds, and one real split (writing-guidance vs structuring-guidance) passed none cleanly — because the actual seam there is **different activity → different provenance**, which the tests omit.

Plan: re-derive the seams from Step 5's own principle so Step 4 and Step 5 share one rule.
Primary seam: **different producing activity (provenance)**; secondary: **divergent lives** (freeze vs current) and **size**; plus **distinct community**.
Add guidance for the reverse case: a pre-existing split with no seam is a merge candidate, but precedent/cost may justify keeping it — flag it as debt rather than forcing a re-merge.

### A10. Step 4/5 never names the "decisions that freeze" artifact — **accept**

The tutorial builds up to "you need a place for decisions that freeze" and then never says what it is (format, filename, contents); a reader who doesn't know "ADR" is left to invent it.

Plan: name it — a **decision record** (ADR): append-only, one per decision, dated, frozen — and point to the `decide` force and its template for the shape.

### A11. Step 5 has no category for generated/ephemeral artifacts — **accept**

weft's per-run logs are neither a current living doc nor a frozen decision; the current/frozen dichotomy assumes every artifact is authored.

Plan: add a short third category — **generated/ephemeral** artifacts (logs, reports, build output) are not documentation; you document *how to read them*, but the artifacts themselves sit outside the corpus (often git-ignored).

### A12. Step 5's "where its users meet it" reasserts a singular user — **accept**

After three steps establishing that a project meets *different* people through *different* activities, the root-placement line collapses them back to "the users" with no method for picking which one anchors root.

Plan: root is the surface for the **dominant / first-contact** community — the audience the project most exists to serve, or who arrives knowing least.
State the rule; other audiences' surfaces are nested or generated. (This is the `dominant-community` idea we already hold; surface it here.)

### A13. No worked example anywhere in the body — **accept (high value)**

Both readers drifted from activity into topic language ("theory", "governance") and had to self-correct, precisely because every instruction is abstract and the only concrete case is the reader's own unseen scratch file.

Plan: thread **one small, neutral toy project** (not ours — a neutral one, e.g. a little CLI or a recipe collection, to open rather than anchor) through all five steps, ending Step 5 with its concrete folder tree.
Add a second short contrasting ordering in Step 3 (installer, evaluator) so the reader sees the *derivation* vary, not one anecdote copied.
A teach without a worked example is under-built for its own force.

### Not accepted / deferred

- Adding `power` to Step 2 (A5): **reject** for now — keep the first run to distance.
- Fixing the spec gaps *inside the tutorial*: out of scope — those are project-level (Part B), not tutorial text.

## Part B — The tutorial's response on our own project

The tutorial *worked*: it produced a coherent structure for our project (`README` + `docs/{theory, writing, structuring, schema, decisions}`) as a consequence of the five steps, not a template dropped on top.
But the run is worth reading for two distinct yields.

**What it reveals about the tutorial.**
The self-run reproduced every A-finding above from the inside, and added one honest note we should keep: the derived tree (grouped by producer activity) **does not match our real repo** (phase-indexed, `write/`, `structure/`).
That mismatch is not a failure — it is the tutorial deriving a *reader-facing grouping* while our source is deliberately *producer/phase-organized* (our own source-vs-generated decision, ADR-018).
But it shows the tutorial does not yet help the user tell "the tree you derive" from "source shelf vs generated surface"; the returning-from-blind reader will read the mismatch as a contradiction.
Plan consequence: the rewrite should, at Step 5, say explicitly that the tree you derive is a *reader view*, which on a real project may be generated and need not equal the source layout — this connects the tutorial to the source/surface split it currently omits.

**What it reveals about our own project (spec gaps, for our front-end, not the tutorial).**
Applying the method surfaced real, unmade decisions in our `self-spec` — several genuinely open:

- No **external-contributor** activity or audience, though "extend/contribute" is the checklist's most-missed function; who onboards, and what do they read first?
- **Phase II** is asserted but has no textual home (A7) — is there a placeholder, or is "nothing yet, deliberately" the answer?
- The **schema's status** is unstated — is it a stale part or the settled reference the rest must catch up to? (This is exactly our open Decision 1/2 on the frontmatter.)
- **Phases named but not bounded** — what ends a phase; can a frozen record be reopened, or only superseded? (We have an answer — supersede, never edit — but the spec didn't say it.)
- **Published vs. notebook** — is the product ever released/versioned, or a continuously-edited repo? This changes what the README is *for*.
- **Small vs. public** tension — "one maintainer, tight readership" vs an academic-register theory meant to be reusable; these pull toward different amounts of structure.

None of these are tutorial bugs; they are our project's own front-end still owing answers — several already on our list, a couple (contributor onboarding, published-vs-notebook) genuinely new.

## Part C — Reactions to Benjamin's own notes

His notes converge with Part A almost everywhere, and on five points they go deeper and override my fixes — for the better, because they trade a pile of local rules for one attitude and a few sharp reframes.

**The biggest correction: relevance, not recurrence.**
I anchored Step 1 (and A2) on the "recurring" test; he is right that the criterion is wrong.
What makes an activity a function is **importance** — that it is worth thinking and talking about — and recurrence is only one *sign* of it.
A one-off scientific analysis is the most important activity of its project; adoption happens once per adopter yet must go well; defensive activities are documented for disasters everyone hopes never happen.
Adopt his drafted definition ("an activity *of relevance*…") wholesale — it dissolves the future / one-off / defensive problems (A2, part of A7) at the root instead of patching them.

**The unifying move: make the fractal explicit — and stop faking determinism.**
This is the deepest thing in his notes, and it reframes half of Part A.
Several of my "accept → add a rule" items (A1 grain, A9 thresholds) were reaching for a determinism the system does not have and should not pretend to.
Replace them with one attitude: **start coarse, keep 3–7 items per level, group into meta-functions past ~7, refine only when a gap becomes intolerable — and assume you have holes; the point is to *see* them.**
Present the moving parts as **hierarchies, not flat lists**, so the reader always has a next step, and give an **explicit licence to leave the path** ("no map, only a light").
This single move answers grain, thresholds, non-determinism, and the "I had to invent an unlicensed move" complaint at once — and it is itself fractal (it applies to functions, to folders, even to ADRs).

**Author, not user.**
His sharpest reframe of A12: the source is organized for **the person writing the document — its first reader** — not for "the user."
External readers get a *generated distribution* in their own reading logic; the folder tree serves the author.
This resolves the singular-user problem cleanly, matches our own source-vs-generated decision (ADR-018), and should replace "where its users meet it" throughout Step 5.

**`imagine` as an activity.**
For design-phase and future work he adds a function I missed: **imagine** — dream what could be done with or extended from what is here.
It homes the not-yet-written (A7) as the output of a real present activity (thinking), pulled out of the hat when the work starts — cleaner than my "planned provenance" patch.

**Worked examples via the conventional repo documents.**
His answer to A10 and A13 at once, and better than mine: because we document a code repo, **name the classics** — README, CONTRIBUTING, LICENSE, ARCHITECTURE, INSTALL, CHANGELOG, ADR — classify each by force, and place each (`./` by convention or installer-speed, or `docs/`, and the `know/do/govern` subfolders once a folder passes ~7).
This names the ADR, gives concrete examples throughout, and yields the hand-holding ending he sketched.
On the final tree, follow his instinct: show **two or three genuinely different valid trees** (or hand the reader the build-rule) rather than one, so the example opens the field instead of anchoring it.

Where his notes and Part A agree, with small adjustments:

- **A6 (triad):** he confirms **know/do/govern** over know/do/decide (a diagnosis's *result* is `govern` with a temporal provenance; a *how-to-diagnose* is `do`), and adds the right framing — at this step we *draw the boxes, we do not yet file into them*, so some frustration is deferred, not a defect.
- **A5 (distance):** reframe as **intended audience [distance + power]**, each dimension "as rich as human relations, not a binary," with the future-self reminder — but keep the observed-vs-intended flag and power's richness *out of this tutorial*, for later.
- **A11 (generated artifacts):** out of scope here (this organizes the *repo's* documentation); point to a later use-case that thinks about generating and placing them.
- **A9 (thresholds):** borrow from the surface-craft patterns (`patterns-ecriture-documentation`) and the 3–7 heuristic rather than inventing line counts.
- **weft's "generated surface" promissory note:** he agrees it is a pedagogy gap → it belongs to a **second tutorial on the frontmatter**, pointed to, not explained here.

One open tension he flags honestly, worth keeping visible: he is **not yet sure the permanent/bounded (current/frozen) distinction is well-founded in the theory** — "on pousse jusqu'à ce que la contradiction éclate."
So A3's "introduce it in Step 1" should be done lightly, as a working device, not sold as settled.

And a moment worth keeping: the blind agent drifted from *activity* into *topic* language ("theory", "governance") and had to consciously translate back — unknowingly performing the exact failure that proves the worked example is needed.

## The shape of the rewrite (consolidated)

Putting Parts A–C together, the next tutorial is not thirteen fixes but **five deep moves plus a few small ones**.

1. **Redefine a function by relevance, not recurrence** (his definition).
2. **Make the fractal explicit**: coarse-first, 3–7 per level, group past ~7, refine only on intolerable gaps; hierarchies not lists; assume-and-see your holes; explicit licence to extend.
3. **Organize for the author** (first reader); readers get generated distribution; defer generation and frontmatter to a second tutorial.
4. **Add `imagine`** as the design / future activity; it homes the not-yet-written.
5. **Ground it in the conventional repo documents** as worked examples — name, classify, place — ending with two or three different valid trees and a hand-holding build-rule.

Small ones: know/do/**govern** (+ "drawing boxes, not filing yet"); permanent/bounded introduced early but held lightly; the **intended-audience** framing; generated artifacts scoped out with a pointer; thresholds via the patterns + the 3–7 heuristic.

We integrate on the next pass, not now.
