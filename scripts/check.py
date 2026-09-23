#!/usr/bin/env python3
"""The documentation gate — run every check, in order, and fail if any fails.

Which checks, and in what order, is instance configuration: docsys.yaml `checks:`,
where each entry carries the reason for its place. This file is the runner — it
loads that list, runs each entry, and reports which failed. It has no list of its
own to drift out of step.

This is what pre-commit and CI run. This file itself is stdlib-only, but the
validators it runs need two things from the devShell: `pyyaml` (the frontmatter
parser, Phase 11 T2) and markdownlint-cli2 (a Node tool). Without `pyyaml` the
whole gate re-runs itself under `nix develop --command`; a pinned tool alone falls
back the same way. So the gate works both inside and outside the shell.

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
        os.execvp("nix", ["nix", "develop", "--command", "python3", os.path.abspath(__file__), *sys.argv[1:]])
    raise SystemExit("GATE FAILED: pyyaml is not importable and the devShell cannot be entered. "
                     "Install nix and run: nix develop")


def pinned_tool_cmd(tool):
    # Always prefer the PINNED tool (its version is part of the contract with our
    # custom rules). Inside the devShell it is already on PATH; outside, go
    # through `nix develop` rather than pick up an unrelated global version.
    if os.environ.get("DOCSYS_DEVSHELL") == "1":
        return [tool]
    if shutil.which("nix"):
        return ["nix", "develop", "--command", tool]
    if shutil.which(tool):
        print(f"WARNING: using {tool} from PATH — not the pinned devShell "
              "version. Enter `nix develop` for the guaranteed version.")
        return [tool]
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


def main():
    ensure_pyyaml()
    from docsys_config import ConfigError, load_config  # after ensure_pyyaml: needs it
    try:
        checks = [(c["name"], resolve(c), c.get("tool")) for c in load_config()["checks"]]
    except ConfigError as exc:
        print(f"GATE FAILED: {exc}")
        return 1
    failures = []
    for name, cmd, tool in checks:
        print(f"\n=== {name} ===")
        if callable(cmd):
            if cmd() != 0:
                failures.append(name)
            continue
        if cmd is None:
            print(f"FAIL — {tool} unavailable (no PATH entry and no nix). "
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
