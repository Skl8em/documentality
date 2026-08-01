---
title: "Phase 09 tooling — the detailed plan"
force: propose
verb: argue
register: govern
intention: suasive
view: synchronic
provenance: { type: project, id: phase-09-tooling }
concerns: [steering, writing, structuring, theorising, imagining]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

The plan for Phase 09, in enough detail to execute.
It is a proposal, not diffs: each part states the goal, the concrete approach and files, the decisions to make, and how it is verified.
Three parts — **markdownlint**, **frontmatter linting**, **ULID + slug identifiers** — plus the **integration** that ties them into one gate.

## Why tooling before the schema

Phase 10 reconciles the frontmatter schema (fields, allowed values, the two open ⚑).
Doing that *by hand* across the corpus is slow and error-prone; doing it against a **validator** is fast and checkable.
So Phase 09 builds the harness first — the linters and the identifier scheme — and Phase 10 fills the schema into it.
This is also why the frontmatter validation here is a **safe starter**: it enforces only what is already settled, leaving the contested fields as warnings the schema phase will turn into rules.

## Guiding principles

- **One ruleset, two surfaces.** The CLI and the VSCode extension must apply *the same* markdownlint configuration and custom rules — never two drifting copies.
- **Python for our validators, Node only for markdownlint.** Markdownlint is David Anson's engine, shared with the editor extension, so it runs on Node; that is unavoidable and desirable. Everything we write ourselves (frontmatter, ULID, links) stays Python, per the project's validation-tooling convention and the existing [`../../../scripts/linkcheck.py`](../../../scripts/linkcheck.py).
- **One gate.** Every check is reachable from a single command that runs in pre-commit and in CI, and is the phase-close gate.
- **Enforce only what is decided.** A linter that flags an open question trains people to ignore it. Contested rules warn; settled rules fail.

## Part 1 — Unified markdownlint (CLI == VSCode)

### Goal

The CLI and the `DavidAnson.vscode-markdownlint` extension apply one shared ruleset, which:

- requires the document **title in the frontmatter**, and forbids a Markdown `# …` H1;
- enforces the **semantic-line-break** rule (one sentence per line — no hard break before a sentence ends), per [ADR-021](../phase-06-refoundation/ADR-021-line-breaks.md);
- **takes over the default** markdownlint ruleset with an explicit, reviewed configuration.

### Approach

Use **`markdownlint-cli2`**, which reads the same `.markdownlint-cli2.jsonc` (and `.markdownlint.jsonc`) that the VSCode extension reads.
The extension also supports `customRules`, so a custom rule module is shared by both surfaces.

Files to add at the repo root:

- `.markdownlint-cli2.jsonc` — the config: `config` (built-in rule settings), `customRules` (our rule modules), `globs`, and `ignores` (`theorising/**` if the essays are exempt, plus anything generated).
- `.markdownlint.jsonc` — the built-in rule block, referenced by the above, so the CLI and extension share exactly one rule set.
- `tools/markdownlint/sentence-per-line.js` — the custom rule (below).
- `.vscode/settings.json` — pin `"markdownlint.configFile"` and `"markdownlint.customRules"` so the editor loads the same rules; optionally disable the editor's bundled defaults in favour of ours.
- `.vscode/extensions.json` — recommend `DavidAnson.vscode-markdownlint`.
- `package.json` — one devDependency (`markdownlint-cli2`) and a script `"lint:md": "markdownlint-cli2"`.

### The two special rules

**Title in frontmatter, no body H1.**
Built-in rules do most of this by configuration:

- `MD025` (single-title/heading) with `front_matter_title` set to a regex matching the YAML `title:` key — this makes markdownlint treat the frontmatter title *as* the document title, so any `# …` in the body is flagged as a second title.
- `MD041` (first-line-heading) with the same `front_matter_title` — satisfied by the frontmatter title, so a document is not required to open with `#`.
- A small guard in the custom-rule module (or `MD025` config) to forbid **any** level-1 heading in the body, since the title lives in the frontmatter.

A separate check that the frontmatter *has* a non-empty `title` belongs to Part 2 (the frontmatter linter), not markdownlint.

