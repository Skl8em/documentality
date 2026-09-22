#!/usr/bin/env python3
"""Fixture test for the frontmatter parser (Phase 11 T2).

The frontmatter linter used to split strings on commas and colons instead of
parsing YAML. Anything outside the subset it handled mis-parsed — and sometimes
*passed*. Each fixture below is a tiny document plus the exact errors the linter
must report, pinning the cases the hand-rolled parser got wrong in either
direction, and the typing policy (`yes`/`no` stay strings) a naive
`yaml.safe_load` would silently break. Fixtures live here as strings, not as `.md`
files in the corpus, for the same reason as the MD100 harness: a document full of
deliberate violations would have to be exempted from the gate that runs this.

Needs `pyyaml` — run inside the devShell (`nix develop`), as scripts/check.py does.

    python3 scripts/test_frontmatter_lint.py
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontmatter_lint  # noqa: E402

# A minimal document that passes the gate: file lines 2–10, one field per line.
VALID = """\
title: Fixture
force: explain
intention: state
constitutive: no
view: synchronic
provenance: { type: function, id: steering }
audience: [contributor]
reader: H+M
status: draft
"""


def doc(frontmatter):
    return f"---\n{frontmatter}---\n\nBody.\n"


def replace(field_line, *new_lines):
    """VALID with the line starting `field_line` swapped for `new_lines`."""
    out = []
    for ln in VALID.splitlines():
        out.extend(new_lines if ln.startswith(field_line) else [ln])
    return "\n".join(out) + "\n"


# (name, frontmatter, [(file line, message fragment)] the linter must report — exactly)
LINT_CASES = [
    # --- wrongly PASSED by the hand-rolled parser -----------------------------
    ("undeclared field hidden by indentation",
     VALID + "  review: pending\n",
     [(11, "invalid YAML")]),
    ("plain scalar folded onto the next line",
     replace("view:", "view: synchronic", "  diachronic"),
     [(6, "view `synchronic diachronic` not in")]),
    ("duplicate key, the last one valid",
     replace("view:", "view: bogus", "view: synchronic"),
     [(7, "duplicate key `view`")]),
    ("duplicate key inside an inline map",
     replace("provenance:", "provenance: { type: bogus, id: steering, type: function }"),
     [(7, "duplicate key `type`")]),
    ("unterminated quoted string",
     replace("title:", 'title: "Fixture'),
     [(10, "while scanning a quoted scalar, from line 2")]),

    # --- failed for the WRONG reason ------------------------------------------
    ("block-mapping provenance with an unknown type",
     replace("provenance:", "provenance:", "  type: bogus", "  id: steering"),
     [(7, "provenance.type `bogus` not in")]),

    # --- wrongly FAILED by the hand-rolled parser -----------------------------
    ("block-sequence audience",
     replace("audience:", "audience:", "  - contributor", "  - decider"),
     []),
    ("inline comment after an enum value",
     replace("view:", "view: synchronic  # the present state"),
     []),
    ("quoted comma inside an inline map",
     replace("provenance:", 'provenance: { type: function, id: "steering, type: bogus" }'),
     []),

    # --- typing policy: what a plain yaml.safe_load would break ----------------
    ("constitutive yes/no stay strings (YAML 1.1 would read booleans)",
     replace("constitutive:", "constitutive: yes"),
     []),
]


def lint(frontmatter_text):
    schema = frontmatter_lint.load_schema()
    with tempfile.TemporaryDirectory() as workdir:
        path = os.path.join(workdir, "case.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(doc(frontmatter_text))
        errors, warnings = [], []
        frontmatter_lint.lint_file(path, schema, errors, warnings)
    return [(line, msg) for _, line, msg in errors]


def matches(got, expected):
    """Every expected (line, fragment) consumes exactly one reported message."""
    remaining = list(got)
    for line, fragment in expected:
        hit = next((g for g in remaining if g[0] == line and fragment in g[1]), None)
        if hit is None:
            return False
        remaining.remove(hit)
    return not remaining


def run_lint_cases():
    failures = 0
    for name, text, expected in LINT_CASES:
        got = lint(text)
        if matches(got, expected):
            print(f"ok    {name}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected {expected}, got {got}")
    return failures


# (name, frontmatter, {key: value} the parser must return) — values the linter
# never checks, so a mis-parse there is invisible to the lint cases above.
PARSE_CASES = [
    ("comment stripped from an unchecked value",
     "axis: provenance       # the producer's shelf\n",
     {"axis": "provenance"}),
    ("ULID made only of digits stays a string",
     "id: 01234567890123456789012345\n",
     {"id": "01234567890123456789012345"}),
    ("date stays a string",
     "valid-for: 2026-09-15\n",
     {"valid-for": "2026-09-15"}),
    ("null is null",
     "supersedes: null\nsuperseded-by: ~\n",
     {"supersedes": None, "superseded-by": None}),
    ("empty block",
     "",
     {}),
]


def run_parse_cases():
    import yaml_frontmatter  # imported late: absent from the pre-T2 tree

    failures = 0
    for name, text, expected in PARSE_CASES:
        got = yaml_frontmatter.values(yaml_frontmatter.parse(doc(text)))
        if got == expected:
            print(f"ok    {name}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected {expected!r}, got {got!r}")
    return failures


def main():
    failures = run_lint_cases() + run_parse_cases()
    total = len(LINT_CASES) + len(PARSE_CASES)
    print("\n" + "=" * 40)
    if failures:
        print(f"frontmatter parser: {failures}/{total} case(s) failed")
        return 1
    print(f"frontmatter parser: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
