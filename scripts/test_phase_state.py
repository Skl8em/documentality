#!/usr/bin/env python3
"""Fixture test for the phase-state check (Phase 12 T6(b)).

Each rule of phase_state.py is a pure function over the ledger as loaded and the text
or paths it compares against, so each case is in memory, not a repository. Every
rule is shown failing on a synthetic mismatch and passing once it is corrected, and
the cases also pin what a rule must NOT flag: a frozen record naming a phase that has
since started, the era name "Phase II". Every message names where, and after `fix:`,
the edit that clears it.

    python3 scripts/test_phase_state.py
"""
import copy
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phase_state  # noqa: E402

LEDGER = {"phases": [
    {"number": "1", "name": "start", "era": "first", "status": "done"},
    {"number": "2", "name": "build", "era": "second", "status": "done"},
    {"number": "3", "name": "harden", "era": "second", "status": "current"},
    {"name": "deploy", "era": "second", "status": "planned"},
]}
ROOT = "phases"
FOLDER = "phase-{number:02d}-{name}"
FIELD = "{number:02d}-{name}"
MARKERS = {"done": "done", "current": "in progress", "planned": "unnumbered"}
ROW = re.compile(r"^\| \*\*(?:(?P<number>\d+) — )?[^*]+\*\*(?: \*\((?P<marker>[^)]*)\)\*)?")
STATUS = re.compile(r"^\*\*v\S+ \(Phase (?P<number>\d+) (?:in progress|complete)\)\*\*")
MENTION = re.compile(r"\b[Pp]hases?[ -](?P<number>\d+)")


def ledger(**top):
    data = copy.deepcopy(LEDGER)
    data.update(top)
    return data


def files(*folders):
    return [f"{ROOT}/{f}/README.md" for f in folders] + ["phases/README.md", "steering/roadmap.md"]


ALL_FOLDERS = ("first/phase-01-start", "second/phase-02-build", "second/phase-03-harden")

FOLDER_CASES = [
    ("every numbered phase has its folder", files(*ALL_FOLDERS), []),
    ("a done phase without its folder", files(ALL_FOLDERS[0], ALL_FOLDERS[2]),
     [["phases/second/phase-02-build", "does not exist"]]),
    ("a folder the ledger does not list", files(*ALL_FOLDERS, "second/phase-04-deploy"),
     [["phases/second/phase-04-deploy", "not in the ledger"]]),
    ("a folder under the wrong era", files(ALL_FOLDERS[0], "first/phase-02-build", ALL_FOLDERS[2]),
     [["phases/second/phase-02-build", "does not exist"], ["phases/first/phase-02-build", "not in the ledger"]]),
]

TABLE = """| Phase | Aim |
|---|---|
| **01 — Start** *(done)* | x |
| **02 — Build** *(done — closed late)* | x |
| **03 — Harden** *(in progress — T1 done)* | x |
| **Deploy** *(unnumbered — see below)* | x |
"""


def table(old, new):
    assert old in TABLE
    return TABLE.replace(old, new)


TABLE_CASES = [
    ("every row carries the ledger's marker", TABLE, []),
    ("the current phase marked done", table("*(in progress — T1 done)*", "*(done)*"),
     [["t.md:5", "phase 3", "done", "in progress"]]),
    ("a done phase still marked next", table("*(done — closed late)*", "*(next)*"),
     [["t.md:4", "phase 2", "next", "done"]]),
    ("a planned phase numbered in a table (ADR-038)", table("**Deploy**", "**04 — Deploy**"),
     [["t.md:6", "phase 4", "not numbered in the ledger", "ADR-038"]]),
    ("an unnumbered row that is not marked planned", table("*(unnumbered — see below)*", "*(done)*"),
     [["t.md:6", "unnumbered", "done"]]),
    ("a row with no marker", table(" *(done — closed late)*", ""), [["t.md:4", "no status marker"]]),
    ("the current phase has no row", table("| **03 — Harden** *(in progress — T1 done)* | x |\n", ""),
     [["t.md", "phase 3", "no row"]]),
    ("a table the pattern matches nowhere", "| Phase |\n|---|\n| 03 Harden | x |\n",
     [["t.md", "no phase row"]]),
]

