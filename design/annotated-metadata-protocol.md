---
summary: Design extensible frameworks using Annotated metadata, duck-typed protocols, and ExceptionGroup
tags: [python, annotated, protocol, type-hints, framework-design]
date: 2026-02-28
---

# Annotated Metadata Protocol Pattern

## The pattern

Use `Annotated[T, metadata...]` to attach framework-consumable metadata to type hints. Each metadata object implements a protocol (e.g., `_validate_`) that the framework discovers at runtime.

```python
type Price = Annotated[float, Gt(0)]

class Product:
    price: Price
```

## Key design decisions

### 1. Protocol with prefix naming

Use `_validate_` not `check` — prefixed naming avoids collisions with unrelated methods, following IPython's `_repr_html_` convention.

### 2. Explicit Protocol over hasattr

```python
@runtime_checkable
class Constraint(Protocol):
    def _validate_(self, name: str, value) -> None: ...

# Good: isinstance(meta, Constraint)
# Bad:  hasattr(meta, "_validate_")
```

`isinstance` with Protocol lets type checkers verify implementations. `hasattr` only checks name existence at runtime.

### 3. TypeAliasType needs unwrapping

Python 3.12+ `type` statements create lazy `TypeAliasType`. `get_type_hints()` returns the alias, not the resolved `Annotated`. Must unwrap via `__value__`:

```python
def unwrap_type(hint):
    while isinstance(hint, TypeAliasType):
        hint = hint.__value__
    return hint
```

Without this, validation silently skips aliased fields — the most dangerous kind of bug.

### 4. ExceptionGroup for collecting errors

Don't fail on the first error. Collect all violations and raise as `ExceptionGroup`:

```python
if errors:
    raise ExceptionGroup("validation failed", errors)
```

Callers use `except*` to handle. Same pattern as Pydantic's `ValidationError`.

### 5. Composability

Multiple frameworks read the same `Annotated` metadata, each taking only what it recognizes:

```python
class Order:
    id: Annotated[int, PrimaryKey(), Description("Unique order ID")]
```

ORM reads `PrimaryKey()`, API docs read `Description()`, validator reads constraints. They coexist without interference.

## Connections

- IPython `_repr_html_` — same duck-typed protocol pattern
- Postel's Law — liberal in what metadata you ignore, strict in what you produce
- Chokepoint architecture — `__metadata__` tuple is the universal carrier, like IPython's MIME dict
