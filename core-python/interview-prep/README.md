# Python Interview Master Guide

Complete module-wise interview preparation for core Python roles.

---

## Module Index

| Module | File | Questions |
|--------|------|-----------|
| 01 Fundamentals | [INTERVIEW.md](../modules/01-fundamentals/INTERVIEW.md) | 28+ |
| 02 Data Structures | [INTERVIEW.md](../modules/02-data-structures/INTERVIEW.md) | 25+ |
| 03 Functions & Modules | [INTERVIEW.md](../modules/03-functions-and-modules/INTERVIEW.md) | 25+ |
| 04 OOP | [INTERVIEW.md](../modules/04-object-oriented-programming/INTERVIEW.md) | 24+ |
| 05 Data Handling | [INTERVIEW.md](../modules/05-data-handling/INTERVIEW.md) | 27+ |
| 06 Intermediate | [INTERVIEW.md](../modules/06-intermediate-python/INTERVIEW.md) | 28+ |
| 07 Advanced & Production | [INTERVIEW.md](../modules/07-advanced-and-production/INTERVIEW.md) | 38+ |

**Total: 195+ questions with answers and code**

---

## Top 30 Most Asked Python Interview Questions (Detailed Answers)

---

### Q1: What is the difference between `==` and `is`?

**Short answer:** `==` checks value equality. `is` checks whether two variables point to the **same object in memory**.

**Detailed explanation:**

Python compares objects in two ways:
1. **Value comparison (`==`)** — calls `__eq__()` method. Two objects with same content return True.
2. **Identity comparison (`is`)** — compares memory addresses using `id()`. Same object → True.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — same values
print(a is b)   # False — different list objects in memory
print(a is c)   # True  — c references the same object as a
print(id(a), id(b), id(c))  # id(a) == id(c), id(b) is different
```

**When to use `is`:**
- Comparing with `None`: `if x is None` (never `x == None`)
- Comparing singletons: `True`, `False`

**Integer caching trap (common follow-up):**
```python
x = 256; y = 256
print(x is y)  # True — Python caches integers -5 to 256

x = 257; y = 257
print(x is y)  # False — may differ (implementation dependent)
```

**Interview tip:** Never use `is` for string or list comparison. Always use `==` for values.

---

### Q2: What are mutable vs immutable types?

**Short answer:** Mutable objects can be changed after creation. Immutable objects cannot.

**Detailed explanation:**

| Mutable | Immutable |
|---------|-----------|
| `list` | `int`, `float`, `bool` |
| `dict` | `str` |
| `set` | `tuple` |
| `bytearray` | `frozenset`, `bytes` |
| custom objects | `None` |

```python
# Mutable — change in place
nums = [1, 2, 3]
nums.append(4)        # [1, 2, 3, 4] — same object

# Immutable — creates new object
s = "hello"
s.upper()             # returns "HELLO" — s is still "hello"
# s[0] = "H"          # TypeError: str does not support item assignment
```

**Why it matters:**
- **Hashability:** Immutable types (if all elements hashable) can be dict keys and set elements. Lists cannot.
- **Function defaults:** Mutable defaults are shared (see Q10).
- **Thread safety:** Immutable objects are inherently thread-safe for reads.
- **Memory:** Immutable objects may be interned/cached (small ints, strings).

**Follow-up:** `tuple` is immutable but can contain mutable objects:
```python
t = ([1, 2], 3)
t[0].append(99)   # works — mutating inner list
# t[0] = [4, 5]   # TypeError — cannot reassign tuple element
```

---

### Q3: List all falsy values in Python.

**Short answer:** Values that evaluate to `False` in boolean context.

**Complete list:**
```python
falsy_values = [
    None,
    False,
    0,          # int zero
    0.0,        # float zero
    0j,         # complex zero
    "",         # empty string
    [],         # empty list
    {},         # empty dict
    set(),      # empty set
    (),         # empty tuple
    range(0),   # empty range
    bytes(),    # empty bytes
]

for v in falsy_values:
    print(f"{repr(v):12} → {bool(v)}")  # all print False
```

**Custom falsy objects:**
```python
class Empty:
    def __bool__(self):
        return False

class ZeroLen:
    def __len__(self):
        return 0

