---
title: "Testing"
force: propose
register: govern
intention: suasive
view: diachronic
provenance: { type: function, id: imagining }
distance: initiated
audience: [contributor, decider]
reader: H+M
status: draft
---

I want a tool where you index testable claims in the documentation to actual test of that claim. That way you can check if the documentation is up-to-date and create single repositories of truth.

E.g.
According to ADR-015 -> links to a test that ADR-015 is still active
We have five perlocutory intentions -> links to a test that the yaml with the perlocutory intentions allowed in the linter are exactly 5.

Test would be ideally in a DSL, with runners either rust, python, maybe javascript or R (for qmd) to facilitate usage in diverse places (avoid other technology stack introduction).

run the test to see where documentation has become outdated.
Test if the file that holds the link has an earlier commit that the test, if so, require a review (use review flag to update commit). 