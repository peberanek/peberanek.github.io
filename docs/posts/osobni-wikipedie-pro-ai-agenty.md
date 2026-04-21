---
date: 2026-04-08
draft: true  # TODO: remove
tags:
  - TODO
---

# Osobní Wikipedie pro AI agenty

Post on X: https://x.com/karpathy/status/2040470801506541998
Spec (for LLMs): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

* QMD - Query Markup Documents: https://github.com/tobi/qmd (cli tool)
* Může sloužit pro ukládání užitečných chatů s LLMs (aby se informace neztratily)
  * Prehlceni informacemi, fomo
  * Private credit
  * Linux overview
  * LLMs a genAI, llama.cpp
* Datové zdroje
  * Poznámky (notes)
  * Osobní blog

## Dosavadni progres

Designed the system
- Read llm-wiki.md together and decided on the architecture: git repo, submodule for the website, one-at-a-time ingestion with you in the loop.
- Settled on git submodule (over direct path or symlink) for the website repo — solves both sandboxing and content discovery.

Set up the repo structure
- Added peberanek.github.io as a git submodule at raw/website/
- Created raw/notes/ (for personal markdown notes) and raw/references/ (for clipped docs)
- Moved llm-wiki.md and conventional-commits.md to raw/references/
- Created the full wiki/ skeleton: projects/, topics/, skills/, sources/
- Wrote CLAUDE.md — the schema that tells me how to maintain the wiki across sessions (page conventions, workflows for ingest/query/lint, commit message rules)
- Initialized wiki/index.md and wiki/log.md

Ingested two sources

1. raw/website/docs/cv.md → created:
  - sources/cv.md — career timeline, skills, education summary
  - overview.md — high-level synthesis of who you are
  - projects/ai-sandbox.md, projects/internal-testing-framework-lvm.md, projects/personal-finance.md — stubs, to be enriched from projects.md
  - skills/python.md, skills/linux.md, skills/generative-ai.md
2. raw/references/karierni-smer-po-vypovedi-na-univerzite-karlove.md → created:
  - sources/karierni-smer.md — summary of the career counseling conversation
  - topics/career-direction.md — current situation, what energizes/drains, values, the interpersonal dynamics pattern to work on
  - Updated overview.md with a current status section

Everything committed in two logical commits following Conventional Commits format.
