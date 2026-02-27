---
summary: APIs should not promise more than they deliver — property, setter, type hints, and platform capabilities
tags: [api-design, philosophy]
date: 2026-02-28
---

# API Honesty

An API's form communicates a promise to the caller. Breaking that promise creates bugs, surprises, and mistrust.

## Property vs method

Property promises: cheap, deterministic, no side effects.
Method promises: work happens, may fail, may be slow.

Putting IO in a setter breaks the property promise. Using async property hides latency behind attribute access.

## Setter side effects

OK: maintaining invariants between independent fields (e.g., ensuring `start <= end`).
Not OK: database writes, notifications, logging to external services.

If it can fail, it's a method.

## Type hints

`list[str]` promises "I need a list" when you only need "something iterable." The caller is unnecessarily constrained. Use `Sequence[str]` — promise only what you actually require.

## Platform capabilities

R can't automatically capture all plots (no chokepoint). GoFigr chose explicit `publish()` rather than faking auto-capture that silently misses base R graphics.

If the platform doesn't support it, don't pretend it does.

## The common thread

Postel's Law: be liberal in what you accept, conservative in what you send.
Principle of Least Astonishment: behavior should match the caller's first intuition.

Both reduce to: **don't let your API lie**.
