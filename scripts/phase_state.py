#!/usr/bin/env python3
"""Phase state — every place that speaks of the current phase agrees with the ledger
(Phase 12 T6(b)).

The ledger (`phases.ledger` in docsys.yaml, checked by phase_ledger.py) declares where
the project is. This check reads every other place that says so and fails where one
disagrees:

  - folders: a done or current phase has its folder, and no phase folder exists that
    the ledger does not list;
  - tables: each phase row of a configured table (the roadmap, the phases index)
    carries the marker of the ledger's status, a number the ledger has not given is
    refused (ADR-038), the current phase has a row, and a pattern that matches no row
    is an error rather than a pass;
  - mentions: no living document names, by number, a phase above the highest the
    ledger has numbered (ADR-038 again; the era name "Phase II" is not a number). A
    frozen record is out of scope: it says what was true when it froze, it cannot be
    edited, and ADR-038 itself quotes a forward-numbered sentence as its example — a
    red there could never be cleared, and red must mean wrong;
  - status: the root README has exactly one status line, and it names the current
    phase;
  - `phase:` fields: each names a numbered phase of the ledger, and none is behind
    the last closed phase unless the ledger lists it under `lagging:` with a reason —
    an allowance that fails once the document has caught up.

It verifies that the places agree, not that any of them is true: a status paragraph
can name the right phase and still describe it wrongly. Where each place is, and the
shape of its rows, is instance configuration (`phases:` in docsys.yaml).

Reads frontmatter and the ledger through scripts/yaml_frontmatter.py, so it needs
`pyyaml` — the devShell provides it.

    python3 scripts/phase_state.py
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def numbered(data):
    """{number: entry} for every phase the ledger has numbered."""
    return {int(e["number"]): e for e in data["phases"] if "number" in e}


def current(data):
    return next((int(e["number"]), e) for e in data["phases"] if e["status"] == "current")


def last_done(data):
    done = [n for n, e in numbered(data).items() if e["status"] == "done"]
    return max(done) if done else None


def folder_errors(data, root, folder, tracked):
    """A numbered phase without its folder; a phase folder the ledger does not list.
    `tracked` is the repository's tracked paths: a folder exists when a file is in it."""
    expected = {f"{root}/{e['era']}/{folder.format(number=n, name=e['name'])}": (n, e)
                for n, e in numbered(data).items()}
    present = {"/".join(p.split("/")[:3]) for p in tracked
               if p.startswith(root + "/") and len(p.split("/")) >= 4}
    errors = []
    for path, (n, e) in expected.items():
        if path not in present:
            errors.append(f"{path}: phase {n} ({e['name']}, {e['status']}) has no folder — it does not exist; "
                          f"fix: create it, or correct the phase's era or name in the ledger")
    for path in sorted(present - set(expected)):
        errors.append(f"{path}: a phase folder that is not in the ledger — fix: add its phase to the ledger, "
                      f"or move the folder to the path the ledger gives it")
    return errors


def table_errors(data, markers, path, row, text):
    """Each phase row of one table against the ledger. `markers` maps a ledger status
    to the word a row shows for it; `row` has the groups `number` (optional) and
    `marker` (optional, so a row without one is reported, not skipped)."""
    by_number = numbered(data)
    cur, cur_entry = current(data)
    rows, seen, errors = 0, set(), []
    for i, line in enumerate(text.splitlines(), 1):
        m = row.match(line)
        if not m:
            continue
        rows += 1
        number, marker = m.group("number"), m.group("marker")
        if marker is None:
            errors.append(f"{path}:{i}: a phase row with no status marker — fix: add the ledger's status "
                          f"after the phase's name, e.g. `*({markers['done']})*`")
            continue
        word = marker.split(" — ")[0].strip()
        if number is None:
            if word != markers["planned"]:
                errors.append(f"{path}:{i}: an unnumbered row marked {word!r}; only a planned phase is "
                              f"unnumbered, and it is marked {markers['planned']!r} — fix: give the row its "
                              f"number, or mark it `*({markers['planned']})*`")
            continue
        n = int(number)
        entry = by_number.get(n)
        if entry is None:
            errors.append(f"{path}:{i}: phase {n} is not numbered in the ledger; a planned phase has no number "
                          f"(ADR-038) — fix: write the row without its number, or start the phase in the ledger")
            continue
        seen.add(n)
        want = markers[entry["status"]]
        if word != want:
            errors.append(f"{path}:{i}: phase {n} is marked {word!r}, but the ledger says {entry['status']} — "
                          f"fix: mark it `*({want})*`")
    if rows == 0:
        return [f"{path}: no phase row matches the configured row pattern — fix: correct the row pattern "
                f"for this table in docsys.yaml (`phases.tables`), or the table's rows"]
    if cur not in seen:
        errors.append(f"{path}: the current phase, phase {cur} ({cur_entry['name']}), has no row — "
                      f"fix: add its row, marked `*({markers['current']})*`")
    return errors


