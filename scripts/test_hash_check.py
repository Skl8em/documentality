#!/usr/bin/env python3
"""Fixture test for the fixity check's verdicts and messages (Phase 12 T4).

Each case writes a tiny sealed document into a temporary directory, changes it or
not, and asks `scan` for its verdict, so the deliberately broken seal never sits in
the corpus (where it would fail the gate that runs this). The failure message must
name the file and, after `fix:`, both remedies: revert, or re-freeze deliberately.

Needs `pyyaml` — run inside the devShell (`nix develop`), as scripts/check.py does.

    python3 scripts/test_hash_check.py
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hash_check  # noqa: E402
import hash_seal  # noqa: E402

FROZEN = """\
---
title: A closed record
view: diachronic
provenance: {{ type: project, id: some-phase }}
status: {status}
---

Body of the record.
"""

FIX_MARKER = "fix:"


def write(directory, name, text):
    path = os.path.join(directory, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def cases(tmp):
    """Yield (name, ok, detail) for each case."""
    sealed = write(tmp, "sealed.md", FROZEN.format(status="done"))
    hash_seal.write_seal(sealed, reseal=False)

    broken, n_sealed, unsealed = hash_check.scan([sealed])
    yield "an intact seal verifies", (broken, n_sealed, unsealed) == ([], 1, []), (broken, n_sealed, unsealed)

    with open(sealed, "a", encoding="utf-8") as fh:
        fh.write("\nA later edit.\n")
    broken, n_sealed, unsealed = hash_check.scan([sealed])
    yield ("an edit after sealing is reported, naming the declared and actual hash",
           n_sealed == 1 and len(broken) == 1 and broken[0][0] == sealed and broken[0][1] != broken[0][2],
           broken)

    open_record = write(tmp, "open.md", FROZEN.format(status="done"))
    broken, n_sealed, unsealed = hash_check.scan([open_record])
    yield "a frozen record with no seal is listed, not failed", (broken, n_sealed, unsealed) == ([], 0, [open_record]), unsealed

    draft = write(tmp, "draft.md", FROZEN.format(status="draft"))
    broken, n_sealed, unsealed = hash_check.scan([draft])
    yield "a record that is not frozen and has no seal is left alone", (broken, n_sealed, unsealed) == ([], 0, []), unsealed

    bare = write(tmp, "bare.md", "No frontmatter here.\n")
    broken, n_sealed, unsealed = hash_check.scan([bare])
    yield "a document without frontmatter is skipped", (broken, n_sealed, unsealed) == ([], 0, []), (broken, unsealed)

    msg = hash_check.format_broken("steering/x.md", "sha256:aaa", "sha256:bbb")
    yield ("the message names the file, both hashes, and both remedies after a fix clause",
           all(part in msg for part in ("steering/x.md", "sha256:aaa", "sha256:bbb", FIX_MARKER,
                                         "revert", "hash_seal.py --reseal steering/x.md")),
           msg)


def main():
    failures = total = 0
    with tempfile.TemporaryDirectory() as tmp:
        for name, ok, detail in cases(tmp):
            total += 1
            print(f"ok    {name}" if ok else f"FAIL  {name}: {detail!r}")
            failures += not ok
    print("\n" + "=" * 40)
    if failures:
        print(f"fixity check: {failures}/{total} case(s) failed")
        return 1
    print(f"fixity check: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