**Semantic line breaks (ADR-021).**
There is no built-in rule for this, so we write a custom markdownlint rule, `sentence-per-line`:

- It inspects paragraph text tokens only, skipping headings, code blocks/spans, tables, HTML comments, link/image destinations, and YAML frontmatter.
- It flags a **hard break inside a sentence** (a line that does not end at a sentence boundary and whose next line continues the sentence) and a **sentence boundary mid-line** (a `.`/`!`/`?` followed by whitespace and more text on the same line).
- It carries a configurable **abbreviation allow-list** (`e.g.`, `i.e.`, `cf.`, `vs.`, `etc.`, `No.`, single-initial patterns) and ignores decimals, ellipses, and URLs, to keep false positives low.
- It is a **heuristic**; ADR-021 is the spec, and the allow-list is tuned on this repo before it is turned from warning to error.

### Take over the defaults

Provide an explicit config rather than inheriting silent defaults. Notable overrides:

- **`MD013` (line length): off** — semantic line breaks make lines as long as a sentence; a length cap contradicts the house style.
- **`MD060` / table pipe style:** pick one (compact vs padded) and set it, since the current corpus mixes them (the warnings seen throughout Phase 08).
- **`MD024` (duplicate headings):** allow same-text headings under different parents if our templates need it (`siblings_only`).
- **`MD033` (inline HTML):** allow the `<!-- … -->` template comments and any needed spans.
- Review the full default list once and record the on/off decision for each in the config, commented.

### Verification

- `npx markdownlint-cli2` exits clean on the whole corpus (after the corpus is brought into line — expect a one-off cleanup pass).
- Opening any file in VSCode shows the **same** diagnostics (proving parity).
- The `sentence-per-line` rule flags a deliberately mis-wrapped test fixture and passes on a correct one.

## Part 2 — Frontmatter linting (safe starter)

### Goal

A Python validator that checks the **settled** frontmatter invariants across every catalogued document, exits non-zero on violation, and is the seed the Phase-10 schema fills in.
It runs the contested fields as **warnings**, so the schema phase can see the current spread without the linter crying wolf.

### Approach

- `scripts/frontmatter_lint.py` — parse YAML frontmatter from each `git ls-files '*.md'`, validate, and report `file:line` diagnostics; derive the repo root from git, like `linkcheck.py`.
- `schema/frontmatter.schema.yaml` — the rules **as data**, so Phase 10 edits one file, not the validator. Start minimal; grow in Phase 10.
- Reuse the existing YAML/link tooling patterns; no new heavy dependency (stdlib + a small YAML parser, or vendor a tiny one).

### What is safe to enforce now (errors)

- `title` present and non-empty.
- The seven required fields present: `force`, `intention`, `view`, `provenance`, `audience`, `reader`, `status`.
- `provenance` is a map `{type, id}` with `type ∈ {function, project}` and a non-empty `id`.
- `view ∈ {synchronic, diachronic}`.
- `force` is one of the twelve (composites `a+b` allowed).
- `reader ∈ {H, M, H+M}`.
- `audience` is a non-empty list.
- Tree-root rule: exactly the root `README.md` carries `axis` + `dominant-community`; no other file does.

### What stays a warning (deferred to Phase 10)

- `intention` **coarse vs fine** — accept *both* value sets for now (⚑ Decision 1).
- `register` **stored vs derived** — do not require it; do not forbid it (⚑ Decision 2).
- `distance` / `power` allowed values, and `concerns` shape — surface, do not reject.
- Force × intention "typical" pairings — surface unusual pairings, never fail (consistent with `writing/frontmatter.md`).

### "As examples"

Prove the harness on a handful of exemplar files first (one per force / provenance kind), then run the safe rules across the whole corpus.
The point is the *machinery*, wired into the gate, so Phase 10's schema decisions become one-line edits to `frontmatter.schema.yaml` plus a validator that already runs everywhere.

### Verification

- `python3 scripts/frontmatter_lint.py` exits clean on the safe rules over the whole corpus.
- Its warning output is captured as the **input catalogue for Phase 10** (the current spread of the contested fields).

