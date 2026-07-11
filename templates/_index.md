---
title: "Templates — one skeleton per force"
force: orient
verb: situate
formative: true
view: synchronic
provenance: { type: function, id: doc-system }
status: stable
---

One template per illocutionary force (see `../writing.md`). Each skeleton carries pre-filled frontmatter, its force's move structure, and comments recalling the stake and failure mode. Copy, rename, fill, delete the `<!-- -->` comments.

| Force | Verb | Template | Default view |
|---|---|---|---|
| orient | situate | [README.md](README.md) | synchronic |
| explain | illuminate | [ARCHITECTURE.md](ARCHITECTURE.md) | synchronic |
| describe | specify | [reference.md](reference.md) | synchronic |
| prove | demonstrate | [validation-report.md](validation-report.md) | diachronic |
| account | report against | [CHANGELOG.md](CHANGELOG.md) | diachronic |
| instruct | walk through | [runbook.md](runbook.md) | synchronic |
| teach | bring along | [tutorial.md](tutorial.md) | synchronic |
| mandate | require | [CONTRIBUTING.md](CONTRIBUTING.md) | synchronic |
| commit | promise precisely | [charter.md](charter.md) | synchronic |
| propose | argue | [RFC.md](RFC.md) | diachronic |
| decide | justify | [ADR.md](ADR.md) | diachronic |

Quick rule: **diachronic** forces (prove, account, propose, decide) produce records that **freeze** — you don't rewrite them, you create new ones. **Synchronic** forces produce **maintained** states. See `../structure.md` §6.
