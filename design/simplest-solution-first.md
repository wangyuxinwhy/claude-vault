---
summary: Resist the urge to reach for libraries when a few lines of stdlib can do the job
tags: [design, yagni, kiss]
date: 2026-02-28
---

# Simplest Solution First

When parsing simple YAML frontmatter (key-value pairs with optional list syntax), a regex + string split is enough. No need for `pyyaml` or `ruamel.yaml`.

Signs you're over-engineering:
- Adding a dependency for a single use case
- The library's API is more complex than the problem itself
- You spend more time configuring the tool than writing the solution

The best code is the code that doesn't need explaining, doesn't need dependencies, and doesn't need maintaining.
