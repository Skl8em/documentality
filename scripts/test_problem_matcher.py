#!/usr/bin/env python3
"""Fixture test for the problem matcher of the editor's gate task.

VS Code's task "docs: run the gate" (.vscode/tasks.json) runs scripts/check.py and
reads its output through two problem matchers, so that a failure lands in the
Problems pane on the file, and line, it names: one for lines that carry a line
number, one, of kind "file", for those that name a file only (VS Code drops a
problem with neither a line nor that kind). This test reads both patterns from
tasks.json and runs them over lines in the shape of every check's output: each
failure line must yield its file, line and message, through one matcher only, and
no other line may yield a problem, a green summary least of all.

The patterns are JavaScript regular expressions; they use only what Python's `re`
reads the same way. tasks.json is read as strict JSON, so it carries no comments.

    python3 scripts/test_problem_matcher.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hash_check  # noqa: E402
import linkcheck  # noqa: E402

TASKS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".vscode", "tasks.json")
TASK = "docs: run the gate"

# (output line, kind of the matcher that must read it, file, line, column, message start)
FAILURES = [
    ("x.md:1:1 MD018/no-missing-space-atx No space after hash on atx style heading [Context: \"#bad\"]",
     "line", "x.md", "1", "1", "MD018/"),
    ("a/b.md:7 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading",
     "line", "a/b.md", "7", None, "MD041/"),
    ("  " + linkcheck.format_broken("a/b.md", 12, "../c.md"), "line", "a/b.md", "12", None, "->  ../c.md"),
    # frontmatter_lint.py prints "  {f}:{line}  {msg}"
    ("  a/b.md:3  `status: dratf` is not one of draft, stable — fix: …", "line", "a/b.md", "3", None, "`status"),
    # phase_state.py prints "PHASE STATE: {message}", the message led by "{path}:{line}:"
    ("PHASE STATE: steering/roadmap.md:41: a phase row with no status marker — fix: …",
     "line", "steering/roadmap.md", "41", None, "a phase row"),
    # slug_check.py and ulid_check.py print "  {f}  {msg}"
    ("  a/foo.md  filename stem 'other' != slug foo — fix: …", "file", "a/foo.md", None, None, "filename stem"),
    ("  README.md  `id` is not a valid ULID — fix: …", "file", "README.md", None, None, "`id`"),
    ("  " + hash_check.format_broken("a/r.md", "sha256:1", "sha256:2").splitlines()[0],
     "file", "a/r.md", None, None, "frozen record changed"),
    ("PHASE STATE: phases/rush-to-mvp/phase-15-x: a phase folder that is not in the ledger — fix: …",
     "file", "phases/rush-to-mvp/phase-15-x", None, None, "a phase folder"),
    ("PHASE LEDGER: steering/phases.yaml: does not exist — fix: …",
     "file", "steering/phases.yaml", None, None, "does not exist"),
]

# Lines the gate prints that are not a problem on a file.
NOT_FAILURES = [
    # The devShell's banner, printed when the gate re-enters the shell, as it does
    # from the editor's task.
    "Not in the devShell — re-running the gate inside it.",
    "warning: Git tree '/home/u/documentation-system' is dirty",
    "documentation-system devShell:",
    "  markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)",
    "  v22.20.0  |  Python 3.12.12  |  uv 0.7.22",
    "Run the full gate with: python3 scripts/check.py",
    "=== frontmatter ===",
    "Worktree OK (nothing untracked).",
    "  scratch.md",  # an untracked path, reported by the worktree check under its header
    "schema/frontmatter-rules.json is up to date with schema/frontmatter-rules.yaml.",
    "SCHEMA DRIFT: schema/frontmatter-rules.json does not match schema/frontmatter-rules.yaml.",
    "Frontmatter OK (127 files; 0 warnings).",
    "    declared sha256:1",
    "    fix: revert the change, or re-freeze deliberately",
    "  commit 72f24b6 everything through the devShell",
    "  fix: in the same commit, update what a reader would need to learn about the change",
    "PHASE LEDGER: `phases[3]` name 'x' is a duplicate — fix: give each phase its own name",
    "markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)",
    "Finding: **/*.md !theorising/**",
    "Linting: 127 file(s)",
    "Summary: 0 error(s)",
    "ok    a stem equal to the slug passes",
    "FAIL  a stem that is not the slug: expected ['filename stem'] on a/other.md",
    "  the extension davidanson.vscode-markdownlint v0.62.1 bundles markdownlint-cli2 0.23.2 — fix: …",
    "GATE FAILED: frontmatter, slug",
]


def matchers():
    """The gate task's problem matchers, keyed by kind ("line" when none is given)."""
    with open(TASKS, encoding="utf-8") as fh:
        tasks = json.load(fh)["tasks"]
    task = next(t for t in tasks if t["label"] == TASK)
    found = {}
    for m in task["problemMatcher"]:
        pattern = m["pattern"]
        found[pattern.get("kind", "line")] = (re.compile(pattern["regexp"]), pattern)
    return found


def read(pattern, match, field):
    group = pattern.get(field)
    return match.group(group) if group is not None else None


def problems(line, found):
    """[(kind, file, line, column, message)], one for each matcher that reads `line`."""
    out = []
    for kind, (regexp, pattern) in found.items():
        m = regexp.match(line)
        if m and read(pattern, m, "message"):
            out.append((kind, read(pattern, m, "file"), read(pattern, m, "line"), read(pattern, m, "column"),
                        read(pattern, m, "message")))
    return out


def main():
    found = matchers()
    failures = 0
    total = 0
    if set(found) != {"line", "file"}:
        print(f"FAIL  the gate task has a line matcher and a file matcher: found {sorted(found)}")
        return 1

    for line, kind, file, lineno, column, message in FAILURES:
        total += 1
        got = problems(line, found)
        if len(got) != 1:
            why = f"expected one problem, got {got}"
        elif got[0][:4] != (kind, file, lineno, column) or not got[0][4].startswith(message):
            why = f"expected {(kind, file, lineno, column, message + '…')}, got {got[0]}"
        else:
            why = None
        print(f"ok    {line[:70]}" if why is None else f"FAIL  {line[:70]}: {why}")
        failures += why is not None

    for line in NOT_FAILURES:
        total += 1
        got = problems(line, found)
        print(f"ok    not a problem: {line[:57]}" if not got else f"FAIL  read as a problem: {line!r}: {got}")
        failures += bool(got)

    print("\n" + "=" * 40)
    if failures:
        print(f"problem matcher: {failures}/{total} case(s) failed")
        return 1
    print(f"problem matcher: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
