# Data Structures

```bash
python3 03-data-structures/01_lists.py
```

## Examples

- `01_lists.py`
- `02_tuples.py`
- `03_sets.py`
- `04_dictionaries.py`
- `05_copy_shallow_deep.py`

→ [04-functions](../04-functions/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [04_Functions](../04_functions/)


---

## Interview Prep

### Must-Know Concepts

- list
- tuple
- set
- dict
- shallow vs deep copy
- time complexity of operations

### Theory Questions

**Q1: List vs Tuple?**  
A: List: mutable. Tuple: immutable, hashable if elements hashable, used for fixed records.

**Q2: Set vs List for membership?**  
A: Set: O(1) lookup. List: O(n). Use set for frequent 'in' checks.

**Q3: Dict insertion order?**  
A: Guaranteed since Python 3.7.

**Q4: Shallow vs deep copy?**  
A: Shallow: new container, same inner objects. Deep: recursive copy of all nested objects.

### Coding Questions

**Two Sum**
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target-n], i]
        seen[n] = i
```

**Remove duplicates preserving order**
```python
unique = list(dict.fromkeys(items))
```

### Common Pitfalls

- Using list as dict key (unhashable)
- Modifying list while iterating
- defaultdict vs dict.get confusion

