#!/usr/bin/env python3
"""Paired-change check (Phase 12 T3) — the tooling may not change unexplained.

Phases 10 and 11 each changed the mechanism (`scripts/`, `schema/`) and left the
documents that explain it describing the old one, and nothing noticed. This is the
noticing: a unit of change that touches the mechanism must also touch at least one
file a human reads for understanding, or the gate fails.

Which paths are mechanism, which are understanding, and where the rule starts are
instance configuration — docsys.yaml `paired_change:` — not literals here.

The unit is one commit, plus the uncommitted work that will become the next one.
It is deliberately not the branch: a phase-long branch nearly always touches some
document, so a branch-level rule would have passed Phase 11, the case that
motivated it. It is also not a proof of adequacy — a one-word edit to a fiche
satisfies it — only that a change to the tooling was not made in silence.

    python3 scripts/paired_change.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PENDING = "uncommitted changes (what the next commit will contain)"


class AnchorError(ValueError):
    """`paired_change.since` cannot be used. The message names the key and the fix."""


def touches(path, prefixes):
    return any(path.startswith(p) for p in prefixes)


def unpaired(units, mechanism, understanding):
    """The units that touch the mechanism and nothing that explains it.
    `units` is [(label, [changed paths])]; returns [(label, [mechanism paths])]."""
    offenders = []
    for label, paths in units:
        mech = [p for p in paths if touches(p, mechanism)]
        if mech and not any(touches(p, understanding) for p in paths):
            offenders.append((label, mech))
    return offenders


def report(offenders, understanding):
    """Lines a reader with no other context can act on: the unit, its files, the fix."""
    lines = [f"PAIRED CHANGE: {len(offenders)} change(s) touched the tooling and nothing that explains it"]
    for label, mech in offenders:
        lines.append(f"  {label}")
        lines.extend(f"    {p}" for p in mech)
    lines.append("  fix: in the same commit, update what a reader would need to learn about the change "
                 f"— a file under {', '.join(understanding)}. "
                 "A commit already made cannot be paired afterwards: amend it if unpublished, "
                 "otherwise move `paired_change.since` in docsys.yaml past it, which is a reviewable, "
                 "deliberate acceptance.")
    return lines


def _git(root, *args, check=True):
    return subprocess.run(["git", "-C", root, "-c", "core.quotepath=off", *args],
                          check=check, capture_output=True, text=True)


def _check_anchor(since, root):
    if _git(root, "rev-parse", "--verify", "--quiet", f"{since}^{{commit}}", check=False).returncode != 0:
        shallow = _git(root, "rev-parse", "--is-shallow-repository").stdout.strip() == "true"
        cause = ("this is a shallow clone, so the history that holds it was not fetched — "
                 "fetch full history (`git fetch --unshallow`, or `fetch-depth: 0` in CI)"
                 if shallow else
                 "no such commit in this repository — set `paired_change.since` in docsys.yaml "
                 "to a commit of this history")
        raise AnchorError(f"`paired_change.since` ({since}) cannot be resolved — fix: {cause}.")
    if _git(root, "merge-base", "--is-ancestor", since, "HEAD", check=False).returncode != 0:
        raise AnchorError(f"`paired_change.since` ({since}) is not an ancestor of HEAD — "
                          "fix: set it in docsys.yaml to a commit on this branch's history.")


def commit_units(since, root):
    """One (label, paths) per non-merge commit in since..HEAD, oldest first. The anchor
    itself is not examined — the rule starts after it."""
    _check_anchor(since, root)
    out = _git(root, "log", "--reverse", "--no-merges", "--no-renames", "--name-only",
               "--format=%x1e%h %s", f"{since}..HEAD").stdout
    units = []
    for record in out.split("\x1e")[1:]:
        label, *paths = record.split("\n")
        units.append((label, [p for p in paths if p]))
    return units


def pending_unit(root):
    """The uncommitted change against HEAD — tracked files, staged or not — or None.
    Renames are split into delete + add so moving a script out of scripts/ still
    counts. Untracked files are the `worktree` check's business."""
    result = _git(root, "diff", "--name-only", "--no-renames", "HEAD", check=False)
    paths = [p for p in result.stdout.splitlines() if p] if result.returncode == 0 else []
    return (PENDING, paths) if paths else None


def main():
    from docsys_config import ConfigError, load_config  # imports pyyaml
    try:
        cfg = load_config()["paired_change"]
    except ConfigError as exc:
        print(f"PAIRED CHANGE: {exc}")
        return 1
    root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
    try:
        units = commit_units(cfg["since"], root)
    except AnchorError as exc:
        print(f"PAIRED CHANGE: docsys.yaml: {exc}")
        return 1
    pending = pending_unit(root)
    if pending:
        units.append(pending)
    offenders = unpaired(units, cfg["mechanism"], cfg["understanding"])
    if offenders:
        print("\n".join(report(offenders, cfg["understanding"])))
        return 1
    print(f"Paired change OK ({len(units)} change(s) since {cfg['since'][:7]}; "
          "none touched the tooling without the account of it).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
