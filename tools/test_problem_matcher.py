#!/usr/bin/env python3
"""Fixture test for the problem matchers of the editor's gate task.

VS Code's task "docs: run the gate" (.vscode/tasks.json) runs `docsys check` and
reads its output through problem matchers, so that a failure lands in the Problems
pane on the file and line it names, with its rule and severity. The output has four
shapes, each read by one matcher:

- an error finding, `path:line: rule: message — fix: …` (docsys/src/docsys/findings.py);
- a warning finding, the same line indented by two spaces, under `warnings (N)`;
- a line of the markdownlint tool, printed under `=== markdownlint ===`:
  `path:line[:column] rule/alias message`;
- a refused configuration, `docsys: docsys.yaml: message — fix: …`, which names
  the file and no line.

This test reads every matcher from tasks.json and runs it over lines of each shape,
copied from real runs: each failure line must yield its file, line, column, rule and
message through exactly one matcher, and no other line may yield a problem, a green
summary least of all. A matcher is known by its source, severity and kind. A path
holds no whitespace, so a line that echoes a failure after a word, as this test's
own output does (`ok    a.md:1: …`), is not read as one.

The patterns are JavaScript regular expressions; they use only what Python's `re`
reads the same way. tasks.json is read as strict JSON, so it carries no comments.

    python3 tools/test_problem_matcher.py
"""

import json
import re
import sys
from pathlib import Path
from typing import Final, NamedTuple, TypeGuard

TASKS: Final = Path(__file__).resolve().parent.parent / ".vscode" / "tasks.json"
TASK: Final = "docs: run the gate"


class Key(NamedTuple):
    """What tells the matchers apart: who reports the problem, how serious it is,
    and whether it names a line ("location") or a file only ("file")."""

    source: str
    severity: str
    kind: str


class Problem(NamedTuple):
    key: Key
    file: str | None
    line: str | None
    column: str | None
    code: str | None
    message: str


class Matcher(NamedTuple):
    key: Key
    regexp: re.Pattern[str]
    groups: dict[str, int]


FINDING: Final = Key("docsys", "error", "location")
WARNING: Final = Key("docsys", "warning", "location")
MARKDOWNLINT: Final = Key("markdownlint", "error", "location")
REFUSAL: Final = Key("docsys", "error", "file")


class Case(NamedTuple):
    output: str
    key: Key
    file: str
    line: str | None
    column: str | None
    code: str | None
    message: str  # how the message starts


FAILURES: Final = [
    Case(
        "README.md:1: frontmatter/required: missing required field `intention` — fix: add `intention:`",
        FINDING,
        "README.md",
        "1",
        None,
        "frontmatter/required",
        "missing required field",
    ),
    Case(
        "a/b.md:4: frontmatter/root-only: the root document must carry `axis` — fix: add `axis:`",
        FINDING,
        "a/b.md",
        "4",
        None,
        "frontmatter/root-only",
        "the root document",
    ),
    # A finding on docsys.yaml itself: a tool that failed, an allowance that outlived its reason.
    Case(
        "docsys.yaml:1: tools/failed: the tool `markdownlint` exited with status 1 — fix: read what it printed",
        FINDING,
        "docsys.yaml",
        "1",
        None,
        "tools/failed",
        "the tool",
    ),
    Case(
        "  a/b.md:8: links/resolve: `missing.md` points to no file or folder — fix: point the link at a path",
        WARNING,
        "a/b.md",
        "8",
        None,
        "links/resolve",
        "`missing.md`",
    ),
    Case(
        "  steering/x.md:4: frontmatter/open: status `dratf` outside the current practice (still open) — fix: …",
        WARNING,
        "steering/x.md",
        "4",
        None,
        "frontmatter/open",
        "status",
    ),
    Case(
        'README.md:6:1 MD018/no-missing-space-atx No space after hash on atx style heading [Context: "#bad heading"]',
        MARKDOWNLINT,
        "README.md",
        "6",
        "1",
        "MD018/no-missing-space-atx",
        "No space after hash",
    ),
    Case(
        "a/b.md:7 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading",
        MARKDOWNLINT,
        "a/b.md",
        "7",
        None,
        "MD041/first-line-heading/first-line-h1",
        "First line",
    ),
    # The custom rule the engine ships.
    Case(
        "a/b.md:7:5 sentence-per-line/MD100 One sentence per line (semantic line breaks, ADR-021) [Two sentences …]",
        MARKDOWNLINT,
        "a/b.md",
        "7",
        "5",
        "sentence-per-line/MD100",
        "One sentence per line",
    ),
    Case(
        "docsys: docsys.yaml: `scope.exclude` gives `a/` no reason — fix: write it as `<pattern>: <reason>`",
        REFUSAL,
        "docsys.yaml",
        None,
        None,
        None,
        "`scope.exclude`",
    ),
]

