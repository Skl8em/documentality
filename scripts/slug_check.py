#!/usr/bin/env python3
"""Slug lint (ADR-028) — the filename must equal the frontmatter slug.

For every document that declares a `slug`, its filename stem must be exactly that
slug (hyphenized), or `slug-<id>` if the ULID is carried in the name (the only
permitted ULID-in-filename form, slug first). Documents without a `slug` are not
checked — the convention is opt-in. A slug must itself be hyphen-cased (lowercase
letters, digits, hyphens). Run `scripts/slugify_names.py` to fix filenames.

Reads frontmatter through scripts/yaml_frontmatter.py, so it needs `pyyaml` — the
devShell provides it.

    python3 scripts/slug_check.py
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yaml_frontmatter import FrontmatterError, load, values  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main():
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    errors = []
    n = 0
    for f in files:
        try:
            fm = values(load(f))
        except FrontmatterError as exc:
            errors.append((f, f"invalid YAML frontmatter at {exc} — fix: correct the YAML at that line"))
            continue
        slug = fm.get("slug")
        if not slug:
            continue
        n += 1
        if not isinstance(slug, str):
            errors.append((f, f"slug {slug!r} is not a string — fix: write it as a plain hyphen-cased word, e.g. `slug: my-record`"))
            continue
        stem = os.path.basename(f)[:-3]  # drop ".md"
        if not SLUG_RE.match(slug):
            errors.append((f, f"slug {slug!r} is not hyphen-cased (a-z, 0-9, -) — fix: rewrite it in lowercase words joined by hyphens"))
        allowed = {slug}
        if fm.get("id"):
            allowed.add(f"{slug}-{fm['id']}")
        if stem not in allowed:
            want = slug + (f" (or {slug}-<id>)" if fm.get("id") else "")
            errors.append((f, f"filename stem {stem!r} != slug {want} — fix: rename the file (`python3 scripts/rename_doc.py` rewrites the links to it), or change `slug`"))

    if errors:
        print(f"SLUG ERRORS: {len(errors)}")
        for f, msg in errors:
            print(f"  {f}  {msg}")
        return 1
    print(f"Slug OK ({n} slugged files; filename == slug).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
