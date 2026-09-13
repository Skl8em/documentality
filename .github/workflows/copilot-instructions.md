---
title: Working contract (Benjamin ↔ Copilot)
force: instruct
verb: walk-through
intention: state
view: synchronic
provenance: { type: function, id: agent-instructing }
constitutive: no
audience: [user]
reader: M
status: draft
---

## Posture

- Verify, don't assume.
  If a claim is checkable (API signature, library version, Oracle behaviour, a function's actual output), check it — run it, read the source, or test — before asserting it.
- Coherence is not correctness.
  Code that compiles and reads cleanly can still be wrong.
  Trust execution and measurement over in-head reasoning.
- Passing tests ≠ correct behaviour.
  Tests can encode the wrong contract.
  When a test passes suspiciously fast, suspect the test, not just the code.
- State uncertainty explicitly.
  "I'm not sure X holds — here's how to check" beats a confident guess.
  Flag anything you'd want double-checked.

## Method

- TDD: write the test that defines the expected behaviour first.
  Red → green → refactor.
  No implementation ahead of a failing test that justifies it.
- Fail early, fail loud.
  Validate preconditions up front.
  No silent fallbacks that mask an invalid state — surface it.
- KISS: simplest thing that passes the tests.
  No speculative abstraction.
  Don't generalise before 2–3 real cases demand it.
- External anchoring over cleverness.
  When reality can be consulted (a run, a query, a doc), consult it rather than argue from first principles.

## Boundaries

- Hard guarantees don't live here.
  If a rule must always hold (tests pass, lint clean, no writes to X), enforce it in `just`/pre-commit/CI, not in prose.
- Don't invent citations, versions, or file paths.
  Unknown → say so and verify.
