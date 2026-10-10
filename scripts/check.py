#!/usr/bin/env python3
"""The documentation gate — run every check, in order, and fail if any fails.

Which checks, and in what order, is instance configuration: docsys.yaml `checks:`,
where each entry carries the reason for its place. This file is the runner — it
loads that list, runs each entry, and reports which failed. It has no list of its
own to drift out of step.

This is what pre-commit and CI run. This file itself is stdlib-only, but the
validators it runs need two things from the devShell: `pyyaml` (the frontmatter
parser, Phase 11 T2) and markdownlint-cli2 (a Node tool), at the versions its
flake.lock pins. Outside the shell, the whole gate re-runs itself under
`nix develop --command`; without nix it fails rather than run on other versions.

    python3 scripts/check.py
"""
import os
import shutil
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)
PY = sys.executable


def ensure_devshell():
    """Run the gate inside the devShell, where `pyyaml` and every tool are the pinned
    versions: re-enter it through `nix develop` when not already in it, whatever
    else this interpreter can import. Fails loud when nix is unavailable — never a
    run on unpinned versions."""
    if os.environ.get("DOCSYS_DEVSHELL") == "1":
        return
    if shutil.which("nix"):
        print("Not in the devShell — re-running the gate inside it.")
        sys.stdout.flush()
        os.execvp("nix", ["nix", "develop", "--command", "python3", os.path.abspath(__file__), *sys.argv[1:]])
    raise SystemExit("GATE FAILED: the gate runs in the Nix devShell, and nix is not available — "
                     "fix: install nix, then run: nix develop --command python3 scripts/check.py")


def pinned_tool_cmd(tool):
    # Inside the devShell (ensure_devshell), the pinned tool is the one on PATH.
    return [tool] if shutil.which(tool) else None


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


# What `builtin:` may name in docsys.yaml (docsys_config.BUILTINS).
BUILTINS = {"worktree": worktree_clean}


def resolve(check):
    """One docsys.yaml `checks:` entry -> what to run: a callable, an argv list, or
    None when a pinned tool cannot be found."""
    if "builtin" in check:
        return BUILTINS[check["builtin"]]
    if "python" in check:
        return [PY, check["python"], *check.get("args", [])]
    return pinned_tool_cmd(check["tool"])


def run_checks(checks):
    """Run each (name, cmd, tool) in order and report. A failing check does not stop
    the ones after it: the gate is the conjunction of every check, and a reader
    needs every failure from one run.

    stdout is flushed before each check runs: a child writes straight to the shared
    file descriptor, so when stdout is a pipe (CI, an agent) an unflushed header
    would surface after the check's own output and misattribute it."""
    failures = []
    for name, cmd, tool in checks:
        print(f"\n=== {name} ===", flush=True)
        if callable(cmd):
            if cmd() != 0:
                failures.append(name)
            continue
        if cmd is None:
            print(f"FAIL — {tool} is not on the devShell's PATH — "
                  "fix: add it to the devShell's packages in flake.nix")
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


def main():
    ensure_devshell()
    from docsys_config import ConfigError, load_config  # after ensure_devshell: needs pyyaml
    try:
        checks = [(c["name"], resolve(c), c.get("tool")) for c in load_config()["checks"]]
    except ConfigError as exc:
        print(f"GATE FAILED: {exc}")
        return 1
    return run_checks(checks)


if __name__ == "__main__":
    sys.exit(main())
