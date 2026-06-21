# Iterators

```bash
python3 10-iterators/01_list_comprehensions.py
```

## Examples

- `01_list_comprehensions.py`
- `02_dict_set_comprehensions.py`
- `03_generators.py`
- `04_iterators_iterables.py`

→ [11-decorators](../11-decorators/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [11_Decorators And Context Managers](../11_decorators_and_context_managers/)


---

## Interview Prep

### Must-Know Concepts

- __iter__/__next__
- yield
- generator expressions
- StopIteration
- itertools

### Theory Questions

**Q1: Generator vs List?**  
A: Generator: lazy, O(1) memory. List: eager, all in memory.

**Q2: yield vs return?**  
A: yield pauses function. return ends it.

**Q3: List comp vs generator expr?**  
A: [x for x in r] = list. (x for x in r) = generator.

### Coding Questions

**Fibonacci generator**
```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

### Common Pitfalls

- Exhausting generator (iterate once only)
- Unreadable nested list comprehensions

