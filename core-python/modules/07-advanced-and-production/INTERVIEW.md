# Module 07 — Interview Prep: Advanced & Production

> Testing, concurrency, internals, performance, best practices

---

## Theory Questions

**Q1: What is GIL?**  
Global Interpreter Lock — only one thread executes Python bytecode at a time. Limits CPU parallelism in threads.

**Q2: Thread vs process vs asyncio?**  
Thread: shared memory, good for I/O. Process: separate memory, true CPU parallelism. asyncio: single-threaded event loop for concurrent I/O.

**Q3: When to use threading?**  
I/O-bound tasks: network, disk, API calls.

**Q4: When to use multiprocessing?**  
CPU-bound tasks: computation, data processing.

**Q5: When to use asyncio?**  
Many concurrent I/O operations: web servers, async APIs.

**Q6: Unit vs integration test?**  
Unit: isolated function/class. Integration: multiple components together.

**Q7: Mock purpose in testing?**  
Replace real dependencies (DB, API) with controlled fakes for isolated testing.

**Q8: pytest vs unittest?**  
pytest: simpler assert, fixtures, parametrize. unittest: built-in, class-based.

**Q9: What is `@dataclass`?**  
Auto-generates `__init__`, `__repr__`, `__eq__`. Reduces boilerplate.

**Q10: Descriptor protocol?**  
Object with `__get__`, `__set__`, `__delete__`. Powers `@property`.

**Q11: Metaclass?**  
Class of a class. `type` is default. Controls class creation. Rare — used in frameworks.

**Q12: `__slots__` purpose?**  
Restrict attributes, save memory (~40-50%), no `__dict__`. Trade flexibility for efficiency.

**Q13: How Python manages memory?**  
Reference counting + cyclic garbage collector for circular references.

**Q14: Profile before optimize?**  
Always. Use cProfile/timeit. Fix algorithm first, micro-optimize last.

**Q15: Design patterns in Python?**  
Strategy, Factory, Singleton, Observer, Repository. Python favors simplicity over heavy patterns.

**Q16: SOLID principles?**  
Single responsibility, Open/closed, Liskov substitution, Interface segregation, Dependency inversion.

**Q17: Race condition?**  
Two threads access shared data concurrently, outcome depends on timing. Fix with Lock.

**Q18: `async def` vs regular def?**  
async def returns coroutine. Must be awaited. Cannot call blocking I/O without blocking event loop.

**Q19: `await` keyword?**  
Pauses coroutine until awaited task completes. Non-blocking.

**Q20: What is `pdb`?**  
Python debugger. `breakpoint()` or `python -m pdb script.py`.

**Q21: Test-driven development (TDD)?**  
Red (write failing test) → Green (make it pass) → Refactor.

**Q22: PEP 8 naming?**  
snake_case functions/vars, PascalCase classes, UPPER_SNAKE constants.

**Q23: Dependency injection?**  
Pass dependencies into class/function instead of creating inside. Improves testability.

**Q24: What is `__init__.py` for?**  
Marks directory as package. Can control exports via `__all__`.

**Q25: Production logging best practice?**  
Use logging module, structured format, RotatingFileHandler, appropriate levels.

---

## Coding Questions

**Q26: Thread-safe counter**
```python
import threading
class SafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    def increment(self):
        with self._lock:
            self._value += 1
    @property
    def value(self):
        return self._value
```

**Q27: Async fetch multiple URLs (pattern)**
```python
import asyncio
async def fetch_all(urls):
    async def fetch(url):
        await asyncio.sleep(0.1)  # simulate I/O
        return f"data from {url}"
    return await asyncio.gather(*[fetch(u) for u in urls])
```

**Q28: pytest test example**
```python
def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def test_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
```

**Q29: Mock external API**
```python
from unittest.mock import Mock, patch
def test_api_call():
    mock_resp = Mock()
    mock_resp.json.return_value = {"status": "ok"}
    with patch("requests.get", return_value=mock_resp):
        result = fetch_data()
        assert result["status"] == "ok"
```

**Q30: Dataclass with validation**
```python
from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
```

**Q31: Singleton (module-level — Pythonic)**
```python
# config.py
class _Config:
    debug = False
config = _Config()  # import config everywhere
```

**Q32: Strategy pattern**
```python
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): pass
class CreditCard(Payment):
    def pay(self, amount): return f"Charged ${amount}"
class PayPal(Payment):
    def pay(self, amount): return f"Paid ${amount} via PayPal"
```

**Q33: timeit benchmark**
```python
import timeit
t1 = timeit.timeit("[x**2 for x in range(1000)]", number=10000)
t2 = timeit.timeit("(x**2 for x in range(1000))", number=10000)
print(f"list: {t1:.4f}s, gen: {t2:.4f}s")
```

**Q34: Implement LRU cache manually (concept)**
```python
from functools import lru_cache
@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

---

## System Design (Python-Specific)

**Q35: How would you process a 10GB file?**  
Read line-by-line with generator. Never load entire file into memory. Process in chunks.

**Q36: How to make Python code faster?**  
Better algorithm → right data structure → generators → built-ins/C extensions → multiprocessing for CPU-bound.

**Q37: How to handle 1000 concurrent API calls?**  
asyncio with aiohttp, or thread pool for sync libraries, with rate limiting and connection pooling.

**Q38: How to structure a Python project?**  
src layout, tests/, requirements.txt or pyproject.toml, .gitignore, README, type hints, CI with pytest.

---

## Common Pitfalls

- Using threads for CPU-bound work (GIL)
- Blocking calls inside async code
- Not using locks for shared mutable state
- Testing implementation instead of behavior
- Overusing metaclasses and complex patterns
- Optimizing without profiling

---

## Quick Checklist

- [ ] Explain GIL and its impact
- [ ] Choose thread vs process vs asyncio for scenario
- [ ] Write pytest test from memory
- [ ] Explain mock/patch purpose
- [ ] Describe dataclass vs regular class
- [ ] Explain __slots__ trade-offs
- [ ] List 3 design patterns with examples