def mention_errors(data, mention, docs, frozen=()):
    """A phase named by a number the ledger has not given. `mention` has the group
    `number`; `docs` maps a path to its text; paths in `frozen` are not read."""
    highest = max(numbered(data))
    errors = []
    for path in sorted(set(docs) - set(frozen)):
        for i, line in enumerate(docs[path].splitlines(), 1):
            for m in mention.finditer(line):
                n = int(m.group("number"))
                if n > highest:
                    errors.append(f"{path}:{i}: {m.group(0)!r} names phase {n}, but the ledger numbers phases "
                                  f"only up to {highest}; unstarted work is named, never numbered (ADR-038) — "
                                  f"fix: name the work instead, or start the phase in the ledger")
    return errors


def status_errors(data, path, line, text):
    """The one status line of `path` names the current phase. `line` has the group
    `number`."""
    cur, cur_entry = current(data)
    found = [(i, m) for i, ln in enumerate(text.splitlines(), 1) for m in [line.match(ln)] if m]
    if not found:
        return [f"{path}: no status line matches the configured pattern — fix: restore the status line, or "
                f"correct `phases.status` in docsys.yaml"]
    if len(found) > 1:
        return [f"{path}: {len(found)} status lines (lines {', '.join(str(i) for i, _ in found)}) — "
                f"fix: keep one, naming the current phase"]
    i, m = found[0]
    n = int(m.group("number"))
    if n != cur:
        return [f"{path}:{i}: the status line names phase {n}, but the current phase is {cur} "
                f"({cur_entry['name']}) — fix: rewrite the status paragraph for phase {cur}"]
    return []


def field_errors(data, field, fields):
    """Each `phase:` value against the ledger. `fields` maps a path to its value;
    `field` is the value's format. An allowance in `lagging:` must still be needed."""
    by_value = {field.format(number=n, name=e["name"]): n for n, e in numbered(data).items()}
    cur, cur_entry = current(data)
    now = field.format(number=cur, name=cur_entry["name"])
    done = last_done(data)
    floor = field.format(number=done, name=numbered(data)[done]["name"]) if done else None
    lagging = {item["path"] for item in data.get("lagging", [])}
    errors = []
    for path in sorted(fields):
        value = str(fields[path])
        n = by_value.get(value)
        behind = n is not None and done is not None and n < done
        if n is None:
            errors.append(f"{path}: `phase: {value}` is not a numbered phase in the ledger — "
                          f"fix: write the phase the document is current as of, e.g. `phase: {now}`")
        elif behind and path not in lagging:
            errors.append(f"{path}: `phase: {value}` is behind {floor}, the last phase closed; a document is "
                          f"re-read and its `phase:` raised when a phase closes — fix: re-read it whole and set "
                          f"`phase: {now}`, or list it under `lagging:` in the ledger with a reason")
        elif not behind and path in lagging:
            errors.append(f"{path}: listed as lagging in the ledger but no longer behind (`phase: {value}`) — "
                          f"fix: remove its `lagging:` entry")
    for path in sorted(lagging - set(fields)):
        errors.append(f"{path}: listed as lagging in the ledger, but it has no `phase:` field — "
                      f"fix: remove the entry, or correct its path")
    return errors


def main():
    from docsys_config import ConfigError, load_config
    from hash_seal import FROZEN_STATUSES
    import phase_ledger
    from yaml_frontmatter import FrontmatterError, load, values, yaml

    root_dir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
    os.chdir(root_dir)
    try:
        cfg = load_config()["phases"]
    except ConfigError as exc:
        print(f"PHASE STATE: {exc}")
        return 1
    try:
        with open(cfg["ledger"], encoding="utf-8") as fh:
            data = phase_ledger.parse(fh)
    except (OSError, yaml.YAMLError) as exc:
        print(f"PHASE STATE: {cfg['ledger']}: cannot be read ({exc}) — fix: see the phase-ledger check")
        return 1
    if phase_ledger.ledger_errors(data, cfg["ledger"]):
        print(f"PHASE STATE: {cfg['ledger']} breaks its own rules — fix: see the phase-ledger check first")
        return 1

    tracked = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
    docs = {}
    for path in (p for p in tracked if p.endswith(".md")):
        with open(path, encoding="utf-8") as fh:
            docs[path] = fh.read()
    fields, frozen = {}, set()
    for path in docs:
        try:
            fm = values(load(path))
        except FrontmatterError:
            continue  # the frontmatter check reports it
        if fm.get("phase") is not None:
            fields[path] = fm["phase"]
        if fm.get("status") in FROZEN_STATUSES:
            frozen.add(path)

    errors = folder_errors(data, cfg["root"], cfg["folder"], tracked)
    for table in cfg["tables"]:
        errors += table_errors(data, cfg["markers"], table["path"], re.compile(table["row"]),
                               docs.get(table["path"], ""))
    errors += mention_errors(data, re.compile(cfg["mention"]), docs, frozen)
    errors += status_errors(data, cfg["status"]["path"], re.compile(cfg["status"]["line"]),
                            docs.get(cfg["status"]["path"], ""))
    errors += field_errors(data, cfg["field"], fields)

    for message in errors:
        print(f"PHASE STATE: {message}")
    if errors:
        print(f"\nPHASE STATE: {len(errors)} place(s) disagree with {cfg['ledger']}.")
        return 1
    cur, entry = current(data)
    print(f"Phase state OK: folders, {len(cfg['tables'])} table(s), mentions, the status line and "
          f"{len(fields)} `phase:` field(s) agree with the ledger (current: phase {cur}, {entry['name']}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
