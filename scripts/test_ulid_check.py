#!/usr/bin/env python3
"""Fixture test for referential integrity (Phase 11 T4).

Each case is a tiny synthetic `records` dict (or register text), not a `.md` file
in the corpus, for the same reason as test_frontmatter_lint.py's fixtures: a
document with a deliberately dangling `supersedes` would have to be exempted from
the gate that runs this. `check_referential_integrity` and `check_register` are
pure functions over already-loaded frontmatter, so no temp files are needed here.

    python3 scripts/test_ulid_check.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ulid_check  # noqa: E402

# --- check_referential_integrity -------------------------------------------

REF_CASES = [
    ("dangling supersedes",
     {"a.md": {"id": None, "supersedes": "no-such-record", "superseded-by": None}},
     [("a.md", "does not resolve")]),

    ("dangling superseded-by, by ULID",
     {"a.md": {"id": "01K0000000000000000000000", "supersedes": None, "superseded-by": "01K9999999999999999999999"}},
     [("a.md", "does not resolve")]),

    ("symmetric pair resolved by filename stem, no error",
     {
         "a.md": {"id": None, "supersedes": None, "superseded-by": "b.md"[:-3]},
         "b.md": {"id": None, "supersedes": "a", "superseded-by": None},
     },
     []),

    ("symmetric pair resolved by id, no error",
     {
         "a.md": {"id": "01K0000000000000000000000", "supersedes": None, "superseded-by": "01K9999999999999999999999"},
         "b.md": {"id": "01K9999999999999999999999", "supersedes": "01K0000000000000000000000", "superseded-by": None},
     },
     []),

    ("asymmetric: A supersedes B, B silent",
     {
         "a.md": {"id": None, "supersedes": "b", "superseded-by": None},
         "b.md": {"id": None, "supersedes": None, "superseded-by": None},
     },
     [("a.md", "does not name this record back")]),

    ("placeholder specimen is not a reference",
     {"a.md": {"id": None, "supersedes": "<ADR-XXX or null>", "superseded-by": None}},
     []),

    ("list-valued supersedes, one dangling",
     {
         "a.md": {"id": None, "supersedes": ["b", "no-such"], "superseded-by": None},
         "b.md": {"id": None, "supersedes": None, "superseded-by": "a"},
     },
     [("a.md", "does not resolve")]),
]


def run_ref_cases():
    failures = 0
    for name, records, expected in REF_CASES:
        got = [(path, msg) for path, msg in ulid_check.check_referential_integrity(records)]
        ok = len(got) == len(expected) and all(
            path == e_path and fragment in msg
            for (path, msg), (e_path, fragment) in zip(sorted(got), sorted(expected))
        )
        if ok:
            print(f"ok    {name}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected {expected}, got {got}")
    return failures


# --- check_register ----------------------------------------------------------

REGISTER = """\
| # | Decision | Phase | Date | Status |
| --- | --- | --- | --- | --- |
| [001](a.md) | Decision A | p1 | 2026-01-01 | superseded by 002 |
| [002](b.md) | Decision B | p1 | 2026-01-02 | accepted |
"""

REGISTER_CASES = [
    ("register agrees with the records",
     {
         "a.md": {"superseded-by": "b.md"[:-3]},
         "b.md": {"superseded-by": None},
     },
     []),

    ("register says superseded, record disagrees",
     {
         "a.md": {"superseded-by": None},
         "b.md": {"superseded-by": None},
     },
     [("a.md", "does not name it")]),

    ("register says plain, record has superseded-by set",
     {
         "a.md": {"superseded-by": "b"},
         "b.md": {"superseded-by": "a"},
     },
     [("b.md", "is set")]),
]


def run_register_cases():
    failures = 0
    for name, records, expected in REGISTER_CASES:
        got = ulid_check.check_register(records, REGISTER, "register.md")
        ok = len(got) == len(expected) and all(
            path == e_path and fragment in msg
            for (path, msg), (e_path, fragment) in zip(sorted(got), sorted(expected))
        )
        if ok:
            print(f"ok    {name}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected {expected}, got {got}")
    return failures


def main():
    failures = run_ref_cases() + run_register_cases()
    total = len(REF_CASES) + len(REGISTER_CASES)
    print("\n" + "=" * 40)
    if failures:
        print(f"referential integrity: {failures}/{total} case(s) failed")
        return 1
    print(f"referential integrity: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
