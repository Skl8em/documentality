#!/usr/bin/env python3
"""ULID verifier (ADR-028) — frontmatter-based.

The canonical identifier is the frontmatter `id:` (a ULID); it is NOT required in
the filename (filenames follow the `<slug>.md` convention, checked by slug_check).
This validates that every declared `id` is a syntactically valid ULID and that ids
are unique across the corpus. Records without an `id` are permitted (adopting ids
on the legacy count-named records is optional; the convention is kept open).

Reads frontmatter through scripts/yaml_frontmatter.py, so it needs `pyyaml` — the
devShell provides it.

    python3 scripts/ulid_check.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ulid import is_ulid  # noqa: E402
from yaml_frontmatter import FrontmatterError, load, values  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)


def main():
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    errors = []
    seen = {}
    n_ids = 0
    for f in files:
        try:
            rid = values(load(f)).get("id")
        except FrontmatterError as exc:
            errors.append((f, f"invalid YAML frontmatter at {exc}"))
            continue
        if not rid:
            continue
        n_ids += 1
        if not isinstance(rid, str) or not is_ulid(rid):
            errors.append((f, f"id {rid!r} is not a valid ULID"))
        if rid in seen:
            errors.append((f, f"duplicate id (also in {seen[rid]})"))
        seen[rid] = f

    if errors:
        print(f"ULID ERRORS: {len(errors)}")
        for f, msg in errors:
            print(f"  {f}  {msg}")
        return 1
    print(f"ULID OK ({n_ids} records carry a valid, unique id).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
