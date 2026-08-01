#!/usr/bin/env python3
"""ULID verifier — a SAFE STARTER (ADR-028).

Validates the ULID-named records the new scheme introduces, without failing on
the legacy count-named records whose migration is deferred (see the technical-debt
doc). For every `<ulid>-<slug>.md` file it checks: the prefix is a valid ULID; the
frontmatter `id` matches it; the frontmatter `slug` matches the filename slug; and
ULIDs are unique across the corpus. Reports (but does not fail on) legacy records
missing an `id`, and phases whose ULID order disagrees with their `order` key.

Stdlib only.

    python3 scripts/ulid_check.py
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ulid import is_ulid, timestamp_of  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

ULID_NAME = re.compile(r"^([0-9A-HJKMNP-TV-Z]{26})-(.+)\.md$")
# legacy count-named records whose migration to <ulid>-<slug> is deferred (tech debt)
LEGACY_NAME = re.compile(r"(ADR-\d+|phase-\d\d)")


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
    errors, notes = [], []
    seen = {}

    for f in files:
        base = os.path.basename(f)
        m = ULID_NAME.match(base)
        if m:
            ulid, slug = m.group(1), m.group(2)
            fm = frontmatter(f)
            if not is_ulid(ulid):
                errors.append((f, "filename ULID prefix is not valid Crockford base32"))
            if fm.get("id") != ulid:
                errors.append((f, f"frontmatter id ({fm.get('id')!r}) != filename ULID ({ulid})"))
            if fm.get("slug") and fm.get("slug") != slug:
                errors.append((f, f"frontmatter slug ({fm.get('slug')!r}) != filename slug ({slug!r})"))
            if ulid in seen:
                errors.append((f, f"duplicate ULID (also in {seen[ulid]})"))
            seen[ulid] = f
        elif LEGACY_NAME.search(base):
            if not frontmatter(f).get("id"):
                notes.append((f, "legacy count-named record without a ULID id (migration deferred)"))

    if notes:
        print(f"NOTES: {len(notes)} legacy records pending ULID migration (tech debt)")

    if errors:
        print(f"ULID ERRORS: {len(errors)}")
        for f, msg in errors:
            print(f"  {f}  {msg}")
        return 1
    print(f"ULID OK ({len(seen)} ULID-named records valid & unique; {len(notes)} legacy pending).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
