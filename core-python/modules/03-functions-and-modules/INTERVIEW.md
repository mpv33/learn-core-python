# Module 03 — Interview Prep: Functions & Modules

> Functions, *args/**kwargs, closures, recursion, imports, packages

---

## Theory Questions

**Q1: What is LEGB rule?**  
Name lookup order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

**Q2: Mutable default argument trap?**  
Default values evaluated once at function definition. Mutable default (`=[]`) shared across calls. Fix: use `None` and create inside function.

**Q3: What is a closure?**  
Inner function that remembers variables from enclosing scope even after outer function returns.

**Q4: `*args` vs `**kwargs`?**  
`*args`: tuple of extra positional args. `**kwargs`: dict of extra keyword args.

**Q5: First-class functions?**  
Functions are objects — can be passed as arguments, returned, stored in variables.

**Q6: `return` vs no return?**  
Function without return (or bare `return`) returns `None`.

**Q7: What is recursion?**  
Function calling itself. Must have base case to avoid infinite recursion / RecursionError.

**Q8: Lambda limitations?**  
Single expression only. No statements. Use `def` for complex logic.

**Q9: `if __name__ == "__main__"`?**  
Runs block only when file executed directly, not imported.

**Q10: Module vs package?**  
Module: single `.py` file. Package: directory with `__init__.py` containing submodules.

**Q11: Absolute vs relative import?**  
Absolute: `from mypackage.utils import helper`. Relative: `from .utils import helper` (within package).

**Q12: Circular import problem?**  
Two modules import each other. Fix: restructure, lazy import inside function, or use importlib.

**Q13: What does `@wraps` do?**  
Preserves original function's `__name__`, `__doc__` when decorating.

**Q14: Difference between function and method?**  
Method is function bound to an object/class. First param is `self` or `cls`.

**Q15: What is `nonlocal`?**  
Modifies variable in nearest enclosing scope (not global).

**Q16: What is `global` keyword?**  
Declares intent to modify module-level variable inside function.

**Q17: Can functions be attributes of dict/list?**  
Yes. Functions are objects.

**Q18: What is `__all__` in package?**  
List of names exported by `from package import *`.

---

## Coding Questions

**Q19: Decorator skeleton**
```python
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```

**Q20: Memoized Fibonacci**
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

**Q21: Flatten nested list (recursive)**
```python
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

**Q22: Retry decorator**
```python
def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1: raise
        return wrapper
    return decorator
```

**Q23: Curry function**
```python
def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more: curried(*(args + more))
    return curried
```

**Q24: Count function calls (closure)**
```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

**Q25: Safe divide**
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None
```

---

## Common Pitfalls

- Mutable default arguments
- Forgetting `@wraps` in decorators
- Circular imports
- Using wildcard import `from x import *`
- Unbounded recursion without base case

---

## Quick Checklist

- [ ] Explain LEGB with example
- [ ] Explain mutable default arg trap
- [ ] Write a simple decorator from memory
- [ ] Explain closure with example
- [ ] Describe module vs package
