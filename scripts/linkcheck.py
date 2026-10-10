#!/usr/bin/env python3
"""Resolve every relative markdown link across tracked .md files; report broken ones.

Phase-close link gate (roadmap: verification runs within each phase). Run from
anywhere; the repo root is derived from git. Exit 1 if any relative link is broken.

    python3 scripts/linkcheck.py
"""
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()
os.chdir(ROOT)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def broken_targets(path, text, exists=os.path.exists):
    """Yield (lineno, target) for each relative link in `text`, the content of the
    document at `path`, that does not resolve. `exists` is what says whether a
    resolved path is there — the filesystem, unless a fixture supplies its own."""
    for lineno, line in enumerate(text.split("\n"), 1):
        for match in LINK_RE.finditer(line):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split()[0]          # drop any link title
            link_path = target.split("#", 1)[0]  # drop any anchor
            if not link_path or link_path.startswith("<") or "…" in link_path:
                continue                        # fill-in placeholder, not a link
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), link_path))
            if not exists(resolved):
                yield lineno, target


def format_broken(path, lineno, target):
    return f"{path}:{lineno}  ->  {target}  — no such file — fix: point the link at an existing path, or remove it"


def main():
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    broken = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            broken.extend((f, lineno, target) for lineno, target in broken_targets(f, fh.read()))
    if broken:
        print(f"BROKEN LINKS: {len(broken)}")
        for f, lineno, target in broken:
            print(f"  {format_broken(f, lineno, target)}")
        return 1
    print("All relative markdown links resolve. OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
