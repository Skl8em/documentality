#!/usr/bin/env python3
"""Paired-change check (Phase 12 T3) — the tooling may not change unexplained.

Phases 10 and 11 each changed the mechanism (`scripts/`, `schema/`) and left the
documents that explain it describing the old one, and nothing noticed. This is the
noticing: a unit of change that touches the mechanism must also touch at least one
file a human reads for understanding, or the gate fails.

Which paths are mechanism, which are understanding, which need no account, where the
rule starts and where it is enforced are instance configuration — docsys.yaml
`paired_change:` — not literals here.

The unit is one commit, plus the uncommitted work that will become the next one.
It is deliberately not the branch: a phase-long branch nearly always touches some
document, so a branch-level rule would have passed Phase 11, the case that
motivated it. It is also not a proof of adequacy — a one-word edit to a fiche
satisfies it — only that a change to the tooling was not made in silence.

Two things are not a change to the mechanism, because there is nothing to explain: a
file under an `exempt` prefix (the tests), and a Python edit whose code is unchanged —
comments, docstrings, formatting.

It fails only where work lands: a branch named in `enforce_on`, or a detached HEAD
(a pull request's merge commit in CI). On any other branch the same findings are a
warning and the exit status is 0, so work in progress is not blocked.

    python3 scripts/paired_change.py
"""
import ast
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PENDING = "uncommitted changes (what the next commit will contain)"


class AnchorError(ValueError):
    """`paired_change.since` cannot be used. The message names the key and the fix."""


class BranchListError(ValueError):
    """`paired_change.enforce_on` names no branch that exists. The message names the key
    and the fix."""


def touches(path, prefixes):
    return any(path.startswith(p) for p in prefixes)


