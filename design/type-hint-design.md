---
summary: Use minimal traits for input types, bind related params, and use Annotated for semantic clarity
tags: [python, type-hints, api-design]
date: 2026-02-28
---

# Type Hint Design

## Minimal trait principle

Input parameters should require only the capabilities actually used:

- Only iterate? → `Iterable`
- Need `len()` or reuse? → `Sequence`
- Need mutation? → `MutableSequence`
- Need uniqueness? → `AbstractSet`

`list[str]` as a parameter type is almost always wrong — it demands a concrete implementation when you only need a trait.

Output types should be concrete — callers benefit from knowing exactly what they get.

## Bind related parameters

If two parameters must have the same length, they shouldn't be separate:

```python
# Bad: caller can pass mismatched lengths
def __init__(self, values: Sequence[float], labels: Sequence[str]): ...

# Good: structurally impossible to mismatch
type DataPoint = Annotated[tuple[str, float], "label, value"]
def __init__(self, data: Sequence[DataPoint]): ...
```

Make illegal states unrepresentable.

## `or` vs `is None`

```python
# Bug: empty list [] is falsy, gets silently replaced
self.labels = labels or default_labels

# Correct: only replaces None
self.labels = default_labels if labels is None else labels
```

## Annotated for semantic types

When a type alias is opaque (e.g., `tuple[str, float]` — which is label, which is value?), use `Annotated`:

```python
type DataPoint = Annotated[tuple[str, float], "label, value"]
```

Type checkers see `tuple[str, float]`, humans see the semantics. Tools like Pydantic can also consume the metadata.
