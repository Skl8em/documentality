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

files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def broken_links():
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                for match in LINK_RE.finditer(line):
                    target = match.group(1).strip()
                    if target.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    target = target.split()[0]          # drop any link title
                    path = target.split("#", 1)[0]      # drop any anchor
                    if not path or path.startswith("<") or "…" in path:
                        continue                        # fill-in placeholder, not a link
                    resolved = os.path.normpath(os.path.join(os.path.dirname(f), path))
                    if not os.path.exists(resolved):
                        yield f, lineno, target


def main():
    broken = list(broken_links())
    if broken:
        print(f"BROKEN LINKS: {len(broken)}")
        for f, lineno, target in broken:
            print(f"  {f}:{lineno}  ->  {target}")
        return 1
    print("All relative markdown links resolve. OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
