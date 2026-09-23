---
title: "T1(b) — the engine/config seam, drawn"
force: explain
intention: state
constitutive: no
view: synchronic
provenance: { type: project, id: phase-12-codifying }
audience: [contributor]
reader: H+M
status: draft
---

`plan.md` T1(b): classify every script as generic engine or repo-specific, and move the repo-specific values out of `scripts/` so the tooling could be extracted later at low cost.
This document records the classification, what moved and where, what was found on the way, and what deliberately stayed.
Extraction itself remains out of scope; this step makes it cheap, it does not perform it.

## The seam: three homes, by rate of change

The plan offered "the rules file or a small config".
Both are used, for different reasons, and a third category had to be named.

| Home | What lives there | Test |
| --- | --- | --- |
| **engine** — `scripts/`, `tools/markdownlint/` | behaviour any project using this documentation system would run unchanged | a second project would not edit it |
| **methodology** — [`schema/frontmatter-rules.yaml`](../../../schema/frontmatter-rules.yaml) | the frontmatter vocabulary, its enums, each optional field's rationale | shared by every instance; changes rarely, by a ruling |
| **instance** — [`docsys.yaml`](../../../docsys.yaml) | where this repo keeps its schema, which documents are out of scope, what its decision register looks like, which checks make up its gate and in what order | a second project would replace it wholesale |

The instance values went to a new file, not into the rules file, because the two change at different rates and for different reasons.
An ignore prefix such as `theorising/` is a fact about this repository's history; a `force` enum is a claim of the theory.
Putting both in one file would have made every layout change look like a schema change, and would have shipped this repo's history to any adopter of the schema.

`docsys.yaml` is read only through [`scripts/docsys_config.py`](../../../scripts/docsys_config.py).
Its vocabulary is closed, like the frontmatter's: an unknown section or key is an error, and every refusal names the file, the key and the fix, because the gate's reader is often a machine with no other context.

## What moved

| Was | Was in | Now |
| --- | --- | --- |
| `IGNORE_PREFIXES`, `IGNORE_SUBSTRINGS` | `frontmatter_lint.py` | `frontmatter:` in `docsys.yaml`; `ignored(path, scope)` takes the scope as an argument |
| `REGISTER_PATH` | `ulid_check.py` | `register.path` |
| the register's row shape: five cells, ordinal in the first, status in the fifth, the first cell a numbered link to the record, "superseded by N" | `ulid_check.py` (`REGISTER_ROW_RE`, `SUPERSEDED_BY_N_RE`, two magic indexes) | `register.columns`, `ordinal_column`, `status_column`, `ordinal_pattern`, `superseded_pattern` |
| the hard-coded check list and its order | `check.py` | `checks:`, each entry carrying its ordering rationale as a comment; `check.py` is now only the runner |
| the schema's two paths | `generate_schema.py`, `frontmatter_lint.py` | `schema.source`, `schema.generated` |
| the docstring enumerating the eleven checks | `check.py` | removed — a second copy of the list that could only drift; the docstring now points at `docsys.yaml` |

The register's format is now expressed as data, and `test_ulid_check.py` proves it by running the engine against a second register shape (four columns, status third, "replaced by") that is not this repo's.

## Classification of every script

| Script | Class | Instance coupling, moved or remaining |
| --- | --- | --- |
| `check.py` | engine (runner) | check list **moved**; remaining: the Nix devShell contract (see below) |
| `docsys_config.py` | engine | new; the single reader of `docsys.yaml` |
| `yaml_frontmatter.py` | engine | none |
| `ulid.py` | engine | none |
| `linkcheck.py` | engine | none |
| `generate_schema.py` | engine | schema paths **moved** |
| `frontmatter_lint.py` | engine, for this methodology's schema | scope and schema path **moved**; remaining: methodology coupling (below) |
| `ulid_check.py` | engine | register path and format **moved**; remaining: the field names `supersedes` / `superseded-by` |
| `slug_check.py` | engine | remaining: the ADR-028 convention itself (filename stem is the slug) |
| `hash_seal.py`, `hash_check.py` | engine | remaining: the definition of a *frozen* record (below) |
| `rename_doc.py`, `slugify_names.py` | engine | a hard-coded sibling-script path **fixed** (below) |
| `migrate_ids.py` | **repo-specific, one-shot** | bakes in `phases/`, `ADR-NNN-slug.md`, `phase-NN-slug/` and the phase ordering gap; not part of the gate |
| `test_*.py` | fixtures for the script beside them | `test_seam.py` holds the seam itself |
| `tools/markdownlint/` | engine (a custom rule) | configured by `.markdownlint-cli2.jsonc`, which cannot read `docsys.yaml` |

