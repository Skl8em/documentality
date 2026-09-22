#!/usr/bin/env python3
"""The documentation gate — run every check, in order, and fail if any fails.

  1. worktree         no untracked cruft on disk (the gate reads git, so it must
                      also notice what git is NOT tracking)
  2. linkcheck        every relative markdown link resolves
  3. schema_drift     schema/frontmatter-rules.json still matches its YAML source
  4. frontmatter_test the YAML frontmatter parser still reads what it must
  5. frontmatter_lint the frontmatter invariants (warns on what is still open)
  6. ulid_test        the referential-integrity checks still flag what they must
  7. ulid_check       every frontmatter `id` is a valid, unique ULID, and every
                      `supersedes`/`superseded-by` resolves, is symmetric, and
                      agrees with the central register
  8. slug_check       filename stem == frontmatter `slug` (ADR-028)
  9. hash_check       every frozen record's fixity seal still matches
 10. md100_test       the custom sentence-per-line rule still flags what it must
 11. markdownlint     one shared ruleset incl. one-sentence-per-line (ADR-021)

This is what pre-commit and CI run. This file itself is stdlib-only, but the
validators it runs need two things from the devShell: `pyyaml` (the frontmatter
parser, Phase 11 T2) and markdownlint-cli2 (a Node tool). Without `pyyaml` the
whole gate re-runs itself under `nix develop --command`; markdownlint-cli2 alone
falls back the same way. So the gate works both inside and outside the shell.

    python3 scripts/check.py
"""
import importlib.util
import os
import shutil
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)
PY = sys.executable


def ensure_pyyaml():
    """Re-enter the gate inside the devShell if this interpreter lacks `pyyaml`.
    Fails loud when nix is unavailable too — never a silent skip of the YAML checks."""
    if importlib.util.find_spec("yaml") is not None:
        if os.environ.get("DOCSYS_DEVSHELL") != "1":
            print("WARNING: using pyyaml from this interpreter — not the pinned devShell "
                  "version. Enter `nix develop` for the guaranteed version.")
        return
    if os.environ.get("DOCSYS_DEVSHELL") != "1" and shutil.which("nix"):
        print("pyyaml not importable here — re-running the gate inside the devShell.")
        sys.stdout.flush()
        os.execvp("nix", ["nix", "develop", "--command", "python3", "scripts/check.py", *sys.argv[1:]])
    raise SystemExit("GATE FAILED: pyyaml is not importable and the devShell cannot be entered. "
                     "Install nix and run: nix develop")


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
    ensure_pyyaml()
    checks = [
        ("worktree", worktree_clean),
        ("linkcheck", [PY, "scripts/linkcheck.py"]),
        # Must pass before anything that loads schema/frontmatter-rules.json: a
        # stale generated file would otherwise let a schema edit go unenforced.
        ("schema-drift", [PY, "scripts/generate_schema.py", "--check"]),
        # Parser fixtures run BEFORE the corpus checks, for the same reason as md100
        # below: a green corpus says nothing if the parser has stopped reading it.
        ("frontmatter-parser", [PY, "scripts/test_frontmatter_lint.py"]),
        ("frontmatter", [PY, "scripts/frontmatter_lint.py"]),
        # Same reasoning as frontmatter-parser above: fixtures for the referential
        # checks run before the corpus check they gate.
        ("ulid-test", [PY, "scripts/test_ulid_check.py"]),
        ("ulid", [PY, "scripts/ulid_check.py"]),
        ("slug", [PY, "scripts/slug_check.py"]),
        ("hash", [PY, "scripts/hash_check.py"]),
        # The rule is a heuristic; its fixtures run BEFORE the corpus lint, so a
        # green corpus can never be read as "the rule works" when it has stopped
        # flagging anything.
        ("md100", [PY, "tools/markdownlint/test_sentence_per_line.py"]),
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