bool(Empty())   # False — __bool__ takes priority
bool(ZeroLen()) # False — __len__ used if no __bool__
```

**Short-circuit evaluation:**
```python
result = expensive() and do_something()  # do_something() skipped if expensive() is falsy
user = get_user() or default_user          # default used if get_user() is falsy
```

**Interview tip:** Everything not in the falsy list is **truthy**, including `"0"`, `"False"`, `[0]`, `[False]`.

---

### Q4: Is Python interpreted or compiled?

**Short answer:** Both — Python compiles to bytecode, then interprets bytecode at runtime.

**Detailed explanation:**

Python execution pipeline:
```
Source (.py) → Compiler → Bytecode (.pyc) → Python Virtual Machine (PVM) → Output
```

1. **Compilation:** `.py` file compiled to bytecode stored in `__pycache__/` as `.pyc` files.
2. **Interpretation:** PVM executes bytecode line by line at runtime.

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
# Shows bytecode instructions: LOAD_FAST, BINARY_ADD, RETURN_VALUE
```

**Why called "interpreted":**
- No ahead-of-time compilation to machine code (unlike C/C++).
- Bytecode runs through interpreter loop, not CPU directly.

**CPython vs others:**
- **CPython** — standard, has GIL, most common.
- **PyPy** — JIT compiler, faster for long-running programs.
- **Cython** — compiles to C extensions.

**Follow-up:** `.pyc` files speed up startup by skipping recompilation if source unchanged.

---

### Q5: List vs tuple vs set vs dict — when to use each?

**Detailed comparison:**

