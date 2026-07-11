---
title: "Templates — one skeleton per force"
force: orient
verb: situate
perlocution: locate
view: synchronic
provenance: { type: function, id: doc-system }
status: stable
---

One template per illocutionary force (see `../writing.md`). Each skeleton carries pre-filled frontmatter, its force's move structure, and comments recalling the stake and failure mode. Copy, rename, fill, delete the `<!-- -->` comments.

The `door` column is the newcomer-facing grouping (`../writing.md` §0): **know** (savoir), **do** (savoir-faire), **govern & record** (the project's own acts). `perl.` is the perlocutionary target when the force reshapes the reader (`none` = the reader is served, not changed).

| Force | Verb | Door | Perl. | View | Template |
|---|---|---|---|---|---|
| orient | situate | know | locate | synchronic | [README.md](README.md) |
| explain | illuminate | know | model | synchronic | [ARCHITECTURE.md](ARCHITECTURE.md) |
| describe | specify | know | none | synchronic | [reference.md](reference.md) |
| account | report-against | know / record | none | diachronic | [CHANGELOG.md](CHANGELOG.md) |
| prove | demonstrate | record | convince | diachronic | [validation-report.md](validation-report.md) |
| teach | bring-along | do | enable | synchronic | [tutorial.md](tutorial.md) |
| instruct | walk-through | do | none | synchronic | [runbook.md](runbook.md) |
| recommend | advise | do | none | synchronic | [recommend.md](recommend.md) |
| mandate | require | govern | none | synchronic | [CONTRIBUTING.md](CONTRIBUTING.md) |
| commit | promise-precisely | govern | none | synchronic | [charter.md](charter.md) |
| propose | argue | govern | none | diachronic | [RFC.md](RFC.md) |
| decide | justify | govern & record | convince | diachronic | [ADR.md](ADR.md) |

Two quick rules:

- **View.** Diachronic forces (prove, account, propose, decide) produce records that **freeze** — you don't rewrite them, you create new ones. Synchronic forces produce **maintained** states. See `../structure.md` §6.
- **Deontic gradient (do → govern).** Within action, three strengths: `instruct` ("here is how"), `recommend` ("you should", non-binding), `mandate` ("you must", binding). Pick by how much you are actually willing to enforce.
