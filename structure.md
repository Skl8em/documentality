---
title: "Structuring and keeping the documentation"
force: explain+mandate
verb: illuminate
formative: true
diataxis: explanation
view: synchronic
audience: [developer, AI, maintainer, archivist]
status: stable
written-at: v1
valid-for: v1
---

This document says **where to place documentation, how to organize it, and how long to keep it**. It first settles the question that governs all the others — a corpus serves two masters no single order satisfies — then derives the topology (docs with the project or in a separate repo), the reading tree, provenance, the state/change seam, the life cycle, and export. Passages marked **RULE** are binding; the rest explains why.

## 1. Two systems, never one

All documentation is pulled in two incompatible directions.

The first master is **communication**: a hurried reader, rarely an expert, must *find* what they came for and sometimes stumble on what they weren't looking for. Beneficiary: a present reader. Horizon: now.

The second master is **evidence**: one must later produce — before an auditor, a successor, or yourself in two years — what was decided, when, by whom, on what grounds. Beneficiary: a future examiner. Horizon: the long term.

These masters command opposite orders. The order that lets you *browse* by the shape of your need scatters the traces of one activity across the whole tree; the order that keeps those traces together buries what the reader came to find. "Organize the docs" is therefore not one task but two: the **communication system** (information architecture: a readable tree) and the **archival system** (records management: provenance). The root failure of most wikis is conflating them.

**RULE.** Never make one order carry both functions. A file has a reading place (the tree) *and* a provenance (the activity that produced it); these are not the same thing and do not coincide.

## 2. The topology already carries the distinction

Your two contexts are not two tooling choices: they are the material projection of the two systems.

**Docs with the project (in-repo).** The docs live in the project's git repo. This is the natural home of the **project's provenance**: the records that freeze (decisions, changelog, reports) belong to the project that produced them and are not rewritten. It is also the *local* synchronic surface: the README that orients, the `ARCHITECTURE.md` that explains, the reference.

**Separate docs repo + submodules.** A dedicated repo aggregates several projects, each mounted as a submodule. This is the home of the **cross-project communication system**: *one readable tree* (§4) organized by business function, above the projects. The decisive point:

> A submodule pinned to an exact commit **is** the archival bond (provenance + fixity) made material. It ties a synchronic reference — a current state, kept up to date — to a frozen, dated project state.

The state/change seam (§6) is therefore settled at the topology level: the docs repo carries the reader tree and the catalogue; each submodule anchors its project's frozen provenance.

**RULE (in-repo).** Docs that *describe or explain the project itself* and records *produced by the project* live in the project's repo.

**RULE (docs repo).** Docs that *federate several projects*, or that must reference an exact, verifiable state of a project, live in the docs repo and point to the project by a pinned submodule — never by copy or moving link.

The two contexts coexist: a project has its local docs *and* can be mounted in one or more cross-project docs repos. Nothing is duplicated: the cross-project layer *references*, it does not copy.

## 3. What belongs together: provenance, and its limit

Ask *which documents belong together*. Intuition says "those about the same subject." That's wrong. The right answer: **those that are traces of the same activity**. A change request, the decision it triggers, the test that validates it, the report that accounts for it belong together because they share a **provenance** — their juxtaposition *is* the evidence. Subject-based filing fails because a document serves several subjects and must then be duplicated or shelved arbitrarily; provenance does not, because a document has *one* activity that produced it even when it bears on several subjects.

Provenance has a limit that a multi-speed project hits fast: the rigid rule *one activity, one folder* does not survive scale, because teams and projects merge, split, and dissolve while the documents outlive them. The fix is to **separate the description of the records from the description of their context**, related by dated links rather than fused into one tree. Hence the distinction that makes provenance operable:

- **Function** — a permanent responsibility of the organization (reporting, a standing calculation, security). It does not end. Its docs are **synchronic**: kept current.
- **Project** — a bounded thing (a migration, a compliance effort). It closes. Its docs are **diachronic**: they freeze when the project closes.

A change touching three functions is not filed three times: its provenance is *the project* that produced it, and its bearing on the functions is a **relation**, not a location. A migration that ends while what it set in motion continues is no paradox: the project closes and its record freezes, the function it served carries on.

**RULE.** Each document declares in its frontmatter `provenance: {type: function|project, id: ...}`. A project record is not rewritten after closure; a function document is maintained.

## 4. Shelf and catalogue: the reading tree

Provenance organizes the archive, not the reading surface. Applying the archive's apparatus to the reader is the second great conflation: an ordinary reader does not think in faceted queries. Librarianship solved this by separating two devices:

- **The shelf** — each item has *one* place, only one, in an order chosen to make *browsing* possible: you look for one thing, meet its neighbours, find what you weren't seeking.
- **The catalogue** — many access points to the same item (by force, by audience, by function), for the reader who already knows what they want or is crossing criteria.

Both are needed; neither substitutes for the other. The reading surface therefore needs **one intelligible tree** (the shelf) *and* a catalogue over it. The catalogue is the frontmatter (`frontmatter.md`): its proper function is to **generate** readable indexes, not to serve as the interface. The reader browses hubs written for them; the machine, and only the machine, reads the tags.

Since a shelf admits one order, the whole difficulty concentrates in choosing its **axis**, governed by one principle: the order must fit the mental map of those who search. But communities do not search alike — a maintainer searches by component, an analyst by business function, an examiner by obligation. Choosing the axis means choosing the **dominant community** the surface serves.

**RULE.** Choose the tree's axis and dominant community explicitly, and write that choice at the top of the tree. Recommended defaults:

