#!/usr/bin/env python3
"""Fixture test for the paired-change check (Phase 12 T3).

`paired_change.py` fails a change to the mechanism (`scripts/`, `schema/`) that does
not also touch a file a human reads for understanding. The unit of "a change" is one
commit, plus the uncommitted work that will become the next one — not the branch:
a phase-long branch nearly always touches some document, so a branch-level rule
passes on exactly the phase (11) that motivated it.

Two layers, because the rule has two halves:

  1. `unpaired` is a pure function over (label, changed paths) units — the rule.
  2. `commit_units` / `pending_unit` read git, so they run against a real throwaway
     repository: a synthetic scripts-only commit fails, then passes once a docs file
     joins it; the same for uncommitted work.

    python3 scripts/test_paired_change.py
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paired_change  # noqa: E402

MECHANISM = ["scripts/", "schema/"]
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
]


def run_rule_cases():
    failures = 0
    for name, units, expected in RULE_CASES:
        got = [label for label, _ in paired_change.unpaired(units, MECHANISM, UNDERSTANDING)]
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
    return [label for label, _ in paired_change.unpaired(units, MECHANISM, UNDERSTANDING)]


def run_git_cases():
    failures = 0

    def report(ok, name, detail=""):
        nonlocal failures
        print(f"{'ok   ' if ok else 'FAIL '} {name}{'' if ok else ': ' + detail}")
        failures += not ok

    with tempfile.TemporaryDirectory() as repo:
        git(repo, "init", "-q")
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
        git(repo, "init", "-q")
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
        git(repo, "init", "-q")
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


def main():
    failures = run_rule_cases() + run_report_case() + run_git_cases()
    print("\n" + "=" * 40)
    if failures:
        print(f"paired change: {failures} failure(s)")
        return 1
    print("paired change: all cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
