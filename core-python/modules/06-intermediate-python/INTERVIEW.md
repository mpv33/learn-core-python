# Module 06 — Interview Prep: Intermediate Python

> Comprehensions, generators, decorators, type hints, stdlib, functional

---

## Theory Questions

**Q1: List comprehension vs generator expression?**  
`[x for x in r]`: eager list. `(x for x in r)`: lazy generator, O(1) memory.

**Q2: Generator vs iterator vs iterable?**  
Iterable: has `__iter__()`. Iterator: has `__next__()`. Generator: iterator from function with `yield`.

**Q3: `yield` vs `return`?**  
yield pauses function preserving state. return ends function. yield makes a generator.

**Q4: What is a decorator?**  
Function taking another function, extending behavior. Syntactic sugar: `@deco` above `def`.

**Q5: Decorator with arguments?**  
Requires extra wrapper level: `def deco(arg): def wrapper(func): ... return wrapper`.

**Q6: Context manager protocol?**  
`__enter__` for setup, `__exit__` for cleanup. Used by `with` statement.

**Q7: `@property` purpose?**  
Computed attribute with optional getter/setter/deleter. Pythonic encapsulation.

**Q8: Are type hints enforced at runtime?**  
No. Used by mypy/pyright for static analysis. Optional documentation.

**Q9: `Optional[str]` vs `str | None`?**  
Same meaning. `str | None` is Python 3.10+ syntax.

**Q10: What is Protocol?**  
Structural subtyping — duck typing with type checker support.

**Q11: `TypedDict`?**  
Dict with fixed key types. For structured dict data.

**Q12: `Counter` use case?**  
Frequency counting. `most_common(n)`.

**Q13: `defaultdict` vs `dict.get()`?**  
defaultdict auto-creates missing keys. Cleaner grouping/accumulation code.

**Q14: `deque` vs list?**  
deque: O(1) both-end operations. Use for queues/BFS.

**Q15: `itertools.groupby` caveat?**  
Requires sorted input for correct grouping.

**Q16: `functools.lru_cache`?**  
Memoization decorator. Caches function results by arguments.

**Q17: `map` vs list comprehension?**  
List comp more Pythonic and readable. map useful with existing named functions.

**Q18: `partial` function?**  
Fixes some arguments of a function, returns new callable.

**Q19: `@classmethod` factory pattern?**  
Alternative constructor: `Date.from_string("2026-01-01")`.

**Q20: Generator one-shot nature?**  
Once exhausted, cannot replay. Create new generator to iterate again.

---

## Coding Questions

**Q21: Fibonacci generator**
```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

**Q22: Timer decorator**
```python
from functools import wraps
import time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter()-start:.4f}s")
        return result
    return wrapper
```

**Q23: Context manager with @contextmanager**
```python
from contextlib import contextmanager
@contextmanager
def temp_attr(obj, attr, value):
    old = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield obj
    finally:
        setattr(obj, attr, old)
```

**Q24: Read large file lazily**
```python
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()
```

**Q25: Flatten with generator**
```python
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

**Q26: Group by key**
```python
from itertools import groupby
def group_by(items, key):
    items = sorted(items, key=key)
    return {k: list(g) for k, g in groupby(items, key=key)}
```

**Q27: Type-hinted function**
```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

**Q28: LRU cache usage**
```python
from functools import lru_cache
@lru_cache(maxsize=128)
def expensive(n: int) -> int:
    return sum(i*i for i in range(n))
```

---

## Common Pitfalls

- Exhausting generator twice
- Forgetting `@wraps` in decorators
- Decorator order (bottom applied first)
- Using `Any` everywhere in type hints
- Nested list comprehensions hurting readability

---

## Quick Checklist

- [ ] Write decorator from memory
- [ ] Explain generator vs list comp
- [ ] Explain context manager protocol
- [ ] Use Counter and defaultdict
- [ ] Explain lru_cache purpose
