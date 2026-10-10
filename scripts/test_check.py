#!/usr/bin/env python3
"""Fixture test for the gate's runner (Phase 12 T1(c)).

`scripts/check.py` prints a `=== name ===` header, then runs a check that writes to
the same stdout. When that stdout is a pipe — CI logs, a coding agent, anything that
is not a terminal — the runner's own prints sit in a block buffer while the child
writes straight through, so every header lands after every check's output and the
failure lines cannot be attributed to the check that produced them. The gate's
machine reader (`reader: M`) is exactly the reader that sees a pipe.

This runs the runner over three synthetic checks with a pipe on stdout, and pins:

  1. each header immediately precedes its own check's output;
  2. a failing check does not stop the ones after it — the gate is a conjunction, and
     a reader needs every failure in one run, not the first;
  3. the summary names the failing check, and the exit status is non-zero;
  4. outside the devShell, with no `nix` to re-enter it, the gate runs no check and
     fails with the instruction, rather than run on whatever versions are installed.

    python3 scripts/test_check.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

DRIVER = f"""
import sys
sys.path.insert(0, {HERE!r})
import check
py = sys.executable
sys.exit(check.run_checks([
    ("first",  [py, "-c", "print('out-first')"], None),
    ("second", [py, "-c", "import sys; print('out-second'); sys.exit(1)"], None),
    ("third",  [py, "-c", "print('out-third')"], None),
]))
"""

EXPECTED_ORDER = [
    "=== first ===", "out-first",
    "=== second ===", "out-second",
    "=== third ===", "out-third",
]


def main():
    proc = subprocess.run([sys.executable, "-c", DRIVER], stdout=subprocess.PIPE, text=True)
    lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
    failures = 0

    def report(ok, name, detail=""):
        nonlocal failures
        print(f"{'ok   ' if ok else 'FAIL '} {name}{'' if ok else ': ' + detail}")
        failures += not ok

    report(lines[:len(EXPECTED_ORDER)] == EXPECTED_ORDER,
           "each header directly precedes its own check's output (piped stdout)",
           f"expected {EXPECTED_ORDER}, got {lines}")
    report("out-third" in lines, "a failing check does not stop the checks after it")
    report(any(ln.startswith("GATE FAILED") and "second" in ln and "first" not in ln
               and "third" not in ln for ln in lines),
           "the summary names exactly the failing check")
    report(proc.returncode == 1, "the exit status is non-zero", f"got {proc.returncode}")

    # Outside the devShell, on a PATH holding git and nothing else (so no nix), even
    # with an interpreter that can import pyyaml.
    with tempfile.TemporaryDirectory() as bindir:
        os.symlink(shutil.which("git"), os.path.join(bindir, "git"))
        env = {k: v for k, v in os.environ.items() if k != "DOCSYS_DEVSHELL"}
        env["PATH"] = bindir
        outside = subprocess.run([sys.executable, os.path.join(HERE, "check.py")],
                                 capture_output=True, text=True, env=env)
    said = outside.stdout + outside.stderr
    report(outside.returncode != 0 and "=== " not in said and "nix develop" in said,
           "outside the devShell and without nix, no check runs and the gate fails naming the fix",
           f"exit {outside.returncode}, output {said[-300:]!r}")

    print()
    if failures:
        print(f"gate runner: {failures} case(s) FAILED")
        return 1
    print("gate runner: all cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
