#!/usr/bin/env python3
"""Fixity verifier — every `hash:` in the corpus still matches its content.

A broken seal is not automatically a fault: it means a *frozen* record changed.
Either the change is wrong (revert it — the seal did its job), or it is a
deliberate re-freeze, in which case `scripts/hash_seal.py --reseal <path>` records
that consciously. Canonicalisation is defined in `hash_seal.py`.

Also reports frozen records that carry no seal (informational, not a failure —
sealing is optional per the schema).

Stdlib only.

    python3 scripts/hash_check.py
    python3 scripts/hash_check.py --unsealed  # also list the unsealed frozen records
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hash_seal import field, is_frozen, seal_of, split_document  # noqa: E402

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)


def main():
    files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()
    broken, sealed, unsealed = [], 0, []
    for f in files:
        try:
            fm_lines, _ = split_document(f)
        except (ValueError, UnicodeDecodeError):
            continue
        declared = field(fm_lines, "hash")
        if declared is None:
            if is_frozen(f):
                unsealed.append(f)
            continue
        sealed += 1
        actual = seal_of(f)
        if declared != actual:
            broken.append((f, declared, actual))

    if "--unsealed" in sys.argv and unsealed:
        print(f"UNSEALED frozen records: {len(unsealed)}")
        for f in unsealed:
            print(f"  {f}")
        print()

    if broken:
        print(f"FIXITY ERRORS: {len(broken)} seal(s) broken")
        for f, declared, actual in broken:
            print(f"  {f}\n    declared {declared}\n    actual   {actual}")
        print("\nA frozen record changed. Revert it, or re-freeze deliberately:"
              "\n  python3 scripts/hash_seal.py --reseal <path>")
        return 1
    print(f"Fixity OK ({sealed} sealed record(s) verified; {len(unsealed)} frozen but unsealed).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
