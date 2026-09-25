---
title: "T1(c) — the gate's messages, audited against the machine reader"
force: explain
intention: state
constitutive: no
view: synchronic
provenance: { type: project, id: phase-12-codifying }
audience: [contributor]
reader: H+M
status: draft
---

`plan.md`'s definition of done asks that the gate's error messages be "checked against the machine reader: each names the file, the rule and the fix without needing the surrounding context".
[`community-map.md`](community-map.md) puts that reader in the map — `reader: M`, far always, "each message is the whole interaction" — and hands the check to T1(c).
This is the check, what it found, and what it left.

## The standard

A line a validator prints for a failure carries three things, in the line itself:

1. **where** — the file, and the line when the failure has one;
2. **the rule** — what is wrong, stated so it needs no other line;
3. **the fix** — the edit or the command that clears it, after a `— fix:` marker.

The marker is structural on purpose.
A test can look for it; it cannot look for "a helpful sentence".
The header a check prints above its lines (`ULID ERRORS: 3`) is shared context a machine may not see, so it does not count toward any of the three.

## What the audit found

| Where | Verdict before | Change |
| --- | --- | --- |
| `frontmatter_lint.py` — every error | file and rule present; **fix absent** for all but two (`register` stored, closed vocabulary) | `— fix:` added to each; an enum failure now says "use one of them", a hash mismatch names the re-seal command |
| `frontmatter_lint.py` — the two schema-load refusals | rule present, fix absent | fix added; they name the schema source through the configuration, not a literal |
| `ulid_check.py` — dangling, asymmetric, register disagreement, duplicate or malformed `id` | file and rule present; **fix absent** | `— fix:` added; a register message names the register's configured path |
| `slug_check.py` — three messages | same | same; the rename fix names the tool that rewrites the links |
| `linkcheck.py` | file, line and target present; the rule ("no such file") and the fix were **both implicit** | both stated on the line |
| `hash_check.py` | fix present, but once in a trailer rather than on each record's line | the fix moved onto each record, with that record's path in the command |
| `generate_schema.py --check` | file, rule and fix present | none |
| `docsys_config.py` refusals | file (the config), key and fix present, and already fixture-tested by `test_seam.py` | none |
| `check.py` | the summary names the failing checks; unavailable-tool message names the fix | see next section |

## A finding the standard did not anticipate

The runner printed each `=== name ===` header, then started the check.
The check's output goes straight to the shared file descriptor; the runner's own prints sat in a block buffer whenever stdout was a pipe.
Every header therefore appeared *after* every check's output, and the lines of a failing check could not be attributed to it.

A terminal hides this, because a terminal is line-buffered.
The machine reader is exactly the reader that sees a pipe — CI logs, a coding agent capturing output.
It was found by reading a piped run in which every header arrived together at the end with nothing beneath it.

The fix is a flush before each check, and the test that would have caught it now runs in the gate as `runner` (`scripts/test_check.py`).
It runs the runner over synthetic checks with a pipe on stdout, and pins the header order, that a failing check does not stop the ones after it, and that the summary names exactly the failing one.
The test was made to fail on the unflushed runner first, so it is known to detect the bug and not merely to pass.

## What is enforced, and what is not

- **Enforced by fixture:** `frontmatter_lint.py`, `ulid_check.py`, `paired_change.py`, and — since Phase 12 T4 — `slug_check.py`, `linkcheck.py` and `hash_check.py`.
  Their fixture runners fail a case whose messages lack the `fix:` clause, so a new message added without one is caught.
  When this audit was written the last three built their messages inline in `main()` and no fixture ran them; T4 extracted the message-building into pure functions, the shape `check_referential_integrity` already had.
  It found the same inline shape in `ulid_check.py`'s own `main()` (a malformed or duplicate `id`, invalid YAML), which the line above had counted as enforced, and extracted those too.
- **Not enforced:** the drift message of `generate_schema.py --check`, which says what to run and to commit the result but not under the `fix:` marker, and has no fixture; and the runner's own messages, which are pinned only for order and attribution.
  Recorded in [`technical-debt.md`](../../../steering/technical-debt.md).
- **Not checked at all:** whether a fix is *correct*, only that one is stated.
  A stated fix that is wrong is worse than none, and only a reader acting on it would find out.
  The only reads of that kind done here were the fixity, link and schema-drift messages, each produced by a real failure and read back.
