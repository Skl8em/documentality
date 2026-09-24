"""Instance configuration — the one reader of docsys.yaml (Phase 12 T1(b)).

scripts/ is the engine: it knows how to lint frontmatter, verify a register, run a
sequence of checks. docsys.yaml is what the engine is *pointed at* in this repo —
where the schema lives, which documents are out of scope, what the decision
register looks like, which checks make up the gate and in what order. Every script
that needs an instance value reads it here, so nothing repo-specific is a literal
in the engine (scripts/test_seam.py enforces that).

The vocabulary is closed, like the frontmatter's: an unknown key is an error, not a
silently ignored typo. Scalars stay strings (scripts/yaml_frontmatter.py's
StrictLoader), so the integer keys are converted here — and refused, loudly, when
they are not integers. Every refusal names the file, the key and the fix: the gate
is often read by a machine with no other context.

    from docsys_config import load_config
    cfg = load_config()
    cfg["register"]["path"]
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yaml_frontmatter import StrictLoader, yaml  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

CONFIG_PATH = "docsys.yaml"

# What `builtin:` may name — checks implemented inside scripts/check.py itself.
BUILTINS = ("worktree",)

SECTIONS = {
    "schema": ("source", "generated"),
    "frontmatter": ("ignore_prefixes", "ignore_substrings"),
    "register": ("path", "columns", "ordinal_column", "status_column",
                 "ordinal_pattern", "superseded_pattern"),
    "paired_change": ("since", "mechanism", "understanding"),
}
CHECK_KINDS = ("python", "builtin", "tool")
CHECK_KEYS = ("name", "args") + CHECK_KINDS
# register.<key> -> number of capture groups its pattern must carry.
PATTERN_GROUPS = {"ordinal_pattern": 2, "superseded_pattern": 1}


class ConfigError(ValueError):
    """The configuration is unusable. The message starts with the file's name."""

    def __init__(self, message):
        super().__init__(f"{CONFIG_PATH}: {message}")


def _string_list(value, key):
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
        raise ConfigError(f"`{key}` must be a list of strings — write it as `{key.split('.')[-1]}: [a, b]`.")


def _integer(value, key):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ConfigError(f"`{key}` must be an integer, got {value!r} — write a bare number, "
                          f"e.g. `{key.split('.')[-1]}: 4`.") from None


def _validate_register(reg):
    for key in ("columns", "ordinal_column", "status_column"):
        reg[key] = _integer(reg[key], f"register.{key}")
    for key in ("ordinal_column", "status_column"):
        if not 0 <= reg[key] < reg["columns"]:
            raise ConfigError(
                f"`register.{key}` ({reg[key]}) is outside the row: `register.columns` is "
                f"{reg['columns']}, so columns are numbered 0–{reg['columns'] - 1}.")
    for key, groups in PATTERN_GROUPS.items():
        try:
            compiled = re.compile(reg[key])
        except re.error as exc:
            raise ConfigError(f"`register.{key}` is not a valid regular expression ({exc}) — fix the pattern.") from None
        if compiled.groups != groups:
            raise ConfigError(f"`register.{key}` must have exactly {groups} capture group(s) "
                              f"(found {compiled.groups}) — wrap the part to extract in ( ).")


def _validate_paired_change(pc):
    if not isinstance(pc["since"], str) or not re.fullmatch(r"[0-9a-f]{7,40}", pc["since"]):
        raise ConfigError(f"`paired_change.since` must be a commit id (7–40 lowercase hex digits), "
                          f"got {pc['since']!r} — write the id of the commit after which the rule applies.")
    for key in ("mechanism", "understanding"):
        _string_list(pc[key], f"paired_change.{key}")
        if not pc[key]:
            raise ConfigError(f"`paired_change.{key}` must list at least one path prefix — "
                              f"the rule would {'never fire' if key == 'mechanism' else 'never pass'}.")


def _validate_check(index, check, seen):
    where = f"checks[{index}]"
    if not isinstance(check, dict):
        raise ConfigError(f"`{where}` must be a mapping with a `name` and one of python/builtin/tool.")
    unknown = sorted(set(check) - set(CHECK_KEYS))
    if unknown:
        raise ConfigError(f"`{where}` has unknown key(s) {unknown} — allowed: {list(CHECK_KEYS)}.")
    name = check.get("name")
    if not isinstance(name, str) or not name:
        raise ConfigError(f"`{where}` has no `name` — give every check a short, unique name.")
    if name in seen:
        raise ConfigError(f"`{where}` name `{name}` is a duplicate — each check name must be unique.")
    seen.add(name)
    kinds = [k for k in CHECK_KINDS if k in check]
    if len(kinds) != 1:
        raise ConfigError(f"`{where}` (`{name}`) must have exactly one of {list(CHECK_KINDS)}, found {kinds or 'none'}.")
    kind = kinds[0]
    if kind == "builtin" and check["builtin"] not in BUILTINS:
        raise ConfigError(f"`{where}` builtin `{check['builtin']}` is unknown — known builtins: {list(BUILTINS)}.")
    if kind == "python" and not os.path.exists(check["python"]):
        raise ConfigError(f"`{where}` python script `{check['python']}` does not exist — "
                          "fix the path (relative to the repo root).")
    if "args" in check:
        _string_list(check["args"], f"{where}.args")


def validate(cfg):
    """Check a loaded configuration and return it with integer keys converted.
    Raises ConfigError, naming the key and the fix."""
    if not isinstance(cfg, dict):
        raise ConfigError("must be a mapping of sections — see the comment at the top of the file.")
    unknown = sorted(set(cfg) - set(SECTIONS) - {"checks"})
    if unknown:
        raise ConfigError(f"unknown section(s) {unknown} — the vocabulary is closed: "
                          f"{[*SECTIONS, 'checks']}.")
    for section, keys in SECTIONS.items():
        if not isinstance(cfg.get(section), dict):
            raise ConfigError(f"section `{section}` is missing — add it with keys {list(keys)}.")
        for key in keys:
            if key not in cfg[section]:
                raise ConfigError(f"`{section}.{key}` is missing — add it to the `{section}` section.")
        extra = sorted(set(cfg[section]) - set(keys))
        if extra:
            raise ConfigError(f"`{section}` has unknown key(s) {extra} — allowed: {list(keys)}.")
    for key in ("ignore_prefixes", "ignore_substrings"):
        _string_list(cfg["frontmatter"][key], f"frontmatter.{key}")
    _validate_register(cfg["register"])
    _validate_paired_change(cfg["paired_change"])

    checks = cfg.get("checks")
    if not isinstance(checks, list) or not checks:
        raise ConfigError("`checks` must list at least one check — the gate would run nothing.")
    seen = set()
    for index, check in enumerate(checks):
        _validate_check(index, check, seen)
    return cfg


def load_config(path=CONFIG_PATH):
    if not os.path.exists(path):
        raise ConfigError(f"`{path}` does not exist — it is the engine's only instance input; "
                          "restore it from git.")
    with open(path, encoding="utf-8") as fh:
        try:
            cfg = yaml.load(fh, Loader=StrictLoader)
        except yaml.YAMLError as exc:
            raise ConfigError(f"is not valid YAML ({exc}).") from None
    return validate(cfg)
