#!/usr/bin/env python3
"""Fixture test for the slug check's verdicts and messages (Phase 12 T4).

`check_slug` is a pure function over one record's path and already-loaded
frontmatter, so each case is a small dict, not a `.md` file in the corpus — the same
reason as test_ulid_check.py. Every message must name the edit that clears it, after
`fix:`: the gate's reader is often a machine with no other context.

    python3 scripts/test_slug_check.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slug_check  # noqa: E402
from yaml_frontmatter import FrontmatterError  # noqa: E402

ULID = "01K0000000000000000000000"

# (name, path, frontmatter, fragments each expected error must contain — one per error)
CASES = [
    ("a stem equal to the slug passes", "a/foo.md", {"slug": "foo"}, []),
    ("the id-suffixed stem passes when the record has that id",
     f"a/foo-{ULID}.md", {"slug": "foo", "id": ULID}, []),
    ("no slug: the convention is opt-in", "a/Anything_Goes.md", {}, []),
    ("a slug that is not a string", "a/foo.md", {"slug": 12}, ["is not a string"]),
    ("a slug that is not hyphen-cased", "a/Foo_Bar.md", {"slug": "Foo_Bar"}, ["not hyphen-cased"]),
    ("a stem that is not the slug", "a/other.md", {"slug": "foo"}, ["filename stem"]),
    ("the id-suffixed stem is refused when the record has no id",
     f"a/foo-{ULID}.md", {"slug": "foo"}, ["filename stem"]),
    ("the id-suffixed stem is refused when the id differs",
     "a/foo-01K9999999999999999999999.md", {"slug": "foo", "id": ULID}, ["filename stem"]),
]

FIX_MARKER = "fix:"


def verdict(got, path, fragments):
    """None when `got` holds one error per fragment, all on `path`, each carrying a
    fix clause; else why not."""
    if len(got) != len(fragments) or any(p != path for p, _ in got):
        return f"expected {fragments} on {path}, got {got}"
    for (_, msg), fragment in zip(got, fragments):
        if fragment not in msg:
            return f"expected {fragment!r} in {msg!r}"
        if FIX_MARKER not in msg:
            return f"message without a `{FIX_MARKER}` clause: {msg!r}"
    return None


def main():
    failures = 0
    for name, path, fm, fragments in CASES:
        why = verdict(slug_check.check_slug(path, fm), path, fragments)
        print(f"ok    {name}" if why is None else f"FAIL  {name}: {why}")
        failures += why is not None

    name = "invalid YAML names the line and how to fix it"
    why = verdict([slug_check.yaml_error("a/foo.md", FrontmatterError(3, "bad"))], "a/foo.md", ["line 3"])
    print(f"ok    {name}" if why is None else f"FAIL  {name}: {why}")
    failures += why is not None

    total = len(CASES) + 1
    print("\n" + "=" * 40)
    if failures:
        print(f"slug check: {failures}/{total} case(s) failed")
        return 1
    print(f"slug check: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