| Feature | list | tuple | set | dict |
|---------|------|-------|-----|------|
| Ordered | Yes | Yes | No* | Yes (3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Indexed | Yes `[0]` | Yes | No | By key |
| Lookup | O(n) | O(n) | O(1) avg | O(1) avg |
| Hashable | No | Yes* | No | No |

*Set iteration order is arbitrary. Tuple hashable if all elements hashable.

**When to use each:**

```python
# LIST — ordered collection, allow duplicates, need to modify
shopping = ["apple", "banana", "apple"]
shopping.append("cherry")

# TUPLE — fixed data, return multiple values, dict keys
point = (10, 20)
person = ("Alice", 30, "Engineer")
locations = {(0, 0): "origin", (1, 2): "point A"}

# SET — unique items, membership testing, set math
unique_ids = {101, 102, 103, 101}  # {101, 102, 103}
if user_id in valid_ids:             # O(1) lookup
    grant_access()

# DICT — key-value mapping, fast lookup by key
user = {"name": "Alice", "age": 30, "role": "admin"}
print(user["name"])  # O(1) lookup
```

**Real-world examples:**
- **list** — queue of tasks, list of records from API
- **tuple** — database row, coordinates, function return values
- **set** — remove duplicates, find common elements between lists
- **dict** — JSON data, configuration, counting with keys

---

### Q6: Shallow copy vs deep copy?

**Short answer:** Shallow copy duplicates the container only. Deep copy duplicates everything recursively.

**Detailed explanation:**

```python
import copy

original = {
    "name": "Alice",
    "scores": [90, 85, 88],
    "meta": {"active": True}
}

# Assignment — NOT a copy (same reference)
assigned = original

# Shallow copy — new outer dict, shared inner objects
shallow = original.copy()          # or copy.copy(original)
shallow["scores"].append(100)
print(original["scores"])          # [90, 85, 88, 100] — AFFECTED!

# Deep copy — fully independent
original["scores"] = [90, 85, 88]  # reset
deep = copy.deepcopy(original)
deep["scores"].append(100)
print(original["scores"])          # [90, 85, 88] — NOT affected
deep["meta"]["active"] = False
print(original["meta"]["active"])  # True — NOT affected
```

**Visual:**
```
Original:  dict → [scores list] → [90, 85, 88]
Shallow:   dict → [same scores list] → [90, 85, 88, 100]
Deep:      dict → [new scores list] → [90, 85, 88, 100]
```

**When to use:**
- **Shallow:** Flat structures, no nested mutable objects.
- **Deep:** Nested lists/dicts where full independence needed.

**Interview trap:**
```python
matrix = [[0]*3]*3   # BAD — all rows reference same list!
matrix[0][0] = 1     # changes ALL rows
# Correct: [[0]*3 for _ in range(3)]
```

---

### Q7: Two Sum — find two indices that add to target.

**Problem:** Given `[2, 7, 11, 15]` and target `9`, return `[0, 1]` because `2 + 7 = 9`.

**Brute force — O(n²):**
```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

**Optimal — O(n) time, O(n) space:**
```python
def two_sum(nums, target):
    seen = {}  # value → index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []  # no solution

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
```

**Walkthrough for `[2, 7, 11, 15]`, target=9:**
```
i=0, n=2: complement=7, not in seen → seen={2:0}
i=1, n=7: complement=2, in seen at index 0 → return [0, 1]
```

**Follow-ups interviewers ask:**
- What if no solution exists? Return `[]` or raise exception.
- What if duplicate values? Hash map stores latest index — still works.
- What if sorted array? Use two-pointer approach O(n) with O(1) space.

---

### Q8: Big-O time complexity of list, dict, set operations?

**List operations:**
| Operation | Time | Example |
|-----------|------|---------|
| Access by index | O(1) | `lst[5]` |
| Append | O(1) amortized | `lst.append(x)` |
| Insert at index | O(n) | `lst.insert(0, x)` |
| Delete by index | O(n) | `del lst[0]` |
| Search (in) | O(n) | `x in lst` |
| Sort | O(n log n) | `lst.sort()` |

**Dict / Set operations:**
| Operation | Average | Worst Case |
|-----------|---------|------------|
| Lookup | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case O(n) happens with many hash collisions (rare in practice).

```python
# O(1) — use set for membership
VALID = {"E001", "E002", "E003"}
if emp_id in VALID:   # fast even with millions of IDs
    process()

# O(n) — list membership is slow for large lists
if emp_id in big_list:  # scans entire list
    process()
```

**Interview tip:** Always mention average vs worst case for hash-based structures.

---

### Q9: What is the LEGB rule?

**Short answer:** Python's order for looking up variable names: Local → Enclosing → Global → Built-in.

**Detailed explanation:**

```python
x = "global"          # G — Global

def outer():
    x = "enclosing"   # E — Enclosing scope for inner()

    def inner():
        x = "local"   # L — Local
        print(x)      # "local" — L found first

    inner()
    print(x)          # "enclosing"

outer()
print(x)              # "global"
```

**Modifying scopes:**
```python
count = 0

def increment():
    global count      # must declare to MODIFY global
    count += 1

def outer():
    total = 10
    def inner():
        nonlocal total  # modify enclosing scope variable
        total += 5
    inner()
    return total  # 15
```

**Built-in scope example:**
```python
print(len([1, 2, 3]))  # B — built-in len()

def demo():
    len = "shadow"     # L — shadows built-in len
    print(len)         # "shadow"
```

**Interview follow-up:** What happens if variable not found in any scope? → `NameError`.

---

### Q10: What is the mutable default argument trap?

**Short answer:** Default arguments are evaluated **once** when the function is defined, not on each call.

**The bug:**
```python
def add_item(item, lst=[]):   # [] created ONCE at definition time
    lst.append(item)
    return lst

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b']  ← SURPRISE! Same list!
print(add_item("c"))  # ['a', 'b', 'c']
```

**Why it happens:**
```python
# Equivalent to:
_default_list = []
def add_item(item, lst=_default_list):
    lst.append(item)
    return lst
# Every call without lst uses the SAME _default_list object
```

**Correct pattern:**
```python
def add_item(item, lst=None):
    if lst is None:
        lst = []          # new list created on each call
    lst.append(item)
    return lst

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b']  ← correct!
```

**Same trap with dict/set defaults:**
```python
# BAD
def configure(opts={}):
    opts["debug"] = True
    return opts

# GOOD
def configure(opts=None):
    if opts is None:
        opts = {}
    opts["debug"] = True
    return opts
```

---

### Q11: What is a closure?

**Short answer:** A function that captures and remembers variables from its enclosing scope, even after the outer function has finished.

**Detailed explanation:**

```python
def make_multiplier(factor):
    # factor is "enclosed" in the closure
    def multiply(number):
        return number * factor  # uses factor from enclosing scope
    return multiply

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50
# Each closure has its own captured `factor` value
```

**How closures work internally:**
```python
print(times3.__closure__)                    # tuple of cell objects
print(times3.__closure__[0].cell_contents)   # 3
```

**Practical uses:**
1. **Data encapsulation (private state):**
```python
def make_counter(start=0):
    count = start
    def increment(step=1):
        nonlocal count
        count += step
        return count
    return increment

counter = make_counter(10)
print(counter())    # 11
print(counter(5))   # 16
```

2. **Decorators** — closures capture the wrapped function.
3. **Callbacks** — factory functions for event handlers.

**Interview follow-up:** Difference between closure and class? Closures are lighter for simple state; classes better for complex behavior.

---

### Q12: How do decorators work?

**Short answer:** A decorator is a function that takes another function and extends its behavior without modifying the original.

**Step by step:**

```python
from functools import wraps

# Step 1: Decorator is a function that accepts a function
def log_calls(func):
    @wraps(func)  # preserves func.__name__ and __doc__
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)  # call original
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Step 2: @ syntax applies decorator
@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

