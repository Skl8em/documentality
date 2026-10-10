#!/usr/bin/env python3
"""Fixture test for the link check's verdicts and messages (Phase 12 T4).

`broken_targets` reads a document's text and asks a callable whether a path exists,
so each case is a string and a set of paths, not a `.md` file with a deliberately
broken link in the corpus (which would fail the gate that runs this). Every message
must name the file, the line, the target and, after `fix:`, the edit that clears it.

    python3 scripts/test_linkcheck.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import linkcheck  # noqa: E402

EXISTING = {"docs/other.md", "docs/sub/deep.md", "top.md"}

# (name, file the text lives in, text, expected [(lineno, target)])
CASES = [
    ("a link to an existing sibling", "docs/a.md", "See [x](other.md).\n", []),
    ("a link up and over, resolved from the file's directory", "docs/sub/a.md", "[x](../other.md)\n", []),
    ("a broken link is reported with its line", "docs/a.md", "ok\n\nSee [x](missing.md).\n", [(3, "missing.md")]),
    ("an anchor is dropped before resolving", "docs/a.md", "[x](other.md#part)\n", []),
    ("a broken link with an anchor is still broken", "docs/a.md", "[x](gone.md#part)\n", [(1, "gone.md#part")]),
    ("a link title is dropped", "docs/a.md", '[x](other.md "Title")\n', []),
    ("http, https, mailto and same-file anchors are not resolved", "docs/a.md",
     "[a](http://x.org) [b](https://x.org) [c](mailto:a@b.c) [d](#here)\n", []),
    ("a fill-in placeholder is not a link", "docs/a.md", "[x](<path>) [y](…)\n", []),
    ("two broken links on one line are both reported", "docs/a.md", "[x](m1.md) [y](m2.md)\n",
     [(1, "m1.md"), (1, "m2.md")]),
]

FIX_MARKER = "fix:"


def exists(path):
    return path in EXISTING


def main():
    failures = 0
    for name, where, text, expected in CASES:
        got = list(linkcheck.broken_targets(where, text, exists))
        ok = got == expected
        print(f"ok    {name}" if ok else f"FAIL  {name}: expected {expected}, got {got}")
        failures += not ok

    name = "the message names the file, the line, the target and a fix"
    msg = linkcheck.format_broken("docs/a.md", 7, "missing.md")
    ok = all(part in msg for part in ("docs/a.md:7", "missing.md", FIX_MARKER))
    print(f"ok    {name}" if ok else f"FAIL  {name}: {msg!r}")
    failures += not ok

    total = len(CASES) + 1
    print("\n" + "=" * 40)
    if failures:
        print(f"link check: {failures}/{total} case(s) failed")
        return 1
    print(f"link check: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
