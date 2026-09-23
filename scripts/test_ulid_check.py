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

# The register's shape is configuration (docsys.yaml `register:`), not code: the
# fixtures state their own, so the engine is tested against a format that is not
# this repo's — a second shape below proves nothing ADR-specific is baked in.
REGISTER_CFG = {
    "path": "register.md",
    "columns": 5,
    "ordinal_column": 0,
    "status_column": 4,
    "ordinal_pattern": r"^\[(\d+)\]\(([^)]+)\)$",
    "superseded_pattern": r"superseded by (\d+)",
}

REGISTER = """\
| # | Decision | Phase | Date | Status |
| --- | --- | --- | --- | --- |
| [001](a.md) | Decision A | p1 | 2026-01-01 | superseded by 002 |
| [002](b.md) | Decision B | p1 | 2026-01-02 | accepted |
"""

# A four-column register, status third, a different verb — same records.
OTHER_REGISTER_CFG = {
    "path": "log/index.md",
    "columns": 4,
    "ordinal_column": 0,
    "status_column": 3,
    "ordinal_pattern": r"^\[(\d+)\]\(([^)]+)\)$",
    "superseded_pattern": r"replaced by (\d+)",
}

OTHER_REGISTER = """\
| # | Decision | Date | Status |
| --- | --- | --- | --- |
| [1](../a.md) | Decision A | 2026-01-01 | replaced by 2 |
| [2](../b.md) | Decision B | 2026-01-02 | accepted |
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


# (name, register text, register config, records, expected)
OTHER_SHAPE_CASES = [
    ("second register shape agrees with the records",
     OTHER_REGISTER, OTHER_REGISTER_CFG,
     {"a.md": {"superseded-by": "b"}, "b.md": {"superseded-by": None}},
     []),

    ("second register shape, record disagrees",
     OTHER_REGISTER, OTHER_REGISTER_CFG,
     {"a.md": {"superseded-by": None}, "b.md": {"superseded-by": None}},
     [("a.md", "does not name it")]),
]


def run_register_cases():
    failures = 0
    cases = [(n, REGISTER, REGISTER_CFG, r, e) for n, r, e in REGISTER_CASES] + OTHER_SHAPE_CASES
    for name, text, cfg, records, expected in cases:
        got = ulid_check.check_register(records, text, cfg)
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


def run_register_file_cases():
    """A configured register that is not a tracked document must fail loud: a typo in
    docsys.yaml would otherwise silently switch the cross-check off."""
    failures = 0
    got = ulid_check.check_register_file({"a.md": {}}, REGISTER_CFG)
    if len(got) == 1 and "register.path" in got[0][1] and "register.md" in got[0][1]:
        print("ok    a register path that is not a tracked document is an error")
    else:
        failures += 1
        print(f"FAIL  a register path that is not a tracked document is an error: got {got}")
    return failures


def main():
    failures = run_ref_cases() + run_register_cases() + run_register_file_cases()
    total = len(REF_CASES) + len(REGISTER_CASES) + len(OTHER_SHAPE_CASES) + 1
    print("\n" + "=" * 40)
    if failures:
        print(f"referential integrity: {failures}/{total} case(s) failed")
        return 1
    print(f"referential integrity: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
