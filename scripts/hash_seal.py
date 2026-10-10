#!/usr/bin/env python3
"""Content-hash fixity seal — mint the `hash:` of a frozen record.

The ULID (`id`) says *which* record; the hash says *this exact content*. Unlike a
git SHA it travels with the document, so a record copied into another repository
can still be verified. Verification is `scripts/hash_check.py`.

The canonical form hashed (this definition IS the contract — changing it invalidates
every existing seal):

  1. read UTF-8, normalise CRLF/CR to LF;
  2. split at the frontmatter fences into frontmatter lines and body;
  3. frontmatter: drop the `hash:` line, strip trailing whitespace, drop blank
     lines, then SORT the lines — so reordering keys does not break a seal;
  4. body: strip trailing whitespace per line, then strip leading/trailing blank lines;
  5. canonical text = sorted frontmatter + "\\n---\\n" + body + "\\n";
  6. seal = "sha256:" + sha256(canonical UTF-8).

Sorting the frontmatter is deliberate: the seal fixes the document's *content and
coordinates*, not the order they happen to be written in.

A record is *frozen* — and so eligible for sealing — when it is a project's
diachronic record that has closed: `view: diachronic`, `provenance.type: project`,
and `status` in accepted / done / stable (FROZEN_STATUSES, below). Those fields are read as YAML (through
scripts/yaml_frontmatter.py, so this needs `pyyaml`); the seal itself stays a
line-based canonical form, above, and does not depend on the parser.

    python3 scripts/hash_seal.py --frozen          # seal every unsealed frozen record
    python3 scripts/hash_seal.py path/to/record.md # seal one file
    python3 scripts/hash_seal.py --reseal <path>   # re-seal a record that changed
    python3 scripts/hash_seal.py --print <path>    # compute, write nothing
"""
import hashlib
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yaml_frontmatter import load, values  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

# Which `status` words close a record. Deliberately here and not in the schema: the
# schema still lists its status vocabulary as an open question, and declaring "frozen"
# there would settle part of it by side effect. Together the two lists classify every
# word of `warn_enums.status` in schema/frontmatter-rules.yaml exactly once, and
# scripts/test_hash_check.py fails the gate when they stop doing so.
FROZEN_STATUSES = ("accepted", "done", "stable")
OPEN_STATUSES = ("draft", "deprecated", "in-progress", "planned")


def split_document(path):
    """Return (frontmatter_lines, body_lines). Raises if there is no frontmatter."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: no frontmatter block")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], lines[i + 1:]
    raise ValueError(f"{path}: unterminated frontmatter block")


def canonical_text(fm_lines, body_lines):
    fm = sorted(
        ln.rstrip() for ln in fm_lines
        if ln.strip() and not ln.split(":", 1)[0].strip() == "hash"
    )
    body = [ln.rstrip() for ln in body_lines]
    while body and not body[0]:
        body.pop(0)
    while body and not body[-1]:
        body.pop()
    return "\n".join(fm) + "\n---\n" + "\n".join(body) + "\n"


def seal_of(path):
    fm_lines, body_lines = split_document(path)
    digest = hashlib.sha256(canonical_text(fm_lines, body_lines).encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def field(fm_lines, key):
    for ln in fm_lines:
        if ln.startswith(f"{key}:"):
            return ln.split(":", 1)[1].strip()
    return None


def is_frozen(path):
    fm = values(load(path))  # malformed YAML raises: never silently "not frozen"
    prov = fm.get("provenance")
    if not isinstance(prov, dict):
        return False
    # A force template carries SPECIMEN frontmatter — `id: <phase-or-project-id>` —
    # which otherwise reads as a frozen project record. A placeholder id is not a
    # project, so the document is not a record of one.
    if "<" in str(prov.get("id", "")):
        return False
    return (fm.get("view") == "diachronic"
            and prov.get("type") == "project"
            and fm.get("status") in FROZEN_STATUSES)


def write_seal(path, reseal):
    """Write (or refresh) the `hash:` line. Returns a status word."""
    fm_lines, body_lines = split_document(path)
    existing = field(fm_lines, "hash")
    new = seal_of(path)
    if existing == new:
        return "unchanged"
    if existing and not reseal:
        return "ALREADY SEALED (use --reseal — a deliberate act)"

    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    kept = [ln for ln in lines[1:end] if not ln.startswith("hash:")]
    out = ["---"] + kept + [f"hash: {new}"] + lines[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    return "resealed" if existing else "sealed"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    reseal = "--reseal" in sys.argv

    if "--print" in sys.argv:
        for path in args:
            print(f"{seal_of(path)}  {path}")
        return 0

    if "--frozen" in sys.argv:
        targets = [f for f in subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
                   if is_frozen(f)]
    elif args:
        targets = args
    else:
        print(__doc__)
        return 2

    for path in targets:
        print(f"{write_seal(path, reseal):10}  {path}")
    print(f"\n{len(targets)} record(s) considered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
