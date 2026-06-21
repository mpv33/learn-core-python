# Type Hints

```bash
python3 12-types/01_basic_types.py
```

## Examples

- `01_basic_types.py`
- `02_advanced_types.py`
- `03_typed_classes.py`

→ [13-stdlib](../13-stdlib/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [13_Standard Library](../13_standard_library/)


---

## Interview Prep

### Must-Know Concepts

- annotations
- Optional
- Union
- Protocol
- TypedDict
- mypy

### Theory Questions

**Q1: Are type hints enforced at runtime?**  
A: No. Used by static analyzers like mypy.

**Q2: Optional[str] vs str | None?**  
A: Same meaning. str | None is Python 3.10+ syntax.

**Q3: Protocol?**  
A: Structural subtyping — duck typing with type checker support.

### Coding Questions


### Common Pitfalls

- Using Any everywhere
- Forward references need quotes or future annotations

