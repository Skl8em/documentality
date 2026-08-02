#!/usr/bin/env python3
"""Correction (ADR-028): make each slugged file's filename equal its slug.

The `<slug>.md` direction of the naming convention. For every document that
declares a `slug` whose filename stem differs, rename it to `<slug>.md` via the
safe-rename core (all links rewritten). The inverse tool — filename := `<slug>-<ulid>`
— is `scripts/migrate_ids.py`; the convention is kept open, tools both ways.

Stdlib only.

    python3 scripts/slugify_names.py            # apply, then run the gate
    python3 scripts/slugify_names.py --dry-run  # show what would change
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rename_doc import rename_path  # noqa: E402
from slug_check import frontmatter  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)


def main():
    dry = "--dry-run" in sys.argv
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    renames = []
    for f in files:
        slug = frontmatter(f).get("slug")
        if not slug:
            continue
        stem = os.path.basename(f)[:-3]
        if stem == slug:
            continue
        target = os.path.join(os.path.dirname(f), f"{slug}.md")
        if os.path.exists(target):
            raise SystemExit(f"cannot rename {f} -> {target}: target exists")
        renames.append((f, target))

    for old, new in renames:
        print(f"{'[dry-run] ' if dry else ''}{old} -> {new}")
        if not dry:
            rename_path(old, new)

    if not renames:
        print("nothing to do — all slugged filenames already match their slug.")
        return 0
    if dry:
        return 0
    print("\n=== running the gate ===")
    return subprocess.call([sys.executable, "scripts/check.py"])


if __name__ == "__main__":
    sys.exit(main())
