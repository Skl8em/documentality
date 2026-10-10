#!/usr/bin/env python3
"""Fixture test for the engine/config seam (Phase 12 T1(b)).

The scripts under scripts/ are the engine; docsys.yaml is this repo's instance
configuration. This test holds the line between them:

  1. the real docsys.yaml loads and validates;
  2. a malformed config is refused, with a message that names the file, the key
     and the fix (the gate's machine reader has no other context);
  3. no instance value from docsys.yaml — a path, a prefix, a script name — appears
     as a string literal in the engine's code. Docstrings are prose and are exempt;
     only literals the interpreter can act on count. The values to look for are read
     FROM the config, so adding an instance value to it extends this check for free.

    python3 scripts/test_seam.py
"""
import ast
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docsys_config  # noqa: E402

VALID = {
    "schema": {"source": "s/rules.yaml", "generated": "s/rules.json"},
    "frontmatter": {"ignore_prefixes": ["raw/"], "ignore_substrings": ["/tmp/"]},
    "register": {
        "path": "log.md", "columns": "5", "ordinal_column": "0", "status_column": "4",
        "ordinal_pattern": r"^\[(\d+)\]\(([^)]+)\)$", "superseded_pattern": r"superseded by (\d+)",
    },
    "paired_change": {
        "since": "0123456789abcdef0123456789abcdef01234567",
        "mechanism": ["engine/"],
        "understanding": ["docs/", "ARCHITECTURE.md"],
        "exempt": ["engine/test_"],
        "enforce_on": ["trunk"],
    },
    "phases": {
        "ledger": "state/phases.yaml",
        "root": "records",
        "folder": "phase-{number:02d}-{name}",
        "field": "{number:02d}-{name}",
        "markers": {"done": "done", "current": "in progress", "planned": "unnumbered"},
        "tables": [{"path": "plan/roadmap.md", "row": r"^\| (?P<number>\d+)? ?\*\((?P<marker>[^)]*)\)\*"}],
        "status": {"path": "INDEX.md", "line": r"^\*\*Phase (?P<number>\d+)\*\*"},
        "mention": r"\bPhase (?P<number>\d+)",
    },
    "checks": [
        {"name": "tree", "builtin": "worktree"},
        {"name": "links", "python": "scripts/linkcheck.py"},
        {"name": "drift", "python": "scripts/generate_schema.py", "args": ["--check"]},
        {"name": "lint", "tool": "markdownlint-cli2"},
    ],
}


def broken(mutate):
    """A deep copy of VALID after `mutate(copy)`."""
    import copy
    cfg = copy.deepcopy(VALID)
    mutate(cfg)
    return cfg


def drop(section, key=None):
    def go(cfg):
        if key is None:
            del cfg[section]
        else:
            del cfg[section][key]
    return go


def setter(section, key, value):
    def go(cfg):
        cfg[section][key] = value
    return go


def set_check(index, **fields):
    def go(cfg):
        cfg["checks"][index] = fields
    return go