# @log_calls is equivalent to:
# add = log_calls(add)

print(add(3, 5))
# Calling add with (3, 5)
# add returned 8
# 8

print(add.__name__)  # "add" (thanks to @wraps)
```

**Decorator with arguments:**
```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # prints 3 times
```

**Stacking decorators (applied bottom-up):**
```python
@decorator_a
@decorator_b
def func():
    pass
# Equivalent to: func = decorator_a(decorator_b(func))
```

**Real-world uses:** `@app.route`, `@login_required`, `@lru_cache`, `@property`, timing, logging, retry logic.

---

### Q13: What are the four pillars of OOP?

**1. Encapsulation** — Bundle data and methods together; hide internal details.
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "private" by convention

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
# Cannot do account._balance = 999999 without bypassing validation
```

**2. Abstraction** — Show only essential features, hide complexity.
```python
# User doesn't need to know HOW email sends
email_service.send("user@example.com", "Hello")
# Internal SMTP, TLS, retry logic hidden
```

**3. Inheritance** — Child class inherits parent's attributes and methods.
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

**4. Polymorphism** — Same interface, different behavior.
```python
def animal_sound(animal):
    print(animal.speak())  # works for Dog, Cat, any Animal

animal_sound(Dog())  # Woof!
animal_sound(Cat())  # Meow!
```

**Python-specific:** Also supports **duck typing** — "if it walks like a duck and quacks like a duck, it's a duck" — no inheritance required.

---

### Q14: What is MRO (Method Resolution Order)?

**Short answer:** The order Python searches for methods in a class hierarchy with multiple inheritance.

**Detailed explanation:**

Python uses **C3 linearization** algorithm for MRO.

```python
class A:
    def greet(self): return "A"

class B(A):
    def greet(self): return "B"

class C(A):
    def greet(self): return "C"

class D(B, C):
    pass

d = D()
print(d.greet())   # "B" — first in MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

**Diamond problem:**
```
    A
   / \
  B   C
   \ /
    D
```
MRO for D: `D → B → C → A → object` — each class appears once, parents before children.

**Using super() with MRO:**
```python
class B(A):
    def __init__(self):
        super().__init__()  # calls C.__init__ next (not A directly!)
        print("B init")

class C(A):
    def __init__(self):
        super().__init__()
        print("C init")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")

D()  # Output: A init, C init, B init, D init
```

**Interview tip:** Always use `super()` instead of hardcoding parent class names.

---

### Q15: `@classmethod` vs `@staticmethod` vs `@property`?

**Detailed comparison:**

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # INSTANCE METHOD — receives self (the instance)
    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    # CLASS METHOD — receives cls (the class), used as factory
    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)  # creates instance

    # STATIC METHOD — no self or cls, utility in class namespace
    @staticmethod
    def is_valid(year, month, day):
        return 1 <= month <= 12 and 1 <= day <= 31

    # PROPERTY — computed attribute with getter/setter
    @property
    def is_leap_year(self):
        y = self.year
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

# Usage
d1 = Date(2026, 6, 21)
d2 = Date.from_string("2026-06-21")   # classmethod factory
print(Date.is_valid(2026, 6, 21))     # staticmethod
print(d1.is_leap_year)                # property (no parentheses)
```

| Type | First arg | Use case |
|------|-----------|----------|
| Instance method | `self` | Operate on instance data |
| `@classmethod` | `cls` | Alternative constructors, class-level ops |
| `@staticmethod` | none | Utility function grouped with class |
| `@property` | none | Computed/validated attributes |

---

### Q16: Composition vs inheritance?

**Inheritance ("is-a")** — child IS a type of parent.
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):  # Manager IS an Employee
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
```

**Composition ("has-a")** — object CONTAINS another object.
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def start(self):
        return self.engine.start()
```

**Why prefer composition:**
- **Flexibility:** Change engine without changing Car hierarchy.
- **Loose coupling:** Engine can be reused in Truck, Boat.
- **Avoid deep hierarchies:** `FlyingSwimmingAnimal` problems.

