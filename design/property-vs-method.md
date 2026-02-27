---
summary: Property for cheap state access, method for work that may fail or cost time
tags: [python, api-design, property]
date: 2026-02-28
---

# Property vs Method

## Core rule

- **Property** communicates: cheap, deterministic, no side effects, safe to read repeatedly.
- **Method** communicates: work is happening, may fail, may be slow, may have side effects.

## Setter guidelines

- OK in setter: simple validation, maintaining invariants between independent fields.
- Not OK in setter: IO, persistence, notifications, anything that can fail.
- If derived value can be computed from existing state, use a read-only property — don't store redundant state.

## Async

- Technically possible to have `async` property in Python. Never do it.
- Use async `classmethod` for loading, keep properties synchronous, use async `save()` for persistence.

## In protocols

- Read-only: use `@property`.
- Read-write: just declare as attribute annotation (`is_active: bool`).
