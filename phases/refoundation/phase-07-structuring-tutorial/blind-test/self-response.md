# Applying the tutorial — a blind first run

I am meeting "Structure your project's documentation" for the first time.
The project I am applying it to is itself a documentation system — a theory plus an operational product for writing and structuring documents.
I am working only from the project spec I was given, not from the project's actual files.
Below is the tutorial's five steps, worked honestly, with real output for this project.

## Step 1 — Name the activities

The tutorial asks for recurring activities, each with the body of knowledge it draws on.
I went past the obvious "write the theory, use the product" pair and tried to find the ones I almost forgot.

| # | Activity (verb) | Knowledge it draws on |
|---|---|---|
| 1 | **Use** the product — document one's own separate project with its guidance, templates, schema | The documenter's own project domain; just enough of the product's conventions to follow a template |
| 2 | **Learn** the product on first contact — work through the tutorial once to decide if it fits | General documentation practice; explicitly *not* assumed to know the theory's vocabulary yet |
| 3 | **Develop/extend the theory** — write or rework the three essays | Philosophy of language, speech-act theory (illocution/perlocution), Ferraris's documentality |
| 4 | **Develop/extend the operational product** — write guidance, templates, the metadata schema | The theory itself (to stay faithful to it), technical-writing craft, YAML/Markdown/Pandoc conventions |
| 5 | **Maintain** — bring older parts still carrying pre-refounding vocabulary up to date | The project's own history, the new vocabulary, ordinary editing/git discipline |
| 6 | **Govern/decide** — record the project's own construction as dated decisions, grouped into phases, with a register and changelog | The project's own decision history, conventions for what counts as a decision worth recording |
| 7 | **Audit/verify** (dogfood) — check that the product's own docs are a worked example of its own theory | Both the theory and the current state of the corpus, held side by side |
| 8 | **Adopt/evaluate** — decide whether to use this system at all, versus another approach or none | Alternative documentation practices/tools, one's own project's needs |
| 9 | **Operate** (future, Phase II, not yet built) — an AI generates and validates documents from the metadata | The metadata schema semantics; whatever automation stack eventually exists — presently unspecified |

Two of these (1 and 2) are easy to collapse into a single "use it" line, and the spec itself does collapse them ("someone documenting their own project reads the product").
I kept them separate because the tutorial's own Step 3 later insists that a first encounter and an ongoing reference use have different needs and a different first document — collapsing them at Step 1 would have hidden that difference until it was too late to recover cheaply.
Activity 9 is named in the spec only as a future intention ("Phase II ... not yet built") — it is not yet a thing anyone does, only a thing the project says it will one day do.
I kept it in the list because the spec is explicit about it, but flag now that "recurring activity" is a strange fit for something that has never yet occurred.

## Step 2 — Who performs each, and their distance

