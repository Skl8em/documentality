#!/usr/bin/env python3
"""The documentation gate — run every check, in order, and fail if any fails.

  1. linkcheck        every relative markdown link resolves
  2. frontmatter_lint settled frontmatter invariants (warns on the contested ones)
  3. ulid_check       ULID-named records valid & unique (legacy noted, not failed)
  4. markdownlint     one shared ruleset incl. one-sentence-per-line (ADR-021)

This is what pre-commit and CI run. Stdlib only. markdownlint-cli2 is a Node tool
from the devShell; if it is not on PATH this falls back to `nix develop --command`,
so the gate works both inside and outside the shell.

    python3 scripts/check.py
"""
import os
import shutil
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)
PY = sys.executable


def markdownlint_cmd():
    # Always prefer the PINNED markdownlint (its version is part of the contract
    # with our custom rules). Inside the devShell it is already on PATH; outside,
    # go through `nix develop` rather than pick up an unrelated global version.
    if os.environ.get("DOCSYS_DEVSHELL") == "1":
        return ["markdownlint-cli2"]
    if shutil.which("nix"):
        return ["nix", "develop", "--command", "markdownlint-cli2"]
    if shutil.which("markdownlint-cli2"):
        print("WARNING: using markdownlint-cli2 from PATH — not the pinned devShell "
              "version. Enter `nix develop` for the guaranteed version.")
        return ["markdownlint-cli2"]
    return None


def main():
    checks = [
        ("linkcheck", [PY, "scripts/linkcheck.py"]),
        ("frontmatter", [PY, "scripts/frontmatter_lint.py"]),
        ("ulid", [PY, "scripts/ulid_check.py"]),
        ("markdownlint", markdownlint_cmd()),
    ]
    failures = []
    for name, cmd in checks:
        print(f"\n=== {name} ===")
        if cmd is None:
            print("FAIL — markdownlint-cli2 unavailable (no PATH entry and no nix). "
                  "Enter the devShell: nix develop")
            failures.append(name)
            continue
        if subprocess.call(cmd) != 0:
            failures.append(name)

    print("\n" + "=" * 40)
    if failures:
        print(f"GATE FAILED: {', '.join(failures)}")
        return 1
    print("GATE PASSED: all checks green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
