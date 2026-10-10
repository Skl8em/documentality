#!/usr/bin/env python3
"""The editor lints Markdown with the markdownlint-cli2 the gate runs.

The VS Code extension (davidanson.vscode-markdownlint) cannot be pointed at the
devShell's markdownlint-cli2: it lints with the copy it bundles. The two share the
configuration and the custom rule, so they agree only when that bundled copy is the
version flake.lock pins — and markdownlint's version is part of the contract with
the custom rule. This check compares the two, on the machine it runs on.

Where VS Code has no extensions (CI), or the extension is not installed, there is no
editor to disagree with, and the check passes saying so.

Needs the devShell: the pinned version is read from the markdownlint-cli2 on PATH.

    python3 scripts/editor_markdownlint.py
"""
import json
import os
import re
import subprocess
import sys

EXTENSION_ID = "davidanson.vscode-markdownlint"
EXTENSIONS_INDEX = os.path.expanduser("~/.vscode/extensions/extensions.json")
BANNER_RE = re.compile(r"^markdownlint-cli2 v(\S+) ")


def pinned_version(banner):
    """The version in markdownlint-cli2's banner, its first line of output."""
    m = BANNER_RE.match(banner)
    if not m:
        raise ValueError(f"cannot read a version from markdownlint-cli2's banner {banner.splitlines()[:1]} — "
                         "fix: run the check inside the devShell (nix develop), where it is pinned")
    return m.group(1)


def find_extension(entries):
    """Every installed copy of the extension in VS Code's extensions.json, as
    [(version, directory)]. VS Code compares ids without regard to case."""
    return [(e["version"], e["location"]["path"]) for e in entries
            if e["identifier"]["id"].lower() == EXTENSION_ID]


def compare(pinned, found):
    """The disagreements between the pinned markdownlint-cli2 and the installed
    extension(s), each given as (extension version, the markdownlint-cli2 it
    bundles); [] when they agree."""
    if len(found) > 1:
        versions = ", ".join(v for v, _ in found)
        return [f"{len(found)} copies of {EXTENSION_ID} are installed ({versions}), so which one the editor "
                f"runs is unknown — fix: uninstall all but one"]
    return [f"the extension {EXTENSION_ID} v{version} bundles markdownlint-cli2 {bundled}, the gate runs {pinned} "
            f"(flake.lock), so the editor and the gate can disagree on the same file — fix: install the "
            f"release of the extension that bundles {pinned} (steering/environment.md names it), "
            f"or move the flake to {bundled}"
            for version, bundled in found if bundled != pinned]


def main():
    if not os.path.exists(EXTENSIONS_INDEX):
        print(f"No VS Code extensions on this machine ({EXTENSIONS_INDEX}): no editor to compare with.")
        return 0
    with open(EXTENSIONS_INDEX, encoding="utf-8") as fh:
        installed = find_extension(json.load(fh))
    if not installed:
        print(f"{EXTENSION_ID} is not installed: no editor to compare with.")
        return 0

    found = []
    for version, directory in installed:
        with open(os.path.join(directory, "package.json"), encoding="utf-8") as fh:
            found.append((version, json.load(fh)["dependencies"]["markdownlint-cli2"]))
    banner = subprocess.run(["markdownlint-cli2"], capture_output=True, text=True, check=False).stdout
    try:
        pinned = pinned_version(banner)
    except ValueError as exc:
        print(f"EDITOR MARKDOWNLINT: {exc}")
        return 1

    errors = compare(pinned, found)
    if errors:
        print(f"EDITOR MARKDOWNLINT: {len(errors)} disagreement(s)")
        for msg in errors:
            print(f"  {msg}")
        return 1
    print(f"Editor markdownlint OK ({EXTENSION_ID} v{found[0][0]} bundles markdownlint-cli2 {pinned}, "
          "the version the gate runs).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