**Real-world example:**
```python
# BAD — deep inheritance
class AuthUser(AdminUser(PremiumUser(BaseUser))): pass

# GOOD — composition
class User:
    def __init__(self):
        self.auth = AuthService()
        self.billing = BillingService()
        self.permissions = PermissionManager()
```

**Interview answer:** "Favor composition over inheritance unless a clear is-a relationship exists."

---

### Q17: Are strings mutable in Python?

**Short answer:** No. Strings are immutable in Python.

**Detailed explanation:**

```python
s = "hello"
print(id(s))       # memory address 1
s = s + " world"   # creates NEW string object
print(id(s))       # memory address 2 — different object!

# Cannot modify in place:
# s[0] = "H"       # TypeError
# s.append("!")    # AttributeError
```

**All string methods return NEW strings:**
```python
s = "  Hello World  "
print(s.strip())    # "Hello World" — s unchanged
print(s.lower())    # "  hello world  " — s unchanged
print(s)            # "  Hello World  "
```

**Performance implication:**
```python
# BAD — O(n²) — creates new string each iteration
result = ""
for word in words:
    result += word

# GOOD — O(n) — join once
result = "".join(words)
```

**String interning:**
```python
a = "hello"
b = "hello"
print(a is b)  # True — Python may intern small/common strings
```

**bytes vs str:** Same immutability applies to `bytes`. Use `bytearray` for mutable binary data.

---

### Q18: try / except / else / finally — execution order?

**Complete flow:**

```python
def demo(mode):
    try:
        print("1. try block")
        if mode == "error":
            raise ValueError("Something went wrong")
        print("2. try completed")
    except ValueError as e:
        print(f"3. except block: {e}")
    else:
        print("4. else block — runs ONLY if no exception")
    finally:
        print("5. finally block — ALWAYS runs")

demo("ok")      # 1, 2, 4, 5
demo("error")   # 1, 3, 5 (else skipped)
```

**Exception hierarchy:**
```
BaseException
├── SystemExit, KeyboardInterrupt
└── Exception
    ├── ValueError, TypeError, KeyError
    ├── IOError, FileNotFoundError
    └── Custom exceptions
```

**Best practices:**
```python
# GOOD — catch specific exceptions
try:
    value = int(user_input)
except ValueError:
    print("Invalid number")

# BAD — bare except catches everything
try:
    risky()
except:              # catches KeyboardInterrupt too!
    pass             # silently swallows errors

# GOOD — exception chaining
try:
    result = 1 / 0
except ZeroDivisionError as e:
    raise RuntimeError("Calculation failed") from e
```

**else block use case:**
```python
try:
    data = json.loads(text)
except json.JSONDecodeError:
    handle_bad_json()
else:
    process(data)  # only runs if JSON was valid
```

---

### Q19: logging vs print — when to use which?

**Detailed comparison:**

| Feature | print() | logging |
|---------|---------|---------|
| Output levels | No | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| Turn off in production | Hard | Set level to WARNING |
| Output to file | Manual | Built-in handlers |
| Timestamp | Manual | Automatic |
| Module name | No | Yes |
| Log rotation | No | RotatingFileHandler |
| Thread safe | No | Yes |

**logging setup (production standard):**
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),                    # console
        logging.FileHandler("app.log"),             # file
    ]
)

logger = logging.getLogger(__name__)

logger.debug("Detailed debug info")       # hidden if level=INFO
logger.info("User logged in: alice")      # shown
logger.warning("Disk space low: 10%")    # shown
logger.error("Payment failed: timeout")  # shown
logger.critical("Database unreachable")  # shown
```

**Log levels usage:**
- **DEBUG** — diagnostic info for developers
- **INFO** — normal operations (user login, request handled)
- **WARNING** — unexpected but handled (deprecated API, retry)
- **ERROR** — serious problem (failed transaction)
- **CRITICAL** — system failure (DB down, out of memory)

**Rule:** Never use `print()` in production code. Use `logging`.

---

### Q20: Generator vs list?

**Detailed comparison:**

| | List | Generator |
|-|------|-----------|
| Syntax | `[x**2 for x in range(n)]` | `(x**2 for x in range(n))` |
| Memory | O(n) — stores all | O(1) — one item at a time |
| Speed (create) | Slower for large n | Instant |
| Speed (access) | O(1) random access | Sequential only |
| Reusable | Yes, many times | No — one iteration only |
| Use case | Small data, need indexing | Large/infinite data streams |

```python
import sys

