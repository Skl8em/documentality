#!/usr/bin/env python3
"""Frontmatter linter.

Validates every tracked Markdown document's YAML frontmatter against
schema/frontmatter.schema.json. Settled rules are ERRORS (exit 1); what is still
genuinely undecided is a WARNING. Stdlib only, so it runs outside the devShell.

Phase 10 promoted the Phase-09 starter's three contested rules to errors:
`intention` is the coarse set, `register` is derived and must NOT be stored, and
`constitutive` is required. See phases/refoundation/phase-10-schema/.

    python3 scripts/frontmatter_lint.py            # errors only gate
    python3 scripts/frontmatter_lint.py --warnings # also print warnings
    python3 scripts/frontmatter_lint.py --registers # print the DERIVED register
"""
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

# Documents outside the authored, refounded catalogue:
#  - theorising/**            raw upstream essays;
#  - phases/naive-sketch/**   pre-refoundation frozen records (predate `intention`);
#  - blind-test transcripts   raw agent outputs, not catalogued documents.
IGNORE_PREFIXES = ("theorising/", "phases/naive-sketch/")
IGNORE_SUBSTRINGS = ("/blind-test/", "/weft-blindtest")


def ignored(path):
    return path.startswith(IGNORE_PREFIXES) or any(s in path for s in IGNORE_SUBSTRINGS)


def load_schema():
    with open("schema/frontmatter.schema.json", encoding="utf-8") as fh:
        schema = json.load(fh)
    # Fail loud if the schema itself is incoherent: the direction-of-fit table must
    # partition the twelve forces exactly, or `register` cannot be derived.
    fit = schema["direction_of_fit"]
    covered = fit["know"] + fit["do"]
    forces = schema["error_enums"]["force"]
    if sorted(covered) != sorted(forces):
        raise SystemExit(
            "schema error: direction_of_fit must partition `force` exactly — "
            f"missing {sorted(set(forces) - set(covered))}, "
            f"unknown {sorted(set(covered) - set(forces))}"
        )
    return schema


def derive_register(schema, force, constitutive):
    """register = constitutive ? govern : direction-of-fit(force). Never stored."""
    if constitutive == "yes":
        return "govern"
    head = str(force).split("+")[0].strip()
    for register, forces in schema["direction_of_fit"].items():
        if head in forces:
            return register
    return "?"


def frontmatter_block(path):
    """Return (list of (lineno, rawline)) for the YAML frontmatter, or None."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    out = []
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return out
        out.append((i + 1, lines[i]))
    return None  # unterminated


def parse_scalar(s):
    s = s.strip()
    if len(s) >= 2 and s[0] in "\"'" and s[-1] == s[0]:
        return s[1:-1]
    if s in ("", "null", "~"):
        return None
    return s


def parse_value(s):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [parse_scalar(x) for x in inner.split(",")] if inner else []
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        m = {}
        for part in inner.split(","):
            if ":" in part:
                k, v = part.split(":", 1)
                m[k.strip()] = parse_scalar(v)
        return m
    return parse_scalar(s)


def parse_frontmatter(block):
    """Return {key: (value, lineno)} for simple `key: value` lines."""
    fm = {}
    for lineno, raw in block:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        if raw[0] in " \t":  # nested continuation line — the corpus uses inline maps, so skip
            continue
        key, val = raw.split(":", 1)
        fm[key.strip()] = (parse_value(val), lineno)
    return fm


def lint_file(path, schema, errors, warnings):
    block = frontmatter_block(path)
    if block is None:
        errors.append((path, 1, "no valid YAML frontmatter block"))
        return
    fm = parse_frontmatter(block)

    def val(key):
        return fm[key][0] if key in fm else None

    def ln(key):
        return fm[key][1] if key in fm else 1

    # Required fields present.
    for field in schema["required"]:
        if field not in fm or fm[field][0] in (None, "", []):
            errors.append((path, 1, f"missing required field `{field}`"))

    # provenance shape.
    prov = val("provenance")
    if prov is not None:
        if not isinstance(prov, dict) or "type" not in prov or "id" not in prov:
            errors.append((path, ln("provenance"), "provenance must be `{type, id}`"))
        elif prov["type"] not in schema["error_enums"]["provenance_type"]:
            errors.append((path, ln("provenance"), f"provenance.type `{prov['type']}` not in {schema['error_enums']['provenance_type']}"))

    # Simple error enums.
    for field in ("view", "reader", "intention", "constitutive"):
        v = val(field)
        if v is not None and v not in schema["error_enums"][field]:
            errors.append((path, ln(field), f"{field} `{v}` not in {schema['error_enums'][field]}"))

    # `register` is DERIVED, never stored (Phase 10: register-derived-constitutive).
    if "register" in fm:
        errors.append((path, ln("register"),
                       "`register` is derived (`constitutive ? govern : direction-of-fit(force)`), "
                       "never stored — remove the field"))

    # `hash`, when present, is a well-formed fixity seal.
    h = val("hash")
    if h is not None and not re.match(schema["hash_pattern"], str(h)):
        errors.append((path, ln("hash"), f"hash `{h}` does not match {schema['hash_pattern']}"))

    # force (allow composite a+b).
    force = val("force")
    if force is not None:
        for comp in str(force).split("+"):
            if comp.strip() not in schema["error_enums"]["force"]:
                errors.append((path, ln("force"), f"force component `{comp.strip()}` not a known force"))

    # audience: non-empty list; unknown roles are warnings (refinable per project).
    aud = val("audience")
    if aud is not None:
        if not isinstance(aud, list) or not aud:
            errors.append((path, ln("audience"), "audience must be a non-empty list"))
        else:
            for role in aud:
                if role not in schema["audience_base_roles"]:
                    warnings.append((path, ln("audience"), f"audience role `{role}` is a project refinement (base: {schema['audience_base_roles']})"))

    # Root-only fields.
    is_root = path == "README.md"
    for field in schema["root_only_fields"]:
        if field in fm and not is_root:
            errors.append((path, ln(field), f"`{field}` may only appear on the root README"))
    if is_root:
        for field in schema["root_only_fields"]:
            if field not in fm:
                errors.append((path, 1, f"root README must carry `{field}`"))

    # Undecided fields → warnings (see the schema's `still_open`).
    for field, allowed in schema["warn_enums"].items():
        v = val(field)
        if v is not None and v not in allowed:
            warnings.append((path, ln(field), f"{field} `{v}` outside the current practice {allowed} (still open)"))


def print_registers(schema, files):
    for path in files:
        block = frontmatter_block(path)
        fm = parse_frontmatter(block) if block else {}
        force = fm["force"][0] if "force" in fm else None
        const = fm["constitutive"][0] if "constitutive" in fm else None
        print(f"{derive_register(schema, force, const):7} {path}")


def main():
    show_warnings = "--warnings" in sys.argv
    schema = load_schema()
    files = [
        f for f in subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
        if not ignored(f)
    ]
    if "--registers" in sys.argv:
        print_registers(schema, files)
        return 0

    errors, warnings = [], []
    for f in files:
        lint_file(f, schema, errors, warnings)

    if show_warnings and warnings:
        print(f"WARNINGS: {len(warnings)} (fields still open — see the schema)")
        for f, line, msg in warnings:
            print(f"  {f}:{line}  {msg}")
        print()

    if errors:
        print(f"FRONTMATTER ERRORS: {len(errors)}")
        for f, line, msg in errors:
            print(f"  {f}:{line}  {msg}")
        return 1
    print(f"Frontmatter OK ({len(files)} files; {len(warnings)} warnings).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
