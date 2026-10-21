---
title: "docsys commands reference"
force: describe
verb: specify
intention: state
view: synchronic
provenance: { type: function, id: codifying }
constitutive: no
audience: [user, contributor]
reader: H+M
distance: far
power: none
status: draft
---

## Scope

This page lists every command of [`docsys`](https://github.com/Skl8em/docsys), what it does and what it exits with, and how a project uses them.
The keys of `docsys.yaml` are in [`docsys-configuration.md`](docsys-configuration.md); what each check verifies belongs with the check.

## Using `docsys`

A project declares `docsys` as a development dependency and runs it from inside its workspace, the directory that holds `docsys.yaml`.
Two commands read the project: `docsys check` is the gate, and `docsys report` shows what the gate leaves out.
Four commands write for its author: they mint an identifier, seal a frozen record, move a document and name documents after their slug, so that the project's rules are met by a command rather than by hand.

Every command but `id`, and `seal` when it is given documents, finds its workspace as the nearest directory above the current one that holds `docsys.yaml`, or takes it with `--workspace PATH`.
A path given to a command is read from the current directory.

| Exit | Means |
| --- | --- |
| `0` | the command did what was asked, and nothing was left for the author to decide |
| `1` | it ran, and reports something the author must settle: a finding, a seal that no longer matches, a slug that cannot name a file |
| `2` | it could not run: usage, configuration, workspace, or a move that cannot be made, in which case nothing was changed |

## `docsys check`

Runs the checks `docsys.yaml` turns on, then the tools it names, and prints each finding as `path:line: rule: message — fix: the edit that clears it`.
It exits `1` when any finding is an error.
It takes `--workspace`.

## `docsys report`

Prints one line per exclusion of the scope, with its reason and the number of documents it leaves out, then the count of documents in scope.
`--documents` adds each excluded document with the exclusion that took it out.
It is not a gate: it exits `0` however many documents are excluded.

## `docsys id`

```text
docsys id [--at DATE | --order N] [--slug SLUG]
```

Prints a new ULID, 26 characters, sortable by its leading timestamp.
It needs no workspace: an identifier is minted before the document that carries it exists.

| Option | Mints |
| --- | --- |
| none | a ULID stamped with the present time |
| `--at DATE` | a chronological ULID stamped with `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SS`, read as UTC |
| `--order N` | an ordinal ULID whose timestamp is the sort key `N`, for records that are re-ordered |
| `--slug SLUG` | `<ulid>-<slug>`, a filename stem |

`--at` and `--order` exclude each other.
A date that cannot be read, or an order outside 48 bits, exits `2` with the reason.

## `docsys seal`

```text
docsys seal [PATH ...] [--frozen] [--reseal] [--print]
```

Writes the `hash:` line of a frozen record, the seal the fixity check verifies, as the last line of its frontmatter.
Give the documents to seal, or `--frozen` to seal every frozen record of the scope: a project's `diachronic` record whose `status` is `accepted`, `done` or `stable`.
Naming documents and `--frozen` together, or neither, exits `2`.

| Result | Meaning |
| --- | --- |
| `sealed` | the record had no seal, and has one now |
| `unchanged` | the record's seal already matches its content |
| `resealed` | `--reseal` replaced a seal whose record had changed |
| `already sealed, content changed` | the seal does not match and `--reseal` was not given: the file is not written and the command exits `1` |

Replacing a seal that no longer matches says the change was meant, so it takes `--reseal`; otherwise the command reports the record and leaves it as it is.
`--print` writes nothing: it prints `<seal>  <path>` for each document, which is the value a hand-written `hash:` line must hold.
A document with no frontmatter block, or, with `--frozen`, one whose frontmatter cannot be read, exits `2` naming it; a record is never taken for not frozen because its YAML failed.

## `docsys rename`

```text
docsys rename OLD NEW [--dry-run]
```

Moves a file or folder and rewrites the target of every relative link that pointed at it, or at anything under it.
It rewrites those links in the documents of the scope, and in each moved document wherever the scope puts it, whose own links it recomputes for the new folder.
An anchor, a link title, a leading `./` and a trailing `/` are kept, and a link the move does not affect is not touched.
Display text, and a path written in prose, are not links: the author revises them.

The move is `git mv` when git tracks `OLD`, and a plain rename otherwise; a workspace need not be a git repository.
`NEW` must not exist and must lie in the workspace, outside `.git` and not inside `OLD`; otherwise the command exits `2` with nothing changed.
`--dry-run` prints what would move and how many links would be rewritten, and changes nothing.
It prints `moved OLD -> NEW; rewrote N links in M files`.

A sealed record whose link is rewritten no longer matches its seal.
The command writes the rewrite, as for any document, and lists each such record with the command that renews its seal, `docsys seal --reseal PATH`: renewing a seal is the author's decision.
A project that would rather leave a frozen record untouched allows its dead link in `links.allow` instead.

## `docsys slugify`

```text
docsys slugify [--dry-run]
```

Renames each document that declares a `slug` and is not named after it to `<slug>.md`, in its own folder, through the same move as `docsys rename`, so every link follows.
A name the slug check accepts is left alone: the slug, or the slug and the document's `id` after a hyphen.
A document without a slug, outside the scope, or whose frontmatter cannot be read is left alone.

A slug that cannot name a file (not a string, or not hyphen-cased) is listed as skipped, and the command exits `1`.
A new name that already exists, or that two documents want, exits `2` before any rename: the plan is made whole first.
`--dry-run` lists the renames and makes none.