| Activity | Person (role) | Distance |
|---|---|---|
| 1. Use the product | **Documenter** — someone with their own project to document | Novice in the theory's vocabulary and jargon (by design, should not need it); distance in their own project domain is theirs, not the product's concern |
| 2. Learn on first contact | **Newcomer** — a first-time reader deciding whether this fits, doing the tutorial once | Novice in the theory; novice, or at best casually initiated, in documentation-structuring practice generally. This is literally the role I am occupying right now. |
| 3. Extend the theory | **Theorist** (= the maintainer, one person, in this project's current state) | Deeply initiated — they wrote the essays |
| 4. Extend the operational product | **Product builder** (= same maintainer, different hat) | Initiated in the theory, but must simulate the Documenter's novice distance while writing for them |
| 5. Maintain / refactor vocabulary | Maintainer | Initiated — it is their own past work |
| 6. Govern/decide | Maintainer, as sole decision authority | Initiated — no one else currently holds this distance question |
| 7. Audit/verify | Maintainer, or conceivably an outside reviewer | Must be initiated enough to judge, yet also able to imagine the novice reader — an unusually doubled distance |
| 8. Adopt/evaluate | **Evaluator** — a prospective adopter comparing this against alternatives | Likely novice in the theory; initiated in the general practice of choosing among documentation approaches |
| 9. Operate (future) | The AI | Not a human role at all — "distance" as the tutorial defines it (shared vocabulary, initiated/novice) does not obviously apply to a machine reading a schema. Unresolved. |

The spec names only one human, "whoever develops it," across activities 3–7.
That is true today (small project, one maintainer) but it means five different distances collapse onto one person's changing hats.
Nothing in the tutorial tells you what to do when the same person is asked to hold five distances at once — I had to invent the "different hat" framing myself to keep the activities from blurring back together.

## Step 3 — What each person needs, and in what order

| Activity × person | First need | Then | Order rationale |
|---|---|---|---|
| Documenter (use) | **Do** — a template to follow for the document they're writing right now | **Know** — the metadata schema, when frontmatter is due | Task-shaped: they came in with a document to produce, not a question about foundations |
| Newcomer (learn) | **Orient** — what is this, is it for me | A guided **how-to** (a tutorial to run once) | Matches the tutorial's own claim: first-run/install-type encounters want the how-to early, not last |
| Theorist (extend theory) | **Orient** — where the theory was left | **Why** — prior essays and decisions, so as not to contradict earlier commitments | Consistent with the tutorial's "returning after three months" case |
| Product builder (extend product) | **Know/Why** — current theory and current guidance, as ground truth | **Do** — write the new guidance | Must not duplicate or silently contradict what already exists |
| Maintainer (vocabulary refactor) | **Orient** — a diff of old vs. new vocabulary | **Do** — a checklist of what counts as current wording | Needs to know what "current" means before touching anything |
| Maintainer (govern/decide) | **Orient/Why** — existing register and past decisions | **Decide** — record the new one | Can't add a decision responsibly without seeing the log it joins |
| Auditor (dogfood) | **Why** — theory and corpus held together for comparison | (no clean second need — this is inherently a comparison, not a linear order) | The tutorial's know/do/decide triad does not fit this activity cleanly — see review |
| Evaluator (adopt) | **Orient** — what this is, what it costs to adopt | **Why** — comparison/rationale before any "do" | Decision-support need, not a task need |
| AI (operate, future) | **Know** — the schema, as machine-readable ground truth | Nothing further specified | Deferred; nothing else exists to write yet |

Worth flagging: the Newcomer's "how-to first" and the Theorist/Maintainer's "orient/why first" split maps suspiciously neatly onto the tutorial's own worked prediction in Step 3.
That is either a genuine confirmation that the method works, or a sign that I unconsciously fitted the project's activities to match the tutorial's own example rather than deriving them independently — I cannot fully rule out the second reading, since the spec was written under the same theory I am now testing.

## Step 4 — Start together, then split at real seams

The tutorial says: open one README, split only when a seam actually bites.
I could not honestly do this move.
The project spec already hands me a decomposition — theory essays, WRITING guidance, STRUCTURING guidance, a METADATA SCHEMA, GOVERNANCE and RECORDS — described as what the project is "made of," in the present tense, already refounded.
This is not a greenfield project the tutorial can walk me into gradually; it is a mid-refactor project with existing seams I am being asked to re-derive after the fact.
So Step 4 became a check of the given seams against the tutorial's three tests, rather than a live discovery:

- **Theory vs. operational guidance** — a real seam on two counts: divergent lives (the theory is closer to a stable foundation; the guidance is a living, frequently-edited reference) and a distinct community (the Theorist's initiated audience vs. the Documenter's deliberately novice-facing audience).
- **Writing guidance vs. structuring guidance** — same audience (the Documenter), different task (write one document vs. structure a corpus).
  The tutorial does not license a split on "different task" alone, only on size or divergent life or distinct community.
  I kept them split because the spec describes each as substantial (move structures, failure modes, templates on one side; provenance, state/change seam, scale/recursion, this tutorial on the other) — a size argument, but a soft one, not the tutorial's clean case.
- **Metadata schema as its own piece** — justified by a genuine divergent-life argument: it is the one artifact meant to eventually be read by a non-human (the future AI operator), which is a distinct future community the other guidance does not have.
- **Governance/records vs. everything else** — the strongest seam of all, and the tutorial's paradigm case: individual decision records freeze once dated, while guidance and theory stay current. This is explicitly named in the spec ("dated decision records ... grouped into phases, with a central register and a changelog"), so it is also a case the tutorial's own vocabulary (frozen vs. current) fits without strain.

Net effect: Step 4 mostly validated a split that already existed rather than producing one from scratch.
That is a legitimate outcome — the tutorial says structure can be "regrouped later," implying it also tolerates being checked later — but a first-time user should know going in that the "start with one README" instruction will feel inapplicable to any project past its very first day.

## Step 5 — Where things go: provenance, current vs. frozen

| Document | Provenance (which Step-1 activity produces/maintains it) | Current or frozen | Root (surface) or docs/ (internal) |
|---|---|---|---|
| README | The product-building / orienting activity, on behalf of Documenter + Newcomer | Current (permanent activity) | Root — it's the surface where the Documenter and Newcomer first meet the project |
| Theory essays (×3) | Extend-the-theory activity | Current for now (project is "recently refounded," theory still actively worked) — but a strong future-freeze candidate once the theory stabilizes | docs/ — not needed to produce one how-to; consulted by Theorist, Product builder, Auditor |
| Writing guidance | Develop-the-operational-product activity | Current | docs/ — but close to the surface, since the Documenter is its direct audience |
| Structuring guidance (incl. this tutorial) | Same as above | Current | docs/ |
| Metadata schema | Develop-the-operational-product activity, shared dependency of writing + structuring + (future) operate | Current, but versioned carefully since Phase II will depend on it | docs/ — a shared reference, arguably deserving its own top-level slot rather than living inside writing or structuring alone |
| Governance / decision records | Govern-and-decide activity, plus the maintenance activity that keeps the register/changelog current | Register and changelog: current (append-only). Individual dated records: **frozen** the moment they're made, per phase | docs/ — internal record of the project's own construction, not something the Documenter needs to read to use the product |
| Phase II material (AI-operates) | No activity currently performs this — it is anticipated, not yet enacted | Cannot be classified current/frozen; there is no provenance yet | Nowhere yet — a genuine gap, see review |

The root-vs-docs/ split falls out cleanly here: the project's own "users" in the tutorial's sense are the Documenter and the Newcomer, so the surface they meet (README, and the near-surface parts of writing/structuring guidance) belongs at or near root; the project's internal records of its own construction (theory-as-foundation, governance, decisions) sit apart in docs/, exactly as Step 5 predicts.

One aside, held at arm's length since I was told to stay blind to the rest of the repository: the file path I was handed to write this response into implies an actual layout of `docs/phases/phase-07-structuring-tutorial/...` — a flat, phase-indexed scheme, rather than the theory/writing/structuring/schema/decisions grouping I derived above from the spec text alone.
I am not treating that path as evidence (I was told not to go looking), but I note the apparent mismatch honestly rather than quietly smoothing it over.

## Proposed documentation structure

```
README.md                                  # orient: what this is, who it's for (Documenter, Newcomer)

docs/
  theory/
    01-inscribed-act.md                    # coordinate theory of the inscribed act
    02-stances.md                          # rhetoric of writers' stances
    03-documentary-system.md               # documentary system / corpus keeping

  writing/
    stances-and-forces.md                  # one stance per illocutionary force
    move-structures.md                     # move structure + failure mode per force
    templates/                             # reusable templates
    readability-patterns.md                # patterns for humans and language models

  structuring/
    provenance-and-shelf.md                # source shelf ordered by provenance
    state-change-seam.md                   # current vs frozen
    scale-and-recursion.md
    this-tutorial.md                       # the guided-start tutorial itself

  schema/
    metadata-schema.md                     # the frontmatter catalogue

  decisions/
    register.md                            # current, append-only index
    changelog.md                           # current, append-only
    phase-00-.../                          # frozen, dated records, grouped by phase
    phase-01-.../
    ...
```

This tree is offered as a consequence of Steps 1–5, not as a template applied on top — but see the review for how much of that derivation was really live versus rubber-stamping a decomposition the spec had already made.