# Memory comparison
lst = [x**2 for x in range(1_000_000)]
gen = (x**2 for x in range(1_000_000))
print(sys.getsizeof(lst))  # ~8 MB
print(sys.getsizeof(gen))  # ~200 bytes

# Generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

**Real-world generator use:**
```python
# Process 10GB file without loading into memory
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("huge.log"):
    if "ERROR" in line:
        handle_error(line)
```

**Infinite generator:**
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])  # first 10 Fibonacci numbers
```

---

### Q21: `yield` vs `return`?

**Detailed comparison:**

```python
# return — ends function completely
def with_return():
    return 1
    return 2  # never reached

print(with_return())  # 1

# yield — pauses function, returns value, keeps state
def with_yield():
    yield 1
    yield 2
    yield 3

gen = with_yield()
print(next(gen))  # 1 — function paused after first yield
print(next(gen))  # 2 — resumes from where it paused
print(next(gen))  # 3
# next(gen)       # StopIteration — generator exhausted
```

**What yield preserves:**
```python
def stateful():
    print("Start")
    x = yield 1      # pauses here, returns 1
    print(f"Got: {x}")  # x = value sent via gen.send()
    yield 2

gen = stateful()
print(next(gen))      # Start, then 1
print(gen.send(99))   # Got: 99, then 2
```

**yield from (delegate to sub-generator):**
```python
def chain():
    yield from range(3)
    yield from ["a", "b"]

print(list(chain()))  # [0, 1, 2, 'a', 'b']
```

**When to use yield:**
- Large datasets (memory efficiency)
- Infinite sequences
- Pipelines (producer-consumer pattern)
- Coroutines (before async/await)

---

### Q22: What is the context manager protocol?

**Short answer:** Object with `__enter__()` and `__exit__()` methods, used by `with` statement for guaranteed setup/cleanup.

**Manual protocol:**
```python
class DatabaseConnection:
    def __enter__(self):
        print("Opening connection...")
        self.conn = create_connection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")
        self.conn.close()
        return False  # don't suppress exceptions

with DatabaseConnection() as conn:
    conn.execute("SELECT * FROM users")
# Connection always closed, even if exception occurs
```

**Built-in context managers:**
```python
with open("file.txt", "w") as f:    # file auto-closed
    f.write("hello")

import threading
lock = threading.Lock()
with lock:                           # lock auto-released
    shared_resource += 1
```

**@contextmanager (simpler):**
```python
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    start = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter()-start:.4f}s")

with timer("Processing"):
    process_data()
```

**__exit__ parameters:**
- `exc_type` — exception class (None if no exception)
- `exc_val` — exception instance
- `exc_tb` — traceback
- Return `True` to suppress exception, `False` to propagate.

---

### Q23: Are type hints enforced at runtime?

**Short answer:** No. Type hints are for static analysis tools and documentation only.

**Detailed explanation:**

```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"

# All of these RUN without error at runtime:
greet("Alice", 30)       # correct
greet(123, "thirty")     # wrong types — runs fine!
greet(None, [1, 2])      # completely wrong — still runs!
```

**Static checking with mypy:**
```bash
pip install mypy
mypy myfile.py  # catches type errors BEFORE runtime
```

**Common type hints:**
```python
from typing import Optional, Union, List, Dict, Callable

def process(
    name: str,
    age: int,
    tags: list[str],                    # list of strings
    config: dict[str, bool],            # dict with str keys, bool values
    callback: Callable[[int], str],     # function taking int, returning str
    email: Optional[str] = None,        # str or None
    status: Union[int, str] = 0,        # int or str (use int | str in 3.10+)
) -> bool:
    return True
```

**Python 3.10+ modern syntax:**
```python
def find_user(user_id: int) -> dict[str, str | int] | None:
    ...

def handle(value: int | float) -> str:
    ...
```

**Runtime validation (if needed):** Use `pydantic`, `beartype`, or manual checks — not built into Python.

---

### Q24: What is the GIL (Global Interpreter Lock)?

**Short answer:** A mutex in CPython that allows only one thread to execute Python bytecode at a time.

**Detailed explanation:**

**Why GIL exists:**
- Protects Python's memory management (reference counting) from race conditions.
- Simplifies CPython implementation.
- Makes C extensions easier to write.

**Impact on performance:**
```python
# CPU-bound with threads — NO speedup (GIL blocks parallelism)
import threading

