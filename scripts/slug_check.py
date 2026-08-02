#!/usr/bin/env python3
"""Slug lint (ADR-028) — the filename must equal the frontmatter slug.

For every document that declares a `slug`, its filename stem must be exactly that
slug (hyphenized), or `slug-<id>` if the ULID is carried in the name (the only
permitted ULID-in-filename form, slug first). Documents without a `slug` are not
checked — the convention is opt-in. A slug must itself be hyphen-cased (lowercase
letters, digits, hyphens). Run `scripts/slugify_names.py` to fix filenames.

Stdlib only.

    python3 scripts/slug_check.py
"""
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path):
    fm = {}
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if not lines or lines[0].strip() != "---":
        return fm
    for ln in lines[1:]:
        if ln.strip() == "---":
            break
        if ":" in ln and not ln.startswith((" ", "\t")):
            k, v = ln.split(":", 1)
            fm[k.strip()] = v.strip().strip("\"'")
    return fm


def main():
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    errors = []
    n = 0
    for f in files:
        fm = frontmatter(f)
        slug = fm.get("slug")
        if not slug:
            continue
        n += 1
        stem = os.path.basename(f)[:-3]  # drop ".md"
        if not SLUG_RE.match(slug):
            errors.append((f, f"slug {slug!r} is not hyphen-cased (a-z, 0-9, -)"))
        allowed = {slug}
        if fm.get("id"):
            allowed.add(f"{slug}-{fm['id']}")
        if stem not in allowed:
            want = slug + (f" (or {slug}-<id>)" if fm.get("id") else "")
            errors.append((f, f"filename stem {stem!r} != slug {want}"))

    if errors:
        print(f"SLUG ERRORS: {len(errors)}")
        for f, msg in errors:
            print(f"  {f}  {msg}")
        return 1
    print(f"Slug OK ({n} slugged files; filename == slug).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