# Lines a run prints that are not a problem on a file.
NOT_FAILURES: Final = [
    # The devShell's banner, printed when the hook or the task enters the shell.
    "warning: Git tree '/home/u/documentation-system' is dirty",
    "documentation-system devShell:",
    "  markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)",
    "  v22.20.0  |  Python 3.12.12  |  uv 0.7.22",
    "docsys 0.1.0.dev0: workspace /home/u/documentation-system",
    "warnings (3), reported without failing the run:",
    "docsys check failed: 17 errors, 3 warnings",
    "docsys check passed: 0 errors, 0 warnings",
    # A run that cannot find its workspace names no file of it.
    "docsys: no docsys.yaml in /home/u or any directory above it — fix: run `docsys init` at the root",
    # The second line of a YAML error in a refused configuration.
    '  in "/home/u/documentation-system/docsys.yaml", line 2, column 1) — fix: correct the line it names.',
    "=== markdownlint ===",
    "markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)",
    "Finding: **/*.md !theorising/**",
    "Linting: 127 file(s)",
    "Summary: 0 error(s)",
    # This repository's own checks, run as tools.
    "=== editor-markdownlint ===",
    "EDITOR MARKDOWNLINT: 1 disagreement(s)",
    "  the extension davidanson.vscode-markdownlint v0.62.1 bundles markdownlint-cli2 0.23.2 — fix: …",
    "Editor markdownlint OK (davidanson.vscode-markdownlint v0.59.0 bundles markdownlint-cli2 0.17.2)",
    "ok    a stem equal to the slug passes",
    "FAIL  a stem that is not the slug: expected ['filename stem'] on a/other.md",
    "problem matcher: all 33 cases pass",
    # This test's own output, which echoes the failure lines it reads.
    "ok    README.md:1: frontmatter/required: missing required field `intention` — fix: add `in",
    "FAIL  a/b.md:7:5 sentence-per-line/MD100 One sentence per line (semantic line breaks, AD: expected",
]


def is_mapping(value: object) -> TypeGuard[dict[str, object]]:
    return isinstance(value, dict)


def is_list(value: object) -> TypeGuard[list[object]]:
    return isinstance(value, list)


def text(mapping: dict[str, object], key: str, default: str) -> str:
    value = mapping.get(key, default)
    if not isinstance(value, str):
        raise ValueError(f"`{key}` is {value!r}, not a string")
    return value


def load(path: Path) -> object:
    """tasks.json as untyped data, narrowed by the caller."""
    data: object = json.loads(path.read_text(encoding="utf-8"))  # pyright: ignore[reportAny] -- json is untyped; this is the boundary
    return data


def matchers() -> list[Matcher]:
    """The gate task's problem matchers, each known by its Key."""
    raw = load(TASKS)
    if not is_mapping(raw) or not is_list(tasks := raw.get("tasks")):
        raise ValueError(f"{TASKS} has no list of tasks")
    task = next((t for t in tasks if is_mapping(t) and t.get("label") == TASK), None)
    if task is None or not is_list(found := task.get("problemMatcher")):
        raise ValueError(f"{TASKS} has no task {TASK!r} with a list of problem matchers")
    out: list[Matcher] = []
    for m in found:
        if not is_mapping(m) or not is_mapping(pattern := m.get("pattern")):
            raise ValueError(f"a problem matcher of {TASK!r} has no pattern: {m!r}")
        key = Key(text(m, "source", ""), text(m, "severity", "error"), text(pattern, "kind", "location"))
        groups = {
            field: group
            for field in ("file", "line", "column", "code", "message")
            if isinstance(group := pattern.get(field), int)
        }
        out.append(Matcher(key, re.compile(text(pattern, "regexp", "")), groups))
    return out


def problems(output: str, found: list[Matcher]) -> list[Problem]:
    """One Problem for each matcher that reads `output`."""
    out: list[Problem] = []
    for matcher in found:
        m = matcher.regexp.match(output)
        if m is None:
            continue

        def read(field: str, m: re.Match[str] = m, groups: dict[str, int] = matcher.groups) -> str | None:
            return m.group(groups[field]) if field in groups else None

        message = read("message")
        if message:
            out.append(Problem(matcher.key, read("file"), read("line"), read("column"), read("code"), message))
    return out


def verdict(case: Case, got: list[Problem]) -> str | None:
    """None when `got` is exactly the problem `case` expects; else why not."""
    if len(got) != 1:
        return f"expected one problem, got {got}"
    p = got[0]
    expected = (case.key, case.file, case.line, case.column, case.code)
    if (p.key, p.file, p.line, p.column, p.code) != expected or not p.message.startswith(case.message):
        return f"expected {(*expected, case.message + '…')}, got {p}"
    return None


def main() -> int:
    found = matchers()
    failures = 0
    total = 0

    keys = [m.key for m in found]
    total += 1
    if len(set(keys)) != len(keys):
        print(f"FAIL  each matcher has its own source, severity and kind: {keys}")
        failures += 1
    else:
        print(f"ok    each matcher has its own source, severity and kind ({len(keys)})")

    for case in FAILURES:
        total += 1
        why = verdict(case, problems(case.output, found))
        print(f"ok    {case.output[:70]}" if why is None else f"FAIL  {case.output[:70]}: {why}")
        failures += why is not None

    for output in NOT_FAILURES:
        total += 1
        got = problems(output, found)
        print(f"ok    not a problem: {output[:57]}" if not got else f"FAIL  read as a problem: {output!r}: {got}")
        failures += bool(got)

    print("\n" + "=" * 40)
    if failures:
        print(f"problem matcher: {failures}/{total} case(s) failed")
        return 1
    print(f"problem matcher: all {total} cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