def cpu_task():
    total = sum(i*i for i in range(10_000_000))

threads = [threading.Thread(target=cpu_task) for _ in range(4)]
# 4 threads run sequentially due to GIL — not 4x faster

# I/O-bound with threads — WORKS (GIL released during I/O wait)
def io_task():
    response = requests.get("https://api.example.com")  # GIL released while waiting
```

**Decision guide:**
| Task type | Best approach | Why |
|-----------|---------------|-----|
| I/O-bound (network, disk) | `threading` or `asyncio` | GIL released during I/O wait |
| CPU-bound (computation) | `multiprocessing` | Separate processes, separate GILs |
| Many concurrent connections | `asyncio` | Single thread, event loop |

**GIL release situations:**
- I/O operations (file, network, sleep)
- NumPy/C extension computations (some release GIL)
- `time.sleep()`

**Interview follow-up:** PyPy, Jython don't have GIL. CPython 3.13+ has experimental no-GIL mode (PEP 703).

---

### Q25: Thread vs process vs asyncio?

**Detailed comparison:**

| | Thread | Process | asyncio |
|-|--------|---------|---------|
| Memory | Shared | Separate | Shared (single thread) |
| Creation cost | Low | High | Very low |
| Communication | Shared memory | Queue, Pipe | await/async |
| Parallelism | GIL limited | True CPU parallel | Cooperative |
| Best for | I/O-bound | CPU-bound | Many I/O connections |
| Debugging | Hard (race conditions) | Medium | Easier (single thread) |

**Threading example:**
```python
import threading
from concurrent.futures import ThreadPoolExecutor

def fetch_url(url):
    # I/O wait — GIL released
    return requests.get(url).text

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_url, urls))
```

**Multiprocessing example:**
```python
from multiprocessing import Pool

def compute(n):
    return sum(i*i for i in range(n))

with Pool(4) as pool:
    results = pool.map(compute, [10_000_000]*4)  # uses 4 CPU cores
```

**Asyncio example:**
```python
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

asyncio.run(main())
```

**When to choose:**
- **1000 API calls** → asyncio
- **Image processing** → multiprocessing
- **Reading 5 files simultaneously** → threading
- **Web server (FastAPI/uvicorn)** → asyncio

---

### Q26: Unit test vs integration test?

**Unit test** — tests ONE unit (function/class) in complete isolation.
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

**Integration test** — tests multiple components working together.
```python
def test_user_registration_flow():
    # Uses real/test database
    user = create_user("alice@example.com")
    token = login(user.email, "password")
    profile = get_profile(token)
    assert profile["email"] == "alice@example.com"
```

**Comparison:**

| | Unit Test | Integration Test |
|-|-----------|-----------------|
| Scope | Single function | Multiple components |
| Speed | Fast (ms) | Slower (seconds) |
| Dependencies | Mocked | Real (or test DB) |
| Catches | Logic bugs | Interface/config bugs |
| When run | Every commit | Before deploy |

**Testing pyramid:**
```
        /  E2E Tests  \        ← few, slow
       / Integration   \
      /   Unit Tests     \     ← many, fast
```

**pytest example:**
```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

### Q27: What is mock/patch used for in testing?

**Short answer:** Replace real dependencies with controlled fakes for isolated, fast, reliable tests.

**Why mock:**
- Don't hit real API/database in tests.
- Control return values and errors.
- Tests run fast and offline.
- Test error paths (API timeout, DB failure).

**unittest.mock examples:**
```python
from unittest.mock import Mock, patch, MagicMock

# Mock object
mock_api = Mock()
mock_api.get_user.return_value = {"name": "Alice", "id": 1}
result = mock_api.get_user(1)
assert result["name"] == "Alice"
mock_api.get_user.assert_called_once_with(1)

# Patch external dependency
@patch("myapp.requests.get")
def test_fetch_user(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"name": "Bob"}

    user = fetch_user(42)
    assert user["name"] == "Bob"
    mock_get.assert_called_with("https://api.example.com/users/42")

# Patch with side effects
@patch("myapp.random.randint")
def test_dice_roll(mock_randint):
    mock_randint.return_value = 6
    assert roll_dice() == 6

# Simulate exceptions
mock_db.connect.side_effect = ConnectionError("DB down")
with pytest.raises(ServiceUnavailable):
    get_users()
```

