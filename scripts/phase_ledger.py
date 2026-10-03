#!/usr/bin/env python3
"""Phase ledger — where the project is, declared once (Phase 12 T6(a)).

The current phase used to be implied in a dozen places — the roadmap's markers, the
phases index, the root README, the folders, `phase:` fields — and nothing tied them
together, so Phases 10 and 11 each closed with some of them stale. The ledger says it
once: an ordered list of phases, each a name, an era and a status of `done`,
`current` or `planned`. This script checks the ledger's own rules; checking every
other place against it is the gate's next step (T6(b)).

The rules:
  - the vocabulary is closed: `phases:` at the top, and `number`, `name`, `era`,
    `status` in each entry;
  - `name` and `era` are hyphen-cased;
  - a `done` or `current` phase has a number; a `planned` one has none, because
    unstarted work is never numbered (ADR-038) — starting a phase is the one edit
    that numbers it and marks it `current`;
  - exactly one phase is `current`;
  - the list is in order: every `done`, then the `current`, then every `planned`;
  - the numbers count 1, 2, 3… in that order, with no gap;
  - names are unique.

Where the ledger lives is instance configuration (`phases.ledger` in docsys.yaml);
the ledger itself is the project's state, kept with steering, not with the gate's
configuration, because it changes at phase boundaries and by a ruling, not when the
tooling does. Reads it through scripts/yaml_frontmatter.py's StrictLoader, so scalars
stay strings and it needs `pyyaml` — the devShell provides it.

    python3 scripts/phase_ledger.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yaml_frontmatter import StrictLoader, yaml  # noqa: E402

TOP_KEYS = ("phases",)
ENTRY_KEYS = ("number", "name", "era", "status")
REQUIRED = ("name", "era", "status")
STATUSES = ("done", "current", "planned")  # in the order the list must follow
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NUMBER_RE = re.compile(r"^[1-9][0-9]*$")


def parse(text):
    """The ledger as loaded: StrictLoader keeps every scalar a string."""
    return yaml.load(text, Loader=StrictLoader)


def entry_errors(index, item):
    """One entry's own errors, as messages without the file prefix."""
    where = f"`phases[{index}]`"
    if not isinstance(item, dict):
        return [f"{where} is not a mapping — fix: write it as `{{number: N, name: …, era: …, status: …}}`"]
    label = f"{where} ({item['name']})" if isinstance(item.get("name"), str) else where
    unknown = sorted(set(item) - set(ENTRY_KEYS))
    if unknown:
        return [f"{label} has unknown key(s) {unknown} — fix: remove them; allowed: {list(ENTRY_KEYS)}"]
    missing = [k for k in REQUIRED if k not in item]
    if missing:
        return [f"{label} is missing {missing} — fix: add them; every phase has a name, an era and a status"]
    errors = []
    for key in ("name", "era"):
        if not isinstance(item[key], str) or not SLUG_RE.match(item[key]):
            errors.append(f"{label} {key} {item[key]!r} is not hyphen-cased (a-z, 0-9, -) — "
                          f"fix: rewrite it in lowercase words joined by hyphens")
    status = item["status"]
    if status not in STATUSES:
        errors.append(f"{label} status {status!r} is not one of done, current or planned — "
                      f"fix: use one of the three")
    elif status == "planned" and "number" in item:
        errors.append(f"{label} is planned and has a number; a planned phase has no number (ADR-038) — "
                      f"fix: remove `number`; it is given when the phase starts and becomes `current`")
    elif status != "planned" and "number" not in item:
        errors.append(f"{label} is {status} and has no number — fix: add `number`, one more than the phase before it")
    if "number" in item and (not isinstance(item["number"], str) or not NUMBER_RE.match(item["number"])):
        errors.append(f"{label} number {item['number']!r} is not a positive integer — "
                      f"fix: write a bare number with no leading zero, e.g. `number: 6`")
    return errors


def order_errors(phases):
    """Errors across well-formed entries: uniqueness, one current, order, numbering."""
    errors = []
    seen = set()
    for index, item in enumerate(phases):
        if item["name"] in seen:
            errors.append(f"`phases[{index}]` name {item['name']!r} is a duplicate — fix: give each phase its own name")
        seen.add(item["name"])
    current = [item for item in phases if item["status"] == "current"]
    if len(current) != 1:
        errors.append(f"exactly one phase must be current, found {len(current)} — "
                      f"fix: mark the phase in progress `current`, and only that one")
    rank = [STATUSES.index(item["status"]) for item in phases]
    for index in range(1, len(phases)):
        if rank[index] < rank[index - 1]:
            errors.append(f"`phases[{index}]` ({phases[index]['name']}) is {phases[index]['status']} after a "
                          f"{phases[index - 1]['status']} phase; the order is every done, then the current, "
                          f"then every planned — fix: move it to its place in the list")
            break
    expected = 1
    for index, item in enumerate(phases):
        if "number" not in item:
            continue
        if int(item["number"]) != expected:
            errors.append(f"`phases[{index}]` ({item['name']}) has number {item['number']}, expected {expected}; "
                          f"numbers count 1, 2, 3… in list order — fix: renumber it {expected}, or restore the "
                          f"missing phase")
            break
        expected += 1
    return errors


def ledger_errors(data, path):
    """Every rule the ledger breaks, as messages that start with `path` and name the
    fix. Entry errors are reported alone: the order rules read well-formed entries."""
    def at(messages):
        return [f"{path}: {m}" for m in messages]

    if not isinstance(data, dict):
        return at(["must be a mapping with a `phases:` list — fix: see the comment at the top of the file"])
    unknown = sorted(set(data) - set(TOP_KEYS))
    if unknown:
        return at([f"unknown top-level key(s) {unknown} — fix: remove them; the vocabulary is closed: {list(TOP_KEYS)}"])
    if "phases" not in data:
        return at(["`phases` is missing — fix: add a `phases:` list of the project's phases, in order"])
    phases = data["phases"]
    if not isinstance(phases, list) or not phases:
        return at(["`phases` must list at least one phase — fix: list the phases in order, one of them `current`"])
    errors = [m for index, item in enumerate(phases) for m in entry_errors(index, item)]
    if errors:
        return at(errors)
    return at(order_errors(phases))


def main():
    from docsys_config import ConfigError, load_config
    try:
        path = load_config()["phases"]["ledger"]
    except ConfigError as exc:
        print(f"PHASE LEDGER: {exc}")
        return 1
    if not os.path.exists(path):
        print(f"PHASE LEDGER: {path}: does not exist — fix: restore it from git, or correct "
              f"`phases.ledger` in docsys.yaml")
        return 1
    with open(path, encoding="utf-8") as fh:
        try:
            data = parse(fh)
        except yaml.YAMLError as exc:
            print(f"PHASE LEDGER: {path}: is not valid YAML ({exc}) — fix: correct the YAML")
            return 1
    errors = ledger_errors(data, path)
    for message in errors:
        print(f"PHASE LEDGER: {message}")
    if errors:
        return 1
    current = next(item for item in data["phases"] if item["status"] == "current")
    print(f"Phase ledger OK: {len(data['phases'])} phases, current is "
          f"{current['number']} — {current['name']} ({current['era']}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
