# Adversarial review

Written after actually running the tutorial against weft.
Part (a) attacks the tutorial; part (b) attacks the spec.
Neither is charitable on purpose.

## Part (a) — the tutorial, step by step

### Step 1

The verb-phrase test ("someone wants to **⟨verb⟩** the project, repeatedly") is the single most useful sentence in the whole tutorial — it's concrete and it worked.
But the step gives no **granularity rule**, and that hurt immediately.
Is "declare a precondition" its own activity, or a sub-case of "author a task"?
Is "embed the Runner" one activity, or two ("construct a Runner" and "invoke it from a host")?
I ended up with 12 activities for weft; a different reader could just as easily produce 6 or 20 from the same spec, and the tutorial gives no way to know which is right, or even that there is a right answer.
For a "guided first run" whose whole promise is a structure that "fits your project," having the very first step's output be this unconstrained is a real gap — not a nuance, a gap, because every later step inherits whatever granularity Step 1 happened to land on.

The step also silently assumes the project already has real, present-tense activity happening around it.
weft is a **design-phase spec** — there is no code, no installed users, no history of anyone actually having run `weft list` yet.
The tutorial never asks "what stage is your project at" and gives no guidance on whether to name activities that are only *intended* (per the spec's feature list) versus activities that have *actually happened*.
I had to guess that "name the activities the spec describes" was the intended reading; a stricter reading of "recurring activity" would have produced almost nothing, since nothing has recurred yet.

The "wide net" bullet list is generic enough to apply to literally any software project — which is fine as a prompt, but it provides zero worked example at the weft level of specificity, so a first-timer has no model of how detailed a Step 1 note is supposed to be ("extend it" vs. "declare a precondition with a resolver and provider alternatives" are wildly different grain sizes and the tutorial's own examples don't disambiguate this).

### Step 2

"Read the people off the list, don't invent them" is good instruction, but it collides head-on with the very common case — arguably the modal case for small/solo tools like weft — where **one physical person performs every activity, wearing different hats at different times**.
The tutorial doesn't say whether to still write out a separate "role" per activity in that case (which is what I did, producing a table of 12 roles that mostly resolve to "the maintainer"), or to collapse them, or how to tell the difference between a genuinely distinct audience and the same person on a different day.
This is not a nitpick: it directly determines whether the eventual doc split (Step 4/5) produces real, load-bearing seams or fake ones.

"Distance: initiated vs. novice" is a clean binary but the tutorial doesn't say whether this is a **description of who exists right now** or a **design target for who you want to reach**.
For a pre-launch, design-phase project like weft, there is no one to observe yet — every distance judgment I made was a prediction, not an observation, and the tutorial gives no vocabulary for that difference (it matters: a prediction should be revisited later, an observation shouldn't need to be).

### Step 3

The know/do/decision trichotomy is useful and I could apply it to most activities.
It strained on **diagnosing a failed run**: that need is not really "know" (abstract understanding) or "do" (perform an action) — it's closer to "figure out what happened," a diagnostic/troubleshooting need that shares features of both and isn't cleanly either.
The tutorial doesn't acknowledge a fourth bucket, or say what to do when an activity's need doesn't fit the three cleanly.

The ordering advice (orient → why → how-to for a returning owner; how-to first for a fresh installer) is the best-specified part of the whole tutorial — concrete, memorable, and I used it directly.
But it only covers **two** canonical orderings out of the many roles Step 2 can produce.
For an integrator embedding a library, an auditor, or a prospective adopter reading a pitch, I had no example ordering to draw an analogy from and had to invent the ordering myself (see Step 3 of the response file) with no way to check it against the tutorial's intent.

### Step 4

The three seam triggers (too big, divergent lives, distinct community) are reasonable in spirit but every one of them is a judgment call with **no threshold given** — no line count, no "how distinct does a community need to be," no example of a document that was borderline and how it was resolved.
"Divergent lives — a decision that should freeze versus a reference you keep editing" is the strongest and clearest of the three, and it mapped cleanly onto weft's four open design decisions.
But the tutorial never actually names the artifact this produces (a decision log / ADR-style record) even though it is unmistakably gesturing at that exact pattern — a first-time user who doesn't already know the term "ADR" from prior experience gets no help inventing the format, filename convention, or contents of that document.
This is a real drop: the tutorial builds up to "you need a place for decisions that freeze" and then does not tell you what that place looks like.

### Step 5

The provenance rule ("which activity does it belong to, does that activity ever end") is the tutorial's best idea and did real work — it's what let me tell the difference between `docs/design.md` (current, because "extend/steer" is ongoing) and `docs/decisions/000N-*.md` (frozen per entry, because each individual decision is a bounded effort even though the log as a whole keeps growing).
That said, applying it exposed a gap the tutorial doesn't cover at all: **generated, ephemeral artifacts**.
weft's spec describes a per-run structured log (`RunReport`s under `workspace/.weft/runs/`).
That is neither a "current" living document (nobody edits it) nor a "frozen decision record" (it isn't a decision) — it's data, produced by running the tool, not authored by a person.
The tutorial's whole current/frozen dichotomy assumes every document is authored; it has no third category for machine-generated logs, and I had to invent the workaround myself (document *how to read* the reports, and exclude the reports themselves from the documentation system) with no textual support for that call.

The root-vs-`docs/` guidance is stated only as an abstract consequence ("your project's surface sits where users meet it, internal records sit apart") with **zero concrete example** — no sample filenames, no sample tree, nothing.
For a tutorial explicitly framed as "a guided first run" (not a reference), ending the entire walkthrough without ever showing what the resulting folder looks like is a strange omission; I had to invent every filename in my response file (`README.md`, `docs/design.md`, `docs/decisions/0001-*.md`, etc.) with no check against the tutorial's intent, and a different first-timer would invent a completely different naming scheme with equal justification.

The line "on a real project [the browsing order] can be generated from the files rather than dictating the folders" is asserted, not explained — no mechanism, no example of front matter or metadata that would make this possible, no pointer to a tool.
It reads like a promissory note for a feature that isn't part of this tutorial, dropped into the middle of the one section that's supposed to close out concretely.

### Overall, what would stop a first-timer cold

1. No stopping rule for Step 1's granularity — you can't tell if you're done.
2. No guidance for pre-launch/no-users-yet projects, despite "design-phase spec" being an extremely common real state for a project to be documented in.
3. No worked example of the final folder tree anywhere in the tutorial, despite Step 5 being explicitly "where things go."
4. No name given for the "decisions that freeze" artifact that Step 4 clearly requires (ADR or equivalent).
5. No treatment of generated/ephemeral artifacts (logs, reports) as a category distinct from authored documentation.

## Part (b) — the weft spec, adversarially

**Contradiction: declared audience vs. described feature surface.**
The spec states the audience is `[maintainer, future-self]`, full stop.
But it also describes: installation from a *corporate* Nexus (implying colleagues, a team, procurement — not a solo hobbyist repo); embedding inside *another library* (implying a second developer who is not the maintainer); and a `weft graph` export that "feeds a docs pipeline" (implying a docs-consuming audience, human or tooling, that is never named).
Either the audience list is aspirationally narrow and wrong, or these three features are speculative and shouldn't be spec'd yet — the spec doesn't say which, and Step 2 of the tutorial forces this contradiction into the open the moment you try to name real people.

**Undefined mechanism, load-bearing: "workspace."**
`FileDeps`, the manifest, and `Context`'s "resolves workspace at invocation time" all depend on how a workspace gets declared.
The spec says the CLI mode uses a `weftfile.py` and the API mode uses "a `Runner` constructed with an explicit workspace Path" — but never says whether these are the same underlying mechanism, whether the CLI's workspace is implicit (cwd?) versus the API's explicit Path, or what happens if they disagree.
Any how-to for either "author a task with file deps" or "embed weft" runs straight into this hole.

**Unowned decision gate.**
The "honest risk" paragraph sets a real go/no-go condition — the custom orchestrator is "justified only if the state-branching / alternative-precondition needs are genuine AND the core stays ~600–900 lines... else fall back to invoke."
This is exactly the kind of decision Step 4/5 of the tutorial says should get its own frozen record.
But the spec never says **who** evaluates this gate, **when** (a line count can be checked mechanically, but "needs are genuine" is a judgment call), or what document captures the answer.
It reads as a decision the spec is aware it owes but has not actually made — a dodge dressed up as honesty.

**The four "open design decisions" are named but not owned.**
Manifest granularity, concurrency model, AWAITING resumption, and the operator-overloading limit are each flagged as unsettled — but the spec gives no owner, no deadline, no process for resolving them, and no signal of whether they block adoption or can ship provisionally.
Listing open questions is good practice; leaving all four permanently open with no resolution mechanism is a spec dodging its own hardest calls.

**The rename is a landmine with no fuse.**
"weft" is explicitly a placeholder "to be renamed before adoption" — but adoption by whom, decided by whom, and what happens to every doc, import path, and Nexus package name written against "weft" in the meantime is entirely unaddressed.
If documentation gets written now (as this exercise just did), all of it is provisionally wrong the moment the rename happens, and the spec offers no versioning or migration story for that.

**RunReport's retention and status are unspecified.**
It's called "a per-run structured local log" living under `workspace/.weft/runs/` — but is it committed to version control, gitignored, rotated, size-capped?
Since a diagnosing developer's entire workflow depends on these reports existing when needed, this is not a cosmetic omission.

**No stability contract for the thing being embedded.**
The pitch to integrators is "no external binary, no daemon... a `Runner` constructed with an explicit workspace Path" — but nothing in the spec says whether `Task`, `Context`, `Runner`, or `State` are a stable public API, versioned, or subject to breaking changes at the maintainer's whim.
An integrator embedding weft inside their own library is taking on a dependency risk the spec never characterizes, despite spending a whole risk paragraph on the *maintainer's* risk (rotation) and none on the *integrator's* risk (API churn).

**No scope-defense process despite explicit non-goals.**
The spec lists clear non-goals (not a scheduler, not a daemon, not an observability platform, not a large build system) — good — but gives no process for what happens when someone asks for one of those anyway.
The tutorial's own "extend or contribute" activity implies this will happen; the spec has nothing for it.

**The Mermaid/docs-pipeline feeding is a dangling thread.**
"`graph` exports Mermaid, feeding a docs pipeline" names a downstream consumer without ever describing it: is it committed to the repo, regenerated in CI, published somewhere?
Without that, "docs pipeline" is a placeholder noun standing in for an entire undesigned system, quietly assumed to already exist.

**Bottom line on the spec:** it is candid about the risk that matters most to the author (a single maintainer, team-rotation risk) but silent or evasive on every risk that matters to someone *else* — the integrator's API stability, the adopter's rename exposure, the team's dependency on a doc pipeline that isn't described, and the four decisions it explicitly admits are still open.
Running the tutorial against it didn't invent these gaps; it just made them impossible to paper over, because Steps 2 and 5 both demand a real person and a real provenance for every document, and several documents this spec implies simply don't have either yet.
