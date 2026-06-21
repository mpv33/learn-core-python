# Exceptions

```bash
python3 09-exceptions/01_try_except.py
```

## Examples

- `01_try_except.py`
- `02_multiple_exceptions.py`
- `03_raise_custom.py`
- `04_finally_else.py`
- `05_logging.py`

→ [10-iterators](../10-iterators/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [10_Iterators Generators Comprehensions](../10_iterators_generators_comprehensions/)


---

## Interview Prep

### Must-Know Concepts

- try/except/else/finally
- exception hierarchy
- raise from
- logging levels

### Theory Questions

**Q1: Exception hierarchy?**  
A: BaseException → Exception → (ValueError, TypeError, etc.). Catch specific exceptions.

**Q2: else in try block?**  
A: Runs if no exception. finally always runs.

**Q3: logging vs print?**  
A: logging: levels, handlers, production-ready.

### Coding Questions


### Common Pitfalls

- Bare except
- Swallowing exceptions silently
- Using print in production

