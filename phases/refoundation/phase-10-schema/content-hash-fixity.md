---
title: "Decision — content-hash fixity: an optional `hash:` seals each frozen record"
id: 01KZ2EQ4002XZHJ733Y4B2AAVX
slug: content-hash-fixity
force: decide
intention: suasive
view: diachronic
provenance: { type: project, id: phase-10-schema }
constitutive: yes
concerns: [steering, structuring, operationalizing]
distance: initiated
audience: [contributor, decider]
reader: H+M
status: accepted
retention: permanent
supersedes: null
superseded-by: null
hash: sha256:8553c69c8973f789171094909139dc88b65b48eeb9ba00be071d457607318e02
---

## Status

accepted — 2026-08-03.
Complements ADR-028 (ULID identifiers): that record gave a document its *identity*, this one gives it its *fixity*.

## Context and forces in play *(justify)*

A frozen record — `view: diachronic`, closed — is supposed to be immutable.
Nothing enforced that.
`CONTRIBUTING` says an edited ADR is reverted, but the rule lived only in prose: a silent edit to a closed decision passed every check we had, and the corpus would carry a decision that says something other than what was decided.
This is precisely the failure documentality is about — a record that no longer testifies to the act it recorded.

Git's commit SHA already fixes content, so it deserved a direct answer rather than a dismissal.
A git SHA fixes *the whole tree at a moment*, not *this record*; it is defined only inside this repository's object graph.
A record copied into another repository, quoted in a generated surface, or handed to a reader as a file carries none of it.
The ULID answers "which record"; nothing answered "is this that record's content".

## Decision

1. **An optional `hash:` field seals a frozen record**, of the form `sha256:<64 lowercase hex>`.
   Optional by design: sealing is an act performed *at freeze*, not a property every document must have.

2. **The canonical form hashed is defined exactly** — this definition is the contract, and changing it invalidates every existing seal:
   read UTF-8 and normalise line endings to LF; split at the frontmatter fences; from the frontmatter drop the `hash:` line itself, strip trailing whitespace, drop blank lines, and **sort** the remaining lines; from the body strip trailing whitespace per line and strip leading and trailing blank lines; hash `sorted-frontmatter + "\n---\n" + body + "\n"`.

3. **The frontmatter is sorted before hashing**.
   The seal fixes a record's content and coordinates, not the order the keys happen to be written in — so a later formatting pass does not read as tampering.

4. **A record is *frozen*, and so eligible for sealing, when** `view: diachronic` **and** `provenance.type: project` **and** `status` is `accepted`, `done`, or `stable`.
   Maintained registers (`steering/ADR.md`, `CHANGELOG.md`) are `diachronic` but belong to a *function*, and are append-only rather than frozen — they are not sealed.

5. **Re-sealing is a deliberate, separate act**.
   `hash_seal.py` refuses to overwrite an existing seal without `--reseal`.
   A broken seal is a question, not a verdict: either the change is wrong and should be reverted — the seal did its job — or the record is being deliberately re-frozen.

6. **Fixity joins the gate**.
   `scripts/hash_check.py` runs in `scripts/check.py`; a broken seal fails the build.

## Entail — what follows

- `scripts/hash_seal.py` mints seals (`--frozen` for every unsealed frozen record, `--print` to compute without writing, `--reseal` to re-freeze); `scripts/hash_check.py` verifies them and reports frozen-but-unsealed records.
- `hash` is declared in `schema/frontmatter.schema.json` and its format is a lint error if malformed.
- The frozen records of the **refoundation era** (phases 06–10, 25 records) were sealed at the close of Phase 10 — *after* the schema sweep, since the sweep rewrote their frontmatter.
  The naive-sketch era (01–05) is deliberately left unsealed and tracked in `steering/technical-debt.md`: those records froze before the seal existed, so sealing them fixes their *current* content rather than the content they closed with, and that deserves a conscious act rather than a bulk sweep.
- A force template is **not** a frozen record even though its specimen frontmatter says `provenance: { type: project, id: <phase-or-project-id> }`; a placeholder id is not a project, and `is_frozen` excludes it.
- Sealing is the record-level counterpart of `pin`: `pin` fixes what a document *points at*, `hash` fixes what a document *is*.

## Honest limit

The seal is only as trustworthy as the place it is stored.
It lives in the record it seals, so anyone able to edit the record is able to edit the seal — this is tamper-*evidence* against accident and drift, not tamper-*proofing* against a determined actor.
Real tamper-proofing needs the seal kept somewhere the editor does not control (a signature, an external register, a timestamping service), and we are not doing that.

It also adds friction on purpose: a corpus-wide migration that touches frozen records — exactly what Phase 10 was — now breaks every seal it crosses and has to re-seal consciously.
That is the feature, but it is a real cost, and it will be felt.
