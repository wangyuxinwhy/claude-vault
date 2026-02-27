---
summary: Python 3.12+ type statements create lazy aliases that need explicit unwrapping
tags: [python, type-hints, gotcha]
date: 2026-02-28
---

# Type Alias Lazy Resolution

## Problem

Python 3.12+ `type` statement creates `TypeAliasType` — a lazy object. `get_type_hints()` returns it as-is, not the resolved type. Code checking `hasattr(hint, "__metadata__")` silently skips these fields.

## The danger

Silent failure. Validation, ORM mapping, or any metadata-driven logic just doesn't run. No error, no warning.

## Solution

```python
from typing import TypeAliasType

def unwrap_type(hint):
    while isinstance(hint, TypeAliasType):
        hint = hint.__value__
    return hint
```

`while` loop handles nested aliases (`type A = Annotated[...]`, `type B = A`).

## Same family of problems

- PEP 810 lazy imports: reification triggered by assignment (Brett Cannon article)
- PEP 649 deferred annotation evaluation
- General pattern: Python is moving toward lazy-by-default; framework code must explicitly resolve