# (name, mutation of VALID, fragments the refusal must contain — the key, and a fix)
REFUSAL_CASES = [
    ("a missing section", drop("register"), ["register", "missing"]),
    ("a missing key", drop("schema", "source"), ["schema.source", "missing"]),
    ("an unknown key", setter("schema", "typo", "x"), ["schema", "typo", "unknown"]),
    ("an unknown section", lambda c: c.update(extra={}), ["extra", "unknown section"]),
    ("a non-integer column", setter("register", "columns", "five"),
     ["register.columns", "integer"]),
    ("a pattern that does not compile", setter("register", "superseded_pattern", "(unclosed"),
     ["register.superseded_pattern", "regular expression"]),
    ("a pattern with the wrong number of groups", setter("register", "superseded_pattern", "superseded by"),
     ["register.superseded_pattern", "group"]),
    ("a status column outside the row", setter("register", "status_column", "9"),
     ["register.status_column", "columns"]),
    ("a since that is not a commit id", setter("paired_change", "since", "main"),
     ["paired_change.since", "commit"]),
    ("an empty mechanism list", setter("paired_change", "mechanism", []),
     ["paired_change.mechanism", "at least one"]),
    ("an understanding list of non-strings", setter("paired_change", "understanding", "docs/"),
     ["paired_change.understanding", "list of strings"]),
    ("an empty enforce_on list", setter("paired_change", "enforce_on", []),
     ["paired_change.enforce_on", "at least one"]),
    ("an exempt list of non-strings", setter("paired_change", "exempt", "engine/test_"),
     ["paired_change.exempt", "list of strings"]),
    ("a missing paired_change key", drop("paired_change", "enforce_on"),
     ["paired_change.enforce_on", "missing"]),
    ("a missing paired_change section",
     drop("paired_change"), ["paired_change", "missing"]),
    ("a missing phases section", drop("phases"), ["phases", "missing"]),
    ("a missing phases.ledger", drop("phases", "ledger"), ["phases.ledger", "missing"]),
    ("a phases.ledger that is not a path", setter("phases", "ledger", ["a.yaml"]),
     ["phases.ledger", "path"]),
    ("a folder format without the number", setter("phases", "folder", "phase-{name}"),
     ["phases.folder", "{number"]),
    ("a field format that does not format", setter("phases", "field", "{number:02d}-{name}-{era}"),
     ["phases.field", "format"]),
    ("markers missing a status", setter("phases", "markers", {"done": "done", "current": "now"}),
     ["phases.markers", "planned"]),
    ("two statuses with one marker",
     setter("phases", "markers", {"done": "done", "current": "done", "planned": "later"}),
     ["phases.markers", "distinct"]),
    ("no table", setter("phases", "tables", []), ["phases.tables", "at least one"]),
    ("a table row pattern without a marker group",
     setter("phases", "tables", [{"path": "r.md", "row": r"^\| (?P<number>\d+)"}]),
     ["phases.tables[0]", "marker"]),
    ("a table row pattern that does not compile",
     setter("phases", "tables", [{"path": "r.md", "row": "(?P<number>"}]),
     ["phases.tables[0]", "regular expression"]),
    ("a table entry with an unknown key",
     setter("phases", "tables", [{"path": "r.md", "row": "x", "header": "y"}]),
     ["phases.tables[0]", "header", "unknown"]),
    ("a status pattern without a number group",
     setter("phases", "status", {"path": "R.md", "line": r"^\*\*Phase \d+"}),
     ["phases.status", "number"]),
    ("a mention pattern without a number group", setter("phases", "mention", r"\bPhase \d+"),
     ["phases.mention", "number"]),
    ("an empty check list", lambda c: c.update(checks=[]), ["checks", "at least one"]),
    ("a check of no known kind", set_check(1, name="links"),
     ["checks[1]", "exactly one of"]),
    ("a check of two kinds", set_check(1, name="links", python="a.py", tool="b"),
     ["checks[1]", "exactly one of"]),
    ("an unknown builtin", set_check(0, name="tree", builtin="nonsense"),
     ["checks[0]", "builtin", "nonsense"]),
    ("a check without a name", set_check(1, python="scripts/linkcheck.py"),
     ["checks[1]", "name"]),
    ("a duplicate check name", set_check(1, name="tree", python="scripts/linkcheck.py"),
     ["checks[1]", "tree", "duplicate"]),
    ("a check script that does not exist", set_check(1, name="links", python="scripts/nope.py"),
     ["checks[1]", "scripts/nope.py", "does not exist"]),
]


def run_refusal_cases():
    failures = 0
    for name, mutate, fragments in REFUSAL_CASES:
        try:
            docsys_config.validate(broken(mutate))
        except docsys_config.ConfigError as exc:
            message = str(exc)
            missing = [f for f in fragments if f not in message]
            if not missing and message.startswith("docsys.yaml"):
                print(f"ok    {name}")
                continue
            failures += 1
            print(f"FAIL  {name}: message {message!r} lacks {missing or ['the docsys.yaml prefix']}")
        else:
            failures += 1
            print(f"FAIL  {name}: the config was accepted")
    return failures