`migrate_ids.py` is the only script that is repo-specific rather than merely configured.
It stays in `scripts/`: it is a documented, deliberately kept tool, and moving it would strand the prose that names its path in records that are frozen and must not be edited.
It was not made configurable, because that would mean inventing a naming-convention language for a tool with no second use — the speculative abstraction the engineering contract rules out.
An extraction would leave it behind or carry it as an example.

## What deliberately stayed, and why

These are couplings the plan did not list and that are not a path, a prefix or a register format.
Naming them is the point: the seam is honest only if its residue is visible.

- **Methodology coupling in the linter.**
  `frontmatter_lint.py` is not a generic YAML linter.
  It encodes the schema's *shape* — that a `direction_of_fit` table must partition `force`, that `register` is derived and never stored, that the root document is `README.md` and carries `axis` and `dominant-community`.
  What extracts is engine plus methodology together; the seam separates them from the instance, not from each other.
- **The definition of a frozen record** (`hash_seal.py`): `view: diachronic`, `provenance.type: project`, and `status` in `accepted` / `done` / `stable`.
  That is schema semantics living in code, and its status list duplicates `warn_enums.status` in the schema, so the two can drift.
  The natural home is the schema; moving it widens the schema's vocabulary, which is a ruling to make on purpose, not a side effect of a refactor.
- **The Nix devShell contract**: `DOCSYS_DEVSHELL`, `nix develop --command`, the pinned-tool fallback.
  It is environment, a third kind of thing that is neither engine behaviour nor instance layout.
  A project without Nix would replace `pinned_tool_cmd`, and no config key would express that.
- **A second copy of the out-of-scope list.**
  `.markdownlint-cli2.jsonc` keeps its own ignore list — wider, since it also covers `imagining/**`.
  markdownlint reads only its own config, so the two cannot be unified.
  "Which documents are out of scope" therefore lives in two places, and nothing checks that the linter's list is contained in the other's.

## Found on the way

- **Sibling paths hard-coded.**
  `rename_doc.py`, `slugify_names.py` and `migrate_ids.py` ran `scripts/linkcheck.py` or `scripts/check.py` by repo-relative path, and `check.py` re-executed itself as `scripts/check.py`.
  An engine that assumes its own directory's name is not relocatable; each now resolves siblings from its own location.
  `test_seam.py` surfaced the ones that named a configured script; the rest were found by reading for the same shape.
- **A silent skip the seam would have created.**
  `ulid_check.py` ran the register cross-check only `if REGISTER_PATH in records`.
  With the path a constant that guard was inert; with the path in config, a typo would have switched the whole cross-check off without a word.
  It is now an error, with a fixture (`check_register_file`).
- **A register that yields no rows still passes.**
  Not introduced here and not fixed: if the configured row shape matches nothing, `parse_register` yields nothing and the check is green.
  The same silent-fallback shape as the previous point, one level down; a candidate for T3's or a later hardening pass.

## How the seam is held

`scripts/test_seam.py` is the second entry of the gate (after the worktree check), so a violation is reported ahead of the checks that read the configuration.
It does not stop them: the runner runs every check, so a leaked value fails the gate through this entry alone, while a malformed configuration also fails the checks that load it ([`codifying/gate.md`](../../../codifying/gate.md)).
It checks three things: the real `docsys.yaml` validates; malformed configurations are refused with a message naming the key and the fix; and no instance value from `docsys.yaml` — a path, a prefix, a script name — appears as a string literal in the engine's code.
The third check parses each script and skips docstrings, which are prose; the values to look for are read from the config itself, so a new instance value extends the check without anyone remembering to.
The definition of done's grep for the old constants (`IGNORE_PREFIXES`, `REGISTER_PATH`, `steering/ADR.md`, …) comes back empty over `scripts/*.py`.

## What this does not establish

The seam is drawn from one instance.
`test_seam.py` proves the dependency runs one way — the engine does not know the instance — not that the boundary sits in the right place.
Only a second consumer, or the seam holding unchanged for a full phase, would show that; both are the extraction triggers `plan.md` already names.

## What this hands to T1(c)

The maintainer fiches should describe `docsys.yaml` as the place a maintainer changes what the gate checks and where the register lives, and the residue above as the places where a change still touches code.
The gate-architecture fiche in particular can now cite the `checks:` list as the source of the sequence, rather than restate it.