MENTION_CASES = [
    ("a mention of a numbered phase", {"a.md": "Phase 3 builds on Phase 2."}, []),
    ("the era name is not a number", {"a.md": "Designing Phase II follows."}, []),
    ("a frozen record naming a phase that has since started",
     {"phases/first/phase-01-start/plan.md": "Phase 3 will follow, then phase-03-harden."}, []),
    ("a range written with a leading zero", {"a.md": "Phases 01–03 are recorded."}, []),
    ("a phase named by number before it is numbered",
     {"a.md": "intro\nPhase 4 will deploy it."}, [["a.md:2", "Phase 4", "3", "ADR-038"]]),
    ("a folder-style forward name", {"a.md": "see phase-04-deploy"}, [["a.md:1", "phase-04", "ADR-038"]]),
    ("a frozen record quoting a forward number as its example is not flagged: it cannot be edited",
     {"frozen.md": 'a sentence that says "Phase 4 will ..." passes'}, []),
    ("the same sentence in a living document is",
     {"living.md": 'a sentence that says "Phase 4 will ..." passes'}, [["living.md:1", "Phase 4"]]),
]
FROZEN = {"frozen.md"}

README = "# R\n\n## Status\n\n**v1.0 (Phase 3 in progress)** — what it is.\n"

STATUS_CASES = [
    ("the status line names the current phase", README, []),
    ("the status line names a closed phase", README.replace("Phase 3 in progress", "Phase 2 complete"),
     [["R.md:5", "phase 2", "current phase is 3"]]),
    ("no status line", "# R\n\nNothing here.\n", [["R.md", "no status line"]]),
    ("two status lines", README + "\n**v0.9 (Phase 2 complete)** — old.\n", [["R.md", "2 status lines"]]),
]

LAG = {"path": "old.md", "reason": "not re-read since phase 1; owed at the next close"}

FIELD_CASES = [
    ("a field at the current phase", ledger(), {"a.md": "03-harden"}, []),
    ("a field at the last done phase", ledger(), {"a.md": "02-build"}, []),
    ("a field ahead of the current phase", ledger(), {"a.md": "04-deploy"},
     [["a.md", "04-deploy", "not a numbered phase"]]),
    ("a field that is not in the ledger's format", ledger(), {"a.md": "3-harden"},
     [["a.md", "3-harden", "not a numbered phase"]]),
    ("a field behind the last done phase", ledger(), {"old.md": "01-start"},
     [["old.md", "01-start", "behind", "02-build"]]),
    ("a lagging field the ledger allows, with its reason", ledger(lagging=[LAG]), {"old.md": "01-start"}, []),
    ("an allowance for a document that no longer lags", ledger(lagging=[LAG]), {"old.md": "02-build"},
     [["old.md", "lagging", "no longer"]]),
    ("an allowance for a document with no phase field", ledger(lagging=[LAG]), {},
     [["old.md", "lagging", "no `phase:`"]]),
]

FIX_MARKER = "fix:"


def verdict(got, expected):
    """None when `got` holds one message per entry of `expected`, in order, each
    containing that entry's fragments and a fix clause; else why not."""
    if len(got) != len(expected):
        return f"expected {len(expected)} error(s) {expected}, got {got}"
    for msg, fragments in zip(got, expected):
        missing = [f for f in fragments if f not in msg]
        if missing:
            return f"expected {missing} in {msg!r}"
        if FIX_MARKER not in msg:
            return f"message without a `{FIX_MARKER}` clause: {msg!r}"
    return None


def run(name, got, expected):
    why = verdict(got, expected)
    print(f"ok    {name}" if why is None else f"FAIL  {name}: {why}")
    return why is not None


def main():
    failures = total = 0
    for name, tracked, expected in FOLDER_CASES:
        failures += run(name, phase_state.folder_errors(LEDGER, ROOT, FOLDER, tracked), expected)
    for name, text, expected in TABLE_CASES:
        failures += run(name, phase_state.table_errors(LEDGER, MARKERS, "t.md", ROW, text), expected)
    for name, docs, expected in MENTION_CASES:
        failures += run(name, phase_state.mention_errors(LEDGER, MENTION, docs, FROZEN), expected)
    for name, text, expected in STATUS_CASES:
        failures += run(name, phase_state.status_errors(LEDGER, "R.md", STATUS, text), expected)
    for name, data, fields, expected in FIELD_CASES:
        failures += run(name, phase_state.field_errors(data, FIELD, fields), expected)
    total = len(FOLDER_CASES) + len(TABLE_CASES) + len(MENTION_CASES) + len(STATUS_CASES) + len(FIELD_CASES)
    print("\n" + "=" * 40)
    if failures:
        print(f"phase state: {failures}/{total} case(s) failed")
        return 1
    print(f"phase state: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