## Part 3 — ULID + slug identifiers

### Goal

Replace the sequential counts (`ADR-027`, `phase-08`, and any other ordinals used as identity) with a **ULID** (time-sortable, globally unique, 26-char Crockford base32) plus a human **slug**, and provide tooling to mint and to verify them.

### Why ULID

A count is a bottleneck and a merge-conflict magnet, and it bakes ordering into the name.
A ULID is unique without coordination, sorts by its leading timestamp, and pairs with a slug for human legibility — `01J9Z…K3-gerund-naming` instead of `ADR-027`.

### Two minting modes — chronological vs ordinal

Not every count means the same thing, so the ULID's timestamp field is fed differently for each.

- **ADRs are append-only and chronological.** Their order *is* their creation order, so their ULID takes the **real creation timestamp** (the record's first-commit time). Nothing to steer.
- **Phases carry an *intentional* order we deliberately rearrange.** We just inserted tooling between refactor and schema-reconciliation; a wall-clock ULID would sort tooling *after* both and destroy the sequence. So a phase's ULID takes a **controlled ordinal key** as its timestamp input, not the wall clock.

The mechanism: a ULID sorts lexicographically by its 48-bit timestamp prefix, so we feed that prefix a **sort key we own**.
Each phase stores an explicit `order` value in its frontmatter, and the ULID's timestamp bits are derived from it.
To insert a phase between two neighbours, pick an `order` strictly between theirs — refactor `= x`, schema `= y > x`, tooling `= z` with `x < z < y` — and mint from `z`.
To keep insertion room, space the initial `order` values with gaps (multiples of a large constant) and insert at the midpoint; if a gap is ever exhausted, a one-line `rebalance` re-spreads the keys (rare — phases are few).
The `order` field is the human-editable source of truth; the ULID is its stable, unique encoding.
The two modes never sort against each other (you never list ADRs and phases in one ordering), so ADRs keep real times and phases keep synthetic ones without conflict.

### Decisions to make (options + recommendation)

- **D-a — canonical id location.** Add `id: <ULID>` to frontmatter as the canonical identity; keep a human `slug`. **Recommend: yes** — `id` is the stable machine key; the slug and the display name stay human.
- **D-b — filenames.** (i) `<ulid>-<slug>.md` (globally unique, time-sortable, but long/ugly); (ii) keep `<slug>.md`, ULID only in frontmatter; (iii) hybrid — records (ADRs, open items) get `id` in frontmatter and keep readable slug filenames, phase folders keep their readable `era/phase-slug` names and gain an `id`. **Recommend: (iii)** — machine identity in frontmatter, readability in the tree; revisit if a flat, sortable record store is ever wanted.
- **D-c — keep a human ordinal?** The ADR register can show a **generated** monotonic index from ULID time-order (derive, don't store), so humans still see "the 27th decision" without a stored count. **Recommend: yes, generated.**
- **D-d — cross-references.** Keep human relative links for *reading* (they already resolve and pass `linkcheck`), and add `id` as the stable key a generated index maps to a path, for *machine* reference and for surviving future renames. **Recommend: both — links for humans, `id` index for machines.**
- **D-e — phase ordering.** Store an explicit `order` sort-key in each phase's frontmatter, feed it into the phase ULID's timestamp bits, and space the initial values with gaps for midpoint insertion (the two-minting-modes section above). **Recommend: yes** — the `order` field is the source of truth; ADRs keep chronological ULIDs, phases keep ordinal ones.

These five are the open forks; they are named here and decided at the start of Phase 09 execution (a short ADR).

### Tooling (Python)

- `scripts/ulid_new.py` — mint a ULID, with the timestamp field taken from an input so both modes are supported: `--at <iso>` for **chronological** records (ADRs; default = the git first-commit time, else now) or `--order <int>` for a **controlled ordinal** (phases, from their `order` field). Implement the spec directly (48-bit timestamp + 80-bit randomness, Crockford base32, excluding `I L O U`), or pin a tiny vetted dependency.
- `scripts/ulid_check.py` — verify: every catalogued record has an `id`; each `id` is a syntactically valid ULID; **uniqueness** across the corpus; the `id` agrees with the filename if D-b picks a ULID-in-filename; **no orphan count-references** remain (a grep gate for `ADR-\d+`, `phase-\d\d` outside intended historical prose); and, for phases, that the ULID order **agrees with the declared `order` field** (no drift) and that `order` values are unique.
- `scripts/migrate_ids.py` — the one-off migration. **ADRs:** a ULID whose timestamp is the record's first commit (`git log --follow --diff-filter=A --format=%aI`), so order matches real history. **Phases:** a ULID from a gap-spaced `order` derived from the current intended sequence (…, refactor, tooling, schema, Phase-II-design, …), *not* wall-clock — preserving the deliberate order through the insertion we just made. Write `id` (and, for phases, `order`) into frontmatter; rewrite the ADR register and cross-references; emit an `old-id → new-id` map for rollback.

### Migration sequence (reversible)

1. Decide D-a…D-d (short ADR).
2. `migrate_ids.py` produces the map and the edits on a branch.
3. Run `linkcheck.py` + `ulid_check.py` + `frontmatter_lint.py` — all clean.
4. Review the diff; keep the map for rollback.
5. Establish the forward workflow: new records call `ulid_new.py`; the register index is generated.

### Verification

- `ulid_check.py` clean (valid, unique, present, no orphan counts).
- `linkcheck.py` clean after any renames.
- The ADR register renders a generated ordinal, with no stored count.

## Integration & workflow

- **Aggregator** — `scripts/check.py` runs, in order: `markdownlint-cli2`, `frontmatter_lint.py`, `ulid_check.py`, `linkcheck.py`, and exits non-zero if any fails. This *is* the phase-close gate.
- **Pre-commit** — a `.pre-commit-config.yaml` (or a committed git hook) invoking `scripts/check.py`, so violations are caught before they land.
- **CI** — one job running `scripts/check.py` (only if/when the repo has a remote; the aggregator is the same locally and in CI).
- **VSCode** — `.vscode/extensions.json` recommends the markdownlint extension; `.vscode/settings.json` pins the shared config and custom-rule path; an optional task runs the Python checks from the editor.
- **Two runtimes, kept minimal** — one Node devDependency (`markdownlint-cli2`) for the shared lint engine; everything else Python and stdlib-only where possible.

## Proposed workstreams for Phase 09

| # | Workstream | Output |
|---|---|---|
| **T1** | Markdownlint config + `sentence-per-line` custom rule + VSCode wiring; one-off corpus cleanup | `.markdownlint*.jsonc`, `tools/markdownlint/`, `.vscode/`, `package.json` |
| **T2** | Frontmatter lint harness (safe invariants) + schema-as-data | `scripts/frontmatter_lint.py`, `schema/frontmatter.schema.yaml` |
| **T3** | ULID scheme ADR (D-a…D-d) + mint/verify/migrate tooling + migration | `scripts/ulid_*.py`, the migration, an ADR |
| **T4** | Integration: aggregator, pre-commit, CI, VSCode tasks | `scripts/check.py`, `.pre-commit-config.yaml`, CI |
| **T5** | Close-out: mark Phase 09 done; record decisions; hand the harness to Phase 10 | records updated |

## Definition of done

- CLI and VSCode markdownlint apply one ruleset; the corpus passes it; title-in-frontmatter and semantic-line-breaks are enforced.
- `frontmatter_lint.py` enforces the safe invariants and warns on the contested ones; the warning catalogue is handed to Phase 10.
- Every record carries a valid, unique ULID `id`; the sequential counts are gone (or generated for display only); `ulid_check.py` is clean.
- `scripts/check.py` runs all four checks as one gate, in pre-commit and CI.

## Open questions routed out of this plan

- The five ULID decisions D-a…D-e (settled by a short ADR at the start of execution), including phase ordering via an explicit `order` key.
- Whether pre-commit is adopted now or left as a documented opt-in.
- Whether `frontmatter_lint.py` should emit an editor-consumable format (SARIF / VSCode Problems) — nice-to-have, not required for the gate.
