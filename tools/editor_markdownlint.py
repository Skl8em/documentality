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

    python3 tools/editor_markdownlint.py
"""

import json
import os
import re
import subprocess
import sys
from typing import Final, TypeGuard

EXTENSION_ID: Final = "davidanson.vscode-markdownlint"
EXTENSIONS_INDEX: Final = os.path.expanduser("~/.vscode/extensions/extensions.json")
BANNER_RE: Final = re.compile(r"^markdownlint-cli2 v(\S+) ")


def is_mapping(value: object) -> TypeGuard[dict[str, object]]:
    return isinstance(value, dict)


def is_list(value: object) -> TypeGuard[list[object]]:
    return isinstance(value, list)


def field(value: object, *path: str) -> str:
    """The string at `path` inside nested mappings of the JSON VS Code writes; a
    ValueError naming the path when the shape differs."""
    for key in path:
        value = value.get(key) if is_mapping(value) else None
    if not isinstance(value, str):
        raise ValueError(
            f"VS Code's JSON has no string at {'.'.join(path)} — fix: update this check to the shape VS Code now writes"
        )
    return value


def load(path: str) -> object:
    """A JSON file as untyped data, narrowed by the caller."""
    with open(path, encoding="utf-8") as fh:
        data: object = json.load(fh)  # pyright: ignore[reportAny] -- json is untyped; this is the boundary
    return data


def pinned_version(banner: str) -> str:
    """The version in markdownlint-cli2's banner, its first line of output."""
    m = BANNER_RE.match(banner)
    if not m:
        raise ValueError(
            f"cannot read a version from markdownlint-cli2's banner {banner.splitlines()[:1]} — "
            "fix: run the check inside the devShell (nix develop), where it is pinned"
        )
    return m.group(1)


def find_extension(entries: object) -> list[tuple[str, str]]:
    """Every installed copy of the extension in VS Code's extensions.json, as
    [(version, directory)]. VS Code compares ids without regard to case."""
    if not is_list(entries):
        raise ValueError(
            "VS Code's extensions.json is not a list — fix: update this check to the shape VS Code now writes"
        )
    return [
        (field(e, "version"), field(e, "location", "path"))
        for e in entries
        if field(e, "identifier", "id").lower() == EXTENSION_ID
    ]


def compare(pinned: str, found: list[tuple[str, str]]) -> list[str]:
    """The disagreements between the pinned markdownlint-cli2 and the installed
    extension(s), each given as (extension version, the markdownlint-cli2 it
    bundles); [] when they agree."""
    if len(found) > 1:
        versions = ", ".join(v for v, _ in found)
        return [
            f"{len(found)} copies of {EXTENSION_ID} are installed ({versions}), so which one the editor "
            f"runs is unknown — fix: uninstall all but one"
        ]
    return [
        f"the extension {EXTENSION_ID} v{version} bundles markdownlint-cli2 {bundled}, the gate runs {pinned} "
        f"(flake.lock), so the editor and the gate can disagree on the same file — fix: install the "
        f"release of the extension that bundles {pinned} (steering/environment.md names it), "
        f"or move the flake to {bundled}"
        for version, bundled in found
        if bundled != pinned
    ]


def main() -> int:
    if not os.path.exists(EXTENSIONS_INDEX):
        print(f"No VS Code extensions on this machine ({EXTENSIONS_INDEX}): no editor to compare with.")
        return 0
    try:
        installed = find_extension(load(EXTENSIONS_INDEX))
        if not installed:
            print(f"{EXTENSION_ID} is not installed: no editor to compare with.")
            return 0
        found = [
            (version, field(load(os.path.join(directory, "package.json")), "dependencies", "markdownlint-cli2"))
            for version, directory in installed
        ]
        banner = subprocess.run(["markdownlint-cli2"], capture_output=True, text=True, check=False).stdout
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
    print(
        f"Editor markdownlint OK ({EXTENSION_ID} v{found[0][0]} bundles markdownlint-cli2 {pinned}, "
        "the version the gate runs)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
