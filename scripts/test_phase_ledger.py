#!/usr/bin/env python3
"""Fixture test for the phase ledger's own rules (Phase 12 T6(a)).

`ledger_errors` is a pure function over the ledger as loaded, so each case is a small
dict, not a file — the same reason as test_slug_check.py. Scalars arrive as strings
(the StrictLoader keeps them so); one case loads real YAML text to prove that the
fixtures are written the way the loader delivers. Every message names the file and
the edit that clears it, after `fix:`: the gate's reader is often a machine.

    python3 scripts/test_phase_ledger.py
"""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phase_ledger  # noqa: E402

PATH = "steering/phases.yaml"

VALID = {"phases": [
    {"number": "1", "name": "sketch", "era": "naive", "status": "done"},
    {"number": "2", "name": "rework", "era": "second", "status": "done"},
    {"number": "3", "name": "harden", "era": "second", "status": "current"},
    {"name": "deploy", "era": "second", "status": "planned"},
    {"name": "next-design", "era": "third", "status": "planned"},
]}


def with_(mutate):
    data = copy.deepcopy(VALID)
    mutate(data)
    return data


def entry(index, **fields):
    """Replace fields of one entry; a value of None deletes the field."""
    def go(data):
        for key, value in fields.items():
            if value is None:
                data["phases"][index].pop(key, None)
            else:
                data["phases"][index][key] = value
    return go


# (name, ledger as loaded, fragments the ONE expected error must all contain; [] = no error)
CASES = [
    ("a well-formed ledger passes", VALID, []),
    ("a ledger with only a current phase passes",
     {"phases": [{"number": "1", "name": "start", "era": "first", "status": "current"}]}, []),
    ("not a mapping", ["phases"], ["mapping"]),
    ("an unknown top-level key", with_(lambda d: d.update(eras=[])), ["eras", "unknown"]),
    ("no phases list", {}, ["`phases`", "missing"]),
    ("an empty phases list", {"phases": []}, ["`phases`", "at least one"]),
    ("an entry that is not a mapping", with_(lambda d: d["phases"].__setitem__(0, "sketch")),
     ["phases[0]", "mapping"]),
    ("an unknown key in an entry", with_(entry(0, title="Sketch")), ["phases[0]", "title", "unknown"]),
    ("an entry without a status", with_(entry(0, status=None)), ["phases[0]", "status", "missing"]),
    ("a status outside the vocabulary", with_(entry(0, status="closed")),
     ["phases[0]", "closed", "done, current or planned"]),
    ("a name that is not hyphen-cased", with_(entry(0, name="Sketch_1")), ["phases[0]", "Sketch_1", "hyphen-cased"]),
    ("an era that is not hyphen-cased", with_(entry(0, era="Naive Sketch")),
     ["phases[0]", "Naive Sketch", "hyphen-cased"]),
    ("a planned phase with a number (ADR-038)", with_(entry(3, number="4")),
     ["phases[3]", "planned", "no number", "ADR-038"]),
    ("a done phase without a number", with_(entry(0, number=None)), ["phases[0]", "done", "number"]),
    ("a number that is not a positive integer", with_(entry(0, number="one")), ["phases[0]", "'one'", "integer"]),
    ("a zero-padded number", with_(entry(0, number="01")), ["phases[0]", "'01'", "integer"]),
    ("a duplicate name", with_(entry(1, name="sketch")), ["phases[1]", "sketch", "duplicate"]),
    ("two current phases", with_(entry(1, status="current")), ["current", "exactly one", "2"]),
    ("no current phase", with_(entry(2, status="done")), ["current", "exactly one", "0"]),
    ("a planned phase listed before a done one",
     {"phases": [{"name": "deploy", "era": "e", "status": "planned"},
                 {"number": "1", "name": "start", "era": "e", "status": "current"}]},
     ["phases[1]", "order"]),
    ("numbers that skip one", with_(entry(2, number="4")), ["phases[2]", "4", "3"]),
    ("numbers that do not start at 1",
     {"phases": [{"number": "2", "name": "start", "era": "e", "status": "current"}]},
     ["phases[0]", "2", "1"]),
]

FIX_MARKER = "fix:"


def verdict(got, fragments):
    """None when `got` is empty and no error is expected, or holds exactly one
    message that names the file, contains every fragment and carries a fix clause;
    else why not."""
    if not fragments:
        return None if not got else f"expected no error, got {got}"
    if len(got) != 1:
        return f"expected one error containing {fragments}, got {got}"
    msg = got[0]
    if not msg.startswith(PATH + ":"):
        return f"message does not start with the file's name: {msg!r}"
    missing = [f for f in fragments if f not in msg]
    if missing:
        return f"expected {missing} in {msg!r}"
    if FIX_MARKER not in msg:
        return f"message without a `{FIX_MARKER}` clause: {msg!r}"
    return None


def from_text_case():
    """The fixtures above write numbers as strings; this proves that is what the
    loader delivers, so a green fixture run is about the real file's shape."""
    text = ("phases:\n"
            "  - {number: 1, name: start, era: first, status: done}\n"
            "  - {number: 2, name: next, era: first, status: current}\n"
            "  - {name: later, era: first, status: planned}\n")
    data = phase_ledger.parse(text)
    if data["phases"][0]["number"] != "1":
        return f"the loader delivered {data['phases'][0]['number']!r}, not the string '1' the fixtures assume"
    return verdict(phase_ledger.ledger_errors(data, PATH), [])


def main():
    failures = 0
    for name, data, fragments in CASES:
        why = verdict(phase_ledger.ledger_errors(data, PATH), fragments)
        print(f"ok    {name}" if why is None else f"FAIL  {name}: {why}")
        failures += why is not None

    name = "a ledger read from YAML text is checked as the fixtures assume"
    why = from_text_case()
    print(f"ok    {name}" if why is None else f"FAIL  {name}: {why}")
    failures += why is not None

    total = len(CASES) + 1
    print("\n" + "=" * 40)
    if failures:
        print(f"phase ledger: {failures}/{total} case(s) failed")
        return 1
    print(f"phase ledger: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