def run_valid_case():
    try:
        cfg = docsys_config.validate(broken(lambda c: None))
    except docsys_config.ConfigError as exc:
        print(f"FAIL  a valid config is accepted: {exc}")
        return 1
    ok = cfg["register"]["columns"] == 5 and cfg["register"]["status_column"] == 4
    if not ok:
        print("FAIL  a valid config is accepted: integer keys were not converted")
        return 1
    print("ok    a valid config is accepted, integer keys converted")
    return 0


def run_real_config_case():
    try:
        docsys_config.load_config()
    except docsys_config.ConfigError as exc:
        print(f"FAIL  the repo's own docsys.yaml validates: {exc}")
        return 1
    print("ok    the repo's own docsys.yaml validates")
    return 0


def run_builtins_case():
    """docsys_config says which builtins a config may name; check.py implements them.
    The two lists must not drift, or a valid config would crash the runner."""
    import check  # the runner; importing it runs nothing
    if set(check.BUILTINS) != set(docsys_config.BUILTINS):
        print(f"FAIL  builtins: check.py implements {sorted(check.BUILTINS)}, "
              f"docsys_config allows {sorted(docsys_config.BUILTINS)}")
        return 1
    print("ok    check.py implements exactly the builtins the config may name")
    return 0


def code_literals(path):
    """Every string literal in a script's code, docstrings excluded."""
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=path)
    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = node.body
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                docstrings.add(id(body[0].value))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docstrings:
            yield node.value


def instance_values(cfg):
    """The strings in docsys.yaml that name this repo's layout or tools. Patterns are
    excluded: they describe a format, and are matched as literals too readily."""
    values = {cfg["schema"]["source"], cfg["schema"]["generated"], cfg["register"]["path"],
              cfg["phases"]["ledger"]}
    # The tables are instance paths. The status file is not checked: here it is the
    # root README.md, which is also the methodology's root document, named in
    # frontmatter_lint.py on purpose (engine-config-seam.md, "what remains").
    values.update(table["path"] for table in cfg["phases"]["tables"])
    values.update(cfg["frontmatter"]["ignore_prefixes"])
    values.update(cfg["frontmatter"]["ignore_substrings"])
    for check in cfg["checks"]:
        if "python" in check:
            values.add(check["python"])
    return values


def instance_prefixes(cfg):
    """Path prefixes that classify a file. Matched only at the START of a literal: a
    prefix like `scripts/` is also how the engine's own messages point at a sibling
    script (`fix: mint one with scripts/ulid.py`), which is prose, not classification.
    The configuration's own file name is not an instance value even when it is listed
    as mechanism: it is how the engine finds its instance, the same in every repo."""
    pc = cfg["paired_change"]
    # The phase root is checked as a directory prefix: its bare name is also the word
    # the ledger and this config use for their own `phases:` key.
    return ((set(pc["mechanism"]) | set(pc["understanding"]) | set(pc["exempt"]) | {cfg["phases"]["root"] + "/"})
            - {docsys_config.CONFIG_PATH})


def run_leak_case():
    """The engine must not carry the instance. A test's own literals (this file) are
    fixtures, not engine, and are skipped."""
    cfg = docsys_config.load_config()
    values = instance_values(cfg)
    prefixes = instance_prefixes(cfg)
    here = os.path.abspath(__file__)
    failures = 0
    for path in sorted(glob.glob(os.path.join(os.path.dirname(here), "*.py"))):
        if os.path.abspath(path) == here or os.path.basename(path).startswith("test_"):
            continue
        for literal in code_literals(path):
            leaked = sorted({v for v in values if v and v in literal}
                            | {v for v in prefixes if v and literal.startswith(v)})
            if leaked:
                failures += 1
                print(f"FAIL  {os.path.relpath(path)} hard-codes {leaked} in {literal!r} — "
                      "move it to docsys.yaml and read it through scripts/docsys_config.py")
    if not failures:
        print("ok    no instance value from docsys.yaml is a literal in the engine")
    return failures


def main():
    failures = run_valid_case() + run_refusal_cases() + run_real_config_case() + run_builtins_case() + run_leak_case()
    print("\n" + "=" * 40)
    if failures:
        print(f"engine/config seam: {failures} failure(s)")
        return 1
    print("engine/config seam: all cases pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
