# Interview Guide

Master reference after completing modules 00–19. Each module README also has topic-specific Q&A.

## Top Questions

1. `==` vs `is`?
2. Mutable vs immutable types?
3. List vs tuple vs set vs dict?
4. What is GIL?
5. Thread vs process vs asyncio?
6. Generator vs iterator?
7. Decorator — how does it work?
8. Mutable default argument trap?
9. Shallow vs deep copy?
10. LEGB rule?

## Coding Patterns

```python
# Two Sum
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

# Palindrome
def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Timer decorator
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

## Module Index

| Module | Guide |
|--------|-------|
| 00 Setup | [00-setup](../00-setup/README.md) |
| 01 Fundamentals | [01-fundamentals](../01-fundamentals/README.md) |
| 02 Control Flow | [02-control-flow](../02-control-flow/README.md) |
| 03 Data Structures | [03-data-structures](../03-data-structures/README.md) |
| 04 Functions | [04-functions](../04-functions/README.md) |
| 05 OOP | [05-oop](../05-oop/README.md) |
| 06 Modules | [06-modules](../06-modules/README.md) |
| 07 Strings | [07-strings](../07-strings/README.md) |
| 08 Files | [08-files](../08-files/README.md) |
| 09 Exceptions | [09-exceptions](../09-exceptions/README.md) |
| 10 Iterators | [10-iterators](../10-iterators/README.md) |
| 11 Decorators | [11-decorators](../11-decorators/README.md) |
| 12 Types | [12-types](../12-types/README.md) |
| 13 Stdlib | [13-stdlib](../13-stdlib/README.md) |
| 14 Functional | [14-functional](../14-functional/README.md) |
| 15 Testing | [15-testing](../15-testing/README.md) |
| 16 Concurrency | [16-concurrency](../16-concurrency/README.md) |
| 17 Advanced | [17-advanced](../17-advanced/README.md) |
| 18 Performance | [18-performance](../18-performance/README.md) |
| 19 Best Practices | [19-best-practices](../19-best-practices/README.md) |

## Study Plan

| Weeks | Modules |
|-------|---------|
| 1–2 | 00–04 |
| 3–4 | 05–09 |
| 5–6 | 10–14 |
| 7–8 | 15–19 + review |
