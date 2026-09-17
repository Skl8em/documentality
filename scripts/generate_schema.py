#!/usr/bin/env python3
"""Compile the frontmatter schema from its YAML source (Phase 11 T3).

schema/frontmatter-rules.yaml is hand-edited: the vocabulary, its enums, and each
optional field's rationale, with room for `#` comments a JSON file cannot carry.
schema/frontmatter-rules.json is generated from it — the dependency-free artifact
scripts/frontmatter_lint.py (and any other reader, in Python or otherwise) actually
loads, so consuming the schema never requires a YAML parser.

The two must never drift apart silently: `--check` regenerates the JSON in memory
and diffs it against the committed file, failing the gate if they differ. This
replaces schema/frontmatter.schema.json, whose name claimed a JSON Schema dialect
the hand-written validator never implemented.

    python3 scripts/generate_schema.py          # write schema/frontmatter-rules.json
    python3 scripts/generate_schema.py --check  # fail if the committed JSON is stale
"""
import difflib
import json
import os
import subprocess
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yaml_frontmatter import StrictLoader  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

SOURCE = "schema/frontmatter-rules.yaml"
GENERATED = "schema/frontmatter-rules.json"


def compile_source():
    # StrictLoader (scripts/yaml_frontmatter.py): this file's vocabulary is
    # strings throughout — plain `yes`/`no` under a bare SafeLoader compile to
    # booleans (YAML 1.1), which silently broke `error_enums.constitutive`.
    with open(SOURCE, encoding="utf-8") as fh:
        data = yaml.load(fh, Loader=StrictLoader)
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def check():
    fresh = compile_source()
    with open(GENERATED, encoding="utf-8") as fh:
        committed = fh.read()
    if fresh == committed:
        print(f"{GENERATED} is up to date with {SOURCE}.")
        return 0
    diff = difflib.unified_diff(
        committed.splitlines(keepends=True), fresh.splitlines(keepends=True),
        fromfile=GENERATED, tofile=f"{SOURCE} (regenerated)")
    print(f"SCHEMA DRIFT: {GENERATED} does not match {SOURCE}.")
    print("Run `python3 scripts/generate_schema.py` and commit the result.\n")
    sys.stdout.writelines(diff)
    return 1


def write():
    fresh = compile_source()
    if os.path.exists(GENERATED):
        with open(GENERATED, encoding="utf-8") as fh:
            if fh.read() == fresh:
                print(f"{GENERATED} already up to date.")
                return 0
    with open(GENERATED, "w", encoding="utf-8") as fh:
        fh.write(fresh)
    print(f"wrote {GENERATED}")
    return 0


def main():
    if "--check" in sys.argv:
        return check()
    return write()


if __name__ == "__main__":
    sys.exit(main())
