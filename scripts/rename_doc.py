#!/usr/bin/env python3
"""Safe rename — move a file or folder and rewrite every relative link to it.

The refactoring capacity that unblocks the deferred ULID migration (ADR-028): a
rename should never rot a link. It `git mv`s OLD to NEW, then rewrites, across all
tracked Markdown, the *target* of every relative link that pointed at the moved
path (or anything under it, for a folder) — recomputing both inbound links and the
moved files' own outbound links for their new depth. Anchors and link titles are
preserved. Stdlib only; run inside the repo.

    python3 scripts/rename_doc.py OLD NEW
    python3 scripts/rename_doc.py --dry-run OLD NEW

Rewrites link TARGETS (what linkcheck verifies). Display text and inline-code path
mentions are prose and are left for a separate pass.
"""
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)]+)(\))")


def tracked_md():
    return subprocess.check_output(["git", "ls-files", "*.md"], text=True).splitlines()


def build_mapping(old, new):
    """old_abs(repo-relative, normalized) -> new_abs for every file that moves."""
    old = os.path.normpath(old)
    new = os.path.normpath(new)
    if os.path.isdir(old):
        mapping = {}
        for f in subprocess.check_output(["git", "ls-files", old], text=True).splitlines():
            f = os.path.normpath(f)
            mapping[f] = os.path.normpath(os.path.join(new, os.path.relpath(f, old)))
        return mapping
    return {old: new}


def rewrite_target(target, old_dir, new_dir, mapping, file_moved):
    if target.startswith(("http://", "https://", "#", "mailto:")):
        return target
    # split off a link title:  path "Title"
    parts = target.split(None, 1)
    pathpart, title = parts[0], (parts[1] if len(parts) > 1 else None)
    path, _, anchor = pathpart.partition("#")
    if not path or path.startswith("<"):
        return target
    old_abs = os.path.normpath(os.path.join(old_dir, path))
    target_moved = old_abs in mapping
    # Only touch a link whose target moved, or whose own file moved (base changed).
    # Never "normalize" an otherwise-unaffected link.
    if not target_moved and not file_moved:
        return target
    new_abs = mapping.get(old_abs, old_abs)
    new_rel = os.path.relpath(new_abs, new_dir)
    if path.endswith("/") and not new_rel.endswith("/"):
        new_rel += "/"  # preserve directory-link trailing slash
    if path.startswith("./") and not new_rel.startswith((".", "/")):
        new_rel = "./" + new_rel
    rebuilt = new_rel + ("#" + anchor if anchor else "")
    return rebuilt + (" " + title if title else "")


def rename_path(old, new, dry=False):
    """git mv OLD to NEW and rewrite every affected relative link. Returns
    (changed_files, changed_links). Does NOT run linkcheck (callers do)."""
    old, new = os.path.normpath(old), os.path.normpath(new)
    if not os.path.exists(old):
        raise SystemExit(f"OLD does not exist: {old}")
    if os.path.exists(new):
        raise SystemExit(f"NEW already exists: {new}")

    mapping = build_mapping(old, new)  # pre-move path -> post-move path
    premove_files = [os.path.normpath(f) for f in tracked_md()]  # captured before the move

    if not dry:
        os.makedirs(os.path.dirname(new) or ".", exist_ok=True)
        subprocess.check_call(["git", "mv", old, new])

    changed_files = 0
    changed_links = 0
    for pre in premove_files:
        post = mapping.get(pre, pre)  # where this file lives after the move
        read_path = post if not dry else pre  # after a real move, the file is at `post`
        old_dir, new_dir = os.path.dirname(pre), os.path.dirname(post)
        file_moved = old_dir != new_dir
        with open(read_path, encoding="utf-8") as fh:
            src = fh.read()

        local = [0]

        def repl(m):
            new_t = rewrite_target(m.group(2), old_dir, new_dir, mapping, file_moved)
            if new_t != m.group(2):
                local[0] += 1
            return m.group(1) + new_t + m.group(3)

        out = LINK_RE.sub(repl, src)
        if local[0]:
            changed_files += 1
            changed_links += local[0]
            if not dry:
                with open(read_path, "w", encoding="utf-8") as fh:
                    fh.write(out)
    return changed_files, changed_links


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    if len(args) != 2:
        raise SystemExit("usage: rename_doc.py [--dry-run] OLD NEW")
    old, new = args
    cf, cl = rename_path(old, new, dry=dry)
    print(f"{'[dry-run] ' if dry else ''}moved {old} -> {new}; "
          f"rewrote {cl} link(s) in {cf} file(s)")
    return 0 if dry else subprocess.call([sys.executable, "scripts/linkcheck.py"])


if __name__ == "__main__":
    sys.exit(main())
