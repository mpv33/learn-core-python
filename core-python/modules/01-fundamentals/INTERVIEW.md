# Module 01 — Interview Prep: Fundamentals

> Setup, syntax, types, operators, I/O, control flow

---

## Theory Questions

**Q1: Is Python interpreted or compiled?**  
Both. Source → bytecode (`.pyc`) → PVM executes bytecode. "Interpreted" means no ahead-of-time machine code compilation.

**Q2: Difference between `==` and `is`?**  
`==` compares **values**. `is` compares **object identity** (same memory address). Use `is` only for `None`, `True`, `False`.

**Q3: List all falsy values.**  
`None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`, `range(0)`. Custom objects with `__bool__` or `__len__` returning False/0.

**Q4: Mutable vs immutable types?**  
Mutable: list, dict, set, bytearray. Immutable: int, float, str, tuple, frozenset, bytes. Immutable objects are hashable (if contents hashable).

**Q5: What is dynamic typing?**  
Variable types are determined at runtime. No need to declare type before assignment. Same variable can be reassigned to different types.

**Q6: Why use virtual environments?**  
Isolate project dependencies. Avoid version conflicts between projects. Standard in all professional Python work.

**Q7: `python` vs `python3`?**  
On macOS/Linux, `python3` explicitly runs Python 3. Inside a venv, `python` points to the venv interpreter.

**Q8: What is `None`?**  
Singleton representing absence of value. Type: `NoneType`. Always check with `is None`, never `== None`.

**Q9: Difference between `str` and `bytes`?**  
`str` = Unicode text. `bytes` = raw binary. Encode: `str → bytes`. Decode: `bytes → str`.

**Q10: What is the walrus operator `:=`?**  
Assigns and returns value in one expression (Python 3.8+). Example: `if (n := len(data)) > 10:`

**Q11: `break` vs `continue` vs `pass`?**  
`break` exits loop. `continue` skips to next iteration. `pass` is a no-op placeholder.

**Q12: When use `for` vs `while`?**  
`for` when iterating a known sequence. `while` when iterations depend on a condition.

**Q13: What is `match/case`?**  
Structural pattern matching (Python 3.10+). Cleaner alternative to long if/elif chains.

**Q14: Integer caching in Python?**  
Small integers (-5 to 256) may be cached. `256 is 256` often True; `257 is 257` may be False.

**Q15: What is PEP 8?**  
Python style guide: snake_case functions, PascalCase classes, 4-space indent, max line length ~79-88.

**Q16: What is `__name__ == "__main__"`?**  
Code runs only when file is executed directly, not when imported.

**Q17: Short-circuit evaluation?**  
`and`/`or` stop evaluating once result is determined. `False and expensive()` never calls `expensive()`.

**Q18: Difference between `/` and `//`?**  
`/` true division (float). `//` floor division (truncates toward negative infinity).

**Q19: What is a docstring?**  
Triple-quoted string at top of module/function/class. Access via `.__doc__`. Used for documentation.

**Q20: What is `pip freeze`?**  
Outputs installed packages with versions. Used to create `requirements.txt`.

---

## Coding Questions

**Q21: Swap two variables without temp**
```python
a, b = b, a
```

**Q22: Check if number is even**
```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

**Q23: FizzBuzz**
```python
for i in range(1, 101):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)
```

**Q24: Check prime number**
```python
def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
```

**Q25: Safe int conversion**
```python
def safe_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None
```

**Q26: Count vowels in string**
```python
def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")
```

**Q27: Reverse a string**
```python
s[::-1]
```

**Q28: Find max without built-in max()**
```python
def find_max(nums):
    m = nums[0]
    for n in nums[1:]:
        if n > m: m = n
    return m
```

---

## Common Pitfalls

- Using `is` to compare strings or integers
- `== None` instead of `is None`
- Off-by-one errors with `range()`
- Infinite `while` loops without update
- Forgetting Python uses indentation, not braces
- Installing packages globally instead of in venv

---

## Quick Checklist

- [ ] Explain `==` vs `is` with example
- [ ] List all falsy values
- [ ] Explain venv workflow end-to-end
- [ ] Write FizzBuzz from memory
- [ ] Explain match/case with example