- **Cross-project docs repo** → axis by **business function** (the shared language of the organization), not by implementation.
- **In-repo docs of a code project** → axis by **component / builder's path**, because the dominant readers there are builders.

In-repo tree skeleton (the project's shelf):

```
README.md                 # orient — front door
docs/
  architecture.md         # explain — the why
  reference/              # describe — current state, kept up to date (synchronic)
  guides/                 # instruct — how-tos, runbooks
  tutorials/              # teach — learning paths
  decisions/              # decide — ADRs, frozen (diachronic)
  CHANGELOG.md            # account — frozen, append-only (diachronic)
CONTRIBUTING.md           # mandate — the rules
```

Cross-project docs-repo skeleton (the shelf by function):

```
README.md                       # orient — map of functions and projects
functions/                      # synchronic — current state per business function
  reporting/
  data-quality/
projects/                       # provenance — one pinned submodule per project
  migration-2026/    (submodule -> exact commit)
  onboarding-kyc/    (submodule -> exact commit)
archive/                        # diachronic — closed records, frozen
catalog/                        # indexes generated from frontmatters (do not hand-edit)
```

## 5. Two communities, two levels of context

`distance` (in the frontmatter) says how much code the reader shares, hence how much you must make explicit. `power` says whether they can sanction you, hence how defensible the document must be. These two settings decide *what rises into the cross-project tree*.

**RULE.** Do not pay the archival cost everywhere. A document whose life is a sprint (working note, draft) deserves neither the armor nor the scaffolding of an evidence dossier. Over-arming routine communication makes it illegible. See `writing.md` §IV.

## 6. The seam: state versus change

Almost every domain runs **two artifacts in parallel**:

- the document that states the present **state** ("here is how this works now") — **synchronic**, belongs to the function, kept current;
- the record that fixes a **change** ("here is what was altered, and why") — **diachronic**, belongs to the project, not rewritten, freezes.

A change *updates* the state document and *is filed with* its project. The two are joined but share neither place, life span, nor service. The asymmetry to remember: **backward**, the current state *is* the integral of the closed sequence of past changes and can in principle be re-derived from them; **forward**, it fails — a proposal weighing three possible futures is the integral of nothing (see `propose` in `writing.md`).

**RULE.** Mark each document's view: `view: synchronic` (state, maintained) or `view: diachronic` (change, frozen). The system's central discipline is to **keep the derived state honest to its authoritative changes**: when you change a state, the corresponding change is recorded (ADR, changelog entry) and not erased.

Concrete example:

- ✗ Editing `architecture.md` in place to reflect a new choice, with no trace of the prior choice.
- ✓ Writing an ADR (`decide`, frozen) that justifies the change, *then* updating `architecture.md` (`explain`, synchronic) which points to the ADR.

## 7. The life cycle: trajectory, not decline

A document's coordinates engender its trajectory: what **decides** freezes and is archived; what **commits** is re-issued in versions; what **describes** is maintained; what **proves** is re-run against its preserved inputs. A record is never truly "finished": it can always be drawn into a new use by a new actor (an audit requisitions a note written to coordinate colleagues). Do not pre-arm a routine document "in case of a lawsuit" — that destroys the very innocence that would give it evidential value.

**RULE (retention).** Each document type has an explicit retention rule. Recommended defaults:

| Type (force) | View | Retention |
|---|---|---|
| Decision (`decide`) | diachronic | permanent, never rewritten |
| Changelog / report (`account`) | diachronic | permanent, append-only |
| Proof / dossier (`prove`) | diachronic | per legal/contractual obligation |
| Reference, architecture (`describe`,`explain`) | synchronic | maintained while the function lives; archived version per release |
| Working note, draft | — | ephemeral; deleted or promoted, never left to sediment |
| Proposal (`propose`) | diachronic | frozen once decided; the ADR references it |

**RULE (wiki-in-decay diagnosis).** A corpus that sediments lacks three *independent* things, repaired independently: (a) a **provenance** (which activity is each doc a trace of?), (b) a **retention rule** (when does it die?), (c) a **tree chosen for a real community**. "The wiki is a mess" is not a diagnosis; those three lacks are.

## 8. Export and dissemination

The source is **Markdown / Quarto (.qmd)**. Everything else is a derived *dissemination package*: the same intellectual content exists as maintained source, as preserved version, and as disseminated copy (site, wiki, Word, ppt, PDF, xlsx). The source holds authority; the export is a convenience, never the reverse.

**RULE.** Never edit in the export target (no fixing directly in the wiki or the docx): the fix happens in the md/qmd source, then re-export. Otherwise the derived state drifts from its authority — exactly the failure §6 forbids.

The system stays **tool-agnostic**: each concrete project adapts its chain (Quarto, MkDocs, mdBook, Docusaurus, wiki, generic Pandoc). The minimal, tool-independent contract is **Pandoc**: every source file must remain convertible by `pandoc source.md -o target.{docx,pptx,pdf,html}` without depending on a particular generator. Concretely:

- Keep standard Markdown (CommonMark/Pandoc); reserve generator-specific extensions for files that will never be exported otherwise.
- The YAML frontmatter is readable by Pandoc *and* by the main generators: it is the pivot.
- Dissemination metadata (target audience, output format) is declared, not hard-coded into the content.

## In short

Always separate the two systems: a readable tree (one place per file, axis chosen for a community) for communication, provenance (function vs project) for the archive. The topology embodies them: in-repo docs for the project, docs repo + pinned submodules for the cross-project layer. Mark each file `view: synchronic|diachronic`, keep the state honest to its changes, give each type a retention rule, and export from the source without ever editing the target.