def _strip_docstrings(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = node.body
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                del body[0]
                if not body:
                    body.append(ast.Pass())
    return tree


def comment_only(old, new):
    """True when two versions of a Python file differ only in comments, docstrings or
    formatting — their syntax trees, docstrings set aside, are equal. A version that
    does not parse is never comment-only: it is not known to be harmless."""
    try:
        return (ast.dump(_strip_docstrings(ast.parse(old))) ==
                ast.dump(_strip_docstrings(ast.parse(new))))
    except SyntaxError:
        return False


def unpaired(units, mechanism, understanding, exempt=()):
    """The units that touch the mechanism and nothing that explains it.
    `units` is [(label, [changed paths])] or [(label, [changed paths], {paths whose
    change is comment-only})]; returns [(label, [mechanism paths])]. A path under an
    `exempt` prefix, or comment-only, needs no account."""
    offenders = []
    for unit in units:
        label, paths, *rest = unit
        trivial = rest[0] if rest else ()
        mech = [p for p in paths
                if touches(p, mechanism) and not touches(p, exempt) and p not in trivial]
        if mech and not any(touches(p, understanding) for p in paths):
            offenders.append((label, mech))
    return offenders


def enforced(branch, enforce_on):
    """Fail here, or only warn? `branch` is the checked-out branch, None when HEAD is
    detached — a checkout of a pull request's merge commit, which is where work lands."""
    return branch is None or branch in enforce_on


def report(offenders, understanding, branch=None, enforce_on=()):
    """Lines a reader with no other context can act on: the unit, its files, the fix.
    Given a `branch`, the findings are advisory and the header says why."""
    if branch is None:
        lines = [f"PAIRED CHANGE: {len(offenders)} change(s) touched the tooling and nothing that explains it"]
    else:
        lines = [f"WARNING — PAIRED CHANGE (not enforced on branch `{branch}`, only on "
                 f"{', '.join(f'`{b}`' for b in enforce_on)} and detached checkouts): "
                 f"{len(offenders)} change(s) touched the tooling and nothing that explains it — "
                 "this will fail when it lands"]
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


def _show(root, rev, path):
    """A file's text at a revision, or in the working tree when `rev` is None; None if it
    does not exist there."""
    if rev is None:
        try:
            with open(os.path.join(root, path), encoding="utf-8") as fh:
                return fh.read()
        except OSError:
            return None
    result = _git(root, "show", f"{rev}:{path}", check=False)
    return result.stdout if result.returncode == 0 else None


def _comment_only_paths(root, paths, old_rev, new_rev):
    """The Python files among `paths` whose change between two revisions is comment-only.
    A file added or deleted in the unit is never comment-only."""
    trivial = set()
    for path in paths:
        if path.endswith(".py"):
            old, new = _show(root, old_rev, path), _show(root, new_rev, path)
            if old is not None and new is not None and comment_only(old, new):
                trivial.add(path)
    return trivial


def commit_units(since, root):
    """One (label, paths, comment-only paths) per non-merge commit in since..HEAD, oldest
    first. The anchor itself is not examined — the rule starts after it."""
    _check_anchor(since, root)
    out = _git(root, "log", "--reverse", "--no-merges", "--no-renames", "--name-only",
               "--format=%x1e%H %s", f"{since}..HEAD").stdout
    units = []
    for record in out.split("\x1e")[1:]:
        head, *paths = record.split("\n")
        sha, subject = head.split(" ", 1)
        paths = [p for p in paths if p]
        units.append((f"{sha[:7]} {subject}", paths,
                      _comment_only_paths(root, paths, f"{sha}^", sha)))
    return units


def pending_unit(root):
    """The uncommitted change against HEAD — tracked files, staged or not — or None.
    Renames are split into delete + add so moving a script out of scripts/ still
    counts. Untracked files are the `worktree` check's business."""
    result = _git(root, "diff", "--name-only", "--no-renames", "HEAD", check=False)
    paths = [p for p in result.stdout.splitlines() if p] if result.returncode == 0 else []
    return (PENDING, paths, _comment_only_paths(root, paths, "HEAD", None)) if paths else None


def _check_enforce_on(enforce_on, root):
    """At least one listed branch exists, locally or on a remote — CI checks out a
    detached HEAD with remote refs only. A list naming none would make the rule a
    warning everywhere but a detached checkout, silently: a renamed integration branch."""
    refs = _git(root, "for-each-ref", "--format=%(refname)", "refs/heads", "refs/remotes").stdout.split()
    names = {r[len("refs/heads/"):] for r in refs if r.startswith("refs/heads/")}
    names |= {r.split("/", 3)[3] for r in refs if r.startswith("refs/remotes/") and r.count("/") >= 3}
    if not names & set(enforce_on):
        raise BranchListError(f"`paired_change.enforce_on` ({', '.join(enforce_on)}) names no branch of this "
                              "repository, so the rule would only ever warn, except on a detached checkout — "
                              "fix: list the integration branch's current name in docsys.yaml.")


def current_branch(root):
    """The checked-out branch's name, or None when HEAD is detached."""
    result = _git(root, "symbolic-ref", "--short", "-q", "HEAD", check=False)
    return result.stdout.strip() or None


def run(cfg, root):
    """Evaluate the rule for one repository: (exit status, lines to print)."""
    _check_enforce_on(cfg["enforce_on"], root)
    units = commit_units(cfg["since"], root)
    pending = pending_unit(root)
    if pending:
        units.append(pending)
    offenders = unpaired(units, cfg["mechanism"], cfg["understanding"], cfg["exempt"])
    if not offenders:
        return 0, [f"Paired change OK ({len(units)} change(s) since {cfg['since'][:7]}; "
                   "none touched the tooling without the account of it)."]
    branch = current_branch(root)
    if enforced(branch, cfg["enforce_on"]):
        return 1, report(offenders, cfg["understanding"])
    return 0, report(offenders, cfg["understanding"], branch, cfg["enforce_on"])


def main():
    from docsys_config import ConfigError, load_config  # imports pyyaml
    try:
        cfg = load_config()["paired_change"]
    except ConfigError as exc:
        print(f"PAIRED CHANGE: {exc}")
        return 1
    root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
    try:
        code, lines = run(cfg, root)
    except (AnchorError, BranchListError) as exc:
        print(f"PAIRED CHANGE: docsys.yaml: {exc}")
        return 1
    print("\n".join(lines))
    return code


if __name__ == "__main__":
    sys.exit(main())
