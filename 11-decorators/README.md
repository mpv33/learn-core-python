# Decorators

```bash
python3 11-decorators/01_decorators.py
```

## Examples

- `01_decorators.py`
- `02_decorator_patterns.py`
- `03_context_managers.py`
- `04_property_classmethod.py`

→ [12-types](../12-types/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [12_Type Hints](../12_type_hints/)


---

## Interview Prep

### Must-Know Concepts

- decorator pattern
- functools.wraps
- property
- enter/exit protocol
- contextlib

### Theory Questions

**Q1: What is a decorator?**  
A: Function extending another function's behavior without modifying it.

**Q2: property purpose?**  
A: Computed attribute with getter/setter. Pythonic encapsulation.

**Q3: Context manager protocol?**  
A: __enter__ for setup, __exit__ for cleanup.

### Coding Questions


### Common Pitfalls

- Forgetting wraps
- Decorator order (bottom applied first)

