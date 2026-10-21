#!/usr/bin/env python3
"""Fixture test for the paired-change check (Phase 12 T3).

`paired_change.py` fails a change to the mechanism (`scripts/`, `schema/`) that does
not also touch a file a human reads for understanding. The unit of "a change" is one
commit, plus the uncommitted work that will become the next one — not the branch:
a phase-long branch nearly always touches some document, so a branch-level rule
passes on exactly the phase (11) that motivated it.

The rule fails only where work lands (`main`, `develop`, or a detached checkout such
as a pull request's merge commit); on any other branch it warns and exits 0. A change
that has nothing to explain — a test file, or a Python edit whose code is unchanged
(comments, docstrings, formatting) — is not a change to the mechanism.

Three layers:

  1. `unpaired` and `comment_only` are pure functions — the rule and its exemption.
  2. `commit_units` / `pending_unit` read git, so they run against a real throwaway
     repository: a synthetic scripts-only commit fails, then passes once a docs file
     joins it; the same for uncommitted work.
  3. `run` decides enforced-or-advisory from the branch, and is exercised on a
     feature branch, on `main`, and on a detached HEAD.

    python3 scripts/test_paired_change.py
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paired_change  # noqa: E402

MECHANISM = ["scripts/", "schema/"]
EXEMPT = ["scripts/test_"]
UNDERSTANDING = ["writing/", "codifying/", "steering/ARCHITECTURE.md"]

# (name, units, labels expected to be reported)
RULE_CASES = [
    ("a scripts-only unit fails", [("c1", ["scripts/x.py"])], ["c1"]),
    ("a schema-only unit fails", [("c1", ["schema/rules.yaml"])], ["c1"]),
    ("the same unit passes once a docs file joins it",
     [("c1", ["scripts/x.py", "codifying/gate.md"])], []),
    ("a unit touching no mechanism is not examined", [("c1", ["README.md"])], []),
    ("a docs-only unit passes", [("c1", ["writing/rules.md"])], []),
    ("a single named file is an accepted pairing",
     [("c1", ["schema/rules.yaml", "steering/ARCHITECTURE.md"])], []),
    ("a sibling of that file is not",
     [("c1", ["schema/rules.yaml", "steering/CONTRIBUTING.md"])], ["c1"]),
    ("the changelog and phase records are not understanding",
     [("c1", ["scripts/x.py", "steering/CHANGELOG.md", "phases/p/plan.md"])], ["c1"]),
    ("each unit stands alone: a later docs commit does not pair an earlier one",
     [("c1", ["scripts/x.py"]), ("c2", ["writing/rules.md"])], ["c1"]),
    ("every offending unit is reported, not the first",
     [("c1", ["scripts/a.py"]), ("c2", ["scripts/b.py", "codifying/x.md"]), ("c3", ["schema/s.yaml"])],
     ["c1", "c3"]),
    ("no units, nothing to report", [], []),
    ("a test-only unit needs no account", [("c1", ["scripts/test_x.py"])], []),
    ("a test beside real mechanism does not excuse the mechanism",
     [("c1", ["scripts/test_x.py", "scripts/x.py"])], ["c1"]),
    ("a comment-only edit (marked trivial by the git layer) needs no account",
     [("c1", ["scripts/x.py"], {"scripts/x.py"})], []),
    ("trivial is per file: another script in the unit still needs one",
     [("c1", ["scripts/x.py", "scripts/y.py"], {"scripts/x.py"})], ["c1"]),
]


def run_rule_cases():
    failures = 0
    for name, units, expected in RULE_CASES:
        got = [o[0] for o in paired_change.unpaired(units, MECHANISM, UNDERSTANDING, EXEMPT)]
        if got == expected:
            print(f"ok    {name}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected {expected}, got {got}")
    return failures


def run_report_case():
    """The report must be self-sufficient for a reader with no other context: name the
    unit, the mechanism files that lacked a pair, where an account would go, and a fix."""
    offenders = paired_change.unpaired([("abc1234 tweak the linter", ["scripts/lint.py"])],
                                       MECHANISM, UNDERSTANDING)
    lines = paired_change.report(offenders, UNDERSTANDING)
    text = "\n".join(lines)
    missing = [f for f in ("abc1234 tweak the linter", "scripts/lint.py", "codifying/", "fix:")
               if f not in text]
    if missing:
        print(f"FAIL  the report names the unit, the file, the accepted places and a fix: lacks {missing}")
        return 1
    print("ok    the report names the unit, the file, the accepted places and a fix")
    return 0


COMMENT_ONLY_CASES = [
    ("a comment added", "x = 1\n", "x = 1  # why\n", True),
    ("a comment removed", "# why\nx = 1\n", "x = 1\n", True),
    ("formatting only", "x = f( 1,2 )\n", "x = f(1, 2)\n", True),
    ("a docstring rewritten", 'def f():\n    """old"""\n    return 1\n',
     'def f():\n    """new, longer"""\n    return 1\n', True),
    ("a docstring added", "def f():\n    return 1\n", 'def f():\n    """doc"""\n    return 1\n', True),
    ("a code change", "x = 1\n", "x = 2\n", False),
    ("a string literal changed (not a docstring)", 'def f():\n    return "a"\n',
     'def f():\n    return "b"\n', False),
    ("a statement added", "x = 1\n", "x = 1\ny = 2\n", False),
    ("the new source does not parse", "x = 1\n", "x = (\n", False),
    ("the old source does not parse", "x = (\n", "x = 1\n", False),
]

ENFORCED_CASES = [
    ("main", ["main", "develop"], True),
    ("develop", ["main", "develop"], True),
    ("a feature branch", ["main", "develop"], False),
    ("a branch that merely contains the word", ["main", "develop"], False),
    ("a detached HEAD (a pull request's merge commit, CI)", ["main", "develop"], True),
]


def run_comment_only_cases():
    failures = 0
    for name, old, new, expected in COMMENT_ONLY_CASES:
        got = paired_change.comment_only(old, new)
        if got == expected:
            print(f"ok    {name}: comment_only is {expected}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected comment_only {expected}, got {got}")
    for name, enforce_on, expected in ENFORCED_CASES:
        branch = None if name.startswith("a detached") else \
            {"main": "main", "develop": "develop", "a feature branch": "feature/x"}.get(name, "maintenance")
        got = paired_change.enforced(branch, enforce_on)
        if got == expected:
            print(f"ok    {name}: enforced is {expected}")
        else:
            failures += 1
            print(f"FAIL  {name}: expected enforced {expected}, got {got}")
    return failures


# --- against a real repository -----------------------------------------------

def git(cwd, *args):
    return subprocess.run(["git", "-C", cwd, "-c", "user.name=t", "-c", "user.email=t@t", *args],
                          check=True, capture_output=True, text=True).stdout.strip()


def write(cwd, path, text):
    full = os.path.join(cwd, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


def commit(cwd, message, files):
    """Commit `files` (path -> text; None deletes)."""
    for path, text in files.items():
        if text is None:
            git(cwd, "rm", "-q", path)
        else:
            write(cwd, path, text)
            git(cwd, "add", path)
    git(cwd, "commit", "-q", "-m", message)
    return git(cwd, "rev-parse", "HEAD")


def offending_labels(cwd, since):
    units = paired_change.commit_units(since, cwd)
    pending = paired_change.pending_unit(cwd)
    if pending:
        units.append(pending)
    return [o[0] for o in paired_change.unpaired(units, MECHANISM, UNDERSTANDING, EXEMPT)]


def run_git_cases():
    failures = 0

    def report(ok, name, detail=""):
        nonlocal failures
        print(f"{'ok   ' if ok else 'FAIL '} {name}{'' if ok else ': ' + detail}")
        failures += not ok

    with tempfile.TemporaryDirectory() as repo:
        git(repo, "init", "-q", "-b", "main")
        # History before the anchor is never examined: it predates the rule.
        commit(repo, "old scripts-only", {"scripts/old.py": "old\n"})
        anchor = commit(repo, "the rule lands", {"writing/a.md": "a\n"})

        report(offending_labels(repo, anchor) == [], "nothing after the anchor: nothing to report")

        commit(repo, "scripts only", {"scripts/x.py": "x\n"})
        got = offending_labels(repo, anchor)
        report(len(got) == 1 and "scripts only" in got[0],
               "a synthetic scripts-only commit fails, naming the commit", str(got))

        # The same change with a docs file in the same commit passes.
        commit(repo, "scripts and docs", {"scripts/y.py": "y\n", "codifying/gate.md": "g\n"})
        got = offending_labels(repo, anchor)
        report(len(got) == 1 and "scripts only" in got[0],
               "the paired commit is fine; only the unpaired one is reported", str(got))

        # A later docs commit does not retroactively pair the earlier one.
        commit(repo, "docs later", {"writing/b.md": "b\n"})
        report(len(offending_labels(repo, anchor)) == 1,
               "a later docs commit does not pair an earlier scripts commit")

        # Advancing the anchor past it is the (visible) way to accept it.
        report(offending_labels(repo, git(repo, "rev-parse", "HEAD")) == [],
               "an anchor at HEAD examines nothing")

        # Deleting a mechanism file is a change to the mechanism.
        deleted = commit(repo, "delete a script", {"scripts/y.py": None})
        got = offending_labels(repo, deleted[:])
        report(got == [], "the anchor commit itself is not examined")
        anchor2 = git(repo, "rev-parse", "HEAD~1")
        got = offending_labels(repo, anchor2)
        report(len(got) == 1 and "delete a script" in got[0],
               "deleting a scripts file without a docs change fails", str(got))

        # Renaming a script out of scripts/ still counts: the old path is a mechanism path.
        git(repo, "mv", "scripts/x.py", "misc_x.py")
        git(repo, "commit", "-q", "-m", "move a script out")
        got = offending_labels(repo, deleted)
        report(len(got) == 1 and "move a script out" in got[0],
               "moving a script out of scripts/ is caught by its old path", str(got))

    with tempfile.TemporaryDirectory() as repo:
        git(repo, "init", "-q", "-b", "main")
        commit(repo, "base", {"scripts/x.py": "x = 1\n", "scripts/test_x.py": "t = 1\n", "writing/a.md": "a\n"})
        anchor = git(repo, "rev-parse", "HEAD")

        commit(repo, "comment only", {"scripts/x.py": "x = 1  # explained\n"})
        report(offending_labels(repo, anchor) == [], "a comment-only commit needs no account")
        commit(repo, "test only", {"scripts/test_x.py": "t = 2\n"})
        report(offending_labels(repo, anchor) == [], "a test-only commit needs no account")
        commit(repo, "real change", {"scripts/x.py": "x = 2  # explained\n"})
        got = offending_labels(repo, anchor)
        report(len(got) == 1 and "real change" in got[0],
               "a code change to the same file still does", str(got))
        commit(repo, "the account", {"codifying/x.md": "x\n"})
        anchor = git(repo, "rev-parse", "HEAD")

        write(repo, "scripts/x.py", "x = 2  # and another\n")
        report(offending_labels(repo, anchor) == [], "uncommitted comment-only work needs no account")
        write(repo, "scripts/x.py", "x = 3\n")
        got = offending_labels(repo, anchor)
        report(len(got) == 1 and "uncommitted" in got[0], "uncommitted code work still does", str(got))
        git(repo, "checkout", "-q", "--", ".")

    with tempfile.TemporaryDirectory() as repo:
        git(repo, "init", "-q", "-b", "main")
        commit(repo, "base", {"scripts/x.py": "x\n", "writing/a.md": "a\n"})
        anchor = git(repo, "rev-parse", "HEAD")

        report(offending_labels(repo, anchor) == [], "a clean tree has no pending unit")

        write(repo, "scripts/x.py", "changed\n")
        got = offending_labels(repo, anchor)
        report(len(got) == 1 and "uncommitted" in got[0],
               "uncommitted scripts work fails, as the next commit would", str(got))

        write(repo, "writing/a.md", "also changed\n")
        report(offending_labels(repo, anchor) == [],
               "the same uncommitted work passes once a docs file is edited beside it")

        write(repo, "scripts/x.py", "x\n")
        report(offending_labels(repo, anchor) == [],
               "a docs-only pending change is fine")

        # A merge commit brings in another line's history, which is that line's to answer for.
        git(repo, "checkout", "-q", "-b", "side")
        git(repo, "checkout", "-q", "--", ".")
        commit(repo, "side: docs and scripts", {"scripts/s.py": "s\n", "writing/s.md": "s\n"})
        git(repo, "checkout", "-q", "-")
        git(repo, "merge", "-q", "--no-ff", "-m", "merge side", "side")
        report(offending_labels(repo, anchor) == [],
               "a merge commit is not itself a unit")

    with tempfile.TemporaryDirectory() as repo:
        git(repo, "init", "-q", "-b", "main")
        commit(repo, "base", {"writing/a.md": "a\n"})
        try:
            paired_change.commit_units("0" * 40, repo)
        except paired_change.AnchorError as exc:
            message = str(exc)
            report("fix:" in message and "since" in message and "docsys.yaml" in message,
                   "an anchor that is not in this history is refused, naming the key and a fix", message)
        else:
            report(False, "an anchor that is not in this history is refused")

        # A shallow clone loses the anchor; the refusal must say so rather than pass vacuously.
        commit(repo, "second", {"writing/b.md": "b\n"})
        commit(repo, "third", {"writing/c.md": "c\n"})
        with tempfile.TemporaryDirectory() as parent:
            clone = os.path.join(parent, "shallow")
            subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + repo, clone],
                           check=True, capture_output=True)
            first = git(repo, "rev-list", "--max-parents=0", "HEAD")
            try:
                paired_change.commit_units(first, clone)
            except paired_change.AnchorError as exc:
                report("fetch" in str(exc), "a shallow clone is refused, and the fix says to fetch full history",
                       str(exc))
            else:
                report(False, "a shallow clone is refused")
    return failures


def run_branch_cases():
    """The same violation is a failure on main and a warning on a feature branch."""
    failures = 0
    cfg = {"since": None, "mechanism": MECHANISM, "understanding": UNDERSTANDING,
           "exempt": EXEMPT, "enforce_on": ["main", "develop"]}

    def report(ok, name, detail=""):
        nonlocal failures
        print(f"{'ok   ' if ok else 'FAIL '} {name}{'' if ok else ': ' + detail}")
        failures += not ok

    with tempfile.TemporaryDirectory() as repo:
        git(repo, "init", "-q", "-b", "main")
        git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
        anchor = commit(repo, "base", {"writing/a.md": "a\n"})
        cfg["since"] = anchor

        code, lines = paired_change.run(cfg, repo)
        report(code == 0 and "OK" in lines[0], "a clean history passes on main", str(lines))

        git(repo, "checkout", "-q", "-b", "feature/x")
        commit(repo, "scripts only", {"scripts/x.py": "x\n"})
        code, lines = paired_change.run(cfg, repo)
        text = "\n".join(lines)
        report(code == 0 and "scripts only" in text and "WARNING" in lines[0] and "feature/x" in text
               and "main" in text,
               "on a feature branch the violation is a warning that names the branch and where it is enforced",
               f"code {code}: {text}")

        git(repo, "checkout", "-q", "main")
        git(repo, "merge", "-q", "--ff-only", "feature/x")
        code, lines = paired_change.run(cfg, repo)
        report(code == 1 and "PAIRED CHANGE" in lines[0] and "scripts only" in "\n".join(lines),
               "the same history fails on main", f"code {code}: {lines}")

        git(repo, "checkout", "-q", "-b", "feature/y")
        git(repo, "checkout", "-q", "--detach")
        code, lines = paired_change.run(cfg, repo)
        report(code == 1, "the same history fails on a detached HEAD (CI on a pull request)", f"code {code}")

        stale = dict(cfg, enforce_on=["trunk", "develop"])
        try:
            paired_change.run(stale, repo)
        except paired_change.BranchListError as exc:
            report("enforce_on" in str(exc) and "trunk" in str(exc) and "fix:" in str(exc),
                   "an enforce_on naming no branch of the repository is refused, naming the key and a fix",
                   str(exc))
        else:
            report(False, "an enforce_on naming no branch of the repository is refused", "it was accepted")

        with tempfile.TemporaryDirectory() as clone:
            git(clone, "clone", "-q", "-b", "main", repo, ".")
            git(clone, "checkout", "-q", "--detach")
            git(clone, "branch", "-q", "-D", "main")
            try:
                paired_change.run(dict(cfg, enforce_on=["main"]), clone)
            except paired_change.BranchListError as exc:
                report(False, "a branch that exists only on a remote counts (CI's detached checkout)", str(exc))
            else:
                report(True, "a branch that exists only on a remote counts (CI's detached checkout)")
    return failures


def main():
    failures = (run_rule_cases() + run_comment_only_cases() + run_report_case()
                + run_git_cases() + run_branch_cases())
    print("\n" + "=" * 40)
    if failures:
        print(f"paired change: {failures} failure(s)")
        return 1
    print("paired change: all cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