**What to mock:** External APIs, databases, file system, time, random, email services.  
**What NOT to mock:** The function you're actually testing.

---

### Q28: What is `__slots__`?

**Short answer:** Declares fixed instance attributes — saves memory and speeds attribute access by eliminating `__dict__`.

**Without slots:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Each instance has __dict__ — ~48 bytes overhead per object

p = Point(1, 2)
p.z = 3  # can add any attribute dynamically
```

**With slots:**
```python
class Point:
    __slots__ = ("x", "y")  # ONLY x and y allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
# p.z = 3  # AttributeError — no __dict__ to store extra attrs
```

**Memory savings:**
```python
import sys
class Regular: pass
class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y

print(sys.getsizeof(Regular()))   # ~48 bytes (empty __dict__)
print(sys.getsizeof(Slotted(1,2))) # ~32 bytes
# For 1 million objects: ~16 MB saved
```

**Trade-offs:**
- ✅ Less memory, faster attribute access
- ❌ Cannot add attributes dynamically
- ❌ Cannot use `__dict__`-based tools (some serialization libraries)
- ❌ Multiple inheritance limitations

**When to use:** Classes with millions of instances (ORM models, data points, game entities).

---

### Q29: Dataclass vs regular class?

**Regular class (verbose):**
```python
class User:
    def __init__(self, name: str, age: int, email: str = ""):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age}, email={self.email!r})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return (self.name, self.age, self.email) == (other.name, other.age, other.email)
```

**Dataclass (same result, less code):**
```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    email: str = ""
    tags: list[str] = field(default_factory=list)  # mutable default fix

user = User("Alice", 30)
print(user)  # User(name='Alice', age=30, email='', tags=[])
```

**Dataclass features:**
```python
@dataclass(frozen=True)     # immutable instances
@dataclass(order=True)      # auto __lt__, __gt__ for sorting
@dataclass
class Product:
    price: float
    def __post_init__(self):           # validation after __init__
        if self.price < 0:
            raise ValueError("Invalid price")
```

**When to use dataclass:** Data-holding objects (DTOs, config, API responses).  
**When to use regular class:** Complex behavior, custom inheritance, frameworks.

---

### Q30: How does Python manage memory?

**Two mechanisms work together:**

**1. Reference Counting (primary)**
```python
import sys

x = [1, 2, 3]    # refcount = 1
y = x             # refcount = 2
print(sys.getrefcount(x) - 1)  # 2 (subtract 1 for getrefcount arg)

del y             # refcount = 1
del x             # refcount = 0 → memory freed immediately
```

Every object tracks how many references point to it. When count hits zero, memory is deallocated instantly.

**2. Garbage Collector (for circular references)**
```python
import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a  # circular reference — refcount never hits 0

del a, b
gc.collect()  # GC detects and cleans circular references
```

**Memory management summary:**
```
Object created → refcount = 1
New reference  → refcount += 1
del reference  → refcount -= 1
refcount = 0   → memory freed immediately
Circular refs  → garbage collector handles periodically
```

**Memory optimization tips:**
```python
# Use __slots__ for many small objects
# Use generators instead of lists for large data
# Delete large objects explicitly: del big_list
# Use weakref for caches that shouldn't prevent GC
import weakref
cache = weakref.WeakValueDictionary()
```

**Interview follow-up:** Python does NOT have manual memory management (no `malloc`/`free`). Developer doesn't allocate/deallocate — reference counting + GC handle it automatically.

---

## Essential Coding Patterns

```python
# Two Sum — O(n)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

# Valid Palindrome
def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# FizzBuzz
for i in range(1, 101):
    print("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)

# Flatten nested list
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

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

# LRU Fibonacci
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

# Group anagrams
from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    return list(groups.values())
```

---

## Study Plan

| Week | Focus | Action |
|------|-------|--------|
| 1 | Q1–Q10 | Fundamentals + data structures |
| 2 | Q11–Q20 | Functions, OOP, strings, generators |
| 3 | Q21–Q30 | Advanced, concurrency, memory |
| 4 | All 30 | Mock interview — answer without looking |
| 5–8 | Module INTERVIEW.md files | Deep dive per module |

## Mock Interview Tips

1. **Clarify** — ask about input size, edge cases, return type
2. **Think aloud** — explain approach before coding
3. **Start simple** — brute force first, then optimize with Big-O
4. **Test** — walk through example + mention edge cases
5. **Know trade-offs** — always explain why you chose your approach
