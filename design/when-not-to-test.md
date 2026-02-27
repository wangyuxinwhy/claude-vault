---
summary: Skip tests for glue code whose output is trivially human-verifiable
tags: [testing, pragmatism]
date: 2026-02-28
---

# When Not to Test

Not all code deserves tests. Tests have maintenance cost — if that cost exceeds the bugs they'd catch, skip them.

Skip tests when:
- Output is human-verifiable at a glance (e.g., a generated INDEX.md)
- The code is short glue logic (<50 lines) with no tricky edge cases
- A test would just restate the implementation
- The code runs as a one-shot script, not a library

Write tests when:
- Logic has non-obvious edge cases
- Failure is silent or hard to detect
- The code is used by others as a dependency
- Correctness matters more than speed of iteration
