# Fundamentals

```bash
python3 01-fundamentals/01_hello_world.py
```

## Examples

- `01_hello_world.py`
- `02_variables_and_types.py`
- `03_operators.py`
- `04_input_output.py`
- `05_truthiness_and_identity.py`
- `06_bytes_and_encoding.py`

→ [02-control-flow](../02-control-flow/)


---

## Interview Prep

### Must-Know Concepts

- Dynamic typing vs static typing
- Mutable vs immutable types
- `==` vs `is` — value equality vs object identity
- Truthy/falsy values
- `int`, `float`, `str`, `bool`, `None`, `bytes`

### Top Interview Questions

**Q1: Is Python interpreted or compiled?**  
A: Both. Source → bytecode (`.pyc`) → Python Virtual Machine (PVM). "Interpreted" refers to runtime execution of bytecode, not direct machine-code compilation.

**Q2: Difference between `==` and `is`?**  
A: `==` compares values. `is` checks if two variables reference the same object in memory. Use `is` only for `None`, `True`, `False` singletons.

**Q3: What are falsy values in Python?**  
A: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`, `range(0)`, custom objects with `__bool__` or `__len__` returning 0/False.

**Q4: What is `None`?**  
A: Singleton object representing absence of value. Type is `NoneType`. Always check with `is None`.

**Q5: Difference between `str` and `bytes`?**  
A: `str` is Unicode text. `bytes` is raw binary data. Encode str→bytes, decode bytes→str.

### Coding Questions

**Q6: Swap two variables without temp variable**
```python
a, b = b, a
```

**Q7: Check if a number is even**
```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

**Q8: Convert "123" to int safely**
```python
def safe_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None
```

### Common Pitfalls

- Using `is` to compare strings or integers (except small cached ints)
- Mutating a default argument (covered in Module 04)
- Forgetting `int("3.14")` raises ValueError — use `float()` first
