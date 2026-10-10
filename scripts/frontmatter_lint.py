#!/usr/bin/env python3
"""Frontmatter linter.

Validates every tracked Markdown document's YAML frontmatter against
the generated schema (schema/frontmatter-rules.json). Settled rules are ERRORS (exit 1); what is still
genuinely undecided is a WARNING. Parses real YAML through
scripts/yaml_frontmatter.py, so it needs `pyyaml` — the devShell provides it.

Phase 10 promoted the Phase-09 starter's three contested rules to errors:
`intention` is the coarse set, `register` is derived and must NOT be stored, and
`constitutive` is required. See phases/refoundation/phase-10-schema/.

Phase 11 T1 closed the vocabulary: any field outside `required` ∪
`optional_fields` ∪ `root_only_fields` is an error. See
phases/refoundation/phase-11-tooling-hardening/.

Phase 11 T2 replaced the hand-rolled comma-and-colon parser with that YAML reader;
its fixtures are scripts/test_frontmatter_lint.py.

Phase 11 T3 moved the schema's source of truth to schema/frontmatter-rules.yaml —
hand-edited, comments allowed. This file loads the JSON generated from it
(scripts/generate_schema.py), so reading the schema never itself requires a YAML
parser. `scripts/check.py` fails the gate if the two have drifted apart.

    python3 scripts/frontmatter_lint.py            # errors only gate
    python3 scripts/frontmatter_lint.py --warnings # also print warnings
    python3 scripts/frontmatter_lint.py --registers # print the DERIVED register
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docsys_config import load_config  # noqa: E402
from yaml_frontmatter import FrontmatterError, load  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

# Every error ends `— fix: <the edit that clears it>`: the gate's reader is often a
# machine with no other context (Phase 12 T1(c)). Located beside this file, not named
# by a literal path — which scripts a repo runs is instance configuration.
GENERATOR = os.path.relpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "generate_schema.py"), ROOT)

def ignored(path, scope):
    """Is `path` outside the authored catalogue? `scope` is docsys.yaml's
    `frontmatter:` section: prefixes match at the start of a path, substrings
    anywhere in it."""
    return path.startswith(tuple(scope["ignore_prefixes"])) or any(
        s in path for s in scope["ignore_substrings"])


def load_schema():
    with open(load_config()["schema"]["generated"], encoding="utf-8") as fh:
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
            f"unknown {sorted(set(covered) - set(forces))} — fix: list every force "
            "under exactly one of know / do in the schema source's `direction_of_fit`"
        )
    # Fail loud if an optional field has no rationale: "declared" and "justified"
    # must be the same act (Phase 11 T1), or the vocabulary is closed in name only.
    for field, rationale in schema["optional_fields"].items():
        if not isinstance(rationale, str) or not rationale.strip():
            raise SystemExit(f"schema error: optional field `{field}` has no rationale string — "
                             f"fix: give it a one-line reason in {load_config()['schema']['source']}, or remove it")
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


def lint_file(path, schema, errors, warnings):
    try:
        fm = load(path)
    except FrontmatterError as exc:
        errors.append((path, exc.line, f"invalid YAML frontmatter — {exc.message} — fix: correct the YAML at this line"))
        return
    if fm is None:
        errors.append((path, 1, "no YAML frontmatter block — fix: open the file with a `---`-fenced block carrying the required fields"))
        return

    def val(key):
        return fm[key][0] if key in fm else None

    def ln(key):
        return fm[key][1] if key in fm else 1

    # Required fields present.
    for field in schema["required"]:
        if field not in fm or fm[field][0] in (None, "", []):
            errors.append((path, 1, f"missing required field `{field}` — fix: add `{field}:` to the frontmatter"))

    # provenance shape.
    prov = val("provenance")
    if prov is not None:
        if not isinstance(prov, dict) or "type" not in prov or "id" not in prov:
            errors.append((path, ln("provenance"), "provenance must be `{type, id}` — fix: write `provenance: { type: function, id: <name> }`"))
        elif prov["type"] not in schema["error_enums"]["provenance_type"]:
            errors.append((path, ln("provenance"), f"provenance.type `{prov['type']}` not in {schema['error_enums']['provenance_type']} — fix: use one of them"))

    # Simple error enums.
    for field in ("view", "reader", "intention", "constitutive"):
        v = val(field)
        if v is not None and v not in schema["error_enums"][field]:
            errors.append((path, ln(field), f"{field} `{v}` not in {schema['error_enums'][field]} — fix: use one of them"))

    # `register` is DERIVED, never stored (Phase 10: register-derived-constitutive).
    if "register" in fm:
        errors.append((path, ln("register"),
                       "`register` is derived (`constitutive ? govern : direction-of-fit(force)`), "
                       "never stored — fix: remove the field"))

    # `hash`, when present, is a well-formed fixity seal.
    h = val("hash")
    if h is not None and not re.match(schema["hash_pattern"], str(h)):
        errors.append((path, ln("hash"), f"hash `{h}` does not match {schema['hash_pattern']} — fix: re-seal with `python3 scripts/hash_seal.py --reseal {path}`, or remove `hash` if the record is not frozen"))

    # force (allow composite a+b).
    force = val("force")
    if force is not None:
        for comp in str(force).split("+"):
            if comp.strip() not in schema["error_enums"]["force"]:
                errors.append((path, ln("force"), f"force component `{comp.strip()}` not a known force — fix: use one of {schema['error_enums']['force']}"))

    # audience: non-empty list; unknown roles are warnings (refinable per project).
    aud = val("audience")
    if aud is not None:
        if not isinstance(aud, list) or not aud:
            errors.append((path, ln("audience"), "audience must be a non-empty list — fix: write it as `audience: [contributor]`"))
        else:
            for role in aud:
                if role not in schema["audience_base_roles"]:
                    warnings.append((path, ln("audience"), f"audience role `{role}` is a project refinement (base: {schema['audience_base_roles']})"))

    # Root-only fields.
    is_root = path == "README.md"
    for field in schema["root_only_fields"]:
        if field in fm and not is_root:
            errors.append((path, ln(field), f"`{field}` may only appear on the root README — fix: remove it from this file"))
    if is_root:
        for field in schema["root_only_fields"]:
            if field not in fm:
                errors.append((path, 1, f"root README must carry `{field}` — fix: add `{field}:` to its frontmatter"))

    # Undecided fields → warnings (see the schema's `still_open`).
    for field, allowed in schema["warn_enums"].items():
        v = val(field)
        if v is not None and v not in allowed:
            warnings.append((path, ln(field), f"{field} `{v}` outside the current practice {allowed} (still open)"))

    # Closed vocabulary (Phase 11 T1): a field is legal only if it is required,
    # declared (with a rationale) in optional_fields, or a root-only field.
    # `register` already has its own dedicated error above.
    known = set(schema["required"]) | set(schema["optional_fields"]) | set(schema["root_only_fields"])
    for field in fm:
        if field not in known and field != "register":
            errors.append((path, ln(field), f"`{field}` is not in the closed frontmatter vocabulary — fix: remove it, or declare it in {load_config()['schema']['source']} with a rationale and run `python3 {GENERATOR}`"))


def print_registers(schema, files):
    for path in files:
        try:
            fm = load(path) or {}
        except FrontmatterError:
            fm = {}
        force = fm["force"][0] if "force" in fm else None
        const = fm["constitutive"][0] if "constitutive" in fm else None
        print(f"{derive_register(schema, force, const):7} {path}")


def main():
    show_warnings = "--warnings" in sys.argv
    schema = load_schema()
    scope = load_config()["frontmatter"]
    files = [
        f for f in subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
        if not ignored(f, scope)
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
