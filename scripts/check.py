#!/usr/bin/env python3
"""The documentation gate — run every check, in order, and fail if any fails.

  1. worktree         no untracked cruft on disk (the gate reads git, so it must
                      also notice what git is NOT tracking)
  2. linkcheck        every relative markdown link resolves
  3. frontmatter_lint the frontmatter invariants (warns on what is still open)
  4. ulid_check       every frontmatter `id` is a valid, unique ULID
  5. slug_check       filename stem == frontmatter `slug` (ADR-028)
  6. hash_check       every frozen record's fixity seal still matches
  7. markdownlint     one shared ruleset incl. one-sentence-per-line (ADR-021)

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


def worktree_clean():
    """Fail on untracked files. Every other check reads `git ls-files`, so on-disk
    cruft — a stale copy of a renamed folder, a scratch file — passes them all
    silently. This is the assertion that would have caught the Phase-08 zombies.
    Ignored paths (.gitignore) do not count; modified tracked files do not either,
    since the gate is run precisely to check work in progress."""
    out = subprocess.check_output(
        ["git", "status", "--porcelain", "--untracked-files=normal"], text=True)
    untracked = [ln[3:] for ln in out.splitlines() if ln.startswith("??")]
    if untracked:
        print(f"UNTRACKED PATHS: {len(untracked)} — `git add` them, or add them to .gitignore")
        for p in untracked:
            print(f"  {p}")
        return 1
    print("Worktree OK (nothing untracked).")
    return 0


def main():
    checks = [
        ("worktree", worktree_clean),
        ("linkcheck", [PY, "scripts/linkcheck.py"]),
        ("frontmatter", [PY, "scripts/frontmatter_lint.py"]),
        ("ulid", [PY, "scripts/ulid_check.py"]),
        ("slug", [PY, "scripts/slug_check.py"]),
        ("hash", [PY, "scripts/hash_check.py"]),
        ("markdownlint", markdownlint_cmd()),
    ]
    failures = []
    for name, cmd in checks:
        print(f"\n=== {name} ===")
        if callable(cmd):
            if cmd() != 0:
                failures.append(name)
            continue
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
