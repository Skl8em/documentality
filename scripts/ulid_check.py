#!/usr/bin/env python3
"""ULID verifier (ADR-028) — frontmatter-based, plus referential integrity (Phase
11 T4).

The canonical identifier is the frontmatter `id:` (a ULID); it is NOT required in
the filename (filenames follow the `<slug>.md` convention, checked by slug_check).
This validates that every declared `id` is a syntactically valid ULID and that ids
are unique across the corpus. Records without an `id` are permitted (adopting ids
on the legacy count-named records is optional; the convention is kept open) — for
those, a record's own identity, wherever something else needs to name it, is its
filename stem (the pre-ULID convention already in use, e.g. `supersedes:
ADR-001-inscribed-act`).

Three referential checks, each catching a way `supersedes`/`superseded-by` can go
stale silently (the motivation recorded in phases/refoundation/phase-11-tooling-
hardening/plan.md: a typo in ADR-034's `supersedes` was caught only by hand):

  1. Every non-null `supersedes`/`superseded-by` resolves to some record's `id`
     or filename stem — a dangling reference is an error, not a warning.
  2. Supersession is symmetric (schema/frontmatter-rules.yaml already documents
     `superseded-by` as "the inverse of `supersedes`, kept symmetric"): if A
     supersedes B, B's `superseded-by` must name A back.
  3. Every row of the central decision register agrees with the record its link
     points at: a "superseded by N" row must match that record's own
     `superseded-by`, and a plain row must find it unset. Which file is the
     register, and the shape of its rows, is instance configuration — docsys.yaml
     `register:` — not something this script knows.

A `<...>` placeholder (a force template's SPECIMEN frontmatter, e.g.
`supersedes: <ADR-XXX or null>`) is not a reference and is skipped, the same test
`hash_seal.is_frozen` already uses for a specimen `provenance.id`.

Reads frontmatter through scripts/yaml_frontmatter.py, so it needs `pyyaml` — the
devShell provides it.

    python3 scripts/ulid_check.py
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docsys_config import load_config  # noqa: E402
from ulid import is_ulid  # noqa: E402
from yaml_frontmatter import FrontmatterError, load, values  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

REF_FIELDS = ("supersedes", "superseded-by")
INVERSE_FIELD = {"supersedes": "superseded-by", "superseded-by": "supersedes"}


def stem(path):
    return os.path.basename(path)[:-3]  # drop ".md"


def identity_of(path, rid):
    """A record's own identity as something else would name it: its `id` if it
    carries one, else its filename stem (the pre-ULID reference convention)."""
    return rid if rid else stem(path)


def normalize_refs(value):
    """None -> []; a string -> [string]; a list -> itself. `<...>` placeholders
    (template SPECIMEN frontmatter) are dropped — they are fill-ins, not
    references."""
    if value is None:
        items = []
    elif isinstance(value, list):
        items = value
    else:
        items = [value]
    return [v for v in items if isinstance(v, str) and "<" not in v]


def build_identity_index(records):
    """records: {path: {"id": str|None, ...}} -> {identity: path}."""
    return {identity_of(path, rec.get("id")): path for path, rec in records.items()}


def check_referential_integrity(records):
    """records: {path: {"id":, "supersedes":, "superseded-by":}}.
    Returns [(path, message)] — dangling references and broken symmetry."""
    index = build_identity_index(records)
    errors = []
    resolved = {}  # (path, field) -> [target_path, ...]
    for path, rec in records.items():
        for field in REF_FIELDS:
            targets = []
            for ref in normalize_refs(rec.get(field)):
                target = index.get(ref)
                if target is None:
                    errors.append((path, f"`{field}: {ref}` does not resolve to any record's `id` or filename"))
                else:
                    targets.append(target)
            resolved[(path, field)] = targets

    for path, rec in records.items():
        for field in REF_FIELDS:
            inverse = INVERSE_FIELD[field]
            for target in resolved[(path, field)]:
                back = resolved.get((target, inverse), [])
                if path not in back:
                    errors.append((path, f"`{field}` names {target}, but its `{inverse}` does not name this record back"))
    return errors


def parse_register(text, register):
    """Yield (ordinal, path, status) for each decision row of the central
    register — `path` resolved relative to the register file's own directory,
    the way the markdown link itself resolves. `register` is docsys.yaml's
    `register:` section: it says what a decision row looks like."""
    base = os.path.dirname(register["path"])
    row_re = re.compile(register["ordinal_pattern"])
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != register["columns"]:
            continue
        m = row_re.match(cells[register["ordinal_column"]])
        if not m:
            continue  # header, separator, or any row that is not a decision row
        ordinal, link = m.groups()
        path = os.path.normpath(os.path.join(base, link))
        yield ordinal, path, cells[register["status_column"]]


def check_register(records, register_text, register):
    """Cross-check the register's "superseded by N" status text against the
    linked record's own `superseded-by`. A broken link is linkcheck's job, not
    re-reported here."""
    index = build_identity_index(records)
    superseded_re = re.compile(register["superseded_pattern"])
    rows = list(parse_register(register_text, register))
    ordinal_to_path = {ordinal: path for ordinal, path, _ in rows}
    errors = []
    for ordinal, path, status in rows:
        if path not in records:
            continue
        actual_targets = {index.get(ref) for ref in normalize_refs(records[path].get("superseded-by"))}
        actual_targets.discard(None)
        m = superseded_re.search(status)
        if m:
            expected = ordinal_to_path.get(m.group(1))
            if expected is None or expected not in actual_targets:
                errors.append((path, f"register row {ordinal} says {status!r}, but this record's `superseded-by` does not name it"))
        elif actual_targets:
            errors.append((path, f"register row {ordinal} says {status!r} (no supersession), but this record's `superseded-by` is set"))
    return errors


def check_register_file(records, register):
    """Read the configured register and cross-check it. A register that is not a
    tracked document is an error, not a skip: a mistyped `register.path` would
    otherwise switch the whole cross-check off without a word."""
    if register["path"] not in records:
        return [(register["path"], f"`register.path` in docsys.yaml names `{register['path']}`, "
                                   "which is not a tracked Markdown file — fix the path")]
    with open(register["path"], encoding="utf-8") as fh:
        return check_register(records, fh.read(), register)


def main():
    register = load_config()["register"]
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    errors = []
    seen = {}
    n_ids = 0
    records = {}
    for f in files:
        try:
            fm = values(load(f))
        except FrontmatterError as exc:
            errors.append((f, f"invalid YAML frontmatter at {exc}"))
            continue
        rid = fm.get("id")
        records[f] = fm
        if not rid:
            continue
        n_ids += 1
        if not isinstance(rid, str) or not is_ulid(rid):
            errors.append((f, f"id {rid!r} is not a valid ULID"))
        if rid in seen:
            errors.append((f, f"duplicate id (also in {seen[rid]})"))
        seen[rid] = f

    errors.extend(check_referential_integrity(records))

    errors.extend(check_register_file(records, register))

    if errors:
        print(f"ULID ERRORS: {len(errors)}")
        for f, msg in errors:
            print(f"  {f}  {msg}")
        return 1
    print(f"ULID OK ({n_ids} records carry a valid, unique id; supersedes/superseded-by resolve, are symmetric, and agree with the register).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
