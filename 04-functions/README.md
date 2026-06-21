# Functions

```bash
python3 04-functions/01_basic_functions.py
```

## Examples

- `01_basic_functions.py`
- `02_args_kwargs.py`
- `03_lambda.py`
- `04_scope_closures.py`
- `05_recursion.py`

→ [05-oop](../05-oop/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [05_Object Oriented Programming](../05_object_oriented_programming/)


---

## Interview Prep

### Must-Know Concepts

- *args/**kwargs
- closures
- LEGB scope
- recursion
- first-class functions
- mutable default args

### Theory Questions

**Q1: What is LEGB?**  
A: Local → Enclosing → Global → Built-in. Python name resolution order.

**Q2: Mutable default argument trap?**  
A: Defaults evaluated once at def time. Use None instead of mutable defaults.

**Q3: Closure?**  
A: Inner function remembering variables from enclosing scope after outer returns.

**Q4: Difference *args vs **kwargs?**  
A: *args: tuple of positional extras. **kwargs: dict of keyword extras.

### Coding Questions

**Decorator skeleton**
```python
from functools import wraps
def deco(func):
    @wraps(func)
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper
```

### Common Pitfalls

- Mutable default args
- Forgetting @wraps in decorators
- Unbounded recursion → RecursionError

