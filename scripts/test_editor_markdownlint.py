#!/usr/bin/env python3
"""Fixture test for the editor-markdownlint check's verdicts and messages.

The check's logic is three pure functions — read the pinned version from
markdownlint-cli2's banner, find the extension among VS Code's installed ones,
compare the two versions — so each case is a string or a small list, not a VS Code
installation. Every message must name the edit that clears it, after `fix:`.

    python3 scripts/test_editor_markdownlint.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editor_markdownlint as em  # noqa: E402

FIX_MARKER = "fix:"


def entry(ext_id, version):
    """One entry of VS Code's extensions.json, reduced to what the check reads."""
    return {"identifier": {"id": ext_id}, "version": version,
            "location": {"path": f"/ext/{ext_id}-{version}"}}


def messages_verdict(got, fragments):
    """None when `got` holds one message per fragment, each carrying it and a fix
    clause; else why not."""
    if len(got) != len(fragments):
        return f"expected {fragments}, got {got}"
    for msg, fragment in zip(got, fragments):
        if fragment not in msg:
            return f"expected {fragment!r} in {msg!r}"
        if FIX_MARKER not in msg:
            return f"message without a `{FIX_MARKER}` clause: {msg!r}"
    return None


def case_banner():
    got = em.pinned_version("markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)\nhttps://...")
    return None if got == "0.17.2" else f"expected 0.17.2, got {got!r}"


def case_banner_unreadable():
    try:
        em.pinned_version("command not found")
    except ValueError as exc:
        return None if FIX_MARKER in str(exc) else f"message without a `{FIX_MARKER}` clause: {exc}"
    return "an unreadable banner was accepted"


def case_find_one():
    got = em.find_extension([entry("charliermarsh.ruff", "2026.86.0"), entry(em.EXTENSION_ID, "0.59.0")])
    want = [("0.59.0", f"/ext/{em.EXTENSION_ID}-0.59.0")]
    return None if got == want else f"expected {want}, got {got}"


def case_find_case_insensitive():
    # VS Code compares extension ids without regard to case.
    got = em.find_extension([entry("DavidAnson.vscode-markdownlint", "0.59.0")])
    return None if len(got) == 1 else f"expected one match, got {got}"


def case_find_none():
    got = em.find_extension([entry("charliermarsh.ruff", "2026.86.0")])
    return None if got == [] else f"expected no match, got {got}"


CASES = [
    ("the pinned version is read from the banner", case_banner),
    ("an unreadable banner is refused, with a fix", case_banner_unreadable),
    ("the extension is found among the others", case_find_one),
    ("the extension id is matched without regard to case", case_find_case_insensitive),
    ("no extension, no match", case_find_none),
    ("the same version on both sides passes",
     lambda: messages_verdict(em.compare("0.17.2", [("0.59.0", "0.17.2")]), [])),
    ("a different bundled version fails, naming both",
     lambda: messages_verdict(em.compare("0.17.2", [("0.62.1", "0.23.2")]), ["0.23.2"])),
    ("a version range is not the pinned version",
     lambda: messages_verdict(em.compare("0.17.2", [("0.59.0", "^0.17.2")]), ["^0.17.2"])),
    ("two installed copies fail: which one the editor runs is unknown",
     lambda: messages_verdict(em.compare("0.17.2", [("0.59.0", "0.17.2"), ("0.62.1", "0.23.2")]),
                              ["2 copies"])),
]


def main():
    failures = 0
    for name, case in CASES:
        why = case()
        print(f"ok    {name}" if why is None else f"FAIL  {name}: {why}")
        failures += why is not None

    print("\n" + "=" * 40)
    if failures:
        print(f"editor-markdownlint check: {failures}/{len(CASES)} case(s) failed")
        return 1
    print(f"editor-markdownlint check: all {len(CASES)} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
